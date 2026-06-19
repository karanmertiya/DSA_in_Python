# Time Complexity: O((N + M) log(N + M))
# Space Complexity: O(1)
# Explanation: Use the Gap method. Initial gap is `ceil((n + m) / 2)`. Iterate with two pointers separated by `gap`. If `left` and `right` elements are out of order, swap them. Reduce `gap` by `ceil(gap / 2)` until `gap == 0`.

import math
def merge(arr1: List[int], arr2: List[int], n: int, m: int):
    length = n + m
    gap = math.ceil(length / 2)
    while gap > 0:
        left = 0
        right = left + gap
        while right < length:
            if left < n and right < n:
                if arr1[left] > arr1[right]:
                    arr1[left], arr1[right] = arr1[right], arr1[left]
            elif left < n and right >= n:
                if arr1[left] > arr2[right - n]:
                    arr1[left], arr2[right - n] = arr2[right - n], arr1[left]
            else:
                if arr2[left - n] > arr2[right - n]:
                    arr2[left - n], arr2[right - n] = arr2[right - n], arr2[left - n]
            left += 1
            right += 1
        if gap == 1: break
        gap = math.ceil(gap / 2)

