# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Use a queue for level order traversal. Maintain a `leftToRight` boolean flag. At each level, collect the nodes and reverse the list if `leftToRight` is false. Toggle the flag after each level.

def zigzagLevelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root: return []
    res = []
    q = collections.deque([root])
    leftToRight = True
    while q:
        level_size = len(q)
        row = [0] * level_size
        for i in range(level_size):
            node = q.popleft()
            index = i if leftToRight else (level_size - 1 - i)
            row[index] = node.val
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        leftToRight = not leftToRight
        res.append(row)
    return res

