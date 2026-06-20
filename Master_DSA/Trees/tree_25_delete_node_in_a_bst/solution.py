# Time Complexity: O(H)
# Space Complexity: O(H) or O(1)
# Explanation: Find the node. If it has no left child, return right child. If no right, return left. If both exist, find the right child of the rightmost node in the left subtree, and point it to the node's right child. Return the node's left child.

def deleteNode(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    def helper(node):
        if not node.left: return node.right
        if not node.right: return node.left
        rightChild = node.right
        lastRight = node.left
        while lastRight.right: lastRight = lastRight.right
        lastRight.right = rightChild
        return node.left
    if not root: return None
    if root.val == key: return helper(root)
    curr = root
    while curr:
        if curr.val > key:
            if curr.left and curr.left.val == key:
                curr.left = helper(curr.left)
                break
            else: curr = curr.left
        else:
            if curr.right and curr.right.val == key:
                curr.right = helper(curr.right)
                break
            else: curr = curr.right
    return root

