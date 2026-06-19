# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Perform standard BFS using a queue. Maintain a boolean flag `leftToRight`. After processing a level, if `leftToRight` is false, reverse the current level's vector before adding it to the result. Toggle the flag for the next level.

from collections import deque
def zigzagLevelOrder(root):
    ans = []
    if not root: return ans
    q = deque([root])
    leftToRight = True
    while q:
        size = len(q)
        level = [0] * size
        for i in range(size):
            node = q.popleft()
            index = i if leftToRight else size - 1 - i
            level[index] = node.val
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        leftToRight = not leftToRight
        ans.append(level)
    return ans

