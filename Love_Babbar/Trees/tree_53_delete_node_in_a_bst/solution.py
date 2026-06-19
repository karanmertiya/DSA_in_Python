# Time Complexity: O(H)
# Space Complexity: O(1)
# Explanation: Search for the node. If found, there are 3 cases: Node is a leaf (just remove), Node has 1 child (replace with child), Node has 2 children (find inorder successor, i.e., min in right subtree, copy value, delete successor from right subtree). Alternatively, connect the left subtree to the leftmost node of the right subtree.

def deleteNode(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    if not root: return None
    if root.val == key:
        if not root.left: return root.right
        if not root.right: return root.left
        rightChild = root.right
        lastRight = root.left
        while lastRight.right: lastRight = lastRight.right
        lastRight.right = rightChild
        return root.left
    curr = root
    while curr:
        if curr.val > key:
            if curr.left and curr.left.val == key:
                if not curr.left.left: curr.left = curr.left.right
                elif not curr.left.right: curr.left = curr.left.left
                else:
                    rc = curr.left.right
                    lr = curr.left.left
                    while lr.right: lr = lr.right
                    lr.right = rc
                    curr.left = curr.left.left
                break
            else:
                curr = curr.left
        else:
            if curr.right and curr.right.val == key:
                if not curr.right.left: curr.right = curr.right.right
                elif not curr.right.right: curr.right = curr.right.left
                else:
                    rc = curr.right.right
                    lr = curr.right.left
                    while lr.right: lr = lr.right
                    lr.right = rc
                    curr.right = curr.right.left
                break
            else:
                curr = curr.right
    return root

