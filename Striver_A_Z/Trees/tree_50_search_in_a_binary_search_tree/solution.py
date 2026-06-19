# Time Complexity: O(H)
# Space Complexity: O(1)
# Explanation: Start at root. If root is null or its value is `val`, return root. If `val < root.val`, go left. Else go right.

def searchBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    while root and root.val != val:
        root = root.left if val < root.val else root.right
    return root

