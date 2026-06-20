# Time Complexity: O(N log N) or O(N)
# Space Complexity: O(N)
# Explanation: Brute Force: Use a HashSet to store unique elements, then put them back into the array.

def removeDuplicates(nums):
    unique_nums = sorted(list(set(nums)))
    for i in range(len(unique_nums)):
        nums[i] = unique_nums[i]
    return len(unique_nums)

# Time Complexity: O(N) (Constraint)
# Space Complexity: O(1) (Constraint)
# Explanation: Optimal: Two-pointer approach. Pointer `i` keeps track of unique elements, pointer `j` scans the array to find new unique elements.

def removeDuplicates(nums: list[int]) -> int:
    if not nums: return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1

