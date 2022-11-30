class Animal:
    def __init__(self,tipo,familia,especie):
        self.tipo=tipo
        self.familia=familia
        self.animal=especie
    def __str__(self):
        cadena = "El nombre de este animal es "+self.raza
        return cadena
    def desplaza(self,tipo_extremidad):
        print("Se despaza usando sus ",tipo_extremidad)

class Perro(Animal):
    def __init__(self,tipo,familia,especie):
        super().__init__(tipo,familia,especie)
    def sonido(self):
        print("Los perros ladran")
        print("Guau")

class Gato(Animal):
     def __init__(self,tipo,familia,especie):
        super().__init__(tipo,familia,especie)
     def sonido(self):
        print("Los gatos maullan")
        print("Miau")

