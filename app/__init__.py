# -*- coding: utf-8 -*-
from .decorators import sqlexception_handler
from .modeldb import Users, Roles, start_db, db

from flask import (
    Flask, redirect, render_template, request, url_for, make_response
)

app = Flask(__name__)
app.config.from_pyfile('../config.py')
app.config.from_object('config.Config')  # Using configuration
db.init_app(app)


"""
Durante el estado de desarrollo.
Cabecera adicional para forzar la recarga de la cache.
"""
@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


@app.route('/')
def index():
    return render_template('front/portada.html')


@app.route(r'/acceso')
def login():
    return render_template('dashboard/login.html')


@app.route('/registrarse', methods=['GET', 'POST'])
def registro():
    if request.method == 'GET':
        return render_template('dashboard/signup.html')
    elif request.method == 'POST':
        cc = request.form.get("cc")
        nombre = request.form.get("nombre")
        apellido = request.form.get("apellido")
        email = request.form.get("email")
        password = request.form.get("password")
        new_user = Users()
        new_user.add_user(cc, nombre, apellido, email, password)
        return "hola" #redirect(url_for('dashboard'))

# Users.query.filter_by(id=123).delete()
# Users.query.filter(User.id == 123).delete()
# users = Users.query.all()

@app.route('/recuperarclave')
def forgot():
    return render_template('dashboard/forgot.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard/dashboard.html')


@sqlexception_handler
@app.route('/db_init')
def check_db_status():
    start_db()
    nr = Roles()
    nr.init_roles()
    return "Todo correcto "


@app.route('/testrule')
def testrule():
    response = make_response("Hola")
    response.set_cookie('answer', '42')
    return response



if __name__ == '__main__':
    app.run()
