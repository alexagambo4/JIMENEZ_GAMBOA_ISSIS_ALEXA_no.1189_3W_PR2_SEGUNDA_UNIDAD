#imprime los datos de la bellisima autora
print("JIMENEZ GAMBOA ISSIS ALEXA")
print("No.1189")
print("3W")
#imprime una linea en blanco para que se vea mas limpiecito el programa 
print("")

#programa no.2: Informacion del usuario
print("Programa no.2: Informacion del usuario")
#imprime una linea en blanco 
print("")
#creamos un diccionario para almacenar la información del usuario
informacion_usuario = {}

#pedimos al usuario que introduzca su nombre, edad, dirección y teléfono
informacion_usuario['nombre'] = input("Introduce tu nombre: ")
informacion_usuario['edad'] = input("Introduce tu edad: ")
informacion_usuario['direccion'] = input("Introduce tu dirección: ")
informacion_usuario['telefono'] = input("Introduce tu número de teléfono: ")

#mostramos la información del usuario en el formato solicitado
print(f"{informacion_usuario['nombre']} "
      f"tiene {informacion_usuario['edad']} años, "
      f"vive en {informacion_usuario['direccion']} "
      f"y su número de teléfono es {informacion_usuario['telefono']}")