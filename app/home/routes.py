from flask import render_template
from app import app
from app.authentication.forms import FormLogin, FormRegister


#ROTA HOME
@app.route('/home')
def home():
    return render_template('home/home.html')