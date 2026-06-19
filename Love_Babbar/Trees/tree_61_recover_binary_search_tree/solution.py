# Time Complexity: O(N)
# Space Complexity: O(H) or O(1) with Morris
# Explanation: Maintain `prev`, `first`, `middle`, and `last` pointers during inorder traversal. If `prev.val > root.val`, a violation occurred. The first violation points to `first=prev` and `middle=root`. A second violation (if any) points to `last=root`. Finally, swap values of `first` and `last` (or `first` and `middle` if adjacent).

def recoverTree(root: Optional[TreeNode]) -> None:
    first = middle = last = prev = None
    def inorder(node):
        nonlocal first, middle, last, prev
        if not node: return
        inorder(node.left)
        if prev and node.val < prev.val:
            if not first:
                first, middle = prev, node
            else:
                last = node
        prev = node
        inorder(node.right)
    inorder(root)
    if first and last:
        first.val, last.val = last.val, first.val
    elif first and middle:
        first.val, middle.val = middle.val, first.val

