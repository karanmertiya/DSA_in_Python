# Time Complexity: O(N * W)
# Space Complexity: O(W)
# Explanation: 2D DP or 1D array space-optimized DP. Check take and not-take scenarios.

def knapSack(W: int, wt: List[int], val: List[int], n: int) -> int:
    prev = [0] * (W + 1)
    for w in range(wt[0], W + 1): prev[w] = val[0]
    for ind in range(1, n):
        for w in range(W, -1, -1):
            notTake = prev[w]
            take = float('-inf')
            if wt[ind] <= w: take = val[ind] + prev[w - wt[ind]]
            prev[w] = max(take, notTake)
    return prev[W]

