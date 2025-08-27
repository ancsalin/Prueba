from pathlib import Path

print("Bienvenido a nuestro Recetario \n Te presento la ruta de nuestras recetas C:\\Users\\acsal\\Documents\\CursoPython\\Dia 6\\Recetas")
print("Tenemos 8 recetas para tu eleccion, te mostramos las opciones")

print("Categorias disponibles: ")
print("1. Carnes")
print("2. Ensaladas")
print("3. Pastas")
print("4. Postres")

categoria = input("Elige la categoria que deseas: ")
# Describe la categoria 1
if categoria == "1":
    print("Receta de carnes:")
    print(" a. Entrecot al Malbec")
    print(" b. Matanbre a la pizza")

    receta = input("Elige una receta (A o B): ")
    if receta == "a":
        print(" Entercol al Malbec. Pollo y queso por 30 min")
    elif receta == "b":
        print("Matanbre a la pizza. (Pizza y Gaseosa) 45 min")
    else:
        print("Opcion no valida")

#Describe la  categoria 2

if categoria == "2":
    print("Receta de Ensaladas: ")
    print(" a. Ensalada Griega")
    print(" b. Ensalada mediterranea")

    receta = input("Elige una receta (A o B): ")
    if receta == "a":
        print(" Ensalada Griega.(Queso Feta y aceite de Oliva) 20 min")
    elif receta == "b":
        print("Ensalada Mediterranea. (Pasto y pepino) 15 min")
    else:
        print("Opcion no valida")

#Describe la  categoria 3

if categoria == "3":
    print("Receta de Pastas: ")
    print(" a.Canelones de espinaca ")
    print(" b. Ravioles de ricotta ")

    receta = input("Elige una receta (A o B): ")
    if receta == "a":
        print(" Canelones de espinaca .(concha y espinacas) 35 min")
    elif receta == "b":
        print("Ensalada Mediterranea. ( Camaron y salmon) ")
    else:
        print("Opcion no valida")

#Describe la  categoria 4

if categoria == "":
    print("Receta de Postres: ")
    print(" a. Compota de manzana")
    print(" b. Tarda de frambuesa")

    receta = input("Elige una receta (A o B): ")
    if receta == "a":
        print("Compota de manzana Griega.(Pure de manzana y aceite de Oliva)")
    elif receta == "b":
        print("Tarda de frambuesa. (Con queso parmesana y yogurt griego)")
    else:
        print("Opcion no valida")

