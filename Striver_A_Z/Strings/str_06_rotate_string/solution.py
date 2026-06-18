# Time Complexity: O(N) (Constraint)
# Space Complexity: O(N) (Trade-off)
# Explanation: If s and goal have the same length, check if `goal` is a substring of `s + s`.

def rotate_string(s: str, goal: str) -> bool:
    if len(s) != len(goal): return False
    return goal in (s + s)

