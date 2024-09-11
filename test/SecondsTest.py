import unittest
from toSeconds import getSecond



class MyTestCase(unittest.TestCase):
    def test_if_toSecond_exist(self):
        getSecond(13,50,45)

    def test_when_13_30_45_is_pass_to_getSecond_should_return_48645(self):
        seconds = getSecond(13,30,45)
        assert seconds == 48645


if __name__ == '__main__':
    unittest.main()
