# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Create frequency arrays for `p` and a window of size `p.length()` in `s`. Slide the window across `s`, updating the window frequencies. If the arrays match, add the window's start index to the result.

def findAnagrams(s, p):
    ans = []
    if len(p) > len(s): return ans
    countP, countS = [0]*26, [0]*26
    for i in range(len(p)):
        countP[ord(p[i]) - ord('a')] += 1
        countS[ord(s[i]) - ord('a')] += 1
    if countP == countS: ans.append(0)
    for i in range(len(p), len(s)):
        countS[ord(s[i]) - ord('a')] += 1
        countS[ord(s[i - len(p)]) - ord('a')] -= 1
        if countP == countS: ans.append(i - len(p) + 1)
    return ans

