# Stacks Queues Revision Table

<table border="1">
  <thead>
    <tr>
      <th style="width: 5%;">S.No</th>
      <th style="width: 15%;">Problem Name</th>
      <th style="width: 30%;">Example & Constraints</th>
      <th style="width: 15%;">Complexity</th>
      <th style="width: 35%;">Logic</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Sq 01 Valid Parentheses<br><br></b> <a href='https://leetcode.com/problems/valid-parentheses/' target='_blank'>LeetCode 20</a></td>
      <td><b>Example 1:</b> Input: s = "()[]{}", Output: true</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Use a Stack. Push open brackets. If a closed bracket is found, verify it matches the top of the stack and pop.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isValid(s: str) -&gt; bool:&#10;    st = []&#10;    mapping = {&#x27;)&#x27;: &#x27;(&#x27;, &#x27;}&#x27;: &#x27;{&#x27;, &#x27;]&#x27;: &#x27;[&#x27;}&#10;    for char in s:&#10;        if char in mapping:&#10;            top = st.pop() if st else &#x27;#&#x27;&#10;            if mapping[char] != top: return False&#10;        else:&#10;            st.append(char)&#10;    return not st</code></pre></details></td>
    </tr>
    <tr>
      <td>2</td>
      <td>Sq 02 Next Greater Element I<br><br></b> <a href='https://leetcode.com/problems/next-greater-element-i/' target='_blank'>LeetCode 496</a></td>
      <td><b>Example 1:</b> Input: nums1 = [4,1,2], nums2 = [1,3,4,2], Output: [-1,3,-1]</td>
      <td><b>Time:</b> O(N + M)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Monotonic Stack traversing `nums2` from right to left. Maintain stack of elements in decreasing order.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def nextGreaterElement(nums1: list[int], nums2: list[int]) -&gt; list[int]:&#10;    mpp = {}&#10;    st = []&#10;    for num in reversed(nums2):&#10;        while st and st[-1] &lt;= num: st.pop()&#10;        mpp[num] = st[-1] if st else -1&#10;        st.append(num)&#10;    return [mpp[num] for num in nums1]</code></pre></details></td>
    </tr>
    <tr>
      <td>3</td>
      <td>Sq 03 Min Stack<br><br></b> <a href='https://leetcode.com/problems/min-stack/' target='_blank'>LeetCode 155</a></td>
      <td><b>Example 1:</b> MinStack minStack = new MinStack(); minStack.push(-2); minStack.push(0); minStack.push(-3); minStack.getMin(); // return -3</td>
      <td><b>Time:</b> O(1) per operation<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Store pairs of `(value, current_minimum)` in the stack. Alternatively, use math to encode the difference between the value and the minimum to achieve O(1) space auxiliary, but a stack of pairs is standard.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class MinStack:&#10;    def __init__(self):&#10;        self.st = []&#10;    def push(self, val: int) -&gt; None:&#10;        if not self.st:&#10;            self.st.append((val, val))&#10;        else:&#10;            self.st.append((val, min(val, self.st[-1][1])))&#10;    def pop(self) -&gt; None:&#10;        self.st.pop()&#10;    def top(self) -&gt; int:&#10;        return self.st[-1][0]&#10;    def getMin(self) -&gt; int:&#10;        return self.st[-1][1]</code></pre></details></td>
    </tr>
    <tr>
      <td>4</td>
      <td>Sq 04 Largest Rectangle In Histogram<br><br></b> <a href='https://leetcode.com/problems/largest-rectangle-in-histogram/' target='_blank'>LeetCode 84</a></td>
      <td><b>Example 1:</b> Input: heights = [2,1,5,6,2,3], Output: 10</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Monotonic Stack. Find the next smaller element on the left and right for each bar. Area for bar `i` is `heights[i] * (right[i] - left[i] + 1)`. Alternatively, do it in a single pass stack loop.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def largestRectangleArea(heights: List[int]) -&gt; int:&#10;    n, maxArea = len(heights), 0&#10;    st = []&#10;    for i in range(n + 1):&#10;        while st and (i == n or heights[st[-1]] &gt;= heights[i]):&#10;            height = heights[st.pop()]&#10;            width = i if not st else i - st[-1] - 1&#10;            maxArea = max(maxArea, width * height)&#10;        st.append(i)&#10;    return maxArea</code></pre></details></td>
    </tr>
    <tr>
      <td>5</td>
      <td>Sq 05 Reverse A String Using Stack<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/reverse-a-string-using-stack/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Push and pop.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Push all characters of the string into a stack. Then pop them out one by one. The popped characters will be in reversed order.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def reverse(S: str) -&gt; str:&#10;    st = []&#10;    for c in S:&#10;        st.append(c)&#10;    res = &quot;&quot;&#10;    while st:&#10;        res += st.pop()&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td>6</td>
      <td>Sq 06 Design A Stack That Supports Getmin<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/special-stack/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Formula approach.</td>
      <td><b>Time:</b> O(1)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> To achieve O(1) space, when pushing `x < minEle`, push `2 * x - minEle` and update `minEle = x`. When popping `y`, if `y < minEle`, then `minEle = 2 * minEle - y`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class SpecialStack:&#10;    def __init__(self):&#10;        self.s = []&#10;        self.minEle = float(&#x27;inf&#x27;)&#10;    def push(self, a):&#10;        if not self.s:&#10;            self.s.append(a)&#10;            self.minEle = a&#10;        elif a &lt; self.minEle:&#10;            self.s.append(2 * a - self.minEle)&#10;            self.minEle = a&#10;        else:&#10;            self.s.append(a)&#10;    def pop(self):&#10;        if not self.s: return -1&#10;        top = self.s.pop()&#10;        if top &lt; self.minEle:&#10;            prevMin = self.minEle&#10;            self.minEle = 2 * self.minEle - top&#10;            return prevMin&#10;        return top&#10;    def getMin(self):&#10;        if not self.s: return -1&#10;        return self.minEle</code></pre></details></td>
    </tr>
    <tr>
      <td>7</td>
      <td>Sq 07 Next Greater Element<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/next-larger-element-1587115620/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Decreasing stack.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Iterate from right to left. Use a stack to keep track of elements. Pop from the stack while the top element is less than or equal to the current element. If stack is empty, NGE is -1, else it's the stack top. Push current element.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def nextLargerElement(arr: List[int], n: int) -&gt; List[int]:&#10;    res = [-1] * n&#10;    st = []&#10;    for i in range(n - 1, -1, -1):&#10;        while st and st[-1] &lt;= arr[i]:&#10;            st.pop()&#10;        if st:&#10;            res[i] = st[-1]&#10;        st.append(arr[i])&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td>8</td>
      <td>Sq 08 Celebrity Problem<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/the-celebrity-problem/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Two pointers or Stack.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Push all elements (0 to N-1) into a stack. Pop two elements `A` and `B`. If `A` knows `B`, `A` cannot be a celebrity, push `B` back. If `A` does not know `B`, `B` cannot be a celebrity, push `A` back. The remaining element is a potential celebrity. Verify it by checking if everyone knows it and it knows no one.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def celebrity(M: List[List[int]], n: int) -&gt; int:&#10;    st = list(range(n))&#10;    while len(st) &gt; 1:&#10;        a = st.pop()&#10;        b = st.pop()&#10;        if M[a][b] == 1:&#10;            st.append(b)&#10;        else:&#10;            st.append(a)&#10;    if not st: return -1&#10;    pot = st[0]&#10;    for i in range(n):&#10;        if i != pot and (M[pot][i] == 1 or M[i][pot] == 0):&#10;            return -1&#10;    return pot</code></pre></details></td>
    </tr>
    <tr>
      <td>9</td>
      <td>Sq 09 Arithmetic Expression Evaluation<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/arithmetic-expression-evaluation/0' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Two stacks (operands and operators).</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Use two stacks: one for numbers and one for operators. Process the expression character by character. If it's a number, push to numbers stack. If it's `(`, push to operators stack. If it's `)`, solve until `(`. If it's an operator, solve while top of operators stack has same or greater precedence, then push.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def evaluate(tokens: str) -&gt; int:&#10;    def precedence(op):&#10;        if op in (&#x27;+&#x27;, &#x27;-&#x27;): return 1&#10;        if op in (&#x27;*&#x27;, &#x27;/&#x27;): return 2&#10;        return 0&#10;    def applyOp(a, b, op):&#10;        if op == &#x27;+&#x27;: return a + b&#10;        if op == &#x27;-&#x27;: return a - b&#10;        if op == &#x27;*&#x27;: return a * b&#10;        if op == &#x27;/&#x27;: return a // b&#10;        return 0&#10;    values = []&#10;    ops = []&#10;    i = 0&#10;    while i &lt; len(tokens):&#10;        if tokens[i] == &#x27; &#x27;:&#10;            i += 1&#10;            continue&#10;        elif tokens[i] == &#x27;(&#x27;:&#10;            ops.append(tokens[i])&#10;        elif tokens[i].isdigit():&#10;            val = 0&#10;            while i &lt; len(tokens) and tokens[i].isdigit():&#10;                val = (val * 10) + int(tokens[i])&#10;                i += 1&#10;            values.append(val)&#10;            i -= 1&#10;        elif tokens[i] == &#x27;)&#x27;:&#10;            while ops and ops[-1] != &#x27;(&#x27;:&#10;                val2 = values.pop()&#10;                val1 = values.pop()&#10;                op = ops.pop()&#10;                values.append(applyOp(val1, val2, op))&#10;            ops.pop()&#10;        else:&#10;            while ops and precedence(ops[-1]) &gt;= precedence(tokens[i]):&#10;                val2 = values.pop()&#10;                val1 = values.pop()&#10;                op = ops.pop()&#10;                values.append(applyOp(val1, val2, op))&#10;            ops.append(tokens[i])&#10;        i += 1&#10;    while ops:&#10;        val2 = values.pop()&#10;        val1 = values.pop()&#10;        op = ops.pop()&#10;        values.append(applyOp(val1, val2, op))&#10;    return values[-1]</code></pre></details></td>
    </tr>
    <tr>
      <td>10</td>
      <td>Sq 10 Evaluation Of Postfix Expression<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/evaluation-of-postfix-expression1735/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Stack of operands.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Iterate through the string. If it's a number, push it to stack. If it's an operator, pop two numbers from stack, apply the operator, and push the result back to stack.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def evaluatePostfix(S: str) -&gt; int:&#10;    st = []&#10;    for c in S:&#10;        if c.isdigit():&#10;            st.append(int(c))&#10;        else:&#10;            op2 = st.pop()&#10;            op1 = st.pop()&#10;            if c == &#x27;+&#x27;: st.append(op1 + op2)&#10;            elif c == &#x27;-&#x27;: st.append(op1 - op2)&#10;            elif c == &#x27;*&#x27;: st.append(op1 * op2)&#10;            elif c == &#x27;/&#x27;: st.append(int(op1 / op2))&#10;    return st[-1]</code></pre></details></td>
    </tr>
    <tr>
      <td>11</td>
      <td>Sq 11 Insert An Element At Its Bottom In A Given Stack<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/insert-an-element-at-the-bottom-of-a-stack/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Recursive push.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Use recursion. If the stack is empty, push the element. Otherwise, pop the top element, recursively call the function, and then push the popped element back.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def insertAtBottom(St: List[int], X: int) -&gt; List[int]:&#10;    if not St:&#10;        St.append(X)&#10;        return St&#10;    top = St.pop()&#10;    insertAtBottom(St, X)&#10;    St.append(top)&#10;    return St</code></pre></details></td>
    </tr>
    <tr>
      <td>12</td>
      <td>Sq 12 Reverse A Stack Using Recursion<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/reverse-a-stack/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Recursive pop and insertAtBottom.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Recursively pop all elements until the stack is empty. Then, as the recursion unwinds, use another recursive function `insertAtBottom` to push the elements at the bottom.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def Reverse(St: List[int]) -&gt; None:&#10;    def insertAtBottom(St, X):&#10;        if not St:&#10;            St.append(X)&#10;            return&#10;        top = St.pop()&#10;        insertAtBottom(St, X)&#10;        St.append(top)&#10;    if not St: return&#10;    top = St.pop()&#10;    Reverse(St)&#10;    insertAtBottom(St, top)</code></pre></details></td>
    </tr>
    <tr>
      <td>13</td>
      <td>Sq 13 Maximum Rectangular Area In A Histogram<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/maximum-rectangular-area-in-a-histogram-1587115620/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Next Smaller Element on left and right.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Use a stack to find Next Smaller Element (NSE) and Previous Smaller Element (PSE) for each bar. Then, the width of the rectangle with bar `i` as the minimum height is `NSE[i] - PSE[i] - 1`. The area is `height[i] * width`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def getMaxArea(arr: List[int], n: int) -&gt; int:&#10;    st = []&#10;    max_area = 0&#10;    for i in range(n + 1):&#10;        while st and (i == n or arr[st[-1]] &gt;= arr[i]):&#10;            height = arr[st.pop()]&#10;            width = i if not st else i - st[-1] - 1&#10;            max_area = max(max_area, height * width)&#10;        st.append(i)&#10;    return max_area</code></pre></details></td>
    </tr>
    <tr>
      <td>14</td>
      <td>Sq 14 Next Smaller Element<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/fab3281cefac7140ca15e21505beddf7e4323e08/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Monotonic Stack.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Iterate from right to left. Use a monotonic stack. Pop elements from the stack that are greater than or equal to the current element. The top of the stack is the next smaller element. Push the current element to the stack.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def help_classmate(arr, n):&#10;    ans = [-1] * n&#10;    s = []&#10;    for i in range(n - 1, -1, -1):&#10;        while s and s[-1] &gt;= arr[i]: s.pop()&#10;        if s: ans[i] = s[-1]&#10;        s.append(arr[i])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>15</td>
      <td>Sq 15 Maximal Rectangle<br><br></b> <a href='https://leetcode.com/problems/maximal-rectangle/' target='_blank'>LeetCode 85</a></td>
      <td><b>Example 1:</b> Largest Rectangle in Histogram reduction.</td>
      <td><b>Time:</b> O(rows * cols)<br><b>Space:</b> O(cols)</td>
      <td><b>Explanation:</b> Treat each row as the base of a histogram. The height of each bar is the number of consecutive 1s above it. Apply the Largest Rectangle in Histogram algorithm for each row and maintain the maximum area.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maximalRectangle(matrix):&#10;    if not matrix: return 0&#10;    rows, cols = len(matrix), len(matrix[0])&#10;    heights = [0] * cols&#10;    maxArea = 0&#10;    def largestRectangleArea(h):&#10;        s, max_a = [], 0&#10;        for i, val in enumerate(h + [0]):&#10;            while s and h[s[-1]] &gt;= val:&#10;                height = h[s.pop()]&#10;                width = i if not s else i - s[-1] - 1&#10;                max_a = max(max_a, height * width)&#10;            s.append(i)&#10;        return max_a&#10;    for row in matrix:&#10;        for j in range(cols):&#10;            heights[j] = heights[j] + 1 if row[j] == &#x27;1&#x27; else 0&#10;        maxArea = max(maxArea, largestRectangleArea(heights))&#10;    return maxArea</code></pre></details></td>
    </tr>
    <tr>
      <td>16</td>
      <td>Sq 16 Online Stock Span<br><br></b> <a href='https://leetcode.com/problems/online-stock-span/' target='_blank'>LeetCode 901</a></td>
      <td><b>Example 1:</b> Monotonic Stack.</td>
      <td><b>Time:</b> O(1) amortized<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Use a stack of pairs `(price, span)`. When a new price comes in, initialize its span to 1. Pop elements from the stack while the top element's price is `<= price`, adding their spans to the current span. Push `(price, span)` to the stack.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class StockSpanner:&#10;    def __init__(self):&#10;        self.s = []&#10;    def next(self, price: int) -&gt; int:&#10;        span = 1&#10;        while self.s and self.s[-1][0] &lt;= price:&#10;            span += self.s.pop()[1]&#10;        self.s.append((price, span))&#10;        return span</code></pre></details></td>
    </tr>
    <tr>
      <td>17</td>
      <td>Sq 17 Rotten Oranges<br><br></b> <a href='https://leetcode.com/problems/rotting-oranges/' target='_blank'>LeetCode 994</a></td>
      <td><b>Example 1:</b> BFS.</td>
      <td><b>Time:</b> O(rows * cols)<br><b>Space:</b> O(rows * cols)</td>
      <td><b>Explanation:</b> Use a Queue for BFS. Find all initially rotten oranges and push them into the queue with time 0. Count total fresh oranges. Pop an orange, rot its adjacent fresh oranges, push them to the queue with `time + 1`, and decrement fresh count. Return the max time if fresh count is 0, else -1.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">from collections import deque&#10;def orangesRotting(grid):&#10;    rows, cols = len(grid), len(grid[0])&#10;    q = deque()&#10;    fresh_cnt = 0&#10;    for i in range(rows):&#10;        for j in range(cols):&#10;            if grid[i][j] == 2: q.append((i, j, 0))&#10;            elif grid[i][j] == 1: fresh_cnt += 1&#10;    tm, cnt = 0, 0&#10;    while q:&#10;        r, c, t = q.popleft()&#10;        tm = max(tm, t)&#10;        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:&#10;            nr, nc = r + dr, c + dc&#10;            if 0 &lt;= nr &lt; rows and 0 &lt;= nc &lt; cols and grid[nr][nc] == 1:&#10;                grid[nr][nc] = 2&#10;                q.append((nr, nc, t + 1))&#10;                cnt += 1&#10;    return tm if cnt == fresh_cnt else -1</code></pre></details></td>
    </tr>
  </tbody>
</table>
