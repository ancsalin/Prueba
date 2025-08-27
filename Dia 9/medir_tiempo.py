import timeit




declaracion = '''
prueba_for(10)
'''

mi_setup = '''
def prueba_for(numero):
    lista = []
    for num in range(1, numero +1 ):
        lista.append(num)
    return  lista'''

duracion = timeit.timeit(declaracion, mi_setup, number = 100000)
print(duracion)

declaracion2 ='''
prueba_while
'''

mi_setup2 = '''
def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista
'''

duracion2 = timeit.timeit(declaracion2, mi_setup2, number = 100000)
print(duracion2)