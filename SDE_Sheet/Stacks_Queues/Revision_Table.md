# Stacks Queues Revision Table

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
      <td>1</td>
      <td>Sq 02 Valid Parentheses<br><br></b> <a href='https://leetcode.com/problems/valid-parentheses/' target='_blank'>LeetCode 20</a></td>
      <td><b>Example 1:</b> Input: s = "()[]{}", Output: true</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><code>std::stack</code></td>
      <td><b>Empty Stack / Unmatched:</b> If a closed bracket arrives while the stack is empty, it's invalid. If stack is NOT empty at the end, it's invalid.</td>
      <td><b>Explanation:</b> Use a Stack. Push open brackets. If a closed bracket is found, verify it matches the top of the stack and pop.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isValid(s: str) -&gt; bool:&#10;    st = []&#10;    mapping = {&#x27;)&#x27;: &#x27;(&#x27;, &#x27;}&#x27;: &#x27;{&#x27;, &#x27;]&#x27;: &#x27;[&#x27;}&#10;    for char in s:&#10;        if char in mapping:&#10;            top = st.pop() if st else &#x27;#&#x27;&#10;            if mapping[char] != top: return False&#10;        else:&#10;            st.append(char)&#10;    return not st</code></pre></details></td>
    </tr>
    <tr>
      <td>2</td>
      <td>Sq 03 Next Greater Element I<br><br></b> <a href='https://leetcode.com/problems/next-greater-element-i/' target='_blank'>LeetCode 496</a></td>
      <td><b>Example 1:</b> Input: nums1 = [4,1,2], nums2 = [1,3,4,2], Output: [-1,3,-1]</td>
      <td><b>Time:</b> O(N + M)<br><b>Space:</b> O(N)</td>
      <td><code>std::stack</code>, <code>std::unordered_map</code></td>
      <td><b>No greater element:</b> If stack becomes empty after popping smaller elements, there is no NGE, store `-1`.</td>
      <td><b>Explanation:</b> Monotonic Stack traversing `nums2` from right to left. Maintain stack of elements in decreasing order.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def nextGreaterElement(nums1: list[int], nums2: list[int]) -&gt; list[int]:&#10;    mpp = {}&#10;    st = []&#10;    for num in reversed(nums2):&#10;        while st and st[-1] &lt;= num: st.pop()&#10;        mpp[num] = st[-1] if st else -1&#10;        st.append(num)&#10;    return [mpp[num] for num in nums1]</code></pre></details></td>
    </tr>
    <tr>
      <td>3</td>
      <td>Sq 03 Min Stack<br><br></b> <a href='https://leetcode.com/problems/min-stack/' target='_blank'>LeetCode 155</a></td>
      <td><b>Example 1:</b> MinStack minStack = new MinStack(); minStack.push(-2); minStack.push(0); minStack.push(-3); minStack.getMin(); // return -3</td>
      <td><b>Time:</b> O(1) per operation<br><b>Space:</b> O(N)</td>
      <td><code>#include <stack></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Store pairs of `(value, current_minimum)` in the stack. Alternatively, use math to encode the difference between the value and the minimum to achieve O(1) space auxiliary, but a stack of pairs is standard.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class MinStack:&#10;    def __init__(self):&#10;        self.st = []&#10;    def push(self, val: int) -&gt; None:&#10;        if not self.st:&#10;            self.st.append((val, val))&#10;        else:&#10;            self.st.append((val, min(val, self.st[-1][1])))&#10;    def pop(self) -&gt; None:&#10;        self.st.pop()&#10;    def top(self) -&gt; int:&#10;        return self.st[-1][0]&#10;    def getMin(self) -&gt; int:&#10;        return self.st[-1][1]</code></pre></details></td>
    </tr>
    <tr>
      <td>4</td>
      <td>Sq 04 Sliding Window Maximum<br><br></b> <a href='https://leetcode.com/problems/sliding-window-maximum/' target='_blank'>LeetCode 239</a></td>
      <td><b>Example 1:</b> Input: nums = [1,3,-1,-3,5,3,6,7], k = 3, Output: [3,3,5,5,6,7]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(K)</td>
      <td><code>#include <deque></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Monotonic Deque. Store indices in a double-ended queue. Maintain elements in strictly decreasing order. Pop front if it's out of window bounds. Add nums[dq.front()] to answer once window reaches size k.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">from collections import deque&#10;def maxSlidingWindow(nums: List[int], k: int) -&gt; List[int]:&#10;    dq = deque()&#10;    ans = []&#10;    for i in range(len(nums)):&#10;        if dq and dq[0] == i - k: dq.popleft()&#10;        while dq and nums[dq[-1]] &lt;= nums[i]: dq.pop()&#10;        dq.append(i)&#10;        if i &gt;= k - 1: ans.append(nums[dq[0]])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>5</td>
      <td>Sq 19 Lru Cache<br><br></b> <a href='https://leetcode.com/problems/lru-cache/' target='_blank'>LeetCode 146</a></td>
      <td><b>Example 1:</b> Doubly Linked List + Hash Map.</td>
      <td><b>Time:</b> O(1) for get and put<br><b>Space:</b> O(Capacity)</td>
      <td>Hash Map, Doubly Linked List</td>
      <td>-</td>
      <td><b>Explanation:</b> Use a hash map to store keys to Node pointers. Use a doubly linked list to track the usage history. The head of the DLL represents the most recently used, and the tail represents the least recently used. On `get` or `put`, move the accessed node to the head. If capacity is exceeded, remove the node before the tail.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class Node:&#10;    def __init__(self, key, val):&#10;        self.key, self.val = key, val&#10;        self.prev = self.next = None&#10;class LRUCache:&#10;    def __init__(self, capacity: int):&#10;        self.cap = capacity&#10;        self.m = {}&#10;        self.head, self.tail = Node(-1, -1), Node(-1, -1)&#10;        self.head.next, self.tail.prev = self.tail, self.head&#10;    def addNode(self, newnode):&#10;        temp = self.head.next&#10;        newnode.next, newnode.prev = temp, self.head&#10;        self.head.next, temp.prev = newnode, newnode&#10;    def deleteNode(self, delnode):&#10;        delprev, delnext = delnode.prev, delnode.next&#10;        delprev.next, delnext.prev = delnext, delprev&#10;    def get(self, key: int) -&gt; int:&#10;        if key in self.m:&#10;            resnode = self.m[key]&#10;            ans = resnode.val&#10;            del self.m[key]&#10;            self.deleteNode(resnode)&#10;            self.addNode(resnode)&#10;            self.m[key] = self.head.next&#10;            return ans&#10;        return -1&#10;    def put(self, key: int, value: int) -&gt; None:&#10;        if key in self.m:&#10;            existingnode = self.m[key]&#10;            del self.m[key]&#10;            self.deleteNode(existingnode)&#10;        if len(self.m) == self.cap:&#10;            del self.m[self.tail.prev.key]&#10;            self.deleteNode(self.tail.prev)&#10;        self.addNode(Node(key, value))&#10;        self.m[key] = self.head.next</code></pre></details></td>
    </tr>
    <tr>
      <td>6</td>
      <td>Sq 20 Lfu Cache<br><br></b> <a href='https://leetcode.com/problems/lfu-cache/' target='_blank'>LeetCode 460</a></td>
      <td><b>Example 1:</b> Hash Maps + Doubly Linked Lists.</td>
      <td><b>Time:</b> O(1) for get and put<br><b>Space:</b> O(Capacity)</td>
      <td>Hash Maps, Doubly Linked List</td>
      <td>-</td>
      <td><b>Explanation:</b> Maintain a `minFreq` variable. Use one hash map to map `key` to its Node. Use another hash map to map `frequency` to a Doubly Linked List of Nodes with that frequency. When accessing an element, increase its frequency and move it to the corresponding DLL. If capacity is reached, remove the least recently used element from the DLL at `minFreq`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class Node:&#10;    def __init__(self, key, value):&#10;        self.key, self.value, self.cnt = key, value, 1&#10;        self.prev = self.next = None&#10;class DLinkedList:&#10;    def __init__(self):&#10;        self.head, self.tail = Node(0, 0), Node(0, 0)&#10;        self.head.next, self.tail.prev = self.tail, self.head&#10;        self.size = 0&#10;    def add_node(self, node):&#10;        node.next, node.prev = self.head.next, self.head&#10;        self.head.next.prev, self.head.next = node, node&#10;        self.size += 1&#10;    def remove_node(self, node):&#10;        node.prev.next, node.next.prev = node.next, node.prev&#10;        self.size -= 1&#10;class LFUCache:&#10;    def __init__(self, capacity: int):&#10;        self.cap, self.size, self.min_freq = capacity, 0, 0&#10;        self.node_map, self.freq_map = {}, {}&#10;    def update(self, node):&#10;        freq = node.cnt&#10;        self.freq_map[freq].remove_node(node)&#10;        if self.min_freq == freq and not self.freq_map[freq].size:&#10;            self.min_freq += 1&#10;        node.cnt += 1&#10;        if node.cnt not in self.freq_map:&#10;            self.freq_map[node.cnt] = DLinkedList()&#10;        self.freq_map[node.cnt].add_node(node)&#10;    def get(self, key: int) -&gt; int:&#10;        if key not in self.node_map: return -1&#10;        node = self.node_map[key]&#10;        self.update(node)&#10;        return node.value&#10;    def put(self, key: int, value: int) -&gt; None:&#10;        if self.cap == 0: return&#10;        if key in self.node_map:&#10;            node = self.node_map[key]&#10;            node.value = value&#10;            self.update(node)&#10;        else:&#10;            if self.size == self.cap:&#10;                node_to_remove = self.freq_map[self.min_freq].tail.prev&#10;                self.freq_map[self.min_freq].remove_node(node_to_remove)&#10;                del self.node_map[node_to_remove.key]&#10;                self.size -= 1&#10;            new_node = Node(key, value)&#10;            self.node_map[key] = new_node&#10;            if 1 not in self.freq_map: self.freq_map[1] = DLinkedList()&#10;            self.freq_map[1].add_node(new_node)&#10;            self.min_freq = 1&#10;            self.size += 1</code></pre></details></td>
    </tr>
    <tr>
      <td>7</td>
      <td>Sq 21 Largest Rectangle In Histogram<br><br></b> <a href='https://leetcode.com/problems/largest-rectangle-in-histogram/' target='_blank'>LeetCode 84</a></td>
      <td><b>Example 1:</b> Monotonic Stack.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Stack</td>
      <td>-</td>
      <td><b>Explanation:</b> Use a stack to keep track of the indices of the bars in increasing order of height. If the current bar is shorter than the top of the stack, pop bars and calculate the area for each popped bar as the shortest bar. The width is `i - stack.top() - 1`. If stack is empty, width is `i`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def largestRectangleArea(heights):&#10;    s, maxArea = [], 0&#10;    for i, h in enumerate(heights + [0]):&#10;        while s and heights[s[-1]] &gt;= h:&#10;            height = heights[s.pop()]&#10;            width = i if not s else i - s[-1] - 1&#10;            maxArea = max(maxArea, height * width)&#10;        s.append(i)&#10;    return maxArea</code></pre></details></td>
    </tr>
    <tr>
      <td>8</td>
      <td>Sq 23 Online Stock Span<br><br></b> <a href='https://leetcode.com/problems/online-stock-span/' target='_blank'>LeetCode 901</a></td>
      <td><b>Example 1:</b> Monotonic Stack.</td>
      <td><b>Time:</b> O(1) amortized<br><b>Space:</b> O(N)</td>
      <td>Stack</td>
      <td>-</td>
      <td><b>Explanation:</b> Use a stack of pairs `(price, span)`. When a new price comes in, initialize its span to 1. Pop elements from the stack while the top element's price is `<= price`, adding their spans to the current span. Push `(price, span)` to the stack.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class StockSpanner:&#10;    def __init__(self):&#10;        self.s = []&#10;    def next(self, price: int) -&gt; int:&#10;        span = 1&#10;        while self.s and self.s[-1][0] &lt;= price:&#10;            span += self.s.pop()[1]&#10;        self.s.append((price, span))&#10;        return span</code></pre></details></td>
    </tr>
    <tr>
      <td>9</td>
      <td>Sq 25 Rotten Oranges<br><br></b> <a href='https://leetcode.com/problems/rotting-oranges/' target='_blank'>LeetCode 994</a></td>
      <td><b>Example 1:</b> BFS.</td>
      <td><b>Time:</b> O(rows * cols)<br><b>Space:</b> O(rows * cols)</td>
      <td>Queue</td>
      <td>Grid without fresh oranges</td>
      <td><b>Explanation:</b> Use a Queue for BFS. Find all initially rotten oranges and push them into the queue with time 0. Count total fresh oranges. Pop an orange, rot its adjacent fresh oranges, push them to the queue with `time + 1`, and decrement fresh count. Return the max time if fresh count is 0, else -1.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">from collections import deque&#10;def orangesRotting(grid):&#10;    rows, cols = len(grid), len(grid[0])&#10;    q = deque()&#10;    fresh_cnt = 0&#10;    for i in range(rows):&#10;        for j in range(cols):&#10;            if grid[i][j] == 2: q.append((i, j, 0))&#10;            elif grid[i][j] == 1: fresh_cnt += 1&#10;    tm, cnt = 0, 0&#10;    while q:&#10;        r, c, t = q.popleft()&#10;        tm = max(tm, t)&#10;        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:&#10;            nr, nc = r + dr, c + dc&#10;            if 0 &lt;= nr &lt; rows and 0 &lt;= nc &lt; cols and grid[nr][nc] == 1:&#10;                grid[nr][nc] = 2&#10;                q.append((nr, nc, t + 1))&#10;                cnt += 1&#10;    return tm if cnt == fresh_cnt else -1</code></pre></details></td>
    </tr>
    <tr>
      <td>10</td>
      <td>Sq 26 Sliding Window Maximum<br><br></b> <a href='https://leetcode.com/problems/sliding-window-maximum/' target='_blank'>LeetCode 239</a></td>
      <td><b>Example 1:</b> Deque.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(K)</td>
      <td>Deque</td>
      <td>-</td>
      <td><b>Explanation:</b> Use a double-ended queue (deque) to store indices. Maintain indices in the deque such that the elements they correspond to are in decreasing order. The front of the deque will always be the maximum for the current window. Remove indices from the front if they are out of the window (`i - k`).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">from collections import deque&#10;def maxSlidingWindow(nums, k):&#10;    dq = deque()&#10;    ans = []&#10;    for i in range(len(nums)):&#10;        if dq and dq[0] == i - k: dq.popleft()&#10;        while dq and nums[dq[-1]] &lt; nums[i]: dq.pop()&#10;        dq.append(i)&#10;        if i &gt;= k - 1: ans.append(nums[dq[0]])&#10;    return ans</code></pre></details></td>
    </tr>
  </tbody>
</table>
