from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mi_clave_secreta' #¡Importante!
items=("arroz", "huevos" "cafe")

class MiFormulario(FlaskForm):
    username = StringField('Nombre')
    password=PasswordField('Contraseña')
    submit = SubmitField('Enviar Datos')

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    form = MiFormulario()
    if form.validate_on_submit():
        nombre = form.nombre.data
        return render_template('resultado.html', nombre=nombre)
    return render_template('formulario.html', form=form)

# Página de inicio
@app.route('/')
def index():
    return render_template('index.html')

# Página "Acerca de"
@app.route("/about")
def about():
    return render_template('about.html')

# Ruta dinámica con nombre de usuario
@app.route('/usuario/<nombre>')
def usuario(nombre):
    return render_template('usuario.html', nombre=nombre)

# Ruta con formulario para ingresar nombre
@app.route('/usuarioform/', methods=['GET', 'POST'])
def usuario_form():
    form = MiFormulario()
    if form.validate_on_submit():
        nombre = form.nombre.data
        return render_template('usuario.html', nombre=nombre)

    return render_template('formulario.html', form=form
    class="container">


if __name__ == '__main__':
    app.run(debug=True)