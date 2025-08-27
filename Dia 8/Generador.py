'''def mi_funcion():
    lista = []
    for x in range(1, 5):
        lista.append(x * 10)
    return

def mi_generador():
    for x in range(1, 5):
        yield x * 10


print(mi_funcion())
print(mi_generador())

g = mi_generador()
print(next(g))

g = mi_generador()

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))'''

#Ejemplo

def mi_generado():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x

r = mi_generado()
print(next(r))
print(next(r))
print(next(r))