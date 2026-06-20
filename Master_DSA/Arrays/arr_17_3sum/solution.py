# Time Complexity: O(N<sup>2</sup>) (Constraint)
# Space Complexity: O(1) (Trade-off)
# Explanation: Sort the array. Use a loop to fix `i`, then use a Two-Pointer approach (`j`, `k`) for the remaining array to find sum `0 - nums[i]`.

def threeSum(nums: list[int]) -> list[list[int]]:
    ans = []
    nums.sort()
    n = len(nums)
    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]: continue
        j, k = i + 1, n - 1
        while j < k:
            s = nums[i] + nums[j] + nums[k]
            if s < 0:
                j += 1
            elif s > 0:
                k -= 1
            else:
                ans.append([nums[i], nums[j], nums[k]])
                j += 1; k -= 1
                while j < k and nums[j] == nums[j-1]: j += 1
                while j < k and nums[k] == nums[k+1]: k -= 1
    return ans

