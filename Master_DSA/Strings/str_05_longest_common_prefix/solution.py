# Time Complexity: O(N log N * M) (Trade-off)
# Space Complexity: O(1)
# Explanation: Sort the array of strings. The longest common prefix of the entire array must be the common prefix of the first and last strings in the sorted array.

def longest_common_prefix(strs: list[str]) -> str:
    if not strs: return ""
    strs.sort()
    first, last = strs[0], strs[-1]
    i = 0
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1
    return first[:i]

