# Time Complexity: O(2^N * N)
# Space Complexity: O(2^N * K)
# Explanation: Sort array. Recursive call adds current `ds` to `ans`. Then iterate `i` from `ind` to `n`. Skip if `i > ind` and `nums[i] == nums[i-1]`. Add to `ds`, recurse for `i+1`, pop from `ds`.

def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    ans = []
    nums.sort()
    def find(ind, ds):
        ans.append(list(ds))
        for i in range(ind, len(nums)):
            if i != ind and nums[i] == nums[i-1]: continue
            ds.append(nums[i])
            find(i + 1, ds)
            ds.pop()
    find(0, [])
    return ans

