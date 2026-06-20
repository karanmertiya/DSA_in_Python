# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Use Level Order Traversal (BFS) using a queue. For serialization, append '#' for null nodes. For deserialization, split string by comma and use a queue to reconstruct the tree structure level by level.

import collections
class Codec:
    def serialize(self, root):
        if not root: return ""
        s = []; q = collections.deque([root])
        while q:
            node = q.popleft()
            if node is None: s.append("#")
            else: s.append(str(node.val)); q.append(node.left); q.append(node.right)
        return ",".join(s)
    def deserialize(self, data):
        if not data: return None
        values = data.split(",")
        root = TreeNode(int(values[0]))
        q = collections.deque([root])
        i = 1
        while q:
            node = q.popleft()
            if values[i] != "#": node.left = TreeNode(int(values[i])); q.append(node.left)
            i += 1
            if values[i] != "#": node.right = TreeNode(int(values[i])); q.append(node.right)
            i += 1
        return root

