# Time Complexity: O(N^2)
# Space Complexity: O(N)
# Explanation: Sort the array. Then use LIS logic: `dp[i]` is max subset ending at `i`. If `nums[i] % nums[j] == 0`, `dp[i] = max(dp[i], dp[j] + 1)`. Also keep a `parent` array to reconstruct the subset.

def largestDivisibleSubset(nums: List[int]) -> List[int]:
    if not nums: return []
    nums.sort()
    n = len(nums)
    dp, parent = [1] * n, [-1] * n
    max_len, max_idx = 1, 0
    for i in range(1, n):
        for j in range(i):
            if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                parent[i] = j
        if dp[i] > max_len:
            max_len, max_idx = dp[i], i
    res = []
    while max_idx != -1:
        res.append(nums[max_idx])
        max_idx = parent[max_idx]
    return res

