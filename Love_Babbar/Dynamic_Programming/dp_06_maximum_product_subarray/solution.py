# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Prefix and Suffix product approach. Calculate product from left to right and right to left. Reset product to 1 when a zero is encountered.

def maxProduct(nums: list[int]) -> int:
    max_prod = float('-inf')
    pref, suff = 1, 1
    n = len(nums)
    for i in range(n):
        if pref == 0: pref = 1
        if suff == 0: suff = 1
        pref *= nums[i]
        suff *= nums[n - 1 - i]
        max_prod = max(max_prod, pref, suff)
    return int(max_prod)

