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
      <td rowspan="1">Tree 01 Binary Tree Inorder Traversal<br><br></b> <a href='https://leetcode.com/problems/binary-tree-inorder-traversal/' target='_blank'>LeetCode 94</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: root = [1,null,2,3], Output: [1,3,2]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td><b>Recursion Depth:</b> Worst-case skewed tree takes `O(N)` space.</td>
      <td><b>Explanation:</b> Recursive approach. Traverse Left, process Root, then traverse Right.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def inorderTraversal(root: TreeNode) -&gt; list[int]:&#10;    ans = []&#10;    def inorder(node):&#10;        if not node: return&#10;        inorder(node.left)&#10;        ans.append(node.val)&#10;        inorder(node.right)&#10;    inorder(root)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">2</td>
      <td rowspan="1">Tree 02 Maximum Depth Of Binary Tree<br><br></b> <a href='https://leetcode.com/problems/maximum-depth-of-binary-tree/' target='_blank'>LeetCode 104</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: root = [3,9,20,null,null,15,7], Output: 3</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H) &cong; O(N)</td>
      <td><code>std::max</code></td>
      <td><b>Null Root:</b> If empty (`root == NULL`), depth is 0.</td>
      <td><b>Explanation:</b> Recursively find the max depth of left and right subtrees. The depth is `1 + max(left_depth, right_depth)`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxDepth(root: TreeNode) -&gt; int:&#10;    if not root: return 0&#10;    return 1 + max(maxDepth(root.left), maxDepth(root.right))</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">3</td>
      <td rowspan="1">Tree 03 Lowest Common Ancestor Of A Binary Tree<br><br></b> <a href='https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/' target='_blank'>LeetCode 236</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1, Output: 3</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td><b>Node is LCA:</b> If one is ancestor of other, it returns immediately.</td>
      <td><b>Explanation:</b> If we find `p` or `q`, return it. If both left and right return non-null, current node is LCA.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -&gt; TreeNode:&#10;    if not root or root == p or root == q: return root&#10;    left = lowestCommonAncestor(root.left, p, q)&#10;    right = lowestCommonAncestor(root.right, p, q)&#10;    if not left: return right&#10;    elif not right: return left&#10;    else: return root</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">4</td>
      <td rowspan="1">Tree 04 Same Tree<br><br></b> <a href='https://leetcode.com/problems/same-tree/' target='_blank'>LeetCode 100</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: p = [1,2,3], q = [1,2,3], Output: true</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td><b>Structural mismatch:</b> Safely handled by `!p || !q`.</td>
      <td><b>Explanation:</b> Traverse both trees simultaneously. If both nodes are null, true. If one is null or values mismatch, false.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isSameTree(p: TreeNode, q: TreeNode) -&gt; bool:&#10;    if not p and not q: return True&#10;    if not p or not q or p.val != q.val: return False&#10;    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">5</td>
      <td rowspan="1">Tree 05 Invert Binary Tree<br><br></b> <a href='https://leetcode.com/problems/invert-binary-tree/' target='_blank'>LeetCode 226</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: root = [4,2,7,1,3,6,9], Output: [4,7,2,9,6,3,1]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><code>std::swap</code></td>
      <td><b>Empty Tree:</b> Returns null immediately.</td>
      <td><b>Explanation:</b> Recursively swap the left and right children of every node.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def invertTree(root: TreeNode) -&gt; TreeNode:&#10;    if not root: return None&#10;    root.left, root.right = root.right, root.left&#10;    invertTree(root.left)&#10;    invertTree(root.right)&#10;    return root</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">6</td>
      <td rowspan="1">Tree 06 Diameter Of Binary Tree<br><br></b> <a href='https://leetcode.com/problems/diameter-of-binary-tree/' target='_blank'>LeetCode 543</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: root = [1,2,3,4,5], Output: 3 (Path is [4,2,1,3] or [5,2,1,3])</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><code>std::max</code></td>
      <td><b>Path doesn't pass through root:</b> Handled correctly by tracking the global maximum `max_d` at every recursive step.</td>
      <td><b>Explanation:</b> Modify the Height/Depth algorithm. Calculate `left_depth + right_depth` at every node to find max diameter, while returning standard height.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def diameterOfBinaryTree(root: TreeNode) -&gt; int:&#10;    max_d = [0]&#10;    def height(node):&#10;        if not node: return 0&#10;        left = height(node.left)&#10;        right = height(node.right)&#10;        max_d[0] = max(max_d[0], left + right)&#10;        return 1 + max(left, right)&#10;    height(root)&#10;    return max_d[0]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">7</td>
      <td rowspan="1">Tree 07 Balanced Binary Tree<br><br></b> <a href='https://leetcode.com/problems/balanced-binary-tree/' target='_blank'>LeetCode 110</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: root = [3,9,20,null,null,15,7], Output: true</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><code>std::abs</code></td>
      <td><b>Early Exit:</b> Checking if `left == -1` or `right == -1` immediately breaks the recursion, optimizing time.</td>
      <td><b>Explanation:</b> Modify the Height algorithm. If the difference between `left` and `right` height is > 1, return `-1` to propagate the unbalanced signal.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isBalanced(root: TreeNode) -&gt; bool:&#10;    def checkHeight(node):&#10;        if not node: return 0&#10;        left = checkHeight(node.left)&#10;        if left == -1: return -1&#10;        right = checkHeight(node.right)&#10;        if right == -1: return -1&#10;        if abs(left - right) &gt; 1: return -1&#10;        return 1 + max(left, right)&#10;    return checkHeight(root) != -1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">8</td>
      <td rowspan="1">Tree 08 Binary Search Tree Iterator<br><br></b> <a href='https://leetcode.com/problems/binary-search-tree-iterator/' target='_blank'>LeetCode 173</a></td>
      <td rowspan="1"><b>Example 1:</b> next() returns smallest element.</td>
      <td><b>Time:</b> O(1) amortized<br><b>Space:</b> O(H)</td>
      <td><code>#include <stack></code></td>
      <td><b>Empty Tree:</b> Stack is empty.</td>
      <td><b>Explanation:</b> Use a stack to simulate in-order traversal. Push all left children initially. On next(), pop, return val, and push all left children of popped node's right child.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class BSTIterator:&#10;    def __init__(self, root: TreeNode):&#10;        self.st = []&#10;        self.pushAll(root)&#10;    def pushAll(self, node):&#10;        while node:&#10;            self.st.append(node)&#10;            node = node.left&#10;    def next(self) -&gt; int:&#10;        tmp = self.st.pop()&#10;        self.pushAll(tmp.right)&#10;        return tmp.val&#10;    def hasNext(self) -&gt; bool:&#10;        return len(self.st) &gt; 0</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">9</td>
      <td rowspan="1">Tree 09 Validate Binary Search Tree<br><br></b> <a href='https://leetcode.com/problems/validate-binary-search-tree/' target='_blank'>LeetCode 98</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: root = [2,1,3], Output: true</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td><code>#include <limits.h></code></td>
      <td><b>Values reach INT bounds:</b> Use LLONG_MIN/LLONG_MAX bounds.</td>
      <td><b>Explanation:</b> Recursive validation with min and max bounds for every node. Long long is used to avoid overflow.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isValidBST(root: TreeNode) -&gt; bool:&#10;    def validate(node, low=-float(&#x27;inf&#x27;), high=float(&#x27;inf&#x27;)):&#10;        if not node: return True&#10;        if node.val &lt;= low or node.val &gt;= high: return False&#10;        return validate(node.left, low, node.val) and validate(node.right, node.val, high)&#10;    return validate(root)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">10</td>
      <td rowspan="1">Tree 10 Lowest Common Ancestor<br><br></b> <a href='https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/' target='_blank'>LeetCode 236</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: root = [3,5,1,6,2,0,8], p = 5, q = 1, Output: 3</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H) recursion stack</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> DFS traversal. If root is NULL or equals p or q, return root. Recursively find LCA in left and right subtrees. If both return non-null, root is LCA. Otherwise return the non-null child.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def lowestCommonAncestor(root: &#x27;TreeNode&#x27;, p: &#x27;TreeNode&#x27;, q: &#x27;TreeNode&#x27;) -&gt; &#x27;TreeNode&#x27;:&#10;    if not root or root == p or root == q: return root&#10;    left = lowestCommonAncestor(root.left, p, q)&#10;    right = lowestCommonAncestor(root.right, p, q)&#10;    if left and right: return root&#10;    return left if left else right</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">11</td>
      <td rowspan="1">Tree 11 Construct Tree From Preorder And Inorder<br><br></b> <a href='https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/' target='_blank'>LeetCode 105</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7], Output: [3,9,20,null,null,15,7]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N) for Hash Map</td>
      <td><code>#include <unordered_map></code></td>
      <td>-</td>
      <td><b>Explanation:</b> First element of preorder is the root. Find this element in inorder to split into left and right subtrees. Use a Hash Map to store inorder indices for O(1) lookups.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def buildTree(preorder: List[int], inorder: List[int]) -&gt; Optional[TreeNode]:&#10;    in_map = {val: i for i, val in enumerate(inorder)}&#10;    def build(pre_start, pre_end, in_start, in_end):&#10;        if pre_start &gt; pre_end or in_start &gt; in_end: return None&#10;        root = TreeNode(preorder[pre_start])&#10;        in_root = in_map[root.val]&#10;        nums_left = in_root - in_start&#10;        root.left = build(pre_start + 1, pre_start + nums_left, in_start, in_root - 1)&#10;        root.right = build(pre_start + nums_left + 1, pre_end, in_root + 1, in_end)&#10;        return root&#10;    return build(0, len(preorder) - 1, 0, len(inorder) - 1)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">12</td>
      <td rowspan="1">Tree 12 Diameter Of Binary Tree<br><br></b> <a href='https://leetcode.com/problems/diameter-of-binary-tree/' target='_blank'>LeetCode 543</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: root = [1,2,3,4,5], Output: 3</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Modify the standard Height of Binary Tree DFS. Compute left height and right height. At each node, the diameter passing through it is `left + right`. Track the max.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def diameterOfBinaryTree(root: Optional[TreeNode]) -&gt; int:&#10;    diameter = [0]&#10;    def height(node):&#10;        if not node: return 0&#10;        lh = height(node.left)&#10;        rh = height(node.right)&#10;        diameter[0] = max(diameter[0], lh + rh)&#10;        return 1 + max(lh, rh)&#10;    height(root)&#10;    return diameter[0]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">13</td>
      <td rowspan="1">Tree 13 Maximum Path Sum<br><br></b> <a href='https://leetcode.com/problems/binary-tree-maximum-path-sum/' target='_blank'>LeetCode 124</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: root = [-10,9,20,null,null,15,7], Output: 42</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td><code>#include <limits.h></code></td>
      <td><b>All Negative Nodes:</b> Initialization with `INT_MIN` properly returns the least negative node.</td>
      <td><b>Explanation:</b> DFS returning max path sum down a single branch. At any node, max path = `node.val + max(0, leftPath) + max(0, rightPath)`. Ignore negative branches.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxPathSum(root: Optional[TreeNode]) -&gt; int:&#10;    maxi = [float(&#x27;-inf&#x27;)]&#10;    def maxPathDown(node):&#10;        if not node: return 0&#10;        left = max(0, maxPathDown(node.left))&#10;        right = max(0, maxPathDown(node.right))&#10;        maxi[0] = max(maxi[0], left + right + node.val)&#10;        return max(left, right) + node.val&#10;    maxPathDown(root)&#10;    return int(maxi[0])</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">14</td>
      <td rowspan="1">Tree 14 Same Tree<br><br></b> <a href='https://leetcode.com/problems/same-tree/' target='_blank'>LeetCode 100</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: p = [1,2,3], q = [1,2,3], Output: true</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Preorder DFS simultaneously on both trees. If both are null, true. If one is null or vals mismatch, false. Recursively check left and right subtrees.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -&gt; bool:&#10;    if not p or not q: return p == q&#10;    return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">15</td>
      <td rowspan="1">Tree 15 Boundary Traversal<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1' target='_blank'>GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Return array of boundary nodes.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> 1) Add root if not leaf. 2) Traverse left boundary (excluding leaves). 3) Inorder traverse all leaves. 4) Traverse right boundary, reverse it, then add to answer.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def printBoundaryView(root: TreeNode) -&gt; List[int]:&#10;    if not root: return []&#10;    res = []&#10;    def isLeaf(node): return not node.left and not node.right&#10;    if not isLeaf(root): res.append(root.val)&#10;    cur = root.left&#10;    while cur:&#10;        if not isLeaf(cur): res.append(cur.val)&#10;        cur = cur.left if cur.left else cur.right&#10;    def addLeaves(node):&#10;        if isLeaf(node): res.append(node.val); return&#10;        if node.left: addLeaves(node.left)&#10;        if node.right: addLeaves(node.right)&#10;    addLeaves(root)&#10;    cur = root.right; tmp = []&#10;    while cur:&#10;        if not isLeaf(cur): tmp.append(cur.val)&#10;        cur = cur.right if cur.right else cur.left&#10;    res.extend(tmp[::-1])&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">16</td>
      <td rowspan="1">Tree 16 Zigzag Traversal<br><br></b> <a href='https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/' target='_blank'>LeetCode 103</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: root = [3,9,20,null,null,15,7], Output: [[3],[20,9],[15,7]]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><code>#include <queue></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Standard BFS Level Order Traversal with a boolean flag `leftToRight`. After finishing a level, if the flag is false, reverse the level array before adding to the result.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def zigzagLevelOrder(root: Optional[TreeNode]) -&gt; List[List[int]]:&#10;    result = []&#10;    if not root: return result&#10;    q = collections.deque([root])&#10;    leftToRight = True&#10;    while q:&#10;        size = len(q)&#10;        row = [0] * size&#10;        for i in range(size):&#10;            node = q.popleft()&#10;            index = i if leftToRight else (size - 1 - i)&#10;            row[index] = node.val&#10;            if node.left: q.append(node.left)&#10;            if node.right: q.append(node.right)&#10;        leftToRight = not leftToRight&#10;        result.append(row)&#10;    return result</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">17</td>
      <td rowspan="1">Tree 17 Vertical Order Traversal<br><br></b> <a href='https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/' target='_blank'>LeetCode 987</a></td>
      <td rowspan="1"><b>Example 1:</b> Output: [[9],[3,15],[20],[7]]</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(N)</td>
      <td><code>#include <map>\n#include <queue>\n#include <set></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Use a map structure: `map<int, map<int, multiset<int>>>` to store nodes mapped by their horizontal distance and level. BFS traversal ensures levels are processed top-down.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def verticalTraversal(root: Optional[TreeNode]) -&gt; List[List[int]]:&#10;    nodes = collections.defaultdict(lambda: collections.defaultdict(list))&#10;    todo = collections.deque([(root, 0, 0)])&#10;    while todo:&#10;        node, x, y = todo.popleft()&#10;        nodes[x][y].append(node.val)&#10;        if node.left: todo.append((node.left, x - 1, y + 1))&#10;        if node.right: todo.append((node.right, x + 1, y + 1))&#10;    ans = []&#10;    for x in sorted(nodes.keys()):&#10;        col = []&#10;        for y in sorted(nodes[x].keys()):&#10;            col.extend(sorted(nodes[x][y]))&#10;        ans.append(col)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">18</td>
      <td rowspan="1">Tree 18 Top View<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1' target='_blank'>GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Return list of values.</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(N)</td>
      <td><code>#include <map>\n#include <queue></code></td>
      <td>-</td>
      <td><b>Explanation:</b> BFS traversal maintaining horizontal distance (HD) from root. Use a map `hd -> value`. Only insert into the map if the HD is not already present, ensuring the top-most node is recorded.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def topView(root: Optional[Node]) -&gt; List[int]:&#10;    ans = []&#10;    if not root: return ans&#10;    mpp = {}&#10;    q = collections.deque([(root, 0)])&#10;    while q:&#10;        node, line = q.popleft()&#10;        if line not in mpp: mpp[line] = node.data&#10;        if node.left: q.append((node.left, line - 1))&#10;        if node.right: q.append((node.right, line + 1))&#10;    for line in sorted(mpp.keys()): ans.append(mpp[line])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">19</td>
      <td rowspan="1">Tree 19 Bottom View<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1' target='_blank'>GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Return list of values.</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(N)</td>
      <td><code>#include <map>\n#include <queue></code></td>
      <td>-</td>
      <td><b>Explanation:</b> BFS traversal maintaining horizontal distance (HD). Map `hd -> value`. Always update the map value for a given HD so that the last node encountered (bottom-most) overrides previous ones.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def bottomView(root: Optional[Node]) -&gt; List[int]:&#10;    ans = []&#10;    if not root: return ans&#10;    mpp = {}&#10;    q = collections.deque([(root, 0)])&#10;    while q:&#10;        node, line = q.popleft()&#10;        mpp[line] = node.data&#10;        if node.left: q.append((node.left, line - 1))&#10;        if node.right: q.append((node.right, line + 1))&#10;    for line in sorted(mpp.keys()): ans.append(mpp[line])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">20</td>
      <td rowspan="1">Tree 20 Right View<br><br></b> <a href='https://leetcode.com/problems/binary-tree-right-side-view/' target='_blank'>LeetCode 199</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: root = [1,2,3,null,5,null,4], Output: [1,3,4]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> DFS Traversing right child before left child. Maintain the current level. If `level == result.size()`, append the node value to the result list.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def rightSideView(root: Optional[TreeNode]) -&gt; List[int]:&#10;    res = []&#10;    def recursion(node, level):&#10;        if not node: return&#10;        if len(res) == level: res.append(node.val)&#10;        recursion(node.right, level + 1)&#10;        recursion(node.left, level + 1)&#10;    recursion(root, 0)&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">21</td>
      <td rowspan="1">Tree 21 Left View<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/left-view-of-binary-tree/1' target='_blank'>GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Print left-most node at each level.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> DFS Traversing left child before right child. Maintain the current level. If `level == result.size()`, append the node value to the result list.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def leftView(root: Optional[Node]) -&gt; List[int]:&#10;    res = []&#10;    def recursion(node, level):&#10;        if not node: return&#10;        if len(res) == level: res.append(node.data)&#10;        recursion(node.left, level + 1)&#10;        recursion(node.right, level + 1)&#10;    recursion(root, 0)&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">22</td>
      <td rowspan="1">Tree 22 Construct Tree From Inorder And Preorder<br><br></b> <a href='https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/' target='_blank'>LeetCode 105</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7], Output: [3,9,20,null,null,15,7]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><code>#include <unordered_map></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Store inorder indices in a HashMap. The first element in preorder is the root. Find this root in inorder map to determine left subtree size. Recursively build left and right subtrees by slicing array indices.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def buildTree(preorder: List[int], inorder: List[int]) -&gt; Optional[TreeNode]:&#10;    inMap = {val: i for i, val in enumerate(inorder)}&#10;    def build(preStart, preEnd, inStart, inEnd):&#10;        if preStart &gt; preEnd or inStart &gt; inEnd: return None&#10;        root = TreeNode(preorder[preStart])&#10;        inRoot = inMap[root.val]&#10;        numsLeft = inRoot - inStart&#10;        root.left = build(preStart + 1, preStart + numsLeft, inStart, inRoot - 1)&#10;        root.right = build(preStart + numsLeft + 1, preEnd, inRoot + 1, inEnd)&#10;        return root&#10;    return build(0, len(preorder) - 1, 0, len(inorder) - 1)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">23</td>
      <td rowspan="1">Tree 23 Construct Tree From Inorder And Postorder<br><br></b> <a href='https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/' target='_blank'>LeetCode 106</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3], Output: [3,9,20,null,null,15,7]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><code>#include <unordered_map></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Store inorder indices in a HashMap. The last element in postorder is the root. Find this root in inorder map to determine left subtree size. Recursively build left and right subtrees by slicing array indices.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def buildTree(inorder: List[int], postorder: List[int]) -&gt; Optional[TreeNode]:&#10;    inMap = {val: i for i, val in enumerate(inorder)}&#10;    def build(inStart, inEnd, postStart, postEnd):&#10;        if inStart &gt; inEnd or postStart &gt; postEnd: return None&#10;        root = TreeNode(postorder[postEnd])&#10;        inRoot = inMap[root.val]&#10;        numsLeft = inRoot - inStart&#10;        root.left = build(inStart, inRoot - 1, postStart, postStart + numsLeft - 1)&#10;        root.right = build(inRoot + 1, inEnd, postStart + numsLeft, postEnd - 1)&#10;        return root&#10;    return build(0, len(inorder) - 1, 0, len(postorder) - 1)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">24</td>
      <td rowspan="1">Tree 24 Serialize And Deserialize Binary Tree<br><br></b> <a href='https://leetcode.com/problems/serialize-and-deserialize-binary-tree/' target='_blank'>LeetCode 297</a></td>
      <td rowspan="1"><b>Example 1:</b> Serialization/Deserialization.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><code>#include <queue>\n#include <sstream></code></td>
      <td><b>Empty Tree:</b> Serialized string is empty. Deserialize returns null.</td>
      <td><b>Explanation:</b> Use Level Order Traversal (BFS) using a queue. For serialization, append '#' for null nodes. For deserialization, split string by comma and use a queue to reconstruct the tree structure level by level.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;class Codec:&#10;    def serialize(self, root):&#10;        if not root: return &quot;&quot;&#10;        s = []; q = collections.deque([root])&#10;        while q:&#10;            node = q.popleft()&#10;            if node is None: s.append(&quot;#&quot;)&#10;            else: s.append(str(node.val)); q.append(node.left); q.append(node.right)&#10;        return &quot;,&quot;.join(s)&#10;    def deserialize(self, data):&#10;        if not data: return None&#10;        values = data.split(&quot;,&quot;)&#10;        root = TreeNode(int(values[0]))&#10;        q = collections.deque([root])&#10;        i = 1&#10;        while q:&#10;            node = q.popleft()&#10;            if values[i] != &quot;#&quot;: node.left = TreeNode(int(values[i])); q.append(node.left)&#10;            i += 1&#10;            if values[i] != &quot;#&quot;: node.right = TreeNode(int(values[i])); q.append(node.right)&#10;            i += 1&#10;        return root</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">25</td>
      <td rowspan="1">Tree 25 Lowest Common Ancestor<br><br></b> <a href='https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/' target='_blank'>LeetCode 236</a></td>
      <td rowspan="1"><b>Example 1:</b> Return the LCA node.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> DFS traversal. If the current node is p or q, return the current node. Recurse left and right. If both left and right return non-null, the current node is the LCA. If one returns non-null, return that one.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def lowestCommonAncestor(root: &#x27;TreeNode&#x27;, p: &#x27;TreeNode&#x27;, q: &#x27;TreeNode&#x27;) -&gt; &#x27;TreeNode&#x27;:&#10;    if root is None or root == p or root == q: return root&#10;    left = lowestCommonAncestor(root.left, p, q)&#10;    right = lowestCommonAncestor(root.right, p, q)&#10;    if left is None: return right&#10;    elif right is None: return left&#10;    else: return root</code></pre></details></td>
    </tr>
  </tbody>
</table>
