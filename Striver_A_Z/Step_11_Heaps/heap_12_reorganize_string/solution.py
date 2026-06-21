# Time Complexity: O(N)
# Space Complexity: O(26)
# Explanation: Count frequencies. If max frequency > (len + 1) / 2, it's impossible. Fill the most frequent character at even indices (0, 2, 4...). Then fill the remaining characters alternately at remaining even indices and then odd indices.

import collections
def reorganizeString(s: str) -> str:
    counts = collections.Counter(s)
    max_f, letter = 0, ''
    for char, count in counts.items():
        if count > max_f:
            max_f = count
            letter = char
    if max_f > (len(s) + 1) // 2: return ""
    res = [''] * len(s)
    idx = 0
    while counts[letter] > 0:
        res[idx] = letter
        idx += 2
        counts[letter] -= 1
    for char, count in counts.items():
        while counts[char] > 0:
            if idx >= len(s): idx = 1
            res[idx] = char
            idx += 2
            counts[char] -= 1
    return "".join(res)

