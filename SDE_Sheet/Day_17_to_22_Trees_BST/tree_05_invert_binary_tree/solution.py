# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Recursively swap the left and right children of every node.

def invertTree(root: TreeNode) -> TreeNode:
    if not root: return None
    root.left, root.right = root.right, root.left
    invertTree(root.left)
    invertTree(root.right)
    return root

