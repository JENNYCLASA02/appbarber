from flask import Blueprint, request, jsonify, json
from backend.config.db import db, app, ma
from backend.models.barberoservicio import Barberoservicio, BarberoserviciosSchema

ruta_barberoservicios = Blueprint("ruta_barberoservicio", __name__)

barberoservicio_schema = BarberoserviciosSchema()
barberoservicios_schema = BarberoserviciosSchema(many=True)

@ruta_barberoservicios.route('/barberoservicios', methods=['GET'])
def barberoservicio():
    resultall = Barberoservicio.query.all() #Select * from barberoservicio
    resultado_barberoservicio= barberoservicios_schema.dump(resultall)
    return jsonify(resultado_barberoservicio)

@ruta_barberoservicios.route('/savebarberoservicio', methods=['POST'])
def save():
    servicio_id = request.json['servicio_id']
    barbero_id = request.json['barbero_id']
    new_barberoservicio = Barberoservicio(servicio_id,barbero_id)
    db.session.add(new_barberoservicio)
    db.session.commit()    
    return "Los datos han sido guardados con éxito"

@ruta_barberoservicios.route('/updatebarberoservicio', methods=['PUT'])
def Update():
    id = request.json['id']
    servicio_id = request.json['servicio_id']
    barbero_id = request.json['barbero_id']
    barberoservicio = Barberoservicio.query.get(id)   
    if barberoservicio :
        print(barberoservicio) 
        barberoservicio.servicio_id = servicio_id
        barberoservicio.barbero_id = barbero_id
        db.session.commit()
        return "Datos actualizados con éxito"
    else:
        return "Error"

@ruta_barberoservicios.route('/deletebarberoservicio/<id>', methods=['DELETE'])
def eliminar(id):
    barberoservicio = Barberoservicio.query.get(id)
    db.session.delete(barberoservicio)
    db.session.commit()
    return jsonify(barberoservicio_schema.dump(barberoservicio))