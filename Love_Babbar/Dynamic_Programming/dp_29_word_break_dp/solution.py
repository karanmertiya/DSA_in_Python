# Time Complexity: O(N^2 * max_word_length)
# Space Complexity: O(N)
# Explanation: `dp[i]` is true if `s[0..i-1]` can be segmented. For each `i`, iterate `j` from 0 to `i-1`. If `dp[j]` is true and `s[j..i-1]` is in dict, then `dp[i] = true`.

def wordBreak(s: str, wordDict: List[str]) -> bool:
    word_set = set(wordDict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(i - 1, -1, -1):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[n]

