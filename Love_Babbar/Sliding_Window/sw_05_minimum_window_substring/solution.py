# Time Complexity: O(N) (Constraint)
# Space Complexity: O(1)
# Explanation: Use a map to count required characters of `t`. Expand right pointer until `required == 0`. Then shrink left pointer to find minimum valid window.

def min_window(s: str, t: str) -> str:
    char_map = [0] * 256
    for char in t: char_map[ord(char)] += 1
    
    left = 0; required = len(t)
    min_len = float('inf'); start_idx = -1
    
    for right in range(len(s)):
        if char_map[ord(s[right])] > 0: required -= 1
        char_map[ord(s[right])] -= 1
        
        while required == 0:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                start_idx = left
            char_map[ord(s[left])] += 1
            if char_map[ord(s[left])] > 0: required += 1
            left += 1
            
    return "" if start_idx == -1 else s[start_idx:start_idx+min_len]

