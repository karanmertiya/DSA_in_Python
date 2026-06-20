# Time Complexity: O(N)
# Space Complexity: O(N) for Hash Map
# Explanation: First element of preorder is the root. Find this element in inorder to split into left and right subtrees. Use a Hash Map to store inorder indices for O(1) lookups.

def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    in_map = {val: i for i, val in enumerate(inorder)}
    def build(pre_start, pre_end, in_start, in_end):
        if pre_start > pre_end or in_start > in_end: return None
        root = TreeNode(preorder[pre_start])
        in_root = in_map[root.val]
        nums_left = in_root - in_start
        root.left = build(pre_start + 1, pre_start + nums_left, in_start, in_root - 1)
        root.right = build(pre_start + nums_left + 1, pre_end, in_root + 1, in_end)
        return root
    return build(0, len(preorder) - 1, 0, len(inorder) - 1)

