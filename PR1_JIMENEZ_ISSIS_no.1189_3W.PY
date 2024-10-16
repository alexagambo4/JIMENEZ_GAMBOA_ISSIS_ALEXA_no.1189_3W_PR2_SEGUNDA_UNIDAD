#imprime los datos de la bellisima autora
print("JIMENEZ GAMBOA ISSIS ALEXA")
print("No.1189")
print("3W")
#imprime una linea en blanco para que se vea mas limpiecito el programa 
print("")

#programa no.1: Diccionario de divisas
print("Programa no.1: Diccionario de divisas")
#imprime una linea en blanco 
print("")

#creamos un diccionario que relaciona divisas con sus símbolos
divisas = {'euro': '€', 'dollar': '$', 'yen': '¥'}

#pedimos al usuario que ingrese una divisa
divisa_input = input("Introduce una divisa (euro, dollar, yen): ")

#comprobamos si la divisa está en el diccionario
if divisa_input in divisas:
    print(f"El símbolo de {divisa_input} es {divisas[divisa_input]}")
else:
    print("La divisa no está en el diccionario")
