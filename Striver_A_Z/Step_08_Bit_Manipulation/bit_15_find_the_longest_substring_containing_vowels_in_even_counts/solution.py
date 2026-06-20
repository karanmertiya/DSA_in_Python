# Time Complexity: O(N)
# Space Complexity: O(32) since only 5 bits used
# Explanation: Use a 5-bit mask to represent the parity of counts for 'a','e','i','o','u'. If we encounter a vowel, flip its bit. If the same mask is seen again at index `i` (was previously seen at `j`), then the substring `s[j+1...i]` has even vowel counts. Use a hash map to store first occurrence of each mask.

def findTheLongestSubstring(s: str) -> int:
    m = {0: -1}
    mask, maxLen = 0, 0
    vowels = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
    for i, char in enumerate(s):
        if char in vowels:
            mask ^= (1 << vowels[char])
        if mask in m:
            maxLen = max(maxLen, i - m[mask])
        else:
            m[mask] = i
    return maxLen

