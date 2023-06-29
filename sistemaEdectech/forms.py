from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from sistemaEdectech.models import User


class FormCriarConta(FlaskForm):
    username = StringField('Nome do Usuario: ', validators=[DataRequired()])
    email = StringField('Email do Usuario: ', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha: ', validators=[DataRequired(), Length(5, 20)])
    confirmacao_senha = PasswordField('Confirme sua Senha: ', validators=[DataRequired(), EqualTo('senha')])
    botao_criarconta = SubmitField('Cadastra-Se')

    def validate_email(self, email):
        usuario = User.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('E-mail já cadastrado. Cadastra-se com outro e-mail ou faça login')


class FormLogin(FlaskForm):
    email = StringField('Email do Usuario: ', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha: ', validators=[DataRequired(), Length(5, 20)])
    lembrar_dados = BooleanField('Lembrar Dados de Acesso: ')
    botao_login = SubmitField('Login')
