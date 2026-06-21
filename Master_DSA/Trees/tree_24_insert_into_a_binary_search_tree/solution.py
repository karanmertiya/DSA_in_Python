# Time Complexity: O(H)
# Space Complexity: O(1)
# Explanation: Traverse left or right depending on the value. Keep track of parent. Insert as left or right child of parent when a null pointer is reached.

def insertIntoBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root: return TreeNode(val)
    curr = root
    while True:
        if val < curr.val:
            if curr.left: curr = curr.left
            else: curr.left = TreeNode(val); break
        else:
            if curr.right: curr = curr.right
            else: curr.right = TreeNode(val); break
    return root

