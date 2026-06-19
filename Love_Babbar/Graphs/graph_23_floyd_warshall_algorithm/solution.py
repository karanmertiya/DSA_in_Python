# Time Complexity: O(V^3)
# Space Complexity: O(V^2) or O(1) if in-place
# Explanation: Iterate `k` (via node) from 0 to V-1. Iterate `i` and `j`. `matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])`. If `matrix[i][i] < 0`, negative cycle exists.

def shortest_distance(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == -1: matrix[i][j] = float('inf')
            if i == j: matrix[i][j] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == float('inf'): matrix[i][j] = -1

