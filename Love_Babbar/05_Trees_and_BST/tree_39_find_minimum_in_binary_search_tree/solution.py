# Time Complexity: O(H)
# Space Complexity: O(1)
# Explanation: Traverse the left children until a node with no left child is reached. That node contains the minimum value.

def minValue(root: Optional[TreeNode]) -> int:
    if not root: return -1
    while root.left:
        root = root.left
    return root.val

