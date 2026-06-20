# Time Complexity: O(N)
# Space Complexity: O(H)
# Explanation: 1) Add root if not leaf. 2) Traverse left boundary (excluding leaves). 3) Inorder traverse all leaves. 4) Traverse right boundary, reverse it, then add to answer.

def printBoundaryView(root: TreeNode) -> List[int]:
    if not root: return []
    res = []
    def isLeaf(node): return not node.left and not node.right
    if not isLeaf(root): res.append(root.val)
    cur = root.left
    while cur:
        if not isLeaf(cur): res.append(cur.val)
        cur = cur.left if cur.left else cur.right
    def addLeaves(node):
        if isLeaf(node): res.append(node.val); return
        if node.left: addLeaves(node.left)
        if node.right: addLeaves(node.right)
    addLeaves(root)
    cur = root.right; tmp = []
    while cur:
        if not isLeaf(cur): tmp.append(cur.val)
        cur = cur.right if cur.right else cur.left
    res.extend(tmp[::-1])
    return res

