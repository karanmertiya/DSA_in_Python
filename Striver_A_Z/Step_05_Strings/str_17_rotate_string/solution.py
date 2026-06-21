# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: If the lengths of `s` and `goal` are not equal, return false. Otherwise, concatenate `s` with itself (`s + s`). If `goal` is a substring of `s + s`, then it's a rotated string.

def rotateString(s, goal):
    if len(s) != len(goal): return False
    return goal in (s + s)

