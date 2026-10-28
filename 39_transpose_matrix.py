"""Program 39: Transpose a matrix."""


def transpose_matrix(matrix):
    if not matrix:
        return []

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("All rows must have the same length")

    return [list(row) for row in zip(*matrix)]


if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    matrix = []

    for i in range(rows):
        row = list(map(
            int,
            input(f"Enter row {i + 1} values separated by spaces: ").split()
        ))
        matrix.append(row)

    print("Transposed matrix:")
    for row in transpose_matrix(matrix):
        print(row)