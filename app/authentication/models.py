from app import db, loginManager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash




@loginManager.user_loader
def get_user(user_id):
    return Users.query.filter_by(id=user_id)


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, )
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String, unique=False)

    #INICIAÇÃO DA CLASSE
    def __ini__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    #VERIFICADOR DE SENHA
    def verifyPassword(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User %r>' % self.name
