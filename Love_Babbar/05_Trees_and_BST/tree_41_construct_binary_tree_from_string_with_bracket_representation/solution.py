# Time Complexity: O(N)
# Space Complexity: O(H)
# Explanation: Iterate through string. If digit or sign, parse number and create node. If '(', continue. If node created, push to stack. If ')', pop from stack. If it has a parent, attach it (left first, then right).

def treeFromString(s: str):
    if not s: return None
    stack = []
    i = 0
    while i < len(s):
        if s[i] == ')':
            stack.pop()
            i += 1
        elif s[i] == '(':
            i += 1
        else:
            j = i
            while j < len(s) and (s[j].isdigit() or s[j] == '-'): j += 1
            node = TreeNode(int(s[i:j]))
            if stack:
                parent = stack[-1]
                if not parent.left: parent.left = node
                else: parent.right = node
            stack.append(node)
            i = j
    return stack[0]

