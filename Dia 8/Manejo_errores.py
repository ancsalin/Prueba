def pedir_numero():

    while True:
        try:
            numero = int(input("Dame un numero: "))
        except:
            print("Eso no es un numero ")
        else:
            print(f"Ingresaste el numero {numero}")
            break
    print("Gracias")

pedir_numero()