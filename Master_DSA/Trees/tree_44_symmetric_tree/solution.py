# Time Complexity: O(N)
# Space Complexity: O(H)
# Explanation: Use a helper function `isMirror(left, right)`. The tree is symmetric if `root->left` and `root->right` are mirrors. Two trees are mirrors if their roots are equal and `left1->left` is mirror of `right1->right`, and `left1->right` is mirror of `right1->left`.

def isSymmetric(root):
    def isMirror(n1, n2):
        if not n1 and not n2: return True
        if not n1 or not n2: return False
        return (n1.val == n2.val) and isMirror(n1.left, n2.right) and isMirror(n1.right, n2.left)
    if not root: return True
    return isMirror(root.left, root.right)

