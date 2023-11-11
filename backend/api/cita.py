from flask import Blueprint, request, jsonify, json
from backend.config.db import db, app, ma
from backend.models.cita import Cita, CitasSchema

ruta_citas = Blueprint("ruta_cita", __name__)

cita_schema = CitasSchema()
citas_schema = CitasSchema(many=True)

@ruta_citas.route('/citas', methods=['GET'])
def cita():
    resultall = Cita.query.all() #Select * from cita
    resultado_cita= citas_schema.dump(resultall)
    return jsonify(resultado_cita)

@ruta_citas.route('/savecita', methods=['POST'])
def save():
    fecha = request.json['fecha']
    hora = request.json['hora']
    estado = request.json['estado']
    usuario_id = request.json['usuario_id']
    barbero_id = request.json['barbero_id']
    horario_id = request.json['horario_id']
    servicio_id = request.json['servicio_id']
    new_cita = Cita(fecha,hora,estado,usuario_id,barbero_id,horario_id,servicio_id)
    db.session.add(new_cita)
    db.session.commit()    
    return "Los datos han sido guardados con éxito"

@ruta_citas.route('/updatecita', methods=['PUT'])
def Update():
    id = request.json['id']
    fecha = request.json['fecha']
    hora = request.json['hora']
    estado = request.json['estado']
    usuario_id = request.json['usuario_id']
    barbero_id = request.json['barbero_id']
    horario_id = request.json['horario_id']
    servicio_id = request.json['servicio_id']
    cita = Cita.query.get(id)   
    if cita :
        print(cita) 
        cita.id = id
        cita.fecha = fecha
        cita.hora = hora
        cita.estado = estado
        cita.usuario_id = usuario_id
        cita.barbero_id = barbero_id
        cita.horario_id = horario_id
        cita.servicio_id = servicio_id
        db.session.commit()
        return "Datos actualizados con éxito"
    else:
        return "Error"

@ruta_citas.route('/deletecita/<id>', methods=['DELETE'])
def eliminar(id):
    cita = Cita.query.get(id)
    db.session.delete(cita)
    db.session.commit()
    return jsonify(cita_schema.dump(cita))