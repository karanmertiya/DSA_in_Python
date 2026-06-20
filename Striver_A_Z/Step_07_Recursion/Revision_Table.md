# Step 07 Recursion Revision Table

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
      <td>Str 01 Palindrome String<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/palindrome-string0817/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td><b>Example 1:</b> Two pointers.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Use two pointers, `left` at the beginning and `right` at the end of the string. Compare the characters at these pointers. If they are different, return 0. Move pointers towards each other. If all characters match, return 1.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isPalindrome(S: str) -&gt; int:&#10;    left, right = 0, len(S) - 1&#10;    while left &lt; right:&#10;        if S[left] != S[right]:&#10;            return 0&#10;        left += 1&#10;        right -= 1&#10;    return 1</code></pre></details></td>
    </tr>
    <tr>
      <td>2</td>
      <td>Rec 02 Combination Sum<br><br></b> <a href="https://leetcode.com/problems/combination-sum/" target="_blank">LeetCode 39</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td><b>Example 1:</b> Input: candidates = [2,3,6,7], target = 7, Output: [[2,2,3],[7]]<br><br><b>Note (Constraint):</b> The same number may be chosen unlimited number of times.</td>
      <td><b>Time:</b> O(2<sup>T</sup>) (Trade-off)<br><b>Space:</b> O(T) (Trade-off)</td>
      <td><b>Explanation:</b> Pick/Non-Pick but when picking, we *do not* increment the index `i`, allowing the same element to be picked infinitely until `target < 0`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def combination_sum(candidates: list[int], target: int) -&gt; list[list[int]]:&#10;    ans = []&#10;    def solve(i, current_target, temp):&#10;        if i == len(candidates):&#10;            if current_target == 0:&#10;                ans.append(temp.copy())&#10;            return&#10;            &#10;        if candidates[i] &lt;= current_target:&#10;            temp.append(candidates[i])&#10;            solve(i, current_target - candidates[i], temp)&#10;            temp.pop()&#10;            &#10;        solve(i + 1, current_target, temp)&#10;        &#10;    solve(0, target, [])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>3</td>
      <td>Rec 03 N Queens<br><br></b> <a href="https://leetcode.com/problems/n-queens/" target="_blank">LeetCode 51</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z, SDE Sheet</details></td>
      <td><b>Example 1:</b> Input: n = 4, Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]<br><br><b>Note (Constraint):</b> 1 &le; n &le; 9</td>
      <td><b>Time:</b> O(N!) (Constraint)<br><b>Space:</b> O(N) (Constraint)</td>
      <td><b>Explanation:</b> Backtracking. Try placing a queen in each row of the current column. Use `O(1)` lookups (Hashing logic) via arrays to check if row/diagonals are safe.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def solve_n_queens(n: int) -&gt; list[list[str]]:&#10;    ans = []&#10;    board = [[&quot;.&quot;] * n for _ in range(n)]&#10;    left_row = [0] * n&#10;    upper_diag = [0] * (2 * n - 1)&#10;    lower_diag = [0] * (2 * n - 1)&#10;    &#10;    def solve(col):&#10;        if col == n:&#10;            ans.append([&quot;&quot;.join(row) for row in board])&#10;            return&#10;            &#10;        for row in range(n):&#10;            if left_row[row] == 0 and lower_diag[row + col] == 0 and upper_diag[n - 1 + col - row] == 0:&#10;                board[row][col] = &#x27;Q&#x27;&#10;                left_row[row] = 1&#10;                lower_diag[row + col] = 1&#10;                upper_diag[n - 1 + col - row] = 1&#10;                &#10;                solve(col + 1)&#10;                &#10;                board[row][col] = &#x27;.&#x27;&#10;                left_row[row] = 0&#10;                lower_diag[row + col] = 0&#10;                upper_diag[n - 1 + col - row] = 0&#10;                &#10;    solve(0)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>4</td>
      <td>Rec 04 Permutations<br><br></b> <a href="https://leetcode.com/problems/permutations/" target="_blank">LeetCode 46</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z, SDE Sheet</details></td>
      <td><b>Example 1:</b> Input: nums = [1,2,3], Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]</td>
      <td><b>Time:</b> O(N! * N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Backtracking. Swap elements to generate permutations. For index `i`, swap it with every index from `i` to `n-1`, recurse, then backtrack (swap back).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def permute(nums: list[int]) -&gt; list[list[int]]:&#10;    ans = []&#10;    def solve(idx):&#10;        if idx == len(nums):&#10;            ans.append(nums[:])&#10;            return&#10;        for i in range(idx, len(nums)):&#10;            nums[idx], nums[i] = nums[i], nums[idx]&#10;            solve(idx + 1)&#10;            nums[idx], nums[i] = nums[i], nums[idx]&#10;    solve(0)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>5</td>
      <td>Rec 05 Sudoku Solver<br><br></b> <a href="https://leetcode.com/problems/sudoku-solver/" target="_blank">LeetCode 37</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td><b>Example 1:</b> Input: board with '.' for empty cells. Solve in-place.</td>
      <td><b>Time:</b> O(9^(n*n))<br><b>Space:</b> O(1) auxiliary</td>
      <td><b>Explanation:</b> Backtracking. Find first empty cell, try placing 1-9. Validate row, col, and 3x3 sub-grid. Recursively solve the rest. If it fails, backtrack.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def solveSudoku(board: List[List[str]]) -&gt; None:&#10;    def isValid(row, col, ch):&#10;        for i in range(9):&#10;            if board[i][col] == ch: return False&#10;            if board[row][i] == ch: return False&#10;            if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == ch: return False&#10;        return True&#10;    def solve():&#10;        for i in range(len(board)):&#10;            for j in range(len(board[0])):&#10;                if board[i][j] == &#x27;.&#x27;:&#10;                    for c in &#x27;123456789&#x27;:&#10;                        if isValid(i, j, c):&#10;                            board[i][j] = c&#10;                            if solve(): return True&#10;                            else: board[i][j] = &#x27;.&#x27;&#10;                    return False&#10;        return True&#10;    solve()</code></pre></details></td>
    </tr>
    <tr>
      <td>6</td>
      <td>Rec 06 M Coloring Problem<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/m-coloring-problem-1587115620/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td><b>Example 1:</b> Return true if possible.</td>
      <td><b>Time:</b> O(M^N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Backtracking. Try coloring each node with color 1 to m. For a color, check if any adjacent node has the same color. If safe, assign and recurse for next node. If recursion returns false, backtrack.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def graphColoring(graph: List[List[int]], m: int, n: int) -&gt; bool:&#10;    color = [0] * n&#10;    def isSafe(node, col):&#10;        for k in range(n):&#10;            if k != node and graph[k][node] == 1 and color[k] == col: return False&#10;        return True&#10;    def solve(node):&#10;        if node == n: return True&#10;        for i in range(1, m + 1):&#10;            if isSafe(node, i):&#10;                color[node] = i&#10;                if solve(node + 1): return True&#10;                color[node] = 0&#10;        return False&#10;    return solve(0)</code></pre></details></td>
    </tr>
    <tr>
      <td>7</td>
      <td>Rec 07 Rat In A Maze<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td><b>Example 1:</b> Lexicographical order paths.</td>
      <td><b>Time:</b> O(4^(N*N))<br><b>Space:</b> O(N*N)</td>
      <td><b>Explanation:</b> Backtracking. Explore 4 directions (D, L, R, U) in lexicographical order to get sorted paths naturally. Mark cell as visited, recurse, then unmark (backtrack).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findPath(m: List[List[int]], n: int) -&gt; List[str]:&#10;    ans = []&#10;    vis = [[0 for _ in range(n)] for _ in range(n)]&#10;    di = [1, 0, 0, -1]&#10;    dj = [0, -1, 1, 0]&#10;    dir_str = &quot;DLRU&quot;&#10;    def solve(i, j, move):&#10;        if i == n - 1 and j == n - 1:&#10;            ans.append(move)&#10;            return&#10;        for ind in range(4):&#10;            nexti, nextj = i + di[ind], j + dj[ind]&#10;            if 0 &lt;= nexti &lt; n and 0 &lt;= nextj &lt; n and not vis[nexti][nextj] and m[nexti][nextj] == 1:&#10;                vis[i][j] = 1&#10;                solve(nexti, nextj, move + dir_str[ind])&#10;                vis[i][j] = 0&#10;    if m[0][0] == 1: solve(0, 0, &quot;&quot;)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>8</td>
      <td>Rec 08 Word Break<br><br></b> <a href="https://leetcode.com/problems/word-break/" target="_blank">LeetCode 139</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z, Apna College, SDE Sheet</details></td>
      <td><b>Example 1:</b> Input: s = 'leetcode', wordDict = ['leet','code'], Output: true</td>
      <td><b>Time:</b> O(N^3)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Recursion with Memoization (or DP). For each index, try all possible word lengths. If a prefix exists in dict, recurse for the suffix. DP array `dp[i]` stores if `s[0...i-1]` is valid.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def wordBreak(s: str, wordDict: List[str]) -&gt; bool:&#10;    word_set = set(wordDict)&#10;    dp = [False] * (len(s) + 1)&#10;    dp[0] = True&#10;    for i in range(1, len(s) + 1):&#10;        for j in range(i):&#10;            if dp[j] and s[j:i] in word_set:&#10;                dp[i] = True&#10;                break&#10;    return dp[-1]</code></pre></details></td>
    </tr>
    <tr>
      <td>9</td>
      <td>Rec 09 Word Break Ii<br><br></b> <a href="https://leetcode.com/problems/word-break-ii/" target="_blank">LeetCode 140</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td><b>Example 1:</b> Return list of sentences.</td>
      <td><b>Time:</b> O(2^N)<br><b>Space:</b> O(2^N)</td>
      <td><b>Explanation:</b> Backtracking. Generate all combinations. At each step, if a prefix is in dict, recursively call for the rest of the string and append the prefix to the result of the recursive call.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def wordBreak(s: str, wordDict: List[str]) -&gt; List[str]:&#10;    word_set = set(wordDict)&#10;    memo = {}&#10;    def solve(s):&#10;        if s in memo: return memo[s]&#10;        if not s: return [&quot;&quot;]&#10;        res = []&#10;        for i in range(1, len(s) + 1):&#10;            word = s[:i]&#10;            if word in word_set:&#10;                rem = solve(s[i:])&#10;                for st in rem:&#10;                    res.append(word + (&quot; &quot; if st else &quot;&quot;) + st)&#10;        memo[s] = res&#10;        return res&#10;    return solve(s)</code></pre></details></td>
    </tr>
    <tr>
      <td>10</td>
      <td>Rec 10 Palindrome Partitioning<br><br></b> <a href="https://leetcode.com/problems/palindrome-partitioning/" target="_blank">LeetCode 131</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td><b>Example 1:</b> Input: s = 'aab', Output: [['a','a','b'],['aa','b']]</td>
      <td><b>Time:</b> O(N * 2^N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Backtracking. Try to partition the string at every index. If the prefix `s[start:i]` is a palindrome, add it to current path and recurse for the rest of the string `s[i:end]`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def partition(s: str) -&gt; List[List[str]]:&#10;    res = []&#10;    path = []&#10;    def isPalindrome(s, start, end):&#10;        while start &lt;= end:&#10;            if s[start] != s[end]: return False&#10;            start += 1; end -= 1&#10;        return True&#10;    def solve(index):&#10;        if index == len(s):&#10;            res.append(list(path))&#10;            return&#10;        for i in range(index, len(s)):&#10;            if isPalindrome(s, index, i):&#10;                path.append(s[index:i+1])&#10;                solve(i + 1)&#10;                path.pop()&#10;    solve(0)&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td>11</td>
      <td>Rec 11 Expression Add Operators<br><br></b> <a href="https://leetcode.com/problems/expression-add-operators/" target="_blank">LeetCode 282</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td><b>Example 1:</b> Return expressions.</td>
      <td><b>Time:</b> O(N * 4^N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Backtracking. Keep track of the evaluated sum so far, and the previous operand (for multiplication precedence). For '*', `newSum = sum - prev + prev * curr`. Handle leading zeros.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def addOperators(num: str, target: int) -&gt; List[str]:&#10;    ans = []&#10;    def solve(ind, path, eval_sum, multed):&#10;        if ind == len(num):&#10;            if eval_sum == target: ans.append(path)&#10;            return&#10;        for i in range(ind, len(num)):&#10;            if i != ind and num[ind] == &#x27;0&#x27;: break&#10;            cur_str = num[ind:i+1]&#10;            cur_num = int(cur_str)&#10;            if ind == 0:&#10;                solve(i + 1, path + cur_str, cur_num, cur_num)&#10;            else:&#10;                solve(i + 1, path + &quot;+&quot; + cur_str, eval_sum + cur_num, cur_num)&#10;                solve(i + 1, path + &quot;-&quot; + cur_str, eval_sum - cur_num, -cur_num)&#10;                solve(i + 1, path + &quot;*&quot; + cur_str, eval_sum - multed + multed * cur_num, multed * cur_num)&#10;    solve(0, &quot;&quot;, 0, 0)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>12</td>
      <td>Rec 12 Subset Sums Ii<br><br></b> <a href="https://leetcode.com/problems/subsets-ii/" target="_blank">LeetCode 90</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td><b>Example 1:</b> Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]</td>
      <td><b>Time:</b> O(2^N * N)<br><b>Space:</b> O(2^N * N)</td>
      <td><b>Explanation:</b> Sort array first to bring duplicates together. In recursive call, loop from `ind` to `n`. If `i > ind` and `nums[i] == nums[i-1]`, `continue` to skip duplicate recursive branches.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def subsetsWithDup(nums: List[int]) -&gt; List[List[int]]:&#10;    ans = []&#10;    nums.sort()&#10;    def findSubsets(ind, ds):&#10;        ans.append(list(ds))&#10;        for i in range(ind, len(nums)):&#10;            if i != ind and nums[i] == nums[i-1]: continue&#10;            ds.append(nums[i])&#10;            findSubsets(i + 1, ds)&#10;            ds.pop()&#10;    findSubsets(0, [])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>13</td>
      <td>Rec 13 Combination Sum Ii<br><br></b> <a href="https://leetcode.com/problems/combination-sum-ii/" target="_blank">LeetCode 40</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td><b>Example 1:</b> Return unique combinations.</td>
      <td><b>Time:</b> O(2^N * k)<br><b>Space:</b> O(k * x)</td>
      <td><b>Explanation:</b> Sort the array. Recursive function iterates from `ind` to `n`. Skip duplicates (`if i > ind and arr[i] == arr[i-1]`). If `arr[i] > target`, break. Else add to path, subtract from target, and recurse.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def combinationSum2(candidates: List[int], target: int) -&gt; List[List[int]]:&#10;    ans = []&#10;    candidates.sort()&#10;    def findCombinations(ind, target, ds):&#10;        if target == 0:&#10;            ans.append(list(ds))&#10;            return&#10;        for i in range(ind, len(candidates)):&#10;            if i &gt; ind and candidates[i] == candidates[i-1]: continue&#10;            if candidates[i] &gt; target: break&#10;            ds.append(candidates[i])&#10;            findCombinations(i + 1, target - candidates[i], ds)&#10;            ds.pop()&#10;    findCombinations(0, target, [])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>14</td>
      <td>Rec 14 Combination Sum Iii<br><br></b> <a href="https://leetcode.com/problems/combination-sum-iii/" target="_blank">LeetCode 216</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td><b>Example 1:</b> Return combinations.</td>
      <td><b>Time:</b> O(2^9)<br><b>Space:</b> O(k)</td>
      <td><b>Explanation:</b> Backtracking. Start from 1, go up to 9. Add the current number to the path and subtract from target. Stop when path size is `k` and `target` is 0.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def combinationSum3(k: int, n: int) -&gt; List[List[int]]:&#10;    ans = []&#10;    def solve(start, k, n, ds):&#10;        if k == 0 and n == 0:&#10;            ans.append(list(ds))&#10;            return&#10;        if k == 0 or n &lt; 0: return&#10;        for i in range(start, 10):&#10;            ds.append(i)&#10;            solve(i + 1, k - 1, n - i, ds)&#10;            ds.pop()&#10;    solve(1, k, n, [])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>15</td>
      <td>Rec 15 Letter Combinations Of A Phone Number<br><br></b> <a href="https://leetcode.com/problems/letter-combinations-of-a-phone-number/" target="_blank">LeetCode 17</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td><b>Example 1:</b> String combinations.</td>
      <td><b>Time:</b> O(4^N * N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Backtracking. Create a mapping of digit to letters. Iterate through digits, for each digit loop through its mapped letters, append to current string, and recurse.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def letterCombinations(digits: str) -&gt; List[str]:&#10;    if not digits: return []&#10;    ans = []&#10;    mapping = [&quot;&quot;, &quot;&quot;, &quot;abc&quot;, &quot;def&quot;, &quot;ghi&quot;, &quot;jkl&quot;, &quot;mno&quot;, &quot;pqrs&quot;, &quot;tuv&quot;, &quot;wxyz&quot;]&#10;    def solve(ind, path):&#10;        if ind == len(digits):&#10;            ans.append(path)&#10;            return&#10;        number = int(digits[ind])&#10;        value = mapping[number]&#10;        for i in range(len(value)):&#10;            solve(ind + 1, path + value[i])&#10;    solve(0, &quot;&quot;)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>16</td>
      <td>Rec 16 Subset Sum I<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/subset-sums2234/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td><b>Example 1:</b> Take / Not Take.</td>
      <td><b>Time:</b> O(2^N)<br><b>Space:</b> O(2^N)</td>
      <td><b>Explanation:</b> Recursively either include `arr[ind]` in sum, or exclude it. If `ind == N`, add `sum` to result array.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def subsetSums(arr: List[int], N: int) -&gt; List[int]:&#10;    sumSubset = []&#10;    def func(ind, current_sum):&#10;        if ind == N:&#10;            sumSubset.append(current_sum)&#10;            return&#10;        func(ind + 1, current_sum + arr[ind])&#10;        func(ind + 1, current_sum)&#10;    func(0, 0)&#10;    sumSubset.sort()&#10;    return sumSubset</code></pre></details></td>
    </tr>
    <tr>
      <td>17</td>
      <td>Rec 17 N Queens Ii<br><br></b> <a href="https://leetcode.com/problems/n-queens-ii/" target="_blank">LeetCode 52</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td><b>Example 1:</b> Backtracking with hashing.</td>
      <td><b>Time:</b> O(N!)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Use backtracking to place queens column by column. Use three hash arrays (or bitmasks) to track attacked rows, upper diagonals, and lower diagonals. If placing a queen is safe, update hashes, recurse for next column, and then backtrack.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def totalNQueens(n: int) -&gt; int:&#10;    count = 0&#10;    leftRow = [0] * n&#10;    upperDiag = [0] * (2 * n - 1)&#10;    lowerDiag = [0] * (2 * n - 1)&#10;    def solve(col):&#10;        nonlocal count&#10;        if col == n:&#10;            count += 1&#10;            return&#10;        for row in range(n):&#10;            if leftRow[row] == 0 and lowerDiag[row + col] == 0 and upperDiag[n - 1 + col - row] == 0:&#10;                leftRow[row] = 1&#10;                lowerDiag[row + col] = 1&#10;                upperDiag[n - 1 + col - row] = 1&#10;                solve(col + 1)&#10;                leftRow[row] = 0&#10;                lowerDiag[row + col] = 0&#10;                upperDiag[n - 1 + col - row] = 0&#10;    solve(0)&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td>18</td>
      <td>Rec 18 Word Search<br><br></b> <a href="https://leetcode.com/problems/word-search/" target="_blank">LeetCode 79</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td><b>Example 1:</b> Backtracking DFS.</td>
      <td><b>Time:</b> O(N * M * 4^L)<br><b>Space:</b> O(L) recursion stack</td>
      <td><b>Explanation:</b> Start DFS from each cell that matches the first letter of the word. In DFS, check 4 neighbors. Mark current cell as visited (e.g. change to '#') before moving to neighbors, and unmark (backtrack) after exploring.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def exist(board: List[List[str]], word: str) -&gt; bool:&#10;    def dfs(i, j, idx):&#10;        if idx == len(word): return True&#10;        if i &lt; 0 or i &gt;= len(board) or j &lt; 0 or j &gt;= len(board[0]) or board[i][j] != word[idx]:&#10;            return False&#10;        temp = board[i][j]&#10;        board[i][j] = &#x27;#&#x27;&#10;        found = (dfs(i+1, j, idx+1) or dfs(i-1, j, idx+1) or&#10;                 dfs(i, j+1, idx+1) or dfs(i, j-1, idx+1))&#10;        board[i][j] = temp&#10;        return found&#10;    for i in range(len(board)):&#10;        for j in range(len(board[0])):&#10;            if board[i][j] == word[0] and dfs(i, j, 0):&#10;                return True&#10;    return False</code></pre></details></td>
    </tr>
    <tr>
      <td>19</td>
      <td>Rec 19 K Th Symbol In Grammar<br><br></b> <a href="https://leetcode.com/problems/k-th-symbol-in-grammar/" target="_blank">LeetCode 779</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td><b>Example 1:</b> Recursive division.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Row N has length 2^(N-1). The first half of row N is exactly same as row N-1. The second half of row N is the complement of row N-1. If k is in the first half (k <= mid), return solve(N-1, k). If k is in the second half, return !solve(N-1, k - mid).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def kthGrammar(n: int, k: int) -&gt; int:&#10;    if n == 1 and k == 1: return 0&#10;    mid = 2 ** (n - 2)&#10;    if k &lt;= mid:&#10;        return kthGrammar(n - 1, k)&#10;    else:&#10;        return 1 - kthGrammar(n - 1, k - mid)</code></pre></details></td>
    </tr>
    <tr>
      <td>20</td>
      <td>Rec 20 Beautiful Arrangement<br><br></b> <a href="https://leetcode.com/problems/beautiful-arrangement/" target="_blank">LeetCode 526</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td><b>Example 1:</b> Backtracking.</td>
      <td><b>Time:</b> O(K) where K is number of valid permutations<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Use an array to track visited numbers. Iterate from index 1 to n. For the current index, try placing an unvisited number. Check if the condition `(num % idx == 0 || idx % num == 0)` is met. If so, mark as visited, recurse to `idx + 1`, then backtrack.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def countArrangement(n: int) -&gt; int:&#10;    count = 0&#10;    visited = [0] * (n + 1)&#10;    def solve(idx):&#10;        nonlocal count&#10;        if idx &gt; n:&#10;            count += 1&#10;            return&#10;        for i in range(1, n + 1):&#10;            if not visited[i] and (i % idx == 0 or idx % i == 0):&#10;                visited[i] = 1&#10;                solve(idx + 1)&#10;                visited[i] = 0&#10;    solve(1)&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td>21</td>
      <td>Rec 21 Print All Permutations Of A String<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/permutations-of-a-given-string2041/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z, SDE Sheet</details></td>
      <td><b>Example 1:</b> Recursive Backtracking.</td>
      <td><b>Time:</b> O(N! * N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Convert string to char array and sort it. Use backtracking: pass a boolean visited array and a temporary string. If temporary string length equals original length, add to answer. Else, iterate through characters. To avoid duplicates, if `i > 0` and `s[i] == s[i-1]` and `!vis[i-1]`, skip. Otherwise, mark visited, append, recurse, unmark, pop.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def find_permutation(S: str) -&gt; List[str]:&#10;    S = sorted(list(S))&#10;    ans = []&#10;    vis = [False] * len(S)&#10;    def solve(curr):&#10;        if len(curr) == len(S):&#10;            ans.append(&quot;&quot;.join(curr))&#10;            return&#10;        for i in range(len(S)):&#10;            if vis[i] or (i &gt; 0 and S[i] == S[i-1] and not vis[i-1]):&#10;                continue&#10;            vis[i] = True&#10;            curr.append(S[i])&#10;            solve(curr)&#10;            curr.pop()&#10;            vis[i] = False&#10;    solve([])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>22</td>
      <td>Rec 22 Find All Possible Palindromic Partitions Of A String<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/find-all-possible-palindromic-partitions-of-a-string/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td><b>Example 1:</b> Recursive Backtracking.</td>
      <td><b>Time:</b> O(N * 2^N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Iterate through the string. Extract substring `S[ind..i]`. If it is a palindrome, add it to the current partition list and recursively call for `i+1`. When `ind == length`, push the partition list to the answer.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def allPalindromicPerms(S: str) -&gt; List[List[str]]:&#10;    ans = []&#10;    def is_pal(s): return s == s[::-1]&#10;    def solve(ind, curr):&#10;        if ind == len(S):&#10;            ans.append(curr[:])&#10;            return&#10;        for i in range(ind, len(S)):&#10;            sub = S[ind:i+1]&#10;            if is_pal(sub):&#10;                curr.append(sub)&#10;                solve(i + 1, curr)&#10;                curr.pop()&#10;    solve(0, [])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>23</td>
      <td>Rec 23 Print 1 To N Without Loop<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/print-1-to-n-without-using-loops-1587115620/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z</details></td>
      <td><b>Example 1:</b> Recursion.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Use a recursive function. Call `f(N-1)` first and then print `N`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def printTillN(N):&#10;    if N == 0: return&#10;    printTillN(N - 1)&#10;    print(N, end=&quot; &quot;)</code></pre></details></td>
    </tr>
    <tr>
      <td>24</td>
      <td>Rec 24 Print N To 1 Without Loop<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/print-n-to-1-without-loop/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z</details></td>
      <td><b>Example 1:</b> Recursion.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Use a recursive function. Print `N` first and then call `f(N-1)`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def printNos(N):&#10;    if N == 0: return&#10;    print(N, end=&quot; &quot;)&#10;    printNos(N - 1)</code></pre></details></td>
    </tr>
    <tr>
      <td>25</td>
      <td>Rec 25 Sum Of First N Terms<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/sum-of-first-n-terms5843/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z</details></td>
      <td><b>Example 1:</b> Math or Recursion.</td>
      <td><b>Time:</b> O(1) Math, O(N) Recursion<br><b>Space:</b> O(1) Math, O(N) Recursion</td>
      <td><b>Explanation:</b> The mathematical formula for the sum of cubes is `(n * (n + 1) / 2)^2`. Alternatively, use recursion `f(n) = n^3 + f(n-1)`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def sumOfSeries(n):&#10;    return (n * (n + 1) // 2) ** 2</code></pre></details></td>
    </tr>
    <tr>
      <td>26</td>
      <td>Rec 26 Find All Factorial Numbers Less Than Or Equal To N<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/find-all-factorial-numbers-less-than-or-equal-to-n3548/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z</details></td>
      <td><b>Example 1:</b> Recursion.</td>
      <td><b>Time:</b> O(K) where K! <= N<br><b>Space:</b> O(K)</td>
      <td><b>Explanation:</b> Maintain a current factorial value and an index `i`. At each recursive step, compute the next factorial by multiplying by `i`. If the next factorial is `<= n`, add it to the list and recurse.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def factorialNumbers(N):&#10;    ans = []&#10;    def findFactorials(i, fact):&#10;        if fact &gt; N: return&#10;        ans.append(fact)&#10;        findFactorials(i + 1, fact * (i + 1))&#10;    findFactorials(1, 1)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>27</td>
      <td>Rec 27 Reverse An Array<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/reverse-an-array/0" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z</details></td>
      <td><b>Example 1:</b> Recursion with two pointers.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N) recursive stack</td>
      <td><b>Explanation:</b> Swap `arr[l]` and `arr[r]` and then recursively call `reverse(arr, l+1, r-1)`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def reverseArray(arr, l, r):&#10;    if l &gt;= r: return&#10;    arr[l], arr[r] = arr[r], arr[l]&#10;    reverseArray(arr, l + 1, r - 1)</code></pre></details></td>
    </tr>
    <tr>
      <td>28</td>
      <td>Rec 28 Fibonacci Number<br><br></b> <a href="https://leetcode.com/problems/fibonacci-number/" target="_blank">LeetCode 509</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z</details></td>
      <td><b>Example 1:</b> Base Case.</td>
      <td><b>Time:</b> O(2^N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Return `fib(n-1) + fib(n-2)` with base cases `fib(0) = 0`, `fib(1) = 1`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def fib(n):&#10;    if n &lt;= 1: return n&#10;    return fib(n - 1) + fib(n - 2)</code></pre></details></td>
    </tr>
    <tr>
      <td>29</td>
      <td>Rec 29 Count Good Numbers<br><br></b> <a href="https://leetcode.com/problems/count-good-numbers/" target="_blank">LeetCode 1922</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z</details></td>
      <td><b>Example 1:</b> Modular Exponentiation.</td>
      <td><b>Time:</b> O(log N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> There are 5 even digits and 4 prime digits. At even indices we have 5 choices. At odd indices we have 4 choices. If `n` is even, we have `n/2` even indices and `n/2` odd indices. So answer is `(5^(n/2) * 4^(n/2)) % mod`. If `n` is odd, we have `n/2 + 1` even indices. So answer is `(5^(n/2 + 1) * 4^(n/2)) % mod`. Use binary exponentiation.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def countGoodNumbers(n):&#10;    mod = 10**9 + 7&#10;    def power(x, y):&#10;        res = 1&#10;        x = x % mod&#10;        while y &gt; 0:&#10;            if y % 2 == 1: res = (res * x) % mod&#10;            y = y // 2&#10;            x = (x * x) % mod&#10;        return res&#10;    evenIndices = (n + 1) // 2&#10;    oddIndices = n // 2&#10;    return (power(5, evenIndices) * power(4, oddIndices)) % mod</code></pre></details></td>
    </tr>
    <tr>
      <td>30</td>
      <td>Rec 30 Sort A Stack Using Recursion<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/sort-a-stack/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td><b>Example 1:</b> Recursive sort and insert.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Recursively pop elements until the stack is empty. When returning from the recursive call, use another recursive function `sortedInsert` to insert the popped element into its correct sorted position in the stack.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def sortedInsert(s, element):&#10;    if not s or element &gt; s[-1]:&#10;        s.append(element)&#10;        return&#10;    num = s.pop()&#10;    sortedInsert(s, element)&#10;    s.append(num)&#10;def sortStack(s):&#10;    if not s: return&#10;    num = s.pop()&#10;    sortStack(s)&#10;    sortedInsert(s, num)</code></pre></details></td>
    </tr>
  </tbody>
</table>
