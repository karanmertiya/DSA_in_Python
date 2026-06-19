# Time Complexity: O(log^2 N)
# Space Complexity: O(log N)
# Explanation: Compute the left height (following left child) and right height (following right child) of the tree. If they are equal, the tree is a full binary tree, and the number of nodes is `2^h - 1`. If they are not equal, recursively count the nodes in the left and right subtrees and add 1 for the root.

def countNodes(root: Optional[TreeNode]) -> int:
    if not root: return 0
    def get_height(node, is_left):
        h = 0
        while node:
            h += 1
            node = node.left if is_left else node.right
        return h
    lh = get_height(root, True)
    rh = get_height(root, False)
    if lh == rh:
        return (1 << lh) - 1
    return 1 + countNodes(root.left) + countNodes(root.right)

