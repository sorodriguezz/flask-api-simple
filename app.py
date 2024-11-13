from flask import Flask
from models.usuario import db
from routes.usuario_routes import usuario_bp
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
  app = Flask(__name__)

  app.config.from_object('config.Config')

  db.init_app(app)

  app.register_blueprint(usuario_bp, url_prefix='/usuarios')

  return app

if __name__ == '__main__':
  app = create_app()
  with app.app_context():
    db.create_all()
  app.run(debug=True)
