nombre = input("Hola jugador, ¿cuál es tu nombre? ")
print("Encantado de conocerte " + nombre)

permiso = input("¿Eres capaz de adivinar el número que estoy pensando(si/no)? ")
if permiso == "si":
    print("Muy bien " + nombre + " empecemos")
    adivina = input("Dime un número del 1 al 20: ")
    secreto = "17"
    if adivina == "17":
        print("Caray " + nombre + ", tienes madera de Rappel")
    else:
        print("Ups, inténtalo de nuevo amigo")
else:
    print("De acuerdo " + nombre + " vuelve cuando quieras")