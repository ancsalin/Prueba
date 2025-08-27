class Padre:
    def hablar(self):
        print(" Hola ")

class Madre:
    def reir(self):
        print("Ja jaja bueno")

    def hablar(self):
        print("¿Como estas?")

class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass


mi_nieto = Nieto()
print(Nieto.mro())

