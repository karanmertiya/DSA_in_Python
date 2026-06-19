# Time Complexity: O(N)
# Space Complexity: O(H)
# Explanation: Pass a valid range `(min_val, max_val)` for each node. For the root, it's `(-infinity, infinity)`. If node value is outside range, return false. Recursively check left subtree with range `(min_val, node.val)` and right subtree with `(node.val, max_val)`.

def isValidBST(root: Optional[TreeNode]) -> bool:
    def validate(node, low=-float('inf'), high=float('inf')):
        if not node: return True
        if node.val <= low or node.val >= high: return False
        return validate(node.left, low, node.val) and validate(node.right, node.val, high)
    return validate(root)

