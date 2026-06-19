# Time Complexity: O(N * M * L) or O(N^2)
# Space Complexity: O(N)
# Explanation: `dp[i]` is true if `s[0..i-1]` can be segmented. For each `i` from 1 to `N`, try each word in dictionary. If `s[i-len(word)..i-1] == word` and `dp[i-len(word)]` is true, then `dp[i] = true`. Or iterate `j` from 0 to `i` and check if `dp[j]` is true and `s[j..i-1]` is in dict.

def wordBreak(s: str, wordDict: List[str]) -> bool:
    dict_set = set(wordDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in dict_set:
                dp[i] = True
                break
    return dp[len(s)]

