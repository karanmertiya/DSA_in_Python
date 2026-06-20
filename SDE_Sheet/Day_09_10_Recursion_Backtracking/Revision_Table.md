# Day 09 10 Recursion Backtracking Revision Table

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
      <td>Bit 01 Subsets<br><br></b> <a href="https://leetcode.com/problems/subsets/" target="_blank">LeetCode 78</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, SDE Sheet, Striver A Z</details></td>
      <td>**Example 1:**
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]</td>
      <td><details><summary><b>Approach 1</b></summary><b>Time:</b> O(N * 2^N)<br><b>Space:</b> O(N * 2^N)</details><details><summary><b>Approach 2</b></summary><b>Time:</b> O(N * 2^N)<br><b>Space:</b> O(N * 2^N)</details></td>
      <td><details><summary><b>Approach 1</b></summary><b>Explanation:</b> Recursive backtracking (include/exclude pattern).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def subsets_rec(nums: list[int]) -&gt; list[list[int]]:&#10;    ans, curr = [], []&#10;    def solve(idx):&#10;        if idx == len(nums):&#10;            ans.append(curr[:])&#10;            return&#10;        curr.append(nums[idx])&#10;        solve(idx + 1)&#10;        curr.pop()&#10;        solve(idx + 1)&#10;    solve(0)&#10;    return ans</code></pre></details></details><details><summary><b>Approach 2</b></summary><b>Explanation:</b> Bit manipulation technique. For N elements, there are 2^N subsets. Count from 0 to 2^N - 1. For each number, its binary representation indicates which elements to include.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def subsets(nums: list[int]) -&gt; list[list[int]]:&#10;    n = len(nums)&#10;    subsets_count = 1 &lt;&lt; n&#10;    ans = []&#10;    for i in range(subsets_count):&#10;        subset = []&#10;        for j in range(n):&#10;            if i &amp; (1 &lt;&lt; j):&#10;                subset.append(nums[j])&#10;        ans.append(subset)&#10;    return ans</code></pre></details></details></td>
    </tr>
    <tr>
      <td>2</td>
      <td>Rec 02 Combination Sum<br><br></b> <a href="https://leetcode.com/problems/combination-sum/" target="_blank">LeetCode 39</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: candidates = [2,3,6,7], target = 7, Output: [[2,2,3],[7]]<br><br>**Note (Constraint):** The same number may be chosen unlimited number of times.</td>
      <td><b>Time:</b> O(2<sup>T</sup>) (Trade-off)<br><b>Space:</b> O(T) (Trade-off)</td>
      <td><b>Explanation:</b> Pick/Non-Pick but when picking, we *do not* increment the index `i`, allowing the same element to be picked infinitely until `target < 0`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def combination_sum(candidates: list[int], target: int) -&gt; list[list[int]]:&#10;    ans = []&#10;    def solve(i, current_target, temp):&#10;        if i == len(candidates):&#10;            if current_target == 0:&#10;                ans.append(temp.copy())&#10;            return&#10;            &#10;        if candidates[i] &lt;= current_target:&#10;            temp.append(candidates[i])&#10;            solve(i, current_target - candidates[i], temp)&#10;            temp.pop()&#10;            &#10;        solve(i + 1, current_target, temp)&#10;        &#10;    solve(0, target, [])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>3</td>
      <td>Rec 03 N Queens<br><br></b> <a href="https://leetcode.com/problems/n-queens/" target="_blank">LeetCode 51</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, SDE Sheet, Striver A Z</details></td>
      <td>**Example 1:** Input: n = 4, Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]<br><br>**Note (Constraint):** 1 &le; n &le; 9</td>
      <td><b>Time:</b> O(N!) (Constraint)<br><b>Space:</b> O(N) (Constraint)</td>
      <td><b>Explanation:</b> Backtracking. Try placing a queen in each row of the current column. Use `O(1)` lookups (Hashing logic) via arrays to check if row/diagonals are safe.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def solve_n_queens(n: int) -&gt; list[list[str]]:&#10;    ans = []&#10;    board = [[&quot;.&quot;] * n for _ in range(n)]&#10;    left_row = [0] * n&#10;    upper_diag = [0] * (2 * n - 1)&#10;    lower_diag = [0] * (2 * n - 1)&#10;    &#10;    def solve(col):&#10;        if col == n:&#10;            ans.append([&quot;&quot;.join(row) for row in board])&#10;            return&#10;            &#10;        for row in range(n):&#10;            if left_row[row] == 0 and lower_diag[row + col] == 0 and upper_diag[n - 1 + col - row] == 0:&#10;                board[row][col] = &#x27;Q&#x27;&#10;                left_row[row] = 1&#10;                lower_diag[row + col] = 1&#10;                upper_diag[n - 1 + col - row] = 1&#10;                &#10;                solve(col + 1)&#10;                &#10;                board[row][col] = &#x27;.&#x27;&#10;                left_row[row] = 0&#10;                lower_diag[row + col] = 0&#10;                upper_diag[n - 1 + col - row] = 0&#10;                &#10;    solve(0)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>4</td>
      <td>Rec 04 Permutations<br><br></b> <a href="https://leetcode.com/problems/permutations/" target="_blank">LeetCode 46</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, SDE Sheet, Striver A Z</details></td>
      <td>**Example 1:** Input: nums = [1,2,3], Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]</td>
      <td><b>Time:</b> O(N! * N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Backtracking. Swap elements to generate permutations. For index `i`, swap it with every index from `i` to `n-1`, recurse, then backtrack (swap back).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def permute(nums: list[int]) -&gt; list[list[int]]:&#10;    ans = []&#10;    def solve(idx):&#10;        if idx == len(nums):&#10;            ans.append(nums[:])&#10;            return&#10;        for i in range(idx, len(nums)):&#10;            nums[idx], nums[i] = nums[i], nums[idx]&#10;            solve(idx + 1)&#10;            nums[idx], nums[i] = nums[i], nums[idx]&#10;    solve(0)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>5</td>
      <td>Rec 05 Print All Permutations Of A String<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/permutations-of-a-given-string2041/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, SDE Sheet, Striver A Z</details></td>
      <td>**Example 1:** Recursive Backtracking.</td>
      <td><b>Time:</b> O(N! * N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Convert string to char array and sort it. Use backtracking: pass a boolean visited array and a temporary string. If temporary string length equals original length, add to answer. Else, iterate through characters. To avoid duplicates, if `i > 0` and `s[i] == s[i-1]` and `!vis[i-1]`, skip. Otherwise, mark visited, append, recurse, unmark, pop.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def find_permutation(S: str) -&gt; List[str]:&#10;    S = sorted(list(S))&#10;    ans = []&#10;    vis = [False] * len(S)&#10;    def solve(curr):&#10;        if len(curr) == len(S):&#10;            ans.append(&quot;&quot;.join(curr))&#10;            return&#10;        for i in range(len(S)):&#10;            if vis[i] or (i &gt; 0 and S[i] == S[i-1] and not vis[i-1]):&#10;                continue&#10;            vis[i] = True&#10;            curr.append(S[i])&#10;            solve(curr)&#10;            curr.pop()&#10;            vis[i] = False&#10;    solve([])&#10;    return ans</code></pre></details></td>
    </tr>
  </tbody>
</table>
