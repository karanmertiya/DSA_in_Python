# Time Complexity: O(N)
# Space Complexity: O(H)
# Explanation: Recursive validation with min and max bounds. `isValidBST(root, min_val, max_val)`. Ensure `min_val < root.val < max_val`. For left child update `max_val = root.val`. For right child update `min_val = root.val`.

def isValidBST(root: Optional[TreeNode]) -> bool:
    def helper(node, min_val, max_val):
        if not node: return True
        if not (min_val < node.val < max_val): return False
        return helper(node.left, min_val, node.val) and helper(node.right, node.val, max_val)
    return helper(root, float('-inf'), float('inf'))

