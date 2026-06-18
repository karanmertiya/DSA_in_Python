# Time Complexity: O(N) (Constraint)
# Space Complexity: O(N) (Constraint)
# Explanation: Recursive approach. Traverse the left subtree, process the current node, then traverse the right subtree.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def inorder_traversal(root: TreeNode) -> list[int]:
    ans = []
    def inorder(node):
        if not node: return
        inorder(node.left)
        ans.append(node.val)
        inorder(node.right)
    inorder(root)
    return ans

