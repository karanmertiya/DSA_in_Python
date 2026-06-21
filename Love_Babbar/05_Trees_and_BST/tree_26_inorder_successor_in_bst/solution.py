# Time Complexity: O(H)
# Space Complexity: O(1)
# Explanation: Traverse BST. If `curr.val > node.val`, then `curr` is a potential successor, store it and move left to find smaller. Else, move right.

def inOrderSuccessor(root, x):
    successor = None
    while root:
        if root.val <= x.val:
            root = root.right
        else:
            successor = root
            root = root.left
    return successor

