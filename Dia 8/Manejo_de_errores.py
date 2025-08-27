def suma():
    n1 = int(input(" Numero 1: "))
    n2 = int(input("Numero 2: "))
    print(n1 + n2)
    print(" Gracias por sumar")


try:
    suma()
except TypeError:
    print("Estas intentando cancatenar tipos distintos  ")
except ValueError:
    print("Eso  no es un numero")
else:
    print("Hiciste todo bien ")
finally:
    print("ESO FUE TODO")





