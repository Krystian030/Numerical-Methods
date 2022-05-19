from MatrixProject import *
import sys
import csv


def write_data(file_name, arr):
    path = "./Files/" + file_name + ".csv"
    with open(path, mode='w', encoding='UTF8', newline='') as csvFile:
        try:
            writer = csv.writer(csvFile)
            for i in range(len(arr)):
                writer.writerow([arr[i]])
        except csv.Error as e:
            sys.exit(e)


if __name__ == '__main__':
    # Zadanie A
    matrix = MatrixProject(184589)
    matrix.createVectorB()
    matrix.createBandMatrix(matrix.e + 5, -1, -1)

    # Zadanie B
    matrix.jacobi_method()
    matrix.gauss_method()

    # Zadanie C
    matrix.createBandMatrix(3, -1, -1)
    matrix.jacobi_method()
    matrix.gauss_method()

    # Zadanie D
    matrix.LU_factorization()

    # Zadanie E
    N = [100, 500, 1000, 2000, 3000]
    write_data("SIZE", N)
    for size in N:
        print(f"|======================== Matrix[{size}][{size}] ========================|")
        matrix.createBandSizeMatrix(matrix.e + 5, -1, -1, size)
        matrix.jacobi_method()
        matrix.gauss_method()
        matrix.LU_factorization()
        print()

    write_data("JACOBI_TIME", matrix.time_jacobi)
    write_data("JACOBI_ITERATION", matrix.iterations_jacobi)
    write_data("GAUSS_SEIDEL_TIME", matrix.time_gauss_seidel)
    write_data("GAUSS_SEIDEL_ITERATION", matrix.iterations_gauss_seidel)
    write_data("FACTORIZATION_TIME", matrix.time_LU_factorization)
    write_data("FACTORIZATION_RESIDUAL", matrix.LU_factorization_residual)
    for i in range(len(N)):
        write_data("JACOBI_RESIDUAL_" + str(N[i]), matrix.jacobi_residual[i])
        write_data("GAUSS_SEIDEL_RESIDUAL_" + str(N[i]), matrix.gauss_seidel_residual[i])
