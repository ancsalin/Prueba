texto = input("Ingresa un texto a eleccion: ")
letras = []

texto = texto.lower()

letras.append(input(" Ingresa la primera letra: ").lower())
letras.append(input(" Ingresa la segunda letra: ").lower())
letras.append(input(" Ingresa la tercera letra: ").lower())

print("\n")
print("CANTIDAD DE LETRAS ")
cant_letras1 = texto.count(letras[0])
cant_letras2 = texto.count(letras[1])
cant_letras3 = texto.count(letras[2])

print(f"Hemos encontrado la letra '{letras[0]}' repetida {cant_letras1} veces")
print(f"Hemos encontrado la letra '{letras[1]}' repetida {cant_letras2} veces")
print(f"Hemos encontrado la letra '{letras[2]}' repetida {cant_letras3} veces")

print("\n")
print("CANTIDAD DE PALABRAS")
palabras =texto.split()
print(f"Hemos encontrado {len(palabras)} palabras en tu texto ")

print("\n")
print("LETRAS DE INICIO Y FIN")
letra_inicio = texto[0]
letra_fin = texto[-1]
print(f" La letra de inicial es'{letra_inicio}' y la letra final es {letra_fin}")

print("\n")
print("TEXTO INVERTIDO")
palabras.reverse()
texto_inv  = ' '.join(palabras)
print(f"Si ordenamos tu texto alreves va a decir'{texto_inv}'")

print("\n")
print("BUSCANDO LA PALABRA PYTHON")
buscar_python = "Python" in texto
dic = {True:"sí", False:"no"}
print(f"La palabra 'Python'{dic[buscar_python]} se encuentra en el texto")