class Vaca:
    def __init__(self,nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + "Dice muuu")


class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice beeee")

vaca1 = Vaca('Camela')
oveja1 = Oveja('Nieve')

def animal_habla(animal):
    animal.hablar()

animal_habla(oveja1)