# Time Complexity: O(K) or O(N)
# Space Complexity: O(H) or O(1)
# Explanation: Perform an inorder traversal (Recursive or Iterative/Morris) and keep track of count. When count reaches `k`, return the node's value.

def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    count, ans = 0, -1
    curr = root
    while curr:
        if not curr.left:
            count += 1
            if count == k: ans = curr.val
            curr = curr.right
        else:
            prev = curr.left
            while prev.right and prev.right != curr: prev = prev.right
            if not prev.right:
                prev.right = curr
                curr = curr.left
            else:
                prev.right = None
                count += 1
                if count == k: ans = curr.val
                curr = curr.right
    return ans

