# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Standard BFS Level Order Traversal with a boolean flag `leftToRight`. After finishing a level, if the flag is false, reverse the level array before adding to the result.

def zigzagLevelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    result = []
    if not root: return result
    q = collections.deque([root])
    leftToRight = True
    while q:
        size = len(q)
        row = [0] * size
        for i in range(size):
            node = q.popleft()
            index = i if leftToRight else (size - 1 - i)
            row[index] = node.val
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        leftToRight = not leftToRight
        result.append(row)
    return result

