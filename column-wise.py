prograd assignment problem
You have given a 2D integer matrix A,return a 1D integer array containing column-wise sums of original matrix.

def column_sums(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    sums = [0] * cols

    for j in range(cols):
        for i in range(rows):
            sums[j] += matrix[i][j]

    return sums



matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 2, 3, 4]]
result = column_sums(matrix)
print(result)
