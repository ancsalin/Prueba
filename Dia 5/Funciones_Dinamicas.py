

def chequear_3_cifras(lista):
   # return  numero in range (100, 1000)
    for n in lista:
        if n in range(100, 1000):
            return  True
        else:
            pass

resultado = chequear_3_cifras([656,99,5000])
print(resultado)