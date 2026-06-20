# Time Complexity: O(N^2)
# Space Complexity: O(N)
# Explanation: Use `dp[i]` to indicate if `A[0..i]` can be segmented. For each `i`, check all prefixes `A[0..j]`. If `dp[j]` is true and `A[j..i]` is in the dictionary, then `dp[i]` is true.

def wordBreak(A, B):
    word_set = set(B)
    n = len(A)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and A[j:i] in word_set:
                dp[i] = True
                break
    return 1 if dp[n] else 0

