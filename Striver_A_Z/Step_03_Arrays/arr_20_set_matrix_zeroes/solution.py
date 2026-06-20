# Time Complexity: O(N^2) or worse
# Space Complexity: O(N) or O(1)
# Explanation: Brute Force: Standard unoptimized approach. (TODO: Implement specific logic)

# TODO: Implement Brute Force
def setZeroes(matrix: List[List[int]]) -> None:
    n, m, col0 = len(matrix), len(matrix[0]), 1
    for i in range(n):
        if matrix[i][0] == 0: col0 = 0
        for j in range(1, m):
            if matrix[i][j] == 0: matrix[i][0] = matrix[0][j] = 0
    for i in range(n-1, -1, -1):
        for j in range(m-1, 0, -1):
            if matrix[i][0] == 0 or matrix[0][j] == 0: matrix[i][j] = 0
        if col0 == 0: matrix[i][0] = 0

# Time Complexity: O(N * M)
# Space Complexity: O(1)
# Explanation: Optimal: Use the first row and first column as marker arrays to save space. We need a separate variable for the first column (or row) to avoid overlapping states.

def setZeroes(matrix: List[List[int]]) -> None:
    n, m, col0 = len(matrix), len(matrix[0]), 1
    for i in range(n):
        if matrix[i][0] == 0: col0 = 0
        for j in range(1, m):
            if matrix[i][j] == 0: matrix[i][0] = matrix[0][j] = 0
    for i in range(n-1, -1, -1):
        for j in range(m-1, 0, -1):
            if matrix[i][0] == 0 or matrix[0][j] == 0: matrix[i][j] = 0
        if col0 == 0: matrix[i][0] = 0

