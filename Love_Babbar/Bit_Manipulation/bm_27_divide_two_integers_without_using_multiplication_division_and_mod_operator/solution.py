# Time Complexity: O(log N)
# Space Complexity: O(1)
# Explanation: Keep shifting `divisor` left by `i` bits until it's just smaller than `dividend`. Subtract `divisor << i` from `dividend` and add `1 << i` to the `quotient`. Repeat.

def divide(dividend: int, divisor: int) -> int:
    if dividend == -2147483648 and divisor == -1: return 2147483647
    a, b = abs(dividend), abs(divisor)
    res = 0
    while a >= b:
        x = 0
        while a >= (b << 1 << x):
            x += 1
        res += 1 << x
        a -= b << x
    return res if (dividend > 0) == (divisor > 0) else -res

