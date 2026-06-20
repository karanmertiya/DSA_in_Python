# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Use a frequency array of size 26. Increment for `s`, decrement for `t`. Check if all counts are 0.

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t): return False
    freq = [0] * 26
    for i in range(len(s)):
        freq[ord(s[i]) - ord('a')] += 1
        freq[ord(t[i]) - ord('a')] -= 1
    return all(count == 0 for count in freq)

