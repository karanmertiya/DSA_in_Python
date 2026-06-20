# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Same as 'Distance K' problem. Map parents. Find the start node. Perform BFS from start node. The time taken is the number of levels in BFS until all reachable nodes are visited.

import collections
def amountOfTime(root: Optional[TreeNode], start: int) -> int:
    parent_track = {}
    target = None
    queue = collections.deque([root])
    while queue:
        node = queue.popleft()
        if node.val == start: target = node
        if node.left:
            parent_track[node.left] = node
            queue.append(node.left)
        if node.right:
            parent_track[node.right] = node
            queue.append(node.right)
    queue = collections.deque([target])
    visited = {target}
    time = 0
    while queue:
        fl = False
        for _ in range(len(queue)):
            current = queue.popleft()
            if current.left and current.left not in visited:
                visited.add(current.left)
                queue.append(current.left)
                fl = True
            if current.right and current.right not in visited:
                visited.add(current.right)
                queue.append(current.right)
                fl = True
            if current in parent_track and parent_track[current] not in visited:
                visited.add(parent_track[current])
                queue.append(parent_track[current])
                fl = True
        if fl: time += 1
    return time

