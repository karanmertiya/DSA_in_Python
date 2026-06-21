# Time Complexity: O(N^2)
# Space Complexity: O(N)
# Explanation: Maintain `lengths[i]` (length of LIS ending at i) and `counts[i]` (number of LIS ending at i). If `nums[i] > nums[j]`: if `lengths[j] + 1 > lengths[i]`, then `lengths[i] = lengths[j] + 1` and `counts[i] = counts[j]`. Else if `lengths[j] + 1 == lengths[i]`, then `counts[i] += counts[j]`.

def findNumberOfLIS(nums: List[int]) -> int:
    n = len(nums)
    lengths = [1] * n
    counts = [1] * n
    max_len = 0
    res = 0
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                if lengths[j] + 1 > lengths[i]:
                    lengths[i] = lengths[j] + 1
                    counts[i] = counts[j]
                elif lengths[j] + 1 == lengths[i]:
                    counts[i] += counts[j]
        if lengths[i] > max_len:
            max_len = lengths[i]
            res = counts[i]
        elif lengths[i] == max_len:
            res += counts[i]
    return res

