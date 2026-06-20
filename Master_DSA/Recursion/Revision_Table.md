# Recursion Revision Table

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
      <td>Rec 01 Combination Sum<br><br></b> <a href="https://leetcode.com/problems/combination-sum/" target="_blank">LeetCode 39</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: candidates = [2,3,6,7], target = 7, Output: [[2,2,3],[7]]<br><br>**Note (Constraint):** The same number may be chosen unlimited number of times.</td>
      <td><b>Time:</b> O(2<sup>T</sup>) (Trade-off)<br><b>Space:</b> O(T) (Trade-off)</td>
      <td><b>Explanation:</b> Pick/Non-Pick but when picking, we *do not* increment the index `i`, allowing the same element to be picked infinitely until `target < 0`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def combination_sum(candidates: list[int], target: int) -&gt; list[list[int]]:&#10;    ans = []&#10;    def solve(i, current_target, temp):&#10;        if i == len(candidates):&#10;            if current_target == 0:&#10;                ans.append(temp.copy())&#10;            return&#10;            &#10;        if candidates[i] &lt;= current_target:&#10;            temp.append(candidates[i])&#10;            solve(i, current_target - candidates[i], temp)&#10;            temp.pop()&#10;            &#10;        solve(i + 1, current_target, temp)&#10;        &#10;    solve(0, target, [])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>2</td>
      <td>Rec 02 N Queens<br><br></b> <a href="https://leetcode.com/problems/n-queens/" target="_blank">LeetCode 51</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: n = 4, Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]<br><br>**Note (Constraint):** 1 &le; n &le; 9</td>
      <td><b>Time:</b> O(N!) (Constraint)<br><b>Space:</b> O(N) (Constraint)</td>
      <td><b>Explanation:</b> Backtracking. Try placing a queen in each row of the current column. Use `O(1)` lookups (Hashing logic) via arrays to check if row/diagonals are safe.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def solve_n_queens(n: int) -&gt; list[list[str]]:&#10;    ans = []&#10;    board = [[&quot;.&quot;] * n for _ in range(n)]&#10;    left_row = [0] * n&#10;    upper_diag = [0] * (2 * n - 1)&#10;    lower_diag = [0] * (2 * n - 1)&#10;    &#10;    def solve(col):&#10;        if col == n:&#10;            ans.append([&quot;&quot;.join(row) for row in board])&#10;            return&#10;            &#10;        for row in range(n):&#10;            if left_row[row] == 0 and lower_diag[row + col] == 0 and upper_diag[n - 1 + col - row] == 0:&#10;                board[row][col] = &#x27;Q&#x27;&#10;                left_row[row] = 1&#10;                lower_diag[row + col] = 1&#10;                upper_diag[n - 1 + col - row] = 1&#10;                &#10;                solve(col + 1)&#10;                &#10;                board[row][col] = &#x27;.&#x27;&#10;                left_row[row] = 0&#10;                lower_diag[row + col] = 0&#10;                upper_diag[n - 1 + col - row] = 0&#10;                &#10;    solve(0)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>3</td>
      <td>Rec 03 Permutations<br><br></b> <a href="https://leetcode.com/problems/permutations/" target="_blank">LeetCode 46</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: nums = [1,2,3], Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]</td>
      <td><b>Time:</b> O(N! * N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Backtracking. Swap elements to generate permutations. For index `i`, swap it with every index from `i` to `n-1`, recurse, then backtrack (swap back).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def permute(nums: list[int]) -&gt; list[list[int]]:&#10;    ans = []&#10;    def solve(idx):&#10;        if idx == len(nums):&#10;            ans.append(nums[:])&#10;            return&#10;        for i in range(idx, len(nums)):&#10;            nums[idx], nums[i] = nums[i], nums[idx]&#10;            solve(idx + 1)&#10;            nums[idx], nums[i] = nums[i], nums[idx]&#10;    solve(0)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>4</td>
      <td>Rec 04 Sudoku Solver<br><br></b> <a href="https://leetcode.com/problems/sudoku-solver/" target="_blank">LeetCode 37</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td>**Example 1:** Input: board with '.' for empty cells. Solve in-place.</td>
      <td><b>Time:</b> O(9^(n*n))<br><b>Space:</b> O(1) auxiliary</td>
      <td><b>Explanation:</b> Backtracking. Find first empty cell, try placing 1-9. Validate row, col, and 3x3 sub-grid. Recursively solve the rest. If it fails, backtrack.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def solveSudoku(board: List[List[str]]) -&gt; None:&#10;    def isValid(row, col, ch):&#10;        for i in range(9):&#10;            if board[i][col] == ch: return False&#10;            if board[row][i] == ch: return False&#10;            if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == ch: return False&#10;        return True&#10;    def solve():&#10;        for i in range(len(board)):&#10;            for j in range(len(board[0])):&#10;                if board[i][j] == &#x27;.&#x27;:&#10;                    for c in &#x27;123456789&#x27;:&#10;                        if isValid(i, j, c):&#10;                            board[i][j] = c&#10;                            if solve(): return True&#10;                            else: board[i][j] = &#x27;.&#x27;&#10;                    return False&#10;        return True&#10;    solve()</code></pre></details></td>
    </tr>
    <tr>
      <td>5</td>
      <td>Rec 05 M Coloring Problem<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/m-coloring-problem-1587115620/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td>**Example 1:** Return true if possible.</td>
      <td><b>Time:</b> O(M^N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Backtracking. Try coloring each node with color 1 to m. For a color, check if any adjacent node has the same color. If safe, assign and recurse for next node. If recursion returns false, backtrack.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def graphColoring(graph: List[List[int]], m: int, n: int) -&gt; bool:&#10;    color = [0] * n&#10;    def isSafe(node, col):&#10;        for k in range(n):&#10;            if k != node and graph[k][node] == 1 and color[k] == col: return False&#10;        return True&#10;    def solve(node):&#10;        if node == n: return True&#10;        for i in range(1, m + 1):&#10;            if isSafe(node, i):&#10;                color[node] = i&#10;                if solve(node + 1): return True&#10;                color[node] = 0&#10;        return False&#10;    return solve(0)</code></pre></details></td>
    </tr>
    <tr>
      <td>6</td>
      <td>Rec 06 Rat In A Maze<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td>**Example 1:** Lexicographical order paths.</td>
      <td><b>Time:</b> O(4^(N*N))<br><b>Space:</b> O(N*N)</td>
      <td><b>Explanation:</b> Backtracking. Explore 4 directions (D, L, R, U) in lexicographical order to get sorted paths naturally. Mark cell as visited, recurse, then unmark (backtrack).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findPath(m: List[List[int]], n: int) -&gt; List[str]:&#10;    ans = []&#10;    vis = [[0 for _ in range(n)] for _ in range(n)]&#10;    di = [1, 0, 0, -1]&#10;    dj = [0, -1, 1, 0]&#10;    dir_str = &quot;DLRU&quot;&#10;    def solve(i, j, move):&#10;        if i == n - 1 and j == n - 1:&#10;            ans.append(move)&#10;            return&#10;        for ind in range(4):&#10;            nexti, nextj = i + di[ind], j + dj[ind]&#10;            if 0 &lt;= nexti &lt; n and 0 &lt;= nextj &lt; n and not vis[nexti][nextj] and m[nexti][nextj] == 1:&#10;                vis[i][j] = 1&#10;                solve(nexti, nextj, move + dir_str[ind])&#10;                vis[i][j] = 0&#10;    if m[0][0] == 1: solve(0, 0, &quot;&quot;)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>7</td>
      <td>Rec 07 Word Break<br><br></b> <a href="https://leetcode.com/problems/word-break/" target="_blank">LeetCode 139</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet, Apna College</details></td>
      <td>**Example 1:** Input: s = 'leetcode', wordDict = ['leet','code'], Output: true</td>
      <td><b>Time:</b> O(N^3)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Recursion with Memoization (or DP). For each index, try all possible word lengths. If a prefix exists in dict, recurse for the suffix. DP array `dp[i]` stores if `s[0...i-1]` is valid.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def wordBreak(s: str, wordDict: List[str]) -&gt; bool:&#10;    word_set = set(wordDict)&#10;    dp = [False] * (len(s) + 1)&#10;    dp[0] = True&#10;    for i in range(1, len(s) + 1):&#10;        for j in range(i):&#10;            if dp[j] and s[j:i] in word_set:&#10;                dp[i] = True&#10;                break&#10;    return dp[-1]</code></pre></details></td>
    </tr>
    <tr>
      <td>8</td>
      <td>Rec 08 Word Break Ii<br><br></b> <a href="https://leetcode.com/problems/word-break-ii/" target="_blank">LeetCode 140</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td>**Example 1:** Return list of sentences.</td>
      <td><b>Time:</b> O(2^N)<br><b>Space:</b> O(2^N)</td>
      <td><b>Explanation:</b> Backtracking. Generate all combinations. At each step, if a prefix is in dict, recursively call for the rest of the string and append the prefix to the result of the recursive call.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def wordBreak(s: str, wordDict: List[str]) -&gt; List[str]:&#10;    word_set = set(wordDict)&#10;    memo = {}&#10;    def solve(s):&#10;        if s in memo: return memo[s]&#10;        if not s: return [&quot;&quot;]&#10;        res = []&#10;        for i in range(1, len(s) + 1):&#10;            word = s[:i]&#10;            if word in word_set:&#10;                rem = solve(s[i:])&#10;                for st in rem:&#10;                    res.append(word + (&quot; &quot; if st else &quot;&quot;) + st)&#10;        memo[s] = res&#10;        return res&#10;    return solve(s)</code></pre></details></td>
    </tr>
    <tr>
      <td>9</td>
      <td>Rec 09 Palindrome Partitioning<br><br></b> <a href="https://leetcode.com/problems/palindrome-partitioning/" target="_blank">LeetCode 131</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td>**Example 1:** Input: s = 'aab', Output: [['a','a','b'],['aa','b']]</td>
      <td><b>Time:</b> O(N * 2^N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Backtracking. Try to partition the string at every index. If the prefix `s[start:i]` is a palindrome, add it to current path and recurse for the rest of the string `s[i:end]`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def partition(s: str) -&gt; List[List[str]]:&#10;    res = []&#10;    path = []&#10;    def isPalindrome(s, start, end):&#10;        while start &lt;= end:&#10;            if s[start] != s[end]: return False&#10;            start += 1; end -= 1&#10;        return True&#10;    def solve(index):&#10;        if index == len(s):&#10;            res.append(list(path))&#10;            return&#10;        for i in range(index, len(s)):&#10;            if isPalindrome(s, index, i):&#10;                path.append(s[index:i+1])&#10;                solve(i + 1)&#10;                path.pop()&#10;    solve(0)&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td>10</td>
      <td>Rec 10 Expression Add Operators<br><br></b> <a href="https://leetcode.com/problems/expression-add-operators/" target="_blank">LeetCode 282</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td>**Example 1:** Return expressions.</td>
      <td><b>Time:</b> O(N * 4^N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Backtracking. Keep track of the evaluated sum so far, and the previous operand (for multiplication precedence). For '*', `newSum = sum - prev + prev * curr`. Handle leading zeros.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def addOperators(num: str, target: int) -&gt; List[str]:&#10;    ans = []&#10;    def solve(ind, path, eval_sum, multed):&#10;        if ind == len(num):&#10;            if eval_sum == target: ans.append(path)&#10;            return&#10;        for i in range(ind, len(num)):&#10;            if i != ind and num[ind] == &#x27;0&#x27;: break&#10;            cur_str = num[ind:i+1]&#10;            cur_num = int(cur_str)&#10;            if ind == 0:&#10;                solve(i + 1, path + cur_str, cur_num, cur_num)&#10;            else:&#10;                solve(i + 1, path + &quot;+&quot; + cur_str, eval_sum + cur_num, cur_num)&#10;                solve(i + 1, path + &quot;-&quot; + cur_str, eval_sum - cur_num, -cur_num)&#10;                solve(i + 1, path + &quot;*&quot; + cur_str, eval_sum - multed + multed * cur_num, multed * cur_num)&#10;    solve(0, &quot;&quot;, 0, 0)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>11</td>
      <td>Rec 11 Subset Sums Ii<br><br></b> <a href="https://leetcode.com/problems/subsets-ii/" target="_blank">LeetCode 90</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td>**Example 1:** Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]</td>
      <td><b>Time:</b> O(2^N * N)<br><b>Space:</b> O(2^N * N)</td>
      <td><b>Explanation:</b> Sort array first to bring duplicates together. In recursive call, loop from `ind` to `n`. If `i > ind` and `nums[i] == nums[i-1]`, `continue` to skip duplicate recursive branches.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def subsetsWithDup(nums: List[int]) -&gt; List[List[int]]:&#10;    ans = []&#10;    nums.sort()&#10;    def findSubsets(ind, ds):&#10;        ans.append(list(ds))&#10;        for i in range(ind, len(nums)):&#10;            if i != ind and nums[i] == nums[i-1]: continue&#10;            ds.append(nums[i])&#10;            findSubsets(i + 1, ds)&#10;            ds.pop()&#10;    findSubsets(0, [])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>12</td>
      <td>Rec 12 Combination Sum Ii<br><br></b> <a href="https://leetcode.com/problems/combination-sum-ii/" target="_blank">LeetCode 40</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td>**Example 1:** Return unique combinations.</td>
      <td><b>Time:</b> O(2^N * k)<br><b>Space:</b> O(k * x)</td>
      <td><b>Explanation:</b> Sort the array. Recursive function iterates from `ind` to `n`. Skip duplicates (`if i > ind and arr[i] == arr[i-1]`). If `arr[i] > target`, break. Else add to path, subtract from target, and recurse.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def combinationSum2(candidates: List[int], target: int) -&gt; List[List[int]]:&#10;    ans = []&#10;    candidates.sort()&#10;    def findCombinations(ind, target, ds):&#10;        if target == 0:&#10;            ans.append(list(ds))&#10;            return&#10;        for i in range(ind, len(candidates)):&#10;            if i &gt; ind and candidates[i] == candidates[i-1]: continue&#10;            if candidates[i] &gt; target: break&#10;            ds.append(candidates[i])&#10;            findCombinations(i + 1, target - candidates[i], ds)&#10;            ds.pop()&#10;    findCombinations(0, target, [])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>13</td>
      <td>Rec 13 Combination Sum Iii<br><br></b> <a href="https://leetcode.com/problems/combination-sum-iii/" target="_blank">LeetCode 216</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td>**Example 1:** Return combinations.</td>
      <td><b>Time:</b> O(2^9)<br><b>Space:</b> O(k)</td>
      <td><b>Explanation:</b> Backtracking. Start from 1, go up to 9. Add the current number to the path and subtract from target. Stop when path size is `k` and `target` is 0.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def combinationSum3(k: int, n: int) -&gt; List[List[int]]:&#10;    ans = []&#10;    def solve(start, k, n, ds):&#10;        if k == 0 and n == 0:&#10;            ans.append(list(ds))&#10;            return&#10;        if k == 0 or n &lt; 0: return&#10;        for i in range(start, 10):&#10;            ds.append(i)&#10;            solve(i + 1, k - 1, n - i, ds)&#10;            ds.pop()&#10;    solve(1, k, n, [])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>14</td>
      <td>Rec 14 Letter Combinations Of A Phone Number<br><br></b> <a href="https://leetcode.com/problems/letter-combinations-of-a-phone-number/" target="_blank">LeetCode 17</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td>**Example 1:** String combinations.</td>
      <td><b>Time:</b> O(4^N * N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Backtracking. Create a mapping of digit to letters. Iterate through digits, for each digit loop through its mapped letters, append to current string, and recurse.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def letterCombinations(digits: str) -&gt; List[str]:&#10;    if not digits: return []&#10;    ans = []&#10;    mapping = [&quot;&quot;, &quot;&quot;, &quot;abc&quot;, &quot;def&quot;, &quot;ghi&quot;, &quot;jkl&quot;, &quot;mno&quot;, &quot;pqrs&quot;, &quot;tuv&quot;, &quot;wxyz&quot;]&#10;    def solve(ind, path):&#10;        if ind == len(digits):&#10;            ans.append(path)&#10;            return&#10;        number = int(digits[ind])&#10;        value = mapping[number]&#10;        for i in range(len(value)):&#10;            solve(ind + 1, path + value[i])&#10;    solve(0, &quot;&quot;)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>15</td>
      <td>Rec 15 Subset Sum I<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/subset-sums2234/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td>**Example 1:** Take / Not Take.</td>
      <td><b>Time:</b> O(2^N)<br><b>Space:</b> O(2^N)</td>
      <td><b>Explanation:</b> Recursively either include `arr[ind]` in sum, or exclude it. If `ind == N`, add `sum` to result array.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def subsetSums(arr: List[int], N: int) -&gt; List[int]:&#10;    sumSubset = []&#10;    def func(ind, current_sum):&#10;        if ind == N:&#10;            sumSubset.append(current_sum)&#10;            return&#10;        func(ind + 1, current_sum + arr[ind])&#10;        func(ind + 1, current_sum)&#10;    func(0, 0)&#10;    sumSubset.sort()&#10;    return sumSubset</code></pre></details></td>
    </tr>
    <tr>
      <td>16</td>
      <td>Rec 16 N Queens Ii<br><br></b> <a href="https://leetcode.com/problems/n-queens-ii/" target="_blank">LeetCode 52</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td>**Example 1:** Backtracking with hashing.</td>
      <td><b>Time:</b> O(N!)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Use backtracking to place queens column by column. Use three hash arrays (or bitmasks) to track attacked rows, upper diagonals, and lower diagonals. If placing a queen is safe, update hashes, recurse for next column, and then backtrack.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def totalNQueens(n: int) -&gt; int:&#10;    count = 0&#10;    leftRow = [0] * n&#10;    upperDiag = [0] * (2 * n - 1)&#10;    lowerDiag = [0] * (2 * n - 1)&#10;    def solve(col):&#10;        nonlocal count&#10;        if col == n:&#10;            count += 1&#10;            return&#10;        for row in range(n):&#10;            if leftRow[row] == 0 and lowerDiag[row + col] == 0 and upperDiag[n - 1 + col - row] == 0:&#10;                leftRow[row] = 1&#10;                lowerDiag[row + col] = 1&#10;                upperDiag[n - 1 + col - row] = 1&#10;                solve(col + 1)&#10;                leftRow[row] = 0&#10;                lowerDiag[row + col] = 0&#10;                upperDiag[n - 1 + col - row] = 0&#10;    solve(0)&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td>17</td>
      <td>Rec 17 Word Search<br><br></b> <a href="https://leetcode.com/problems/word-search/" target="_blank">LeetCode 79</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td>**Example 1:** Backtracking DFS.</td>
      <td><b>Time:</b> O(N * M * 4^L)<br><b>Space:</b> O(L) recursion stack</td>
      <td><b>Explanation:</b> Start DFS from each cell that matches the first letter of the word. In DFS, check 4 neighbors. Mark current cell as visited (e.g. change to '#') before moving to neighbors, and unmark (backtrack) after exploring.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def exist(board: List[List[str]], word: str) -&gt; bool:&#10;    def dfs(i, j, idx):&#10;        if idx == len(word): return True&#10;        if i &lt; 0 or i &gt;= len(board) or j &lt; 0 or j &gt;= len(board[0]) or board[i][j] != word[idx]:&#10;            return False&#10;        temp = board[i][j]&#10;        board[i][j] = &#x27;#&#x27;&#10;        found = (dfs(i+1, j, idx+1) or dfs(i-1, j, idx+1) or&#10;                 dfs(i, j+1, idx+1) or dfs(i, j-1, idx+1))&#10;        board[i][j] = temp&#10;        return found&#10;    for i in range(len(board)):&#10;        for j in range(len(board[0])):&#10;            if board[i][j] == word[0] and dfs(i, j, 0):&#10;                return True&#10;    return False</code></pre></details></td>
    </tr>
    <tr>
      <td>18</td>
      <td>Rec 18 K Th Symbol In Grammar<br><br></b> <a href="https://leetcode.com/problems/k-th-symbol-in-grammar/" target="_blank">LeetCode 779</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td>**Example 1:** Recursive division.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Row N has length 2^(N-1). The first half of row N is exactly same as row N-1. The second half of row N is the complement of row N-1. If k is in the first half (k <= mid), return solve(N-1, k). If k is in the second half, return !solve(N-1, k - mid).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def kthGrammar(n: int, k: int) -&gt; int:&#10;    if n == 1 and k == 1: return 0&#10;    mid = 2 ** (n - 2)&#10;    if k &lt;= mid:&#10;        return kthGrammar(n - 1, k)&#10;    else:&#10;        return 1 - kthGrammar(n - 1, k - mid)</code></pre></details></td>
    </tr>
    <tr>
      <td>19</td>
      <td>Rec 19 Beautiful Arrangement<br><br></b> <a href="https://leetcode.com/problems/beautiful-arrangement/" target="_blank">LeetCode 526</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td>**Example 1:** Backtracking.</td>
      <td><b>Time:</b> O(K) where K is number of valid permutations<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Use an array to track visited numbers. Iterate from index 1 to n. For the current index, try placing an unvisited number. Check if the condition `(num % idx == 0 || idx % num == 0)` is met. If so, mark as visited, recurse to `idx + 1`, then backtrack.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def countArrangement(n: int) -&gt; int:&#10;    count = 0&#10;    visited = [0] * (n + 1)&#10;    def solve(idx):&#10;        nonlocal count&#10;        if idx &gt; n:&#10;            count += 1&#10;            return&#10;        for i in range(1, n + 1):&#10;            if not visited[i] and (i % idx == 0 or idx % i == 0):&#10;                visited[i] = 1&#10;                solve(idx + 1)&#10;                visited[i] = 0&#10;    solve(1)&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td>20</td>
      <td>Rec 20 Print All Permutations Of A String<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/permutations-of-a-given-string2041/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Recursive Backtracking.</td>
      <td><b>Time:</b> O(N! * N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Convert string to char array and sort it. Use backtracking: pass a boolean visited array and a temporary string. If temporary string length equals original length, add to answer. Else, iterate through characters. To avoid duplicates, if `i > 0` and `s[i] == s[i-1]` and `!vis[i-1]`, skip. Otherwise, mark visited, append, recurse, unmark, pop.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def find_permutation(S: str) -&gt; List[str]:&#10;    S = sorted(list(S))&#10;    ans = []&#10;    vis = [False] * len(S)&#10;    def solve(curr):&#10;        if len(curr) == len(S):&#10;            ans.append(&quot;&quot;.join(curr))&#10;            return&#10;        for i in range(len(S)):&#10;            if vis[i] or (i &gt; 0 and S[i] == S[i-1] and not vis[i-1]):&#10;                continue&#10;            vis[i] = True&#10;            curr.append(S[i])&#10;            solve(curr)&#10;            curr.pop()&#10;            vis[i] = False&#10;    solve([])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>21</td>
      <td>Rec 21 Remove Invalid Parentheses<br><br></b> <a href="https://leetcode.com/problems/remove-invalid-parentheses/" target="_blank">LeetCode 301</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td>**Example 1:** Recursion and Backtracking.</td>
      <td><b>Time:</b> O(2^N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> First find the number of misplaced left (`rm_l`) and right (`rm_r`) parentheses. Then use backtracking to try removing `rm_l` and `rm_r` parentheses. To avoid duplicates, skip identical adjacent characters. Finally, check if the resulting string is valid.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def removeInvalidParentheses(s: str) -&gt; List[str]:&#10;    def is_valid(s):&#10;        count = 0&#10;        for c in s:&#10;            if c == &#x27;(&#x27;: count += 1&#10;            elif c == &#x27;)&#x27;: count -= 1&#10;            if count &lt; 0: return False&#10;        return count == 0&#10;    rm_l, rm_r = 0, 0&#10;    for c in s:&#10;        if c == &#x27;(&#x27;: rm_l += 1&#10;        elif c == &#x27;)&#x27;:&#10;            if rm_l &gt; 0: rm_l -= 1&#10;            else: rm_r += 1&#10;    ans = []&#10;    def solve(s, start, rm_l, rm_r):&#10;        if rm_l == 0 and rm_r == 0:&#10;            if is_valid(s): ans.append(s)&#10;            return&#10;        for i in range(start, len(s)):&#10;            if i != start and s[i] == s[i-1]: continue&#10;            if s[i] == &#x27;(&#x27; and rm_l &gt; 0:&#10;                solve(s[:i] + s[i+1:], i, rm_l - 1, rm_r)&#10;            elif s[i] == &#x27;)&#x27; and rm_r &gt; 0:&#10;                solve(s[:i] + s[i+1:], i, rm_l, rm_r - 1)&#10;    solve(s, 0, rm_l, rm_r)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>22</td>
      <td>Rec 22 Matchsticks To Square<br><br></b> <a href="https://leetcode.com/problems/matchsticks-to-square/" target="_blank">LeetCode 473</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td>**Example 1:** Backtracking to 4 subsets.</td>
      <td><b>Time:</b> O(4^N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Calculate sum. If sum % 4 != 0, return false. Target side length is sum / 4. Sort matchsticks in descending order to optimize. Create an array `sides` of size 4. For each matchstick, try adding it to one of the 4 sides. If a side equals the target or is less, recurse.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def makesquare(matchsticks: List[int]) -&gt; bool:&#10;    total = sum(matchsticks)&#10;    if total % 4 != 0 or len(matchsticks) &lt; 4: return False&#10;    target = total // 4&#10;    matchsticks.sort(reverse=True)&#10;    sides = [0] * 4&#10;    def solve(ind):&#10;        if ind == len(matchsticks):&#10;            return sides[0] == sides[1] == sides[2] == target&#10;        for i in range(4):&#10;            if sides[i] + matchsticks[ind] &lt;= target:&#10;                sides[i] += matchsticks[ind]&#10;                if solve(ind + 1): return True&#10;                sides[i] -= matchsticks[ind]&#10;            if sides[i] == 0: break&#10;        return False&#10;    return solve(0)</code></pre></details></td>
    </tr>
    <tr>
      <td>23</td>
      <td>Rec 23 Tug Of War<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/tug-of-war/0" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td>**Example 1:** Recursive Backtracking.</td>
      <td><b>Time:</b> O(2^N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Keep track of the number of elements included in subset 1 and their sum. Recurse by including the current element in subset 1 or subset 2. Base case: if we reach end, check if subset 1 has `n/2` elements. If so, compute difference and update global minimum.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def tugOfWar(arr: List[int]) -&gt; int:&#10;    n = len(arr)&#10;    totalSum = sum(arr)&#10;    minDiff = [float(&#x27;inf&#x27;)]&#10;    def solve(ind, cnt, sum1):&#10;        if ind == n:&#10;            if cnt == n // 2:&#10;                sum2 = totalSum - sum1&#10;                minDiff[0] = min(minDiff[0], abs(sum1 - sum2))&#10;            return&#10;        if cnt &lt; n // 2:&#10;            solve(ind + 1, cnt + 1, sum1 + arr[ind])&#10;        solve(ind + 1, cnt, sum1)&#10;    solve(0, 0, 0)&#10;    return minDiff[0]</code></pre></details></td>
    </tr>
    <tr>
      <td>24</td>
      <td>Rec 24 Find Paths From Corner Cell To Middle Cell<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/paths-from-corner-to-middle/0" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td>**Example 1:** BFS / DFS for path finding.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N^2)</td>
      <td><b>Explanation:</b> Perform BFS or DFS starting from all 4 corners simultaneously or individually. At each cell `(r, c)`, the jump size is `val = grid[r][c]`. We can move to `(r+val, c)`, `(r-val, c)`, `(r, c+val)`, `(r, c-val)`. Target is `(N/2, N/2)`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def solve(grid: List[List[int]]):&#10;    n = len(grid)&#10;    q = collections.deque([(0,0), (0,n-1), (n-1,0), (n-1,n-1)])&#10;    vis = set(q)&#10;    dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]&#10;    while q:&#10;        r, c = q.popleft()&#10;        if r == n // 2 and c == n // 2: return True&#10;        val = grid[r][c]&#10;        if val == 0: continue&#10;        for i in range(4):&#10;            nr, nc = r + dr[i] * val, c + dc[i] * val&#10;            if 0 &lt;= nr &lt; n and 0 &lt;= nc &lt; n and (nr, nc) not in vis:&#10;                vis.add((nr, nc))&#10;                q.append((nr, nc))&#10;    return False</code></pre></details></td>
    </tr>
    <tr>
      <td>25</td>
      <td>Rec 25 Arithmetic Expressions<br><br></b> <a href="https://www.hackerrank.com/challenges/arithmetic-expressions/problem" target="_blank">HackerRank</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td>**Example 1:** DP with path reconstruction.</td>
      <td><b>Time:</b> O(N * 101)<br><b>Space:</b> O(N * 101)</td>
      <td><b>Explanation:</b> Use a DP table `dp[i][mod]` to store the operator used to reach remainder `mod` at index `i`. Iterate through the array, for each reachable mod from previous step, try `(mod + arr[i]) % 101`, `(mod - arr[i]) % 101`, `(mod * arr[i]) % 101`. Then backtrack from `dp[N-1][0]` to find the operators.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def arithmeticExpressions(arr: List[int]) -&gt; str:&#10;    n = len(arr)&#10;    dp = [[None] * 101 for _ in range(n)]&#10;    dp[0][arr[0] % 101] = (&#x27;&#x27;, 0)&#10;    for i in range(1, n):&#10;        for j in range(101):&#10;            if dp[i-1][j] is not None:&#10;                dp[i][(j + arr[i]) % 101] = (&#x27;+&#x27;, j)&#10;                dp[i][(j - arr[i] % 101 + 101) % 101] = (&#x27;-&#x27;, j)&#10;                dp[i][(j * arr[i]) % 101] = (&#x27;*&#x27;, j)&#10;    res = []&#10;    curr = 0&#10;    for i in range(n - 1, 0, -1):&#10;        op, prev_mod = dp[i][curr]&#10;        res.append(str(arr[i]))&#10;        res.append(op)&#10;        curr = prev_mod&#10;    res.append(str(arr[0]))&#10;    return &quot;&quot;.join(reversed(res))</code></pre></details></td>
    </tr>
    <tr>
      <td>26</td>
      <td>Rec 26 Find All Possible Palindromic Partitions Of A String<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/find-all-possible-palindromic-partitions-of-a-string/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td>**Example 1:** Recursive Backtracking.</td>
      <td><b>Time:</b> O(N * 2^N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Iterate through the string. Extract substring `S[ind..i]`. If it is a palindrome, add it to the current partition list and recursively call for `i+1`. When `ind == length`, push the partition list to the answer.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def allPalindromicPerms(S: str) -&gt; List[List[str]]:&#10;    ans = []&#10;    def is_pal(s): return s == s[::-1]&#10;    def solve(ind, curr):&#10;        if ind == len(S):&#10;            ans.append(curr[:])&#10;            return&#10;        for i in range(ind, len(S)):&#10;            sub = S[ind:i+1]&#10;            if is_pal(sub):&#10;                curr.append(sub)&#10;                solve(i + 1, curr)&#10;                curr.pop()&#10;    solve(0, [])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>27</td>
      <td>Rec 27 Partition Array To K Subsets<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/partition-array-to-k-subsets/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td>**Example 1:** Recursive Backtracking.</td>
      <td><b>Time:</b> O(K * 2^N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> If total sum is not divisible by K, return false. Sort array in descending order. Use a boolean array `vis`. Helper function `solve(ind, currentSum, k)`: if `k == 1` return true. If `currentSum == target`, `solve(0, 0, k-1)`. Otherwise, iterate from `ind` to `N`, if `!vis[i]` and `currentSum + arr[i] <= target`, mark `vis[i] = true`, recurse, unmark.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isKPartitionPossible(a: List[int], n: int, k: int) -&gt; bool:&#10;    total = sum(a)&#10;    if total % k != 0 or n &lt; k: return False&#10;    target = total // k&#10;    vis = [False] * n&#10;    def solve(ind, currSum, k):&#10;        if k == 1: return True&#10;        if currSum == target: return solve(0, 0, k - 1)&#10;        for i in range(ind, n):&#10;            if not vis[i] and currSum + a[i] &lt;= target:&#10;                vis[i] = True&#10;                if solve(i + 1, currSum + a[i], k): return True&#10;                vis[i] = False&#10;        return False&#10;    return solve(0, 0, k)</code></pre></details></td>
    </tr>
    <tr>
      <td>28</td>
      <td>Rec 28 Longest Possible Route In A Matrix With Hurdles<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/longest-possible-route-in-a-matrix-with-hurdles/0" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td>**Example 1:** Recursive Backtracking.</td>
      <td><b>Time:</b> O(4^(N*M))<br><b>Space:</b> O(N*M)</td>
      <td><b>Explanation:</b> Use a global `max_dist` or pass it by reference. In `solve(r, c, dist)`, if `(r, c) == (dest_r, dest_c)`, `max_dist = max(max_dist, dist)` and return. Mark `(r, c)` as visited. Explore 4 directions. Unmark `(r, c)`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def longestPath(mat: List[List[int]], xs: int, ys: int, xd: int, yd: int) -&gt; int:&#10;    if mat[xs][ys] == 0 or mat[xd][yd] == 0: return -1&#10;    maxDist = [-1]&#10;    n, m = len(mat), len(mat[0])&#10;    def solve(r, c, dist):&#10;        if r == xd and c == yd:&#10;            maxDist[0] = max(maxDist[0], dist)&#10;            return&#10;        mat[r][c] = 0&#10;        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:&#10;            if 0 &lt;= nr &lt; n and 0 &lt;= nc &lt; m and mat[nr][nc] == 1:&#10;                solve(nr, nc, dist + 1)&#10;        mat[r][c] = 1&#10;    solve(xs, ys, 0)&#10;    return maxDist[0]</code></pre></details></td>
    </tr>
    <tr>
      <td>29</td>
      <td>Rec 29 Find Shortest Safe Route In A Path With Landmines<br><br></b> <a href="https://www.geeksforgeeks.org/find-shortest-safe-route-in-a-path-with-landmines/" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td>**Example 1:** BFS or Backtracking.</td>
      <td><b>Time:</b> O(R * C)<br><b>Space:</b> O(R * C)</td>
      <td><b>Explanation:</b> First, mark all adjacent cells of landmines as unsafe. Then start from each cell in the first column and use BFS or Backtracking to find the shortest path to the last column, avoiding unsafe cells.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">from collections import deque&#10;def findShortestPath(mat):&#10;    R, C = len(mat), len(mat[0])&#10;    grid = [[1] * C for _ in range(R)]&#10;    dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]&#10;    for i in range(R):&#10;        for j in range(C):&#10;            if mat[i][j] == 0:&#10;                grid[i][j] = 0&#10;                for k in range(4):&#10;                    nr, nc = i + dr[k], j + dc[k]&#10;                    if 0 &lt;= nr &lt; R and 0 &lt;= nc &lt; C: grid[nr][nc] = 0&#10;    q = deque()&#10;    vis = [[False] * C for _ in range(R)]&#10;    for i in range(R):&#10;        if grid[i][0] == 1:&#10;            q.append((i, 0, 1))&#10;            vis[i][0] = True&#10;    while q:&#10;        r, c, dist = q.popleft()&#10;        if c == C - 1: return dist&#10;        for k in range(4):&#10;            nr, nc = r + dr[k], c + dc[k]&#10;            if 0 &lt;= nr &lt; R and 0 &lt;= nc &lt; C and grid[nr][nc] == 1 and not vis[nr][nc]:&#10;                vis[nr][nc] = True&#10;                q.append((nr, nc, dist + 1))&#10;    return -1</code></pre></details></td>
    </tr>
    <tr>
      <td>30</td>
      <td>Rec 30 Combinational Sum<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/combination-sum-1587115620/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td>**Example 1:** Backtracking.</td>
      <td><b>Time:</b> O(2^N * K)<br><b>Space:</b> O(K * X)</td>
      <td><b>Explanation:</b> Sort the array and remove duplicates. Use backtracking. At each step, either include the current element (and stay at the current element to allow unlimited picks) or move to the next element. Backtrack when sum < 0 or we reach the end.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def combinationSum(A, B):&#10;    A = sorted(list(set(A)))&#10;    ans = []&#10;    def solve(idx, current_sum, curr):&#10;        if current_sum == B:&#10;            ans.append(list(curr))&#10;            return&#10;        if current_sum &gt; B or idx == len(A): return&#10;        curr.append(A[idx])&#10;        solve(idx, current_sum + A[idx], curr)&#10;        curr.pop()&#10;        solve(idx + 1, current_sum, curr)&#10;    solve(0, 0, [])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>31</td>
      <td>Rec 31 Find Maximum Number Possible By Doing At Most K Swaps<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/largest-number-in-k-swaps-1587115620/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td>**Example 1:** Backtracking.</td>
      <td><b>Time:</b> O(N! / (N-K)!)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Use backtracking to try swapping each digit with every digit that appears after it and is greater than it. Keep track of the maximum string seen so far. Prune if swaps == 0.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findMaximumNum(str_val, k):&#10;    max_str = [str_val]&#10;    def solve(curr, k_left, idx):&#10;        if k_left == 0 or idx == len(curr) - 1: return&#10;        max_char = curr[idx]&#10;        for i in range(idx + 1, len(curr)):&#10;            if curr[i] &gt; max_char: max_char = curr[i]&#10;        if max_char != curr[idx]: k_left -= 1&#10;        for i in range(len(curr) - 1, idx - 1, -1):&#10;            if curr[i] == max_char:&#10;                curr_list = list(curr)&#10;                curr_list[idx], curr_list[i] = curr_list[i], curr_list[idx]&#10;                new_str = &quot;&quot;.join(curr_list)&#10;                if new_str &gt; max_str[0]: max_str[0] = new_str&#10;                solve(new_str, k_left, idx + 1)&#10;    solve(str_val, k, 0)&#10;    return max_str[0]</code></pre></details></td>
    </tr>
    <tr>
      <td>32</td>
      <td>Rec 32 Find If There Is A Path Of More Than K Length From A Source<br><br></b> <a href="https://www.geeksforgeeks.org/find-if-there-is-a-path-of-more-than-k-length-from-a-source/" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td>**Example 1:** DFS Backtracking.</td>
      <td><b>Time:</b> O(V!)<br><b>Space:</b> O(V)</td>
      <td><b>Explanation:</b> Use Backtracking to perform DFS traversal from the source. Mark the current vertex as visited, subtract the edge weight from `k`, and recursively call for all adjacent unvisited vertices. If `k <= 0`, return true. Backtrack by unmarking the vertex.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def pathMoreThanK(src, k, adj, vis):&#10;    if k &lt;= 0: return True&#10;    vis[src] = True&#10;    for v, w in adj[src]:&#10;        if not vis[v]:&#10;            if pathMoreThanK(v, k - w, adj, vis):&#10;                return True&#10;    vis[src] = False&#10;    return False</code></pre></details></td>
    </tr>
    <tr>
      <td>33</td>
      <td>Rec 33 Longest Possible Route In A Matrix With Hurdles<br><br></b> <a href="https://www.geeksforgeeks.org/longest-possible-route-in-a-matrix-with-hurdles/" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td>**Example 1:** Backtracking.</td>
      <td><b>Time:</b> O(4^(M*N))<br><b>Space:</b> O(M*N)</td>
      <td><b>Explanation:</b> Use Backtracking. Start from the source, mark it as visited, recursively find the longest path from all valid unvisited adjacent cells, add 1 to the maximum among them. Unmark the cell after returning.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findLongestPath(mat, i, j, di, dj, curr, max_dist, vis):&#10;    if i == di and j == dj:&#10;        max_dist[0] = max(max_dist[0], curr)&#10;        return&#10;    vis[i][j] = True&#10;    dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]&#10;    for k in range(4):&#10;        nr, nc = i + dr[k], j + dc[k]&#10;        if 0 &lt;= nr &lt; len(mat) and 0 &lt;= nc &lt; len(mat[0]) and mat[nr][nc] == 1 and not vis[nr][nc]:&#10;            findLongestPath(mat, nr, nc, di, dj, curr + 1, max_dist, vis)&#10;    vis[i][j] = False</code></pre></details></td>
    </tr>
    <tr>
      <td>34</td>
      <td>Rec 34 Print All Possible Paths From Top Left To Bottom Right Of A Mxn Matrix<br><br></b> <a href="https://www.geeksforgeeks.org/print-all-possible-paths-from-top-left-to-bottom-right-of-a-mxn-matrix/" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td>**Example 1:** DFS.</td>
      <td><b>Time:</b> O(2^(M+N))<br><b>Space:</b> O(M+N)</td>
      <td><b>Explanation:</b> Use simple DFS from top-left. From cell (i, j), we can move to (i+1, j) or (i, j+1). Keep track of the path elements in an array/list. When reaching bottom-right, print/save the path.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findPaths(mat, i, j, path, ans):&#10;    if i == len(mat) - 1 and j == len(mat[0]) - 1:&#10;        ans.append(path + [mat[i][j]])&#10;        return&#10;    path.append(mat[i][j])&#10;    if i + 1 &lt; len(mat): findPaths(mat, i + 1, j, path, ans)&#10;    if j + 1 &lt; len(mat[0]): findPaths(mat, i, j + 1, path, ans)&#10;    path.pop()</code></pre></details></td>
    </tr>
    <tr>
      <td>35</td>
      <td>Rec 35 Word Break Problem Using Backtracking<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/word-break-part-23249/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td>**Example 1:** Backtracking.</td>
      <td><b>Time:</b> O(2^N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Iterate from current index. For each prefix, if it is in the dictionary, add it to the current sentence string, add a space, and recur for the suffix. If we reach the end of the string, add the current sentence to the answer.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def wordBreak(n, dict_words, s):&#10;    st = set(dict_words)&#10;    ans = []&#10;    def solve(idx, curr):&#10;        if idx == len(s):&#10;            ans.append(curr.strip())&#10;            return&#10;        for i in range(idx, len(s)):&#10;            word = s[idx:i+1]&#10;            if word in st:&#10;                solve(i + 1, curr + word + &quot; &quot;)&#10;    solve(0, &quot;&quot;)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>36</td>
      <td>Rec 36 Print 1 To N Without Loop<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/print-1-to-n-without-using-loops-1587115620/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z</details></td>
      <td>**Example 1:** Recursion.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Use a recursive function. Call `f(N-1)` first and then print `N`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def printTillN(N):&#10;    if N == 0: return&#10;    printTillN(N - 1)&#10;    print(N, end=&quot; &quot;)</code></pre></details></td>
    </tr>
    <tr>
      <td>37</td>
      <td>Rec 37 Print N To 1 Without Loop<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/print-n-to-1-without-loop/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z</details></td>
      <td>**Example 1:** Recursion.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Use a recursive function. Print `N` first and then call `f(N-1)`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def printNos(N):&#10;    if N == 0: return&#10;    print(N, end=&quot; &quot;)&#10;    printNos(N - 1)</code></pre></details></td>
    </tr>
    <tr>
      <td>38</td>
      <td>Rec 38 Sum Of First N Terms<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/sum-of-first-n-terms5843/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z</details></td>
      <td>**Example 1:** Math or Recursion.</td>
      <td><b>Time:</b> O(1) Math, O(N) Recursion<br><b>Space:</b> O(1) Math, O(N) Recursion</td>
      <td><b>Explanation:</b> The mathematical formula for the sum of cubes is `(n * (n + 1) / 2)^2`. Alternatively, use recursion `f(n) = n^3 + f(n-1)`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def sumOfSeries(n):&#10;    return (n * (n + 1) // 2) ** 2</code></pre></details></td>
    </tr>
    <tr>
      <td>39</td>
      <td>Rec 39 Find All Factorial Numbers Less Than Or Equal To N<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/find-all-factorial-numbers-less-than-or-equal-to-n3548/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z</details></td>
      <td>**Example 1:** Recursion.</td>
      <td><b>Time:</b> O(K) where K! <= N<br><b>Space:</b> O(K)</td>
      <td><b>Explanation:</b> Maintain a current factorial value and an index `i`. At each recursive step, compute the next factorial by multiplying by `i`. If the next factorial is `<= n`, add it to the list and recurse.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def factorialNumbers(N):&#10;    ans = []&#10;    def findFactorials(i, fact):&#10;        if fact &gt; N: return&#10;        ans.append(fact)&#10;        findFactorials(i + 1, fact * (i + 1))&#10;    findFactorials(1, 1)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>40</td>
      <td>Rec 40 Reverse An Array<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/reverse-an-array/0" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z</details></td>
      <td>**Example 1:** Recursion with two pointers.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N) recursive stack</td>
      <td><b>Explanation:</b> Swap `arr[l]` and `arr[r]` and then recursively call `reverse(arr, l+1, r-1)`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def reverseArray(arr, l, r):&#10;    if l &gt;= r: return&#10;    arr[l], arr[r] = arr[r], arr[l]&#10;    reverseArray(arr, l + 1, r - 1)</code></pre></details></td>
    </tr>
    <tr>
      <td>41</td>
      <td>Rec 41 Fibonacci Number<br><br></b> <a href="https://leetcode.com/problems/fibonacci-number/" target="_blank">LeetCode 509</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z</details></td>
      <td>**Example 1:** Base Case.</td>
      <td><b>Time:</b> O(2^N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Return `fib(n-1) + fib(n-2)` with base cases `fib(0) = 0`, `fib(1) = 1`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def fib(n):&#10;    if n &lt;= 1: return n&#10;    return fib(n - 1) + fib(n - 2)</code></pre></details></td>
    </tr>
    <tr>
      <td>42</td>
      <td>Rec 42 Count Good Numbers<br><br></b> <a href="https://leetcode.com/problems/count-good-numbers/" target="_blank">LeetCode 1922</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z</details></td>
      <td>**Example 1:** Modular Exponentiation.</td>
      <td><b>Time:</b> O(log N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> There are 5 even digits and 4 prime digits. At even indices we have 5 choices. At odd indices we have 4 choices. If `n` is even, we have `n/2` even indices and `n/2` odd indices. So answer is `(5^(n/2) * 4^(n/2)) % mod`. If `n` is odd, we have `n/2 + 1` even indices. So answer is `(5^(n/2 + 1) * 4^(n/2)) % mod`. Use binary exponentiation.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def countGoodNumbers(n):&#10;    mod = 10**9 + 7&#10;    def power(x, y):&#10;        res = 1&#10;        x = x % mod&#10;        while y &gt; 0:&#10;            if y % 2 == 1: res = (res * x) % mod&#10;            y = y // 2&#10;            x = (x * x) % mod&#10;        return res&#10;    evenIndices = (n + 1) // 2&#10;    oddIndices = n // 2&#10;    return (power(5, evenIndices) * power(4, oddIndices)) % mod</code></pre></details></td>
    </tr>
    <tr>
      <td>43</td>
      <td>Rec 43 Sort A Stack Using Recursion<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/sort-a-stack/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td>**Example 1:** Recursive sort and insert.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Recursively pop elements until the stack is empty. When returning from the recursive call, use another recursive function `sortedInsert` to insert the popped element into its correct sorted position in the stack.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def sortedInsert(s, element):&#10;    if not s or element &gt; s[-1]:&#10;        s.append(element)&#10;        return&#10;    num = s.pop()&#10;    sortedInsert(s, element)&#10;    s.append(num)&#10;def sortStack(s):&#10;    if not s: return&#10;    num = s.pop()&#10;    sortStack(s)&#10;    sortedInsert(s, num)</code></pre></details></td>
    </tr>
  </tbody>
</table>
