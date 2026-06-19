# Time Complexity: O(N log N * M)
# Space Complexity: O(1) auxiliary
# Explanation: Sort the array of strings. Compare only the first and last strings in the sorted array, as they will have the most differing characters.

def longestCommonPrefix(strs: List[str]) -> str:
    if not strs: return ""
    strs.sort()
    first, last = strs[0], strs[-1]
    i = 0
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1
    return first[:i]

