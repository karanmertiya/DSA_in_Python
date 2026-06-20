# Time Complexity: O(N^2) or worse
# Space Complexity: O(N) or O(1)
# Explanation: Brute Force: Standard unoptimized approach. (TODO: Implement specific logic)

# TODO: Implement Brute Force
import bisect
def findMedian(A: List[List[int]]) -> int:
    low, high = 1, int(1e9)
    n, m = len(A), len(A[0])
    while low <= high:
        mid = low + (high - low) // 2
        cnt = sum(bisect.bisect_right(row, mid) for row in A)
        if cnt <= (n * m) // 2:
            low = mid + 1
        else:
            high = mid - 1
    return low

# Time Complexity: O(32 * N log M)
# Space Complexity: O(1)
# Explanation: Optimal: Binary search on the value range `[1, 10^9]`. For a candidate `mid`, count how many numbers are `<= mid` across all rows using `upper_bound`. If count `> (N*M)/2`, `mid` could be median, search lower. Else search higher.

import bisect
def findMedian(A: List[List[int]]) -> int:
    low, high = 1, int(1e9)
    n, m = len(A), len(A[0])
    while low <= high:
        mid = low + (high - low) // 2
        cnt = sum(bisect.bisect_right(row, mid) for row in A)
        if cnt <= (n * m) // 2:
            low = mid + 1
        else:
            high = mid - 1
    return low

