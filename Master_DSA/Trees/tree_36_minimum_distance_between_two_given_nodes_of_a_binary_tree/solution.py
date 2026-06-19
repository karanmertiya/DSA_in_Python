# Time Complexity: O(N)
# Space Complexity: O(H)
# Explanation: Find the Lowest Common Ancestor (LCA) of the two nodes. Then find the distance from LCA to the first node and the distance from LCA to the second node. The total distance is the sum of these two distances.

def lca(root, n1, n2):
    if not root or root.data == n1 or root.data == n2: return root
    left = lca(root.left, n1, n2)
    right = lca(root.right, n1, n2)
    if left and right: return root
    return left if left else right
def findDist(root, val, dist):
    if not root: return -1
    if root.data == val: return dist
    left = findDist(root.left, val, dist + 1)
    if left != -1: return left
    return findDist(root.right, val, dist + 1)
def findDistMain(root, a, b):
    lca_node = lca(root, a, b)
    return findDist(lca_node, a, 0) + findDist(lca_node, b, 0)

