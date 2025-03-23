from flask_login import UserMixin


class usuario(UserMixin):
    def __init__(self, id_usuario, nombre, email, password):
        self.id = id_usuario
        self.nombre = nombre
        self.email = email
        self.password = password

    def obtener_usuario_por_email(email):
        conexion = obtener_conexion()
        cursor=conexion.cursor(directionary=true)
        cursor.execute("SELECT * FROM usuarios WHERE email = %s AND password = %s", (email,))
        user_data = cursor.fetchone()
        cursor.close()
        conexion.close()
        if user_data:
            user = User(user_data['id_usuario'], user_data['nombre'], user_data['email'], user_data['password'])
            login_user(user)
            return redirect(url_for('protegido'))
        else:
            return 'Credenciales inválidas'

    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('inicio'))


@app.route('/protegido')
@login_required
def protegido():
    return 'Esta es una ruta protegida'