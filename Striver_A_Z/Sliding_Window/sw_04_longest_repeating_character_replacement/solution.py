# Time Complexity: O(N) (Constraint)
# Space Complexity: O(1) (Constraint)
# Explanation: Sliding window tracking the `max_frequency_count` inside the window. If `window_len - max_freq > k`, slide the window.

def character_replacement(s: str, k: int) -> int:
    count = [0] * 26
    left = max_freq = 0
    for right in range(len(s)):
        count[ord(s[right]) - 65] += 1
        max_freq = max(max_freq, count[ord(s[right]) - 65])
        
        if (right - left + 1) - max_freq > k:
            count[ord(s[left]) - 65] -= 1
            left += 1
    return len(s) - left

