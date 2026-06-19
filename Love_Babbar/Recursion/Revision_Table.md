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
    <tr>
      <td rowspan="1">2</td>
      <td rowspan="1">Rec 02 Combination Sum<br><br></b> <a href='https://leetcode.com/problems/combination-sum/' target='_blank'>LeetCode 39</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: candidates = [2,3,6,7], target = 7, Output: [[2,2,3],[7]]<br><br><b>Note (Constraint):</b> The same number may be chosen unlimited number of times.</td>
      <td><b>Time:</b> O(2<sup>T</sup>) (Trade-off)<br><b>Space:</b> O(T) (Trade-off)</td>
      <td>-</td>
      <td><b>Infinite Loop Prevention:</b> Base cases must immediately return if `target < 0` to prevent infinite recursion on the same index.</td>
      <td><b>Explanation:</b> Pick/Non-Pick but when picking, we *do not* increment the index `i`, allowing the same element to be picked infinitely until `target < 0`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def combination_sum(candidates: list[int], target: int) -&gt; list[list[int]]:&#10;    ans = []&#10;    def solve(i, current_target, temp):&#10;        if i == len(candidates):&#10;            if current_target == 0:&#10;                ans.append(temp.copy())&#10;            return&#10;            &#10;        if candidates[i] &lt;= current_target:&#10;            temp.append(candidates[i])&#10;            solve(i, current_target - candidates[i], temp)&#10;            temp.pop()&#10;            &#10;        solve(i + 1, current_target, temp)&#10;        &#10;    solve(0, target, [])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">3</td>
      <td rowspan="1">Rec 03 N Queens<br><br></b> <a href='https://leetcode.com/problems/n-queens/' target='_blank'>LeetCode 51</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: n = 4, Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]<br><br><b>Note (Constraint):</b> 1 &le; n &le; 9</td>
      <td><b>Time:</b> O(N!) (Constraint)<br><b>Space:</b> O(N) (Constraint)</td>
      <td>Hash Maps/Arrays for safety checks</td>
      <td><b>Diagonal Math:</b> Lower diagonal is tracked via `row + col`, Upper diagonal via `(n - 1) + (col - row)`.</td>
      <td><b>Explanation:</b> Backtracking. Try placing a queen in each row of the current column. Use `O(1)` lookups (Hashing logic) via arrays to check if row/diagonals are safe.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def solve_n_queens(n: int) -&gt; list[list[str]]:&#10;    ans = []&#10;    board = [[&quot;.&quot;] * n for _ in range(n)]&#10;    left_row = [0] * n&#10;    upper_diag = [0] * (2 * n - 1)&#10;    lower_diag = [0] * (2 * n - 1)&#10;    &#10;    def solve(col):&#10;        if col == n:&#10;            ans.append([&quot;&quot;.join(row) for row in board])&#10;            return&#10;            &#10;        for row in range(n):&#10;            if left_row[row] == 0 and lower_diag[row + col] == 0 and upper_diag[n - 1 + col - row] == 0:&#10;                board[row][col] = &#x27;Q&#x27;&#10;                left_row[row] = 1&#10;                lower_diag[row + col] = 1&#10;                upper_diag[n - 1 + col - row] = 1&#10;                &#10;                solve(col + 1)&#10;                &#10;                board[row][col] = &#x27;.&#x27;&#10;                left_row[row] = 0&#10;                lower_diag[row + col] = 0&#10;                upper_diag[n - 1 + col - row] = 0&#10;                &#10;    solve(0)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">4</td>
      <td rowspan="1">Rec 02 Subsets<br><br></b> <a href='https://leetcode.com/problems/subsets/' target='_blank'>LeetCode 78</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: nums = [1,2,3], Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]</td>
      <td><b>Time:</b> O(2<sup>N</sup> * N)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td><b>Reference Storage:</b> In Python, `temp[:]` must be used to append a copy of the subset, not the reference to the mutating list.</td>
      <td><b>Explanation:</b> Pick / Not Pick technique. For every element, branch recursively: one path includes the element, the other path excludes it.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def subsets(nums: list[int]) -&gt; list[list[int]]:&#10;    ans = []&#10;    def solve(idx, temp):&#10;        if idx == len(nums):&#10;            ans.append(temp[:])&#10;            return&#10;        temp.append(nums[idx])&#10;        solve(idx + 1, temp)&#10;        temp.pop()&#10;        solve(idx + 1, temp)&#10;    solve(0, [])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">5</td>
      <td rowspan="1">Rec 03 Permutations<br><br></b> <a href='https://leetcode.com/problems/permutations/' target='_blank'>LeetCode 46</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: nums = [1,2,3], Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]</td>
      <td><b>Time:</b> O(N! * N)<br><b>Space:</b> O(N)</td>
      <td><code>std::swap</code></td>
      <td><b>Backtracking necessity:</b> Without the second swap (backtrack), the array remains mutated for subsequent sibling recursion branches.</td>
      <td><b>Explanation:</b> Backtracking. Swap elements to generate permutations. For index `i`, swap it with every index from `i` to `n-1`, recurse, then backtrack (swap back).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def permute(nums: list[int]) -&gt; list[list[int]]:&#10;    ans = []&#10;    def solve(idx):&#10;        if idx == len(nums):&#10;            ans.append(nums[:])&#10;            return&#10;        for i in range(idx, len(nums)):&#10;            nums[idx], nums[i] = nums[i], nums[idx]&#10;            solve(idx + 1)&#10;            nums[idx], nums[i] = nums[i], nums[idx]&#10;    solve(0)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">6</td>
      <td rowspan="1">Rec 06 N Queens<br><br></b> <a href='https://leetcode.com/problems/n-queens/' target='_blank'>LeetCode 51</a></td>
      <td rowspan="1"><b>Example 1:</b> Classic N-Queens constraint satisfaction.</td>
      <td><b>Time:</b> O(N!)<br><b>Space:</b> O(N^2)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Backtracking. Place queen column by column. To optimize collision checking to O(1), use 3 arrays/hashmaps: `leftRow`, `upperDiagonal`, and `lowerDiagonal`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def solveNQueens(n: int) -&gt; List[List[str]]:&#10;    ans = []&#10;    board = [[&#x27;.&#x27;] * n for _ in range(n)]&#10;    leftRow, upperDiag, lowerDiag = [0]*n, [0]*(2*n-1), [0]*(2*n-1)&#10;    def solve(col):&#10;        if col == n:&#10;            ans.append([&#x27;&#x27;.join(row) for row in board])&#10;            return&#10;        for row in range(n):&#10;            if leftRow[row] == 0 and lowerDiag[row + col] == 0 and upperDiag[n - 1 + col - row] == 0:&#10;                board[row][col] = &#x27;Q&#x27;&#10;                leftRow[row] = 1; lowerDiag[row + col] = 1; upperDiag[n - 1 + col - row] = 1&#10;                solve(col + 1)&#10;                board[row][col] = &#x27;.&#x27;&#10;                leftRow[row] = 0; lowerDiag[row + col] = 0; upperDiag[n - 1 + col - row] = 0&#10;    solve(0)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">7</td>
      <td rowspan="1">Rec 07 Sudoku Solver<br><br></b> <a href='https://leetcode.com/problems/sudoku-solver/' target='_blank'>LeetCode 37</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: board with '.' for empty cells. Solve in-place.</td>
      <td><b>Time:</b> O(9^(n*n))<br><b>Space:</b> O(1) auxiliary</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Backtracking. Find first empty cell, try placing 1-9. Validate row, col, and 3x3 sub-grid. Recursively solve the rest. If it fails, backtrack.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def solveSudoku(board: List[List[str]]) -&gt; None:&#10;    def isValid(row, col, ch):&#10;        for i in range(9):&#10;            if board[i][col] == ch: return False&#10;            if board[row][i] == ch: return False&#10;            if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == ch: return False&#10;        return True&#10;    def solve():&#10;        for i in range(len(board)):&#10;            for j in range(len(board[0])):&#10;                if board[i][j] == &#x27;.&#x27;:&#10;                    for c in &#x27;123456789&#x27;:&#10;                        if isValid(i, j, c):&#10;                            board[i][j] = c&#10;                            if solve(): return True&#10;                            else: board[i][j] = &#x27;.&#x27;&#10;                    return False&#10;        return True&#10;    solve()</code></pre></details></td>
    </tr>
  </tbody>
</table>
