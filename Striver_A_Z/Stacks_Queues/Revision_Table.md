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
      <td>Sq 05 Lru Cache<br><br></b> <a href='https://leetcode.com/problems/lru-cache/' target='_blank'>LeetCode 146</a></td>
      <td><b>Example 1:</b> Design question.</td>
      <td><b>Time:</b> O(1) per operation<br><b>Space:</b> O(Capacity)</td>
      <td><code>#include <unordered_map></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Use a Hash Map and a Doubly Linked List. The Map stores `key -> Node*`. The DLL maintains recency (head is most recent, tail is least recent). Update DLL pointers on access/insert.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class Node:&#10;    def __init__(self, key, val):&#10;        self.key, self.val = key, val&#10;        self.prev = self.next = None&#10;class LRUCache:&#10;    def __init__(self, capacity: int):&#10;        self.cap = capacity&#10;        self.head, self.tail = Node(-1, -1), Node(-1, -1)&#10;        self.head.next, self.tail.prev = self.tail, self.head&#10;        self.m = {}&#10;    def addNode(self, newnode):&#10;        temp = self.head.next&#10;        newnode.next = temp; newnode.prev = self.head&#10;        self.head.next = newnode; temp.prev = newnode&#10;    def deleteNode(self, delnode):&#10;        delprev, delnext = delnode.prev, delnode.next&#10;        delprev.next = delnext; delnext.prev = delprev&#10;    def get(self, key: int) -&gt; int:&#10;        if key in self.m:&#10;            resnode = self.m[key]&#10;            res = resnode.val&#10;            del self.m[key]&#10;            self.deleteNode(resnode)&#10;            self.addNode(resnode)&#10;            self.m[key] = self.head.next&#10;            return res&#10;        return -1&#10;    def put(self, key: int, value: int) -&gt; None:&#10;        if key in self.m:&#10;            existing = self.m[key]&#10;            del self.m[key]; self.deleteNode(existing)&#10;        if len(self.m) == self.cap:&#10;            del self.m[self.tail.prev.key]; self.deleteNode(self.tail.prev)&#10;        self.addNode(Node(key, value))&#10;        self.m[key] = self.head.next</code></pre></details></td>
    </tr>
    <tr>
      <td>6</td>
      <td>Sq 06 Largest Rectangle In Histogram<br><br></b> <a href='https://leetcode.com/problems/largest-rectangle-in-histogram/' target='_blank'>LeetCode 84</a></td>
      <td><b>Example 1:</b> Input: heights = [2,1,5,6,2,3], Output: 10</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><code>#include <stack></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Monotonic Stack. Find the next smaller element on the left and right for each bar. Area for bar `i` is `heights[i] * (right[i] - left[i] + 1)`. Alternatively, do it in a single pass stack loop.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def largestRectangleArea(heights: List[int]) -&gt; int:&#10;    n, maxArea = len(heights), 0&#10;    st = []&#10;    for i in range(n + 1):&#10;        while st and (i == n or heights[st[-1]] &gt;= heights[i]):&#10;            height = heights[st.pop()]&#10;            width = i if not st else i - st[-1] - 1&#10;            maxArea = max(maxArea, width * height)&#10;        st.append(i)&#10;    return maxArea</code></pre></details></td>
    </tr>
  </tbody>
</table>
