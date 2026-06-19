# Time Complexity: O(N)
# Space Complexity: O(H)
# Explanation: 1. Find LCA of the two nodes. 2. Find distance from LCA to node 1. 3. Find distance from LCA to node 2. 4. Return the sum.

def findDist(root: Optional[TreeNode], a: int, b: int) -> int:
    def lca(node):
        if not node or node.val == a or node.val == b: return node
        left = lca(node.left)
        right = lca(node.right)
        if not left: return right
        if not right: return left
        return node
    
    def getDist(node, val, dist):
        if not node: return -1
        if node.val == val: return dist
        d = getDist(node.left, val, dist + 1)
        if d != -1: return d
        return getDist(node.right, val, dist + 1)
        
    lca_node = lca(root)
    return getDist(lca_node, a, 0) + getDist(lca_node, b, 0)

