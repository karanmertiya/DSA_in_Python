# Time Complexity: O(log(min(m, n)))
# Space Complexity: O(1)
# Explanation: Binary Search on the smaller array. Partition both arrays such that the left half has `(m+n+1)/2` elements. Find the valid partition where `max(left1) <= min(right2)` and `max(left2) <= min(right1)`.

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    if len(nums1) > len(nums2): return self.findMedianSortedArrays(nums2, nums1)
    n1, n2 = len(nums1), len(nums2)
    low, high = 0, n1
    while low <= high:
        cut1 = (low + high) // 2
        cut2 = (n1 + n2 + 1) // 2 - cut1
        left1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
        left2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]
        right1 = float('inf') if cut1 == n1 else nums1[cut1]
        right2 = float('inf') if cut2 == n2 else nums2[cut2]
        if left1 <= right2 and left2 <= right1:
            if (n1 + n2) % 2 == 0:
                return (max(left1, left2) + min(right1, right2)) / 2.0
            else:
                return max(left1, left2)
        elif left1 > right2:
            high = cut1 - 1
        else:
            low = cut1 + 1
    return 0.0

