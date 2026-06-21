# Time Complexity: O(N)
# Space Complexity: O(H)
# Explanation: DFS Traversing left child before right child. Maintain the current level. If `level == result.size()`, append the node value to the result list.

def leftView(root: Optional[Node]) -> List[int]:
    res = []
    def recursion(node, level):
        if not node: return
        if len(res) == level: res.append(node.data)
        recursion(node.left, level + 1)
        recursion(node.right, level + 1)
    recursion(root, 0)
    return res

