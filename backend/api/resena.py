from flask import Blueprint, request, jsonify, json
from backend.config.db import db, app, ma
from backend.models.resena import Resena, ResenasSchema

ruta_resenas = Blueprint("ruta_resena", __name__)

resena_schema = ResenasSchema()
resenas_schema = ResenasSchema(many=True)

@ruta_resenas.route('/resenas', methods=['GET'])
def resena():
    resultall = Resena.query.all() #Select * from resena
    resultado_resena= resenas_schema.dump(resultall)
    return jsonify(resultado_resena)

@ruta_resenas.route('/saveresena', methods=['POST'])
def save():
    calificacion = request.json['calificacion']
    comentario = request.json['comentario']
    cita_id = request.json['cita_id']
    new_resena = Resena(calificacion,comentario,cita_id)
    db.session.add(new_resena)
    db.session.commit()    
    return "Los datos han sido guardados con éxito"

@ruta_resenas.route('/updateresena', methods=['PUT'])
def Update():
    id = request.json['id']
    calificacion = request.json['calificacion']
    comentario = request.json['comentario']
    cita_id = request.json['cita_id']
    resena = Resena.query.get(id)   
    if resena :
        print(resena) 
        resena.id = id
        resena.calificacion = calificacion
        resena.comentario = comentario
        resena.cita_id = cita_id
        db.session.commit()
        return "Datos actualizados con éxito"
    else:
        return "Error"

@ruta_resenas.route('/deleteresena/<id>', methods=['DELETE'])
def eliminar(id):
    resena = Resena.query.get(id)
    db.session.delete(resena)
    db.session.commit()
    return jsonify(resena_schema.dump(resena))