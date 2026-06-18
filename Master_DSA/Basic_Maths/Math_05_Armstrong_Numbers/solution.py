# --- Optimal Approach ---
# Time Complexity: O(log10(N)) (Constraint)
# Space Complexity: O(1) (Constraint)
# Edge Cases: <b>Two-Pass Logic:</b> Requires digit count upfront before processing sum of powers.
# Note: Calculate digit count first, then mathematically extract digits and compute power sums.

import math

def is_armstrong(n: int) -> bool:
    dup = n
    sum_val = 0
    digits = int(math.log10(n) + 1) if n > 0 else 1
    while n > 0:
        ld = n % 10
        sum_val += ld ** digits
        n //= 10
    return sum_val == dup

