# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Insert all elements into a hash set. Iterate through the set. If `x - 1` is not in the set, `x` is the start of a sequence. Count consecutive elements `x + 1`, `x + 2`... Update max length.

def longestConsecutive(nums):
    s = set(nums)
    max_len = 0
    for num in s:
        if num - 1 not in s:
            curr_num, curr_len = num, 1
            while curr_num + 1 in s:
                curr_num += 1
                curr_len += 1
            max_len = max(max_len, curr_len)
    return max_len

