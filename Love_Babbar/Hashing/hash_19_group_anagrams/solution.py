# Time Complexity: O(N * K log K) where K is max string length
# Space Complexity: O(N * K)
# Explanation: Use a hash map. The key is the sorted version of the string (or a character count string), and the value is a list of original strings that match this key.

from collections import defaultdict
def groupAnagrams(strs):
    m = defaultdict(list)
    for s in strs:
        m[tuple(sorted(s))].append(s)
    return list(m.values())

