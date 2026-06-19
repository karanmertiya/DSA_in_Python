# Time Complexity: O(N)
# Space Complexity: O(H)
# Explanation: Implement two BST iterators: one for normal inorder (next) and one for reverse inorder (before). Set `i = next()` and `j = before()`. While `i < j`, if `i + j == k` return true, if `i + j < k` increment `i`, else decrement `j`.

class BSTIterator:
    def __init__(self, root, isReverse):
        self.stack = []
        self.reverse = isReverse
        self.pushAll(root)
    def pushAll(self, node):
        while node:
            self.stack.append(node)
            node = node.right if self.reverse else node.left
    def next(self):
        tmp = self.stack.pop()
        self.pushAll(tmp.left if self.reverse else tmp.right)
        return tmp.val
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

