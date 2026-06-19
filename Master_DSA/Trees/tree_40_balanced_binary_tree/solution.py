# Time Complexity: O(N)
# Space Complexity: O(H)
# Explanation: Modify the function that calculates the height of the tree. If at any node, the difference between the left and right subtree heights is greater than 1, or if any subtree is unbalanced, return -1. Otherwise, return the height.

def isBalanced(root):
    def checkHeight(node):
        if not node: return 0
        leftHeight = checkHeight(node.left)
        if leftHeight == -1: return -1
        rightHeight = checkHeight(node.right)
        if rightHeight == -1: return -1
        if abs(leftHeight - rightHeight) > 1: return -1
        return max(leftHeight, rightHeight) + 1
    return checkHeight(root) != -1

