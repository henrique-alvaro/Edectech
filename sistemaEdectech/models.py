from sistemaEdectech import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def loud_usuario(id_usuario):
    return User.query.get(int(id_usuario))


class User(db.Model, UserMixin):
    __tablename__ = "usuario"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    senha = db.Column(db.String, nullable=False)
    nascimento = db.Column(db.String)
    telefone = db.Column(db.String)
    cpf = db.Column(db.String, unique=True)
    sexo = db.Column(db.String)

