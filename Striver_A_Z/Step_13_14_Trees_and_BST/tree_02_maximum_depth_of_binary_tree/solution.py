# Time Complexity: O(N)
# Space Complexity: O(H) &cong; O(N)
# Explanation: Recursively find the max depth of left and right subtrees. The depth is `1 + max(left_depth, right_depth)`.

def maxDepth(root: TreeNode) -> int:
    if not root: return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))

