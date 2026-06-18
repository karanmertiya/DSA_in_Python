# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Recursive approach. Traverse Left, process Root, then traverse Right.

def inorderTraversal(root: TreeNode) -> list[int]:
    ans = []
    def inorder(node):
        if not node: return
        inorder(node.left)
        ans.append(node.val)
        inorder(node.right)
    inorder(root)
    return ans

