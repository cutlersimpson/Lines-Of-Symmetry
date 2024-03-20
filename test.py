import unittest
from app import find_lines_of_symmetry, coefficients_to_equation


class TestFindLinesOfSymmetry(unittest.TestCase):
    def test_empty(self):
        points = []
        coeffs = find_lines_of_symmetry(points)
        eqns = [coefficients_to_equation(a, b, c) for a, b, c in coeffs]
        expected_output = []
        self.assertEqual(eqns, expected_output)

    def test_square(self):
        points = [(0, 0), (0, 1), (1, 0), (1, 1)]
        coeffs = find_lines_of_symmetry(points)
        eqns = [coefficients_to_equation(a, b, c) for a, b, c in coeffs]
        expected_output = [
            "y = -1.0x + 1.0",
            "x = 0.5",
            "y = 0.0x + 0.5",
            "y = 1.0x + -0.0",
        ]
        self.assertEqual(eqns, expected_output)

    def test_rectangle(self):
        points = [(0, 0), (0, 2), (3, 0), (3, 2)]
        coeffs = find_lines_of_symmetry(points)
        eqns = [coefficients_to_equation(a, b, c) for a, b, c in coeffs]
        expected_output = ["y = 0.0x + 1.0", "x = 1.5"]
        self.assertEqual(eqns, expected_output)

    def test_rhombus(self):
        points = [(0, 1), (1, 0), (2, 1), (1, 2)]
        coeffs = find_lines_of_symmetry(points)
        eqns = [coefficients_to_equation(a, b, c) for a, b, c in coeffs]
        expected_output = [
            "y = 0.0x + 1.0",
            "y = 1.0x + -0.0",
            "x = 1.0",
            "y = -1.0x + 2.0",
        ]
        self.assertEqual(eqns, expected_output)

    def test_trapezoid(self):
        points = [(0, 0), (1, 2), (3, 2), (4, 0)]
        coeffs = find_lines_of_symmetry(points)
        eqns = [coefficients_to_equation(a, b, c) for a, b, c in coeffs]
        expected_output = ["x = 2.0"]
        self.assertEqual(eqns, expected_output)

    def test_parallelogram(self):
        points = [(0, 0), (1, 1), (3, 1), (2, 0)]
        coeffs = find_lines_of_symmetry(points)
        eqns = [coefficients_to_equation(a, b, c) for a, b, c in coeffs]
        expected_output = []
        self.assertEqual(eqns, expected_output)

    def test_triangle(self):
        points = [(0, 0), (2, 0), (1, 1)]
        coeffs = find_lines_of_symmetry(points)
        eqns = [coefficients_to_equation(a, b, c) for a, b, c in coeffs]
        expected_output = ["x = 1.0"]
        self.assertEqual(eqns, expected_output)


if __name__ == "__main__":
    unittest.main()
