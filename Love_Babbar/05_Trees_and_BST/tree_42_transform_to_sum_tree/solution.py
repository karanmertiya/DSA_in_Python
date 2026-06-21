# Time Complexity: O(N)
# Space Complexity: O(H)
# Explanation: Recursively get the sum of the left subtree and right subtree. Update current node's value to the sum of left and right. Return the old value of current node + sum of left + sum of right to the caller.

def toSumTree(root):
    def helper(node):
        if not node: return 0
        leftSum = helper(node.left)
        rightSum = helper(node.right)
        oldVal = node.val
        node.val = leftSum + rightSum
        return node.val + oldVal
    helper(root)

