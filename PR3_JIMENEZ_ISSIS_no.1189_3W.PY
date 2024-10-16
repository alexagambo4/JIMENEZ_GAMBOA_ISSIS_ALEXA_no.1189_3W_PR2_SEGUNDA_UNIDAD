#imprime los datos de la bellisima autora
print("JIMENEZ GAMBOA ISSIS ALEXA")
print("No.1189")
print("3W")
#imprime una linea en blanco para que se vea mas limpiecito el programa 
print("")

#programa no.3: Precios de frutas
print("Programa no.3: Precios de frutas ")
#creamos un diccionario que relaciona frutas con sus precios por kilo
precios_frutas = {
    'manzana': 3.0,  #precio por kilo
    'plátano': 2.5,
    'naranja': 4.0
}

#pedimos al usuario que introduzca una fruta y un numero de kilos
fruta_input = input("Introduce una fruta (manzana, plátano, naranja): ").lower()
kilos = float(input("Introduce el número de kilos: "))

#comprobamos si la fruta está en el diccionario y calculamos el precio
if fruta_input in precios_frutas:
    precio_total = precios_frutas[fruta_input] * kilos
    print(f"El precio de {kilos} kilos de {fruta_input} es {precio_total:.2f} €")
else:
    print("La fruta no está en el diccionarion")
