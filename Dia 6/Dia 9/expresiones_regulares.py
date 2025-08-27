
import re

texto = " Llama al 562-542-323-5245 ya "

patron = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

resultado = re.search(patron, texto)

print(resultado.group(1))


clave = input("Clave: ")

patron = r'\D{1}w{7}'

chequear = re.search(patron, clave)
print(chequear)