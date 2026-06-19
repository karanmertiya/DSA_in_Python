# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Serialize: Use a queue for BFS. For every node, if it's not null, append its value and push its children. If null, append 'null' or '#'. Deserialize: Split the string. Use a queue. The first element is the root. For each node popped from the queue, read the next two elements from the list to form its left and right children, push non-null children to the queue.

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
        vals = data.split(",")
        root = TreeNode(int(vals[0]))
        q = collections.deque([root])
        i = 1
        while q:
            node = q.popleft()
            if vals[i] != "#":
                node.left = TreeNode(int(vals[i]))
                q.append(node.left)
            i += 1
            if vals[i] != "#":
                node.right = TreeNode(int(vals[i]))
                q.append(node.right)
            i += 1
        return root

