from flask import Blueprint, request, jsonify, json
from backend.config.db import db, app, ma
from backend.models.servicio import Servicio, ServiciosSchema

ruta_servicios = Blueprint("ruta_servicio", __name__)

servicio_schema = ServiciosSchema()
servicios_schema = ServiciosSchema(many=True)

@ruta_servicios.route('/servicios', methods=['GET'])
def servicio():
    resultall = Servicio.query.all() #Select * from servicio
    resultado_servicio= servicios_schema.dump(resultall)
    return jsonify(resultado_servicio)

@ruta_servicios.route('/saveservicio', methods=['POST'])
def save():
    nombre = request.json['nombre']
    descripcion = request.json['descripcion']
    imagen_url = request.json['imagen_url']
    precio = request.json['precio']
    duracion = request.json['duracion']
    categoria_id = request.json['categoria_id']
    new_servicio = Servicio(nombre,descripcion,imagen_url,precio,duracion,categoria_id)
    db.session.add(new_servicio)
    db.session.commit()    
    return "Los datos han sido guardados con éxito"

@ruta_servicios.route('/updateservicio', methods=['PUT'])
def Update():
    id = request.json['id']
    nombre = request.json['nombre']
    descripcion = request.json['descripcion']
    imagen_url = request.json['imagen_url']
    precio = request.json['precio']
    duracion = request.json['duracion']
    categoria_id = request.json['categoria_id']
    servicio = Servicio.query.get(id)   
    if servicio :
        print(servicio) 
        servicio.id = id
        servicio.nombre = nombre
        servicio.descripcion = descripcion
        servicio.imagen_url = imagen_url
        servicio.precio = precio
        servicio.duracion = duracion
        servicio.categoria_id = categoria_id
        db.session.commit()
        return "Datos actualizados con éxito"
    else:
        return "Error"

@ruta_servicios.route('/deleteservicio/<id>', methods=['DELETE'])
def eliminar(id):
    servicio = Servicio.query.get(id)
    db.session.delete(servicio)
    db.session.commit()
    return jsonify(servicio_schema.dump(servicio))