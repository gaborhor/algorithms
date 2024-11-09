
def printMatrix(m):
    for row in m:
        print(row)

def matrixMult(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        print("Invalid matrix dimensions for multiplication")
        return None

    elif cols_A == rows_B:
        new_matrix = [[None for i in range(cols_B)] for j in range(rows_A)]

        for i in range(rows_A):
            for j in range(cols_B):
                new_val = 0

                for x in range(cols_A):
                    print(A[i][x], B[x][j])
                    new_val += A[i][x] * B[x][j]
                print(f"---\n{new_val}\n---")

                new_matrix[i][j] = new_val

        print(new_matrix)
        return new_matrix


# Testing code

# # Test1
# A = [[2, -3, 3],
#      [-2, 6, 5],
#      [4, 7, 8]]
# B = [[-1, 9, 1],
#      [0, 6, 5],
#      [3, 4, 7]]
# C = matrixMult(A, B)
# if not C == None:
#     printMatrix(C)

# # Test2
# A = [[ 2, -3, 3, 0],
#     [-2, 6, 5, 1],
#     [ 4, 7, 8, 2]]
# B = [[-1, 9, 1],
#     [ 0, 6, 5],
#     [ 3, 4, 7]]
# C = matrixMult(A, B)
# if not C == None:
#     printMatrix(C)

# # Test3
# A = [[ 2, -3, 3, 5],
#     [-2, 6, 5, -2]]
# B = [[-1, 9, 1],
#     [ 0, 6, 5],
#     [ 3, 4, 7],
#     [ 1, 2, 3]]
# C = matrixMult(A, B)
# if not C == None:
#     printMatrix(C)


