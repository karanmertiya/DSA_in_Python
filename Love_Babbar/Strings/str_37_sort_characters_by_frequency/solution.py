# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Count frequencies using a map. Then, sort the map entries by frequency in descending order, or use a Max Heap, or use Bucket Sort (where index is frequency and value is a list of characters). Build the new string by appending each character `freq` times.

from collections import Counter
def frequencySort(s):
    counts = Counter(s)
    return "".join(char * count for char, count in counts.most_common())

