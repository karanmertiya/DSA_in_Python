# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Perform BFS/DFS to map each node to its parent. Then, start a BFS from the target node, visiting left, right, and parent. Track visited nodes. After `k` levels in BFS, the current queue holds the answer.

import collections
def distanceK(root: TreeNode, target: TreeNode, k: int) -> List[int]:
    parent_track = {}
    def markParents(node):
        if node.left:
            parent_track[node.left] = node
            markParents(node.left)
        if node.right:
            parent_track[node.right] = node
            markParents(node.right)
    markParents(root)
    queue = collections.deque([target])
    visited = {target}
    curr_level = 0
    while queue:
        if curr_level == k: break
        size = len(queue)
        for _ in range(size):
            current = queue.popleft()
            if current.left and current.left not in visited:
                queue.append(current.left)
                visited.add(current.left)
            if current.right and current.right not in visited:
                queue.append(current.right)
                visited.add(current.right)
            if current in parent_track and parent_track[current] not in visited:
                queue.append(parent_track[current])
                visited.add(parent_track[current])
        curr_level += 1
    return [node.val for node in queue]

