# Time Complexity: O(N log N)
# Space Complexity: O(N)
# Explanation: BFS traversal maintaining horizontal distance (HD). Map `hd -> value`. Always update the map value for a given HD so that the last node encountered (bottom-most) overrides previous ones.

import collections
def bottomView(root: Optional[Node]) -> List[int]:
    ans = []
    if not root: return ans
    mpp = {}
    q = collections.deque([(root, 0)])
    while q:
        node, line = q.popleft()
        mpp[line] = node.data
        if node.left: q.append((node.left, line - 1))
        if node.right: q.append((node.right, line + 1))
    for line in sorted(mpp.keys()): ans.append(mpp[line])
    return ans

