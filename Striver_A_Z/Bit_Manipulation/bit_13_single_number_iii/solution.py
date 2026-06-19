# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: XOR all elements to get `A ^ B`. The rightmost set bit in `A ^ B` means A and B differ at this bit. Use this bit to partition the array into two groups and XOR elements in each group. The results are A and B.

def singleNumber(nums):
    XOR = 0
    for num in nums: XOR ^= num
    rightmost_set_bit = XOR & ~(XOR - 1)
    b1, b2 = 0, 0
    for num in nums:
        if num & rightmost_set_bit:
            b1 ^= num
        else:
            b2 ^= num
    return [b1, b2]

