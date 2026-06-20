# Time Complexity: O(1)
# Space Complexity: O(1)
# Explanation: Right shift N by K times and check if the least significant bit is 1.

def check_kth_bit_right_shift(n: int, k: int) -> bool:
    return ((n >> k) & 1) != 0

# Time Complexity: O(1)
# Space Complexity: O(1)
# Explanation: Create a mask by left shifting 1 by K times and check if the bitwise AND with N is non-zero.

def check_kth_bit(n: int, k: int) -> bool:
    return (n & (1 << k)) != 0

