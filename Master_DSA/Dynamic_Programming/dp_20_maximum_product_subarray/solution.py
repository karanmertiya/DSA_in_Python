# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Iterate through the array while maintaining a `currMax` and `currMin`. If `nums[i] < 0`, swap `currMax` and `currMin`. `currMax = max(nums[i], currMax * nums[i])`. `currMin = min(nums[i], currMin * nums[i])`. Update `globalMax`.

def maxProduct(nums: List[int]) -> int:
    if not nums: return 0
    currMax = currMin = ans = nums[0]
    for num in nums[1:]:
        if num < 0:
            currMax, currMin = currMin, currMax
        currMax = max(num, currMax * num)
        currMin = min(num, currMin * num)
        ans = max(ans, currMax)
    return ans

