# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: 1. If root is not leaf, add root. 2. Get left boundary (excluding leaves). 3. Get all leaves. 4. Get right boundary (excluding leaves) and reverse it.

def boundary(root: Optional[TreeNode]) -> List[int]:
    if not root: return []
    res = []
    def isLeaf(node):
        return not node.left and not node.right
    if not isLeaf(root): res.append(root.val)
    
    curr = root.left
    while curr:
        if not isLeaf(curr): res.append(curr.val)
        if curr.left: curr = curr.left
        else: curr = curr.right
        
    def addLeaves(node):
        if isLeaf(node):
            res.append(node.val)
            return
        if node.left: addLeaves(node.left)
        if node.right: addLeaves(node.right)
    addLeaves(root)
    
    curr = root.right
    temp = []
    while curr:
        if not isLeaf(curr): temp.append(curr.val)
        if curr.right: curr = curr.right
        else: curr = curr.left
    for val in reversed(temp):
        res.append(val)
        
    return res

