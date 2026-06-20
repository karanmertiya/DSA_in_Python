# Time Complexity: O(N^2)
# Space Complexity: O(N)
# Explanation: Similar to minimum path sum, but we can fall diagonally. Space optimize by using previous row.

def minFallingPathSum(matrix: List[List[int]]) -> int:
    n = len(matrix)
    prev = matrix[0][:]
    for i in range(1, n):
        cur = [0] * n
        for j in range(n):
            up = matrix[i][j] + prev[j]
            ld = matrix[i][j] + (prev[j-1] if j > 0 else float('inf'))
            rd = matrix[i][j] + (prev[j+1] if j < n-1 else float('inf'))
            cur[j] = min(up, ld, rd)
        prev = cur
    return min(prev)

