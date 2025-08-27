#Ejericicios 1
import re


def verificar_email(email):
    # Patrón para verificar que contiene @ y termina en .com o .com.algo
    patron = r'^[^@]+@[^@]+\.(com)(\.\w+)?$'

    if re.match(patron, email):
        print("Ok")
    else:
        print("La dirección de email es incorrecta")


    #Ejericicio 2

    import re

    def verificar_saludo(frase):
        patron = r'^Hola\b'
        if re.match(patron, frase):
            print("Ok")
        else:
            print("No has saludado")

#Ejericio 3
import re


def verificar_cp(codigo_postal):
    # Patrón: dos caracteres alfanuméricos seguidos de cuatro dígitos
    patron = r'^[A-Za-z0-9]{2}[0-9]{4}$'

    if re.match(patron, codigo_postal):
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")
        
