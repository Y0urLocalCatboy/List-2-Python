import unittest
from polynomial import Polynomial

class TestPolynomial(unittest.TestCase):
    """
    Unit test class for testing the Polynomial class.

    Methods:
        test_degree(): Tests if the polynomial degree is calculated correctly.
        test_str(): Tests if the polynomial is correctly represented as a string.
        test_call(): Tests polynomial evaluation at specific x-values.
        test_addition(): Tests addition of two polynomials.
        test_subtraction(): Tests subtraction of two polynomials.
        test_multiplication(): Tests multiplication of two polynomials.
        test_iadd(): Tests in-place addition of two polynomials.
        test_isub(): Tests in-place subtraction of two polynomials.
        test_imul(): Tests in-place multiplication of two polynomials.
    """

    def test_degree(self):
        """
        Tests the degree() method for correct polynomial degree calculation.

        Asserts:
            p.degree() returns the degree of polynomial with non-zero coefficients.
            q.degree() returns 0 for a zero polynomial.
        """
        p = Polynomial([1, 2, 0, 3])
        self.assertEqual(p.degree(), 3)

        q = Polynomial([0])
        self.assertEqual(q.degree(), 0)

    def test_str(self):
        """
        Tests the __str__() method to ensure the polynomial string representation is accurate.

        Asserts:
            str(r) produces "x^2 - 2" for Polynomial([1, 0, -2]).
            str(p) produces "x^3 + 2x^2 + 3" for Polynomial([1, 2, 0, 3]).
            str(q) produces "0" for a zero polynomial.
        """
        r = Polynomial([1, 0, -2])
        self.assertEqual(str(r), "x^2 - 2")

        p = Polynomial([1, 2, 0, 3])
        self.assertEqual(str(p), "x^3 + 2x^2 + 3")

        q = Polynomial([0, 0, 0])
        self.assertEqual(str(q), "0")

    def test_call(self):
        """
        Tests the __call__() method to check polynomial evaluation at a given x value.

        Asserts:
            p(0) returns the constant term for Polynomial([1, 2, 3]).
            p(1) returns the sum of all coefficients as expected.
        """
        p = Polynomial([1, 2, 3])
        self.assertEqual(p(0), 3)
        self.assertEqual(p(1), 6)

    def test_addition(self):
        """
        Tests the __add__() method to verify addition of two polynomials.

        Asserts:
            The resulting coefficients of Polynomial([1, 2, 3]) + Polynomial([3, 4])
            yield [1, 5, 7].
        """
        p = Polynomial([1, 2, 3])
        q = Polynomial([3, 4])
        r = p + q
        self.assertEqual(r.coefficients, [1, 5, 7])

    def test_subtraction(self):
        """
        Tests the __sub__() method to verify subtraction of two polynomials.

        Asserts:
            The resulting coefficients of Polynomial([1, 2, 3]) - Polynomial([3, 4])
            yield [1, -1, -1].
        """
        p = Polynomial([1, 2, 3])
        q = Polynomial([3, 4])
        r = p - q
        self.assertEqual(r.coefficients, [1, -1, -1])

    def test_multiplication(self):
        """
        Tests the __mul__() method to verify multiplication of two polynomials.

        Asserts:
            The resulting coefficients of Polynomial([1, 2]) * Polynomial([3, 4])
            yield [3, 10, 8].
        """
        p = Polynomial([1, 2])
        q = Polynomial([3, 4])
        r = p * q
        self.assertEqual(r.coefficients, [3, 10, 8])

    def test_iadd(self):
        """
        Tests the __iadd__() method for in-place addition.

        Asserts:
            After in-place addition of Polynomial([1, 2, 3]) and Polynomial([3, 4]),
            the coefficients are updated to [1, 5, 7].
        """
        p = Polynomial([1, 2, 3])
        q = Polynomial([3, 4])
        p += q
        self.assertEqual(p.coefficients, [1, 5, 7])

    def test_isub(self):
        """
        Tests the __isub__() method for in-place subtraction.

        Asserts:
            After in-place subtraction of Polynomial([1, 2, 3]) and Polynomial([3, 4]),
            the coefficients are updated to [1, -1, -1].
        """
        p = Polynomial([1, 2, 3])
        q = Polynomial([3, 4])
        p -= q
        self.assertEqual(p.coefficients, [1, -1, -1])

    def test_imul(self):
        """
        Tests the __imul__() method for in-place multiplication.

        Asserts:
            After in-place multiplication of Polynomial([1, 2]) and Polynomial([3, 4]),
            the coefficients are updated to [3, 10, 8].
        """
        p = Polynomial([1, 2])
        q = Polynomial([3, 4])
        p *= q
        self.assertEqual(p.coefficients, [3, 10, 8])

if __name__ == "__main__":
    unittest.main()
