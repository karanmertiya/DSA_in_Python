# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Use Level Order Traversal (BFS) to serialize into a comma-separated string, using '#' for null. For deserialization, split string and use a queue to rebuild.

import collections
class Codec:
    def serialize(self, root):
        if not root: return ""
        q = collections.deque([root])
        res = []
        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("#")
        return ",".join(res)
    def deserialize(self, data):
        if not data: return None
        values = data.split(",")
        root = TreeNode(int(values[0]))
        q = collections.deque([root])
        i = 1
        while q:
            node = q.popleft()
            if values[i] != "#":
                node.left = TreeNode(int(values[i]))
                q.append(node.left)
            i += 1
            if values[i] != "#":
                node.right = TreeNode(int(values[i]))
                q.append(node.right)
            i += 1
        return root

