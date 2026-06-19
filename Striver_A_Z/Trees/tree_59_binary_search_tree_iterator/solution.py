# Time Complexity: O(1) amortized for next/hasNext
# Space Complexity: O(H)
# Explanation: Use a stack to simulate inorder traversal. In constructor, push all left children of root to stack. For `next()`, pop the top node, push all left children of its right child, and return the popped node's value. `hasNext()` checks if stack is not empty.

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.pushAll(root)
    def pushAll(self, node):
        while node:
            self.stack.append(node)
            node = node.left
    def next(self) -> int:
        tmpNode = self.stack.pop()
        self.pushAll(tmpNode.right)
        return tmpNode.val
    def hasNext(self) -> bool:
        return len(self.stack) > 0

