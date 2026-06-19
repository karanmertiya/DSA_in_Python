# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Use a sliding window. Keep expanding the window by adding characters. If a duplicate character is found, shrink the window from the left until the duplicate is removed.

def lengthOfLongestSubstring(s: str) -> int:
    seen = set()
    l = 0
    maxLen = 0
    for r in range(len(s)):
        while s[r] in seen:
            seen.remove(s[l])
            l += 1
        seen.add(s[r])
        maxLen = max(maxLen, r - l + 1)
    return maxLen

