# Time Complexity: O(N^3)
# Space Complexity: O(N^2)
# Explanation: Partition DP. Try partitioning the matrices at every possible split `k` between `i` and `j`. Cost is `arr[i-1]*arr[k]*arr[j]`. Take the minimum.

def matrixMultiplication(N: int, arr: List[int]) -> int:
    dp = [[-1] * N for _ in range(N)]
    def f(i, j):
        if i == j: return 0
        if dp[i][j] != -1: return dp[i][j]
        mini = int(1e9)
        for k in range(i, j):
            steps = arr[i-1] * arr[k] * arr[j] + f(i, k) + f(k+1, j)
            mini = min(mini, steps)
        dp[i][j] = mini
        return mini
    return f(1, N-1)

