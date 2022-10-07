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


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, modelo):
        self.color = color
        self.ruedas = ruedas
        self.modelo = modelo


class Tren(Vehiculo):
    def __init__(self, color, ruedas, longuitud, antiguedad):
        self.color = color
        self.ruedas = ruedas
        self.longuitud = longuitud
        self.antiguedad = antiguedad

c = Coche("azul", 4, 150, 1200)
b = Bicicleta("verde", 2, "X15")
t = Tren("gris", "muchas", 650, 2)
lista_objetos = [c, b, t]

def catalogar(lista, ruedas=0):
    for elemento in lista:
        print(elemento)

catalogar(lista_objetos)