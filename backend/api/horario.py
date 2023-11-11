from flask import Blueprint, request, jsonify, json
from backend.config.db import db, app, ma
from backend.models.horario import Horario, HorariosSchema

ruta_horarios = Blueprint("ruta_horario", __name__)

horario_schema = HorariosSchema()
horarios_schema = HorariosSchema(many=True)

@ruta_horarios.route('/horarios', methods=['GET'])
def horario():
    resultall = Horario.query.all() #Select * from horario
    resultado_horario= horarios_schema.dump(resultall)
    return jsonify(resultado_horario)

@ruta_horarios.route('/savehorario', methods=['POST'])
def save():
    hora_inicio = request.json['hora_inicio']
    hora_fin = request.json['hora_fin']
    barbero_id = request.json['barbero_id']
    new_horario = Horario(hora_inicio,hora_fin,barbero_id)
    db.session.add(new_horario)
    db.session.commit()    
    return "Los datos han sido guardados con éxito"

@ruta_horarios.route('/updatehorario', methods=['PUT'])
def Update():
    id = request.json['id']
    hora_inicio = request.json['hora_inicio']
    hora_fin = request.json['hora_fin']
    barbero_id = request.json['barbero_id']
    horario = Horario.query.get(id)   
    if horario :
        print(horario) 
        horario.id = id
        horario.hora_inicio = hora_inicio
        horario.hora_fin = hora_fin
        horario.barbero_id = barbero_id
        db.session.commit()
        return "Datos actualizados con éxito"
    else:
        return "Error"

@ruta_horarios.route('/deletehorario/<id>', methods=['DELETE'])
def eliminar(id):
    horario = Horario.query.get(id)
    db.session.delete(horario)
    db.session.commit()
    return jsonify(horario_schema.dump(horario))