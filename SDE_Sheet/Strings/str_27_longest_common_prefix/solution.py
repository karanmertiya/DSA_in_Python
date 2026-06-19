# Time Complexity: O(N log N * M)
# Space Complexity: O(1)
# Explanation: Sort the array of strings. Compare the first and the last string in the sorted array, as they will be the most different. The common prefix of these two will be the common prefix for all.

def longestCommonPrefix(strs):
    if not strs: return ""
    strs.sort()
    first, last = strs[0], strs[-1]
    i = 0
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1
    return first[:i]

