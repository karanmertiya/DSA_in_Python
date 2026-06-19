# Time Complexity: O(N^2)
# Space Complexity: O(1) excluding output
# Explanation: Sort the array. Fix the first element `nums[i]`. Use two pointers (`left = i+1`, `right = n-1`) to find the remaining two elements that sum to `-nums[i]`. Skip duplicates for `i`, `left`, and `right` to ensure unique triplets.

def threeSum(nums):
    nums.sort()
    ans = []
    n = len(nums)
    for i in range(n - 2):
        if i == 0 or nums[i] != nums[i-1]:
            low, high, target = i + 1, n - 1, -nums[i]
            while low < high:
                if nums[low] + nums[high] == target:
                    ans.append([nums[i], nums[low], nums[high]])
                    while low < high and nums[low] == nums[low+1]: low += 1
                    while low < high and nums[high] == nums[high-1]: high -= 1
                    low += 1
                    high -= 1
                elif nums[low] + nums[high] < target: low += 1
                else: high -= 1
    return ans

