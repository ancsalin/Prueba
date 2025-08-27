#Ejercicio 1
lista =['Ana','Carlos', 'Camila', 'Karen']

for letra in lista:
    numero_letra = lista.index(letra)+ 1
    print(f"Letra{numero_letra}: {letra}")

#Ejemplo 2

lista1 = ['Andrea','laura','fede','luis','julia' ]

for nombre in lista1:
    if nombre.startswith('l'):
        print(nombre)
    else:
        print('Nombre que no comienza con l')

#Eejmplo 3

numeros =[1,2,3,4,5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero

print(mi_valor)

#Ejemplo 4
for a,b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)

#Ejemplo 4
dic = {'clave1':'a','clave2':'b', 'clave3':'c'}

for item in dic.values():
    print(item)