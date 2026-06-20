# 14 DP Revision Table

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
      <td>Rec 01 Word Break<br><br></b> <a href="https://leetcode.com/problems/word-break/" target="_blank">LeetCode 139</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> SDE Sheet, Striver A Z, Apna College, Love Babbar</details></td>
      <td>**Example 1:** Input: s = 'leetcode', wordDict = ['leet','code'], Output: true</td>
      <td><b>Time:</b> O(N^3)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Recursion with Memoization (or DP). For each index, try all possible word lengths. If a prefix exists in dict, recurse for the suffix. DP array `dp[i]` stores if `s[0...i-1]` is valid.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def wordBreak(s: str, wordDict: List[str]) -&gt; bool:&#10;    word_set = set(wordDict)&#10;    dp = [False] * (len(s) + 1)&#10;    dp[0] = True&#10;    for i in range(1, len(s) + 1):&#10;        for j in range(i):&#10;            if dp[j] and s[j:i] in word_set:&#10;                dp[i] = True&#10;                break&#10;    return dp[-1]</code></pre></details></td>
    </tr>
    <tr>
      <td>2</td>
      <td>Dp 02 Matrix Chain Multiplication<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> SDE Sheet, Striver A Z, Apna College, Love Babbar</details></td>
      <td>**Example 1:** Input: N=5, arr=[40, 20, 30, 10, 30], Output: 26000</td>
      <td><b>Time:</b> O(N^3)<br><b>Space:</b> O(N^2)</td>
      <td><b>Explanation:</b> Partition DP. Try partitioning the matrices at every possible split `k` between `i` and `j`. Cost is `arr[i-1]*arr[k]*arr[j]`. Take the minimum.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def matrixMultiplication(N: int, arr: List[int]) -&gt; int:&#10;    dp = [[-1] * N for _ in range(N)]&#10;    def f(i, j):&#10;        if i == j: return 0&#10;        if dp[i][j] != -1: return dp[i][j]&#10;        mini = int(1e9)&#10;        for k in range(i, j):&#10;            steps = arr[i-1] * arr[k] * arr[j] + f(i, k) + f(k+1, j)&#10;            mini = min(mini, steps)&#10;        dp[i][j] = mini&#10;        return mini&#10;    return f(1, N-1)</code></pre></details></td>
    </tr>
    <tr>
      <td>3</td>
      <td>Dp 03 Subset Sum Problem<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet, Apna College</details></td>
      <td>**Example 1:** Input: set=[3,34,4,12,5,2], sum=9, Output: True</td>
      <td><b>Time:</b> O(N * Sum)<br><b>Space:</b> O(Sum) space optimized</td>
      <td><b>Explanation:</b> DP logic like 0/1 Knapsack. DP state is `dp[index][target]`. At each index, you can take or not take the element if `target >= arr[i]`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isSubsetSum(arr: List[int], sum: int) -&gt; bool:&#10;    n = len(arr)&#10;    prev = [False] * (sum + 1)&#10;    prev[0] = True&#10;    if arr[0] &lt;= sum: prev[arr[0]] = True&#10;    for ind in range(1, n):&#10;        cur = [False] * (sum + 1)&#10;        cur[0] = True&#10;        for target in range(1, sum + 1):&#10;            notTaken = prev[target]&#10;            taken = False&#10;            if arr[ind] &lt;= target: taken = prev[target - arr[ind]]&#10;            cur[target] = notTaken or taken&#10;        prev = cur&#10;    return prev[sum]</code></pre></details></td>
    </tr>
  </tbody>
</table>
