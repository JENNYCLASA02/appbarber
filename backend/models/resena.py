from backend.config.db import  db, ma, app

class Resena(db.Model):
    __tablename__ = "tblresenas"

    id = db.Column(db.Integer, primary_key =True)
    calificacion = db.Column(db.Integer)
    comentario = db.Column(db.String(50))
    cita_id = db.Column(db.Integer, db.ForeignKey('tblcita.id'))

    def __init__(self,calificacion,comentario,cita_id) :
       self.calificacion = calificacion
       self.comentario = comentario
       self.cita_id = cita_id

with app.app_context():
    db.create_all()

class ResenasSchema(ma.Schema):
    class Meta:
        fields = ('id','calificacion','comentario','cita_id')