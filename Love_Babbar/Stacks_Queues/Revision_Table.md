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
  </tbody>
</table>
