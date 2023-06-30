from flask import render_template, request, flash, url_for, redirect
from sistemaEdectech import app, bcrypt, db
from sistemaEdectech.forms import FormCriarConta, FormLogin
from flask_login import login_required, login_user, logout_user
from sistemaEdectech.models import User


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    if form_login.validate_on_submit() and 'botao_login' in request.form:
        usuario = User.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario, remember=form_login.lembrar_dados.data)
            flash('Login feito com Sucesso', 'alert-success')
            par_next = request.args.get('next')
            if par_next:
                return redirect(par_next)
            else:
                return redirect(url_for('perfil'))
        else:
            flash('falha no login, Email ou senha errado', 'alert-danger')
    return render_template('login.html', form_login=form_login)


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form_criarconta = FormCriarConta()
    if form_criarconta.validate_on_submit() and 'botao_criarconta' in request.form:
        senha_cript = bcrypt.generate_password_hash(form_criarconta.senha.data)
        usuario = User(nome=form_criarconta.username.data, email=form_criarconta.email.data, senha=senha_cript)
        db.session.add(usuario)
        db.session.commit()
        flash('Conta Criada com Sucesso', 'alert-success')
        return redirect(url_for('perfil'))
    return render_template('cadastro.html', form_criarconta=form_criarconta)


""""@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()
    if form_login.validate_on_submit() and 'botao_login' in request.form:
        usuario = User.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario, remember=form_login.lembrar_dados.data)
            flash(f'Login feito com Sucesso', 'alert-success')
            par_next = request.args.get('next')
            if par_next:
                return redirect(par_next)
            else:
                return redirect(url_for('perfil'))
        else:
            flash(f'Falha no Login, E-mail ou senha incorreta', 'alert-danger')
    if form_criarconta.validate_on_submit() and 'botao_criarconta' in request.form:
        senha_cript = bcrypt.generate_password_hash(form_criarconta.senha.data)
        usuario = User(nome=form_criarconta.username.data, email=form_criarconta.email.data, senha=senha_cript)
        db.session.add(usuario)
        db.session.commit()
        flash(f'Conta Criada com Sucesso', 'alert-success')
        return redirect(url_for('perfil'))
    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)
"""


@app.route('/sair')
@login_required
def sair():
    logout_user()
    flash(f'Logout Feito com Sucesso', 'alert-success')
    return redirect(url_for('home'))


@app.route('/Perfil')
@login_required
def perfil():
    return render_template('perfil.html')


@app.route('/usuarios')
@login_required
def usuarios():
    usuario = User.query.order_by(User.id.desc())
    return render_template('usuarios.html', usuario=usuario)


@app.route('/carreiras')
def carreiras():
    return render_template('carreiras.html')


@app.route('/desenvolvedores')
def desenvolvedores():
    return render_template('desenvolvedores.html')

