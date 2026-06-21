# Time Complexity: O(min(a, b))
# Space Complexity: O(1)
# Explanation: Brute Force: Iterate from 1 to min(a, b) and find the highest number that divides both.

def lcmAndGcd(a: int, b: int) -> list[int]:
    gcd = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    lcm = (a // gcd) * b  # Divide first to prevent overflow
    return [lcm, gcd]

# Time Complexity: O(log(min(a, b)))
# Space Complexity: O(1)
# Explanation: Euclidean Algorithm (Optimal): Repeatedly replace max(a,b) with max(a,b) % min(a,b). The final non-zero value is the GCD. Note: LCM can be found in O(1) extra time using formula: LCM(a,b) = (a*b) / GCD(a,b)

def lcmAndGcd(a: int, b: int) -> list[int]:
    original_a, original_b = a, b
    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    # The non-zero value is the GCD. Since one of them is 0, we can just return a + b
    gcd = a + b
    lcm = (original_a // gcd) * original_b  # Divide first to prevent overflow
    return [lcm, gcd]

