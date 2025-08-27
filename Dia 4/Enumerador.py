#Ejemplo 1
lista = ['a', 'b', 'c']

for indice,item in enumerate(range(50,55)):
    print(indice,item)

#Ejemplo 2
mis_tuples = list(enumerate(lista))
print(mis_tuples[1][0])


#Ejemplo 3
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice, nombre in enumerate(lista_nombres):
    print(f"{nombre} se encuentra en el índice {indice}")