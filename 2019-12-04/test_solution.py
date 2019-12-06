import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_can_calculate_distance(self):
        test_cases = [
            ('111111', True),
            ('223450', False),
            ('123789', False),
            ('123729', False),
        ]

        for password, expected in test_cases:
            actual = solution.check_password(password)
            print(password)
            print(actual)
            print('test')
            self.assertEqual(actual, expected)

    def test_do_part_2(self):
        test_cases = [
            ('112345', True),
            ('111111', False),
            ('112233', True),
            ('123444', False),
            ('111122', True),
            ('223450', False),
            ('123789', False),
            ('123729', False),
        ]

        for password, expected in test_cases:
            actual = solution.check_extended_password(password)
            print(password)
            print(actual)
            print('test')
            self.assertEqual(actual, expected)
