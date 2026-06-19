# Time Complexity: O(log10(X))
# Space Complexity: O(1)
# Explanation: Negative numbers are not palindromes. Numbers ending in 0 (except 0 itself) are not palindromes. Reverse the second half of the number. If `x == reversed` or `x == reversed / 10` (for odd length), it's a palindrome.

def isPalindrome(x):
    if x < 0 or (x != 0 and x % 10 == 0): return False
    rev = 0
    while x > rev:
        rev = rev * 10 + x % 10
        x //= 10
    return x == rev or x == rev // 10

