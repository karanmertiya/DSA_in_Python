# Time Complexity: O(min(a, b))
# Space Complexity: O(1)
# Explanation: Brute Force: Iterate from 1 to min(a, b) and find the highest number that divides both.

def gcd(a: int, b: int) -> int:
    ans = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            ans = i
    return ans

# Time Complexity: O(log(min(a,b)))
# Space Complexity: O(1)
# Explanation: Optimal: Euclidean Algorithm. gcd(a, b) = gcd(b, a % b).

def gcd(a: int, b: int) -> int:
    while a > 0 and b > 0:
        if a > b: a = a % b
        else: b = b % a
    return b if a == 0 else a

