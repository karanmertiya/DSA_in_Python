# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Use a helper function that takes the string and an index pointer. Extract the number. Then if there's a '(' build left tree, and if there's another '(' build right tree.

def treeFromString(s: str) -> Optional[TreeNode]:
    i = 0
    def helper():
        nonlocal i
        if i >= len(s): return None
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        num = 0
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        root = TreeNode(num * sign)
        if i < len(s) and s[i] == '(':
            i += 1
            root.left = helper()
            i += 1
        if i < len(s) and s[i] == '(':
            i += 1
            root.right = helper()
            i += 1
        return root
    return helper()

