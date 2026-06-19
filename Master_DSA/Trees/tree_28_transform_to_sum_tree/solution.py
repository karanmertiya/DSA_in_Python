# Time Complexity: O(N)
# Space Complexity: O(H)
# Explanation: Use a postorder traversal. For a node, store its original value. Update the node's value to the sum of its left and right subtrees. Return the old value plus the new value to the parent.

def toSumTree(root):
    def toSumTreeUtil(node):
        if not node: return 0
        old_val = node.data
        node.data = toSumTreeUtil(node.left) + toSumTreeUtil(node.right)
        return node.data + old_val
    toSumTreeUtil(root)

