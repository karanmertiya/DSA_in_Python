# Time Complexity: O(N)
# Space Complexity: O(H)
# Explanation: Return `[minNode, maxNode, maxSize]` from each subtree. For current node, if `left.max < node.val < right.min`, it's a BST. Return `[min(node.val, left.min), max(node.val, right.max), left.size + right.size + 1]`. Else, it's not a BST, return `[-inf, inf, max(left.size, right.size)]`.

class NodeValue:
    def __init__(self, minNode, maxNode, maxSize):
        self.minNode = minNode
        self.maxNode = maxNode
        self.maxSize = maxSize
def largestBSTSubtreeHelper(root):
    if not root: return NodeValue(float('inf'), float('-inf'), 0)
    left = largestBSTSubtreeHelper(root.left)
    right = largestBSTSubtreeHelper(root.right)
    if left.maxNode < root.data < right.minNode:
        return NodeValue(min(root.data, left.minNode), max(root.data, right.maxNode), left.maxSize + right.maxSize + 1)
    return NodeValue(float('-inf'), float('inf'), max(left.maxSize, right.maxSize))
def largestBst(root):
    return largestBSTSubtreeHelper(root).maxSize

