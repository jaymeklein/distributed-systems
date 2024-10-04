import multiprocessing
from tqdm import tqdm  # Biblioteca para estimar tempo de iterações de um loop.
import numpy as np


def load_matrix(filename: str) -> list[list[float]]:
    with open(filename, "r") as f:
        matrix = []

        for line in f:
            row = list(map(float, line.strip().split()))
            matrix.append(row)

    return matrix


def multiply_row_by_matrix(row: list[float], matB: list[list[float]]) -> list[float]:
    result_row = []
    for j in range(len(matB[0])):
        element_sum = 0

        for k in range(len(row)):
            element_sum += row[k] * matB[k][j]

        result_row.append(element_sum)

    return result_row


def numpy_multiply_row_by_matrix(row: np.ndarray, matB: np.ndarray) -> np.ndarray:
    return np.dot(row, matB)


def matrix_multiply_worker(
    matA: list[list[float]],
    matB: list[list[float]],
    rows_range: tuple[int, int],
    output: list[list[float]],
    index: int,
    use_numpy: bool,
):
    partial_result = []
    for i in tqdm(range(*rows_range), desc=f"Processador {index}"):
        row = matA[i]
        if use_numpy:
            partial_result.append(
                numpy_multiply_row_by_matrix(np.array(row), np.array(matB))
            )
        else:
            partial_result.append(multiply_row_by_matrix(row, matB))

    output[index] = partial_result


def parallel_matrix_multiply(
    matA: list[list[float]], matB: list[list[float]], num_workers: int, use_numpy: bool
):
    print("Multiplicando matrizes.")
    manager = multiprocessing.Manager()
    output = manager.dict()

    rows_per_worker = len(matA) // num_workers
    processes = []

    for i in range(num_workers):
        start_row = i * rows_per_worker
        if i == num_workers - 1:
            end_row = len(matA)
        else:
            end_row = (i + 1) * rows_per_worker

        process = multiprocessing.Process(
            target=matrix_multiply_worker,
            args=(matA, matB, (start_row, end_row), output, i, use_numpy),
        )
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    result = []
    for i in range(num_workers):
        result.extend(output[i])

    return result


def print_matrix(matrix: list[list[float]]):
    for row in matrix:
        print("\t".join(map(str, row)))


if __name__ == "__main__":
    matA = load_matrix(r"C:/Users/jayme/Downloads/matA_B/matA.txt")
    matB = load_matrix(r"C:/Users/jayme/Downloads/matA_B/matB.txt")

    if len(matA[0]) != len(matB):
        raise ValueError(
            "As matrizes não podem ser multiplicadas. O número de colunas de A deve ser igual ao número de linhas de B."
        )

    num_workers = multiprocessing.cpu_count()  # Aumente por sua conta e risco.
    use_numpy: bool = True

    print(f"Multiplicando matrizes usando {num_workers} processadores lógicos.")

    result = parallel_matrix_multiply(matA, matB, num_workers, use_numpy)

    print("Resultado da multiplicação de matrizes:")
    print_matrix(result)
