# Time Complexity: O(N)
# Space Complexity: O(min(N, M))
# Explanation: Sliding window with a Hash Map storing the latest index of each character. Move `left` pointer to `max(left, map[char] + 1)`.

def lengthOfLongestSubstring(s: str) -> int:
    mpp = {}
    left = max_len = 0
    for right, char in enumerate(s):
        if char in mpp:
            left = max(left, mpp[char] + 1)
        mpp[char] = right
        max_len = max(max_len, right - left + 1)
    return max_len

