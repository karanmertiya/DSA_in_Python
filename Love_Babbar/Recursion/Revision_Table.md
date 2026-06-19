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
      <td>1</td>
      <td>Rec 01 Subsets<br><br></b> <a href='https://leetcode.com/problems/subsets/' target='_blank'>LeetCode 78</a></td>
      <td><b>Example 1:</b> Input: nums = [1,2,3], Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]<br><br><b>Note (Constraint):</b> The solution set must not contain duplicate subsets.</td>
      <td><b>Time:</b> O(2<sup>N</sup>) (Constraint)<br><b>Space:</b> O(N) (Constraint)</td>
      <td>-</td>
      <td><b>Recursion Tree Depth:</b> The maximum depth of the recursive stack is `N`, leading to `O(N)` auxiliary space.</td>
      <td><b>Explanation:</b> Pick / Non-Pick logic. For every element, we have two choices: either include it in the current subset, or don't. Recursively explore both paths.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def subsets(nums: list[int]) -&gt; list[list[int]]:&#10;    ans = []&#10;    def solve(i, temp):&#10;        if i == len(nums):&#10;            ans.append(temp.copy())&#10;            return&#10;        # Pick&#10;        temp.append(nums[i])&#10;        solve(i + 1, temp)&#10;        temp.pop()&#10;        &#10;        # Not Pick&#10;        solve(i + 1, temp)&#10;        &#10;    solve(0, [])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>2</td>
      <td>Rec 02 Combination Sum<br><br></b> <a href='https://leetcode.com/problems/combination-sum/' target='_blank'>LeetCode 39</a></td>
      <td><b>Example 1:</b> Input: candidates = [2,3,6,7], target = 7, Output: [[2,2,3],[7]]<br><br><b>Note (Constraint):</b> The same number may be chosen unlimited number of times.</td>
      <td><b>Time:</b> O(2<sup>T</sup>) (Trade-off)<br><b>Space:</b> O(T) (Trade-off)</td>
      <td>-</td>
      <td><b>Infinite Loop Prevention:</b> Base cases must immediately return if `target < 0` to prevent infinite recursion on the same index.</td>
      <td><b>Explanation:</b> Pick/Non-Pick but when picking, we *do not* increment the index `i`, allowing the same element to be picked infinitely until `target < 0`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def combination_sum(candidates: list[int], target: int) -&gt; list[list[int]]:&#10;    ans = []&#10;    def solve(i, current_target, temp):&#10;        if i == len(candidates):&#10;            if current_target == 0:&#10;                ans.append(temp.copy())&#10;            return&#10;            &#10;        if candidates[i] &lt;= current_target:&#10;            temp.append(candidates[i])&#10;            solve(i, current_target - candidates[i], temp)&#10;            temp.pop()&#10;            &#10;        solve(i + 1, current_target, temp)&#10;        &#10;    solve(0, target, [])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>3</td>
      <td>Rec 03 N Queens<br><br></b> <a href='https://leetcode.com/problems/n-queens/' target='_blank'>LeetCode 51</a></td>
      <td><b>Example 1:</b> Input: n = 4, Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]<br><br><b>Note (Constraint):</b> 1 &le; n &le; 9</td>
      <td><b>Time:</b> O(N!) (Constraint)<br><b>Space:</b> O(N) (Constraint)</td>
      <td>Hash Maps/Arrays for safety checks</td>
      <td><b>Diagonal Math:</b> Lower diagonal is tracked via `row + col`, Upper diagonal via `(n - 1) + (col - row)`.</td>
      <td><b>Explanation:</b> Backtracking. Try placing a queen in each row of the current column. Use `O(1)` lookups (Hashing logic) via arrays to check if row/diagonals are safe.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def solve_n_queens(n: int) -&gt; list[list[str]]:&#10;    ans = []&#10;    board = [[&quot;.&quot;] * n for _ in range(n)]&#10;    left_row = [0] * n&#10;    upper_diag = [0] * (2 * n - 1)&#10;    lower_diag = [0] * (2 * n - 1)&#10;    &#10;    def solve(col):&#10;        if col == n:&#10;            ans.append([&quot;&quot;.join(row) for row in board])&#10;            return&#10;            &#10;        for row in range(n):&#10;            if left_row[row] == 0 and lower_diag[row + col] == 0 and upper_diag[n - 1 + col - row] == 0:&#10;                board[row][col] = &#x27;Q&#x27;&#10;                left_row[row] = 1&#10;                lower_diag[row + col] = 1&#10;                upper_diag[n - 1 + col - row] = 1&#10;                &#10;                solve(col + 1)&#10;                &#10;                board[row][col] = &#x27;.&#x27;&#10;                left_row[row] = 0&#10;                lower_diag[row + col] = 0&#10;                upper_diag[n - 1 + col - row] = 0&#10;                &#10;    solve(0)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>4</td>
      <td>Rec 02 Subsets<br><br></b> <a href='https://leetcode.com/problems/subsets/' target='_blank'>LeetCode 78</a></td>
      <td><b>Example 1:</b> Input: nums = [1,2,3], Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]</td>
      <td><b>Time:</b> O(2<sup>N</sup> * N)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td><b>Reference Storage:</b> In Python, `temp[:]` must be used to append a copy of the subset, not the reference to the mutating list.</td>
      <td><b>Explanation:</b> Pick / Not Pick technique. For every element, branch recursively: one path includes the element, the other path excludes it.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def subsets(nums: list[int]) -&gt; list[list[int]]:&#10;    ans = []&#10;    def solve(idx, temp):&#10;        if idx == len(nums):&#10;            ans.append(temp[:])&#10;            return&#10;        temp.append(nums[idx])&#10;        solve(idx + 1, temp)&#10;        temp.pop()&#10;        solve(idx + 1, temp)&#10;    solve(0, [])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>5</td>
      <td>Rec 03 Permutations<br><br></b> <a href='https://leetcode.com/problems/permutations/' target='_blank'>LeetCode 46</a></td>
      <td><b>Example 1:</b> Input: nums = [1,2,3], Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]</td>
      <td><b>Time:</b> O(N! * N)<br><b>Space:</b> O(N)</td>
      <td><code>std::swap</code></td>
      <td><b>Backtracking necessity:</b> Without the second swap (backtrack), the array remains mutated for subsequent sibling recursion branches.</td>
      <td><b>Explanation:</b> Backtracking. Swap elements to generate permutations. For index `i`, swap it with every index from `i` to `n-1`, recurse, then backtrack (swap back).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def permute(nums: list[int]) -&gt; list[list[int]]:&#10;    ans = []&#10;    def solve(idx):&#10;        if idx == len(nums):&#10;            ans.append(nums[:])&#10;            return&#10;        for i in range(idx, len(nums)):&#10;            nums[idx], nums[i] = nums[i], nums[idx]&#10;            solve(idx + 1)&#10;            nums[idx], nums[i] = nums[i], nums[idx]&#10;    solve(0)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>6</td>
      <td>Rec 06 N Queens<br><br></b> <a href='https://leetcode.com/problems/n-queens/' target='_blank'>LeetCode 51</a></td>
      <td><b>Example 1:</b> Classic N-Queens constraint satisfaction.</td>
      <td><b>Time:</b> O(N!)<br><b>Space:</b> O(N^2)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Backtracking. Place queen column by column. To optimize collision checking to O(1), use 3 arrays/hashmaps: `leftRow`, `upperDiagonal`, and `lowerDiagonal`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def solveNQueens(n: int) -&gt; List[List[str]]:&#10;    ans = []&#10;    board = [[&#x27;.&#x27;] * n for _ in range(n)]&#10;    leftRow, upperDiag, lowerDiag = [0]*n, [0]*(2*n-1), [0]*(2*n-1)&#10;    def solve(col):&#10;        if col == n:&#10;            ans.append([&#x27;&#x27;.join(row) for row in board])&#10;            return&#10;        for row in range(n):&#10;            if leftRow[row] == 0 and lowerDiag[row + col] == 0 and upperDiag[n - 1 + col - row] == 0:&#10;                board[row][col] = &#x27;Q&#x27;&#10;                leftRow[row] = 1; lowerDiag[row + col] = 1; upperDiag[n - 1 + col - row] = 1&#10;                solve(col + 1)&#10;                board[row][col] = &#x27;.&#x27;&#10;                leftRow[row] = 0; lowerDiag[row + col] = 0; upperDiag[n - 1 + col - row] = 0&#10;    solve(0)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>7</td>
      <td>Rec 07 Sudoku Solver<br><br></b> <a href='https://leetcode.com/problems/sudoku-solver/' target='_blank'>LeetCode 37</a></td>
      <td><b>Example 1:</b> Input: board with '.' for empty cells. Solve in-place.</td>
      <td><b>Time:</b> O(9^(n*n))<br><b>Space:</b> O(1) auxiliary</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Backtracking. Find first empty cell, try placing 1-9. Validate row, col, and 3x3 sub-grid. Recursively solve the rest. If it fails, backtrack.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def solveSudoku(board: List[List[str]]) -&gt; None:&#10;    def isValid(row, col, ch):&#10;        for i in range(9):&#10;            if board[i][col] == ch: return False&#10;            if board[row][i] == ch: return False&#10;            if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == ch: return False&#10;        return True&#10;    def solve():&#10;        for i in range(len(board)):&#10;            for j in range(len(board[0])):&#10;                if board[i][j] == &#x27;.&#x27;:&#10;                    for c in &#x27;123456789&#x27;:&#10;                        if isValid(i, j, c):&#10;                            board[i][j] = c&#10;                            if solve(): return True&#10;                            else: board[i][j] = &#x27;.&#x27;&#10;                    return False&#10;        return True&#10;    solve()</code></pre></details></td>
    </tr>
    <tr>
      <td>8</td>
      <td>Rec 08 M Coloring Problem<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/m-coloring-problem-1587115620/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Return true if possible.</td>
      <td><b>Time:</b> O(M^N)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Backtracking. Try coloring each node with color 1 to m. For a color, check if any adjacent node has the same color. If safe, assign and recurse for next node. If recursion returns false, backtrack.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def graphColoring(graph: List[List[int]], m: int, n: int) -&gt; bool:&#10;    color = [0] * n&#10;    def isSafe(node, col):&#10;        for k in range(n):&#10;            if k != node and graph[k][node] == 1 and color[k] == col: return False&#10;        return True&#10;    def solve(node):&#10;        if node == n: return True&#10;        for i in range(1, m + 1):&#10;            if isSafe(node, i):&#10;                color[node] = i&#10;                if solve(node + 1): return True&#10;                color[node] = 0&#10;        return False&#10;    return solve(0)</code></pre></details></td>
    </tr>
    <tr>
      <td>9</td>
      <td>Rec 09 Rat In A Maze<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Lexicographical order paths.</td>
      <td><b>Time:</b> O(4^(N*N))<br><b>Space:</b> O(N*N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Backtracking. Explore 4 directions (D, L, R, U) in lexicographical order to get sorted paths naturally. Mark cell as visited, recurse, then unmark (backtrack).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findPath(m: List[List[int]], n: int) -&gt; List[str]:&#10;    ans = []&#10;    vis = [[0 for _ in range(n)] for _ in range(n)]&#10;    di = [1, 0, 0, -1]&#10;    dj = [0, -1, 1, 0]&#10;    dir_str = &quot;DLRU&quot;&#10;    def solve(i, j, move):&#10;        if i == n - 1 and j == n - 1:&#10;            ans.append(move)&#10;            return&#10;        for ind in range(4):&#10;            nexti, nextj = i + di[ind], j + dj[ind]&#10;            if 0 &lt;= nexti &lt; n and 0 &lt;= nextj &lt; n and not vis[nexti][nextj] and m[nexti][nextj] == 1:&#10;                vis[i][j] = 1&#10;                solve(nexti, nextj, move + dir_str[ind])&#10;                vis[i][j] = 0&#10;    if m[0][0] == 1: solve(0, 0, &quot;&quot;)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>10</td>
      <td>Rec 10 Word Break<br><br></b> <a href='https://leetcode.com/problems/word-break/' target='_blank'>LeetCode 139</a></td>
      <td><b>Example 1:</b> Input: s = 'leetcode', wordDict = ['leet','code'], Output: true</td>
      <td><b>Time:</b> O(N^3)<br><b>Space:</b> O(N)</td>
      <td><code>#include <unordered_set></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Recursion with Memoization (or DP). For each index, try all possible word lengths. If a prefix exists in dict, recurse for the suffix. DP array `dp[i]` stores if `s[0...i-1]` is valid.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def wordBreak(s: str, wordDict: List[str]) -&gt; bool:&#10;    word_set = set(wordDict)&#10;    dp = [False] * (len(s) + 1)&#10;    dp[0] = True&#10;    for i in range(1, len(s) + 1):&#10;        for j in range(i):&#10;            if dp[j] and s[j:i] in word_set:&#10;                dp[i] = True&#10;                break&#10;    return dp[-1]</code></pre></details></td>
    </tr>
    <tr>
      <td>11</td>
      <td>Rec 11 Word Break Ii<br><br></b> <a href='https://leetcode.com/problems/word-break-ii/' target='_blank'>LeetCode 140</a></td>
      <td><b>Example 1:</b> Return list of sentences.</td>
      <td><b>Time:</b> O(2^N)<br><b>Space:</b> O(2^N)</td>
      <td><code>#include <unordered_set></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Backtracking. Generate all combinations. At each step, if a prefix is in dict, recursively call for the rest of the string and append the prefix to the result of the recursive call.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def wordBreak(s: str, wordDict: List[str]) -&gt; List[str]:&#10;    word_set = set(wordDict)&#10;    memo = {}&#10;    def solve(s):&#10;        if s in memo: return memo[s]&#10;        if not s: return [&quot;&quot;]&#10;        res = []&#10;        for i in range(1, len(s) + 1):&#10;            word = s[:i]&#10;            if word in word_set:&#10;                rem = solve(s[i:])&#10;                for st in rem:&#10;                    res.append(word + (&quot; &quot; if st else &quot;&quot;) + st)&#10;        memo[s] = res&#10;        return res&#10;    return solve(s)</code></pre></details></td>
    </tr>
    <tr>
      <td>12</td>
      <td>Rec 12 Palindrome Partitioning<br><br></b> <a href='https://leetcode.com/problems/palindrome-partitioning/' target='_blank'>LeetCode 131</a></td>
      <td><b>Example 1:</b> Input: s = 'aab', Output: [['a','a','b'],['aa','b']]</td>
      <td><b>Time:</b> O(N * 2^N)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Backtracking. Try to partition the string at every index. If the prefix `s[start:i]` is a palindrome, add it to current path and recurse for the rest of the string `s[i:end]`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def partition(s: str) -&gt; List[List[str]]:&#10;    res = []&#10;    path = []&#10;    def isPalindrome(s, start, end):&#10;        while start &lt;= end:&#10;            if s[start] != s[end]: return False&#10;            start += 1; end -= 1&#10;        return True&#10;    def solve(index):&#10;        if index == len(s):&#10;            res.append(list(path))&#10;            return&#10;        for i in range(index, len(s)):&#10;            if isPalindrome(s, index, i):&#10;                path.append(s[index:i+1])&#10;                solve(i + 1)&#10;                path.pop()&#10;    solve(0)&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td>13</td>
      <td>Rec 13 Expression Add Operators<br><br></b> <a href='https://leetcode.com/problems/expression-add-operators/' target='_blank'>LeetCode 282</a></td>
      <td><b>Example 1:</b> Return expressions.</td>
      <td><b>Time:</b> O(N * 4^N)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Backtracking. Keep track of the evaluated sum so far, and the previous operand (for multiplication precedence). For '*', `newSum = sum - prev + prev * curr`. Handle leading zeros.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def addOperators(num: str, target: int) -&gt; List[str]:&#10;    ans = []&#10;    def solve(ind, path, eval_sum, multed):&#10;        if ind == len(num):&#10;            if eval_sum == target: ans.append(path)&#10;            return&#10;        for i in range(ind, len(num)):&#10;            if i != ind and num[ind] == &#x27;0&#x27;: break&#10;            cur_str = num[ind:i+1]&#10;            cur_num = int(cur_str)&#10;            if ind == 0:&#10;                solve(i + 1, path + cur_str, cur_num, cur_num)&#10;            else:&#10;                solve(i + 1, path + &quot;+&quot; + cur_str, eval_sum + cur_num, cur_num)&#10;                solve(i + 1, path + &quot;-&quot; + cur_str, eval_sum - cur_num, -cur_num)&#10;                solve(i + 1, path + &quot;*&quot; + cur_str, eval_sum - multed + multed * cur_num, multed * cur_num)&#10;    solve(0, &quot;&quot;, 0, 0)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>14</td>
      <td>Rec 14 Subset Sums Ii<br><br></b> <a href='https://leetcode.com/problems/subsets-ii/' target='_blank'>LeetCode 90</a></td>
      <td><b>Example 1:</b> Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]</td>
      <td><b>Time:</b> O(2^N * N)<br><b>Space:</b> O(2^N * N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Sort array first to bring duplicates together. In recursive call, loop from `ind` to `n`. If `i > ind` and `nums[i] == nums[i-1]`, `continue` to skip duplicate recursive branches.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def subsetsWithDup(nums: List[int]) -&gt; List[List[int]]:&#10;    ans = []&#10;    nums.sort()&#10;    def findSubsets(ind, ds):&#10;        ans.append(list(ds))&#10;        for i in range(ind, len(nums)):&#10;            if i != ind and nums[i] == nums[i-1]: continue&#10;            ds.append(nums[i])&#10;            findSubsets(i + 1, ds)&#10;            ds.pop()&#10;    findSubsets(0, [])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>15</td>
      <td>Rec 15 Combination Sum Ii<br><br></b> <a href='https://leetcode.com/problems/combination-sum-ii/' target='_blank'>LeetCode 40</a></td>
      <td><b>Example 1:</b> Return unique combinations.</td>
      <td><b>Time:</b> O(2^N * k)<br><b>Space:</b> O(k * x)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Sort the array. Recursive function iterates from `ind` to `n`. Skip duplicates (`if i > ind and arr[i] == arr[i-1]`). If `arr[i] > target`, break. Else add to path, subtract from target, and recurse.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def combinationSum2(candidates: List[int], target: int) -&gt; List[List[int]]:&#10;    ans = []&#10;    candidates.sort()&#10;    def findCombinations(ind, target, ds):&#10;        if target == 0:&#10;            ans.append(list(ds))&#10;            return&#10;        for i in range(ind, len(candidates)):&#10;            if i &gt; ind and candidates[i] == candidates[i-1]: continue&#10;            if candidates[i] &gt; target: break&#10;            ds.append(candidates[i])&#10;            findCombinations(i + 1, target - candidates[i], ds)&#10;            ds.pop()&#10;    findCombinations(0, target, [])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>16</td>
      <td>Rec 16 Combination Sum Iii<br><br></b> <a href='https://leetcode.com/problems/combination-sum-iii/' target='_blank'>LeetCode 216</a></td>
      <td><b>Example 1:</b> Return combinations.</td>
      <td><b>Time:</b> O(2^9)<br><b>Space:</b> O(k)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Backtracking. Start from 1, go up to 9. Add the current number to the path and subtract from target. Stop when path size is `k` and `target` is 0.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def combinationSum3(k: int, n: int) -&gt; List[List[int]]:&#10;    ans = []&#10;    def solve(start, k, n, ds):&#10;        if k == 0 and n == 0:&#10;            ans.append(list(ds))&#10;            return&#10;        if k == 0 or n &lt; 0: return&#10;        for i in range(start, 10):&#10;            ds.append(i)&#10;            solve(i + 1, k - 1, n - i, ds)&#10;            ds.pop()&#10;    solve(1, k, n, [])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>17</td>
      <td>Rec 17 Letter Combinations Of A Phone Number<br><br></b> <a href='https://leetcode.com/problems/letter-combinations-of-a-phone-number/' target='_blank'>LeetCode 17</a></td>
      <td><b>Example 1:</b> String combinations.</td>
      <td><b>Time:</b> O(4^N * N)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Backtracking. Create a mapping of digit to letters. Iterate through digits, for each digit loop through its mapped letters, append to current string, and recurse.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def letterCombinations(digits: str) -&gt; List[str]:&#10;    if not digits: return []&#10;    ans = []&#10;    mapping = [&quot;&quot;, &quot;&quot;, &quot;abc&quot;, &quot;def&quot;, &quot;ghi&quot;, &quot;jkl&quot;, &quot;mno&quot;, &quot;pqrs&quot;, &quot;tuv&quot;, &quot;wxyz&quot;]&#10;    def solve(ind, path):&#10;        if ind == len(digits):&#10;            ans.append(path)&#10;            return&#10;        number = int(digits[ind])&#10;        value = mapping[number]&#10;        for i in range(len(value)):&#10;            solve(ind + 1, path + value[i])&#10;    solve(0, &quot;&quot;)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>18</td>
      <td>Rec 18 Rat In A Maze<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Backtracking.</td>
      <td><b>Time:</b> O(4^(N^2))<br><b>Space:</b> O(N^2)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Use backtracking to explore paths in lexicographical order: Down, Left, Right, Up (DLRU). Maintain a visited array. If destination is reached, add path to answers. Backtrack by unmarking visited.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findPath(m: List[List[int]], n: int) -&gt; List[str]:&#10;    ans = []&#10;    vis = [[0 for _ in range(n)] for _ in range(n)]&#10;    di = [1, 0, 0, -1]&#10;    dj = [0, -1, 1, 0]&#10;    direction = &quot;DLRU&quot;&#10;    def solve(i, j, move):&#10;        if i == n - 1 and j == n - 1:&#10;            ans.append(move)&#10;            return&#10;        for ind in range(4):&#10;            nexti = i + di[ind]&#10;            nextj = j + dj[ind]&#10;            if 0 &lt;= nexti &lt; n and 0 &lt;= nextj &lt; n and not vis[nexti][nextj] and m[nexti][nextj] == 1:&#10;                vis[i][j] = 1&#10;                solve(nexti, nextj, move + direction[ind])&#10;                vis[i][j] = 0&#10;    if m[0][0] == 1: solve(0, 0, &quot;&quot;)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>19</td>
      <td>Rec 19 Word Break Ii<br><br></b> <a href='https://leetcode.com/problems/word-break-ii/' target='_blank'>LeetCode 140</a></td>
      <td><b>Example 1:</b> Recursion + Memoization.</td>
      <td><b>Time:</b> O(N * 2^N)<br><b>Space:</b> O(2^N * N)</td>
      <td><code>#include <unordered_set>\n#include <unordered_map></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Backtracking. For each index, try all possible prefixes. If prefix is in dict, recursively break the remaining string. Use memoization or DP to store answers for a substring to avoid recomputation.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def wordBreak(s: str, wordDict: List[str]) -&gt; List[str]:&#10;    wordSet = set(wordDict)&#10;    memo = {}&#10;    def dfs(s):&#10;        if s in memo: return memo[s]&#10;        res = []&#10;        if s in wordSet: res.append(s)&#10;        for i in range(1, len(s)):&#10;            right = s[i:]&#10;            if right in wordSet:&#10;                left_res = dfs(s[:i])&#10;                for l in left_res:&#10;                    res.append(l + &quot; &quot; + right)&#10;        memo[s] = res&#10;        return res&#10;    return dfs(s)</code></pre></details></td>
    </tr>
    <tr>
      <td>20</td>
      <td>Rec 20 M Coloring Problem<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/m-coloring-problem-1587115620/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Graph coloring backtracking.</td>
      <td><b>Time:</b> O(M^N)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Try coloring each node from `1` to `M`. Before coloring, check if it's safe (no adjacent node has same color). If safe, color it and recurse for next node. Backtrack if no color works.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def graphColoring(graph, m, V):&#10;    color = [0] * V&#10;    def isSafe(node, col):&#10;        for k in range(V):&#10;            if k != node and graph[k][node] == 1 and color[k] == col:&#10;                return False&#10;        return True&#10;    def solve(node):&#10;        if node == V: return True&#10;        for i in range(1, m + 1):&#10;            if isSafe(node, i):&#10;                color[node] = i&#10;                if solve(node + 1): return True&#10;                color[node] = 0&#10;        return False&#10;    return solve(0)</code></pre></details></td>
    </tr>
    <tr>
      <td>21</td>
      <td>Rec 21 Sudoku Solver<br><br></b> <a href='https://leetcode.com/problems/sudoku-solver/' target='_blank'>LeetCode 37</a></td>
      <td><b>Example 1:</b> Classic backtracking.</td>
      <td><b>Time:</b> O(9^(N^2))<br><b>Space:</b> O(N^2)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Iterate through matrix. If empty, try '1' to '9'. Check `isValid` (row, col, 3x3 box). If valid, set it and recurse. If recursion returns true, puzzle solved. Else backtrack. If loop ends without returning true, return false.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def solveSudoku(board: List[List[str]]) -&gt; None:&#10;    def is_valid(r, c, ch):&#10;        for i in range(9):&#10;            if board[i][c] == ch: return False&#10;            if board[r][i] == ch: return False&#10;            if board[3 * (r // 3) + i // 3][3 * (c // 3) + i % 3] == ch: return False&#10;        return True&#10;    def solve():&#10;        for i in range(9):&#10;            for j in range(9):&#10;                if board[i][j] == &#x27;.&#x27;:&#10;                    for ch in &#x27;123456789&#x27;:&#10;                        if is_valid(i, j, ch):&#10;                            board[i][j] = ch&#10;                            if solve(): return True&#10;                            board[i][j] = &#x27;.&#x27;&#10;                    return False&#10;        return True&#10;    solve()</code></pre></details></td>
    </tr>
    <tr>
      <td>22</td>
      <td>Rec 22 N Queens<br><br></b> <a href='https://leetcode.com/problems/n-queens/' target='_blank'>LeetCode 51</a></td>
      <td><b>Example 1:</b> Backtracking on board.</td>
      <td><b>Time:</b> O(N!)<br><b>Space:</b> O(N^2)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Place queens column by column. Keep track of safe rows and diagonals using hashing arrays: `leftRow`, `lowerDiagonal`, `upperDiagonal`. If safe, place queen, update hashes, and recurse.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def solveNQueens(n: int) -&gt; List[List[str]]:&#10;    ans = []&#10;    board = [[&quot;.&quot;] * n for _ in range(n)]&#10;    leftRow = [0] * n&#10;    upperDiagonal = [0] * (2 * n - 1)&#10;    lowerDiagonal = [0] * (2 * n - 1)&#10;    def solve(col):&#10;        if col == n:&#10;            ans.append([&quot;&quot;.join(r) for r in board])&#10;            return&#10;        for row in range(n):&#10;            if leftRow[row] == 0 and lowerDiagonal[row + col] == 0 and upperDiagonal[n - 1 + col - row] == 0:&#10;                board[row][col] = &#x27;Q&#x27;&#10;                leftRow[row] = 1; lowerDiagonal[row + col] = 1; upperDiagonal[n - 1 + col - row] = 1&#10;                solve(col + 1)&#10;                board[row][col] = &#x27;.&#x27;&#10;                leftRow[row] = 0; lowerDiagonal[row + col] = 0; upperDiagonal[n - 1 + col - row] = 0&#10;    solve(0)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>23</td>
      <td>Rec 23 Permutations Of A String Or Array<br><br></b> <a href='https://leetcode.com/problems/permutations/' target='_blank'>LeetCode 46</a></td>
      <td><b>Example 1:</b> Backtracking swap.</td>
      <td><b>Time:</b> O(N! * N)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Iterate `i` from `index` to `n-1`. Swap `nums[index]` and `nums[i]`, then recurse for `index + 1`. Swap back to backtrack.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def permute(nums: List[int]) -&gt; List[List[int]]:&#10;    ans = []&#10;    def recur(index):&#10;        if index == len(nums):&#10;            ans.append(nums[:])&#10;            return&#10;        for i in range(index, len(nums)):&#10;            nums[index], nums[i] = nums[i], nums[index]&#10;            recur(index + 1)&#10;            nums[index], nums[i] = nums[i], nums[index]&#10;    recur(0)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>24</td>
      <td>Rec 24 Combination Sum Ii<br><br></b> <a href='https://leetcode.com/problems/combination-sum-ii/' target='_blank'>LeetCode 40</a></td>
      <td><b>Example 1:</b> `candidates = [10,1,2,7,6,1,5], target = 8`.</td>
      <td><b>Time:</b> O(2^N)<br><b>Space:</b> O(N * X) where X is number of combinations</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Sort candidates. Recursively pick combinations. If `i > ind` and `candidates[i] == candidates[i-1]`, skip to avoid duplicates. If `target - candidates[i] >= 0`, pick it.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def combinationSum2(candidates: List[int], target: int) -&gt; List[List[int]]:&#10;    candidates.sort()&#10;    ans = []&#10;    def find(ind, target, ds):&#10;        if target == 0:&#10;            ans.append(list(ds))&#10;            return&#10;        for i in range(ind, len(candidates)):&#10;            if i &gt; ind and candidates[i] == candidates[i-1]: continue&#10;            if candidates[i] &gt; target: break&#10;            ds.append(candidates[i])&#10;            find(i + 1, target - candidates[i], ds)&#10;            ds.pop()&#10;    find(0, target, [])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>25</td>
      <td>Rec 25 Subset Sum I<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/subset-sums2234/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Take / Not Take.</td>
      <td><b>Time:</b> O(2^N)<br><b>Space:</b> O(2^N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Recursively either include `arr[ind]` in sum, or exclude it. If `ind == N`, add `sum` to result array.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def subsetSums(arr: List[int], N: int) -&gt; List[int]:&#10;    sumSubset = []&#10;    def func(ind, current_sum):&#10;        if ind == N:&#10;            sumSubset.append(current_sum)&#10;            return&#10;        func(ind + 1, current_sum + arr[ind])&#10;        func(ind + 1, current_sum)&#10;    func(0, 0)&#10;    sumSubset.sort()&#10;    return sumSubset</code></pre></details></td>
    </tr>
    <tr>
      <td>26</td>
      <td>Rec 26 Subset Sum Ii<br><br></b> <a href='https://leetcode.com/problems/subsets-ii/' target='_blank'>LeetCode 90</a></td>
      <td><b>Example 1:</b> Subset skip duplicates.</td>
      <td><b>Time:</b> O(2^N * N)<br><b>Space:</b> O(2^N * K)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Sort array. Recursive call adds current `ds` to `ans`. Then iterate `i` from `ind` to `n`. Skip if `i > ind` and `nums[i] == nums[i-1]`. Add to `ds`, recurse for `i+1`, pop from `ds`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def subsetsWithDup(nums: List[int]) -&gt; List[List[int]]:&#10;    ans = []&#10;    nums.sort()&#10;    def find(ind, ds):&#10;        ans.append(list(ds))&#10;        for i in range(ind, len(nums)):&#10;            if i != ind and nums[i] == nums[i-1]: continue&#10;            ds.append(nums[i])&#10;            find(i + 1, ds)&#10;            ds.pop()&#10;    find(0, [])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>27</td>
      <td>Rec 27 Palindrome Partitioning<br><br></b> <a href='https://leetcode.com/problems/palindrome-partitioning/' target='_blank'>LeetCode 131</a></td>
      <td><b>Example 1:</b> Valid palindrome checks on prefix.</td>
      <td><b>Time:</b> O(N * 2^N)<br><b>Space:</b> O(N * X)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Recurse through string. For index `i`, check substring `s[index...i]`. If it is palindrome, add it to current list, and recurse for `i+1`. Backtrack after recursion.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def partition(s: str) -&gt; List[List[str]]:&#10;    res = []&#10;    def isPal(string, l, r):&#10;        while l &lt;= r:&#10;            if string[l] != string[r]: return False&#10;            l += 1; r -= 1&#10;        return True&#10;    def func(index, path):&#10;        if index == len(s):&#10;            res.append(list(path))&#10;            return&#10;        for i in range(index, len(s)):&#10;            if isPal(s, index, i):&#10;                path.append(s[index:i+1])&#10;                func(i + 1, path)&#10;                path.pop()&#10;    func(0, [])&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td>28</td>
      <td>Recursion 27 N Queens Ii<br><br></b> <a href='https://leetcode.com/problems/n-queens-ii/' target='_blank'>LeetCode 52</a></td>
      <td><b>Example 1:</b> Backtracking with hashing.</td>
      <td><b>Time:</b> O(N!)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Use backtracking to place queens column by column. Use three hash arrays (or bitmasks) to track attacked rows, upper diagonals, and lower diagonals. If placing a queen is safe, update hashes, recurse for next column, and then backtrack.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def totalNQueens(n: int) -&gt; int:&#10;    count = 0&#10;    leftRow = [0] * n&#10;    upperDiag = [0] * (2 * n - 1)&#10;    lowerDiag = [0] * (2 * n - 1)&#10;    def solve(col):&#10;        nonlocal count&#10;        if col == n:&#10;            count += 1&#10;            return&#10;        for row in range(n):&#10;            if leftRow[row] == 0 and lowerDiag[row + col] == 0 and upperDiag[n - 1 + col - row] == 0:&#10;                leftRow[row] = 1&#10;                lowerDiag[row + col] = 1&#10;                upperDiag[n - 1 + col - row] = 1&#10;                solve(col + 1)&#10;                leftRow[row] = 0&#10;                lowerDiag[row + col] = 0&#10;                upperDiag[n - 1 + col - row] = 0&#10;    solve(0)&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td>29</td>
      <td>Recursion 28 Sudoku Solver<br><br></b> <a href='https://leetcode.com/problems/sudoku-solver/' target='_blank'>LeetCode 37</a></td>
      <td><b>Example 1:</b> Backtracking.</td>
      <td><b>Time:</b> O(9^(n*n))<br><b>Space:</b> O(1) excluding recursion stack</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Iterate through each cell. If it's empty, try placing digits '1' to '9'. For each digit, check if it's valid in its row, column, and 3x3 subgrid. If valid, place it and recursively try to solve the rest. If a path leads to a solution, return true. Otherwise, backtrack (remove digit).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def solveSudoku(board: List[List[str]]) -&gt; None:&#10;    def isValid(row, col, c):&#10;        for i in range(9):&#10;            if board[i][col] == c: return False&#10;            if board[row][i] == c: return False&#10;            if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == c: return False&#10;        return True&#10;    def solve():&#10;        for i in range(len(board)):&#10;            for j in range(len(board[0])):&#10;                if board[i][j] == &#x27;.&#x27;:&#10;                    for c in map(str, range(1, 10)):&#10;                        if isValid(i, j, c):&#10;                            board[i][j] = c&#10;                            if solve(): return True&#10;                            board[i][j] = &#x27;.&#x27;&#10;                    return False&#10;        return True&#10;    solve()</code></pre></details></td>
    </tr>
    <tr>
      <td>30</td>
      <td>Recursion 29 Word Search<br><br></b> <a href='https://leetcode.com/problems/word-search/' target='_blank'>LeetCode 79</a></td>
      <td><b>Example 1:</b> Backtracking DFS.</td>
      <td><b>Time:</b> O(N * M * 4^L)<br><b>Space:</b> O(L) recursion stack</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Start DFS from each cell that matches the first letter of the word. In DFS, check 4 neighbors. Mark current cell as visited (e.g. change to '#') before moving to neighbors, and unmark (backtrack) after exploring.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def exist(board: List[List[str]], word: str) -&gt; bool:&#10;    def dfs(i, j, idx):&#10;        if idx == len(word): return True&#10;        if i &lt; 0 or i &gt;= len(board) or j &lt; 0 or j &gt;= len(board[0]) or board[i][j] != word[idx]:&#10;            return False&#10;        temp = board[i][j]&#10;        board[i][j] = &#x27;#&#x27;&#10;        found = (dfs(i+1, j, idx+1) or dfs(i-1, j, idx+1) or&#10;                 dfs(i, j+1, idx+1) or dfs(i, j-1, idx+1))&#10;        board[i][j] = temp&#10;        return found&#10;    for i in range(len(board)):&#10;        for j in range(len(board[0])):&#10;            if board[i][j] == word[0] and dfs(i, j, 0):&#10;                return True&#10;    return False</code></pre></details></td>
    </tr>
    <tr>
      <td>31</td>
      <td>Recursion 30 Palindrome Partitioning<br><br></b> <a href='https://leetcode.com/problems/palindrome-partitioning/' target='_blank'>LeetCode 131</a></td>
      <td><b>Example 1:</b> Backtracking.</td>
      <td><b>Time:</b> O(N * 2^N)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Iterate through the string. If a prefix is a palindrome, add it to the current partition list, and recursively partition the remaining substring. When we reach the end of the string, add the current partition to the result.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def partition(s: str) -&gt; List[List[str]]:&#10;    def is_palindrome(sub):&#10;        return sub == sub[::-1]&#10;    res = []&#10;    def solve(idx, path):&#10;        if idx == len(s):&#10;            res.append(path[:])&#10;            return&#10;        for i in range(idx, len(s)):&#10;            if is_palindrome(s[idx:i+1]):&#10;                path.append(s[idx:i+1])&#10;                solve(i+1, path)&#10;                path.pop()&#10;    solve(0, [])&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td>32</td>
      <td>Recursion 31 Rat In A Maze Problem I<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Backtracking DFS.</td>
      <td><b>Time:</b> O(4^(N*N))<br><b>Space:</b> O(N*N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Start DFS from (0,0). Try D, L, R, U sequentially. If valid and not visited, mark visited, append direction to path, recurse, then unmark (backtrack) and pop direction. If reached (N-1, N-1), add path to results.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findPath(m, n):&#10;    ans = []&#10;    vis = [[0 for _ in range(n)] for _ in range(n)]&#10;    dirs = &quot;DLRU&quot;&#10;    di = [1, 0, 0, -1]&#10;    dj = [0, -1, 1, 0]&#10;    def solve(i, j, move):&#10;        if i == n - 1 and j == n - 1:&#10;            ans.append(move)&#10;            return&#10;        for ind in range(4):&#10;            ni = i + di[ind]&#10;            nj = j + dj[ind]&#10;            if 0 &lt;= ni &lt; n and 0 &lt;= nj &lt; n and not vis[ni][nj] and m[ni][nj] == 1:&#10;                vis[i][j] = 1&#10;                solve(ni, nj, move + dirs[ind])&#10;                vis[i][j] = 0&#10;    if m[0][0] == 1:&#10;        solve(0, 0, &quot;&quot;)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>33</td>
      <td>Recursion 32 Word Break Ii<br><br></b> <a href='https://leetcode.com/problems/word-break-ii/' target='_blank'>LeetCode 140</a></td>
      <td><b>Example 1:</b> Backtracking with Memoization (optional, but good for optimization).</td>
      <td><b>Time:</b> O(N * 2^N)<br><b>Space:</b> O(N * 2^N)</td>
      <td><code>#include <unordered_set></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Iterate through all possible prefixes. If a prefix exists in the wordDict, recursively solve for the remaining suffix. Backtrack by appending the current prefix to the results of the suffix.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def wordBreak(s: str, wordDict: List[str]) -&gt; List[str]:&#10;    dict_set = set(wordDict)&#10;    res = []&#10;    def solve(idx, path):&#10;        if idx == len(s):&#10;            res.append(path[:-1])&#10;            return&#10;        temp = &quot;&quot;&#10;        for i in range(idx, len(s)):&#10;            temp += s[i]&#10;            if temp in dict_set:&#10;                solve(i + 1, path + temp + &quot; &quot;)&#10;    solve(0, &quot;&quot;)&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td>34</td>
      <td>Recursion 33 M Coloring Problem<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/m-coloring-problem-1587115620/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Backtracking.</td>
      <td><b>Time:</b> O(M^N)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Try coloring nodes one by one. For each node, try all M colors. Check if it's safe (no adjacent node has the same color). If safe, color it and recurse to the next node. If recursion returns true, we are done. Else backtrack and try next color.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def graphColoring(graph, m, n):&#10;    color = [0] * n&#10;    def isSafe(node, col):&#10;        for k in range(n):&#10;            if k != node and graph[k][node] == 1 and color[k] == col:&#10;                return False&#10;        return True&#10;    def solve(node):&#10;        if node == n: return True&#10;        for i in range(1, m + 1):&#10;            if isSafe(node, i):&#10;                color[node] = i&#10;                if solve(node + 1): return True&#10;                color[node] = 0&#10;        return False&#10;    return solve(0)</code></pre></details></td>
    </tr>
    <tr>
      <td>35</td>
      <td>Recursion 34 Expression Add Operators<br><br></b> <a href='https://leetcode.com/problems/expression-add-operators/' target='_blank'>LeetCode 282</a></td>
      <td><b>Example 1:</b> Backtracking with value and previous operand tracking.</td>
      <td><b>Time:</b> O(4^N)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Iterate through the string, extracting substrings as numbers. Prevent numbers with leading zeros. Recursively try `+`, `-`, `*`. For `*`, we must subtract the previous added value, and add `prev * current_val` to maintain precedence.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def addOperators(num: str, target: int) -&gt; List[str]:&#10;    res = []&#10;    def solve(idx, path, prevNum, currVal):&#10;        if idx == len(num):&#10;            if currVal == target: res.append(path)&#10;            return&#10;        s = &quot;&quot;&#10;        n = 0&#10;        for i in range(idx, len(num)):&#10;            if i &gt; idx and num[idx] == &#x27;0&#x27;: break&#10;            s += num[i]&#10;            n = n * 10 + int(num[i])&#10;            if idx == 0:&#10;                solve(i + 1, s, n, n)&#10;            else:&#10;                solve(i + 1, path + &quot;+&quot; + s, n, currVal + n)&#10;                solve(i + 1, path + &quot;-&quot; + s, -n, currVal - n)&#10;                solve(i + 1, path + &quot;*&quot; + s, prevNum * n, currVal - prevNum + prevNum * n)&#10;    solve(0, &quot;&quot;, 0, 0)&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td>36</td>
      <td>Recursion 35 K Th Symbol In Grammar<br><br></b> <a href='https://leetcode.com/problems/k-th-symbol-in-grammar/' target='_blank'>LeetCode 779</a></td>
      <td><b>Example 1:</b> Recursive division.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Row N has length 2^(N-1). The first half of row N is exactly same as row N-1. The second half of row N is the complement of row N-1. If k is in the first half (k <= mid), return solve(N-1, k). If k is in the second half, return !solve(N-1, k - mid).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def kthGrammar(n: int, k: int) -&gt; int:&#10;    if n == 1 and k == 1: return 0&#10;    mid = 2 ** (n - 2)&#10;    if k &lt;= mid:&#10;        return kthGrammar(n - 1, k)&#10;    else:&#10;        return 1 - kthGrammar(n - 1, k - mid)</code></pre></details></td>
    </tr>
    <tr>
      <td>37</td>
      <td>Recursion 36 Beautiful Arrangement<br><br></b> <a href='https://leetcode.com/problems/beautiful-arrangement/' target='_blank'>LeetCode 526</a></td>
      <td><b>Example 1:</b> Backtracking.</td>
      <td><b>Time:</b> O(K) where K is number of valid permutations<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Use an array to track visited numbers. Iterate from index 1 to n. For the current index, try placing an unvisited number. Check if the condition `(num % idx == 0 || idx % num == 0)` is met. If so, mark as visited, recurse to `idx + 1`, then backtrack.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def countArrangement(n: int) -&gt; int:&#10;    count = 0&#10;    visited = [0] * (n + 1)&#10;    def solve(idx):&#10;        nonlocal count&#10;        if idx &gt; n:&#10;            count += 1&#10;            return&#10;        for i in range(1, n + 1):&#10;            if not visited[i] and (i % idx == 0 or idx % i == 0):&#10;                visited[i] = 1&#10;                solve(idx + 1)&#10;                visited[i] = 0&#10;    solve(1)&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td>38</td>
      <td>Rec 38 Print All Permutations Of A String<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/permutations-of-a-given-string2041/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Recursive Backtracking.</td>
      <td><b>Time:</b> O(N! * N)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Convert string to char array and sort it. Use backtracking: pass a boolean visited array and a temporary string. If temporary string length equals original length, add to answer. Else, iterate through characters. To avoid duplicates, if `i > 0` and `s[i] == s[i-1]` and `!vis[i-1]`, skip. Otherwise, mark visited, append, recurse, unmark, pop.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def find_permutation(S: str) -&gt; List[str]:&#10;    S = sorted(list(S))&#10;    ans = []&#10;    vis = [False] * len(S)&#10;    def solve(curr):&#10;        if len(curr) == len(S):&#10;            ans.append(&quot;&quot;.join(curr))&#10;            return&#10;        for i in range(len(S)):&#10;            if vis[i] or (i &gt; 0 and S[i] == S[i-1] and not vis[i-1]):&#10;                continue&#10;            vis[i] = True&#10;            curr.append(S[i])&#10;            solve(curr)&#10;            curr.pop()&#10;            vis[i] = False&#10;    solve([])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>39</td>
      <td>Rec 39 Word Break Problem<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/word-break1352/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Recursive with Memoization.</td>
      <td><b>Time:</b> O(N^2 * L)<br><b>Space:</b> O(N)</td>
      <td><code>#include <unordered_set></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Use a helper function `solve(index)` that returns true if substring `s[index...]` can be segmented. Try all possible prefixes from `index`. If `s[index...i]` is in dict, recursively call `solve(i+1)`. Use memoization.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def wordBreak(A: str, B: List[str]) -&gt; int:&#10;    word_set = set(B)&#10;    memo = {}&#10;    def solve(ind):&#10;        if ind == len(A): return 1&#10;        if ind in memo: return memo[ind]&#10;        for i in range(ind, len(A)):&#10;            if A[ind:i+1] in word_set:&#10;                if solve(i + 1):&#10;                    memo[ind] = 1&#10;                    return 1&#10;        memo[ind] = 0&#10;        return 0&#10;    return solve(0)</code></pre></details></td>
    </tr>
    <tr>
      <td>40</td>
      <td>Rec 40 Remove Invalid Parentheses<br><br></b> <a href='https://leetcode.com/problems/remove-invalid-parentheses/' target='_blank'>LeetCode 301</a></td>
      <td><b>Example 1:</b> Recursion and Backtracking.</td>
      <td><b>Time:</b> O(2^N)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> First find the number of misplaced left (`rm_l`) and right (`rm_r`) parentheses. Then use backtracking to try removing `rm_l` and `rm_r` parentheses. To avoid duplicates, skip identical adjacent characters. Finally, check if the resulting string is valid.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def removeInvalidParentheses(s: str) -&gt; List[str]:&#10;    def is_valid(s):&#10;        count = 0&#10;        for c in s:&#10;            if c == &#x27;(&#x27;: count += 1&#10;            elif c == &#x27;)&#x27;: count -= 1&#10;            if count &lt; 0: return False&#10;        return count == 0&#10;    rm_l, rm_r = 0, 0&#10;    for c in s:&#10;        if c == &#x27;(&#x27;: rm_l += 1&#10;        elif c == &#x27;)&#x27;:&#10;            if rm_l &gt; 0: rm_l -= 1&#10;            else: rm_r += 1&#10;    ans = []&#10;    def solve(s, start, rm_l, rm_r):&#10;        if rm_l == 0 and rm_r == 0:&#10;            if is_valid(s): ans.append(s)&#10;            return&#10;        for i in range(start, len(s)):&#10;            if i != start and s[i] == s[i-1]: continue&#10;            if s[i] == &#x27;(&#x27; and rm_l &gt; 0:&#10;                solve(s[:i] + s[i+1:], i, rm_l - 1, rm_r)&#10;            elif s[i] == &#x27;)&#x27; and rm_r &gt; 0:&#10;                solve(s[:i] + s[i+1:], i, rm_l, rm_r - 1)&#10;    solve(s, 0, rm_l, rm_r)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>41</td>
      <td>Rec 41 Matchsticks To Square<br><br></b> <a href='https://leetcode.com/problems/matchsticks-to-square/' target='_blank'>LeetCode 473</a></td>
      <td><b>Example 1:</b> Backtracking to 4 subsets.</td>
      <td><b>Time:</b> O(4^N)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Calculate sum. If sum % 4 != 0, return false. Target side length is sum / 4. Sort matchsticks in descending order to optimize. Create an array `sides` of size 4. For each matchstick, try adding it to one of the 4 sides. If a side equals the target or is less, recurse.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def makesquare(matchsticks: List[int]) -&gt; bool:&#10;    total = sum(matchsticks)&#10;    if total % 4 != 0 or len(matchsticks) &lt; 4: return False&#10;    target = total // 4&#10;    matchsticks.sort(reverse=True)&#10;    sides = [0] * 4&#10;    def solve(ind):&#10;        if ind == len(matchsticks):&#10;            return sides[0] == sides[1] == sides[2] == target&#10;        for i in range(4):&#10;            if sides[i] + matchsticks[ind] &lt;= target:&#10;                sides[i] += matchsticks[ind]&#10;                if solve(ind + 1): return True&#10;                sides[i] -= matchsticks[ind]&#10;            if sides[i] == 0: break&#10;        return False&#10;    return solve(0)</code></pre></details></td>
    </tr>
    <tr>
      <td>42</td>
      <td>Rec 42 Tug Of War<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/tug-of-war/0' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Recursive Backtracking.</td>
      <td><b>Time:</b> O(2^N)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Keep track of the number of elements included in subset 1 and their sum. Recurse by including the current element in subset 1 or subset 2. Base case: if we reach end, check if subset 1 has `n/2` elements. If so, compute difference and update global minimum.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def tugOfWar(arr: List[int]) -&gt; int:&#10;    n = len(arr)&#10;    totalSum = sum(arr)&#10;    minDiff = [float(&#x27;inf&#x27;)]&#10;    def solve(ind, cnt, sum1):&#10;        if ind == n:&#10;            if cnt == n // 2:&#10;                sum2 = totalSum - sum1&#10;                minDiff[0] = min(minDiff[0], abs(sum1 - sum2))&#10;            return&#10;        if cnt &lt; n // 2:&#10;            solve(ind + 1, cnt + 1, sum1 + arr[ind])&#10;        solve(ind + 1, cnt, sum1)&#10;    solve(0, 0, 0)&#10;    return minDiff[0]</code></pre></details></td>
    </tr>
    <tr>
      <td>43</td>
      <td>Rec 43 Find Paths From Corner Cell To Middle Cell<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/paths-from-corner-to-middle/0' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> BFS / DFS for path finding.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N^2)</td>
      <td><code>#include <queue></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Perform BFS or DFS starting from all 4 corners simultaneously or individually. At each cell `(r, c)`, the jump size is `val = grid[r][c]`. We can move to `(r+val, c)`, `(r-val, c)`, `(r, c+val)`, `(r, c-val)`. Target is `(N/2, N/2)`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def solve(grid: List[List[int]]):&#10;    n = len(grid)&#10;    q = collections.deque([(0,0), (0,n-1), (n-1,0), (n-1,n-1)])&#10;    vis = set(q)&#10;    dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]&#10;    while q:&#10;        r, c = q.popleft()&#10;        if r == n // 2 and c == n // 2: return True&#10;        val = grid[r][c]&#10;        if val == 0: continue&#10;        for i in range(4):&#10;            nr, nc = r + dr[i] * val, c + dc[i] * val&#10;            if 0 &lt;= nr &lt; n and 0 &lt;= nc &lt; n and (nr, nc) not in vis:&#10;                vis.add((nr, nc))&#10;                q.append((nr, nc))&#10;    return False</code></pre></details></td>
    </tr>
    <tr>
      <td>44</td>
      <td>Rec 44 Arithmetic Expressions<br><br></b> <a href='https://www.hackerrank.com/challenges/arithmetic-expressions/problem' target='_blank'>HackerRank</a></td>
      <td><b>Example 1:</b> DP with path reconstruction.</td>
      <td><b>Time:</b> O(N * 101)<br><b>Space:</b> O(N * 101)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Use a DP table `dp[i][mod]` to store the operator used to reach remainder `mod` at index `i`. Iterate through the array, for each reachable mod from previous step, try `(mod + arr[i]) % 101`, `(mod - arr[i]) % 101`, `(mod * arr[i]) % 101`. Then backtrack from `dp[N-1][0]` to find the operators.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def arithmeticExpressions(arr: List[int]) -&gt; str:&#10;    n = len(arr)&#10;    dp = [[None] * 101 for _ in range(n)]&#10;    dp[0][arr[0] % 101] = (&#x27;&#x27;, 0)&#10;    for i in range(1, n):&#10;        for j in range(101):&#10;            if dp[i-1][j] is not None:&#10;                dp[i][(j + arr[i]) % 101] = (&#x27;+&#x27;, j)&#10;                dp[i][(j - arr[i] % 101 + 101) % 101] = (&#x27;-&#x27;, j)&#10;                dp[i][(j * arr[i]) % 101] = (&#x27;*&#x27;, j)&#10;    res = []&#10;    curr = 0&#10;    for i in range(n - 1, 0, -1):&#10;        op, prev_mod = dp[i][curr]&#10;        res.append(str(arr[i]))&#10;        res.append(op)&#10;        curr = prev_mod&#10;    res.append(str(arr[0]))&#10;    return &quot;&quot;.join(reversed(res))</code></pre></details></td>
    </tr>
    <tr>
      <td>45</td>
      <td>Rec 45 Find All Possible Palindromic Partitions Of A String<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/find-all-possible-palindromic-partitions-of-a-string/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Recursive Backtracking.</td>
      <td><b>Time:</b> O(N * 2^N)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Iterate through the string. Extract substring `S[ind..i]`. If it is a palindrome, add it to the current partition list and recursively call for `i+1`. When `ind == length`, push the partition list to the answer.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def allPalindromicPerms(S: str) -&gt; List[List[str]]:&#10;    ans = []&#10;    def is_pal(s): return s == s[::-1]&#10;    def solve(ind, curr):&#10;        if ind == len(S):&#10;            ans.append(curr[:])&#10;            return&#10;        for i in range(ind, len(S)):&#10;            sub = S[ind:i+1]&#10;            if is_pal(sub):&#10;                curr.append(sub)&#10;                solve(i + 1, curr)&#10;                curr.pop()&#10;    solve(0, [])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>46</td>
      <td>Rec 46 Partition Array To K Subsets<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/partition-array-to-k-subsets/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Recursive Backtracking.</td>
      <td><b>Time:</b> O(K * 2^N)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> If total sum is not divisible by K, return false. Sort array in descending order. Use a boolean array `vis`. Helper function `solve(ind, currentSum, k)`: if `k == 1` return true. If `currentSum == target`, `solve(0, 0, k-1)`. Otherwise, iterate from `ind` to `N`, if `!vis[i]` and `currentSum + arr[i] <= target`, mark `vis[i] = true`, recurse, unmark.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isKPartitionPossible(a: List[int], n: int, k: int) -&gt; bool:&#10;    total = sum(a)&#10;    if total % k != 0 or n &lt; k: return False&#10;    target = total // k&#10;    vis = [False] * n&#10;    def solve(ind, currSum, k):&#10;        if k == 1: return True&#10;        if currSum == target: return solve(0, 0, k - 1)&#10;        for i in range(ind, n):&#10;            if not vis[i] and currSum + a[i] &lt;= target:&#10;                vis[i] = True&#10;                if solve(i + 1, currSum + a[i], k): return True&#10;                vis[i] = False&#10;        return False&#10;    return solve(0, 0, k)</code></pre></details></td>
    </tr>
    <tr>
      <td>47</td>
      <td>Rec 47 Longest Possible Route In A Matrix With Hurdles<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/longest-possible-route-in-a-matrix-with-hurdles/0' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Recursive Backtracking.</td>
      <td><b>Time:</b> O(4^(N*M))<br><b>Space:</b> O(N*M)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Use a global `max_dist` or pass it by reference. In `solve(r, c, dist)`, if `(r, c) == (dest_r, dest_c)`, `max_dist = max(max_dist, dist)` and return. Mark `(r, c)` as visited. Explore 4 directions. Unmark `(r, c)`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def longestPath(mat: List[List[int]], xs: int, ys: int, xd: int, yd: int) -&gt; int:&#10;    if mat[xs][ys] == 0 or mat[xd][yd] == 0: return -1&#10;    maxDist = [-1]&#10;    n, m = len(mat), len(mat[0])&#10;    def solve(r, c, dist):&#10;        if r == xd and c == yd:&#10;            maxDist[0] = max(maxDist[0], dist)&#10;            return&#10;        mat[r][c] = 0&#10;        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:&#10;            if 0 &lt;= nr &lt; n and 0 &lt;= nc &lt; m and mat[nr][nc] == 1:&#10;                solve(nr, nc, dist + 1)&#10;        mat[r][c] = 1&#10;    solve(xs, ys, 0)&#10;    return maxDist[0]</code></pre></details></td>
    </tr>
  </tbody>
</table>
