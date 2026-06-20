# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Store inorder indices in a HashMap. The last element in postorder is the root. Find this root in inorder map to determine left subtree size. Recursively build left and right subtrees by slicing array indices.

def buildTree(inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    inMap = {val: i for i, val in enumerate(inorder)}
    def build(inStart, inEnd, postStart, postEnd):
        if inStart > inEnd or postStart > postEnd: return None
        root = TreeNode(postorder[postEnd])
        inRoot = inMap[root.val]
        numsLeft = inRoot - inStart
        root.left = build(inStart, inRoot - 1, postStart, postStart + numsLeft - 1)
        root.right = build(inRoot + 1, inEnd, postStart + numsLeft, postEnd - 1)
        return root
    return build(0, len(inorder) - 1, 0, len(postorder) - 1)

