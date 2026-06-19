# Time Complexity: O(log(min(N, M)))
# Space Complexity: O(1)
# Explanation: Ensure arr1 is smaller. Binary search on arr1. `cut1` is between `max(0, k-m)` and `min(k, n)`. `cut2 = k - cut1`. Compare `l1 <= r2` and `l2 <= r1`. If so, return `max(l1, l2)`. Else adjust `low` and `high`.

def kthElement(arr1: List[int], arr2: List[int], n: int, m: int, k: int) -> int:
    if n > m: return kthElement(arr2, arr1, m, n, k)
    low, high = max(0, k - m), min(k, n)
    while low <= high:
        cut1 = (low + high) // 2
        cut2 = k - cut1
        l1 = float('-inf') if cut1 == 0 else arr1[cut1 - 1]
        l2 = float('-inf') if cut2 == 0 else arr2[cut2 - 1]
        r1 = float('inf') if cut1 == n else arr1[cut1]
        r2 = float('inf') if cut2 == m else arr2[cut2]
        if l1 <= r2 and l2 <= r1: return max(l1, l2)
        elif l1 > r2: high = cut1 - 1
        else: low = cut1 + 1
    return 1

