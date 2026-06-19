# Time Complexity: O(N)
# Space Complexity: O(H)
# Explanation: Use a recursive postorder function. For each node, calculate the maximum path sum in its left and right subtrees (ignoring negative sums by taking max(0, sum)). Update the global `max_sum` with `node.val + left_sum + right_sum`. Return `node.val + max(left_sum, right_sum)` to be used by the parent.

def maxPathSum(root):
    maxi = float('-inf')
    def maxPathDown(node):
        nonlocal maxi
        if not node: return 0
        left = max(0, maxPathDown(node.left))
        right = max(0, maxPathDown(node.right))
        maxi = max(maxi, node.val + left + right)
        return node.val + max(left, right)
    maxPathDown(root)
    return maxi

