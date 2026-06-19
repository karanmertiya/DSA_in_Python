# Time Complexity: O(N * 2^N)
# Space Complexity: O(2^N * N)
# Explanation: Iterate from `0` to `2^N - 1`. If the `j`th bit is set in `i`, include `nums[j]` in the current subset.

def subsets(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    ans = []
    for i in range(1 << n):
        sub = []
        for j in range(n):
            if i & (1 << j):
                sub.append(nums[j])
        ans.append(sub)
    return ans

