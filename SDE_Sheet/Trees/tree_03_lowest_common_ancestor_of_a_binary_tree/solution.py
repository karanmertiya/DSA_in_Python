# Time Complexity: O(N) (Constraint)
# Space Complexity: O(N)
# Explanation: Traverse the tree. If we find `p` or `q`, return it. If left and right subtrees both return non-null, the current node is the LCA. Otherwise, return the non-null subtree result.

def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if not root or root == p or root == q: return root
    
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    
    if not left: return right
    elif not right: return left
    else: return root

