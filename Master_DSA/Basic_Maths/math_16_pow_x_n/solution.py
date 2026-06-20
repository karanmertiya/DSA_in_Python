# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Brute Force: Loop n times and multiply ans by x.

def myPow(x: float, n: int) -> float:
    ans = 1.0
    nn = abs(n)
    for _ in range(nn):
        ans *= x
    return 1.0 / ans if n < 0 else ans

# Time Complexity: O(log N)
# Space Complexity: O(1)
# Explanation: Optimal: Binary Exponentiation. If n is even, x = x*x, n = n/2. If odd, ans = ans*x, n = n-1.

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

