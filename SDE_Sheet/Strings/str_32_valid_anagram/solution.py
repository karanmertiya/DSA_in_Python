# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: If lengths differ, return false. Create an array of size 26. Increment counts for characters in `s` and decrement for characters in `t`. If all counts are 0, it's an anagram.

def isAnagram(s, t):
    if len(s) != len(t): return False
    count = [0] * 26
    for char_s, char_t in zip(s, t):
        count[ord(char_s) - ord('a')] += 1
        count[ord(char_t) - ord('a')] -= 1
    return all(c == 0 for c in count)

