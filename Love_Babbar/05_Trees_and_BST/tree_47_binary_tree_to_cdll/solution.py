# Time Complexity: O(N)
# Space Complexity: O(H)
# Explanation: Perform an inorder traversal. Maintain a `prev` pointer. If `prev` is NULL, it's the `head`. Else, set `prev->right = curr` and `curr->left = prev`. Update `prev = curr`. Finally, connect `head` and `prev` (the tail).

def bTreeToCList(root):
    head = [None]
    prev = [None]
    def inorder(node):
        if not node: return
        inorder(node.left)
        if not head[0]: head[0] = node
        else:
            prev[0].right = node
            node.left = prev[0]
        prev[0] = node
        inorder(node.right)
    inorder(root)
    if head[0] and prev[0]:
        head[0].left = prev[0]
        prev[0].right = head[0]
    return head[0]

