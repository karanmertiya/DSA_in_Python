# Time Complexity: O(N)
# Space Complexity: O(H)
# Explanation: Use a recursive function. A leaf node is always a SumTree. For an internal node, calculate the sum of its left and right subtrees. If its value equals the sum, and both subtrees are SumTrees, return true.

def isSumTree(root):
    def isSumTreeFast(node):
        if not node: return True, 0
        if not node.left and not node.right: return True, node.data
        left_is, left_sum = isSumTreeFast(node.left)
        right_is, right_sum = isSumTreeFast(node.right)
        is_sum = node.data == (left_sum + right_sum)
        if left_is and right_is and is_sum:
            return True, 2 * node.data
        else:
            return False, 0
    return isSumTreeFast(root)[0]

