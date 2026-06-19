# Time Complexity: O(N log 26)
# Space Complexity: O(26)
# Explanation: Hash map to store frequencies, then max-heap to process them in descending order of frequency.

import collections
def frequencySort(s: str) -> str:
    counts = collections.Counter(s)
    ans = ""
    for char, freq in counts.most_common():
        ans += char * freq
    return ans

