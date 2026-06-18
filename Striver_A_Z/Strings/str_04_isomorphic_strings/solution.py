# Time Complexity: O(N) (Constraint)
# Space Complexity: O(1) (Constraint)
# Explanation: Use two arrays to map characters from `s -> t` and `t -> s` ensuring a 1-to-1 bijective mapping.

def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t): return False
    mapST, mapTS = {}, {}
    for c1, c2 in zip(s, t):
        if (c1 in mapST and mapST[c1] != c2) or (c2 in mapTS and mapTS[c2] != c1):
            return False
        mapST[c1] = c2
        mapTS[c2] = c1
    return True

