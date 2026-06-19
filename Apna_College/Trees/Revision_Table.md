# Trees Revision Table

<table border="1">
  <thead>
    <tr>
      <th rowspan="2" style="width: 5%;">S.No</th>
      <th rowspan="2" style="width: 15%;">Problem Name</th>
      <th rowspan="2" style="width: 25%;">Example & Constraints</th>
      <th rowspan="2" style="width: 10%;">Complexity</th>
      <th colspan="2" style="width: 20%;">Conditions & Edge Cases</th>
      <th rowspan="2" style="width: 25%;">Logic</th>
    </tr>
    <tr>
      <th>Dependencies / Setup</th>
      <th>Edge Case Handling</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="1">1</td>
      <td rowspan="1">Tree 10 Lowest Common Ancestor<br><br></b> <a href='https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/' target='_blank'>LeetCode 236</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: root = [3,5,1,6,2,0,8], p = 5, q = 1, Output: 3</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H) recursion stack</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> DFS traversal. If root is NULL or equals p or q, return root. Recursively find LCA in left and right subtrees. If both return non-null, root is LCA. Otherwise return the non-null child.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def lowestCommonAncestor(root: &#x27;TreeNode&#x27;, p: &#x27;TreeNode&#x27;, q: &#x27;TreeNode&#x27;) -&gt; &#x27;TreeNode&#x27;:&#10;    if not root or root == p or root == q: return root&#10;    left = lowestCommonAncestor(root.left, p, q)&#10;    right = lowestCommonAncestor(root.right, p, q)&#10;    if left and right: return root&#10;    return left if left else right</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">2</td>
      <td rowspan="1">Tree 11 Construct Tree From Preorder And Inorder<br><br></b> <a href='https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/' target='_blank'>LeetCode 105</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7], Output: [3,9,20,null,null,15,7]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N) for Hash Map</td>
      <td><code>#include <unordered_map></code></td>
      <td>-</td>
      <td><b>Explanation:</b> First element of preorder is the root. Find this element in inorder to split into left and right subtrees. Use a Hash Map to store inorder indices for O(1) lookups.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def buildTree(preorder: List[int], inorder: List[int]) -&gt; Optional[TreeNode]:&#10;    in_map = {val: i for i, val in enumerate(inorder)}&#10;    def build(pre_start, pre_end, in_start, in_end):&#10;        if pre_start &gt; pre_end or in_start &gt; in_end: return None&#10;        root = TreeNode(preorder[pre_start])&#10;        in_root = in_map[root.val]&#10;        nums_left = in_root - in_start&#10;        root.left = build(pre_start + 1, pre_start + nums_left, in_start, in_root - 1)&#10;        root.right = build(pre_start + nums_left + 1, pre_end, in_root + 1, in_end)&#10;        return root&#10;    return build(0, len(preorder) - 1, 0, len(inorder) - 1)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">3</td>
      <td rowspan="1">Tree 12 Diameter Of Binary Tree<br><br></b> <a href='https://leetcode.com/problems/diameter-of-binary-tree/' target='_blank'>LeetCode 543</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: root = [1,2,3,4,5], Output: 3</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Modify the standard Height of Binary Tree DFS. Compute left height and right height. At each node, the diameter passing through it is `left + right`. Track the max.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def diameterOfBinaryTree(root: Optional[TreeNode]) -&gt; int:&#10;    diameter = [0]&#10;    def height(node):&#10;        if not node: return 0&#10;        lh = height(node.left)&#10;        rh = height(node.right)&#10;        diameter[0] = max(diameter[0], lh + rh)&#10;        return 1 + max(lh, rh)&#10;    height(root)&#10;    return diameter[0]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">4</td>
      <td rowspan="1">Tree 13 Maximum Path Sum<br><br></b> <a href='https://leetcode.com/problems/binary-tree-maximum-path-sum/' target='_blank'>LeetCode 124</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: root = [-10,9,20,null,null,15,7], Output: 42</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td><code>#include <limits.h></code></td>
      <td><b>All Negative Nodes:</b> Initialization with `INT_MIN` properly returns the least negative node.</td>
      <td><b>Explanation:</b> DFS returning max path sum down a single branch. At any node, max path = `node.val + max(0, leftPath) + max(0, rightPath)`. Ignore negative branches.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxPathSum(root: Optional[TreeNode]) -&gt; int:&#10;    maxi = [float(&#x27;-inf&#x27;)]&#10;    def maxPathDown(node):&#10;        if not node: return 0&#10;        left = max(0, maxPathDown(node.left))&#10;        right = max(0, maxPathDown(node.right))&#10;        maxi[0] = max(maxi[0], left + right + node.val)&#10;        return max(left, right) + node.val&#10;    maxPathDown(root)&#10;    return int(maxi[0])</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">5</td>
      <td rowspan="1">Tree 14 Same Tree<br><br></b> <a href='https://leetcode.com/problems/same-tree/' target='_blank'>LeetCode 100</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: p = [1,2,3], q = [1,2,3], Output: true</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Preorder DFS simultaneously on both trees. If both are null, true. If one is null or vals mismatch, false. Recursively check left and right subtrees.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -&gt; bool:&#10;    if not p or not q: return p == q&#10;    return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">6</td>
      <td rowspan="1">Tree 15 Boundary Traversal<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1' target='_blank'>GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Return array of boundary nodes.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> 1) Add root if not leaf. 2) Traverse left boundary (excluding leaves). 3) Inorder traverse all leaves. 4) Traverse right boundary, reverse it, then add to answer.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def printBoundaryView(root: TreeNode) -&gt; List[int]:&#10;    if not root: return []&#10;    res = []&#10;    def isLeaf(node): return not node.left and not node.right&#10;    if not isLeaf(root): res.append(root.val)&#10;    cur = root.left&#10;    while cur:&#10;        if not isLeaf(cur): res.append(cur.val)&#10;        cur = cur.left if cur.left else cur.right&#10;    def addLeaves(node):&#10;        if isLeaf(node): res.append(node.val); return&#10;        if node.left: addLeaves(node.left)&#10;        if node.right: addLeaves(node.right)&#10;    addLeaves(root)&#10;    cur = root.right; tmp = []&#10;    while cur:&#10;        if not isLeaf(cur): tmp.append(cur.val)&#10;        cur = cur.right if cur.right else cur.left&#10;    res.extend(tmp[::-1])&#10;    return res</code></pre></details></td>
    </tr>
  </tbody>
</table>
