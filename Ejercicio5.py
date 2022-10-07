class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

 

    def __str__(self):
        return "color {}, {} ruedas".format( self.color, self.ruedas )


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, modelo):
        super().__init__(color, ruedas)
        self.modelo = modelo

    def __str__(self):
        return Vehiculo.__str__(self) + ", Modelo {}".format(self.velocidad, self.cilindrada)


class Tren(Vehiculo):
    def __init__(self, color, ruedas, longuitud, antiguedad):
        super().__init__(color, ruedas)
        self.longuitud = longuitud
        self.antiguedad = antiguedad

    def __str__(self):
        return Vehiculo.__str__(self) + ", {} m de longuitud, {} años de antiguedad".format(self.velocidad, self.cilindrada)