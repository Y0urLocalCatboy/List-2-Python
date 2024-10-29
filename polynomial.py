class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients
    def degree(self):
        return len(self.coefficients) - 1
    def __str__(self):
        return ' + '.join([f'{self.coefficients[i]}x^{i}' for i in range(len(self.coefficients))])
    def __call__(self, x):
        return sum([self.coefficients[i] * x**i for i in range(len(self.coefficients))])
    def addition(self, other):
        return Polynomial([self.coefficients[i] + other.coefficients[i] for i in range(max(self.degree(), other.degree()) + 1)])
    def subtraction(self, other):
        return Polynomial([self.coefficients[i] - other.coefficients[i] for i in range(max(self.degree(), other.degree()) + 1)])
    def multiplication(self, other):
        return Polynomial([sum([self.coefficients[j] * other.coefficients[i-j] for j in range(i+1)]) for i in range(self.degree() + other.degree() + 1)])