# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Traverse both trees simultaneously. If both nodes are null, true. If one is null or values mismatch, false.

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q: return True
    if not p or not q or p.val != q.val: return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

