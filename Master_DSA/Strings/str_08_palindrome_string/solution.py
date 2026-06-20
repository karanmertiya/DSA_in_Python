# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Use two pointers, `left` at the beginning and `right` at the end of the string. Compare the characters at these pointers. If they are different, return 0. Move pointers towards each other. If all characters match, return 1.

def isPalindrome(S: str) -> int:
    left, right = 0, len(S) - 1
    while left < right:
        if S[left] != S[right]:
            return 0
        left += 1
        right -= 1
    return 1

