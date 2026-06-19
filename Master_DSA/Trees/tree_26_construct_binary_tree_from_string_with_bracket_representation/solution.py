# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Use a recursive function. Read the number (handling negatives and multi-digits) to create the node. If the next character is `(`, make a recursive call for the left child. If there's another `(`, make a recursive call for the right child. Return the node.

class Node:
    def __init__(self, val): self.data = val; self.left = None; self.right = None
def treeFromString(s):
    if not s: return None
    idx = [0]
    def construct():
        if idx[0] >= len(s): return None
        num = 0; sign = 1
        if s[idx[0]] == '-': sign = -1; idx[0] += 1
        while idx[0] < len(s) and s[idx[0]].isdigit():
            num = num * 10 + int(s[idx[0]])
            idx[0] += 1
        node = Node(num * sign)
        if idx[0] < len(s) and s[idx[0]] == '(':
            idx[0] += 1
            node.left = construct()
            idx[0] += 1
        if idx[0] < len(s) and s[idx[0]] == '(':
            idx[0] += 1
            node.right = construct()
            idx[0] += 1
        return node
    return construct()

