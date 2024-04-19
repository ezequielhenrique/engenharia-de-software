from unittest import main, TestCase
from calculator import divisao, Soma, Subtracao


class DivisaoTest(TestCase):
    def test_divisao_por_inteiro(self):
        self.assertEqual(divisao(8, 4), 2)
    
    def test_divisao_por_flutuante(self):
        self.assertEqual(divisao(10, 2.5), 4)
    
    def test_divisao_por_numero_maior(self):
        self.assertEqual(divisao(1, 100), 0.01)
    
    def test_divisao_por_zero(self):
        self.assertRaises(ZeroDivisionError, divisao, 20, 0)

class SomaTest(TestCase):
    def test_soma_dois_numeros_positivos(self):
        self.assertEqual(Soma(3, 7), 10)
    def test_soma_numeros_positivos_negativos(self):
        self.assertEqual(Soma(6,-1) , 5 )
    def test_soma_numeros_negativos(self):
        self.assertEqual(Soma(-6,-3),-9)

class  SubtracaoTest(TestCase):
    def test_sub_dois_numeros_positivos(self):
        self.assertEqual(Subtracao(10, 7), 3)
    def test_sub_numeros_positivos_negativos(self):
        self.assertEqual(Subtracao(10,-1) , 11 )
    def test_sub_numeros_negativos(self):
        self.assertEqual(Subtracao(-6,-3),-3)

if __name__ == '__main__':
    main()
