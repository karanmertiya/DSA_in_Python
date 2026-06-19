# Time Complexity: O(N^3)
# Space Complexity: O(N^2)
# Explanation: Use a 3D DP array `dp[i][j][isTrue]` representing the number of ways to evaluate the substring from `i` to `j` to `isTrue`. Iterate over all possible split points `k` with an operator. Combine the True and False counts from left and right halves based on the operator.

def countWays(N, S):
    dp = [[[0] * 2 for _ in range(N)] for _ in range(N)]
    for i in range(0, N, 2):
        dp[i][i][1] = 1 if S[i] == 'T' else 0
        dp[i][i][0] = 1 if S[i] == 'F' else 0
    for length in range(3, N + 1, 2):
        for i in range(0, N - length + 1, 2):
            j = i + length - 1
            for k in range(i + 1, j, 2):
                lt, lf = dp[i][k-1][1], dp[i][k-1][0]
                rt, rf = dp[k+1][j][1], dp[k+1][j][0]
                if S[k] == '&':
                    dp[i][j][1] = (dp[i][j][1] + lt * rt) % 1003
                    dp[i][j][0] = (dp[i][j][0] + lt * rf + lf * rt + lf * rf) % 1003
                elif S[k] == '|':
                    dp[i][j][1] = (dp[i][j][1] + lt * rt + lt * rf + lf * rt) % 1003
                    dp[i][j][0] = (dp[i][j][0] + lf * rf) % 1003
                elif S[k] == '^':
                    dp[i][j][1] = (dp[i][j][1] + lt * rf + lf * rt) % 1003
                    dp[i][j][0] = (dp[i][j][0] + lt * rt + lf * rf) % 1003
    return dp[0][N-1][1]

