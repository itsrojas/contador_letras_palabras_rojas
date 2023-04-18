import unittest

from trabajo_contar_letras import contar_letras

class TestCountLetters(unittest.TestCase):

    def test_simple(self):
        result = contar_letras('a')
        self.assertEqual(result, {'a': 1})

    def test_complex(self):
        result = contar_letras('hola')
        self.assertEqual(
            result,
            {
                'h': 1,
                'o': 1,
                'l': 1,
                'a': 1,
            }
        )

    def test_super_complex(self):
        result = contar_letras('hola chau')
        self.assertEqual(
            result,
            {
                'h': 2,
                'o': 1,
                'l': 1,
                'a': 2,
                ' ': 1,
                'c': 1,
                'u': 1
            }
        )

if __name__ == '__main__':
    unittest.main()