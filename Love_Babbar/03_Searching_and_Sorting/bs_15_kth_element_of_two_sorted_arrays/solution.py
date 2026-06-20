# Time Complexity: O(N^2) or worse
# Space Complexity: O(N) or O(1)
# Explanation: Brute Force: Standard unoptimized approach. (TODO: Implement specific logic)

# TODO: Implement Brute Force
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
        if left1 <= right2 and left2 <= right1: return max(left1, left2)
        elif left1 > right2: high = cut1 - 1
        else: low = cut1 + 1
    return 1

# Time Complexity: O(log(min(n, m)))
# Space Complexity: O(1)
# Explanation: Optimal: Binary search on the smaller array. Similar to Median of two sorted arrays, but the left partition size is strictly `k`. Search space for `cut1` is `[max(0, k-m), min(k, n)]`.

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
        if left1 <= right2 and left2 <= right1: return max(left1, left2)
        elif left1 > right2: high = cut1 - 1
        else: low = cut1 + 1
    return 1

