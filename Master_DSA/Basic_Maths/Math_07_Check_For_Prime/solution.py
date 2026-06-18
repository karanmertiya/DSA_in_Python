# --- Brute Force Approach ---
# Time Complexity: O(N) (Trade-off)
# Space Complexity: O(1) (Constraint)
# Edge Cases: <b>TLE Guarantee:</b> N=10^9 takes ~10<sup>9</sup> ops. Guaranteed TLE on any modern platform.
# Note: Iterate from 2 to N-1 and check divisibility.

def check_prime_brute(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# --- Optimal Approach ---
# Time Complexity: O(&radic;N) (Constraint)
# Space Complexity: O(1) (Constraint)
# Edge Cases: <b>Loop Optimization:</b> `i * i <= n` is far superior to computing `sqrt(n)` repeatedly.
# Note: Iterate from 2 up to sqrt(N) since divisors come in pairs.

def check_prime_optimal(n: int) -> bool:
    if n <= 1:
        return False
    limit = int(n**0.5)
    for i in range(2, limit + 1):
        if n % i == 0:
            return False
    return True

