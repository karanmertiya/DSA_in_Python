# Time Complexity: O(N^3)
# Space Complexity: O(N^2)
# Explanation: MCM DP. `dp[i][j][isTrue]` stores the number of ways to evaluate `S[i..j]` to boolean `isTrue`. Iterate length, start, and partition `k`. Calculate T/F ways based on the operator at `k`.

def countWays(N: int, S: str) -> int:
    mod = 1003
    dp = [[[0, 0] for _ in range(N)] for _ in range(N)]
    for i in range(N - 1, -1, -2):
        for j in range(i, N, 2):
            if i == j:
                dp[i][j][1] = 1 if S[i] == 'T' else 0
                dp[i][j][0] = 1 if S[i] == 'F' else 0
                continue
            waysT, waysF = 0, 0
            for k in range(i + 1, j, 2):
                lT, lF = dp[i][k-1][1], dp[i][k-1][0]
                rT, rF = dp[k+1][j][1], dp[k+1][j][0]
                if S[k] == '&':
                    waysT = (waysT + lT * rT) % mod
                    waysF = (waysF + lT * rF + lF * rT + lF * rF) % mod
                elif S[k] == '|':
                    waysT = (waysT + lT * rT + lT * rF + lF * rT) % mod
                    waysF = (waysF + lF * rF) % mod
                elif S[k] == '^':
                    waysT = (waysT + lT * rF + lF * rT) % mod
                    waysF = (waysF + lT * rT + lF * rF) % mod
            dp[i][j][1] = waysT
            dp[i][j][0] = waysF
    return dp[0][N-1][1]

