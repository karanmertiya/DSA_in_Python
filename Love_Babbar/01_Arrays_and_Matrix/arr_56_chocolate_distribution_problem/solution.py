# Time Complexity: O(N log N)
# Space Complexity: O(1)
# Explanation: Optimal: Sort the array. Find the minimum difference between `A[i+M-1]` and `A[i]` for all possible `i` from `0` to `N-M`.

def findMinDiff(a, n, m):
    a.sort()
    min_diff = float('inf')
    for i in range(n - m + 1):
        diff = a[i + m - 1] - a[i]
        if diff < min_diff:
            min_diff = diff
    return min_diff

