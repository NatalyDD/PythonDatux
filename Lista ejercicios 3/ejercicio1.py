class Profesor:
    def __init__(self,nombre,apellido,dni,celular):
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni
        self.celular=celular
    def __str__(self):
        name = self.apellido + "," + self.nombre
        return f'Su nombre es {name}'
    def correo(self,correo):
        self.correo=correo
    def enseñar(self):
        pass
    def corregir_tareas (self):
        pass
    def calificar(self):
        pass


