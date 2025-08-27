#Ejemplo1

def suma(**kwargs):

    total = 0

    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
    return total

print(suma(x=3, y=5,z=6))

#Ejemplo2
def prueba(num1, num2, *args,**kwargs):
    print(f'El primer valor es {num1}')
    print(f'El segundo valor es: {num2}')

    for arg in args:
        print(f"arg = {arg}")
    
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        
args = [100,200,300,400]
kwargs: dict[str, str] ={'x': 'uno','y':'dos','z':'tres'}

prueba(15,50,*args, **kwargs)

#Ejercicio 3
def cantidad_atributos(**kwargs):
    return len(kwargs)
resultado = cantidad_atributos(Nombre="Andrea", Edad=29, Profesion=" Ing de Software")

print(f"Cantidad atributos:", resultado)

#Ejemplo 4
def lista_atributos(**kwargs):
    return list(kwargs.values())


lista = lista_atributos(Nombre="Andrea", Edad=29, Profesion=" Ing de Software")
print(f"Lista atributos ", lista)

#Ejemplo 5
def describir_persona(nombre, **caracteristicas):
    print(f"Características de {nombre}:")
    for clave, valor in caracteristicas.items():
        print(f"{clave}: {valor}")