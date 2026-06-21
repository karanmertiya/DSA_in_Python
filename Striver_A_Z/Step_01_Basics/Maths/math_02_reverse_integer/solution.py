# Time Complexity: O(log10 x)
# Space Complexity: O(1)
# Explanation: Optimal Approach: Use a 64-bit integer to naturally store the reversed number. A variant note explains how to do this strictly with 32-bit integers if long is not allowed.

def reverse(x: int) -> int:
    ans = 0
    sign = -1 if x < 0 else 1
    x = abs(x)
    while x != 0:
        digit = x % 10
        ans = ans * 10 + digit
        x //= 10
    ans *= sign
    if ans > 2**31 - 1 or ans < -2**31:
        return 0
    return ans

# Time Complexity: O(log10 x)
# Space Complexity: O(log10 x)
# Explanation: Brute Force / String Approach: Convert to string, reverse, and then parse back to integer.

def reverse(x: int) -> int:
    sign = [1, -1][x < 0]
    ans = int(str(abs(x))[::-1])
    return sign * ans if ans <= 2**31 - 1 else 0

