from unittest import main, TestCase
from calculator import divisao


class DivisaoTest(TestCase):
    def test_divisao_por_inteiro(self):
        self.assertEqual(divisao(8, 4), 2)
    
    def test_divisao_por_flutuante(self):
        self.assertEqual(divisao(10, 2.5), 4)
    
    def test_divisao_por_numero_maior(self):
        self.assertEqual(divisao(1, 100), 0.01)
    
    def test_divisao_por_zero(self):
        self.assertRaises(ZeroDivisionError, divisao, 20, 0)


if __name__ == '__main__':
    main()
