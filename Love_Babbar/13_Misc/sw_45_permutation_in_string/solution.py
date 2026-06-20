# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Use a sliding window of size `len(s1)` over `s2`. Maintain frequency arrays for `s1` and the current window in `s2`. Compare arrays at each step.

def checkInclusion(s1, s2):
    if len(s1) > len(s2): return False
    c1, c2 = [0]*26, [0]*26
    for i in range(len(s1)):
        c1[ord(s1[i]) - 97] += 1
        c2[ord(s2[i]) - 97] += 1
    if c1 == c2: return True
    for i in range(len(s1), len(s2)):
        c2[ord(s2[i]) - 97] += 1
        c2[ord(s2[i - len(s1)]) - 97] -= 1
        if c1 == c2: return True
    return False

