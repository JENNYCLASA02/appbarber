from flask import Blueprint, request, jsonify, json
from backend.config.db import db, app, ma
from backend.models.categoria import Categoria, CategoriasSchema

ruta_categorias = Blueprint("ruta_categoria", __name__)

categoria_schema = CategoriasSchema()
categorias_schema = CategoriasSchema(many=True)

@ruta_categorias.route('/categorias', methods=['GET'])
def categoria():
    resultall = Categoria.query.all() #Select * from Categorias
    resultado_categoria= categorias_schema.dump(resultall)
    return jsonify(resultado_categoria)

@ruta_categorias.route('/savecategoria', methods=['POST'])
def save():
    nombre = request.json['nombre']
    imagen_url = request.json['imagen_url'] 
    new_categoria = Categoria(nombre=nombre, imagen_url=imagen_url)
    db.session.add(new_categoria)
    db.session.commit()
    return "Datos guardados con éxito"

@ruta_categorias.route('/updatecategoria', methods=['PUT'])
def Update():
    id = request.json['id']
    nombre = request.json['nombre']
    imagen_url = request.json['imagen_url'] 
    categoria = Categoria.query.get(id)   
    if categoria :
        print(categoria) 
        categoria.nombre = nombre
        categoria.imagen_url = imagen_url
        db.session.commit()
        return "Datos actualizados con éxito"
    else:
        return "Error"
    
@ruta_categorias.route('/deletecategoria/<id>', methods=['DELETE'])
def eliminar(id):
    categoria = Categoria.query.get(id)
    db.session.delete(categoria)
    db.session.commit()
    return {'message': 'Categoría eliminada con éxito'}, 200