import unittest
from datetime import datetime

from python_deitel.dateAndTime import date_and_time


class MyTestCase(unittest.TestCase):
    def test_that_date_and_type_return_datetime_type(self):
        self.assertIsInstance(date_and_time(), datetime)  # add assertion here

if __name__ == '__main__':
    unittest.main()
