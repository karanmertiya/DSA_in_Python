# Time Complexity: O(N) (Constraint)
# Space Complexity: O(H) &cong; O(N) (Constraint)
# Explanation: Recursively find the max depth of left and right subtrees. The depth of the current node is `1 + max(left_depth, right_depth)`.

def max_depth(root: TreeNode) -> int:
    if not root: return 0
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    return 1 + max(left_depth, right_depth)

