class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


# Clase Alumno que hereda de Persona
class Alumno(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)


# Ejemplo de uso
persona1 = Persona("Carlos", 40)
alumno1 = Alumno("Ana", 20)

print(f"Persona: {persona1.nombre}, Edad: {persona1.edad}")
print(f"Alumno: {alumno1.nombre}, Edad: {alumno1.edad}")


#EJERCICIO 2

class Mascota:
    def __init__(self, edad, nombre, cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas


class Perro(Mascota):
    def __init__(self, edad, nombre, cantidad_patas):
        super().__init__(edad, nombre, cantidad_patas)


mascota1 = Mascota(40, "Gato", 4)
perro1 = Perro(12, "Rocky", 3)

#EJERCICIO 3

class Mago():
    def atacar(self):
        print("Ataque mágico")


class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")


class Samurai():
    def atacar(self):
        print("Ataque con katana")


gandalf = Mago()
hawkeye = Arquero()
jack = Samurai()

personajes = [hawkeye, gandalf, jack]

for personaje in personajes:
    personaje.atacar()