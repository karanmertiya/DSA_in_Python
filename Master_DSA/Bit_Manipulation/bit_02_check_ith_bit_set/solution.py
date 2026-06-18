# Time Complexity: O(1)
# Space Complexity: O(1)
# Explanation: Right shift N by i times and check if the least significant bit is 1.

def check_kth_bit_right_shift(n: int, k: int) -> bool:
    return ((n >> k) & 1) != 0

# Time Complexity: O(1) (Constraint)
# Space Complexity: O(1)
# Explanation: Left shift 1 by i times to create a mask, then bitwise AND with N.

def check_kth_bit_left_shift(n: int, k: int) -> bool:
    # Python handles arbitrary length ints natively
    return (n & (1 << k)) != 0

