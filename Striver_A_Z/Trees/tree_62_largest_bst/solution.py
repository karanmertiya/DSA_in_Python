# Time Complexity: O(N)
# Space Complexity: O(H)
# Explanation: Return a struct `[minNode, maxNode, maxSize]`. For any node, if `left.maxNode < node.val < right.minNode`, it's a BST. Then `size = left.maxSize + right.maxSize + 1`. Return `[min(left.min, node.val), max(right.max, node.val), size]`. If not a BST, return `[-inf, inf, max(left.size, right.size)]`.

def largestBst(root):
    def helper(node):
        if not node: return float('inf'), float('-inf'), 0
        l_min, l_max, l_size = helper(node.left)
        r_min, r_max, r_size = helper(node.right)
        if l_max < node.val < r_min:
            return min(node.val, l_min), max(node.val, r_max), l_size + r_size + 1
        return float('-inf'), float('inf'), max(l_size, r_size)
    return helper(root)[2]

