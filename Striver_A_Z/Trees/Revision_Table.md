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
    <tr>
      <td rowspan="1">26</td>
      <td rowspan="1">Tree 25 Construct Binary Tree From Preorder And Inorder Traversal<br><br></b> <a href='https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/' target='_blank'>LeetCode 105</a></td>
      <td rowspan="1"><b>Example 1:</b> Recursive construction.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><code>#include <unordered_map></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Use a hash map to store indices of inorder elements. The first element of preorder is the root. Find its index in inorder array to divide into left and right subtrees. Recursively build left and right.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def buildTree(preorder: List[int], inorder: List[int]) -&gt; Optional[TreeNode]:&#10;    inMap = {val: i for i, val in enumerate(inorder)}&#10;    def helper(preStart, preEnd, inStart, inEnd):&#10;        if preStart &gt; preEnd or inStart &gt; inEnd: return None&#10;        root = TreeNode(preorder[preStart])&#10;        inRoot = inMap[root.val]&#10;        numsLeft = inRoot - inStart&#10;        root.left = helper(preStart + 1, preStart + numsLeft, inStart, inRoot - 1)&#10;        root.right = helper(preStart + numsLeft + 1, preEnd, inRoot + 1, inEnd)&#10;        return root&#10;    return helper(0, len(preorder) - 1, 0, len(inorder) - 1)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">27</td>
      <td rowspan="1">Tree 26 Construct Binary Tree From Inorder And Postorder Traversal<br><br></b> <a href='https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/' target='_blank'>LeetCode 106</a></td>
      <td rowspan="1"><b>Example 1:</b> Recursive construction.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><code>#include <unordered_map></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Similar to preorder+inorder, but the root is at the end of the postorder array. Map inorder indices. Find root, divide, and recurse.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def buildTree(inorder: List[int], postorder: List[int]) -&gt; Optional[TreeNode]:&#10;    inMap = {val: i for i, val in enumerate(inorder)}&#10;    def helper(inStart, inEnd, postStart, postEnd):&#10;        if inStart &gt; inEnd or postStart &gt; postEnd: return None&#10;        root = TreeNode(postorder[postEnd])&#10;        inRoot = inMap[root.val]&#10;        numsLeft = inRoot - inStart&#10;        root.left = helper(inStart, inRoot - 1, postStart, postStart + numsLeft - 1)&#10;        root.right = helper(inRoot + 1, inEnd, postStart + numsLeft, postEnd - 1)&#10;        return root&#10;    return helper(0, len(inorder) - 1, 0, len(postorder) - 1)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">28</td>
      <td rowspan="1">Tree 27 Serialize And Deserialize Binary Tree<br><br></b> <a href='https://leetcode.com/problems/serialize-and-deserialize-binary-tree/' target='_blank'>LeetCode 297</a></td>
      <td rowspan="1"><b>Example 1:</b> String based tree.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><code>#include <queue>\n#include <sstream></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Use Level Order Traversal (BFS) to serialize into a comma-separated string, using '#' for null. For deserialization, split string and use a queue to rebuild.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;class Codec:&#10;    def serialize(self, root):&#10;        if not root: return &quot;&quot;&#10;        q = collections.deque([root])&#10;        res = []&#10;        while q:&#10;            node = q.popleft()&#10;            if node:&#10;                res.append(str(node.val))&#10;                q.append(node.left)&#10;                q.append(node.right)&#10;            else:&#10;                res.append(&quot;#&quot;)&#10;        return &quot;,&quot;.join(res)&#10;    def deserialize(self, data):&#10;        if not data: return None&#10;        values = data.split(&quot;,&quot;)&#10;        root = TreeNode(int(values[0]))&#10;        q = collections.deque([root])&#10;        i = 1&#10;        while q:&#10;            node = q.popleft()&#10;            if values[i] != &quot;#&quot;:&#10;                node.left = TreeNode(int(values[i]))&#10;                q.append(node.left)&#10;            i += 1&#10;            if values[i] != &quot;#&quot;:&#10;                node.right = TreeNode(int(values[i]))&#10;                q.append(node.right)&#10;            i += 1&#10;        return root</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">29</td>
      <td rowspan="1">Tree 28 Flatten Binary Tree To Linked List<br><br></b> <a href='https://leetcode.com/problems/flatten-binary-tree-to-linked-list/' target='_blank'>LeetCode 114</a></td>
      <td rowspan="1"><b>Example 1:</b> In-place flatten.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Morris Traversal. If node has a left child, find the rightmost node of the left subtree. Point its right to current node's right. Move current node's left to its right, and set left to null. Move to current's right.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def flatten(root: Optional[TreeNode]) -&gt; None:&#10;    curr = root&#10;    while curr:&#10;        if curr.left:&#10;            pre = curr.left&#10;            while pre.right: pre = pre.right&#10;            pre.right = curr.right&#10;            curr.right = curr.left&#10;            curr.left = None&#10;        curr = curr.right</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">30</td>
      <td rowspan="1">Tree 29 Validate Binary Search Tree<br><br></b> <a href='https://leetcode.com/problems/validate-binary-search-tree/' target='_blank'>LeetCode 98</a></td>
      <td rowspan="1"><b>Example 1:</b> Check valid ranges.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>-</td>
      <td><b>Integer Overflow:</b> Use long long for bounds to handle INT_MIN/INT_MAX node values.</td>
      <td><b>Explanation:</b> Recursive validation with min and max bounds. `isValidBST(root, min_val, max_val)`. Ensure `min_val < root.val < max_val`. For left child update `max_val = root.val`. For right child update `min_val = root.val`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isValidBST(root: Optional[TreeNode]) -&gt; bool:&#10;    def helper(node, min_val, max_val):&#10;        if not node: return True&#10;        if not (min_val &lt; node.val &lt; max_val): return False&#10;        return helper(node.left, min_val, node.val) and helper(node.right, node.val, max_val)&#10;    return helper(root, float(&#x27;-inf&#x27;), float(&#x27;inf&#x27;))</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">31</td>
      <td rowspan="1">Tree 30 Kth Smallest Element In A Bst<br><br></b> <a href='https://leetcode.com/problems/kth-smallest-element-in-a-bst/' target='_blank'>LeetCode 230</a></td>
      <td rowspan="1"><b>Example 1:</b> Inorder traversal.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1) using Morris Traversal</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Inorder traversal of BST gives sorted elements. Keep a counter, when it reaches K, store the result. Morris Traversal can do this in O(1) space.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def kthSmallest(root: Optional[TreeNode], k: int) -&gt; int:&#10;    count, ans = 0, -1&#10;    curr = root&#10;    while curr:&#10;        if curr.left is None:&#10;            count += 1&#10;            if count == k: ans = curr.val&#10;            curr = curr.right&#10;        else:&#10;            pre = curr.left&#10;            while pre.right and pre.right != curr: pre = pre.right&#10;            if pre.right is None:&#10;                pre.right = curr&#10;                curr = curr.left&#10;            else:&#10;                pre.right = None&#10;                count += 1&#10;                if count == k: ans = curr.val&#10;                curr = curr.right&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">32</td>
      <td rowspan="1">Tree 31 Lowest Common Ancestor Of A Binary Search Tree<br><br></b> <a href='https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/' target='_blank'>LeetCode 235</a></td>
      <td rowspan="1"><b>Example 1:</b> Exploit BST property.</td>
      <td><b>Time:</b> O(H)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> If both `p` and `q` are less than root, LCA is in the left subtree. If both are greater, LCA is in the right subtree. Otherwise, the current node is the LCA.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def lowestCommonAncestor(root: &#x27;TreeNode&#x27;, p: &#x27;TreeNode&#x27;, q: &#x27;TreeNode&#x27;) -&gt; &#x27;TreeNode&#x27;:&#10;    while root:&#10;        if root.val &gt; p.val and root.val &gt; q.val: root = root.left&#10;        elif root.val &lt; p.val and root.val &lt; q.val: root = root.right&#10;        else: return root&#10;    return None</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">33</td>
      <td rowspan="1">Tree 32 Insert Into A Binary Search Tree<br><br></b> <a href='https://leetcode.com/problems/insert-into-a-binary-search-tree/' target='_blank'>LeetCode 701</a></td>
      <td rowspan="1"><b>Example 1:</b> Traverse and insert.</td>
      <td><b>Time:</b> O(H)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Traverse left or right depending on the value. Keep track of parent. Insert as left or right child of parent when a null pointer is reached.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def insertIntoBST(root: Optional[TreeNode], val: int) -&gt; Optional[TreeNode]:&#10;    if not root: return TreeNode(val)&#10;    curr = root&#10;    while True:&#10;        if val &lt; curr.val:&#10;            if curr.left: curr = curr.left&#10;            else: curr.left = TreeNode(val); break&#10;        else:&#10;            if curr.right: curr = curr.right&#10;            else: curr.right = TreeNode(val); break&#10;    return root</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">34</td>
      <td rowspan="1">Tree 33 Delete Node In A Bst<br><br></b> <a href='https://leetcode.com/problems/delete-node-in-a-bst/' target='_blank'>LeetCode 450</a></td>
      <td rowspan="1"><b>Example 1:</b> Locate and delete.</td>
      <td><b>Time:</b> O(H)<br><b>Space:</b> O(H) or O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Find the node. If it has no left child, return right child. If no right, return left. If both exist, find the right child of the rightmost node in the left subtree, and point it to the node's right child. Return the node's left child.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def deleteNode(root: Optional[TreeNode], key: int) -&gt; Optional[TreeNode]:&#10;    def helper(node):&#10;        if not node.left: return node.right&#10;        if not node.right: return node.left&#10;        rightChild = node.right&#10;        lastRight = node.left&#10;        while lastRight.right: lastRight = lastRight.right&#10;        lastRight.right = rightChild&#10;        return node.left&#10;    if not root: return None&#10;    if root.val == key: return helper(root)&#10;    curr = root&#10;    while curr:&#10;        if curr.val &gt; key:&#10;            if curr.left and curr.left.val == key:&#10;                curr.left = helper(curr.left)&#10;                break&#10;            else: curr = curr.left&#10;        else:&#10;            if curr.right and curr.right.val == key:&#10;                curr.right = helper(curr.right)&#10;                break&#10;            else: curr = curr.right&#10;    return root</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">35</td>
      <td rowspan="1">Tree 34 Inorder Successor In Bst<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/inorder-successor-in-bst/1' target='_blank'>GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Find next greater.</td>
      <td><b>Time:</b> O(H)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Traverse BST. If `curr.val > node.val`, then `curr` is a potential successor, store it and move left to find smaller. Else, move right.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def inOrderSuccessor(root, x):&#10;    successor = None&#10;    while root:&#10;        if root.val &lt;= x.val:&#10;            root = root.right&#10;        else:&#10;            successor = root&#10;            root = root.left&#10;    return successor</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">36</td>
      <td rowspan="1">Tree 35 Two Sum Iv Input Is A Bst<br><br></b> <a href='https://leetcode.com/problems/two-sum-iv-input-is-a-bst/' target='_blank'>LeetCode 653</a></td>
      <td rowspan="1"><b>Example 1:</b> BST Iterator two pointer.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Use two BST iterators: one for normal inorder (next) and one for reverse inorder (before). Apply two-pointer approach like in a sorted array.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class BSTIterator:&#10;    def __init__(self, root, isReverse):&#10;        self.st = []&#10;        self.reverse = isReverse&#10;        self.pushAll(root)&#10;    def pushAll(self, node):&#10;        while node:&#10;            self.st.append(node)&#10;            if self.reverse: node = node.right&#10;            else: node = node.left&#10;    def next(self) -&gt; int:&#10;        tmpNode = self.st.pop()&#10;        if self.reverse: self.pushAll(tmpNode.left)&#10;        else: self.pushAll(tmpNode.right)&#10;        return tmpNode.val&#10;def findTarget(root: Optional[TreeNode], k: int) -&gt; bool:&#10;    if not root: return False&#10;    l = BSTIterator(root, False)&#10;    r = BSTIterator(root, True)&#10;    i = l.next()&#10;    j = r.next()&#10;    while i &lt; j:&#10;        if i + j == k: return True&#10;        elif i + j &lt; k: i = l.next()&#10;        else: j = r.next()&#10;    return False</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">37</td>
      <td rowspan="1">Tree 36 Recover Binary Search Tree<br><br></b> <a href='https://leetcode.com/problems/recover-binary-search-tree/' target='_blank'>LeetCode 99</a></td>
      <td rowspan="1"><b>Example 1:</b> Inorder traversal tracking anomalies.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Inorder traversal of BST gives sorted array. If two are swapped, there will be 1 or 2 anomalies where `prev->val > curr->val`. First anomaly: `first = prev`, `middle = curr`. Second anomaly: `last = curr`. Swap `first` and `last` (or `first` and `middle` if adjacent).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def recoverTree(root: Optional[TreeNode]) -&gt; None:&#10;    first = middle = last = prev = None&#10;    def inorder(node):&#10;        nonlocal first, middle, last, prev&#10;        if not node: return&#10;        inorder(node.left)&#10;        if prev and node.val &lt; prev.val:&#10;            if not first:&#10;                first = prev&#10;                middle = node&#10;            else:&#10;                last = node&#10;        prev = node&#10;        inorder(node.right)&#10;    inorder(root)&#10;    if first and last:&#10;        first.val, last.val = last.val, first.val&#10;    elif first and middle:&#10;        first.val, middle.val = middle.val, first.val</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">38</td>
      <td rowspan="1">Tree 37 Largest Bst In Binary Tree<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/largest-bst/1' target='_blank'>GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Bottom-up verification.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Return `[minNode, maxNode, maxSize]` from each subtree. For current node, if `left.max < node.val < right.min`, it's a BST. Return `[min(node.val, left.min), max(node.val, right.max), left.size + right.size + 1]`. Else, it's not a BST, return `[-inf, inf, max(left.size, right.size)]`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class NodeValue:&#10;    def __init__(self, minNode, maxNode, maxSize):&#10;        self.minNode = minNode&#10;        self.maxNode = maxNode&#10;        self.maxSize = maxSize&#10;def largestBSTSubtreeHelper(root):&#10;    if not root: return NodeValue(float(&#x27;inf&#x27;), float(&#x27;-inf&#x27;), 0)&#10;    left = largestBSTSubtreeHelper(root.left)&#10;    right = largestBSTSubtreeHelper(root.right)&#10;    if left.maxNode &lt; root.data &lt; right.minNode:&#10;        return NodeValue(min(root.data, left.minNode), max(root.data, right.maxNode), left.maxSize + right.maxSize + 1)&#10;    return NodeValue(float(&#x27;-inf&#x27;), float(&#x27;inf&#x27;), max(left.maxSize, right.maxSize))&#10;def largestBst(root):&#10;    return largestBSTSubtreeHelper(root).maxSize</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">39</td>
      <td rowspan="1">Tree 38 Binary Search Tree Iterator<br><br></b> <a href='https://leetcode.com/problems/binary-search-tree-iterator/' target='_blank'>LeetCode 173</a></td>
      <td rowspan="1"><b>Example 1:</b> Stack based partial inorder.</td>
      <td><b>Time:</b> O(1) average per call<br><b>Space:</b> O(H)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Maintain a stack of nodes. In constructor, push all left children of root. In `next()`, pop top, value is answer, if popped node has right child, push it and all its left children. `hasNext()` checks if stack is not empty.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class BSTIterator:&#10;    def __init__(self, root: Optional[TreeNode]):&#10;        self.st = []&#10;        self.pushAll(root)&#10;    def pushAll(self, node):&#10;        while node:&#10;            self.st.append(node)&#10;            node = node.left&#10;    def next(self) -&gt; int:&#10;        tmpNode = self.st.pop()&#10;        self.pushAll(tmpNode.right)&#10;        return tmpNode.val&#10;    def hasNext(self) -&gt; bool:&#10;        return len(self.st) &gt; 0</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">40</td>
      <td rowspan="1">Tree 39 Maximum Sum Bst In Binary Tree<br><br></b> <a href='https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/' target='_blank'>LeetCode 1373</a></td>
      <td rowspan="1"><b>Example 1:</b> Similar to largest BST.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Bottom-up traversal. Return `[isBST, minNode, maxNode, sum]`. Update global max sum when valid BST is found.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class Info:&#10;    def __init__(self, isBST, minNode, maxNode, sum_val):&#10;        self.isBST = isBST&#10;        self.minNode = minNode&#10;        self.maxNode = maxNode&#10;        self.sum = sum_val&#10;def maxSumBST(root: Optional[TreeNode]) -&gt; int:&#10;    maxSum = 0&#10;    def solve(node):&#10;        nonlocal maxSum&#10;        if not node: return Info(True, float(&#x27;inf&#x27;), float(&#x27;-inf&#x27;), 0)&#10;        left = solve(node.left)&#10;        right = solve(node.right)&#10;        if left.isBST and right.isBST and left.maxNode &lt; node.val &lt; right.minNode:&#10;            currSum = left.sum + right.sum + node.val&#10;            maxSum = max(maxSum, currSum)&#10;            return Info(True, min(node.val, left.minNode), max(node.val, right.maxNode), currSum)&#10;        return Info(False, float(&#x27;-inf&#x27;), float(&#x27;inf&#x27;), max(left.sum, right.sum))&#10;    solve(root)&#10;    return maxSum if maxSum &gt; 0 else 0</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">41</td>
      <td rowspan="1">Tree 40 Kth Largest Element In A Bst<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/kth-largest-element-in-bst/1' target='_blank'>GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Reverse inorder traversal.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Kth largest is Kth element in reverse inorder traversal (Right, Root, Left). Maintain a counter `k`. When visiting a node, decrement `k`. If `k == 0`, current node is the answer.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def kthLargest(root, k):&#10;    ans = -1&#10;    def reverseInorder(node):&#10;        nonlocal ans, k&#10;        if not node or k == 0: return&#10;        reverseInorder(node.right)&#10;        k -= 1&#10;        if k == 0:&#10;            ans = node.data&#10;            return&#10;        reverseInorder(node.left)&#10;    reverseInorder(root)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">42</td>
      <td rowspan="1">Tree 41 Predecessor And Successor In Bst<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/predecessor-and-successor/1' target='_blank'>GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Search down the tree.</td>
      <td><b>Time:</b> O(H)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> For Successor: search for key. If node->val <= key, go right. If node->val > key, update succ = node, go left. For Predecessor: If node->val >= key, go left. If node->val < key, update pred = node, go right.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findPreSuc(root, pre, suc, key):&#10;    curr = root&#10;    while curr:&#10;        if curr.key &gt; key:&#10;            suc[0] = curr&#10;            curr = curr.left&#10;        else:&#10;            curr = curr.right&#10;    curr = root&#10;    while curr:&#10;        if curr.key &lt; key:&#10;            pre[0] = curr&#10;            curr = curr.right&#10;        else:&#10;            curr = curr.left</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">43</td>
      <td rowspan="1">Tree 42 Construct Bst From Preorder Traversal<br><br></b> <a href='https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/' target='_blank'>LeetCode 1008</a></td>
      <td rowspan="1"><b>Example 1:</b> Upper bound tracking.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Use an upper bound value. `build(preorder, index, bound)`: If index >= len or preorder[index] > bound, return NULL. Create root with preorder[index]. `root->left = build(..., root->val)`. `root->right = build(..., bound)`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def bstFromPreorder(preorder: List[int]) -&gt; Optional[TreeNode]:&#10;    i = 0&#10;    def build(bound):&#10;        nonlocal i&#10;        if i == len(preorder) or preorder[i] &gt; bound: return None&#10;        root = TreeNode(preorder[i])&#10;        i += 1&#10;        root.left = build(root.val)&#10;        root.right = build(bound)&#10;        return root&#10;    return build(float(&#x27;inf&#x27;))</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">44</td>
      <td rowspan="1">Tree 43 All Nodes Distance K In Binary Tree<br><br></b> <a href='https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/' target='_blank'>LeetCode 863</a></td>
      <td rowspan="1"><b>Example 1:</b> Convert to graph or use parent pointers.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><code>#include <unordered_map>\n#include <queue>\n#include <unordered_set></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Perform BFS/DFS to map each node to its parent. Then, start a BFS from the target node, visiting left, right, and parent. Track visited nodes. After `k` levels in BFS, the current queue holds the answer.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def distanceK(root: TreeNode, target: TreeNode, k: int) -&gt; List[int]:&#10;    parent_track = {}&#10;    def markParents(node):&#10;        if node.left:&#10;            parent_track[node.left] = node&#10;            markParents(node.left)&#10;        if node.right:&#10;            parent_track[node.right] = node&#10;            markParents(node.right)&#10;    markParents(root)&#10;    queue = collections.deque([target])&#10;    visited = {target}&#10;    curr_level = 0&#10;    while queue:&#10;        if curr_level == k: break&#10;        size = len(queue)&#10;        for _ in range(size):&#10;            current = queue.popleft()&#10;            if current.left and current.left not in visited:&#10;                queue.append(current.left)&#10;                visited.add(current.left)&#10;            if current.right and current.right not in visited:&#10;                queue.append(current.right)&#10;                visited.add(current.right)&#10;            if current in parent_track and parent_track[current] not in visited:&#10;                queue.append(parent_track[current])&#10;                visited.add(parent_track[current])&#10;        curr_level += 1&#10;    return [node.val for node in queue]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">45</td>
      <td rowspan="1">Tree 44 Amount Of Time For Binary Tree To Be Infected<br><br></b> <a href='https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/' target='_blank'>LeetCode 2385</a></td>
      <td rowspan="1"><b>Example 1:</b> Parent pointers and BFS.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Same as 'Distance K' problem. Map parents. Find the start node. Perform BFS from start node. The time taken is the number of levels in BFS until all reachable nodes are visited.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def amountOfTime(root: Optional[TreeNode], start: int) -&gt; int:&#10;    parent_track = {}&#10;    target = None&#10;    queue = collections.deque([root])&#10;    while queue:&#10;        node = queue.popleft()&#10;        if node.val == start: target = node&#10;        if node.left:&#10;            parent_track[node.left] = node&#10;            queue.append(node.left)&#10;        if node.right:&#10;            parent_track[node.right] = node&#10;            queue.append(node.right)&#10;    queue = collections.deque([target])&#10;    visited = {target}&#10;    time = 0&#10;    while queue:&#10;        fl = False&#10;        for _ in range(len(queue)):&#10;            current = queue.popleft()&#10;            if current.left and current.left not in visited:&#10;                visited.add(current.left)&#10;                queue.append(current.left)&#10;                fl = True&#10;            if current.right and current.right not in visited:&#10;                visited.add(current.right)&#10;                queue.append(current.right)&#10;                fl = True&#10;            if current in parent_track and parent_track[current] not in visited:&#10;                visited.add(parent_track[current])&#10;                queue.append(parent_track[current])&#10;                fl = True&#10;        if fl: time += 1&#10;    return time</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">46</td>
      <td rowspan="1">Tree 45 Count Complete Tree Nodes<br><br></b> <a href='https://leetcode.com/problems/count-complete-tree-nodes/' target='_blank'>LeetCode 222</a></td>
      <td rowspan="1"><b>Example 1:</b> Recursive with Height check.</td>
      <td><b>Time:</b> O(log^2 N)<br><b>Space:</b> O(log N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Compute the left height (following left child) and right height (following right child) of the tree. If they are equal, the tree is a full binary tree, and the number of nodes is `2^h - 1`. If they are not equal, recursively count the nodes in the left and right subtrees and add 1 for the root.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def countNodes(root: Optional[TreeNode]) -&gt; int:&#10;    if not root: return 0&#10;    def get_height(node, is_left):&#10;        h = 0&#10;        while node:&#10;            h += 1&#10;            node = node.left if is_left else node.right&#10;        return h&#10;    lh = get_height(root, True)&#10;    rh = get_height(root, False)&#10;    if lh == rh:&#10;        return (1 &lt;&lt; lh) - 1&#10;    return 1 + countNodes(root.left) + countNodes(root.right)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">47</td>
      <td rowspan="1">Tree 46 Serialize And Deserialize Binary Tree<br><br></b> <a href='https://leetcode.com/problems/serialize-and-deserialize-binary-tree/' target='_blank'>LeetCode 297</a></td>
      <td rowspan="1"><b>Example 1:</b> Level-order traversal (BFS) with a queue.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><code>#include <queue>\n#include <sstream></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Serialize: Use a queue for BFS. For every node, if it's not null, append its value and push its children. If null, append 'null' or '#'. Deserialize: Split the string. Use a queue. The first element is the root. For each node popped from the queue, read the next two elements from the list to form its left and right children, push non-null children to the queue.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;class Codec:&#10;    def serialize(self, root):&#10;        if not root: return &quot;&quot;&#10;        q = collections.deque([root])&#10;        res = []&#10;        while q:&#10;            node = q.popleft()&#10;            if node:&#10;                res.append(str(node.val))&#10;                q.append(node.left)&#10;                q.append(node.right)&#10;            else:&#10;                res.append(&quot;#&quot;)&#10;        return &quot;,&quot;.join(res)&#10;    def deserialize(self, data):&#10;        if not data: return None&#10;        vals = data.split(&quot;,&quot;)&#10;        root = TreeNode(int(vals[0]))&#10;        q = collections.deque([root])&#10;        i = 1&#10;        while q:&#10;            node = q.popleft()&#10;            if vals[i] != &quot;#&quot;:&#10;                node.left = TreeNode(int(vals[i]))&#10;                q.append(node.left)&#10;            i += 1&#10;            if vals[i] != &quot;#&quot;:&#10;                node.right = TreeNode(int(vals[i]))&#10;                q.append(node.right)&#10;            i += 1&#10;        return root</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">48</td>
      <td rowspan="1">Tree 47 Morris Inorder Traversal<br><br></b> <a href='https://leetcode.com/problems/binary-tree-inorder-traversal/' target='_blank'>LeetCode 94</a></td>
      <td rowspan="1"><b>Example 1:</b> Threaded Binary Tree.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> If left child is null, process current node, move to right. Else, find predecessor (rightmost node in left subtree). If predecessor's right is null, make it point to current (thread), move to left. If predecessor's right is current, remove thread, process current, move to right.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def inorderTraversal(root: Optional[TreeNode]) -&gt; List[int]:&#10;    inorder = []&#10;    curr = root&#10;    while curr:&#10;        if not curr.left:&#10;            inorder.append(curr.val)&#10;            curr = curr.right&#10;        else:&#10;            prev = curr.left&#10;            while prev.right and prev.right != curr:&#10;                prev = prev.right&#10;            if not prev.right:&#10;                prev.right = curr&#10;                curr = curr.left&#10;            else:&#10;                prev.right = None&#10;                inorder.append(curr.val)&#10;                curr = curr.right&#10;    return inorder</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">49</td>
      <td rowspan="1">Tree 48 Morris Preorder Traversal<br><br></b> <a href='https://leetcode.com/problems/binary-tree-preorder-traversal/' target='_blank'>LeetCode 144</a></td>
      <td rowspan="1"><b>Example 1:</b> Threaded Binary Tree.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Similar to Morris Inorder. If left child is null, process current, move right. Else, find predecessor. If predecessor's right is null, process current, make thread, move left. If predecessor's right is current, remove thread, move right.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def preorderTraversal(root: Optional[TreeNode]) -&gt; List[int]:&#10;    preorder = []&#10;    curr = root&#10;    while curr:&#10;        if not curr.left:&#10;            preorder.append(curr.val)&#10;            curr = curr.right&#10;        else:&#10;            prev = curr.left&#10;            while prev.right and prev.right != curr:&#10;                prev = prev.right&#10;            if not prev.right:&#10;                prev.right = curr&#10;                preorder.append(curr.val)&#10;                curr = curr.left&#10;            else:&#10;                prev.right = None&#10;                curr = curr.right&#10;    return preorder</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">50</td>
      <td rowspan="1">Tree 49 Flatten Binary Tree To Linked List<br><br></b> <a href='https://leetcode.com/problems/flatten-binary-tree-to-linked-list/' target='_blank'>LeetCode 114</a></td>
      <td rowspan="1"><b>Example 1:</b> Reverse Postorder / Stack / Morris.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Morris-like approach (O(1) space): If node has a left child, find the rightmost node in the left subtree. Connect it to the current node's right child. Move the left child to the right child, and set the left child to null. Move to the next right node.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def flatten(root: Optional[TreeNode]) -&gt; None:&#10;    curr = root&#10;    while curr:&#10;        if curr.left:&#10;            prev = curr.left&#10;            while prev.right:&#10;                prev = prev.right&#10;            prev.right = curr.right&#10;            curr.right = curr.left&#10;            curr.left = None&#10;        curr = curr.right</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">51</td>
      <td rowspan="1">Tree 50 Search In A Binary Search Tree<br><br></b> <a href='https://leetcode.com/problems/search-in-a-binary-search-tree/' target='_blank'>LeetCode 700</a></td>
      <td rowspan="1"><b>Example 1:</b> Iterative or Recursive.</td>
      <td><b>Time:</b> O(H)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Start at root. If root is null or its value is `val`, return root. If `val < root.val`, go left. Else go right.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def searchBST(root: Optional[TreeNode], val: int) -&gt; Optional[TreeNode]:&#10;    while root and root.val != val:&#10;        root = root.left if val &lt; root.val else root.right&#10;    return root</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">52</td>
      <td rowspan="1">Tree 51 Find Minimum In Binary Search Tree<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/minimum-element-in-bst/1' target='_blank'>GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Leftmost node.</td>
      <td><b>Time:</b> O(H)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Traverse the left children until a node with no left child is reached. That node contains the minimum value.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minValue(root: Optional[TreeNode]) -&gt; int:&#10;    if not root: return -1&#10;    while root.left:&#10;        root = root.left&#10;    return root.val</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">53</td>
      <td rowspan="1">Tree 52 Insert Into A Binary Search Tree<br><br></b> <a href='https://leetcode.com/problems/insert-into-a-binary-search-tree/' target='_blank'>LeetCode 701</a></td>
      <td rowspan="1"><b>Example 1:</b> Iterative search and insert.</td>
      <td><b>Time:</b> O(H)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Traverse the tree. If `val < current.val`, go left. If left is null, insert here. If `val > current.val`, go right. If right is null, insert here.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def insertIntoBST(root: Optional[TreeNode], val: int) -&gt; Optional[TreeNode]:&#10;    if not root: return TreeNode(val)&#10;    curr = root&#10;    while True:&#10;        if curr.val &lt;= val:&#10;            if curr.right: curr = curr.right&#10;            else:&#10;                curr.right = TreeNode(val)&#10;                break&#10;        else:&#10;            if curr.left: curr = curr.left&#10;            else:&#10;                curr.left = TreeNode(val)&#10;                break&#10;    return root</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">54</td>
      <td rowspan="1">Tree 53 Delete Node In A Bst<br><br></b> <a href='https://leetcode.com/problems/delete-node-in-a-bst/' target='_blank'>LeetCode 450</a></td>
      <td rowspan="1"><b>Example 1:</b> Find and Replace.</td>
      <td><b>Time:</b> O(H)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Search for the node. If found, there are 3 cases: Node is a leaf (just remove), Node has 1 child (replace with child), Node has 2 children (find inorder successor, i.e., min in right subtree, copy value, delete successor from right subtree). Alternatively, connect the left subtree to the leftmost node of the right subtree.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def deleteNode(root: Optional[TreeNode], key: int) -&gt; Optional[TreeNode]:&#10;    if not root: return None&#10;    if root.val == key:&#10;        if not root.left: return root.right&#10;        if not root.right: return root.left&#10;        rightChild = root.right&#10;        lastRight = root.left&#10;        while lastRight.right: lastRight = lastRight.right&#10;        lastRight.right = rightChild&#10;        return root.left&#10;    curr = root&#10;    while curr:&#10;        if curr.val &gt; key:&#10;            if curr.left and curr.left.val == key:&#10;                if not curr.left.left: curr.left = curr.left.right&#10;                elif not curr.left.right: curr.left = curr.left.left&#10;                else:&#10;                    rc = curr.left.right&#10;                    lr = curr.left.left&#10;                    while lr.right: lr = lr.right&#10;                    lr.right = rc&#10;                    curr.left = curr.left.left&#10;                break&#10;            else:&#10;                curr = curr.left&#10;        else:&#10;            if curr.right and curr.right.val == key:&#10;                if not curr.right.left: curr.right = curr.right.right&#10;                elif not curr.right.right: curr.right = curr.right.left&#10;                else:&#10;                    rc = curr.right.right&#10;                    lr = curr.right.left&#10;                    while lr.right: lr = lr.right&#10;                    lr.right = rc&#10;                    curr.right = curr.right.left&#10;                break&#10;            else:&#10;                curr = curr.right&#10;    return root</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">55</td>
      <td rowspan="1">Tree 54 Kth Smallest Element In A Bst<br><br></b> <a href='https://leetcode.com/problems/kth-smallest-element-in-a-bst/' target='_blank'>LeetCode 230</a></td>
      <td rowspan="1"><b>Example 1:</b> Inorder traversal.</td>
      <td><b>Time:</b> O(K) or O(N)<br><b>Space:</b> O(H) or O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Perform an inorder traversal (Recursive or Iterative/Morris) and keep track of count. When count reaches `k`, return the node's value.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def kthSmallest(root: Optional[TreeNode], k: int) -&gt; int:&#10;    count, ans = 0, -1&#10;    curr = root&#10;    while curr:&#10;        if not curr.left:&#10;            count += 1&#10;            if count == k: ans = curr.val&#10;            curr = curr.right&#10;        else:&#10;            prev = curr.left&#10;            while prev.right and prev.right != curr: prev = prev.right&#10;            if not prev.right:&#10;                prev.right = curr&#10;                curr = curr.left&#10;            else:&#10;                prev.right = None&#10;                count += 1&#10;                if count == k: ans = curr.val&#10;                curr = curr.right&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">56</td>
      <td rowspan="1">Tree 55 Validate Binary Search Tree<br><br></b> <a href='https://leetcode.com/problems/validate-binary-search-tree/' target='_blank'>LeetCode 98</a></td>
      <td rowspan="1"><b>Example 1:</b> Recursive with Range.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Pass a valid range `(min_val, max_val)` for each node. For the root, it's `(-infinity, infinity)`. If node value is outside range, return false. Recursively check left subtree with range `(min_val, node.val)` and right subtree with `(node.val, max_val)`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isValidBST(root: Optional[TreeNode]) -&gt; bool:&#10;    def validate(node, low=-float(&#x27;inf&#x27;), high=float(&#x27;inf&#x27;)):&#10;        if not node: return True&#10;        if node.val &lt;= low or node.val &gt;= high: return False&#10;        return validate(node.left, low, node.val) and validate(node.right, node.val, high)&#10;    return validate(root)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">57</td>
      <td rowspan="1">Tree 56 Lowest Common Ancestor Of A Binary Search Tree<br><br></b> <a href='https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/' target='_blank'>LeetCode 235</a></td>
      <td rowspan="1"><b>Example 1:</b> Iterative Traversal based on BST property.</td>
      <td><b>Time:</b> O(H)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Start at root. If both `p` and `q` are less than root, move left. If both are greater, move right. Otherwise, the current node is the LCA.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def lowestCommonAncestor(root: &#x27;TreeNode&#x27;, p: &#x27;TreeNode&#x27;, q: &#x27;TreeNode&#x27;) -&gt; &#x27;TreeNode&#x27;:&#10;    while root:&#10;        if p.val &lt; root.val and q.val &lt; root.val:&#10;            root = root.left&#10;        elif p.val &gt; root.val and q.val &gt; root.val:&#10;            root = root.right&#10;        else:&#10;            return root&#10;    return None</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">58</td>
      <td rowspan="1">Tree 57 Construct Binary Search Tree From Preorder Traversal<br><br></b> <a href='https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/' target='_blank'>LeetCode 1008</a></td>
      <td rowspan="1"><b>Example 1:</b> Recursive with upper bound.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Keep track of an index for the `preorder` array and a maximum valid bound. To build the left subtree, the upper bound is the current node's value. To build the right subtree, the bound remains the parent's bound. If the current value is greater than the bound, return NULL.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def bstFromPreorder(preorder: List[int]) -&gt; Optional[TreeNode]:&#10;    i = 0&#10;    def build(bound):&#10;        nonlocal i&#10;        if i == len(preorder) or preorder[i] &gt; bound:&#10;            return None&#10;        root = TreeNode(preorder[i])&#10;        i += 1&#10;        root.left = build(root.val)&#10;        root.right = build(bound)&#10;        return root&#10;    return build(float(&#x27;inf&#x27;))</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">59</td>
      <td rowspan="1">Tree 58 Inorder Successor In Bst<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/populate-inorder-successor-for-all-nodes/1' target='_blank'>GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Iterative search.</td>
      <td><b>Time:</b> O(H)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Start from root. If `p.val >= root.val`, the successor must be in the right subtree (`root = root.right`). If `p.val < root.val`, the current root could be the successor, so record it and search the left subtree for a closer successor (`successor = root; root = root.left`).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def inorderSuccessor(root: &#x27;TreeNode&#x27;, p: &#x27;TreeNode&#x27;) -&gt; &#x27;TreeNode&#x27;:&#10;    successor = None&#10;    while root:&#10;        if p.val &gt;= root.val:&#10;            root = root.right&#10;        else:&#10;            successor = root&#10;            root = root.left&#10;    return successor</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">60</td>
      <td rowspan="1">Tree 59 Binary Search Tree Iterator<br><br></b> <a href='https://leetcode.com/problems/binary-search-tree-iterator/' target='_blank'>LeetCode 173</a></td>
      <td rowspan="1"><b>Example 1:</b> Stack based partial traversal.</td>
      <td><b>Time:</b> O(1) amortized for next/hasNext<br><b>Space:</b> O(H)</td>
      <td><code>#include <stack></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Use a stack to simulate inorder traversal. In constructor, push all left children of root to stack. For `next()`, pop the top node, push all left children of its right child, and return the popped node's value. `hasNext()` checks if stack is not empty.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class BSTIterator:&#10;    def __init__(self, root: Optional[TreeNode]):&#10;        self.stack = []&#10;        self.pushAll(root)&#10;    def pushAll(self, node):&#10;        while node:&#10;            self.stack.append(node)&#10;            node = node.left&#10;    def next(self) -&gt; int:&#10;        tmpNode = self.stack.pop()&#10;        self.pushAll(tmpNode.right)&#10;        return tmpNode.val&#10;    def hasNext(self) -&gt; bool:&#10;        return len(self.stack) &gt; 0</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">61</td>
      <td rowspan="1">Tree 60 Two Sum Iv Input Is A Bst<br><br></b> <a href='https://leetcode.com/problems/two-sum-iv-input-is-a-bst/' target='_blank'>LeetCode 653</a></td>
      <td rowspan="1"><b>Example 1:</b> Two Pointers using dual BST Iterators.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td><code>#include <stack></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Implement two BST iterators: one for normal inorder (next) and one for reverse inorder (before). Set `i = next()` and `j = before()`. While `i < j`, if `i + j == k` return true, if `i + j < k` increment `i`, else decrement `j`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class BSTIterator:&#10;    def __init__(self, root, isReverse):&#10;        self.stack = []&#10;        self.reverse = isReverse&#10;        self.pushAll(root)&#10;    def pushAll(self, node):&#10;        while node:&#10;            self.stack.append(node)&#10;            node = node.right if self.reverse else node.left&#10;    def next(self):&#10;        tmp = self.stack.pop()&#10;        self.pushAll(tmp.left if self.reverse else tmp.right)&#10;        return tmp.val&#10;def findTarget(root: Optional[TreeNode], k: int) -&gt; bool:&#10;    if not root: return False&#10;    l = BSTIterator(root, False)&#10;    r = BSTIterator(root, True)&#10;    i = l.next()&#10;    j = r.next()&#10;    while i &lt; j:&#10;        if i + j == k: return True&#10;        elif i + j &lt; k: i = l.next()&#10;        else: j = r.next()&#10;    return False</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">62</td>
      <td rowspan="1">Tree 61 Recover Binary Search Tree<br><br></b> <a href='https://leetcode.com/problems/recover-binary-search-tree/' target='_blank'>LeetCode 99</a></td>
      <td rowspan="1"><b>Example 1:</b> Inorder Traversal looking for violations.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H) or O(1) with Morris</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Maintain `prev`, `first`, `middle`, and `last` pointers during inorder traversal. If `prev.val > root.val`, a violation occurred. The first violation points to `first=prev` and `middle=root`. A second violation (if any) points to `last=root`. Finally, swap values of `first` and `last` (or `first` and `middle` if adjacent).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def recoverTree(root: Optional[TreeNode]) -&gt; None:&#10;    first = middle = last = prev = None&#10;    def inorder(node):&#10;        nonlocal first, middle, last, prev&#10;        if not node: return&#10;        inorder(node.left)&#10;        if prev and node.val &lt; prev.val:&#10;            if not first:&#10;                first, middle = prev, node&#10;            else:&#10;                last = node&#10;        prev = node&#10;        inorder(node.right)&#10;    inorder(root)&#10;    if first and last:&#10;        first.val, last.val = last.val, first.val&#10;    elif first and middle:&#10;        first.val, middle.val = middle.val, first.val</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">63</td>
      <td rowspan="1">Tree 62 Largest Bst<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/largest-bst/1' target='_blank'>GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Postorder Traversal returning a custom tuple.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Return a struct `[minNode, maxNode, maxSize]`. For any node, if `left.maxNode < node.val < right.minNode`, it's a BST. Then `size = left.maxSize + right.maxSize + 1`. Return `[min(left.min, node.val), max(right.max, node.val), size]`. If not a BST, return `[-inf, inf, max(left.size, right.size)]`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def largestBst(root):&#10;    def helper(node):&#10;        if not node: return float(&#x27;inf&#x27;), float(&#x27;-inf&#x27;), 0&#10;        l_min, l_max, l_size = helper(node.left)&#10;        r_min, r_max, r_size = helper(node.right)&#10;        if l_max &lt; node.val &lt; r_min:&#10;            return min(node.val, l_min), max(node.val, r_max), l_size + r_size + 1&#10;        return float(&#x27;-inf&#x27;), float(&#x27;inf&#x27;), max(l_size, r_size)&#10;    return helper(root)[2]</code></pre></details></td>
    </tr>
  </tbody>
</table>
