# Time Complexity: O(min(a, b))
# Space Complexity: O(1)
# Explanation: Brute Force: Iterate from 1 to min(a, b) and find the highest number that divides both.

def gcd(a: int, b: int) -> int:
    ans = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            ans = i
    return ans

# Time Complexity: O(log(min(a, b)))
# Space Complexity: O(1)
# Explanation: Euclidean Algorithm (Optimal): Repeatedly replace max(a,b) with max(a,b) % min(a,b). The final non-zero value is the GCD. Note: LCM can be found in O(1) extra time using formula: LCM(a,b) = (a*b) / GCD(a,b)

def calcGCD(n: int, m: int) -> int:
    while n > 0 and m > 0:
        if n > m: n = n % m
        else: m = m % n
    return m if n == 0 else n

    # LCM Calculation
    # lcm = (n * m) // calcGCD(n, m)

