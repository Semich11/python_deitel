import unittest

from average import average


class MyTestCase(unittest.TestCase):
    def test_that_average_exist(self):
         average(6)# add assertion here

    def test_that_when_pass_5_and_10_to_average_should_return_7_5(self):
        self.assertEqual(7.5, average(5, 10))



if __name__ == '__main__':
    unittest.main()
