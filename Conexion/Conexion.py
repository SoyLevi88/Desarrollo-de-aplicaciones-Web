import mysql.connector

def obtener_conexion():
    """Obtiene una conexión a la base de datos MySQL."""
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="tu_contraseña",
            database="desarrollo_web"
        )
        return conexion
    except mysql.connector.Error as error:
        print(f"Error al conectar a MySQL: {error}")
        return None