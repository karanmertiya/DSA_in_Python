# Time Complexity: O(N log N * M) (Constraint)
# Space Complexity: O(1) / O(M)
# Explanation: Sort the array. The common prefix will be constrained by the first and last strings in the sorted array.

def longestCommonPrefix(strs: list[str]) -> str:
    if not strs: return ""
    strs.sort()
    first, last = strs[0], strs[-1]
    i = 0
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1
    return first[:i]

