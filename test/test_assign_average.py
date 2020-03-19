import unittest
from more_fun_with_collections import assign_average


class MyTestCase(unittest.TestCase):
    def test_average_for_grade_a(self):
        self.assertEqual(assign_average.switch_average('A'), 90)

    def test_average_for_grade_b(self):
        self.assertEqual(assign_average.switch_average('B'), 80)

    def test_average_for_grade_c(self):
        self.assertEqual(assign_average.switch_average('C'), 70)

    def test_average_for_grade_d(self):
        self.assertEqual(assign_average.switch_average('D'), 60)

    def test_average_for_grade_f(self):
        self.assertEqual(assign_average.switch_average('F'), 0)

    def test_for_invalid_grade(self):
        self.assertEqual(assign_average.switch_average('E'), "Invalid Grade")


if __name__ == '__main__':
    unittest.main()
