# Time Complexity: O(min(a, b)) (Trade-off)
# Space Complexity: O(1)
# Explanation: Iterate from min(a,b) down to 1 for GCD. Compute LCM normally.

def gcd_lcm_brute(a: int, b: int) -> None:
    gcd = 1
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            gcd = i
            break
    # Edge Case: Divide first to strictly avoid mathematical overflow
    lcm = (a // gcd) * b
    print(f"GCD: {gcd}, LCM: {lcm}")

# Time Complexity: O(log(&Phi;)(min(a, b))) (Constraint)
# Space Complexity: O(1)
# Explanation: Euclidean algorithm for GCD: gcd(a,b) = gcd(b, a%b). Then calculate LCM.

def gcd_lcm_optimal(a: int, b: int) -> None:
    orig_a, orig_b = a, b
    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    gcd = b if a == 0 else a
    lcm = (orig_a // gcd) * orig_b
    print(f"GCD: {gcd}, LCM: {lcm}")

