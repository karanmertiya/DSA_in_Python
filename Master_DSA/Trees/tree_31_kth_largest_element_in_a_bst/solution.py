# Time Complexity: O(N)
# Space Complexity: O(H)
# Explanation: Kth largest is Kth element in reverse inorder traversal (Right, Root, Left). Maintain a counter `k`. When visiting a node, decrement `k`. If `k == 0`, current node is the answer.

def kthLargest(root, k):
    ans = -1
    def reverseInorder(node):
        nonlocal ans, k
        if not node or k == 0: return
        reverseInorder(node.right)
        k -= 1
        if k == 0:
            ans = node.data
            return
        reverseInorder(node.left)
    reverseInorder(root)
    return ans

