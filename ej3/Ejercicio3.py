class Producto():
    def __init__(self, codigo, nombre, precio, tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
        print("La clase se ha creado con éxito")

    def __str__(self):
        return "El producto tiene codigo {}, nombre {}, precio {} € y tipo {}".format(self.codigo, self.nombre, self.precio, self.tipo)

a = Producto(1122, "A-steroid", 17, "Spray")
print(a)
a.precio = 18
print(a)