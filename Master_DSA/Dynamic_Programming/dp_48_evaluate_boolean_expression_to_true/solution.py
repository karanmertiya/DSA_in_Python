# Time Complexity: O(N^3)
# Space Complexity: O(N^2 * 2)
# Explanation: `dp[i][j][isTrue]` is number of ways to evaluate substring `i..j` to boolean `isTrue`. Iterate `k` from `i+1` to `j-1` with step 2 (k is operator). Combine left (`i..k-1`) and right (`k+1..j`) results based on the operator.

def countWays(n: int, s: str) -> int:
    dp = [[[0, 0] for _ in range(n)] for _ in range(n)]
    for i in range(0, n, 2):
        if s[i] == 'T': dp[i][i][1] = 1
        else: dp[i][i][0] = 1
    for length in range(3, n + 1, 2):
        for i in range(0, n - length + 1, 2):
            j = i + length - 1
            for k in range(i + 1, j, 2):
                lT, lF = dp[i][k-1][1], dp[i][k-1][0]
                rT, rF = dp[k+1][j][1], dp[k+1][j][0]
                if s[k] == '&':
                    dp[i][j][1] = (dp[i][j][1] + lT * rT) % 1003
                    dp[i][j][0] = (dp[i][j][0] + lF * rT + lT * rF + lF * rF) % 1003
                elif s[k] == '|':
                    dp[i][j][1] = (dp[i][j][1] + lT * rT + lF * rT + lT * rF) % 1003
                    dp[i][j][0] = (dp[i][j][0] + lF * rF) % 1003
                elif s[k] == '^':
                    dp[i][j][1] = (dp[i][j][1] + lT * rF + lF * rT) % 1003
                    dp[i][j][0] = (dp[i][j][0] + lT * rT + lF * rF) % 1003
    return dp[0][n-1][1]

