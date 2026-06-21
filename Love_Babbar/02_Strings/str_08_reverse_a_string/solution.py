# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Use two pointers, `left` at the beginning and `right` at the end of the string. Swap the characters at these pointers and move them towards each other until they meet.

def reverseString(s: List[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

