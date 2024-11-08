class Polynomial:
    def __init__(self, coefficients):
        while len(coefficients) > 1 and coefficients[-1] == 0:
            coefficients.pop()
        self.coefficients = coefficients[::-1]
    def degree(self):
        return len(self.coefficients) - 1

    def __str__(self):
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
        return sum([self.coefficients[i] * x**i for i in range(len(self.coefficients))])

    def __add__(self, other):
        max_deg = max(self.degree(), other.degree())
        new_coeffs = [
            (self.coefficients[i] if i < len(self.coefficients) else 0) +
            (other.coefficients[i] if i < len(other.coefficients) else 0)
            for i in range(max_deg + 1)
        ]
        return Polynomial(new_coeffs)
    def __sub__(self, other):
        max_deg = max(self.degree(), other.degree())
        new_coeffs = [
            (self.coefficients[i] if i < len(self.coefficients) else 0) -
            (other.coefficients[i] if i < len(other.coefficients) else 0)
            for i in range(max_deg + 1)
        ]
        return Polynomial(new_coeffs)
    def __mul__(self, other):
        new_coeffs = [0] * (self.degree() + other.degree() + 1)
        for i in range(len(self.coefficients)):
            for j in range(len(other.coefficients)):
                new_coeffs[i + j] += self.coefficients[i] * other.coefficients[j]
        return Polynomial(new_coeffs)
    def __iadd__(self, other):
        result = self + other
        self.coefficients = result.coefficients
        return self
    def __isub__(self, other):
        result = self - other
        self.coefficients = result.coefficients
        return self
    def __imul__(self, other):
        result = self * other
        self.coefficients = result.coefficients
        return self

