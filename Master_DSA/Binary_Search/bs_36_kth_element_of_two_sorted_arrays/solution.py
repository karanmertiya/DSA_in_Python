# Time Complexity: O(log(min(N, M, K)))
# Space Complexity: O(1)
# Explanation: Similar to Median of 2 sorted arrays. Apply binary search on the smaller array. The partition requires `cut1 + cut2 = k`. Boundaries for `cut1` are `max(0, k - m)` and `min(k, n)`.

def kthElement(arr1: List[int], arr2: List[int], n: int, m: int, k: int) -> int:
    if n > m: return kthElement(arr2, arr1, m, n, k)
    low, high = max(0, k - m), min(k, n)
    while low <= high:
        cut1 = (low + high) // 2
        cut2 = k - cut1
        left1 = float('-inf') if cut1 == 0 else arr1[cut1-1]
        left2 = float('-inf') if cut2 == 0 else arr2[cut2-1]
        right1 = float('inf') if cut1 == n else arr1[cut1]
        right2 = float('inf') if cut2 == m else arr2[cut2]
        if left1 <= right2 and left2 <= right1:
            return max(left1, left2)
        elif left1 > right2:
            high = cut1 - 1
        else:
            low = cut1 + 1
    return 1

