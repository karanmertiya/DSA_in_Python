# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Iterate through the string. Maintain a `current_depth` counter. If we see `(`, increment the counter and update `max_depth`. If we see `)`, decrement the counter. Ignore other characters.

def maxDepth(s):
    max_d = cur_d = 0
    for c in s:
        if c == '(':
            cur_d += 1
            max_d = max(max_d, cur_d)
        elif c == ')':
            cur_d -= 1
    return max_d

