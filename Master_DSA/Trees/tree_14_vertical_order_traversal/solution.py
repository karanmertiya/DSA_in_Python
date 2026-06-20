# Time Complexity: O(N log N)
# Space Complexity: O(N)
# Explanation: Use a map structure: `map<int, map<int, multiset<int>>>` to store nodes mapped by their horizontal distance and level. BFS traversal ensures levels are processed top-down.

import collections
def verticalTraversal(root: Optional[TreeNode]) -> List[List[int]]:
    nodes = collections.defaultdict(lambda: collections.defaultdict(list))
    todo = collections.deque([(root, 0, 0)])
    while todo:
        node, x, y = todo.popleft()
        nodes[x][y].append(node.val)
        if node.left: todo.append((node.left, x - 1, y + 1))
        if node.right: todo.append((node.right, x + 1, y + 1))
    ans = []
    for x in sorted(nodes.keys()):
        col = []
        for y in sorted(nodes[x].keys()):
            col.extend(sorted(nodes[x][y]))
        ans.append(col)
    return ans

