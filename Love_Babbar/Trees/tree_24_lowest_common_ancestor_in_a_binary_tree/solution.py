# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: If root is null or root matches n1 or n2, return root. Recurse for left and right. If both return non-null, root is LCA. If one returns non-null, return that one.

def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root or root == p or root == q: return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    if not left: return right
    if not right: return left
    return root

