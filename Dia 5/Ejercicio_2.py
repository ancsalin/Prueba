
def volver_palabras(animal):
    palabra =  set(animal)
    palabra_ordenada = sorted(palabra)
    return palabra_ordenada

print(volver_palabras("Carrosa"))