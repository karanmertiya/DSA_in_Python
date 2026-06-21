# Day 17 to 22 Trees BST Revision Table

<table border="1">
  <thead>
    <tr>
      <th style="width: 5%;">S.No</th>
      <th style="width: 15%;">Problem Name</th>
      <th style="width: 20%;">Example & Constraints</th>
      <th style="width: 10%;">Complexity</th>
      <th style="width: 20%;">Approach & Dependencies</th>
      <th style="width: 30%;">Logic & Edge Cases</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="1">1</td>
      <td rowspan="1">Tree 01 Binary Tree Inorder Traversal<br><br></b> <a href="https://leetcode.com/problems/binary-tree-inorder-traversal/" target="_blank">LeetCode 94</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, SDE Sheet, Striver A Z</details></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> root = [1,null,2,3]<br><b>Output:</b> [1,3,2]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Recursive approach. Traverse Left, process Root, then traverse Right.</td>
      <td><b>Edge Cases:</b> <b>Recursion Depth:</b> Worst-case skewed tree takes `O(N)` space.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def inorderTraversal(root: TreeNode) -&gt; list[int]:&#10;    ans = []&#10;    def inorder(node):&#10;        if not node: return&#10;        inorder(node.left)&#10;        ans.append(node.val)&#10;        inorder(node.right)&#10;    inorder(root)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">2</td>
      <td rowspan="1">Tree 02 Maximum Depth Of Binary Tree<br><br></b> <a href="https://leetcode.com/problems/maximum-depth-of-binary-tree/" target="_blank">LeetCode 104</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, SDE Sheet, Striver A Z</details></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> root = [3,9,20,null,null,15,7]<br><b>Output:</b> 3</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H) &cong; O(N)</td>
      <td>Recursively find the max depth of left and right subtrees. The depth is `1 + max(left_depth, right_depth)`.<br><br><b>Dependencies:</b> <code>std::max</code></td>
      <td><b>Edge Cases:</b> <b>Null Root:</b> If empty (`root == NULL`), depth is 0.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxDepth(root: TreeNode) -&gt; int:&#10;    if not root: return 0&#10;    return 1 + max(maxDepth(root.left), maxDepth(root.right))</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">3</td>
      <td rowspan="1">Tree 03 Lowest Common Ancestor Of A Binary Tree<br><br></b> <a href="https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/" target="_blank">LeetCode 236</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> SDE Sheet, Love Babbar, Striver A Z, Apna College</details></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1<br><b>Output:</b> 3</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>If we find `p` or `q`, return it. If both left and right return non-null, current node is LCA.</td>
      <td><b>Edge Cases:</b> <b>Node is LCA:</b> If one is ancestor of other, it returns immediately.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -&gt; TreeNode:&#10;    if not root or root == p or root == q: return root&#10;    left = lowestCommonAncestor(root.left, p, q)&#10;    right = lowestCommonAncestor(root.right, p, q)&#10;    if not left: return right&#10;    elif not right: return left&#10;    else: return root</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">4</td>
      <td rowspan="1">Tree 04 Same Tree<br><br></b> <a href="https://leetcode.com/problems/same-tree/" target="_blank">LeetCode 100</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, SDE Sheet, Striver A Z, Apna College</details></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> p = [1,2,3], q = [1,2,3]<br><b>Output:</b> true</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Traverse both trees simultaneously. If both nodes are null, true. If one is null or values mismatch, false.</td>
      <td><b>Edge Cases:</b> <b>Structural mismatch:</b> Safely handled by `!p || !q`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isSameTree(p: TreeNode, q: TreeNode) -&gt; bool:&#10;    if not p and not q: return True&#10;    if not p or not q or p.val != q.val: return False&#10;    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">5</td>
      <td rowspan="1">Tree 05 Invert Binary Tree<br><br></b> <a href="https://leetcode.com/problems/invert-binary-tree/" target="_blank">LeetCode 226</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> root = [4,2,7,1,3,6,9]<br><b>Output:</b> [4,7,2,9,6,3,1]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Recursively swap the left and right children of every node.<br><br><b>Dependencies:</b> <code>std::swap</code></td>
      <td><b>Edge Cases:</b> <b>Empty Tree:</b> Returns null immediately.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def invertTree(root: TreeNode) -&gt; TreeNode:&#10;    if not root: return None&#10;    root.left, root.right = root.right, root.left&#10;    invertTree(root.left)&#10;    invertTree(root.right)&#10;    return root</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">6</td>
      <td rowspan="1">Tree 06 Diameter Of Binary Tree<br><br></b> <a href="https://leetcode.com/problems/diameter-of-binary-tree/" target="_blank">LeetCode 543</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, SDE Sheet, Striver A Z, Apna College</details></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> root = [1,2,3,4,5]<br><b>Output:</b> 3 (Path is [4,2,1,3] or [5,2,1,3])</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Modify the Height/Depth algorithm. Calculate `left_depth + right_depth` at every node to find max diameter, while returning standard height.<br><br><b>Dependencies:</b> <code>std::max</code></td>
      <td><b>Edge Cases:</b> <b>Path doesn't pass through root:</b> Handled correctly by tracking the global maximum `max_d` at every recursive step.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def diameterOfBinaryTree(root: TreeNode) -&gt; int:&#10;    max_d = [0]&#10;    def height(node):&#10;        if not node: return 0&#10;        left = height(node.left)&#10;        right = height(node.right)&#10;        max_d[0] = max(max_d[0], left + right)&#10;        return 1 + max(left, right)&#10;    height(root)&#10;    return max_d[0]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">7</td>
      <td rowspan="1">Tree 07 Balanced Binary Tree<br><br></b> <a href="https://leetcode.com/problems/balanced-binary-tree/" target="_blank">LeetCode 110</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> SDE Sheet, Love Babbar, Striver A Z</details></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> root = [3,9,20,null,null,15,7]<br><b>Output:</b> true</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Modify the Height algorithm. If the difference between `left` and `right` height is > 1, return `-1` to propagate the unbalanced signal.<br><br><b>Dependencies:</b> <code>std::abs</code></td>
      <td><b>Edge Cases:</b> <b>Early Exit:</b> Checking if `left == -1` or `right == -1` immediately breaks the recursion, optimizing time.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isBalanced(root: TreeNode) -&gt; bool:&#10;    def checkHeight(node):&#10;        if not node: return 0&#10;        left = checkHeight(node.left)&#10;        if left == -1: return -1&#10;        right = checkHeight(node.right)&#10;        if right == -1: return -1&#10;        if abs(left - right) &gt; 1: return -1&#10;        return 1 + max(left, right)&#10;    return checkHeight(root) != -1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">8</td>
      <td rowspan="1">Tree 08 Binary Search Tree Iterator<br><br></b> <a href="https://leetcode.com/problems/binary-search-tree-iterator/" target="_blank">LeetCode 173</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> SDE Sheet, Love Babbar, Striver A Z</details></td>
      <td rowspan="1"><b>Example 1:</b> next() returns smallest element.</td>
      <td><b>Time:</b> O(1) amortized<br><b>Space:</b> O(H)</td>
      <td>Use a stack to simulate in-order traversal. Push all left children initially. On next(), pop, return val, and push all left children of popped node's right child.<br><br><b>Dependencies:</b> <code>#include <stack></code></td>
      <td><b>Edge Cases:</b> <b>Empty Tree:</b> Stack is empty.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class BSTIterator:&#10;    def __init__(self, root: TreeNode):&#10;        self.st = []&#10;        self.pushAll(root)&#10;    def pushAll(self, node):&#10;        while node:&#10;            self.st.append(node)&#10;            node = node.left&#10;    def next(self) -&gt; int:&#10;        tmp = self.st.pop()&#10;        self.pushAll(tmp.right)&#10;        return tmp.val&#10;    def hasNext(self) -&gt; bool:&#10;        return len(self.st) &gt; 0</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">9</td>
      <td rowspan="1">Tree 09 Validate Binary Search Tree<br><br></b> <a href="https://leetcode.com/problems/validate-binary-search-tree/" target="_blank">LeetCode 98</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> SDE Sheet, Love Babbar, Striver A Z</details></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> root = [2,1,3]<br><b>Output:</b> true</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>Recursive validation with min and max bounds for every node. Long long is used to avoid overflow.<br><br><b>Dependencies:</b> <code>#include <limits.h></code></td>
      <td><b>Edge Cases:</b> <b>Values reach INT bounds:</b> Use LLONG_MIN/LLONG_MAX bounds.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isValidBST(root: TreeNode) -&gt; bool:&#10;    def validate(node, low=-float(&#x27;inf&#x27;), high=float(&#x27;inf&#x27;)):&#10;        if not node: return True&#10;        if node.val &lt;= low or node.val &gt;= high: return False&#10;        return validate(node.left, low, node.val) and validate(node.right, node.val, high)&#10;    return validate(root)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">10</td>
      <td rowspan="1">Tree 10 Construct Tree From Preorder And Inorder<br><br></b> <a href="https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/" target="_blank">LeetCode 105</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> SDE Sheet, Love Babbar, Striver A Z, Apna College</details></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]<br><b>Output:</b> [3,9,20,null,null,15,7]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N) for Hash Map</td>
      <td>First element of preorder is the root. Find this element in inorder to split into left and right subtrees. Use a Hash Map to store inorder indices for O(1) lookups.<br><br><b>Dependencies:</b> <code>#include <unordered_map></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def buildTree(preorder: List[int], inorder: List[int]) -&gt; Optional[TreeNode]:&#10;    in_map = {val: i for i, val in enumerate(inorder)}&#10;    def build(pre_start, pre_end, in_start, in_end):&#10;        if pre_start &gt; pre_end or in_start &gt; in_end: return None&#10;        root = TreeNode(preorder[pre_start])&#10;        in_root = in_map[root.val]&#10;        nums_left = in_root - in_start&#10;        root.left = build(pre_start + 1, pre_start + nums_left, in_start, in_root - 1)&#10;        root.right = build(pre_start + nums_left + 1, pre_end, in_root + 1, in_end)&#10;        return root&#10;    return build(0, len(preorder) - 1, 0, len(inorder) - 1)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">11</td>
      <td rowspan="1">Tree 11 Maximum Path Sum<br><br></b> <a href="https://leetcode.com/problems/binary-tree-maximum-path-sum/" target="_blank">LeetCode 124</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, SDE Sheet, Striver A Z, Apna College</details></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> root = [-10,9,20,null,null,15,7]<br><b>Output:</b> 42</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>DFS returning max path sum down a single branch. At any node, max path = `node.val + max(0, leftPath) + max(0, rightPath)`. Ignore negative branches.<br><br><b>Dependencies:</b> <code>#include <limits.h></code></td>
      <td><b>Edge Cases:</b> <b>All Negative Nodes:</b> Initialization with `INT_MIN` properly returns the least negative node.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxPathSum(root: Optional[TreeNode]) -&gt; int:&#10;    maxi = [float(&#x27;-inf&#x27;)]&#10;    def maxPathDown(node):&#10;        if not node: return 0&#10;        left = max(0, maxPathDown(node.left))&#10;        right = max(0, maxPathDown(node.right))&#10;        maxi[0] = max(maxi[0], left + right + node.val)&#10;        return max(left, right) + node.val&#10;    maxPathDown(root)&#10;    return int(maxi[0])</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">12</td>
      <td rowspan="1">Tree 12 Boundary Traversal<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, SDE Sheet, Striver A Z, Apna College</details></td>
      <td rowspan="1"><b>Example 1:</b> Return array of boundary nodes.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>1) Add root if not leaf. 2) Traverse left boundary (excluding leaves). 3) Inorder traverse all leaves. 4) Traverse right boundary, reverse it, then add to answer.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def printBoundaryView(root: TreeNode) -&gt; List[int]:&#10;    if not root: return []&#10;    res = []&#10;    def isLeaf(node): return not node.left and not node.right&#10;    if not isLeaf(root): res.append(root.val)&#10;    cur = root.left&#10;    while cur:&#10;        if not isLeaf(cur): res.append(cur.val)&#10;        cur = cur.left if cur.left else cur.right&#10;    def addLeaves(node):&#10;        if isLeaf(node): res.append(node.val); return&#10;        if node.left: addLeaves(node.left)&#10;        if node.right: addLeaves(node.right)&#10;    addLeaves(root)&#10;    cur = root.right; tmp = []&#10;    while cur:&#10;        if not isLeaf(cur): tmp.append(cur.val)&#10;        cur = cur.right if cur.right else cur.left&#10;    res.extend(tmp[::-1])&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">13</td>
      <td rowspan="1">Tree 13 Zigzag Traversal<br><br></b> <a href="https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/" target="_blank">LeetCode 103</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> root = [3,9,20,null,null,15,7]<br><b>Output:</b> [[3],[20,9],[15,7]]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Standard BFS Level Order Traversal with a boolean flag `leftToRight`. After finishing a level, if the flag is false, reverse the level array before adding to the result.<br><br><b>Dependencies:</b> <code>#include <queue></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def zigzagLevelOrder(root: Optional[TreeNode]) -&gt; List[List[int]]:&#10;    result = []&#10;    if not root: return result&#10;    q = collections.deque([root])&#10;    leftToRight = True&#10;    while q:&#10;        size = len(q)&#10;        row = [0] * size&#10;        for i in range(size):&#10;            node = q.popleft()&#10;            index = i if leftToRight else (size - 1 - i)&#10;            row[index] = node.val&#10;            if node.left: q.append(node.left)&#10;            if node.right: q.append(node.right)&#10;        leftToRight = not leftToRight&#10;        result.append(row)&#10;    return result</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">14</td>
      <td rowspan="1">Tree 14 Symmetric Tree<br><br></b> <a href="https://leetcode.com/problems/symmetric-tree/" target="_blank">LeetCode 101</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, SDE Sheet</details></td>
      <td rowspan="1"><b>Example 1:</b> Recursive.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>Use a helper function `isMirror(left, right)`. The tree is symmetric if `root->left` and `root->right` are mirrors. Two trees are mirrors if their roots are equal and `left1->left` is mirror of `right1->right`, and `left1->right` is mirror of `right1->left`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isSymmetric(root):&#10;    def isMirror(n1, n2):&#10;        if not n1 and not n2: return True&#10;        if not n1 or not n2: return False&#10;        return (n1.val == n2.val) and isMirror(n1.left, n2.right) and isMirror(n1.right, n2.left)&#10;    if not root: return True&#10;    return isMirror(root.left, root.right)</code></pre></details></td>
    </tr>
  </tbody>
</table>
