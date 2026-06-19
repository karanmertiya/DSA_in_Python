# Time Complexity: O(1) average per call
# Space Complexity: O(H)
# Explanation: Maintain a stack of nodes. In constructor, push all left children of root. In `next()`, pop top, value is answer, if popped node has right child, push it and all its left children. `hasNext()` checks if stack is not empty.

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.st = []
        self.pushAll(root)
    def pushAll(self, node):
        while node:
            self.st.append(node)
            node = node.left
    def next(self) -> int:
        tmpNode = self.st.pop()
        self.pushAll(tmpNode.right)
        return tmpNode.val
    def hasNext(self) -> bool:
        return len(self.st) > 0

