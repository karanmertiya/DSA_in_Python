# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Row N has length 2^(N-1). The first half of row N is exactly same as row N-1. The second half of row N is the complement of row N-1. If k is in the first half (k <= mid), return solve(N-1, k). If k is in the second half, return !solve(N-1, k - mid).

def kthGrammar(n: int, k: int) -> int:
    if n == 1 and k == 1: return 0
    mid = 2 ** (n - 2)
    if k <= mid:
        return kthGrammar(n - 1, k)
    else:
        return 1 - kthGrammar(n - 1, k - mid)

