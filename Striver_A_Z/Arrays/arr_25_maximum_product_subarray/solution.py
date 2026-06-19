# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Maintain the prefix product and suffix product. If a zero is encountered, reset the product to 1. The maximum product will be the maximum of all prefix and suffix products.

def maxProduct(nums: List[int]) -> int:
    n = len(nums)
    pre, suff = 1, 1
    ans = float('-inf')
    for i in range(n):
        if pre == 0: pre = 1
        if suff == 0: suff = 1
        pre *= nums[i]
        suff *= nums[n - i - 1]
        ans = max(ans, pre, suff)
    return int(ans)

