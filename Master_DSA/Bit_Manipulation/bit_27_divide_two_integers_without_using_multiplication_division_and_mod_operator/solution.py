# Time Complexity: O(log N)
# Space Complexity: O(1)
# Explanation: Determine the sign. Work with absolute values. Keep shifting the divisor left (multiplying by 2) until it's greater than the dividend. The shift amount `i` means the divisor can be multiplied by `2^i`. Subtract `(divisor << i)` from dividend, add `2^i` to quotient. Repeat until dividend < divisor.

def divide(dividend, divisor):
    sign = -1 if ((dividend < 0) ^ (divisor < 0)) else 1
    dividend, divisor = abs(dividend), abs(divisor)
    quotient = 0
    temp = 0
    for i in range(31, -1, -1):
        if temp + (divisor << i) <= dividend:
            temp += divisor << i
            quotient |= 1 << i
    res = sign * quotient
    if res > 2147483647: return 2147483647
    if res < -2147483648: return -2147483648
    return res

