import unittest
from polynomial import Polynomial

class TestPolynomial(unittest.TestCase):

    def test_degree(self):
        p = Polynomial([1, 2, 0, 3])
        self.assertEqual(p.degree(), 3)

        q = Polynomial([0])
        self.assertEqual(q.degree(), 0)

    def test_str(self):
        r = Polynomial([1, 0, -2])
        self.assertEqual(str(r), "x^2 - 2")

        p = Polynomial([1, 2, 0, 3])
        self.assertEqual(str(p), "x^3 + 2x^2 + 3")

        q = Polynomial([0, 0, 0])
        self.assertEqual(str(q), "0")



    def test_call(self):
        p = Polynomial([1, 2, 3])
        self.assertEqual(p(0), 3)  # W(0) = 3
        self.assertEqual(p(1), 6) # W(1) = 6

    def test_addition(self):
        p = Polynomial([1, 2, 3])  # x^2 + 2x + 3
        q = Polynomial([3, 4])     # 3x + 4
        r = p + q  # x^2 + 5x + 7
        self.assertEqual(r.coefficients, [1, 5, 7])

    def test_subtraction(self):
        p = Polynomial([1, 2, 3])  # x^2 + 2x + 3
        q = Polynomial([3, 4])     # 3x + 4
        r = p - q  # x^2 - x - 1
        self.assertEqual(r.coefficients, [1, -1, -1])

    def test_multiplication(self):
        p = Polynomial([1, 2])     # x + 2
        q = Polynomial([3, 4])     # 3x + 4
        r = p * q  # 3x^2 + 10x + 8
        self.assertEqual(r.coefficients, [3, 10, 8])

    def test_iadd(self):
        p = Polynomial([1, 2, 3])
        q = Polynomial([3, 4])
        p += q  # x^2 + 5x + 7
        self.assertEqual(p.coefficients, [1, 5, 7])

    def test_isub(self):
        p = Polynomial([1, 2, 3])
        q = Polynomial([3, 4])
        p -= q  # x^2 - 1x - 1
        self.assertEqual(p.coefficients, [1, -1, -1])

    def test_imul(self):
        p = Polynomial([1, 2])
        q = Polynomial([3, 4])
        p *= q  # 3x^2 + 10x + 8
        self.assertEqual(p.coefficients, [3, 10, 8])

if __name__ == "__main__":
    unittest.main()