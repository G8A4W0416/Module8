import unittest
import datetime
from more_fun_with_collections import half_birthday


class MyTestCase(unittest.TestCase):
    def test_half_birthday(self):
        self.assertEqual(half_birthday.half_birthday(datetime.date(2020, 2, 28)), '2020-08-28')


if __name__ == '__main__':
    unittest.main()
