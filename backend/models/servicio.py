from backend.config.db import  db, ma, app

class Servicio(db.Model):
    __tablename__ = "tblservicio"

    id = db.Column(db.Integer, primary_key =True)
    nombre = db.Column(db.String(50))
    descripcion = db.Column(db.String(500))
    imagen_url = db.Column(db.String(255))
    precio = db.Column(db.Double)
    duracion = db.Column(db.String(50))
    categoria_id = db.Column(db.Integer, db.ForeignKey('tblcategoria.id'))

    def __init__(self,nombre,descripcion,imagen_url,precio,duracion,categoria_id) :
       self.nombre = nombre
       self.descripcion = descripcion
       self.imagen_url = imagen_url
       self.precio = precio
       self.duracion = duracion
       self.categoria_id = categoria_id

with app.app_context():
    db.create_all()

class ServiciosSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre','descripcion','imagen_url','precio','duracion','categoria_id')