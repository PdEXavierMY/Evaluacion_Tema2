class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print("La clase se ha creado con éxito")

    def calificacion(self):
        if self.nota >= 5:
            print("El alumno ha aprobado")
        else:
            print("El alumno ha suspendido")