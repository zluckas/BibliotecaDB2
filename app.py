from flask import Flask, render_template, request, redirect, url_for, flash, session, make_response
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash 

app = Flask(__name__)
app.secret_key = 'secret_key_123'



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro')
def cadastro_usuario():
    return render_template('cadastro_usuario.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cadastro_livro')
def cadastro_livro():
    return render_template('cadastro_livro.html')