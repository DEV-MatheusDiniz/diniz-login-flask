from flask import render_template, redirect
from app import app, db
from app.authentication.forms import FormLogin, FormRegister
from app.authentication import validate
from flask_login import login_user, logout_user
from app.authentication.models import Users




#ROTA RAIZ
@app.route("/", methods=['GET', 'POST'])
def index():
    return redirect('login')
    
@app.route("/diniz-login-flask.git", methods=['GET', 'POST'])
def index():
    return redirect('login')


#ROTA LOGIN
@app.route("/login", methods=['GET', 'POST'])
def login():
    formLogin = FormLogin()
    if formLogin.validate_on_submit():
        email = formLogin.email.data
        password = formLogin.password.data

        verifica = validate.verificarLogin(email, password)
        if verifica:
            return redirect('home')
        else:
            vLogin = False
            return render_template("accounts/login.html", form=formLogin, vLogin=vLogin)
    return render_template("accounts/login.html", form=formLogin)


#ROTA REGISTER
@app.route("/register", methods=['GET', 'POST'])
def register():
    formRegister = FormRegister()
    if formRegister.validate_on_submit():
        name = formRegister.name.data
        email = formRegister.email.data
        password1 = formRegister.password1.data
        password2 = formRegister.password2.data

        user = validate.VerificarEmail(email)
        pwd = validate.senhasIguais(password1, password2)
        if user and pwd:
            validate.cadatrarUser(name, email, password1)
            return redirect('home')
        else:
            vEmail = user
            vSenha = pwd
            return render_template('accounts/register.html', form=formRegister, vEmail=vEmail, vSenha=vSenha)
    return render_template('accounts/register.html', form=formRegister)


#ROTA LOGOUT
@app.route('/logout')
def logout():
    logout_user()
    return redirect('login')
