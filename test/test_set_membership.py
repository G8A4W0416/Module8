import unittest
from more_fun_with_collections import set_membership


class MyTestCase(unittest.TestCase):
    def test_in_set_true(self):
        my_set = {1, 2, 3, 5, 8, 13}
        self.assertEqual(set_membership.in_set(my_set, 13), True)

    def test_in_set_false(self):
        my_set = {1, 2, 3, 5, 8, 13}
        self.assertEqual(set_membership.in_set(my_set, 99), False)


if __name__ == '__main__':
    unittest.main()
