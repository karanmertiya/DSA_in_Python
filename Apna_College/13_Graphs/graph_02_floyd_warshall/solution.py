# Time Complexity: O(V^3)
# Space Complexity: O(1) in-place
# Explanation: Multi-source shortest path. Try to go from i to j via every possible vertex k. Update `matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])`.

def shortest_distance(matrix: List[List[int]]) -> None:
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == -1: matrix[i][j] = int(1e9)
            if i == j: matrix[i][j] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matrix[i][k] != int(1e9) and matrix[k][j] != int(1e9):
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == int(1e9): matrix[i][j] = -1

