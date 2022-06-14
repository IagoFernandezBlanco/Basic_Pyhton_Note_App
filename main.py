"""
Proeycto pythom MYSQL
Un asistente que te permite loguearte/registro
Permite crear notas, una vez registrado
"""
#importar módulo sqlite
import sqlite3

# creación base de datos
conexion = sqlite3.connect("./20-proyecto-python/usuarios.db")

# Crear tablas de usuario y notas
tabla_usuario = conexion.cursor()
tabla_notas = conexion.cursor()

tabla_usuario.execute("""CREATE TABLE IF NOT EXISTS usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre varchar(8),
    contraseña varchar(10)
)""")

tabla_notas.execute("""CREATE TABLE IF NOT EXISTS notas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo varchar(10),
    contenido varchar(120),
    nombre varchar(8)
)""")

accion_usuario = int(input("Que acción quieres realizar \n1.Logueo \n2.Registro \n3.Salir \n"))
while accion_usuario >=1:
    if accion_usuario == 1:
        # Sistema de logueo del proyecto
        print("Logueo")
        confirmar_usuario = input("Introduce tu nombre de usuario: ")
        confirmar_contraseña = input("Introduce tu contraseña: ")
        buscar_usuario_registrado = conexion.cursor()
        buscar_usuario_registrado.execute("SELECT * from usuario WHERE nombre = ? and contraseña = ?", (confirmar_usuario, confirmar_contraseña))
        comprobar_usuario = buscar_usuario_registrado.fetchone()
        while comprobar_usuario == None:
            print("Usuario no existente")
            confirmar_usuario = input("Introduce de nuevo el usuario: ")
            confirmar_contraseña = input("Introduce la contraseña de nuevo: ")
            buscar_usuario_registrado = conexion.cursor()
            buscar_usuario_registrado.execute("SELECT * from usuario WHERE nombre = ? and contraseña = ?", (confirmar_usuario, confirmar_contraseña))
            comprobar_usuario = buscar_usuario_registrado.fetchone()
        
        accion_usuario_registro = int(input("Que acción quieres realizar \n1.Crear notas \n2. Eliminar notas \n3.Modificar \n4.Salir \n"))
        if accion_usuario_registro == 1:
            print("Crear")
        elif accion_usuario_registro == 2:
            print("Eliminar")
        elif accion_usuario_registro == 3:
            print("Modificar")
        else:
            print("opcion no valida")
    
    # Acción de registro finalizada
    elif accion_usuario == 2:
        print("Registro")
        nombre_usuario = input("Introduce tu nombre de usuario: ")
        contraseña = input("Introduce tu contraseña: ")
        cursor_insert_users = conexion.cursor()
        cursor_insert_users.execute("INSERT INTO usuario VALUES (null,?,?)", (nombre_usuario, contraseña))
        conexion.commit()
    elif accion_usuario == 3:
        print("salir")
        break
    else :
        print("Opcion no valida")
        accion_usuario = int(input("introduce una opción válida \n"))

conexion.close()
