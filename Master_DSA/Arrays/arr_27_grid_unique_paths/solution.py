# Time Complexity: O(m-1)
# Space Complexity: O(1)
# Explanation: Combinatorics approach. The total number of steps to reach the bottom-right corner is (m - 1) + (n - 1) = m + n - 2. Out of these steps, we need to choose (m - 1) downward steps (or n - 1 rightward steps). The number of paths is (m + n - 2) C (m - 1).

def uniquePaths(m: int, n: int) -> int:
    N = n + m - 2
    r = m - 1
    res = 1
    for i in range(1, r + 1):
        res = res * (N - r + i) // i
    return res

