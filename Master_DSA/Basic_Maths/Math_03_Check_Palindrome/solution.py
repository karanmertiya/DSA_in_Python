# --- Optimal Approach ---
# Time Complexity: O(log10(N)) (Constraint)
# Space Complexity: O(1) (Constraint)
# Edge Cases: <b>Variable Requirement:</b> Number is destroyed during loop, requires `dup` variable for final check.
# Note: Reverse the number mathematically and compare it to the original.

def is_palindrome_optimal(n: int) -> bool:
    # Edge Case: Negative numbers are strictly not palindromes
    if n < 0: return False
    
    dup = n
    rev_num = 0
    while n > 0:
        ld = n % 10
        rev_num = (rev_num * 10) + ld
        n //= 10
    return dup == rev_num

