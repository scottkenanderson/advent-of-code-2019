import unittest
import day3 as solution

class TestDay2(unittest.TestCase):
    def test_can_calculate_distance(self):
        test_cases = [
            (["R8,U5,L5,D3", "U7,R6,D4,L4"], 6),
            (["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"], 159),
            (["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"], 135),
        ]

        for wires, expected in test_cases:
            actual = solution.run_code(wires)
            print(actual)
            self.assertEqual(actual, expected)
