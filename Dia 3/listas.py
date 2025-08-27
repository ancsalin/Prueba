mi_lista = ['a','b','c']
#resultado = len(mi_lista)
mi_lista2 =['d','e','f']
#resultado = mi_lista[0:]
#print(mi_lista+mi_lista2)
mi_lista3 =  mi_lista + mi_lista2

mi_lista3[0]='alfa'
mi_lista3.append('g')

eliminado = mi_lista3.pop(0)

print(mi_lista3)
print(eliminado)


#otra_lista = ['Hola', 55, 6.1]


#Ordenar Listas
lista = ['g', 'o','b','m','c']
lista.sort() #Ordena la lista alfabeticamente
lista.reverse() # Las ordena alrevez
print(lista)