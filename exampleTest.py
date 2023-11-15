import unittest
import functions_example as e

class Numbers(unittest.TestCase):

    def test_20(self):
        x = 13
        self.assertEqual(x, 20)

    def test_2(self):
        x = 13
        self.assertEqual(x, 2)

    def test_a(self):
        x = 'a'
        self.assertEqual(x, 'a')

    def test_odd(self):
        x = 13
        self.assertTrue(x % 2 == 1)

    def test_even(self):
        x = 13
        self.assertTrue(x % 2 == 0)

    def test_1(self):
        x = 13
        self.assertEqual(x, 1)

    def test_99(self):
        x = 13
        self.assertEqual(x, 99)

    def test_foobar(self):
        return_value = e.foobar('barfoo')
        self.assertEqual(True, return_value)

if __name__ == '__main__':
    unittest.main()