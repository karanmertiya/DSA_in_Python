# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Use a sliding window. Maintain the character frequencies and the `max_freq` in the window. The number of replacements needed is `window_size - max_freq`. If this is > k, shrink the window from left and decrement the corresponding frequency.

def characterReplacement(s, k):
    count = [0] * 26
    left = 0
    max_freq = 0
    max_len = 0
    for right in range(len(s)):
        count[ord(s[right]) - ord('A')] += 1
        max_freq = max(max_freq, count[ord(s[right]) - ord('A')])
        if (right - left + 1) - max_freq > k:
            count[ord(s[left]) - ord('A')] -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len

