# Time Complexity: O(1)
# Space Complexity: O(1)
# Explanation: Right shift N by i times and check if the least significant bit is 1.

def check_kth_bit_right_shift(n: int, k: int) -> bool:
    return ((n >> k) & 1) != 0

