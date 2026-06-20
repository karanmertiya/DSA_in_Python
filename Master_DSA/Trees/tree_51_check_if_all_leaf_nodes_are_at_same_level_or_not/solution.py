# Time Complexity: O(N)
# Space Complexity: O(H)
# Explanation: Traverse the tree, maintaining the current level. The first time a leaf is encountered, store its level. For subsequent leaves, compare their level with the stored level. If any mismatch occurs, return false.

def check(root):
    leafLevel = [0]
    def checkUtil(node, level):
        if not node: return True
        if not node.left and not node.right:
            if leafLevel[0] == 0:
                leafLevel[0] = level
                return True
            return level == leafLevel[0]
        return checkUtil(node.left, level + 1) and checkUtil(node.right, level + 1)
    return checkUtil(root, 1)

