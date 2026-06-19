# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Store frequency of chars in `t`. Use `left` and `right` pointers. Expand `right`, if the character is in `t`, decrease its required count. If all characters are found, update the minimum length and start shrinking from `left`.

def minWindow(s, t):
    count = [0] * 128
    for c in t: count[ord(c)] += 1
    required = len(t)
    left, min_len, min_start = 0, float('inf'), 0
    for right in range(len(s)):
        if count[ord(s[right])] > 0: required -= 1
        count[ord(s[right])] -= 1
        while required == 0:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_start = left
            count[ord(s[left])] += 1
            if count[ord(s[left])] > 0: required += 1
            left += 1
    return "" if min_len == float('inf') else s[min_start:min_start + min_len]

