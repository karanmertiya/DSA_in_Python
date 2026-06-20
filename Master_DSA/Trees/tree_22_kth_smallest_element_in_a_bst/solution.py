# Time Complexity: O(N)
# Space Complexity: O(1) using Morris Traversal
# Explanation: Inorder traversal of BST gives sorted elements. Keep a counter, when it reaches K, store the result. Morris Traversal can do this in O(1) space.

def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    count, ans = 0, -1
    curr = root
    while curr:
        if curr.left is None:
            count += 1
            if count == k: ans = curr.val
            curr = curr.right
        else:
            pre = curr.left
            while pre.right and pre.right != curr: pre = pre.right
            if pre.right is None:
                pre.right = curr
                curr = curr.left
            else:
                pre.right = None
                count += 1
                if count == k: ans = curr.val
                curr = curr.right
    return ans

