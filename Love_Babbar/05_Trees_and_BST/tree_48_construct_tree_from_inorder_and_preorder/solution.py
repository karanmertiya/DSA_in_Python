# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: The first element in preorder is the root. Find this root in inorder using a hash map. Elements to the left in inorder form the left subtree, elements to the right form the right subtree. Recurse.

class Node:
    def __init__(self,val): self.data = val; self.left = None; self.right = None
def buildTree(In, pre, n):
    mp = {val: idx for idx, val in enumerate(In)}
    preIdx = [0]
    def buildTreeUtil(inSt, inEnd):
        if inSt > inEnd: return None
        curr = pre[preIdx[0]]
        preIdx[0] += 1
        node = Node(curr)
        if inSt == inEnd: return node
        inIdx = mp[curr]
        node.left = buildTreeUtil(inSt, inIdx - 1)
        node.right = buildTreeUtil(inIdx + 1, inEnd)
        return node
    return buildTreeUtil(0, n - 1)

