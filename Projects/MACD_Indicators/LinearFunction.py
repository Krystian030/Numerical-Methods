import numpy


# y = ax + b
class LinearFunction:

    def __init__(self, A, B):
        self.x = (A[0], B[0])
        self.y = (A[1], B[1])
        coefficients = numpy.polyfit(self.x, self.y, 1)
        self.a = coefficients[0]
        self.b = coefficients[1]

    # funkcja obliczająca punkty przecięcia
    def intersection(self, y):
        A = numpy.array([[self.a, -1], [y.a, -1]])
        B = numpy.array([-self.b, -y.b])
        X = numpy.linalg.solve(A, B)
        return X

    # funkcja sprawdzająca czy punkt przecięcia znajduje się w dziedzinie
    def isIntersectInRange(self, y):
        X = self.intersection(y)
        if self.x[0] <= X[0] <= self.x[1]:
            return True
        else:
            return False

    # funkcja sprawdzająca czy funkcja jest większa
    def isUpper(self, y):
        x = self.x[0]
        xy = y.x[0]
        if self.y[0] > y.y[0]:
            return True
        else:
            return False

    def __str__(self):
        return "Function: y = " + str(self.a) + "x + " + str(self.b)
