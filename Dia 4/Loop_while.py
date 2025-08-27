monedas = 5

while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1
else: print("No tengo mas dinero")

#Ejemplo 2
respuesta = "s"

while respuesta == "s":
    respuesta = input("Quieres seguir? s/n")
else:
    print("Gracias")

# Pass = Pasar el programa
while respuesta == "s":
    pass

print("Hola")

#Break, interrumpe la ejecucion del programa
nombre = input("Tu nombre: ")
for letra in nombre:
        if letra == 'r':
            break
        print(letra)

#Continue, da continuidad al codigo
nombre = input("Tu nombre: ")
for letra in nombre:
        if letra == 'r':
            continue
        print(letra)