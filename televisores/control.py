class Control:
    def __init__(self):
        self.tv = None

    def enlazar(self, tv):
        self.tv = tv
        tv.set_control(self)

    def turn_on(self):
        self.tv.turn_on()

    def turn_off(self):
        self.tv.turn_off()

    def canal_up(self):
        self.tv.canal_up()

    def canal_down(self):
        self.tv.canal_down()

    def volumen_up(self):
        self.tv.volumen_up()

    def volumen_down(self):
        self.tv.volumen_down()

    def set_canal(self, canal):
        self.tv.set_canal(canal)

    def set_volumen(self, volumen):
        self.tv.set_volumen(volumen)

    def get_tv(self):
        return self.tv

    def set_tv(self, tv):
        self.tv = tv