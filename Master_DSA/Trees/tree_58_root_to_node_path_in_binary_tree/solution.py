# Time Complexity: O(N)
# Space Complexity: O(H)
# Explanation: Use recursion. Push current node to the path array. If it's the target node, return true. Recursively search left and right subtrees. If either returns true, return true. If not found in either, pop the current node from the path array and return false.

def solve(A, B):
    arr = []
    def getPath(node, x):
        if not node: return False
        arr.append(node.val)
        if node.val == x: return True
        if getPath(node.left, x) or getPath(node.right, x): return True
        arr.pop()
        return False
    if not A: return arr
    getPath(A, B)
    return arr

