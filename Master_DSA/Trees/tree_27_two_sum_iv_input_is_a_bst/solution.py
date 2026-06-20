# Time Complexity: O(N)
# Space Complexity: O(H)
# Explanation: Use two BST iterators: one for normal inorder (next) and one for reverse inorder (before). Apply two-pointer approach like in a sorted array.

class BSTIterator:
    def __init__(self, root, isReverse):
        self.st = []
        self.reverse = isReverse
        self.pushAll(root)
    def pushAll(self, node):
        while node:
            self.st.append(node)
            if self.reverse: node = node.right
            else: node = node.left
    def next(self) -> int:
        tmpNode = self.st.pop()
        if self.reverse: self.pushAll(tmpNode.left)
        else: self.pushAll(tmpNode.right)
        return tmpNode.val
def findTarget(root: Optional[TreeNode], k: int) -> bool:
    if not root: return False
    l = BSTIterator(root, False)
    r = BSTIterator(root, True)
    i = l.next()
    j = r.next()
    while i < j:
        if i + j == k: return True
        elif i + j < k: i = l.next()
        else: j = r.next()
    return False

