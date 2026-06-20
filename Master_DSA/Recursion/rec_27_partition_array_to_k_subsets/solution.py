# Time Complexity: O(K * 2^N)
# Space Complexity: O(N)
# Explanation: If total sum is not divisible by K, return false. Sort array in descending order. Use a boolean array `vis`. Helper function `solve(ind, currentSum, k)`: if `k == 1` return true. If `currentSum == target`, `solve(0, 0, k-1)`. Otherwise, iterate from `ind` to `N`, if `!vis[i]` and `currentSum + arr[i] <= target`, mark `vis[i] = true`, recurse, unmark.

def isKPartitionPossible(a: List[int], n: int, k: int) -> bool:
    total = sum(a)
    if total % k != 0 or n < k: return False
    target = total // k
    vis = [False] * n
    def solve(ind, currSum, k):
        if k == 1: return True
        if currSum == target: return solve(0, 0, k - 1)
        for i in range(ind, n):
            if not vis[i] and currSum + a[i] <= target:
                vis[i] = True
                if solve(i + 1, currSum + a[i], k): return True
                vis[i] = False
        return False
    return solve(0, 0, k)

