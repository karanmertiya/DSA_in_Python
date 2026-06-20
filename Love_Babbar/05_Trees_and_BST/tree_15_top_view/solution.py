# Time Complexity: O(N log N)
# Space Complexity: O(N)
# Explanation: BFS traversal maintaining horizontal distance (HD) from root. Use a map `hd -> value`. Only insert into the map if the HD is not already present, ensuring the top-most node is recorded.

import collections
def topView(root: Optional[Node]) -> List[int]:
    ans = []
    if not root: return ans
    mpp = {}
    q = collections.deque([(root, 0)])
    while q:
        node, line = q.popleft()
        if line not in mpp: mpp[line] = node.data
        if node.left: q.append((node.left, line - 1))
        if node.right: q.append((node.right, line + 1))
    for line in sorted(mpp.keys()): ans.append(mpp[line])
    return ans

