# Time Complexity: O(N)
# Space Complexity: O(H)
# Explanation: Use a recursive function. If the target node is found, return it. As you return back up the call stack, decrement `k`. When `k` becomes 0, the current node is the kth ancestor.

def kthAncestor(root, k, node):
    ans_node = None
    def solve(root):
        nonlocal k, ans_node
        if not root: return False
        if root.data == node: return True
        left = solve(root.left)
        right = solve(root.right)
        if left or right:
            k -= 1
            if k == 0:
                ans_node = root
                return False
            return True
        return False
    solve(root)
    return ans_node.data if ans_node else -1

