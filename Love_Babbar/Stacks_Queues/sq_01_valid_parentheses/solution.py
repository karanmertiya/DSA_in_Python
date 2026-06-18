# Time Complexity: O(N) (Constraint)
# Space Complexity: O(N)
# Explanation: Use a Stack. Push opening brackets. For closing brackets, pop the stack and check if it matches the corresponding opening bracket.

def is_valid(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top: return False
        else:
            stack.append(char)
    return not stack

