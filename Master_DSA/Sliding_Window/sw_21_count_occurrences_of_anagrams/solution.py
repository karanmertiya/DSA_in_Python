# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Use a sliding window of size `pat.length()`. Keep frequency map of `pat`. Track `count` of distinct characters to match. While moving window, decrease `count` if char frequency matches. If `count == 0`, increment answer.

def search(pat, txt):
    m = {}
    for c in pat: m[c] = m.get(c, 0) + 1
    count, ans, k = len(m), 0, len(pat)
    i = 0
    for j in range(len(txt)):
        if txt[j] in m:
            m[txt[j]] -= 1
            if m[txt[j]] == 0: count -= 1
        if j - i + 1 == k:
            if count == 0: ans += 1
            if txt[i] in m:
                m[txt[i]] += 1
                if m[txt[i]] == 1: count += 1
            i += 1
    return ans

