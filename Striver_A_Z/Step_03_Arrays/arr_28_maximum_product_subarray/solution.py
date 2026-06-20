# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Optimal: Maintain prefix and suffix products. If a 0 is encountered, reset the product to 1. The max overall is the answer since negatives cancel out in pairs.

def maxProduct(nums: List[int]) -> int:
    pref, suff, ans = 1, 1, float('-inf')
    n = len(nums)
    for i in range(n):
        if pref == 0: pref = 1
        if suff == 0: suff = 1
        pref *= nums[i]
        suff *= nums[n-1-i]
        ans = max(ans, pref, suff)
    return int(ans)

