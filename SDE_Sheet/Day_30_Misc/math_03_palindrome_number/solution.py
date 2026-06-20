# Time Complexity: O(log10 x)
# Space Complexity: O(1)
# Explanation: Negative numbers are false. Reverse half the number. If original equals reversed, it is a palindrome.

def isPalindrome(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0): return False
    rev = 0
    while x > rev:
        rev = rev * 10 + x % 10
        x //= 10
    return x == rev or x == rev // 10

