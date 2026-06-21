# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Modify the Height algorithm. If the difference between `left` and `right` height is > 1, return `-1` to propagate the unbalanced signal.

def isBalanced(root: TreeNode) -> bool:
    def checkHeight(node):
        if not node: return 0
        left = checkHeight(node.left)
        if left == -1: return -1
        right = checkHeight(node.right)
        if right == -1: return -1
        if abs(left - right) > 1: return -1
        return 1 + max(left, right)
    return checkHeight(root) != -1

