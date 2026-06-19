# Time Complexity: O(N^3)
# Space Complexity: O(1) excluding output
# Explanation: Sort the array. Fix the first two elements using nested loops (`i` and `j`). Then use two pointers (`left` and `right`) to find the remaining two elements that sum up to `target - nums[i] - nums[j]`. Skip duplicates for all 4 variables.

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

