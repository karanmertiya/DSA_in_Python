# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: 1) XOR all elements. Result is XOR of the two odd numbers. 2) Find the rightmost set bit in the result. 3) Divide array elements into two buckets based on this set bit. 4) XORing the two buckets individually yields the two numbers.

def twoOddNum(Arr: List[int], N: int) -> List[int]:
    xor_all = 0
    for num in Arr: xor_all ^= num
    right_set_bit = xor_all & ~(xor_all - 1)
    x, y = 0, 0
    for num in Arr:
        if num & right_set_bit: x ^= num
        else: y ^= num
    if x < y: x, y = y, x
    return [x, y]

