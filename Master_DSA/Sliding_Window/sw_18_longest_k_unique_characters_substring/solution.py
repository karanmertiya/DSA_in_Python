# Time Complexity: O(N)
# Space Complexity: O(K)
# Explanation: Use a sliding window `[left, right]` and a hash map to count characters. If map size > K, shrink window from `left` until map size == K. If map size == K, update max length.

def longestKSubstr(s, k):
    m = {}
    left, max_len = 0, -1
    for right in range(len(s)):
        m[s[right]] = m.get(s[right], 0) + 1
        if len(m) == k: max_len = max(max_len, right - left + 1)
        elif len(m) > k:
            while len(m) > k:
                m[s[left]] -= 1
                if m[s[left]] == 0: del m[s[left]]
                left += 1
    return max_len

