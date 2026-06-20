# Time Complexity: O(N log N)
# Space Complexity: O(1)
# Explanation: Sort array. We want to find the longest subarray `arr[i..j]` such that `arr[j] - arr[i] <= K`. `dp[i]` could store the max `j` for index `i`. Or use Binary Search (`upper_bound`) for each `i` to find the valid `j`, maximizing `j - i + 1`. Total removed = `N - max_length`.

import bisect
def removals(arr: List[int], k: int) -> int:
    n = len(arr)
    arr.sort()
    maxLen = 0
    for i in range(n):
        j = bisect.bisect_right(arr, arr[i] + k) - 1
        maxLen = max(maxLen, j - i + 1)
    return n - maxLen

