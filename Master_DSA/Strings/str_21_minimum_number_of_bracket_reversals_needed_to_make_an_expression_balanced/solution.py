# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: If the length of string is odd, return -1. Remove all balanced parts. The remaining string looks like `}}}{{{`. The number of reversals needed is `ceil(close/2) + ceil(open/2)`.

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

