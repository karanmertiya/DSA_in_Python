# Time Complexity: O(1) amortized
# Space Complexity: O(H)
# Explanation: Use a stack to simulate in-order traversal. Push all left children initially. On next(), pop, return val, and push all left children of popped node's right child.

class BSTIterator:
    def __init__(self, root: TreeNode):
        self.st = []
        self.pushAll(root)
    def pushAll(self, node):
        while node:
            self.st.append(node)
            node = node.left
    def next(self) -> int:
        tmp = self.st.pop()
        self.pushAll(tmp.right)
        return tmp.val
    def hasNext(self) -> bool:
        return len(self.st) > 0

