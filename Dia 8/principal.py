import  numeros

def preguntar():

    print("Bienvenido a Farmacia Andrea")


    while True:
        print("[P] - Perfumeria\n [F] - Farmacia\n[C] - Cosmetica")
        try:
            mi_rubro =input("Elija su rubro: ").upper()
            ["P","F", "C"].index(mi_rubro)
        except ValueError:
            print("Esa no es una opcion valida ")
        else:
            break


    numeros.decorador(mi_rubro)

'''def inicio():
    while True:
        preguntar()
        try:
            otro_turno = input("Quieres sacar otro turno? [S] [N]: ").upper()
        except ValueError:
            print("Esa no es una opcion valida ")
        else:
            if otro_turno == "N":
                print("Gracias por su visita ")
                break'''


def inicio():
    while True:
        preguntar()
        while True:
            otro_turno = input("¿Quieres sacar otro turno? [S] [N]: ").upper()
            if otro_turno in ["S", "N"]:
                break
            else:
                print("Respuesta inválida. Por favor, ingresa solo 'S' o 'N'.")
        if otro_turno == "N":
            print("Gracias por su visita.")
            break

inicio()