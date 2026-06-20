# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Brute Force: Iterate from 2 to N-1 and check if N is divisible.

def isPrime(N: int) -> int:
    if N <= 1: return 0
    for i in range(2, N):
        if N % i == 0: return 0
    return 1

# Time Complexity: O(sqrt(N))
# Space Complexity: O(1)
# Explanation: Optimal: Check divisibility up to sqrt(N). Factors appear in pairs.

def isPrime(N: int) -> int:
    if N <= 1: return 0
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0: return 0
    return 1

