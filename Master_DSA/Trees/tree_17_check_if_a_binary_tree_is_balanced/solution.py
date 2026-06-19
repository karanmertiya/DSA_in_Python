# Time Complexity: O(N)
# Space Complexity: O(N) recursion stack
# Explanation: Modify the `maxDepth` function to return -1 if the tree is not balanced. If `abs(left - right) > 1` or either subtree returns -1, return -1. Otherwise, return `max(left, right) + 1`.

def isBalanced(root: Optional[TreeNode]) -> bool:
    def dfs(node):
        if not node: return 0
        left = dfs(node.left)
        if left == -1: return -1
        right = dfs(node.right)
        if right == -1: return -1
        if abs(left - right) > 1: return -1
        return max(left, right) + 1
    return dfs(root) != -1

