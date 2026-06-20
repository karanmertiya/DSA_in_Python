# Time Complexity: O(H)
# Space Complexity: O(1)
# Explanation: Start from root. If `p.val >= root.val`, the successor must be in the right subtree (`root = root.right`). If `p.val < root.val`, the current root could be the successor, so record it and search the left subtree for a closer successor (`successor = root; root = root.left`).

def inorderSuccessor(root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
    successor = None
    while root:
        if p.val >= root.val:
            root = root.right
        else:
            successor = root
            root = root.left
    return successor

