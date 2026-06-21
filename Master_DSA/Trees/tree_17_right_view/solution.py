# Time Complexity: O(N)
# Space Complexity: O(H)
# Explanation: DFS Traversing right child before left child. Maintain the current level. If `level == result.size()`, append the node value to the result list.

def rightSideView(root: Optional[TreeNode]) -> List[int]:
    res = []
    def recursion(node, level):
        if not node: return
        if len(res) == level: res.append(node.val)
        recursion(node.right, level + 1)
        recursion(node.left, level + 1)
    recursion(root, 0)
    return res

