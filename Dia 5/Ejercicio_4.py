def contar_primos(numero):
    primos = [2]
    iteracioin = 3

    if numero < 2:
        return 0
    while iteracioin <= numero:
        for n in range(3, iteracioin,2):
            if iteracioin % n == 0:
                iteracioin+= 2
                break
        else:
            primos.append(iteracioin)
            iteracioin += 2
        print(primos)
    return len(primos)

print(contar_primos(40))