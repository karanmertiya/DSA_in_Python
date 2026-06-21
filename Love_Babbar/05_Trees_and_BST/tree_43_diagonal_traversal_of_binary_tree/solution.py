# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Use a queue. Push root. Then loop: Pop a node `curr`. While `curr` is not null, add its value to result, push `curr->left` to queue, and move to `curr->right`.

def diagonal(root: Optional[TreeNode]) -> List[int]:
    res = []
    if not root: return res
    q = collections.deque([root])
    while q:
        curr = q.popleft()
        while curr:
            res.append(curr.val)
            if curr.left: q.append(curr.left)
            curr = curr.right
    return res

