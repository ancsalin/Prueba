nombres = ['Ana', 'Hugo', 'Valeria']
edades = [65, 29, 42]
ciudades = ['Lima','Madrid', 'Mexico']

combinados = list(zip(nombres,edades,ciudades))

for nombre, edades, ciudades in combinados:
    print(f"{nombres} tiene {edades} años y vive en {ciudades}")


#Ejercicio 2

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]



for paises, capitales in zip(paises, capitales):
    print(f"La capital de {paises} es {capitales}")