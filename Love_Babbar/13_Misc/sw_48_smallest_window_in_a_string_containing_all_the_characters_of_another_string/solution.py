# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Same as Minimum Window Substring. Use frequency map of `P` and a sliding window over `S`. Shrink window from left when all characters match to find the minimum length.

def smallestWindow(s, p):
    if len(p) > len(s): return "-1"
    m = {}
    for c in p: m[c] = m.get(c, 0) + 1
    count, minLen, start, i = len(m), float('inf'), 0, 0
    for j in range(len(s)):
        if s[j] in m:
            m[s[j]] -= 1
            if m[s[j]] == 0: count -= 1
        while count == 0:
            if j - i + 1 < minLen:
                minLen = j - i + 1
                start = i
            if s[i] in m:
                m[s[i]] += 1
                if m[s[i]] > 0: count += 1
            i += 1
    return "-1" if minLen == float('inf') else s[start:start+minLen]

