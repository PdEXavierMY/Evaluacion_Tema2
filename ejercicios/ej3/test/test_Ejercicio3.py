import copy
import os
import sys
import inspect
import unittest
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
import Ejercicio3 as e3

class TestEj1(unittest.TestCase):
    def setUp(self):
        lista = [e3.Producto(1134, "N", 23, "A"), e3.Producto(1135, "W", 19, "B"), e3.Producto(1135, "M", 10, "C")]

    def test_clase(self):
        testclase = e3.Producto(1134, "N", 23, "A")