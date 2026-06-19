# Time Complexity: O(log(min(N, M)))
# Space Complexity: O(1)
# Explanation: Similar to median of two sorted arrays. Do binary search on the smaller array for a partition such that the total number of elements on the left side is `k`. Ensure `cut1` is between `max(0, k-m)` and `min(k, n)`.

def kthElement(arr1, arr2, n, m, k):
    if n > m: return kthElement(arr2, arr1, m, n, k)
    low = max(0, k - m)
    high = min(k, n)
    while low <= high:
        cut1 = (low + high) // 2
        cut2 = k - cut1
        l1 = float('-inf') if cut1 == 0 else arr1[cut1 - 1]
        l2 = float('-inf') if cut2 == 0 else arr2[cut2 - 1]
        r1 = float('inf') if cut1 == n else arr1[cut1]
        r2 = float('inf') if cut2 == m else arr2[cut2]
        if l1 <= r2 and l2 <= r1:
            return max(l1, l2)
        elif l1 > r2:
            high = cut1 - 1
        else:
            low = cut1 + 1
    return 1

