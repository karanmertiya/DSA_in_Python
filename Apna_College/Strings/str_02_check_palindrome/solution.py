# Time Complexity: O(N) (Constraint)
# Space Complexity: O(N) (Trade-off)
# Explanation: Clean the string to remove non-alphanumeric characters, convert to lowercase, and check if it equals its reverse.

def is_palindrome_brute(s: str) -> bool:
    clean = "".join(c.lower() for c in s if c.isalnum())
    return clean == clean[::-1]

# Time Complexity: O(N) (Constraint)
# Space Complexity: O(1) (Constraint)
# Explanation: Two-pointer approach skipping non-alphanumeric characters in a single pass without extra memory.

def is_palindrome_optimal(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum(): left += 1
        while left < right and not s[right].isalnum(): right -= 1
        if s[left].lower() != s[right].lower(): return False
        left += 1; right -= 1
    return True

