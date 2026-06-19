# Time Complexity: O(N)
# Space Complexity: O(K)
# Explanation: Maintain a hash map of character frequencies. Expand the window by moving `j`. If the number of unique characters exceeds `k`, shrink the window from the left (`i`) until the number of unique characters is `k`. Update the maximum length when exactly `k` unique characters are present.

import collections
def longestKSubstr(s: str, k: int) -> int:
    count = collections.defaultdict(int)
    i = j = 0
    maxLen = -1
    while j < len(s):
        count[s[j]] += 1
        if len(count) == k:
            maxLen = max(maxLen, j - i + 1)
        elif len(count) > k:
            while len(count) > k:
                count[s[i]] -= 1
                if count[s[i]] == 0:
                    del count[s[i]]
                i += 1
        j += 1
    return maxLen

