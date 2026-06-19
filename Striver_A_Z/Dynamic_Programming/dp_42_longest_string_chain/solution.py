# Time Complexity: O(N log N + N * L^2) where L is max word length
# Space Complexity: O(N * L)
# Explanation: Sort words by length. Use a hash map `dp` to store the longest chain ending at `word`. For each word, try removing one character at a time to form `prev_word`. `dp[word] = max(dp[word], dp[prev_word] + 1)`.

def longestStrChain(words: List[str]) -> int:
    words.sort(key=len)
    dp = {}
    max_len = 1
    for word in words:
        dp[word] = 1
        for i in range(len(word)):
            prev = word[:i] + word[i+1:]
            if prev in dp:
                dp[word] = max(dp[word], dp[prev] + 1)
        max_len = max(max_len, dp[word])
    return max_len

