# Time Complexity: O(log N)
# Space Complexity: O(1)
# Explanation: Use binary exponentiation. Initialize `ans = 1.0`. Keep a copy of `n` as a long long `nn`. If `nn < 0`, make it positive. While `nn > 0`, if `nn % 2 == 1`, multiply `ans` by `x` and decrement `nn`. Otherwise, square `x` and halve `nn`. If original `n < 0`, return `1.0 / ans`.

def myPow(x, n):
    ans, nn = 1.0, abs(n)
    while nn > 0:
        if nn % 2 == 1:
            ans *= x
            nn -= 1
        else:
            x *= x
            nn //= 2
    return ans if n >= 0 else 1.0 / ans

