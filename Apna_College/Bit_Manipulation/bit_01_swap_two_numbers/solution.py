# Time Complexity: O(1)
# Space Complexity: O(1)
# Explanation: Use basic arithmetic (addition and subtraction) to swap.

def swap_arithmetic(a: int, b: int) -> tuple:
    a = a + b
    b = a - b
    a = a - b
    return a, b

# Time Complexity: O(1) (Constraint)
# Space Complexity: O(1)
# Explanation: Use XOR bitwise operation. XOR of a number with itself is 0, and with 0 is the number itself.

def swap_optimal(a: int, b: int) -> tuple:
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

