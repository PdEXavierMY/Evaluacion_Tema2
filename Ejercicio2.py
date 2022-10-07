class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print("La clase se ha creado con éxito")
    
    def __str__(self):
        return "El alumno se llama {} y su nota es {}".format(self.nombre, self.nota)

    def calificacion(self):
        if self.nota >= 5:
            print("El alumno ha aprobado")
        else:
            print("El alumno ha suspendido")

