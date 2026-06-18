# Dynamic Programming Revision Table

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
      <td rowspan="2">1</td>
      <td rowspan="2">Dp 01 Climbing Stairs<br><br></b> <a href='https://leetcode.com/problems/climbing-stairs/' target='_blank'>LeetCode 70</a></td>
      <td rowspan="2"><b>Example 1:</b> Input: n = 3, Output: 3 (1+1+1, 1+2, 2+1)<br><br><b>Note (Constraint):</b> This is the Fibonacci sequence in disguise.</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(N) + O(N) Recursion Stack</td>
      <td>-</td>
      <td><b>Base Cases:</b> `n <= 1` returns 1. Array initialized to `-1` to denote uncomputed states.</td>
      <td><b>Explanation:</b> Memoization (Top-Down): Recursive tree caching already solved subproblems in an array.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def climb_stairs_memo(n: int) -&gt; int:&#10;    dp = [-1] * (n + 1)&#10;    def solve(n):&#10;        if n &lt;= 1: return 1&#10;        if dp[n] != -1: return dp[n]&#10;        dp[n] = solve(n - 1) + solve(n - 2)&#10;        return dp[n]&#10;    return solve(n)</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1) (Constraint)</td>
      <td>-</td>
      <td><b>Variable Swapping:</b> `prev2` becomes `prev`, and `prev` becomes the new `curr`.</td>
      <td><b>Explanation:</b> Space Optimization (Bottom-Up): Since state `n` only depends on `n-1` and `n-2`, we only need two variables.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def climb_stairs_optimal(n: int) -&gt; int:&#10;    if n &lt;= 1: return 1&#10;    prev2 = 1&#10;    prev = 1&#10;    for i in range(2, n + 1):&#10;        curr = prev + prev2&#10;        prev2 = prev&#10;        prev = curr&#10;    return prev</code></pre></details></td>
    </tr>
  </tbody>
</table>
