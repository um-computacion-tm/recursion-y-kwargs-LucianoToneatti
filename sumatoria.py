def sumatoria1(value):
    resultado = 0
    while value > 0:
        resultado = resultado + value 
        value -= 1
    return resultado
result = sumatoria1(4)
print(result)

def sumatoria(value):
    if value == 1:
        return 1
    return value + sumatoria(value - 1)
resultado = sumatoria(6)
print(resultado)

###TEST###

import unittest
#quiero los test de Sumatoria: 

class TestSumatoria(unittest.TestCase):
    def test_con_1(self):
        resultado = sumatoria(1)
        self.assertEqual(resultado, 1)

    def test_con_2(self):
        resultado = sumatoria(2)
        self.assertEqual(resultado, 3)

    def test_con_3(self):
        resultado = sumatoria(3)
        self.assertEqual(resultado, 6)

    def test_con_4(self):
        resultado = sumatoria(4)
        self.assertEqual(resultado, 10)

    def test_con_5(self):
        resultado = sumatoria(5)
        self.assertEqual(resultado, 15)

    def test_con_6(self):
        resultado = sumatoria(6)
        self.assertEqual(resultado, 21)

unittest.main()