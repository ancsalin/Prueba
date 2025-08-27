from  random import  *

colores = ['azul', 'rojo', 'verde','amarillo']
#aleatorio = randint(1,50)
#aleatorio = round(uniform(1,5),1)
#aleatorio = random()
aleatorio =choice(colores)
print(aleatorio)

#Ejercicio 2
numeros = list(range(5,50, 5))

shuffle(numeros)
print(numeros)


