# Time Complexity: O(log N)
# Space Complexity: O(log N) recursive stack
# Explanation: If n is even, `pow(x, n) = pow(x*x, n/2)`. If n is odd, `pow(x, n) = x * pow(x, n-1)`. Handle negative n by making it positive and returning `1 / ans`.

def myPow(x, n):
    nn = abs(n)
    ans = 1.0
    while nn > 0:
        if nn % 2 == 1:
            ans *= x
            nn -= 1
        else:
            x *= x
            nn //= 2
    if n < 0: ans = 1.0 / ans
    return ans

