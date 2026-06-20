# Time Complexity: O(N)
# Space Complexity: O(H)
# Explanation: Recursive validation with min and max bounds for every node. Long long is used to avoid overflow.

def isValidBST(root: TreeNode) -> bool:
    def validate(node, low=-float('inf'), high=float('inf')):
        if not node: return True
        if node.val <= low or node.val >= high: return False
        return validate(node.left, low, node.val) and validate(node.right, node.val, high)
    return validate(root)

