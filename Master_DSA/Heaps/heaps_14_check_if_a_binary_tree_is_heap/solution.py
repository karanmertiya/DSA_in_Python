# Time Complexity: O(N)
# Space Complexity: O(H)
# Explanation: Use recursion to check two properties: 1. Is it a Complete Binary Tree? (Count nodes and ensure index of any node is < total count). 2. Is it a Max Heap? (Parent data >= children data).

def countNodes(root):
    if not root: return 0
    return 1 + countNodes(root.left) + countNodes(root.right)
def isCBT(root, index, count):
    if not root: return True
    if index >= count: return False
    return isCBT(root.left, 2 * index + 1, count) and isCBT(root.right, 2 * index + 2, count)
def isMaxOrder(root):
    if not root.left and not root.right: return True
    if not root.right: return root.data >= root.left.data
    return (root.data >= root.left.data and root.data >= root.right.data) and isMaxOrder(root.left) and isMaxOrder(root.right)
def isHeap(tree):
    count = countNodes(tree)
    return isCBT(tree, 0, count) and isMaxOrder(tree)

