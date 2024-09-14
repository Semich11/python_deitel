import unittest
from temperatureConversion import temperature_convertor

# from python_deitel.temperatureConversion import temperature_convertor


class MyTestCase(unittest.TestCase):
    def test_that_temperature_conversion_exist(self):
         calsius = temperature_convertor();


if __name__ == '__main__':
    unittest.main()
