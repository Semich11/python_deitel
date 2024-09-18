import unittest

from python_deitel.arbitraryArgumentList import product

class MyTestCase(unittest.TestCase):
    def test_product_with_first_number_of_argument(self):
        self.assertEqual(24, product(2,3,4))

    def test_product_with_another_set_of_number_argument(self):
        self.assertEqual(1_260, product(5,21,2,6))
    # add assertion here


if __name__ == '__main__':
    unittest.main()
