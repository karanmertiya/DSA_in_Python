# Time Complexity: O(N log M) where M is unique characters
# Space Complexity: O(M)
# Explanation: Count frequencies of each character. Store pairs of `(frequency, character)` in a max-heap (or sort an array). Construct the result string by popping from the heap.

import collections
def frequencySort(s: str) -> str:
    counts = collections.Counter(s)
    return "".join([char * count for char, count in counts.most_common()])

