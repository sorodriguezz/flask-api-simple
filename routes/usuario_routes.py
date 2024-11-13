from flask import Blueprint, jsonify, request
from models.usuario import Usuario, db

usuario_bp = Blueprint('usuario_bp', __name__)

@usuario_bp.route('/', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([usuario.to_dict() for usuario in usuarios])

@usuario_bp.route('/<int:id>', methods=['GET'])
def get_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    return jsonify(usuario.to_dict())

@usuario_bp.route('/', methods=['POST'])
def create_usuario():
    data = request.get_json()
    nuevo_usuario = Usuario(nombre=data['nombre'], email=data['email'])
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify(nuevo_usuario.to_dict()), 201

@usuario_bp.route('/<int:id>', methods=['PUT'])
def update_usuario(id):
    data = request.get_json()
    usuario = Usuario.query.get_or_404(id)
    usuario.nombre = data.get('nombre', usuario.nombre)
    usuario.email = data.get('email', usuario.email)
    db.session.commit()
    return jsonify(usuario.to_dict())

@usuario_bp.route('/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return jsonify({"message": "Usuario eliminado"})