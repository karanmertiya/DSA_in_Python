# Time Complexity: O(1)
# Space Complexity: O(1)
# Explanation: Use basic arithmetic (addition and subtraction) to swap.

def swap_arithmetic(a: int, b: int) -> tuple:
    a = a + b
    b = a - b
    a = a - b
    return a, b

