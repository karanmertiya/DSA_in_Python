# Time Complexity: O(N^2)
# Space Complexity: O(N^2)
# Explanation: Create a `dp` array where `dp[i]` is min cuts for `str[0..i]`. Also use a 2D boolean DP to check if `str[j..i]` is a palindrome. If it is, `dp[i] = min(dp[i], dp[j-1] + 1)`.

def palindromicPartition(string: str) -> int:
    n = len(string)
    isPal = [[False] * n for _ in range(n)]
    dp = [0] * n
    for i in range(n):
        minCut = i
        for j in range(i + 1):
            if string[i] == string[j] and (i - j < 2 or isPal[j+1][i-1]):
                isPal[j][i] = True
                if j == 0:
                    minCut = 0
                else:
                    minCut = min(minCut, dp[j-1] + 1)
        dp[i] = minCut
    return dp[-1]

