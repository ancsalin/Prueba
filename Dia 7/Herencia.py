class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal nacio ")

class Pajaro(Animal):
    pass

piolin = Pajaro(2, 'Amarilo')

print(piolin.color)