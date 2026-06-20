# Time Complexity: O(N)
# Space Complexity: O(H)
# Explanation: Perform Inorder traversal. Maintain a `prev` pointer (initially null). At each node: if `prev == null`, this node is the head of DLL. Else, `prev->right = node` and `node->left = prev`. Update `prev = node`.

def bToDLL(root: Optional[TreeNode]) -> Optional[TreeNode]:
    head = prev = None
    def inorder(node):
        nonlocal head, prev
        if not node: return
        inorder(node.left)
        if prev is None:
            head = node
        else:
            node.left = prev
            prev.right = node
        prev = node
        inorder(node.right)
    inorder(root)
    return head

