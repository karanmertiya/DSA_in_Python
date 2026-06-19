# Time Complexity: O(log10 x)
# Space Complexity: O(1)
# Explanation: Extract last digit using modulo, multiply answer by 10 and add. Check bounds for 32-bit integer.

def reverse(x: int) -> int:
    sign = [1, -1][x < 0]
    ans = int(str(abs(x))[::-1])
    return sign * ans if ans <= 2**31 - 1 else 0

