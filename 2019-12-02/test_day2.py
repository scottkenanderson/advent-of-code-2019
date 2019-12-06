import unittest
import day2

class TestDay2(unittest.TestCase):
    def test_can_split_code(self):
        expected = [[1, 0, 0, 3]]#, [99]]
        actual = day2.intcode_reader("1,0,0,3,99")
        self.assertEqual(actual, expected)

    def test_can_split_longer_code(self):
        expected = [[1,9,10,3], [2,3,11,0]]#, [99]]
        actual = day2.intcode_reader("1,9,10,3,2,3,11,0,99,30,40,50")
        self.assertEqual(actual, expected)

    def test_can_run_code(self):
        test_cases = [
            ("1,0,0,0,99", "2,0,0,0,99"),
            ("2,3,0,3,99", "2,3,0,6,99"),
            ("2,4,4,5,99,0", "2,4,4,5,99,9801"),
            ("1,1,1,4,99,5,6,0,99", "30,1,1,4,2,5,6,0,99")
        ]

        for input, expected in test_cases:
            actual = day2.run_code([int(x) for x in input.split(',')])
            print(actual)
            self.assertEqual(actual, expected)

    def test_can_perform_part_1(self):
        test_cases = [
            (','.join(['1' for x in range(0, 16)]), "1")
        ]

        for input, expected in test_cases:
            actual = day2.part_1(input)
            print(actual)
            self.assertEqual(actual, expected)
