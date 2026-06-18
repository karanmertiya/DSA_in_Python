# Time Complexity: O(N) (Trade-off)
# Space Complexity: O(1)
# Explanation: Iterate from 2 to N-1 and check divisibility.

def check_prime_brute(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Time Complexity: O(&radic;N) (Constraint)
# Space Complexity: O(1)
# Explanation: Iterate from 2 up to sqrt(N) checking divisor pairs.

def check_prime_optimal(n: int) -> bool:
    if n <= 1: return False
    if n == 2: return True
    # Edge Case Optimization: Halve range by skipping evens
    if n % 2 == 0: return False
    
    limit = int(n**0.5)
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True

