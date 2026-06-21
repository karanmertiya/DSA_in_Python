# Time Complexity: O(N * M)
# Space Complexity: O(M)
# Explanation: `dp[i][j]` is the length of longest common suffix of `S1[0..i-1]` and `S2[0..j-1]`. If `S1[i-1] == S2[j-1]`, `dp[i][j] = dp[i-1][j-1] + 1`. Else, `dp[i][j] = 0`. Max value in `dp` table is answer.

def longestCommonSubstr(S1: str, S2: str, n: int, m: int) -> int:
    prev = [0] * (m + 1)
    ans = 0
    for i in range(1, n + 1):
        curr = [0] * (m + 1)
        for j in range(1, m + 1):
            if S1[i-1] == S2[j-1]:
                curr[j] = prev[j-1] + 1
                ans = max(ans, curr[j])
            else:
                curr[j] = 0
        prev = curr
    return ans

