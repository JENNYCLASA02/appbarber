from backend.config.db import  db, ma, app

class Horario(db.Model):
    __tablename__ = "tblhorario"

    id = db.Column(db.Integer, primary_key =True)
    hora_inicio = db.Column(db.Time)
    hora_fin = db.Column(db.Time)
    barbero_id = db.Column(db.Integer, db.ForeignKey('tblbarbero.id'))

    def __init__(self,hora_inicio,hora_fin,barbero_id) :
       self.hora_inicio = hora_inicio
       self.hora_fin = hora_fin
       self.barbero_id = barbero_id

with app.app_context():
    db.create_all()

class HorariosSchema(ma.Schema):
    class Meta:
        fields = ('id','hora_inicio','hora_fin','barbero_id')