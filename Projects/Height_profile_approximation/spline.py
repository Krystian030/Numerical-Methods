from matrix import *
COEFFICIENTS_NUMBER = 4

# n + 1 => liczba węzłów
# n => liczba przedziałów
# equations_number => liczba równań
def spline(data):
    # data = [(1, 6), (3, -2), (5, 4)]
    n = len(data) - 1
    equations_number = n * 4
    coefficients_number = 4
    matrix = [[0 for x in range(equations_number)] for y in range(equations_number)]
    b = [0 for x in range(equations_number)]

    # Tworzenie macierzy do interpolacji funkcjami sklejanymi
    for j in range(0, n):

        h = data[j+1][0] - data[j][0]
        # 1) S_j(x_j) = f(x_j) =>
        #    a_j + b_j(x - x_j) + c_j(x - x_j)^2 + d_j(x - x_j)^3 =
        #    = a_j + b_j(x_j - x_j) + c_j(x_j - x_j)^2 + d_j(x_j - x_j)^3 = a_j
        matrix[coefficients_number * j][coefficients_number * j] = 1
        b[4 * j] = data[j][1]

        # 2) S_(j)(x_{j+1}) = f(x_{j+1})
        # współczynnik i
        for i in range(coefficients_number):
            matrix[coefficients_number * j + 1][coefficients_number * j + i] = h**i
            b[coefficients_number * j + 1] = data[j+1][1]

        # 3) S'_{j-1}(x_j) = S'_{j}(x_j) =>
        # S'_{j-1}(x_j) = b_{j-1} + 2c_{j-1}(x_j - x_{j-1} + 3d_{j-1}(x_j - x_{j-1})^2
        # S'_{j-1}(x_j) = b_{j} => S'_{j-1}(x_j) - b_{j} = 0
        if j > 0:
            for i in range(coefficients_number):
                if i == 0:
                    matrix[coefficients_number * (j - 1) + 2][i + coefficients_number * (j - 1)] = i
                else:
                    matrix[coefficients_number * (j - 1) + 2][i + coefficients_number * (j - 1)] = i * h**(i-1)
            matrix[coefficients_number * (j - 1) + 2][1 + coefficients_number * j] = -1

        # 4) S''_{j-1}(x_j) = S''_{j}(x_j) =>
        # S''_{j-1}(x_j) = 2c_{j-1} + 6d_{j-1} * (x_j - x_{j-1})
        # S''_{j-1}(x_j) = 2c_{j} => S''_{j-1}(x_j) - 2*c_{j} = 0
        if j > 0:
            matrix[coefficients_number * (j - 1) + 3][coefficients_number * (j - 1) + 2] = 2
            matrix[coefficients_number * (j - 1) + 3][coefficients_number * (j - 1) + 3] = 6 * h
            matrix[coefficients_number * (j - 1) + 3][coefficients_number * j + 2] = -2

        # 5) 2 ostatnie równania:
        # S''_{0}(x_0) = 0 and S''_{n-1}(x_n) = 0
        #  S''_{0}(x_0) = 0 => c_0 = 0
        #  S''_{n-1}(x_n) = 0 => 2 * c_(n-1) +
        if j == n-2:
            matrix[equations_number - 2][2] = 2
        if j == n-1:
            matrix[equations_number - 1][-2] = 2
            matrix[equations_number - 1][-1] = 6 * h

    coefficients = LU_factorization(matrix, b)
    return coefficients


def spline_calc(x, coefficients_number, coefficients, data):
    for i in range(len(data)-1):
        result = 0
        if data[i][0] <= x <= data[i+1][0]:
            for j in range(coefficients_number):
                h = x - data[i][0]
                result += coefficients[4 * i + j] * h**j
            break
    return result


def spline_interpolation(step, data_interpolation):
    input_nodes = data_interpolation[::step]    # węzły użyte do interpolacji
    result = []
    coefficients = spline(input_nodes)
    for x in range(0, input_nodes[-1][0] + 1):
        height = spline_calc(x, COEFFICIENTS_NUMBER, coefficients, input_nodes)
        result.append((x, height))
    return result, input_nodes
