# Time Complexity: O(N^2 * L)
# Space Complexity: O(N)
# Explanation: Use a helper function `solve(index)` that returns true if substring `s[index...]` can be segmented. Try all possible prefixes from `index`. If `s[index...i]` is in dict, recursively call `solve(i+1)`. Use memoization.

def wordBreak(A: str, B: List[str]) -> int:
    word_set = set(B)
    memo = {}
    def solve(ind):
        if ind == len(A): return 1
        if ind in memo: return memo[ind]
        for i in range(ind, len(A)):
            if A[ind:i+1] in word_set:
                if solve(i + 1):
                    memo[ind] = 1
                    return 1
        memo[ind] = 0
        return 0
    return solve(0)

