# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: 1. XOR all elements to get `x ^ y`. 2. Find the rightmost set bit in `x ^ y` using `(x ^ y) & -(x ^ y)`. 3. Divide elements into two groups based on this bit. 4. XOR elements in each group to get `x` and `y`.

def singleNumber(nums: List[int]) -> List[int]:
    XOR = 0
    for n in nums: XOR ^= n
    rightmost_set_bit = XOR & ~(XOR - 1)
    x, y = 0, 0
    for n in nums:
        if n & rightmost_set_bit:
            x ^= n
        else:
            y ^= n
    return sorted([x, y])

