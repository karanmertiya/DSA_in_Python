# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Remove all balanced brackets using a stack. The remaining string will be of the form `}}...{{...`. The required reversals will be `ceil(open_count/2) + ceil(close_count/2)`.

import math
def countRev(s):
    if len(s) % 2 != 0: return -1
    stack = []
    for c in s:
        if c == '{': stack.append(c)
        else:
            if stack and stack[-1] == '{': stack.pop()
            else: stack.append(c)
    open_count = stack.count('{')
    close_count = len(stack) - open_count
    return math.ceil(open_count / 2) + math.ceil(close_count / 2)

