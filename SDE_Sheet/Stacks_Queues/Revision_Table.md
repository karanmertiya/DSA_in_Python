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
      <td rowspan="1">Sq 01 Valid Parentheses<br><br></b> <a href='https://leetcode.com/problems/valid-parentheses/' target='_blank'>LeetCode 20</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: s = "()[]{}", Output: true<br><br><b>Note (Constraint):</b> Use LIFO behavior.</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(N)</td>
      <td><code>std::stack</code></td>
      <td><b>Empty Stack pop:</b> Must check `!st.empty()` before popping to prevent segfaults when given extra closing brackets `)]}`.</td>
      <td><b>Explanation:</b> Use a Stack. Push opening brackets. For closing brackets, pop the stack and check if it matches the corresponding opening bracket.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def is_valid(s: str) -&gt; bool:&#10;    stack = []&#10;    mapping = {&#x27;)&#x27;: &#x27;(&#x27;, &#x27;}&#x27;: &#x27;{&#x27;, &#x27;]&#x27;: &#x27;[&#x27;}&#10;    for char in s:&#10;        if char in mapping:&#10;            top = stack.pop() if stack else &#x27;#&#x27;&#10;            if mapping[char] != top: return False&#10;        else:&#10;            stack.append(char)&#10;    return not stack</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">2</td>
      <td rowspan="1">Sq 02 Implement Queue Using Stacks<br><br></b> <a href='https://leetcode.com/problems/implement-queue-using-stacks/' target='_blank'>LeetCode 232</a></td>
      <td rowspan="1"><b>Example 1:</b> `push(1)`, `push(2)`, `peek()` -> 1, `pop()` -> 1, `empty()` -> false.</td>
      <td><b>Time:</b> O(1) Amortized<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td><b>Amortized Transfer:</b> Reversing `input` into `output` takes `O(N)` but only happens rarely, making average pop operations `O(1)`.</td>
      <td><b>Explanation:</b> Amortized O(1). Maintain an `input` stack for pushes and an `output` stack for pops. Only transfer elements when `output` is empty.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class MyQueue:&#10;    def __init__(self):&#10;        self.input = []&#10;        self.output = []&#10;        &#10;    def push(self, x: int) -&gt; None:&#10;        self.input.append(x)&#10;        &#10;    def pop(self) -&gt; int:&#10;        self.peek()&#10;        return self.output.pop()&#10;        &#10;    def peek(self) -&gt; int:&#10;        if not self.output:&#10;            while self.input:&#10;                self.output.append(self.input.pop())&#10;        return self.output[-1]&#10;        &#10;    def empty(self) -&gt; bool:&#10;        return not self.input and not self.output</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">3</td>
      <td rowspan="1">Sq 03 Next Greater Element I<br><br></b> <a href='https://leetcode.com/problems/next-greater-element-i/' target='_blank'>LeetCode 496</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: nums = [4,1,2], Output: [-1, 2, -1]<br><br><b>Note (Constraint):</b> Monotonic Stack.</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(N)</td>
      <td>Monotonic Stack</td>
      <td><b>Linear Time:</b> Even with an inner `while` loop, every element is pushed and popped exactly once, guaranteeing overall `O(2N)` time.</td>
      <td><b>Explanation:</b> Iterate backwards maintaining a strictly decreasing Monotonic Stack. The top of the stack is the next greater element.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def next_greater_element(nums: list[int]) -&gt; list[int]:&#10;    res = [-1] * len(nums)&#10;    stack = []&#10;    for i in range(len(nums) - 1, -1, -1):&#10;        while stack and stack[-1] &lt;= nums[i]:&#10;            stack.pop()&#10;        if stack:&#10;            res[i] = stack[-1]&#10;        stack.append(nums[i])&#10;    return res</code></pre></details></td>
    </tr>
  </tbody>
</table>
