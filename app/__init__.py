from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager



#APLICATIVO
app = Flask(__name__)
app.config.from_object('config')

#BANCO DE DADOS
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#LOGIN
loginManager = LoginManager(app)

#ROTAS
from app.authentication import routes
from app.home import routes