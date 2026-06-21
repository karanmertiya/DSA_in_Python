# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Maintain a frequency map of `t`. Expand the window by moving `right`. When the window contains all characters of `t`, try to shrink it by moving `left` to find the minimum window. Keep track of the minimum window length and its starting index.

import collections
def minWindow(s: str, t: str) -> str:
    if len(s) < len(t): return ""
    count = collections.Counter(t)
    required = len(t)
    l = r = 0
    minLen = float('inf')
    minStart = 0
    while r < len(s):
        if count[s[r]] > 0:
            required -= 1
        count[s[r]] -= 1
        r += 1
        while required == 0:
            if r - l < minLen:
                minLen = r - l
                minStart = l
            count[s[l]] += 1
            if count[s[l]] > 0:
                required += 1
            l += 1
    return "" if minLen == float('inf') else s[minStart:minStart+minLen]

