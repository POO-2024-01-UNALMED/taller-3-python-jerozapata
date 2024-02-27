class Marca:
    def __init__(self, nombre):
        self.set_nombre(nombre)

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre