from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Practica Web'

#Nueva ruta para mostrar un mensaje personalizado
@app.route('/usuario/<nombre>')
def usuario(nombre):
    return  f'Bienvenido, {nombre}!'
#Nueva Ruta
# Ruta para mostrar formulario
@app.route('/usuario', methods=['GET', 'POST'])
def usuario_form():
     if request.method == 'POST':
         nombre = request.form['nombre']
         return f' Bienvenido , {nombre}!'
     return '''
    , <form method="post">
         <label for="nombre">Ingrese tu nombre:</label>
         <input type="text" id="nombre" name="nombre">
         <button type="submit">Enviar </button>
     </form>
     '''
         


if __name__ == '__main__':
    app.run()
