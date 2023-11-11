from backend.config.db import  db, ma, app

class Barbero(db.Model):
    __tablename__ = "tblbarbero"

    id = db.Column(db.Integer, primary_key =True)
    nombre = db.Column(db.String(50))
    especialidad = db.Column(db.String(250))
    imagen_url = db.Column(db.String(255))
    usuario_id = db.Column(db.Integer, db.ForeignKey('tblusuario.id'))
    
    def __init__(self,nombre,especialidad,imagen_url,usuario_id) :
       self.nombre = nombre
       self.especialidad = especialidad
       self.imagen_url = imagen_url
       self.usuario_id = usuario_id
       
with app.app_context():
    db.create_all()

class BarberosSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre','especialidad','imagen_url','usuario_id')