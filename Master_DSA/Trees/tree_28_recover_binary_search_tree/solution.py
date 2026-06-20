# Time Complexity: O(N)
# Space Complexity: O(H)
# Explanation: Inorder traversal of BST gives sorted array. If two are swapped, there will be 1 or 2 anomalies where `prev->val > curr->val`. First anomaly: `first = prev`, `middle = curr`. Second anomaly: `last = curr`. Swap `first` and `last` (or `first` and `middle` if adjacent).

def recoverTree(root: Optional[TreeNode]) -> None:
    first = middle = last = prev = None
    def inorder(node):
        nonlocal first, middle, last, prev
        if not node: return
        inorder(node.left)
        if prev and node.val < prev.val:
            if not first:
                first = prev
                middle = node
            else:
                last = node
        prev = node
        inorder(node.right)
    inorder(root)
    if first and last:
        first.val, last.val = last.val, first.val
    elif first and middle:
        first.val, middle.val = middle.val, first.val

