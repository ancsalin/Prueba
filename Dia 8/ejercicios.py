#Ejemplo 1
def suma(num1, num2):
    try:
        resultado = num1 + num2
    except:
        print("Error inesperado")
    else:
        print(resultado)

#Ejemplo 2
def cociente(num1, num2):
    try:
        resultado = num1 / num2
    except TypeError:
        print("Los argumentos a ingresar deben ser números")
    except ZeroDivisionError:
        print("El segundo argumento no debe ser cero")
    else:
        print(resultado)

#Ejercicio 3
def secuencia_infinita():
    num = 0
    while True:
        num += 1
        yield num


generador = secuencia_infinita()

#Ejercico 4
def multiplos_siete():
    num = 1
    while True:
        yield 7 * num
        num += 1

generador = multiplos_siete()

#Ejercicio 5

def mensaje():
    x = "Te quedan 3 vidas"
    yield x

    x = "Te quedan 2 vidas"
    yield x

    x = "Te queda 1 vida"
    yield x

    x = "Game Over"
    yield x


perder_vida = mensaje()