# Time Complexity: O(2^N * N)
# Space Complexity: O(2^N * N)
# Explanation: Sort array first to bring duplicates together. In recursive call, loop from `ind` to `n`. If `i > ind` and `nums[i] == nums[i-1]`, `continue` to skip duplicate recursive branches.

def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    ans = []
    nums.sort()
    def findSubsets(ind, ds):
        ans.append(list(ds))
        for i in range(ind, len(nums)):
            if i != ind and nums[i] == nums[i-1]: continue
            ds.append(nums[i])
            findSubsets(i + 1, ds)
            ds.pop()
    findSubsets(0, [])
    return ans

