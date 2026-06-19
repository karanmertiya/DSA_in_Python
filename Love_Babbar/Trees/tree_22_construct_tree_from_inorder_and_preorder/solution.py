# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Store inorder indices in a HashMap. The first element in preorder is the root. Find this root in inorder map to determine left subtree size. Recursively build left and right subtrees by slicing array indices.

def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    inMap = {val: i for i, val in enumerate(inorder)}
    def build(preStart, preEnd, inStart, inEnd):
        if preStart > preEnd or inStart > inEnd: return None
        root = TreeNode(preorder[preStart])
        inRoot = inMap[root.val]
        numsLeft = inRoot - inStart
        root.left = build(preStart + 1, preStart + numsLeft, inStart, inRoot - 1)
        root.right = build(preStart + numsLeft + 1, preEnd, inRoot + 1, inEnd)
        return root
    return build(0, len(preorder) - 1, 0, len(inorder) - 1)

