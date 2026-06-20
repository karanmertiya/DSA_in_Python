# Time Complexity: O(N * M)
# Space Complexity: O(min(N, M))
# Explanation: Brute Force: Iterate through the first array and check each element in the second array.

def intersection(nums1, nums2):
    res = []
    for x in nums1:
        if x in nums2 and x not in res:
            res.append(x)
    return res

# Time Complexity: O(N + M) (Constraint)
# Space Complexity: O(N) (Trade-off)
# Explanation: Optimal: Store elements of the first array in a Hash Set, then iterate over the second array to find matches.

def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    set1 = set(nums1)
    res = []
    for num in nums2:
        if num in set1:
            res.append(num)
            set1.remove(num) # Ensure uniqueness
    return res

