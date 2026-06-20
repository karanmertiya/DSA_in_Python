# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Modify the Height/Depth algorithm. Calculate `left_depth + right_depth` at every node to find max diameter, while returning standard height.

def diameterOfBinaryTree(root: TreeNode) -> int:
    max_d = [0]
    def height(node):
        if not node: return 0
        left = height(node.left)
        right = height(node.right)
        max_d[0] = max(max_d[0], left + right)
        return 1 + max(left, right)
    height(root)
    return max_d[0]

