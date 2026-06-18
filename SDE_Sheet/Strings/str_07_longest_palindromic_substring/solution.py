# Time Complexity: O(N<sup>2</sup>) (Constraint)
# Space Complexity: O(1) (Constraint)
# Explanation: Expand Around Center: For each character, treat it as the center of an odd and even length palindrome and expand outwards.

def longest_palindrome(s: str) -> str:
    if not s: return ""
    start, max_len = 0, 0
    def expand(l, r):
        nonlocal start, max_len
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > max_len:
                max_len = r - l + 1
                start = l
            l -= 1; r += 1
            
    for i in range(len(s)):
        expand(i, i)     # Odd length
        expand(i, i + 1) # Even length
    return s[start:start+max_len]

