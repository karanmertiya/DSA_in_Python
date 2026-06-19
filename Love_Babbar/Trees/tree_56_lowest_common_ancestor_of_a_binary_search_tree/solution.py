# Time Complexity: O(H)
# Space Complexity: O(1)
# Explanation: Start at root. If both `p` and `q` are less than root, move left. If both are greater, move right. Otherwise, the current node is the LCA.

def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root
    return None

