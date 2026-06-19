# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Similar to preorder+inorder, but the root is at the end of the postorder array. Map inorder indices. Find root, divide, and recurse.

def buildTree(inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    inMap = {val: i for i, val in enumerate(inorder)}
    def helper(inStart, inEnd, postStart, postEnd):
        if inStart > inEnd or postStart > postEnd: return None
        root = TreeNode(postorder[postEnd])
        inRoot = inMap[root.val]
        numsLeft = inRoot - inStart
        root.left = helper(inStart, inRoot - 1, postStart, postStart + numsLeft - 1)
        root.right = helper(inRoot + 1, inEnd, postStart + numsLeft, postEnd - 1)
        return root
    return helper(0, len(inorder) - 1, 0, len(postorder) - 1)

