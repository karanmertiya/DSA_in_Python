# Time Complexity: O(N log N)
# Space Complexity: O(N)
# Explanation: Use BFS to traverse the tree. Store coordinates `(x, y)` along with nodes in a queue. Use a nested map `map<int, map<int, multiset<int>>> nodes` to store nodes grouped by `x` (vertical level), then by `y` (horizontal level). `multiset` handles sorting when multiple nodes share the same coordinates.

from collections import deque, defaultdict
def verticalTraversal(root):
    nodes = defaultdict(lambda: defaultdict(list))
    q = deque([(root, 0, 0)])
    while q:
        node, x, y = q.popleft()
        nodes[x][y].append(node.val)
        if node.left: q.append((node.left, x - 1, y + 1))
        if node.right: q.append((node.right, x + 1, y + 1))
    ans = []
    for x in sorted(nodes.keys()):
        col = []
        for y in sorted(nodes[x].keys()):
            col.extend(sorted(nodes[x][y]))
        ans.append(col)
    return ans

