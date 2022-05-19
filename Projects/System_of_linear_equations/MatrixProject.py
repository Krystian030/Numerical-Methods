import copy
import math
import time


class MatrixProject:

    # N = 9cd
    # e - 4 cyfra nr indeksu
    # f - 3 cyfra nr indeksu
    # c - przedostatnia cyfra nr indeksu
    # d - ostatnia cyfra nr indeksu
    # indeks: 184589 -> N = 989
    def __init__(self, indexNumber):
        self.c = indexNumber % 100 // 10
        self.d = indexNumber % 10
        self.e = indexNumber % 1000 // 100
        self.f = indexNumber % 10_000 // 1000
        self.N = 9 * 100 + self.c * 10 + self.d * 1
        self.matrix = [[0 for x in range(self.N)] for y in range(self.N)]
        self.b = [0 for x in range(self.N)]
        self.time_jacobi = []
        self.time_gauss_seidel = []
        self.time_LU_factorization = []
        self.iterations_jacobi = []
        self.iterations_gauss_seidel = []
        self.iterations_LU_factorization = []
        self.jacobi_residual = []
        self.gauss_seidel_residual = []
        self.LU_factorization_residual = []

    def createVectorB(self):
        for j in range(self.N):
            n = math.sin(j * (self.f + 1))
            self.b[j] = n

    def createBandMatrix(self, a1, a2, a3):

        for i in range(self.N):
            if i < len(self.matrix) - 1:
                # 1th lower diagonal
                self.matrix[i + 1][i] = a2
                # 2nd lower diagonal
                if i < self.N - 2:
                    self.matrix[i + 2][i] = a3

            if i > 0:
                # 1th upper diagonal
                self.matrix[i - 1][i] = a2
                # 2nd upper diagonal
                if i > 1:
                    self.matrix[i - 2][i] = a3
            # main diagonal
            for j in range(self.N):
                if i == j:
                    self.matrix[i][j] = a1

    def createBandSizeMatrix(self, a1, a2, a3, N):
        self.N = N
        self.matrix = [[0 for x in range(self.N)] for y in range(self.N)]
        self.b = [0 for x in range(self.N)]
        self.createVectorB()
        for i in range(self.N):
            if i < len(self.matrix) - 1:
                # 1th lower diagonal
                self.matrix[i + 1][i] = a2
                # 2nd lower diagonal
                if i < self.N - 2:
                    self.matrix[i + 2][i] = a3

            if i > 0:
                # 1th upper diagonal
                self.matrix[i - 1][i] = a2
                # 2nd upper diagonal
                if i > 1:
                    self.matrix[i - 2][i] = a3
            # main diagonal
            for j in range(self.N):
                if i == j:
                    self.matrix[i][j] = a1

    @staticmethod
    def multiplyMatrixVector(matrix1, vector):
        # can't multiply matrix with different size
        if len(matrix1) != len(vector):
            return 0
        newVector = [0 for x in range(len(matrix1))]
        for i in range(len(newVector)):
            for j in range(len(newVector)):
                newVector[i] += matrix1[i][j] * vector[j]
        return newVector

    def calc_residual(self, matrix, r, b):
        newVector = self.multiplyMatrixVector(matrix, r)
        for i in range(len(newVector)):
            newVector[i] -= b[i]
        return newVector

    def jacobi_method(self):
        r = [1 for x in range(len(self.matrix))]
        r_prev = copy.deepcopy(r)
        norm_res = self.norm(self.calc_residual(self.matrix, r, self.b))

        iteration = 0
        val = 10 ** (-9)
        residual = []
        start = time.time()
        while val < norm_res < 10e9:
            residual.append(norm_res)
            for i in range(len(r)):
                tmp_sum = 0
                for j in range(len(r)):
                    if i != j:
                        tmp_sum += self.matrix[i][j]*r_prev[j]
                r[i] = (self.b[i] - tmp_sum)/self.matrix[i][i]
            r_prev = copy.deepcopy(r)
            iteration += 1
            norm_res = self.norm(self.calc_residual(self.matrix, r, self.b))
        end = time.time()
        timeString = str(end - start) + " [s]"
        normBiggerThan = "Bigger than " + str(norm_res)
        self.time_jacobi.append(end-start)
        self.iterations_jacobi.append(iteration)
        self.jacobi_residual.append(residual)
        print(f"|=============== Jacobi Method ===============|")
        print(f"|-> Time: {timeString}")
        print(f"|-> Iteration: {iteration}")
        print(f"|-> Residuum: {norm_res if (norm_res < 10e9) else normBiggerThan}")

    def gauss_method(self):
        r = [1 for x in range(len(self.matrix))]
        r_prev = copy.deepcopy(r)
        norm_res = self.norm(self.calc_residual(self.matrix, r, self.b))

        iteration = 0
        val = 10 ** (-9)

        start = time.time()
        residual = []
        while val < norm_res < 10e9:
            residual.append(norm_res)
            for i in range(len(r)):
                tmp1 = 0
                tmp2 = 0
                for j in range(len(r)):
                    if i > j:
                        tmp1 += self.matrix[i][j] * r[j]
                    if j > i:
                        tmp2 += self.matrix[i][j] * r_prev[j]
                r[i] = (self.b[i] - tmp1 - tmp2) / self.matrix[i][i]
            r_prev = copy.deepcopy(r)
            iteration += 1
            norm_res = self.norm(self.calc_residual(self.matrix, r, self.b))
        end = time.time()
        timeString = str(end - start) + " [s]"
        normBiggerThan = "Bigger than " + str(norm_res)
        self.time_gauss_seidel.append(end-start)
        self.iterations_gauss_seidel.append(iteration)
        self.gauss_seidel_residual.append(residual)
        print(f"|=============== Gauss-Seidel Method ===============|")
        print(f"|-> Time: {timeString}")
        print(f"|-> Iteration: {iteration}")
        print(f"|-> Residuum: {norm_res if (norm_res < 10e9) else normBiggerThan}")

    def LU_factorization(self):
        start = time.time()

        U, L = create_LU(self.matrix, self.N)

        # podstawienie w przód (forward-substitution)
        y = [0 for y in range(len(U))]
        for i in range(len(y)):
            tmp = 0
            for k in range(i):
                tmp += L[i][k] * y[k]
            y[i] = (self.b[i] - tmp)/L[i][i]

        for i in y:
            print(i, end=" ")
        print()

        # podstawienie wstecz (back-substitution)
        x = [0 for x in range(len(U))]
        for i in reversed(range(len(x))):
            tmp = 0
            for k in range(i+1, len(x)):
                tmp = tmp + U[i][k]*x[k]
            x[i] = (y[i] - tmp)/U[i][i]
        end = time.time()

        for i in x:
            print(i, end=" ")
        print()
        timeString = str(end - start) + " [s]"

        norm_res = self.norm(self.calc_residual(self.matrix, x, self.b))
        self.time_LU_factorization.append(end-start)
        self.LU_factorization_residual.append(norm_res)
        print(f"|=============== Faktoryzacja LU ===============|")
        print(f"|-> Time: {timeString}")
        print(f"|-> Residuum: {norm_res}")

    @staticmethod
    def norm(vector):
        norm_res = 0
        for i in range(len(vector)):
            norm_res += vector[i] ** 2
        return math.sqrt(norm_res)

    @staticmethod
    def printMatrix(matrix):
        for i in range(len(matrix)):
            print("[", end="\t")
            for j in range(len(matrix[i])):
                print(str(matrix[i][j]), end="\t\t")
            print("]")


def create_LU(matrix, N):
    U = copy.deepcopy(matrix)
    L = create_unit_matrix(N)
    for k in range(N - 1):
        for j in range(k + 1, N):
            L[j][k] = U[j][k] / U[k][k]
            for m in range(k, N):
                U[j][m] -= L[j][k] * U[k][m]
    return U, L


def create_unit_matrix(N):
    unit = [[0 for x in range(N)] for y in range(N)]
    for i in range(N):
        unit[i][i] = 1.0
    return unit