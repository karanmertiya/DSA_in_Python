# Time Complexity: O(log^2 N)
# Space Complexity: O(1)
# Explanation: Use left shift to find the largest multiple of divisor that fits into dividend. Subtract it and add the shifted value to quotient. Repeat until dividend < divisor.

def divide(dividend: int, divisor: int) -> int:
    if dividend == -2147483648 and divisor == -1: return 2147483647
    n, d = abs(dividend), abs(divisor)
    sign = (dividend < 0) == (divisor < 0)
    quotient = 0
    while n >= d:
        temp, multiple = d, 1
        while n >= (temp << 1):
            temp <<= 1
            multiple <<= 1
        n -= temp
        quotient += multiple
    return quotient if sign else -quotient

