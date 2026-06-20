# Time Complexity: O(N)
# Space Complexity: O(H)
# Explanation: First, check if the tree is complete by counting nodes and ensuring no node's index `i > count`. Then check if every node satisfies the max-heap property (`node.val >= left.val` and `node.val >= right.val`).

def isHeap(tree: Node) -> bool:
    def countNodes(node):
        if not node: return 0
        return 1 + countNodes(node.left) + countNodes(node.right)
    def isCBT(node, index, count):
        if not node: return True
        if index >= count: return False
        return isCBT(node.left, 2 * index + 1, count) and isCBT(node.right, 2 * index + 2, count)
    def isMaxOrder(node):
        if not node.left and not node.right: return True
        if not node.right: return node.data >= node.left.data
        return (node.data >= node.left.data and node.data >= node.right.data and
                isMaxOrder(node.left) and isMaxOrder(node.right))
    count = countNodes(tree)
    return isCBT(tree, 0, count) and isMaxOrder(tree)

