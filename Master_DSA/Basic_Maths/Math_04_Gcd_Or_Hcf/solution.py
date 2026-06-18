# --- Brute Force Approach ---
# Time Complexity: O(min(N1, N2)) (Trade-off)
# Space Complexity: O(1) (Constraint)
# Edge Cases: <b>TLE Risk:</b> ~10<sup>9</sup> ops heavily exceeds 1 sec limit.
# Note: Iterate from min(N1, N2) down to 1. The first number dividing both is the GCD.

def gcd_brute(n1: int, n2: int) -> int:
    for i in range(min(n1, n2), 0, -1):
        if n1 % i == 0 and n2 % i == 0:
            return i
    return 1

# --- Optimal Approach ---
# Time Complexity: O(log(&Phi;)(min(N1, N2))) (Constraint)
# Space Complexity: O(1) (Constraint)
# Edge Cases: <b>Modulo Safety:</b> Euclidean Algorithm easily passes 10<sup>9</sup> via log-scale modulo operations.
# Note: Euclidean algorithm: gcd(a, b) = gcd(b, a % b) until one becomes 0.

def gcd_optimal(a: int, b: int) -> int:
    while a > 0 and b > 0:
        # Uses modulo rather than subtraction for logarithmic time complexity
        if a > b:
            a = a % b
        else:
            b = b % a
    if a == 0:
        return b
    return a

