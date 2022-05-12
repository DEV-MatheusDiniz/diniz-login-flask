from app import db
from app.authentication.models import Users
from werkzeug.security import generate_password_hash, check_password_hash


#VERIFICA SE A SENHA É A MESMA CADASTRADA NO BANCO DE DADOS
def verificarLogin(email,password):
    user = Users.query.filter_by(email=email).first()
    if user:
        pwd = user.password
        verifica = check_password_hash(pwd, password)
        if verifica:
            return True
    return False

#VERIFICA SE AS SENHAS INSERIDAS NO CADASTRO SÃO IGUAIS
def senhasIguais(password1,password2):
    if password1 == password2:
        return True
    else:
        return False

#VERIFICA E-MAIL
def VerificarEmail(email):
    verifica = Users.query.filter_by(email=email).first()
    if not verifica:
        return True
    else:
        return False

#CADASTRAR USUARIO NO BANCO
def cadatrarUser(name, email,password):
    password = generate_password_hash(password)
    user = Users(name=name, email=email, password=password)
    db.session.add(user)
    db.session.commit()