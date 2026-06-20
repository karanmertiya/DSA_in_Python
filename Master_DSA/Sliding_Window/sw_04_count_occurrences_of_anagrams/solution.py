# Time Complexity: O(N)
# Space Complexity: O(26) = O(1)
# Explanation: Maintain a frequency map of the pattern. Use a sliding window of size equal to the length of the pattern. Keep track of the number of characters fully matched (`count`). If `count` equals the number of unique characters in the pattern, an anagram is found.

import collections
def search(pat: str, txt: str) -> int:
    k, n = len(pat), len(txt)
    if k > n: return 0
    count = collections.Counter(pat)
    distinct = len(count)
    i = j = ans = 0
    while j < n:
        if txt[j] in count:
            count[txt[j]] -= 1
            if count[txt[j]] == 0:
                distinct -= 1
        if j - i + 1 < k:
            j += 1
        elif j - i + 1 == k:
            if distinct == 0:
                ans += 1
            if txt[i] in count:
                count[txt[i]] += 1
                if count[txt[i]] == 1:
                    distinct += 1
            i += 1
            j += 1
    return ans

