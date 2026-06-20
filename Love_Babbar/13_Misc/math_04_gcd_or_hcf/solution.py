# Time Complexity: O(log(min(a,b)))
# Space Complexity: O(1)
# Explanation: Euclidean Algorithm. gcd(a, b) = gcd(b, a % b). Stop when one is 0.

def gcd(a: int, b: int) -> int:
    while a > 0 and b > 0:
        if a > b: a = a % b
        else: b = b % a
    return b if a == 0 else a

