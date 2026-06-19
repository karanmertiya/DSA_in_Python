# Time Complexity: O(N^3)
# Space Complexity: O(N^2 * 2)
# Explanation: MCM variant. `dp[i][j][isTrue]` stores the number of ways to evaluate the expression from `i` to `j` to `isTrue`. Partition at every operator `k`. Calculate `leftTrue`, `leftFalse`, `rightTrue`, `rightFalse`. Combine these based on the operator `S[k]`.

def countWays(N, S):
    mod = 1003
    dp = [[[-1] * 2 for _ in range(N)] for _ in range(N)]
    def solve(i, j, isTrue):
        if i > j: return 0
        if i == j:
            if isTrue: return 1 if S[i] == 'T' else 0
            else: return 1 if S[i] == 'F' else 0
        if dp[i][j][isTrue] != -1: return dp[i][j][isTrue]
        ways = 0
        for k in range(i + 1, j, 2):
            lT = solve(i, k - 1, 1)
            lF = solve(i, k - 1, 0)
            rT = solve(k + 1, j, 1)
            rF = solve(k + 1, j, 0)
            if S[k] == '&':
                if isTrue: ways = (ways + lT * rT) % mod
                else: ways = (ways + lT * rF + lF * rT + lF * rF) % mod
            elif S[k] == '|':
                if isTrue: ways = (ways + lT * rT + lT * rF + lF * rT) % mod
                else: ways = (ways + lF * rF) % mod
            elif S[k] == '^':
                if isTrue: ways = (ways + lT * rF + lF * rT) % mod
                else: ways = (ways + lT * rT + lF * rF) % mod
        dp[i][j][isTrue] = ways
        return ways
    return solve(0, N - 1, 1)

