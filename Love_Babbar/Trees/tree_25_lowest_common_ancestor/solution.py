# Time Complexity: O(N)
# Space Complexity: O(H)
# Explanation: DFS traversal. If the current node is p or q, return the current node. Recurse left and right. If both left and right return non-null, the current node is the LCA. If one returns non-null, return that one.

def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if root is None or root == p or root == q: return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    if left is None: return right
    elif right is None: return left
    else: return root

