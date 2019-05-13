calculo = input("Hola usuario, ¿quiere sumar (+), restar (-), multiplicar (*) o dividir (/)? ")
x1 = int(input("Dígame su primer número: "))
x2 = int(input("Digame su segundo número: "))

if calculo == "+":
    print("El resultado es: ", x1+x2)
elif calculo == "-":
    print("El resultaod es: ", x1-x2)
elif calculo == "*":
    print("El resulado es: ", x1*x2)
elif calculo == "/":
    print("El resultado es: ", x1/x2)