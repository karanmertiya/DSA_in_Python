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
      <td rowspan="1">1</td>
      <td rowspan="1">Sq 02 Valid Parentheses<br><br></b> <a href='https://leetcode.com/problems/valid-parentheses/' target='_blank'>LeetCode 20</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: s = "()[]{}", Output: true</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><code>std::stack</code></td>
      <td><b>Empty Stack / Unmatched:</b> If a closed bracket arrives while the stack is empty, it's invalid. If stack is NOT empty at the end, it's invalid.</td>
      <td><b>Explanation:</b> Use a Stack. Push open brackets. If a closed bracket is found, verify it matches the top of the stack and pop.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isValid(s: str) -&gt; bool:&#10;    st = []&#10;    mapping = {&#x27;)&#x27;: &#x27;(&#x27;, &#x27;}&#x27;: &#x27;{&#x27;, &#x27;]&#x27;: &#x27;[&#x27;}&#10;    for char in s:&#10;        if char in mapping:&#10;            top = st.pop() if st else &#x27;#&#x27;&#10;            if mapping[char] != top: return False&#10;        else:&#10;            st.append(char)&#10;    return not st</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">2</td>
      <td rowspan="1">Sq 03 Next Greater Element I<br><br></b> <a href='https://leetcode.com/problems/next-greater-element-i/' target='_blank'>LeetCode 496</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: nums1 = [4,1,2], nums2 = [1,3,4,2], Output: [-1,3,-1]</td>
      <td><b>Time:</b> O(N + M)<br><b>Space:</b> O(N)</td>
      <td><code>std::stack</code>, <code>std::unordered_map</code></td>
      <td><b>No greater element:</b> If stack becomes empty after popping smaller elements, there is no NGE, store `-1`.</td>
      <td><b>Explanation:</b> Monotonic Stack traversing `nums2` from right to left. Maintain stack of elements in decreasing order.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def nextGreaterElement(nums1: list[int], nums2: list[int]) -&gt; list[int]:&#10;    mpp = {}&#10;    st = []&#10;    for num in reversed(nums2):&#10;        while st and st[-1] &lt;= num: st.pop()&#10;        mpp[num] = st[-1] if st else -1&#10;        st.append(num)&#10;    return [mpp[num] for num in nums1]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">3</td>
      <td rowspan="1">Sq 03 Min Stack<br><br></b> <a href='https://leetcode.com/problems/min-stack/' target='_blank'>LeetCode 155</a></td>
      <td rowspan="1"><b>Example 1:</b> MinStack minStack = new MinStack(); minStack.push(-2); minStack.push(0); minStack.push(-3); minStack.getMin(); // return -3</td>
      <td><b>Time:</b> O(1) per operation<br><b>Space:</b> O(N)</td>
      <td><code>#include <stack></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Store pairs of `(value, current_minimum)` in the stack. Alternatively, use math to encode the difference between the value and the minimum to achieve O(1) space auxiliary, but a stack of pairs is standard.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class MinStack:&#10;    def __init__(self):&#10;        self.st = []&#10;    def push(self, val: int) -&gt; None:&#10;        if not self.st:&#10;            self.st.append((val, val))&#10;        else:&#10;            self.st.append((val, min(val, self.st[-1][1])))&#10;    def pop(self) -&gt; None:&#10;        self.st.pop()&#10;    def top(self) -&gt; int:&#10;        return self.st[-1][0]&#10;    def getMin(self) -&gt; int:&#10;        return self.st[-1][1]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">4</td>
      <td rowspan="1">Sq 04 Sliding Window Maximum<br><br></b> <a href='https://leetcode.com/problems/sliding-window-maximum/' target='_blank'>LeetCode 239</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: nums = [1,3,-1,-3,5,3,6,7], k = 3, Output: [3,3,5,5,6,7]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(K)</td>
      <td><code>#include <deque></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Monotonic Deque. Store indices in a double-ended queue. Maintain elements in strictly decreasing order. Pop front if it's out of window bounds. Add nums[dq.front()] to answer once window reaches size k.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">from collections import deque&#10;def maxSlidingWindow(nums: List[int], k: int) -&gt; List[int]:&#10;    dq = deque()&#10;    ans = []&#10;    for i in range(len(nums)):&#10;        if dq and dq[0] == i - k: dq.popleft()&#10;        while dq and nums[dq[-1]] &lt;= nums[i]: dq.pop()&#10;        dq.append(i)&#10;        if i &gt;= k - 1: ans.append(nums[dq[0]])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">5</td>
      <td rowspan="1">Sq 05 Lru Cache<br><br></b> <a href='https://leetcode.com/problems/lru-cache/' target='_blank'>LeetCode 146</a></td>
      <td rowspan="1"><b>Example 1:</b> Design question.</td>
      <td><b>Time:</b> O(1) per operation<br><b>Space:</b> O(Capacity)</td>
      <td><code>#include <unordered_map></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Use a Hash Map and a Doubly Linked List. The Map stores `key -> Node*`. The DLL maintains recency (head is most recent, tail is least recent). Update DLL pointers on access/insert.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class Node:&#10;    def __init__(self, key, val):&#10;        self.key, self.val = key, val&#10;        self.prev = self.next = None&#10;class LRUCache:&#10;    def __init__(self, capacity: int):&#10;        self.cap = capacity&#10;        self.head, self.tail = Node(-1, -1), Node(-1, -1)&#10;        self.head.next, self.tail.prev = self.tail, self.head&#10;        self.m = {}&#10;    def addNode(self, newnode):&#10;        temp = self.head.next&#10;        newnode.next = temp; newnode.prev = self.head&#10;        self.head.next = newnode; temp.prev = newnode&#10;    def deleteNode(self, delnode):&#10;        delprev, delnext = delnode.prev, delnode.next&#10;        delprev.next = delnext; delnext.prev = delprev&#10;    def get(self, key: int) -&gt; int:&#10;        if key in self.m:&#10;            resnode = self.m[key]&#10;            res = resnode.val&#10;            del self.m[key]&#10;            self.deleteNode(resnode)&#10;            self.addNode(resnode)&#10;            self.m[key] = self.head.next&#10;            return res&#10;        return -1&#10;    def put(self, key: int, value: int) -&gt; None:&#10;        if key in self.m:&#10;            existing = self.m[key]&#10;            del self.m[key]; self.deleteNode(existing)&#10;        if len(self.m) == self.cap:&#10;            del self.m[self.tail.prev.key]; self.deleteNode(self.tail.prev)&#10;        self.addNode(Node(key, value))&#10;        self.m[key] = self.head.next</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">6</td>
      <td rowspan="1">Sq 06 Largest Rectangle In Histogram<br><br></b> <a href='https://leetcode.com/problems/largest-rectangle-in-histogram/' target='_blank'>LeetCode 84</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: heights = [2,1,5,6,2,3], Output: 10</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><code>#include <stack></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Monotonic Stack. Find the next smaller element on the left and right for each bar. Area for bar `i` is `heights[i] * (right[i] - left[i] + 1)`. Alternatively, do it in a single pass stack loop.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def largestRectangleArea(heights: List[int]) -&gt; int:&#10;    n, maxArea = len(heights), 0&#10;    st = []&#10;    for i in range(n + 1):&#10;        while st and (i == n or heights[st[-1]] &gt;= heights[i]):&#10;            height = heights[st.pop()]&#10;            width = i if not st else i - st[-1] - 1&#10;            maxArea = max(maxArea, width * height)&#10;        st.append(i)&#10;    return maxArea</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">7</td>
      <td rowspan="1">Sq 7 Reverse A String Using Stack<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/reverse-a-string-using-stack/1' target='_blank'>GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Push and pop.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><code>#include <stack></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Push all characters of the string into a stack. Then pop them out one by one. The popped characters will be in reversed order.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def reverse(S: str) -&gt; str:&#10;    st = []&#10;    for c in S:&#10;        st.append(c)&#10;    res = &quot;&quot;&#10;    while st:&#10;        res += st.pop()&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">8</td>
      <td rowspan="1">Sq 8 Design A Stack That Supports Getmin<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/special-stack/1' target='_blank'>GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Formula approach.</td>
      <td><b>Time:</b> O(1)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> To achieve O(1) space, when pushing `x < minEle`, push `2 * x - minEle` and update `minEle = x`. When popping `y`, if `y < minEle`, then `minEle = 2 * minEle - y`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class SpecialStack:&#10;    def __init__(self):&#10;        self.s = []&#10;        self.minEle = float(&#x27;inf&#x27;)&#10;    def push(self, a):&#10;        if not self.s:&#10;            self.s.append(a)&#10;            self.minEle = a&#10;        elif a &lt; self.minEle:&#10;            self.s.append(2 * a - self.minEle)&#10;            self.minEle = a&#10;        else:&#10;            self.s.append(a)&#10;    def pop(self):&#10;        if not self.s: return -1&#10;        top = self.s.pop()&#10;        if top &lt; self.minEle:&#10;            prevMin = self.minEle&#10;            self.minEle = 2 * self.minEle - top&#10;            return prevMin&#10;        return top&#10;    def getMin(self):&#10;        if not self.s: return -1&#10;        return self.minEle</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">9</td>
      <td rowspan="1">Sq 9 Next Greater Element<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/next-larger-element-1587115620/1' target='_blank'>GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Decreasing stack.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><code>#include <stack></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Iterate from right to left. Use a stack to keep track of elements. Pop from the stack while the top element is less than or equal to the current element. If stack is empty, NGE is -1, else it's the stack top. Push current element.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def nextLargerElement(arr: List[int], n: int) -&gt; List[int]:&#10;    res = [-1] * n&#10;    st = []&#10;    for i in range(n - 1, -1, -1):&#10;        while st and st[-1] &lt;= arr[i]:&#10;            st.pop()&#10;        if st:&#10;            res[i] = st[-1]&#10;        st.append(arr[i])&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">10</td>
      <td rowspan="1">Sq 10 Celebrity Problem<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/the-celebrity-problem/1' target='_blank'>GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Two pointers or Stack.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><code>#include <stack></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Push all elements (0 to N-1) into a stack. Pop two elements `A` and `B`. If `A` knows `B`, `A` cannot be a celebrity, push `B` back. If `A` does not know `B`, `B` cannot be a celebrity, push `A` back. The remaining element is a potential celebrity. Verify it by checking if everyone knows it and it knows no one.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def celebrity(M: List[List[int]], n: int) -&gt; int:&#10;    st = list(range(n))&#10;    while len(st) &gt; 1:&#10;        a = st.pop()&#10;        b = st.pop()&#10;        if M[a][b] == 1:&#10;            st.append(b)&#10;        else:&#10;            st.append(a)&#10;    if not st: return -1&#10;    pot = st[0]&#10;    for i in range(n):&#10;        if i != pot and (M[pot][i] == 1 or M[i][pot] == 0):&#10;            return -1&#10;    return pot</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">11</td>
      <td rowspan="1">Sq 11 Arithmetic Expression Evaluation<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/arithmetic-expression-evaluation/0' target='_blank'>GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Two stacks (operands and operators).</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Use two stacks: one for numbers and one for operators. Process the expression character by character. If it's a number, push to numbers stack. If it's `(`, push to operators stack. If it's `)`, solve until `(`. If it's an operator, solve while top of operators stack has same or greater precedence, then push.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def evaluate(tokens: str) -&gt; int:&#10;    def precedence(op):&#10;        if op in (&#x27;+&#x27;, &#x27;-&#x27;): return 1&#10;        if op in (&#x27;*&#x27;, &#x27;/&#x27;): return 2&#10;        return 0&#10;    def applyOp(a, b, op):&#10;        if op == &#x27;+&#x27;: return a + b&#10;        if op == &#x27;-&#x27;: return a - b&#10;        if op == &#x27;*&#x27;: return a * b&#10;        if op == &#x27;/&#x27;: return a // b&#10;        return 0&#10;    values = []&#10;    ops = []&#10;    i = 0&#10;    while i &lt; len(tokens):&#10;        if tokens[i] == &#x27; &#x27;:&#10;            i += 1&#10;            continue&#10;        elif tokens[i] == &#x27;(&#x27;:&#10;            ops.append(tokens[i])&#10;        elif tokens[i].isdigit():&#10;            val = 0&#10;            while i &lt; len(tokens) and tokens[i].isdigit():&#10;                val = (val * 10) + int(tokens[i])&#10;                i += 1&#10;            values.append(val)&#10;            i -= 1&#10;        elif tokens[i] == &#x27;)&#x27;:&#10;            while ops and ops[-1] != &#x27;(&#x27;:&#10;                val2 = values.pop()&#10;                val1 = values.pop()&#10;                op = ops.pop()&#10;                values.append(applyOp(val1, val2, op))&#10;            ops.pop()&#10;        else:&#10;            while ops and precedence(ops[-1]) &gt;= precedence(tokens[i]):&#10;                val2 = values.pop()&#10;                val1 = values.pop()&#10;                op = ops.pop()&#10;                values.append(applyOp(val1, val2, op))&#10;            ops.append(tokens[i])&#10;        i += 1&#10;    while ops:&#10;        val2 = values.pop()&#10;        val1 = values.pop()&#10;        op = ops.pop()&#10;        values.append(applyOp(val1, val2, op))&#10;    return values[-1]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">12</td>
      <td rowspan="1">Sq 12 Evaluation Of Postfix Expression<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/evaluation-of-postfix-expression1735/1' target='_blank'>GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Stack of operands.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Iterate through the string. If it's a number, push it to stack. If it's an operator, pop two numbers from stack, apply the operator, and push the result back to stack.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def evaluatePostfix(S: str) -&gt; int:&#10;    st = []&#10;    for c in S:&#10;        if c.isdigit():&#10;            st.append(int(c))&#10;        else:&#10;            op2 = st.pop()&#10;            op1 = st.pop()&#10;            if c == &#x27;+&#x27;: st.append(op1 + op2)&#10;            elif c == &#x27;-&#x27;: st.append(op1 - op2)&#10;            elif c == &#x27;*&#x27;: st.append(op1 * op2)&#10;            elif c == &#x27;/&#x27;: st.append(int(op1 / op2))&#10;    return st[-1]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">13</td>
      <td rowspan="1">Sq 13 Insert An Element At Its Bottom In A Given Stack<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/insert-an-element-at-the-bottom-of-a-stack/1' target='_blank'>GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Recursive push.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Use recursion. If the stack is empty, push the element. Otherwise, pop the top element, recursively call the function, and then push the popped element back.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def insertAtBottom(St: List[int], X: int) -&gt; List[int]:&#10;    if not St:&#10;        St.append(X)&#10;        return St&#10;    top = St.pop()&#10;    insertAtBottom(St, X)&#10;    St.append(top)&#10;    return St</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">14</td>
      <td rowspan="1">Sq 14 Reverse A Stack Using Recursion<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/reverse-a-stack/1' target='_blank'>GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Recursive pop and insertAtBottom.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Recursively pop all elements until the stack is empty. Then, as the recursion unwinds, use another recursive function `insertAtBottom` to push the elements at the bottom.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def Reverse(St: List[int]) -&gt; None:&#10;    def insertAtBottom(St, X):&#10;        if not St:&#10;            St.append(X)&#10;            return&#10;        top = St.pop()&#10;        insertAtBottom(St, X)&#10;        St.append(top)&#10;    if not St: return&#10;    top = St.pop()&#10;    Reverse(St)&#10;    insertAtBottom(St, top)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">15</td>
      <td rowspan="1">Sq 15 Sort A Stack<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/sort-a-stack/1' target='_blank'>GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Recursive pop and sortedInsert.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Recursively pop elements until the stack is empty. Then, as the recursion unwinds, use another recursive function `sortedInsert` to insert the element in its sorted position.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def sortedInsert(s: List[int], x: int):&#10;    if not s or x &gt; s[-1]:&#10;        s.append(x)&#10;        return&#10;    temp = s.pop()&#10;    sortedInsert(s, x)&#10;    s.append(temp)&#10;def sortStack(s: List[int]) -&gt; None:&#10;    if not s: return&#10;    temp = s.pop()&#10;    sortStack(s)&#10;    sortedInsert(s, temp)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">16</td>
      <td rowspan="1">Sq 16 Merge Overlapping Intervals<br><br></b> <a href='https://leetcode.com/problems/merge-intervals/' target='_blank'>LeetCode 56</a></td>
      <td rowspan="1"><b>Example 1:</b> Stack of intervals.</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Sort intervals based on start time. Push first interval to stack. For each subsequent interval, if it overlaps with the stack top, pop the stack top, merge the two, and push back. Else, push it to stack.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def merge(intervals: List[List[int]]) -&gt; List[List[int]]:&#10;    if not intervals: return []&#10;    intervals.sort(key=lambda x: x[0])&#10;    st = [intervals[0]]&#10;    for i in range(1, len(intervals)):&#10;        if st[-1][1] &gt;= intervals[i][0]:&#10;            st[-1][1] = max(st[-1][1], intervals[i][1])&#10;        else:&#10;            st.append(intervals[i])&#10;    return st</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">17</td>
      <td rowspan="1">Sq 17 Maximum Rectangular Area In A Histogram<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/maximum-rectangular-area-in-a-histogram-1587115620/1' target='_blank'>GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Next Smaller Element on left and right.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Use a stack to find Next Smaller Element (NSE) and Previous Smaller Element (PSE) for each bar. Then, the width of the rectangle with bar `i` as the minimum height is `NSE[i] - PSE[i] - 1`. The area is `height[i] * width`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def getMaxArea(arr: List[int], n: int) -&gt; int:&#10;    st = []&#10;    max_area = 0&#10;    for i in range(n + 1):&#10;        while st and (i == n or arr[st[-1]] &gt;= arr[i]):&#10;            height = arr[st.pop()]&#10;            width = i if not st else i - st[-1] - 1&#10;            max_area = max(max_area, height * width)&#10;        st.append(i)&#10;    return max_area</code></pre></details></td>
    </tr>
  </tbody>
</table>
