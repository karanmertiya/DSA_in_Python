# Time Complexity: O(N<sup>2</sup>) (Constraint)
# Space Complexity: O(1)
# Explanation: Expand Around Center. A palindrome can have an odd (center is 1 char) or even (center is between 2 chars) length. Test both.

def longestPalindrome(s: str) -> str:
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
        
    start, max_len = 0, 0
    for i in range(len(s)):
        len1 = expand(i, i)
        len2 = expand(i, i + 1)
        l = max(len1, len2)
        if l > max_len:
            max_len = l
            start = i - (l - 1) // 2
    return s[start : start + max_len]

