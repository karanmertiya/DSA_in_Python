# Time Complexity: O(N * K log K)
# Space Complexity: O(N * K)
# Explanation: Optimal: Use a hash map where the key is the sorted version of the string, and the value is a list of anagrams.

from collections import defaultdict
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    mpp = defaultdict(list)
    for s in strs:
        mpp[tuple(sorted(s))].append(s)
    return list(mpp.values())

