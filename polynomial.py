class Polynomial:
    """
    A class representing a polynomial, supporting basic operations such as addition, subtraction,
    and multiplication.

    Attributes:
        coefficients (list): A list of polynomial coefficients ordered from the highest degree to the constant term.

    Methods:
        degree(): Returns the degree of the polynomial.
        __str__(): Returns the polynomial in string form, e.g., "3x^2 + 2x + 1".
        __call__(x): Evaluates the polynomial at a given value of x.
        __add__(other): Adds two polynomials and returns the result as a new Polynomial instance.
        __sub__(other): Subtracts one polynomial from another and returns the result as a new Polynomial instance.
        __mul__(other): Multiplies two polynomials and returns the result as a new Polynomial instance.
        __iadd__(other): Adds another polynomial in-place and updates the coefficients.
        __isub__(other): Subtracts another polynomial in-place and updates the coefficients.
        __imul__(other): Multiplies by another polynomial in-place and updates the coefficients.
    """

    def __init__(self, coefficients):
        """
        Initializes the Polynomial with the given coefficients, removing any trailing zeros.

        Parameters:
            coefficients (list): List of coefficients, ordered from the constant term to the highest degree.
        """
        while len(coefficients) > 1 and coefficients[-1] == 0:
            coefficients.pop()
        self.coefficients = coefficients[::-1]  # Store coefficients in reverse for easy access

    def degree(self):
        """
        Returns the degree of the polynomial.

        Returns:
            int: Degree of the polynomial, determined by the highest non-zero coefficient.
        """
        return len(self.coefficients) - 1

    def __str__(self):
        """
        Returns a string representation of the polynomial in a human-readable format.

        Returns:
            str: The polynomial as a formatted string, e.g., "3x^2 + 2x + 1".
        """
        terms = []
        for i in range(len(self.coefficients) - 1, -1, -1):
            coeff = self.coefficients[i]
            if coeff == 0:
                continue
            if i == 0:
                terms.append(f"{abs(coeff)}")
            elif i == 1 and abs(coeff) == 1:
                terms.append("x")
            elif i == 1:
                terms.append(f"{abs(coeff)}x")
            elif abs(coeff) == 1:
                terms.append(f"x^{i}")
            else:
                terms.append(f"{abs(coeff)}x^{i}")
        if coeff > 0:
            return " + ".join(terms) if terms else "0"
        else:
            return " - ".join(terms) if terms else "0"

    def __call__(self, x):
        """
        Evaluates the polynomial at a given value of x.

        Parameters:
            x (float or int): The value at which to evaluate the polynomial.

        Returns:
            float: The result of the polynomial evaluated at x.
        """
        return sum([self.coefficients[i] * x**i for i in range(len(self.coefficients))])

    def __add__(self, other):
        """
        Adds two polynomials and returns the result as a new Polynomial instance.

        Parameters:
            other (Polynomial): The polynomial to add.

        Returns:
            Polynomial: A new Polynomial representing the sum.
        """
        max_deg = max(self.degree(), other.degree())
        new_coeffs = [
            (self.coefficients[i] if i < len(self.coefficients) else 0) +
            (other.coefficients[i] if i < len(other.coefficients) else 0)
            for i in range(max_deg + 1)
        ]
        return Polynomial(new_coeffs)

    def __sub__(self, other):
        """
        Subtracts another polynomial and returns the result as a new Polynomial instance.

        Parameters:
            other (Polynomial): The polynomial to subtract.

        Returns:
            Polynomial: A new Polynomial representing the difference.
        """
        max_deg = max(self.degree(), other.degree())
        new_coeffs = [
            (self.coefficients[i] if i < len(self.coefficients) else 0) -
            (other.coefficients[i] if i < len(other.coefficients) else 0)
            for i in range(max_deg + 1)
        ]
        return Polynomial(new_coeffs)

    def __mul__(self, other):
        """
        Multiplies two polynomials and returns the result as a new Polynomial instance.

        Parameters:
            other (Polynomial): The polynomial to multiply.

        Returns:
            Polynomial: A new Polynomial representing the product.
        """
        new_coeffs = [0] * (self.degree() + other.degree() + 1)
        for i in range(len(self.coefficients)):
            for j in range(len(other.coefficients)):
                new_coeffs[i + j] += self.coefficients[i] * other.coefficients[j]
        return Polynomial(new_coeffs)

    def __iadd__(self, other):
        """
        In-place addition of another polynomial.

        Parameters:
            other (Polynomial): The polynomial to add.

        Returns:
            Polynomial: The current instance after addition.
        """
        result = self + other
        self.coefficients = result.coefficients
        return self

    def __isub__(self, other):
        """
        In-place subtraction of another polynomial.

        Parameters:
            other (Polynomial): The polynomial to subtract.

        Returns:
            Polynomial: The current instance after subtraction.
        """
        result = self - other
        self.coefficients = result.coefficients
        return self

    def __imul__(self, other):
        """
        In-place multiplication by another polynomial.

        Parameters:
            other (Polynomial): The polynomial to multiply.

        Returns:
            Polynomial: The current instance after multiplication.
        """
        result = self * other
        self.coefficients = result.coefficients
        return self