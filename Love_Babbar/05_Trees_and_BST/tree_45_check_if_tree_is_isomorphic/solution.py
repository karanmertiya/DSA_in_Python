# Time Complexity: O(min(M, N))
# Space Complexity: O(min(H1, H2))
# Explanation: Two trees are isomorphic if one can be obtained from another by a series of flips. If roots are null, return true. If values don't match, false. Then check `(isIsomorphic(n1.left, n2.left) && isIsomorphic(n1.right, n2.right))` OR `(isIsomorphic(n1.left, n2.right) && isIsomorphic(n1.right, n2.left))`.

def isIsomorphic(n1: Optional[TreeNode], n2: Optional[TreeNode]) -> bool:
    if not n1 and not n2: return True
    if not n1 or not n2: return False
    if n1.val != n2.val: return False
    no_swap = isIsomorphic(n1.left, n2.left) and isIsomorphic(n1.right, n2.right)
    swap = isIsomorphic(n1.left, n2.right) and isIsomorphic(n1.right, n2.left)
    return no_swap or swap

