import copy
import os
import sys
import inspect
import unittest
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
import Ejercicio1 as e1

class TestEj1(unittest.TestCase):
    def setUp(self):
        lista = [e1.Alumno("Juan", 2), e1.Alumno("Pepe", 3), e1.Alumno("Sylvia", 9)]

    def test_calificacion(self):
        bcatalogado = e1.Alumno("Juan", 2).calificacion()