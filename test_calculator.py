from unittest import main, TestCase
from calculator import divisao, Soma, Subtracao,Multiplicar


class DivisaoTest(TestCase):
    def test_divisao_por_inteiro(self):
        self.assertEqual(divisao(8, 4), 2)
    
    def test_divisao_por_flutuante(self):
        self.assertEqual(divisao(10, 2.5), 4)
    
    def test_divisao_por_numero_maior(self):
        self.assertEqual(divisao(1, 100), 0.01)
    
    def test_divisao_por_zero(self):
        self.assertRaises(ZeroDivisionError, divisao, 20, 0)
class Mulriplicar(TestCase):
    def test_multiplicar_pNegativos(self):
        self.assertEqual(Multiplicar(8,-1),-8)
    def test_multiplicar_pZero(self):
       self.assertEqual(Multiplicar(8,0),0)
    def test_multiplicar_pPositivos(self):
        self.assertEqual(Multiplicar(8,5),40)
    def test_multiplicar_NegativosAmbos(self):
        self.assertEqual(Multiplicar(-10,-10),100)
    def test_multiplicar_CVirgula(self):
        self.assertEqual(Multiplicar(10,2.5),25)
    def test_multiplicar_CvirgulaAmbos(self):
        self.assertEqual(Multiplicar(2.5,2.5),6.25)
    def test_multiplicarCVirgulaNegativo(self):
        self.assertEqual(Multiplicar(2.5,-2.5),-6.25)
    def test_multiplicarCVirgulas_ambosNegativos(self):
        self.assertEqual(Multiplicar(-2.5,-2.5),6.25)
        
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
