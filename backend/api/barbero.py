from flask import Blueprint, request, jsonify, json
from backend.config.db import db, app, ma
from backend.models.barbero import Barbero, BarberosSchema

ruta_barberos = Blueprint("ruta_barbero", __name__)

barbero_schema = BarberosSchema()
barberos_schema = BarberosSchema(many=True)

@ruta_barberos.route('/barberos', methods=['GET'])
def barbero():
    resultall = Barbero.query.all() #Select * from barbero
    resultado_barbero= barberos_schema.dump(resultall)
    return jsonify(resultado_barbero)

@ruta_barberos.route('/savebarbero', methods=['POST'])
def save():
    nombre = request.json['nombre']
    especialidad = request.json['especialidad']
    imagen_url = request.json ['imagen_url']
    usuario_id = request.json ['usuario_id']
    new_barbero = Barbero(nombre,especialidad,imagen_url,usuario_id)
    db.session.add(new_barbero)
    db.session.commit()    
    return "Los datos han sido guardados con éxito"

@ruta_barberos.route('/updatebarbero', methods=['PUT'])
def Update():
    id = request.json['id']
    nombre = request.json['nombre']
    especialidad = request.json['especialidad']
    imagen_url = request.json ['imagen_url']
    usuario_id = request.json ['usuario_id']
    barbero = Barbero.query.get(id)   
    if barbero :
        print(barbero) 
        barbero.nombre = nombre
        barbero.especialidad = especialidad
        barbero.imagen_url = imagen_url
        barbero.usuario_id = usuario_id
        db.session.commit()
        return "Datos actualizados con éxito"
    else:
        return "Error"

@ruta_barberos.route('/deletebarbero/<id>', methods=['DELETE'])
def eliminar(id):
    barbero = Barbero.query.get(id)
    db.session.delete(barbero)
    db.session.commit()
    return jsonify(barbero_schema.dump(barbero))