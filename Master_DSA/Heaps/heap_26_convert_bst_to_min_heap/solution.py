# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Since a BST inorder gives sorted values, store the inorder traversal in an array. The requirement says left subtree elements < right subtree elements, which matches a Preorder traversal (Root, Left, Right) since we want the smallest element at the root. So do a Preorder traversal of the tree and replace nodes with array elements.

def convertToMinHeapUtil(root):
    arr = []
    def inorder(node):
        if not node: return
        inorder(node.left)
        arr.append(node.data)
        inorder(node.right)
    def preorderFill(node, idx):
        if not node: return
        node.data = arr[idx[0]]
        idx[0] += 1
        preorderFill(node.left, idx)
        preorderFill(node.right, idx)
    inorder(root)
    preorderFill(root, [0])

