# --- Brute Force Approach ---
# Time Complexity: O(N) (Trade-off)
# Space Complexity: O(1) (Constraint)
# Edge Cases: <b>TLE Risk:</b> N=10^6 takes ~10<sup>6</sup> ops. Highly inefficient compared to optimal.
# Note: Iterate from 1 to N and check for divisibility.

def print_divisors_brute(n: int) -> None:
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")

# --- Optimal Approach ---
# Time Complexity: O(&radic;N * log(&radic;N)) (Constraint)
# Space Complexity: O(&radic;N) (Trade-off)
# Edge Cases: <b>Perfect Squares:</b> Checking `(n / i) != i` explicitly prevents duplicate divisor entries.
# Note: Iterate up to sqrt(N) to find pairs of divisors, then sort.

def print_divisors_optimal(n: int) -> None:
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            # Edge Case: Avoid duplicate addition for perfect square roots
            if n // i != i:
                divisors.append(n // i)
    divisors.sort()
    for d in divisors:
        print(d, end=" ")

