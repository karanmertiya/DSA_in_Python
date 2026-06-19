# Time Complexity: O(log(min(M, N)))
# Space Complexity: O(1)
# Explanation: Ensure `nums1` is the smaller array. Do binary search on `nums1` to find a partition such that the left half has `(m+n+1)/2` elements. Calculate the maximums of left halves and minimums of right halves. If `maxLeft1 <= minRight2` and `maxLeft2 <= minRight1`, the partition is correct. The median depends on whether `m+n` is even or odd.

def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2): return findMedianSortedArrays(nums2, nums1)
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

