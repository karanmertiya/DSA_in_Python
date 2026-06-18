# --- Brute Force Approach ---
# Time Complexity: O(log10(N)) (Constraint)
# Space Complexity: O(1) (Constraint)
# Edge Cases: <b>Sign Edge Case:</b> Fails on N=0. Requires explicit check.
# Note: Divide by 10 continuously until N becomes 0.

def count_digits_brute(n: int) -> int:
    # Edge Case: Handle N=0 specifically
    if n <= 0: return 1
    cnt = 0
    while n > 0:
        cnt += 1
        n //= 10
    return cnt

# --- Better Approach ---
# Time Complexity: O(1) (Constraint)
# Space Complexity: O(log10(N)) (Trade-off)
# Edge Cases: <b>Memory Trade-off:</b> String allocation required. Avoid for strictly O(1) space constraints.
# Note: Convert number to string and return length.

def count_digits_better(n: int) -> int:
    # Trade-off: Allocates string memory proportional to digit count
    return len(str(n))

# --- Optimal Approach ---
# Time Complexity: O(1) (Constraint)
# Space Complexity: O(1) (Constraint)
# Edge Cases: <b>Library Requirement:</b> Must use math library. Fails if standard libraries are restricted.
# Note: Use base-10 logarithm to find digit count mathematically.

import math

def count_digits_optimal(n: int) -> int:
    # Edge Case check for zero
    if n <= 0: return 1
    return int(math.log10(n) + 1)

