cliente = {'Nombre' : 'Andrea',
           'Edad': 29,
           'Ocupacion': 'Ingeniera'}

pelicula ={'Titulo':'Matrix',
           'Ficha_Tecnica':{'Protagonista':'Keanu Reeves',
                            'Director':'Lana y Lilly Wachoswi'}}

elementos = [cliente,pelicula,'libro']

for e in elementos:
    match e:
        case {'Nombre': nombre,
              'Edad': edad,
              'Ocupacion': ocupacion}:
            print("Este es un cliente ")
            print(nombre, edad, ocupacion)
        case{'Titulo': titulo,
             'Ficha_Tecnica':{'Protagonista': protagonista,
                              'Director': director}}:
            print("Es una pelicula ")
            print(titulo,protagonista,director)
        case _:
            print("No se que es esto ")
