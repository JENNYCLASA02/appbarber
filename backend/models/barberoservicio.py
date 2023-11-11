from backend.config.db import  db, ma, app

class Barberoservicio(db.Model):
    __tablename__ = "tblfavorito"

    id = db.Column(db.Integer, primary_key =True)
    servicio_id = db.Column(db.Integer, db.ForeignKey('tblservicio.id'))
    barbero_id = db.Column(db.Integer, db.ForeignKey('tblbarbero.id'))
    
    def __init__(self,servicio_id,barbero_id) :
       self.servicio_id = servicio_id
       self.barbero_id = barbero_id
       
with app.app_context():
    db.create_all()

class BarberoserviciosSchema(ma.Schema):
    class Meta:
        fields = ('id','servicio_id','barbero_id')