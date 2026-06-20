# Day 25 to 27 DP Revision Table

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
      <td>Rec 01 Word Break<br><br></b> <a href="https://leetcode.com/problems/word-break/" target="_blank">LeetCode 139</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> SDE Sheet, Love Babbar, Apna College, Striver A Z</details></td>
      <td>**Example 1:** Input: s = 'leetcode', wordDict = ['leet','code'], Output: true</td>
      <td><b>Time:</b> O(N^3)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Recursion with Memoization (or DP). For each index, try all possible word lengths. If a prefix exists in dict, recurse for the suffix. DP array `dp[i]` stores if `s[0...i-1]` is valid.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def wordBreak(s: str, wordDict: List[str]) -&gt; bool:&#10;    word_set = set(wordDict)&#10;    dp = [False] * (len(s) + 1)&#10;    dp[0] = True&#10;    for i in range(1, len(s) + 1):&#10;        for j in range(i):&#10;            if dp[j] and s[j:i] in word_set:&#10;                dp[i] = True&#10;                break&#10;    return dp[-1]</code></pre></details></td>
    </tr>
    <tr>
      <td>2</td>
      <td>Dp 02 Climbing Stairs<br><br></b> <a href="https://leetcode.com/problems/climbing-stairs/" target="_blank">LeetCode 70</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: n = 3, Output: 3 (1+1+1, 1+2, 2+1)</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><b>Explanation:</b> Space Optimization (Bottom-Up): Since state `n` only depends on `n-1` and `n-2`, we only need two variables.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def climbStairs(n: int) -&gt; int:&#10;    if n &lt;= 1: return 1&#10;    prev2, prev = 1, 1&#10;    for i in range(2, n + 1):&#10;        curr = prev + prev2&#10;        prev2, prev = prev, curr&#10;    return prev</code></pre></details></td>
    </tr>
    <tr>
      <td>3</td>
      <td>Dp 03 Longest Common Subsequence<br><br></b> <a href="https://leetcode.com/problems/longest-common-subsequence/" target="_blank">LeetCode 1143</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> SDE Sheet, Love Babbar, Striver A Z</details></td>
      <td>**Example 1:** Input: text1 = "abcde", text2 = "ace", Output: 3 ("ace")</td>
      <td><b>Time:</b> O(M * N) (Constraint)<br><b>Space:</b> O(M * N) (Trade-off)</td>
      <td><b>Explanation:</b> Tabulation (Bottom-Up). Use a 2D array where `dp[i][j]` represents the LCS of prefixes of length `i` and `j`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def longestCommonSubsequence(text1: str, text2: str) -&gt; int:&#10;    n, m = len(text1), len(text2)&#10;    dp = [[0] * (m + 1) for _ in range(n + 1)]&#10;    for i in range(1, n + 1):&#10;        for j in range(1, m + 1):&#10;            if text1[i - 1] == text2[j - 1]:&#10;                dp[i][j] = 1 + dp[i - 1][j - 1]&#10;            else:&#10;                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])&#10;    return dp[n][m]</code></pre></details></td>
    </tr>
    <tr>
      <td>4</td>
      <td>Dp 04 Coin Change<br><br></b> <a href="https://leetcode.com/problems/coin-change/" target="_blank">LeetCode 322</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> SDE Sheet, Love Babbar, Striver A Z</details></td>
      <td>**Example 1:** Input: coins = [1,2,5], amount = 11, Output: 3 (5+5+1)</td>
      <td><b>Time:</b> O(Amount * N)<br><b>Space:</b> O(Amount)</td>
      <td><b>Explanation:</b> Unbounded Knapsack. State `dp[i]` is the min coins needed to make amount `i`. `dp[i] = min(dp[i], 1 + dp[i - coin])`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def coinChange(coins: list[int], amount: int) -&gt; int:&#10;    dp = [amount + 1] * (amount + 1)&#10;    dp[0] = 0&#10;    for i in range(1, amount + 1):&#10;        for coin in coins:&#10;            if i - coin &gt;= 0:&#10;                dp[i] = min(dp[i], 1 + dp[i - coin])&#10;    return dp[amount] if dp[amount] &lt;= amount else -1</code></pre></details></td>
    </tr>
    <tr>
      <td>5</td>
      <td>Dp 05 Longest Increasing Subsequence<br><br></b> <a href="https://leetcode.com/problems/longest-increasing-subsequence/" target="_blank">LeetCode 300</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> SDE Sheet, Love Babbar, Striver A Z</details></td>
      <td>**Example 1:** Input: nums = [10,9,2,5,3,7,101,18], Output: 4 ([2,3,7,101])</td>
      <td><b>Time:</b> O(N log N) (Constraint)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Binary Search Patience Sorting method. Maintain a `temp` array. If current element is larger than `temp.back()`, append. Else, replace the first element >= current.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import bisect&#10;def lengthOfLIS(nums: list[int]) -&gt; int:&#10;    temp = []&#10;    for num in nums:&#10;        idx = bisect.bisect_left(temp, num)&#10;        if idx == len(temp):&#10;            temp.append(num)&#10;        else:&#10;            temp[idx] = num&#10;    return len(temp)</code></pre></details></td>
    </tr>
    <tr>
      <td>6</td>
      <td>Dp 06 House Robber<br><br></b> <a href="https://leetcode.com/problems/house-robber/" target="_blank">LeetCode 198</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: nums = [1,2,3,1], Output: 4 (Rob house 1 and 3)</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Space Optimized DP. Maintain two variables: `prev1` (max up to previous house) and `prev2` (max up to the house before previous). `curr = max(num + prev2, prev1)`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def rob(nums: list[int]) -&gt; int:&#10;    prev1, prev2 = 0, 0&#10;    for num in nums:&#10;        curr = max(num + prev2, prev1)&#10;        prev2 = prev1&#10;        prev1 = curr&#10;    return prev1</code></pre></details></td>
    </tr>
    <tr>
      <td>7</td>
      <td>Dp 07 01 Knapsack<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> SDE Sheet, Love Babbar, Striver A Z</details></td>
      <td>**Example 1:** Input: N=3, W=4, values[]={1,2,3}, weight[]={4,5,1}, Output: 3</td>
      <td><b>Time:</b> O(N * W)<br><b>Space:</b> O(W)</td>
      <td><b>Explanation:</b> 2D DP or 1D array space-optimized DP. Check take and not-take scenarios.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def knapSack(W: int, wt: List[int], val: List[int], n: int) -&gt; int:&#10;    prev = [0] * (W + 1)&#10;    for w in range(wt[0], W + 1): prev[w] = val[0]&#10;    for ind in range(1, n):&#10;        for w in range(W, -1, -1):&#10;            notTake = prev[w]&#10;            take = float(&#x27;-inf&#x27;)&#10;            if wt[ind] &lt;= w: take = val[ind] + prev[w - wt[ind]]&#10;            prev[w] = max(take, notTake)&#10;    return prev[W]</code></pre></details></td>
    </tr>
    <tr>
      <td>8</td>
      <td>Dp 08 Edit Distance<br><br></b> <a href="https://leetcode.com/problems/edit-distance/" target="_blank">LeetCode 72</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: word1 = 'horse', word2 = 'ros', Output: 3</td>
      <td><b>Time:</b> O(N * M)<br><b>Space:</b> O(M)</td>
      <td><b>Explanation:</b> 2D DP. If chars match, dp[i-1][j-1]. Else, 1 + min(insert, delete, replace).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minDistance(word1: str, word2: str) -&gt; int:&#10;    n, m = len(word1), len(word2)&#10;    prev = list(range(m+1))&#10;    for i in range(1, n+1):&#10;        cur = [i] + [0]*m&#10;        for j in range(1, m+1):&#10;            if word1[i-1] == word2[j-1]: cur[j] = prev[j-1]&#10;            else: cur[j] = 1 + min(prev[j], cur[j-1], prev[j-1])&#10;        prev = cur&#10;    return prev[m]</code></pre></details></td>
    </tr>
    <tr>
      <td>9</td>
      <td>Dp 09 Matrix Chain Multiplication<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, Apna College, SDE Sheet</details></td>
      <td>**Example 1:** Input: N=5, arr=[40, 20, 30, 10, 30], Output: 26000</td>
      <td><b>Time:</b> O(N^3)<br><b>Space:</b> O(N^2)</td>
      <td><b>Explanation:</b> Partition DP. Try partitioning the matrices at every possible split `k` between `i` and `j`. Cost is `arr[i-1]*arr[k]*arr[j]`. Take the minimum.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def matrixMultiplication(N: int, arr: List[int]) -&gt; int:&#10;    dp = [[-1] * N for _ in range(N)]&#10;    def f(i, j):&#10;        if i == j: return 0&#10;        if dp[i][j] != -1: return dp[i][j]&#10;        mini = int(1e9)&#10;        for k in range(i, j):&#10;            steps = arr[i-1] * arr[k] * arr[j] + f(i, k) + f(k+1, j)&#10;            mini = min(mini, steps)&#10;        dp[i][j] = mini&#10;        return mini&#10;    return f(1, N-1)</code></pre></details></td>
    </tr>
    <tr>
      <td>10</td>
      <td>Dp 10 Subset Sum Problem<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet, Apna College</details></td>
      <td>**Example 1:** Input: set=[3,34,4,12,5,2], sum=9, Output: True</td>
      <td><b>Time:</b> O(N * Sum)<br><b>Space:</b> O(Sum) space optimized</td>
      <td><b>Explanation:</b> DP logic like 0/1 Knapsack. DP state is `dp[index][target]`. At each index, you can take or not take the element if `target >= arr[i]`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isSubsetSum(arr: List[int], sum: int) -&gt; bool:&#10;    n = len(arr)&#10;    prev = [False] * (sum + 1)&#10;    prev[0] = True&#10;    if arr[0] &lt;= sum: prev[arr[0]] = True&#10;    for ind in range(1, n):&#10;        cur = [False] * (sum + 1)&#10;        cur[0] = True&#10;        for target in range(1, sum + 1):&#10;            notTaken = prev[target]&#10;            taken = False&#10;            if arr[ind] &lt;= target: taken = prev[target - arr[ind]]&#10;            cur[target] = notTaken or taken&#10;        prev = cur&#10;    return prev[sum]</code></pre></details></td>
    </tr>
  </tbody>
</table>
