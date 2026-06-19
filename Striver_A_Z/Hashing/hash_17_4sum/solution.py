# Time Complexity: O(N^3)
# Space Complexity: O(1)
# Explanation: Sort array. Use nested loops for first two elements. Use two pointers for the remaining two. Skip duplicates to ensure unique quadruplets.

def fourSum(nums, target):
    nums.sort()
    ans = []
    n = len(nums)
    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]: continue
        for j in range(i + 1, n):
            if j > i + 1 and nums[j] == nums[j-1]: continue
            low, high = j + 1, n - 1
            while low < high:
                total = nums[i] + nums[j] + nums[low] + nums[high]
                if total == target:
                    ans.append([nums[i], nums[j], nums[low], nums[high]])
                    while low < high and nums[low] == nums[low+1]: low += 1
                    while low < high and nums[high] == nums[high-1]: high -= 1
                    low += 1; high -= 1
                elif total < target: low += 1
                else: high -= 1
    return ans

