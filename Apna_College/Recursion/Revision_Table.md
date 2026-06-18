# Recursion Revision Table

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
      <td rowspan="1">Rec 01 Subsets<br><br></b> <a href='https://leetcode.com/problems/subsets/' target='_blank'>LeetCode 78</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: nums = [1,2,3], Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]<br><br><b>Note (Constraint):</b> The solution set must not contain duplicate subsets.</td>
      <td><b>Time:</b> O(2<sup>N</sup>) (Constraint)<br><b>Space:</b> O(N) (Constraint)</td>
      <td>-</td>
      <td><b>Recursion Tree Depth:</b> The maximum depth of the recursive stack is `N`, leading to `O(N)` auxiliary space.</td>
      <td><b>Explanation:</b> Pick / Non-Pick logic. For every element, we have two choices: either include it in the current subset, or don't. Recursively explore both paths.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def subsets(nums: list[int]) -&gt; list[list[int]]:&#10;    ans = []&#10;    def solve(i, temp):&#10;        if i == len(nums):&#10;            ans.append(temp.copy())&#10;            return&#10;        # Pick&#10;        temp.append(nums[i])&#10;        solve(i + 1, temp)&#10;        temp.pop()&#10;        &#10;        # Not Pick&#10;        solve(i + 1, temp)&#10;        &#10;    solve(0, [])&#10;    return ans</code></pre></details></td>
    </tr>
  </tbody>
</table>
