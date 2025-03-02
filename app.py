from flask import Flask, render_template, redirect , url_for, request, flash
from flask_bootstraps import Bootstraps
from flask_wtf import Flaskform
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta'

class MiFormulario(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Enviar')
app = Flask(__name__)

# Página de inicio
@app.route('/')
def index():
    return render_template('index.html')

# Página "Acerca de"
@app.route('/about')
def about():
    return render_template('about.html')

# Ruta dinámica con nombre de usuario
@app.route('/usuario/<nombre>')
def usuario(nombre):
    return render_template('usuario.html', nombre=nombre)

# Ruta con formulario para ingresar nombre
@app.route('/usuario/', methods=['GET', 'POST'])
def usuario_form():
    if request.method == 'POST':
        nombre = request.form['nombre']
        return render_template('usuario.html', nombre=nombre)
    return render_template('formulario.html')

if __name__ == '__main__':
    app.run(debug=True)