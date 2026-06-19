# Time Complexity: O(log N)
# Space Complexity: O(1)
# Explanation: Binary Exponentiation. If n is even, `x^n = (x*x)^(n/2)`. If n is odd, `x^n = x * x^(n-1)`. Handles negative powers by computing `1 / pow(x, -n)`.

def myPow(x: float, n: int) -> float:
    ans = 1.0
    nn = abs(n)
    while nn > 0:
        if nn % 2 == 1:
            ans = ans * x
            nn -= 1
        else:
            x = x * x
            nn //= 2
    if n < 0: ans = 1.0 / ans
    return ans

