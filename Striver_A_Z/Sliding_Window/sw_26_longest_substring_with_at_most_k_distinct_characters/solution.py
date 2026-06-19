# Time Complexity: O(N)
# Space Complexity: O(K)
# Explanation: Sliding window with hash map to count characters. While map size > k, shrink window from left.

def lengthOfLongestSubstringKDistinct(s, k):
    m = {}
    left, max_len = 0, 0
    for right in range(len(s)):
        m[s[right]] = m.get(s[right], 0) + 1
        while len(m) > k:
            m[s[left]] -= 1
            if m[s[left]] == 0: del m[s[left]]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len

