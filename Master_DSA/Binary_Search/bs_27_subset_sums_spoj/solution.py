# Time Complexity: O(2^(N/2) * log(2^(N/2)))
# Space Complexity: O(2^(N/2))
# Explanation: Divide the array into two halves. Find all possible subset sums for both halves (`sum1` and `sum2`). Sort `sum2`. For each sum in `sum1`, we need to find the number of elements in `sum2` that satisfy `A - sum <= x <= B - sum`. This can be done using Binary Search (`upper_bound` - `lower_bound`).

import bisect
def solve(arr: List[int], A: int, B: int) -> int:
    n = len(arr)
    def get_sums(arr_slice):
        sums = [0]
        for x in arr_slice:
            sums += [s + x for s in sums]
        return sums
    left = get_sums(arr[:n//2])
    right = sorted(get_sums(arr[n//2:]))
    count = 0
    for x in left:
        low = bisect.bisect_left(right, A - x)
        high = bisect.bisect_right(right, B - x)
        count += (high - low)
    return count

