# Time Complexity: O(sqrt(N))
# Space Complexity: O(1)
# Explanation: Check divisibility up to sqrt(N). Iterating up to N (O(N) time) is unnecessary and inefficient since factors always appear in pairs.

def isPrime(N: int) -> int:
    if N <= 1: return 0
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0: return 0
    return 1

