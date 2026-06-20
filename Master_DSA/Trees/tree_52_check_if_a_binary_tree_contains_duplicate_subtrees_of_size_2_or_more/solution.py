# Time Complexity: O(N^2)
# Space Complexity: O(N)
# Explanation: Serialize each subtree into a string. Use a hash map to store the frequencies of the serialized strings. If any string (of length > 3 to ignore leaves) has a frequency > 1, a duplicate subtree exists.

def dupSub(root):
    m = {}
    def solve(node):
        if not node: return "$"
        s = ""
        if not node.left and not node.right:
            return str(node.data)
        s = str(node.data) + "-" + solve(node.left) + "-" + solve(node.right)
        m[s] = m.get(s, 0) + 1
        return s
    solve(root)
    for count in m.values():
        if count >= 2: return 1
    return 0

