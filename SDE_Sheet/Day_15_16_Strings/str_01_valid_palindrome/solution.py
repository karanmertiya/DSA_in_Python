# Time Complexity: O(N) (Constraint)
# Space Complexity: O(1) (Constraint)
# Explanation: Two-pointer approach skipping non-alphanumeric characters. Compare characters from both ends.

def isPalindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum(): left += 1
        while left < right and not s[right].isalnum(): right -= 1
        if s[left].lower() != s[right].lower(): return False
        left += 1; right -= 1
    return True

