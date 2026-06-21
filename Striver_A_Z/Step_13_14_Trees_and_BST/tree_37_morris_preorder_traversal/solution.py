# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Similar to Morris Inorder. If left child is null, process current, move right. Else, find predecessor. If predecessor's right is null, process current, make thread, move left. If predecessor's right is current, remove thread, move right.

def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
    preorder = []
    curr = root
    while curr:
        if not curr.left:
            preorder.append(curr.val)
            curr = curr.right
        else:
            prev = curr.left
            while prev.right and prev.right != curr:
                prev = prev.right
            if not prev.right:
                prev.right = curr
                preorder.append(curr.val)
                curr = curr.left
            else:
                prev.right = None
                curr = curr.right
    return preorder

