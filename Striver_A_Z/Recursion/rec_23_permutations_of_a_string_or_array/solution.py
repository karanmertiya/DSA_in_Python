# Time Complexity: O(N! * N)
# Space Complexity: O(N)
# Explanation: Iterate `i` from `index` to `n-1`. Swap `nums[index]` and `nums[i]`, then recurse for `index + 1`. Swap back to backtrack.

def permute(nums: List[int]) -> List[List[int]]:
    ans = []
    def recur(index):
        if index == len(nums):
            ans.append(nums[:])
            return
        for i in range(index, len(nums)):
            nums[index], nums[i] = nums[i], nums[index]
            recur(index + 1)
            nums[index], nums[i] = nums[i], nums[index]
    recur(0)
    return ans

