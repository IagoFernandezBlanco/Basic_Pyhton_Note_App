"""
Proeycto pythom MYSQL
Un asistente que te permite loguearte/registro
Permite crear notas, una vez registrado
"""

accion_usuario = int(input("Que acción quieres realizar \n1.Logueo \n2.Registro \n3.Salir \n"))
while accion_usuario >=1:
    if accion_usuario == 1:
        print("Logueo")
        
    elif accion_usuario == 2:
        print("Registro")
        accion_usuario_registro = int(input("Que acción quieres realizar \n1.Crear notas \n2. Eliminar notas \n3.Modificar \n4.Salir \n"))
        if accion_usuario_registro == 1:
            print("Crear")
        elif accion_usuario_registro == 2:
            print("Eliminar")
        elif accion_usuario_registro == 3:
            print("Modificar")
        else:
            print("opcion no valida")
    elif accion_usuario == 3:
        print("salir")
        break
    else :
        print("Opcion no valida")
        accion_usuario = int(input("introduce una opción válida \n"))
