# Time Complexity: O(N^3)
# Space Complexity: O(N)
# Explanation: 1D DP array. `dp[i]` is true if string up to index `i` can be broken. Loop `i` from 1 to N, loop `j` from 0 to i. If `dp[j]` is true and `s[j...i]` is in dict, then `dp[i] = true`.

def wordBreak(s: str, wordDict: List[str]) -> bool:
    wordSet = set(wordDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordSet:
                dp[i] = True
                break
    return dp[len(s)]

