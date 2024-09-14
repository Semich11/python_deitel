import unittest
from python_deitel.guessTheNumberGame import guessTheNumberGameFunction

class MyTestCase(unittest.TestCase):
    def test_that_guessTheNumberGameFunction_will_return_the_expected_number(self):
        muNumber = guessTheNumberGameFunction()
        self.assertEqual(muNumber, guessTheNumberGameFunction())
    def test_that_will_return_high(self):
        self.assertEqual("high", False)

    def test_that_will_return_congratulation(self):
        self.assertEqual("congratulation", False)

if __name__ == '__main__':
    unittest.main()
