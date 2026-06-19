# Time Complexity: O(N)
# Space Complexity: O(H)
# Explanation: Preorder DFS simultaneously on both trees. If both are null, true. If one is null or vals mismatch, false. Recursively check left and right subtrees.

def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p or not q: return p == q
    return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

