# Time Complexity: O(N + M) (Constraint)
# Space Complexity: O(N) (Trade-off)
# Explanation: Store elements of the first array in a Hash Set, then iterate over the second array to find matches.

def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    set1 = set(nums1)
    res = []
    for num in nums2:
        if num in set1:
            res.append(num)
            set1.remove(num) # Ensure uniqueness
    return res

