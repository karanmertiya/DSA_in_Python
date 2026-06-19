# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Use a hash map to store indices of inorder elements. The first element of preorder is the root. Find its index in inorder array to divide into left and right subtrees. Recursively build left and right.

def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    inMap = {val: i for i, val in enumerate(inorder)}
    def helper(preStart, preEnd, inStart, inEnd):
        if preStart > preEnd or inStart > inEnd: return None
        root = TreeNode(preorder[preStart])
        inRoot = inMap[root.val]
        numsLeft = inRoot - inStart
        root.left = helper(preStart + 1, preStart + numsLeft, inStart, inRoot - 1)
        root.right = helper(preStart + numsLeft + 1, preEnd, inRoot + 1, inEnd)
        return root
    return helper(0, len(preorder) - 1, 0, len(inorder) - 1)

