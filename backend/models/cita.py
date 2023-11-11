from backend.config.db import  db, ma, app

class Cita(db.Model):
    __tablename__ = "tblcita"

    id = db.Column(db.Integer, primary_key =True)
    fecha = db.Column(db.Date)
    hora = db.Column(db.Time)
    estado = db.Colum(db.Boolean)
    usuario_id = db.Column(db.Integer, db.ForeignKey('tblusuario.id'))
    barbero_id = db.Column(db.Integer, db.ForeignKey('tblbarbero.id'))
    horario_id = db.Column(db.Integer, db.ForeignKey('tblhorario.id'))
    servicio_id = db.Column(db.Integer, db.ForeignKey('tblservicio.id'))

    def __init__(self,fecha,hora,estado,usuario_id,barbero_id,horario_id,servicio_id) :
       self.fecha = fecha
       self.hora = hora
       self.estado = estado
       self.usuario_id = usuario_id
       self.barbero_id = barbero_id
       self.horario_id = horario_id
       self.servicio_id = servicio_id


with app.app_context():
    db.create_all()

class CitasSchema(ma.Schema):
    class Meta:
        fields = ('id','fecha','hora','estado','usuario_id','barbero_id','horario_id','servicio_id')