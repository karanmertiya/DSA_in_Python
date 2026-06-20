# Time Complexity: O(N log K) where K is unique chars
# Space Complexity: O(K)
# Explanation: Optimal: Count frequencies using a hash map. Add pairs `(freq, char)` to a max heap or vector and sort. Reconstruct string.

from collections import Counter
def frequencySort(s):
    counts = Counter(s)
    return "".join(char * count for char, count in counts.most_common())

