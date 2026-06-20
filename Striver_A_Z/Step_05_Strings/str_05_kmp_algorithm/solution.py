# Time Complexity: O(N + M)
# Space Complexity: O(M)
# Explanation: Compute the LPS (Longest Proper Prefix which is also Suffix) array for the needle. Use the LPS array to skip characters while matching with the haystack, reducing time to O(N+M).

def strStr(haystack: str, needle: str) -> int:
    if not needle: return 0
    m, n = len(needle), len(haystack)
    lps = [0] * m
    length, i = 0, 1
    while i < m:
        if needle[i] == needle[length]:
            length += 1
            lps[i] = length; i += 1
        else:
            if length != 0: length = lps[length - 1]
            else: lps[i] = 0; i += 1
    i = j = 0
    while i < n:
        if needle[j] == haystack[i]: i += 1; j += 1
        if j == m: return i - j
        elif i < n and needle[j] != haystack[i]:
            if j != 0: j = lps[j - 1]
            else: i += 1
    return -1

