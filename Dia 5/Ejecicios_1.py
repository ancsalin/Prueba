def devolver_distintos(x,y,z):
    numeros = [x,y,z]
    suma = sum(numeros)

    if suma > 15:
        return max(numeros)
    elif suma < 10:
        return min(numeros)
    else:
        numeros.sort()
        return numeros[1]

print(devolver_distintos(9, 6, 7))  # Suma = 18, devuelve 7 (el mayor)
print(devolver_distintos(1, 2, 3))   # Suma = 6, devuelve 1 (el menor)
print(devolver_distintos(4, 5, 3))   # Suma = 12, devuelve 4 (el intermedio)