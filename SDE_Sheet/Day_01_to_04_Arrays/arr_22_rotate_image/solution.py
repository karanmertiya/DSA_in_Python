# Time Complexity: O(N^2)
# Space Complexity: O(1)
# Explanation: Optimal: Transpose the matrix (swap matrix[i][j] with matrix[j][i]), then reverse every row.

def rotate(matrix: List[List[int]]) -> None:
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()

