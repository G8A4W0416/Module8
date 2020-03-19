import unittest
from more_fun_with_collections import dict_membership


class MyTestCase(unittest.TestCase):
    def test_in_dict_true(self):
        my_set = {'A': 1, 'B': 2, 'C': 3, 'E': 5, 'H': 8, 'M': 13}
        self.assertEqual(dict_membership.in_dict(my_set, 'M'), True)

    def test_in_dict_false(self):
        my_set = {'A': 1, 'B': 2, 'C': 3, 'E': 5, 'H': 8, 'M': 13}
        self.assertEqual(dict_membership.in_dict(my_set, 'F'), False)


if __name__ == '__main__':
    unittest.main()
