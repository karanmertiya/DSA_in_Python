# Time Complexity: O(N^2)
# Space Complexity: O(1)
# Explanation: For each character, treat it as the center of an odd-length palindrome and expand outwards. Also treat it and the next character as the center of an even-length palindrome and expand outwards. Keep track of the longest palindrome found.

def longestPalindrome(S: str) -> str:
    start = 0; maxLen = 1; n = len(S)
    for i in range(n):
        l = r = i
        while l >= 0 and r < n and S[l] == S[r]:
            if r - l + 1 > maxLen:
                start = l; maxLen = r - l + 1
            l -= 1; r += 1
        l = i; r = i + 1
        while l >= 0 and r < n and S[l] == S[r]:
            if r - l + 1 > maxLen:
                start = l; maxLen = r - l + 1
            l -= 1; r += 1
    return S[start:start+maxLen]

