nombre = input("¿Cómo te llamas? ")
estado_de_animo = input("¿Qué tal " + nombre + ", cómo te encuentras? ")

if estado_de_animo == "contento":
    print("Me alegro mucho " + nombre)

elif estado_de_animo == "cansado":
    print(nombre + " tienes que descansar")

elif estado_de_animo == "triste":
    print("vamos " + nombre + ", que es lunes y puedes ver Juego de Tronos")

else:
    print(nombre + " eso que te pasa es muy raro")