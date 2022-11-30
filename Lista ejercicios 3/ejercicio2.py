class Producto:
    def __init__(self,pieza,marca,modelo):
        self.pieza=pieza
        self.marca=marca
        self.modelo=modelo
        print("Se ha agregado la siguiente autoparte: ",self.pieza," / ",self.marca)
    def __str__(self):
        return '{} ({}) ({})'.format(self.pieza, self.marca, self.modelo)

class Catalogo:
    listaProductos = []
    def __init__(self, producto):
        self.listaProductos.append(producto)

    def agregar(self, p): 
        self.listaProductos.append(p)

    def mostrar(self):
        for p in self.listaProductos:
            print(p) 

