# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Use two arrays to map characters from `s` to `t` and `t` to `s`. If `s[i]` is mapped to a character other than `t[i]`, or `t[i]` is mapped to a character other than `s[i]`, return false. Else, create the mappings.

def isIsomorphic(s, t):
    m1, m2 = [-1] * 256, [-1] * 256
    for i in range(len(s)):
        if m1[ord(s[i])] != m2[ord(t[i])]: return False
        m1[ord(s[i])] = i
        m2[ord(t[i])] = i
    return True

