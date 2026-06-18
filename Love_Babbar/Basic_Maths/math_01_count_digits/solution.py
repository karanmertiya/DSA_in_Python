# Time Complexity: O(log10(N))
# Space Complexity: O(1)
# Explanation: Divide by 10 continuously until N becomes 0.

def count_digits_brute(n: int) -> int:
    # Edge Case: 0 has 1 digit, negative numbers require abs()
    if n == 0: return 1
    n = abs(n)
    cnt = 0
    while n > 0:
        cnt += 1
        n //= 10
    return cnt

# Time Complexity: O(1) (Constraint)
# Space Complexity: O(log10(N)) (Trade-off)
# Explanation: Convert number to string and return length.

def count_digits_better(n: int) -> int:
    if n == 0: return 1
    # Trade-off: Allocates string memory
    return len(str(abs(n)))

# Time Complexity: O(1) (Constraint)
# Space Complexity: O(1)
# Explanation: Use base-10 logarithm to find digit count mathematically.

import math

def count_digits_optimal(n: int) -> int:
    if n == 0: return 1
    n = abs(n)
    return int(math.log10(n) + 1)

