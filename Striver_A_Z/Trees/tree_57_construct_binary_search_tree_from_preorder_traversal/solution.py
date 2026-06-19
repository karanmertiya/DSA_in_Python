# Time Complexity: O(N)
# Space Complexity: O(H)
# Explanation: Keep track of an index for the `preorder` array and a maximum valid bound. To build the left subtree, the upper bound is the current node's value. To build the right subtree, the bound remains the parent's bound. If the current value is greater than the bound, return NULL.

def bstFromPreorder(preorder: List[int]) -> Optional[TreeNode]:
    i = 0
    def build(bound):
        nonlocal i
        if i == len(preorder) or preorder[i] > bound:
            return None
        root = TreeNode(preorder[i])
        i += 1
        root.left = build(root.val)
        root.right = build(bound)
        return root
    return build(float('inf'))

