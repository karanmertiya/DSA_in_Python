# Time Complexity: O(1)
# Space Complexity: O(1)
# Explanation: Use OR (`|`) to set, AND with NOT (`& ~`) to clear, and XOR (`^`) to toggle.

def bit_operations(n: int, i: int) -> list:
    set_bit = n | (1 << i)
    clear_bit = n & ~(1 << i)
    toggle_bit = n ^ (1 << i)
    return [set_bit, clear_bit, toggle_bit]

