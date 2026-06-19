# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Use two pointers, `left` starting at 0 and `right` starting at `n-1`. Skip non-alphanumeric characters. Compare the characters at `left` and `right` after converting to lowercase. If they mismatch, return false.

def isPalindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum(): left += 1
        while left < right and not s[right].isalnum(): right -= 1
        if s[left].lower() != s[right].lower(): return False
        left += 1; right -= 1
    return True

