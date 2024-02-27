class TV:
    numTv = 0

    def __init__(self, marca, estado):
        self.marca = marca
        self.estado = estado
        self.canal = 1
        self.volumen = 1
        self.precio = 500

        TV.numTv += 1

    @staticmethod
    def getNumTv():
        return TV.numTv

    @staticmethod
    def setNumTv(num_tv):
        TV.numTv = numTv

    def turnOn(self):
        self.estado = True

    def turnOff(self):
        self.estado = False

    def canalUp(self):
        self.setCanal(self.canal + 1)

    def canalDown(self):
        self.setCanal(self.canal - 1)

    def volumenUp(self):
        self.setVolumen(self.volumen + 1)

    def volumenDown(self):
        self.setVolumen(self.volumen - 1)

    def getMarca(self):
        return self.marca

    def getCanal(self):
        return self.canal

    def getPrecio(self):
        return self.precio

    def getEstado(self):
        return self.estado

    def getVolumen(self):
        return self.volumen

    def getControl(self):
        return self.control

    def setMarca(self, marca):
        self.marca = marca

    def setCanal(self, canal):
        if self.estado and 1 <= canal <= 120:
            self.canal = canal

    def setPrecio(self, precio):
        self.precio = precio

    def setVolumen(self, volumen):
        if self.estado and 0 <= volumen <= 7:
            self.volumen = volumen

    def setControl(self, control):
        self.control = control