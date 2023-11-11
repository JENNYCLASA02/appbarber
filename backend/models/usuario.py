from backend.config.db import  db, ma, app

class Usuario(db.Model):
    __tablename__ = "tblusuario"

    id = db.Column(db.Integer, primary_key =True)
    nombreusuario = db.Column(db.String(50))
    correo = db.Column(db.String(50))
    contrasena = db.Column(db.String(50))
    celular = db.Column(db.String(50))
    tipousuario = db.Column(db.Boolean)
    
    def __init__(self, nombreusuario, correo, contrasena,celular,tipousuario) :
       self.nombreusuario = nombreusuario
       self.correo = correo
       self.contrasena = contrasena
       self.celular = celular
       self.tipousuario = tipousuario
       
with app.app_context():
    db.create_all()

class UsuariosSchema(ma.Schema):
    class Meta:
        fields = ('id','nombreusuario','correo','contrasena','celular','tipousuario')