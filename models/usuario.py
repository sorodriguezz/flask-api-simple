from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
  __tablename__ = 'usuarios'

  id = db.Column(db.Integer, primary_key=True)
  nombre = db.Column(db.String(50), nullable=False)
  email = db.Column(db.String(100), unique=True, nullable=False)

  def to_dict(self):
    return {"id": self.id, "nombre": self.nombre, "email": self.email}
