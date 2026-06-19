# Time Complexity: O(N^2)
# Space Complexity: O(N^2)
# Explanation: Serialize each subtree into a string (e.g., using preorder traversal). Use a hash map to count the frequencies of these serialized strings. If a string appears exactly twice, add the root of that subtree to the result list.

def printAllDups(root):
    m = {}
    ans = []
    def solve(node):
        if not node: return "N"
        s = str(node.data) + "," + solve(node.left) + "," + solve(node.right)
        m[s] = m.get(s, 0) + 1
        if m[s] == 2: ans.append(node)
        return s
    solve(root)
    return ans

