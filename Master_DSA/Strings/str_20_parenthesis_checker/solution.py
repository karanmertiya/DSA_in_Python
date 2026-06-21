# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Use a stack to keep track of opening brackets. If a closing bracket is encountered, check if it matches the top of the stack.

def ispar(x):
    stack = []
    for c in x:
        if c in '({[':
            stack.append(c)
        else:
            if not stack: return False
            if c == ')' and stack[-1] != '(': return False
            if c == '}' and stack[-1] != '{': return False
            if c == ']' and stack[-1] != '[': return False
            stack.pop()
    return len(stack) == 0

