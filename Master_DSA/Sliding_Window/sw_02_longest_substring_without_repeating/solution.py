# Time Complexity: O(2N) &cong; O(N) (Trade-off)
# Space Complexity: O(N) (Trade-off)
# Explanation: Use a Hash Set to track characters in the current window. If a duplicate is found, shrink the window from the left.

def length_of_longest_substring_better(s: str) -> int:
    char_set = set()
    left = max_len = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len

# Time Complexity: O(N) (Constraint)
# Space Complexity: O(1) (Constraint)
# Explanation: Optimal: Store the latest index of each character in a Hash Map. Jump `left` directly to `map[char] + 1`.

def length_of_longest_substring_optimal(s: str) -> int:
    char_index = {}
    left = max_len = 0
    for right, char in enumerate(s):
        if char in char_index:
            left = max(left, char_index[char] + 1)
        char_index[char] = right
        max_len = max(max_len, right - left + 1)
    return max_len

