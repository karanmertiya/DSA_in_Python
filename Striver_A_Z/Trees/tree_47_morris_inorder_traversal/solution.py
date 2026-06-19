# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: If left child is null, process current node, move to right. Else, find predecessor (rightmost node in left subtree). If predecessor's right is null, make it point to current (thread), move to left. If predecessor's right is current, remove thread, process current, move to right.

def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    inorder = []
    curr = root
    while curr:
        if not curr.left:
            inorder.append(curr.val)
            curr = curr.right
        else:
            prev = curr.left
            while prev.right and prev.right != curr:
                prev = prev.right
            if not prev.right:
                prev.right = curr
                curr = curr.left
            else:
                prev.right = None
                inorder.append(curr.val)
                curr = curr.right
    return inorder

