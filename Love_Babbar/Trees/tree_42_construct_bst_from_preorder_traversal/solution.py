# Time Complexity: O(N)
# Space Complexity: O(H)
# Explanation: Use an upper bound value. `build(preorder, index, bound)`: If index >= len or preorder[index] > bound, return NULL. Create root with preorder[index]. `root->left = build(..., root->val)`. `root->right = build(..., bound)`.

def bstFromPreorder(preorder: List[int]) -> Optional[TreeNode]:
    i = 0
    def build(bound):
        nonlocal i
        if i == len(preorder) or preorder[i] > bound: return None
        root = TreeNode(preorder[i])
        i += 1
        root.left = build(root.val)
        root.right = build(bound)
        return root
    return build(float('inf'))

