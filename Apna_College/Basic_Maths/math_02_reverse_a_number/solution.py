# Time Complexity: O(log10(N))
# Space Complexity: O(log10(N)) (Trade-off)
# Explanation: Convert to string, reverse the string, and parse back to integer.

def reverse_number_brute(n: int) -> int:
    # Edge Case: Explicitly store and remove sign before string conversion
    is_neg = n < 0
    s = str(abs(n))
    res = int(s[::-1])
    if res > 2**31 - 1: return 0
    return -res if is_neg else res

# Time Complexity: O(log10(N))
# Space Complexity: O(1)
# Explanation: Extract digits using modulo 10 and build the reversed number mathematically.

def reverse_number_optimal(n: int) -> int:
    rev_num = 0
    sign = -1 if n < 0 else 1
    n = abs(n)
    while n > 0:
        ld = n % 10
        rev_num = (rev_num * 10) + ld
        n //= 10
    if rev_num > 2**31 - 1: return 0
    return sign * rev_num

