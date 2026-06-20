# Time Complexity: O(N + M) (Constraint)
# Space Complexity: O(N + M) (Trade-off)
# Explanation: Insert all elements from both arrays into a Hash Set. The Set natively drops duplicates.

def find_union(a: list[int], b: list[int]) -> list[int]:
    # Set union operator implicitly merges and drops duplicates
    s = set(a) | set(b)
    return list(s)

