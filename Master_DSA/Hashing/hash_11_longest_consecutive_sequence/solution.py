# Time Complexity: O(N log N)
# Space Complexity: O(1)
# Explanation: Brute Force: Sort the array first, then count consecutive elements linearly.

def longestConsecutive(nums):
    if not nums: return 0
    nums.sort()
    longest, current = 1, 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]: continue
        if nums[i] == nums[i-1] + 1:
            current += 1
        else:
            longest = max(longest, current)
            current = 1
    return max(longest, current)

# Time Complexity: O(N) (Constraint)
# Space Complexity: O(N)
# Explanation: Optimal: Insert all elements into a Hash Set. Iterate through elements. If `num - 1` is NOT in the set, it's the start of a sequence. Count forwards.

def longestConsecutive(nums: list[int]) -> int:
    num_set = set(nums)
    max_len = 0
    for num in num_set:
        if num - 1 not in num_set:
            curr_num = num
            curr_len = 1
            while curr_num + 1 in num_set:
                curr_num += 1
                curr_len += 1
            max_len = max(max_len, curr_len)
    return max_len

