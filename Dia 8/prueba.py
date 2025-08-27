import unittest
import cambia_texto

class Pruebame(unittest.TestCase):
    def test_mayus(self):
        palabra = 'aja pues'
        resultado = cambia_texto.todo_mayus()
        self.assertEqual(resultado, 'Aja Pues')


if __name__ == '__main__':
    unittest.main()