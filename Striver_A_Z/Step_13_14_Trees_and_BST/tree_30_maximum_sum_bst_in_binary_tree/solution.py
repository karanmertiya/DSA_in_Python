# Time Complexity: O(N)
# Space Complexity: O(H)
# Explanation: Bottom-up traversal. Return `[isBST, minNode, maxNode, sum]`. Update global max sum when valid BST is found.

class Info:
    def __init__(self, isBST, minNode, maxNode, sum_val):
        self.isBST = isBST
        self.minNode = minNode
        self.maxNode = maxNode
        self.sum = sum_val
def maxSumBST(root: Optional[TreeNode]) -> int:
    maxSum = 0
    def solve(node):
        nonlocal maxSum
        if not node: return Info(True, float('inf'), float('-inf'), 0)
        left = solve(node.left)
        right = solve(node.right)
        if left.isBST and right.isBST and left.maxNode < node.val < right.minNode:
            currSum = left.sum + right.sum + node.val
            maxSum = max(maxSum, currSum)
            return Info(True, min(node.val, left.minNode), max(node.val, right.maxNode), currSum)
        return Info(False, float('-inf'), float('inf'), max(left.sum, right.sum))
    solve(root)
    return maxSum if maxSum > 0 else 0

