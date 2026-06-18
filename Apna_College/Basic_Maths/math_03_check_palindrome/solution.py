# Time Complexity: O(log10(N))
# Space Complexity: O(log10(N)) (Trade-off)
# Explanation: Convert the number to a string and compare it with its reversed version.

def is_palindrome_brute(n: int) -> bool:
    s = str(n)
    return s == s[::-1]

# Time Complexity: O(log10(N))
# Space Complexity: O(1)
# Explanation: Reverse the number mathematically and compare it to the original.

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

