# --- Brute Force Approach ---
# Time Complexity: O(log10(N)) (Trade-off)
# Space Complexity: O(log10(N)) (Trade-off)
# Edge Cases: <b>Negative Signs:</b> Reversing a string with '-' results in invalid parsing.
# Note: Convert to string, reverse the string, and parse back to integer.

def reverse_number_brute(n: int) -> int:
    # Edge Case: Explicitly store and remove sign before string conversion
    is_neg = n < 0
    s = str(abs(n))
    res = int(s[::-1])
    return -res if is_neg else res

# --- Optimal Approach ---
# Time Complexity: O(log10(N)) (Constraint)
# Space Complexity: O(1) (Constraint)
# Edge Cases: <b>Overflow Risk:</b> Number fits in 32-bit int, but its reverse might not. Forces explicit checks.
# Note: Extract digits using modulo 10 and build the reversed number mathematically.

def reverse_number_optimal(n: int) -> int:
    rev_num = 0
    sign = -1 if n < 0 else 1
    n = abs(n)
    while n > 0:
        ld = n % 10
        rev_num = (rev_num * 10) + ld
        n //= 10
    # Python handles arbitrarily large ints, but we enforce 32-bit constraint artificially if required.
    return sign * rev_num

