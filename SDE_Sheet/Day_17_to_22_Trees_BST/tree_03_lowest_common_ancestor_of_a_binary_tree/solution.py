# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: If we find `p` or `q`, return it. If both left and right return non-null, current node is LCA.

def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if not root or root == p or root == q: return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    if not left: return right
    elif not right: return left
    else: return root

