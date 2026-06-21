# Time Complexity: O(N)
# Space Complexity: O(H)
# Explanation: DFS returning max path sum down a single branch. At any node, max path = `node.val + max(0, leftPath) + max(0, rightPath)`. Ignore negative branches.

def maxPathSum(root: Optional[TreeNode]) -> int:
    maxi = [float('-inf')]
    def maxPathDown(node):
        if not node: return 0
        left = max(0, maxPathDown(node.left))
        right = max(0, maxPathDown(node.right))
        maxi[0] = max(maxi[0], left + right + node.val)
        return max(left, right) + node.val
    maxPathDown(root)
    return int(maxi[0])

