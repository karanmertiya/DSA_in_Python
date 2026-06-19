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
      <td>1</td>
      <td>Dp 01 Climbing Stairs<br><br></b> <a href='https://leetcode.com/problems/climbing-stairs/' target='_blank'>LeetCode 70</a></td>
      <td><b>Example 1:</b> Input: n = 3, Output: 3 (1+1+1, 1+2, 2+1)</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1) (Constraint)</td>
      <td>-</td>
      <td><b>Variable Swapping:</b> `prev2` becomes `prev`, and `prev` becomes the new `curr`.</td>
      <td><b>Explanation:</b> Space Optimization (Bottom-Up): Since state `n` only depends on `n-1` and `n-2`, we only need two variables.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def climbStairs(n: int) -&gt; int:&#10;    if n &lt;= 1: return 1&#10;    prev2, prev = 1, 1&#10;    for i in range(2, n + 1):&#10;        curr = prev + prev2&#10;        prev2, prev = prev, curr&#10;    return prev</code></pre></details></td>
    </tr>
    <tr>
      <td>2</td>
      <td>Dp 02 Longest Common Subsequence<br><br></b> <a href='https://leetcode.com/problems/longest-common-subsequence/' target='_blank'>LeetCode 1143</a></td>
      <td><b>Example 1:</b> Input: text1 = "abcde", text2 = "ace", Output: 3 ("ace")</td>
      <td><b>Time:</b> O(M * N) (Constraint)<br><b>Space:</b> O(M * N) (Trade-off)</td>
      <td><code>std::max</code></td>
      <td><b>1-Based Indexing:</b> Shifting indices by 1 prevents out-of-bounds checks and elegantly handles the 0-length prefix base case.</td>
      <td><b>Explanation:</b> Tabulation (Bottom-Up). Use a 2D array where `dp[i][j]` represents the LCS of prefixes of length `i` and `j`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def longestCommonSubsequence(text1: str, text2: str) -&gt; int:&#10;    n, m = len(text1), len(text2)&#10;    dp = [[0] * (m + 1) for _ in range(n + 1)]&#10;    for i in range(1, n + 1):&#10;        for j in range(1, m + 1):&#10;            if text1[i - 1] == text2[j - 1]:&#10;                dp[i][j] = 1 + dp[i - 1][j - 1]&#10;            else:&#10;                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])&#10;    return dp[n][m]</code></pre></details></td>
    </tr>
    <tr>
      <td>3</td>
      <td>Dp 03 Coin Change<br><br></b> <a href='https://leetcode.com/problems/coin-change/' target='_blank'>LeetCode 322</a></td>
      <td><b>Example 1:</b> Input: coins = [1,2,5], amount = 11, Output: 3 (5+5+1)</td>
      <td><b>Time:</b> O(Amount * N)<br><b>Space:</b> O(Amount)</td>
      <td><code>std::min</code></td>
      <td><b>Initialization:</b> Fill array with `Amount + 1` (acting as infinity). If `dp[Amount]` remains `Amount + 1`, return `-1`.</td>
      <td><b>Explanation:</b> Unbounded Knapsack. State `dp[i]` is the min coins needed to make amount `i`. `dp[i] = min(dp[i], 1 + dp[i - coin])`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def coinChange(coins: list[int], amount: int) -&gt; int:&#10;    dp = [amount + 1] * (amount + 1)&#10;    dp[0] = 0&#10;    for i in range(1, amount + 1):&#10;        for coin in coins:&#10;            if i - coin &gt;= 0:&#10;                dp[i] = min(dp[i], 1 + dp[i - coin])&#10;    return dp[amount] if dp[amount] &lt;= amount else -1</code></pre></details></td>
    </tr>
    <tr>
      <td>4</td>
      <td>Dp 04 Longest Increasing Subsequence<br><br></b> <a href='https://leetcode.com/problems/longest-increasing-subsequence/' target='_blank'>LeetCode 300</a></td>
      <td><b>Example 1:</b> Input: nums = [10,9,2,5,3,7,101,18], Output: 4 ([2,3,7,101])</td>
      <td><b>Time:</b> O(N log N) (Constraint)<br><b>Space:</b> O(N)</td>
      <td><code>std::lower_bound</code> / <code>bisect_left</code></td>
      <td><b>Temp Array:</b> `temp` does NOT store the actual LIS, but its length correctly represents the LIS length.</td>
      <td><b>Explanation:</b> Binary Search Patience Sorting method. Maintain a `temp` array. If current element is larger than `temp.back()`, append. Else, replace the first element >= current.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import bisect&#10;def lengthOfLIS(nums: list[int]) -&gt; int:&#10;    temp = []&#10;    for num in nums:&#10;        idx = bisect.bisect_left(temp, num)&#10;        if idx == len(temp):&#10;            temp.append(num)&#10;        else:&#10;            temp[idx] = num&#10;    return len(temp)</code></pre></details></td>
    </tr>
    <tr>
      <td>5</td>
      <td>Dp 05 House Robber<br><br></b> <a href='https://leetcode.com/problems/house-robber/' target='_blank'>LeetCode 198</a></td>
      <td><b>Example 1:</b> Input: nums = [1,2,3,1], Output: 4 (Rob house 1 and 3)</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><code>std::max</code></td>
      <td><b>Array length < 2:</b> Automatically handled if initialized properly and loop condition ensures no out-of-bounds.</td>
      <td><b>Explanation:</b> Space Optimized DP. Maintain two variables: `prev1` (max up to previous house) and `prev2` (max up to the house before previous). `curr = max(num + prev2, prev1)`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def rob(nums: list[int]) -&gt; int:&#10;    prev1, prev2 = 0, 0&#10;    for num in nums:&#10;        curr = max(num + prev2, prev1)&#10;        prev2 = prev1&#10;        prev1 = curr&#10;    return prev1</code></pre></details></td>
    </tr>
    <tr>
      <td>6</td>
      <td>Dp 06 Maximum Product Subarray<br><br></b> <a href='https://leetcode.com/problems/maximum-product-subarray/' target='_blank'>LeetCode 152</a></td>
      <td><b>Example 1:</b> Input: nums = [2,3,-2,4], Output: 6 ([2,3])</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><code>std::max</code></td>
      <td><b>Zero Element:</b> A zero resets the contiguous product segment. We restart the prefix/suffix product from `1`.</td>
      <td><b>Explanation:</b> Prefix and Suffix product approach. Calculate product from left to right and right to left. Reset product to 1 when a zero is encountered.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxProduct(nums: list[int]) -&gt; int:&#10;    max_prod = float(&#x27;-inf&#x27;)&#10;    pref, suff = 1, 1&#10;    n = len(nums)&#10;    for i in range(n):&#10;        if pref == 0: pref = 1&#10;        if suff == 0: suff = 1&#10;        pref *= nums[i]&#10;        suff *= nums[n - 1 - i]&#10;        max_prod = max(max_prod, pref, suff)&#10;    return int(max_prod)</code></pre></details></td>
    </tr>
    <tr>
      <td>7</td>
      <td>Dp 06 Longest Increasing Subsequence<br><br></b> <a href='https://leetcode.com/problems/longest-increasing-subsequence/' target='_blank'>LeetCode 300</a></td>
      <td><b>Example 1:</b> Input: nums = [10,9,2,5,3,7,101,18], Output: 4 (LIS is [2,3,7,101])</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td><b>Empty Array:</b> Handled appropriately.</td>
      <td><b>Explanation:</b> Create a dp array where dp[i] is the length of LIS ending at index i. For each i, check all j < i to see if nums[i] > nums[j] and update dp[i] = max(dp[i], dp[j] + 1). O(N log N) patience sorting approach is better but standard DP is O(N^2).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def lengthOfLIS(nums: List[int]) -&gt; int:&#10;    if not nums: return 0&#10;    dp = [1] * len(nums)&#10;    for i in range(1, len(nums)):&#10;        for j in range(i):&#10;            if nums[i] &gt; nums[j]: dp[i] = max(dp[i], dp[j] + 1)&#10;    return max(dp)</code></pre></details></td>
    </tr>
    <tr>
      <td>8</td>
      <td>Dp 07 Coin Change<br><br></b> <a href='https://leetcode.com/problems/coin-change/' target='_blank'>LeetCode 322</a></td>
      <td><b>Example 1:</b> Input: coins = [1,2,5], amount = 11, Output: 3 (5+5+1)</td>
      <td><b>Time:</b> O(amount * N)<br><b>Space:</b> O(amount)</td>
      <td>-</td>
      <td><b>Cannot make amount:</b> Check if dp[amount] > amount, return -1.</td>
      <td><b>Explanation:</b> Bottom-up DP. dp[i] = min coins for amount i. Initialize dp array with amount + 1. dp[i] = min(dp[i], dp[i - coin] + 1).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def coinChange(coins: List[int], amount: int) -&gt; int:&#10;    dp = [amount + 1] * (amount + 1)&#10;    dp[0] = 0&#10;    for i in range(1, amount + 1):&#10;        for c in coins:&#10;            if i - c &gt;= 0: dp[i] = min(dp[i], dp[i - c] + 1)&#10;    return dp[amount] if dp[amount] != amount + 1 else -1</code></pre></details></td>
    </tr>
    <tr>
      <td>9</td>
      <td>Dp 08 01 Knapsack<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Input: N=3, W=4, values[]={1,2,3}, weight[]={4,5,1}, Output: 3</td>
      <td><b>Time:</b> O(N * W)<br><b>Space:</b> O(W)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> 2D DP or 1D array space-optimized DP. Check take and not-take scenarios.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def knapSack(W: int, wt: List[int], val: List[int], n: int) -&gt; int:&#10;    prev = [0] * (W + 1)&#10;    for w in range(wt[0], W + 1): prev[w] = val[0]&#10;    for ind in range(1, n):&#10;        for w in range(W, -1, -1):&#10;            notTake = prev[w]&#10;            take = float(&#x27;-inf&#x27;)&#10;            if wt[ind] &lt;= w: take = val[ind] + prev[w - wt[ind]]&#10;            prev[w] = max(take, notTake)&#10;    return prev[W]</code></pre></details></td>
    </tr>
    <tr>
      <td>10</td>
      <td>Dp 09 Longest Common Subsequence<br><br></b> <a href='https://leetcode.com/problems/longest-common-subsequence/' target='_blank'>LeetCode 1143</a></td>
      <td><b>Example 1:</b> Input: text1 = 'abcde', text2 = 'ace', Output: 3</td>
      <td><b>Time:</b> O(N * M)<br><b>Space:</b> O(N * M)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> 2D DP. If match, 1 + dp[i-1][j-1]. If not match, max(dp[i-1][j], dp[i][j-1]).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def longestCommonSubsequence(text1: str, text2: str) -&gt; int:&#10;    n, m = len(text1), len(text2)&#10;    dp = [[0]*(m+1) for _ in range(n+1)]&#10;    for i in range(1, n+1):&#10;        for j in range(1, m+1):&#10;            if text1[i-1] == text2[j-1]: dp[i][j] = 1 + dp[i-1][j-1]&#10;            else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])&#10;    return dp[n][m]</code></pre></details></td>
    </tr>
    <tr>
      <td>11</td>
      <td>Dp 10 Edit Distance<br><br></b> <a href='https://leetcode.com/problems/edit-distance/' target='_blank'>LeetCode 72</a></td>
      <td><b>Example 1:</b> Input: word1 = 'horse', word2 = 'ros', Output: 3</td>
      <td><b>Time:</b> O(N * M)<br><b>Space:</b> O(M)</td>
      <td>-</td>
      <td><b>Empty Strings:</b> Deletions/insertions equal to length.</td>
      <td><b>Explanation:</b> 2D DP. If chars match, dp[i-1][j-1]. Else, 1 + min(insert, delete, replace).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minDistance(word1: str, word2: str) -&gt; int:&#10;    n, m = len(word1), len(word2)&#10;    prev = list(range(m+1))&#10;    for i in range(1, n+1):&#10;        cur = [i] + [0]*m&#10;        for j in range(1, m+1):&#10;            if word1[i-1] == word2[j-1]: cur[j] = prev[j-1]&#10;            else: cur[j] = 1 + min(prev[j], cur[j-1], prev[j-1])&#10;        prev = cur&#10;    return prev[m]</code></pre></details></td>
    </tr>
    <tr>
      <td>12</td>
      <td>Dp 11 Matrix Chain Multiplication<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Input: N=5, arr=[40, 20, 30, 10, 30], Output: 26000</td>
      <td><b>Time:</b> O(N^3)<br><b>Space:</b> O(N^2)</td>
      <td><code>#include <vector></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Partition DP. Try partitioning the matrices at every possible split `k` between `i` and `j`. Cost is `arr[i-1]*arr[k]*arr[j]`. Take the minimum.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def matrixMultiplication(N: int, arr: List[int]) -&gt; int:&#10;    dp = [[-1] * N for _ in range(N)]&#10;    def f(i, j):&#10;        if i == j: return 0&#10;        if dp[i][j] != -1: return dp[i][j]&#10;        mini = int(1e9)&#10;        for k in range(i, j):&#10;            steps = arr[i-1] * arr[k] * arr[j] + f(i, k) + f(k+1, j)&#10;            mini = min(mini, steps)&#10;        dp[i][j] = mini&#10;        return mini&#10;    return f(1, N-1)</code></pre></details></td>
    </tr>
    <tr>
      <td>13</td>
      <td>Dp 12 Subset Sum Problem<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Input: set=[3,34,4,12,5,2], sum=9, Output: True</td>
      <td><b>Time:</b> O(N * Sum)<br><b>Space:</b> O(Sum) space optimized</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> DP logic like 0/1 Knapsack. DP state is `dp[index][target]`. At each index, you can take or not take the element if `target >= arr[i]`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isSubsetSum(arr: List[int], sum: int) -&gt; bool:&#10;    n = len(arr)&#10;    prev = [False] * (sum + 1)&#10;    prev[0] = True&#10;    if arr[0] &lt;= sum: prev[arr[0]] = True&#10;    for ind in range(1, n):&#10;        cur = [False] * (sum + 1)&#10;        cur[0] = True&#10;        for target in range(1, sum + 1):&#10;            notTaken = prev[target]&#10;            taken = False&#10;            if arr[ind] &lt;= target: taken = prev[target - arr[ind]]&#10;            cur[target] = notTaken or taken&#10;        prev = cur&#10;    return prev[sum]</code></pre></details></td>
    </tr>
    <tr>
      <td>14</td>
      <td>Dp 13 Word Break<br><br></b> <a href='https://leetcode.com/problems/word-break/' target='_blank'>LeetCode 139</a></td>
      <td><b>Example 1:</b> Input: s='leetcode', wordDict=['leet', 'code'], Output: true</td>
      <td><b>Time:</b> O(N^3)<br><b>Space:</b> O(N)</td>
      <td><code>#include <unordered_set></code></td>
      <td>-</td>
      <td><b>Explanation:</b> 1D DP array. `dp[i]` is true if string up to index `i` can be broken. Loop `i` from 1 to N, loop `j` from 0 to i. If `dp[j]` is true and `s[j...i]` is in dict, then `dp[i] = true`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def wordBreak(s: str, wordDict: List[str]) -&gt; bool:&#10;    wordSet = set(wordDict)&#10;    dp = [False] * (len(s) + 1)&#10;    dp[0] = True&#10;    for i in range(1, len(s) + 1):&#10;        for j in range(i):&#10;            if dp[j] and s[j:i] in wordSet:&#10;                dp[i] = True&#10;                break&#10;    return dp[len(s)]</code></pre></details></td>
    </tr>
    <tr>
      <td>15</td>
      <td>Dp 14 Longest Common Subsequence<br><br></b> <a href='https://leetcode.com/problems/longest-common-subsequence/' target='_blank'>LeetCode 1143</a></td>
      <td><b>Example 1:</b> Input: text1 = 'abcde', text2 = 'ace', Output: 3</td>
      <td><b>Time:</b> O(N * M)<br><b>Space:</b> O(M)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> 2D DP. If characters match, `dp[i][j] = 1 + dp[i-1][j-1]`. If they don't, `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`. Can be space optimized to two 1D arrays.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def longestCommonSubsequence(text1: str, text2: str) -&gt; int:&#10;    n, m = len(text1), len(text2)&#10;    prev = [0] * (m + 1)&#10;    for i in range(1, n + 1):&#10;        cur = [0] * (m + 1)&#10;        for j in range(1, m + 1):&#10;            if text1[i-1] == text2[j-1]: cur[j] = 1 + prev[j-1]&#10;            else: cur[j] = max(prev[j], cur[j-1])&#10;        prev = cur&#10;    return prev[m]</code></pre></details></td>
    </tr>
    <tr>
      <td>16</td>
      <td>Dp 15 Longest Increasing Subsequence<br><br></b> <a href='https://leetcode.com/problems/longest-increasing-subsequence/' target='_blank'>LeetCode 300</a></td>
      <td><b>Example 1:</b> Input: nums = [10,9,2,5,3,7,101,18], Output: 4</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Binary Search approach. Maintain an array `temp` of the increasing sequence. If `nums[i] > temp.back()`, append it. Else, find the lower bound of `nums[i]` in `temp` and replace it.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import bisect&#10;def lengthOfLIS(nums: List[int]) -&gt; int:&#10;    temp = [nums[0]]&#10;    for i in range(1, len(nums)):&#10;        if nums[i] &gt; temp[-1]: temp.append(nums[i])&#10;        else:&#10;            ind = bisect.bisect_left(temp, nums[i])&#10;            temp[ind] = nums[i]&#10;    return len(temp)</code></pre></details></td>
    </tr>
    <tr>
      <td>17</td>
      <td>Dp 16 Edit Distance<br><br></b> <a href='https://leetcode.com/problems/edit-distance/' target='_blank'>LeetCode 72</a></td>
      <td><b>Example 1:</b> Input: word1 = 'horse', word2 = 'ros', Output: 3</td>
      <td><b>Time:</b> O(N * M)<br><b>Space:</b> O(M)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> If chars match, move both pointers. Else, try all 3 ops: 1 + min(insert(i, j-1), delete(i-1, j), replace(i-1, j-1)). Space optimized to 1D.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minDistance(word1: str, word2: str) -&gt; int:&#10;    n, m = len(word1), len(word2)&#10;    prev = list(range(m + 1))&#10;    for i in range(1, n + 1):&#10;        cur = [0] * (m + 1)&#10;        cur[0] = i&#10;        for j in range(1, m + 1):&#10;            if word1[i-1] == word2[j-1]: cur[j] = prev[j-1]&#10;            else: cur[j] = 1 + min(prev[j-1], prev[j], cur[j-1])&#10;        prev = cur&#10;    return prev[m]</code></pre></details></td>
    </tr>
    <tr>
      <td>18</td>
      <td>Dp 17 Coin Change<br><br></b> <a href='https://leetcode.com/problems/coin-change/' target='_blank'>LeetCode 322</a></td>
      <td><b>Example 1:</b> Input: coins = [1,2,5], amount = 11, Output: 3</td>
      <td><b>Time:</b> O(N * Amount)<br><b>Space:</b> O(Amount)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Unbounded Knapsack variant. State `dp[amount]` stores min coins. Iterate through coins, and for each amount from `coin` to `target`, `dp[amt] = min(dp[amt], 1 + dp[amt - coin])`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def coinChange(coins: List[int], amount: int) -&gt; int:&#10;    dp = [float(&#x27;inf&#x27;)] * (amount + 1)&#10;    dp[0] = 0&#10;    for coin in coins:&#10;        for amt in range(coin, amount + 1):&#10;            dp[amt] = min(dp[amt], 1 + dp[amt - coin])&#10;    return dp[amount] if dp[amount] != float(&#x27;inf&#x27;) else -1</code></pre></details></td>
    </tr>
    <tr>
      <td>19</td>
      <td>Dp 18 Minimum Path Sum<br><br></b> <a href='https://leetcode.com/problems/minimum-path-sum/' target='_blank'>LeetCode 64</a></td>
      <td><b>Example 1:</b> Input: grid = [[1,3,1],[1,5,1],[4,2,1]], Output: 7</td>
      <td><b>Time:</b> O(N * M)<br><b>Space:</b> O(M)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> DP on Grids. Space optimize to 1D. `cur[j] = grid[i][j] + min(up, left)`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minPathSum(grid: List[List[int]]) -&gt; int:&#10;    n, m = len(grid), len(grid[0])&#10;    prev = [0] * m&#10;    for i in range(n):&#10;        cur = [0] * m&#10;        for j in range(m):&#10;            if i == 0 and j == 0: cur[j] = grid[i][j]&#10;            else:&#10;                up, left = grid[i][j], grid[i][j]&#10;                up += prev[j] if i &gt; 0 else float(&#x27;inf&#x27;)&#10;                left += cur[j-1] if j &gt; 0 else float(&#x27;inf&#x27;)&#10;                cur[j] = min(up, left)&#10;        prev = cur&#10;    return prev[-1]</code></pre></details></td>
    </tr>
    <tr>
      <td>20</td>
      <td>Dp 19 Triangle<br><br></b> <a href='https://leetcode.com/problems/triangle/' target='_blank'>LeetCode 120</a></td>
      <td><b>Example 1:</b> Output: 11</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Start from bottom row and move upwards. `dp[j] = triangle[i][j] + min(dp[j], dp[j+1])`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minimumTotal(triangle: List[List[int]]) -&gt; int:&#10;    n = len(triangle)&#10;    front = triangle[-1][:]&#10;    for i in range(n-2, -1, -1):&#10;        cur = [0] * n&#10;        for j in range(i, -1, -1):&#10;            cur[j] = triangle[i][j] + min(front[j], front[j+1])&#10;        front = cur&#10;    return front[0]</code></pre></details></td>
    </tr>
    <tr>
      <td>21</td>
      <td>Dp 20 Minimum Falling Path Sum<br><br></b> <a href='https://leetcode.com/problems/minimum-falling-path-sum/' target='_blank'>LeetCode 931</a></td>
      <td><b>Example 1:</b> Output: 13</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Similar to minimum path sum, but we can fall diagonally. Space optimize by using previous row.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minFallingPathSum(matrix: List[List[int]]) -&gt; int:&#10;    n = len(matrix)&#10;    prev = matrix[0][:]&#10;    for i in range(1, n):&#10;        cur = [0] * n&#10;        for j in range(n):&#10;            up = matrix[i][j] + prev[j]&#10;            ld = matrix[i][j] + (prev[j-1] if j &gt; 0 else float(&#x27;inf&#x27;))&#10;            rd = matrix[i][j] + (prev[j+1] if j &lt; n-1 else float(&#x27;inf&#x27;))&#10;            cur[j] = min(up, ld, rd)&#10;        prev = cur&#10;    return min(prev)</code></pre></details></td>
    </tr>
    <tr>
      <td>22</td>
      <td>Dp 21 Cherry Pickup Ii<br><br></b> <a href='https://leetcode.com/problems/cherry-pickup-ii/' target='_blank'>LeetCode 1463</a></td>
      <td><b>Example 1:</b> 3D DP.</td>
      <td><b>Time:</b> O(N * M * M * 9)<br><b>Space:</b> O(M * M)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Robots move simultaneously. State is `dp[row][col1][col2]`. Try all 9 combinations of moves for both robots.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def cherryPickup(grid: List[List[int]]) -&gt; int:&#10;    n, m = len(grid), len(grid[0])&#10;    front = [[0]*m for _ in range(m)]&#10;    for j1 in range(m):&#10;        for j2 in range(m):&#10;            if j1 == j2: front[j1][j2] = grid[n-1][j1]&#10;            else: front[j1][j2] = grid[n-1][j1] + grid[n-1][j2]&#10;    for i in range(n-2, -1, -1):&#10;        cur = [[0]*m for _ in range(m)]&#10;        for j1 in range(m):&#10;            for j2 in range(m):&#10;                maxi = -int(1e9)&#10;                for dj1 in [-1, 0, 1]:&#10;                    for dj2 in [-1, 0, 1]:&#10;                        val = grid[i][j1] if j1 == j2 else grid[i][j1] + grid[i][j2]&#10;                        if 0 &lt;= j1+dj1 &lt; m and 0 &lt;= j2+dj2 &lt; m:&#10;                            val += front[j1+dj1][j2+dj2]&#10;                        else: val += -int(1e9)&#10;                        maxi = max(maxi, val)&#10;                cur[j1][j2] = maxi&#10;        front = cur&#10;    return front[0][m-1]</code></pre></details></td>
    </tr>
    <tr>
      <td>23</td>
      <td>Dp 22 Partition Equal Subset Sum<br><br></b> <a href='https://leetcode.com/problems/partition-equal-subset-sum/' target='_blank'>LeetCode 416</a></td>
      <td><b>Example 1:</b> Output: True.</td>
      <td><b>Time:</b> O(N * Target)<br><b>Space:</b> O(Target)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> If total sum is odd, impossible. Else, find if there's a subset with sum `Total/2` using space-optimized DP.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def canPartition(nums: List[int]) -&gt; bool:&#10;    total_sum = sum(nums)&#10;    if total_sum % 2 != 0: return False&#10;    target = total_sum // 2&#10;    prev = [False] * (target + 1)&#10;    prev[0] = True&#10;    if nums[0] &lt;= target: prev[nums[0]] = True&#10;    for ind in range(1, len(nums)):&#10;        cur = [False] * (target + 1)&#10;        cur[0] = True&#10;        for t in range(1, target + 1):&#10;            notTaken = prev[t]&#10;            taken = False&#10;            if nums[ind] &lt;= t: taken = prev[t - nums[ind]]&#10;            cur[t] = notTaken or taken&#10;        prev = cur&#10;    return prev[target]</code></pre></details></td>
    </tr>
    <tr>
      <td>24</td>
      <td>Dp 23 Target Sum<br><br></b> <a href='https://leetcode.com/problems/target-sum/' target='_blank'>LeetCode 494</a></td>
      <td><b>Example 1:</b> Count Subsets with Diff = target.</td>
      <td><b>Time:</b> O(N * Target)<br><b>Space:</b> O(Target)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Subset sum variation. `S1 - S2 = target`, `S1 + S2 = totalSum`. So, `S1 = (target + totalSum) / 2`. Find subsets with this target sum.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findTargetSumWays(nums: List[int], target: int) -&gt; int:&#10;    total = sum(nums)&#10;    if total - target &lt; 0 or (total - target) % 2 == 1: return 0&#10;    s2 = (total - target) // 2&#10;    prev = [0] * (s2 + 1)&#10;    if nums[0] == 0: prev[0] = 2&#10;    else: prev[0] = 1&#10;    if nums[0] != 0 and nums[0] &lt;= s2: prev[nums[0]] = 1&#10;    for ind in range(1, len(nums)):&#10;        cur = [0] * (s2 + 1)&#10;        for t in range(s2 + 1):&#10;            notTaken = prev[t]&#10;            taken = 0&#10;            if nums[ind] &lt;= t: taken = prev[t - nums[ind]]&#10;            cur[t] = notTaken + taken&#10;        prev = cur&#10;    return prev[s2]</code></pre></details></td>
    </tr>
    <tr>
      <td>25</td>
      <td>Dp 24 Burst Balloons<br><br></b> <a href='https://leetcode.com/problems/burst-balloons/' target='_blank'>LeetCode 312</a></td>
      <td><b>Example 1:</b> Input: nums = [3,1,5,8], Output: 167</td>
      <td><b>Time:</b> O(N^3)<br><b>Space:</b> O(N^2)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> MCM Pattern. Add 1 at the beginning and end. Loop lengths from 1 to N. Iterate start `i` and end `j`. Then iterate `k` from `i` to `j`, meaning balloon `k` is the LAST one to burst in the range `[i, j]`. The coins collected are `nums[i-1] * nums[k] * nums[j+1] + dp[i][k-1] + dp[k+1][j]`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxCoins(nums: List[int]) -&gt; int:&#10;    n = len(nums)&#10;    nums = [1] + nums + [1]&#10;    dp = [[0] * (n + 2) for _ in range(n + 2)]&#10;    for i in range(n, 0, -1):&#10;        for j in range(1, n + 1):&#10;            if i &gt; j: continue&#10;            maxi = float(&#x27;-inf&#x27;)&#10;            for k in range(i, j + 1):&#10;                cost = nums[i-1]*nums[k]*nums[j+1] + dp[i][k-1] + dp[k+1][j]&#10;                maxi = max(maxi, cost)&#10;            dp[i][j] = maxi&#10;    return dp[1][n]</code></pre></details></td>
    </tr>
    <tr>
      <td>26</td>
      <td>Dp 25 Palindrome Partitioning Ii<br><br></b> <a href='https://leetcode.com/problems/palindrome-partitioning-ii/' target='_blank'>LeetCode 132</a></td>
      <td><b>Example 1:</b> Input: s = 'aab', Output: 1</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Front Partitioning. `dp[i]` is the minimum cuts for `s[i...n-1]`. To compute `dp[i]`, iterate `j` from `i` to `n-1`. If `s[i...j]` is a palindrome, then `cost = 1 + dp[j+1]`. `dp[i]` is the minimum of these costs. Return `dp[0] - 1`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minCut(s: str) -&gt; int:&#10;    n = len(s)&#10;    dp = [0] * (n + 1)&#10;    for i in range(n - 1, -1, -1):&#10;        min_cuts = float(&#x27;inf&#x27;)&#10;        for j in range(i, n):&#10;            if s[i:j+1] == s[i:j+1][::-1]:&#10;                cost = 1 + dp[j+1]&#10;                min_cuts = min(min_cuts, cost)&#10;        dp[i] = min_cuts&#10;    return dp[0] - 1</code></pre></details></td>
    </tr>
    <tr>
      <td>27</td>
      <td>Dp 26 Evaluate Boolean Expression To True<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/boolean-parenthesization5610/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> MCM DP pattern.</td>
      <td><b>Time:</b> O(N^3)<br><b>Space:</b> O(N^2)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> MCM DP. `dp[i][j][isTrue]` stores the number of ways to evaluate `S[i..j]` to boolean `isTrue`. Iterate length, start, and partition `k`. Calculate T/F ways based on the operator at `k`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def countWays(N: int, S: str) -&gt; int:&#10;    mod = 1003&#10;    dp = [[[0, 0] for _ in range(N)] for _ in range(N)]&#10;    for i in range(N - 1, -1, -2):&#10;        for j in range(i, N, 2):&#10;            if i == j:&#10;                dp[i][j][1] = 1 if S[i] == &#x27;T&#x27; else 0&#10;                dp[i][j][0] = 1 if S[i] == &#x27;F&#x27; else 0&#10;                continue&#10;            waysT, waysF = 0, 0&#10;            for k in range(i + 1, j, 2):&#10;                lT, lF = dp[i][k-1][1], dp[i][k-1][0]&#10;                rT, rF = dp[k+1][j][1], dp[k+1][j][0]&#10;                if S[k] == &#x27;&amp;&#x27;:&#10;                    waysT = (waysT + lT * rT) % mod&#10;                    waysF = (waysF + lT * rF + lF * rT + lF * rF) % mod&#10;                elif S[k] == &#x27;|&#x27;:&#10;                    waysT = (waysT + lT * rT + lT * rF + lF * rT) % mod&#10;                    waysF = (waysF + lF * rF) % mod&#10;                elif S[k] == &#x27;^&#x27;:&#10;                    waysT = (waysT + lT * rF + lF * rT) % mod&#10;                    waysF = (waysF + lT * rT + lF * rF) % mod&#10;            dp[i][j][1] = waysT&#10;            dp[i][j][0] = waysF&#10;    return dp[0][N-1][1]</code></pre></details></td>
    </tr>
    <tr>
      <td>28</td>
      <td>Dp 27 Maximum Rectangle Area With All 1S<br><br></b> <a href='https://leetcode.com/problems/maximal-rectangle/' target='_blank'>LeetCode 85</a></td>
      <td><b>Example 1:</b> Calculate largest area.</td>
      <td><b>Time:</b> O(N * M)<br><b>Space:</b> O(M)</td>
      <td><code>#include <stack></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Maintain a histogram for each row. The height of the histogram is the consecutive 1s ending at that cell. For each row's histogram, use the 'Largest Rectangle in Histogram' stack algorithm.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maximalRectangle(matrix: List[List[str]]) -&gt; int:&#10;    if not matrix: return 0&#10;    def largestRectangleArea(heights):&#10;        st = []&#10;        maxA = 0&#10;        heights.append(0)&#10;        for i, h in enumerate(heights):&#10;            while st and heights[st[-1]] &gt;= h:&#10;                height = heights[st.pop()]&#10;                w = i if not st else i - st[-1] - 1&#10;                maxA = max(maxA, height * w)&#10;            st.append(i)&#10;        return maxA&#10;    &#10;    maxArea = 0&#10;    heights = [0] * len(matrix[0])&#10;    for row in matrix:&#10;        for j, val in enumerate(row):&#10;            heights[j] = heights[j] + 1 if val == &#x27;1&#x27; else 0&#10;        maxArea = max(maxArea, largestRectangleArea(heights))&#10;    return maxArea</code></pre></details></td>
    </tr>
    <tr>
      <td>29</td>
      <td>Dp 28 Count Square Submatrices With All Ones<br><br></b> <a href='https://leetcode.com/problems/count-square-submatrices-with-all-ones/' target='_blank'>LeetCode 1277</a></td>
      <td><b>Example 1:</b> Return total count.</td>
      <td><b>Time:</b> O(N * M)<br><b>Space:</b> O(N * M)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> `dp[i][j]` is the size of the largest square ending at `(i, j)`. It also represents the number of squares ending at `(i, j)`. `dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1` if `matrix[i][j] == 1`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def countSquares(matrix: List[List[int]]) -&gt; int:&#10;    n, m = len(matrix), len(matrix[0])&#10;    dp = [[0]*m for _ in range(n)]&#10;    total = 0&#10;    for i in range(n):&#10;        for j in range(m):&#10;            if matrix[i][j] == 1:&#10;                if i == 0 or j == 0: dp[i][j] = 1&#10;                else: dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1&#10;                total += dp[i][j]&#10;    return total</code></pre></details></td>
    </tr>
    <tr>
      <td>30</td>
      <td>Dp 29 Word Break Dp<br><br></b> <a href='https://leetcode.com/problems/word-break/' target='_blank'>LeetCode 139</a></td>
      <td><b>Example 1:</b> `s = "leetcode"`. Output: `true`.</td>
      <td><b>Time:</b> O(N^2 * max_word_length)<br><b>Space:</b> O(N)</td>
      <td><code>#include <unordered_set></code></td>
      <td>-</td>
      <td><b>Explanation:</b> `dp[i]` is true if `s[0..i-1]` can be segmented. For each `i`, iterate `j` from 0 to `i-1`. If `dp[j]` is true and `s[j..i-1]` is in dict, then `dp[i] = true`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def wordBreak(s: str, wordDict: List[str]) -&gt; bool:&#10;    word_set = set(wordDict)&#10;    n = len(s)&#10;    dp = [False] * (n + 1)&#10;    dp[0] = True&#10;    for i in range(1, n + 1):&#10;        for j in range(i - 1, -1, -1):&#10;            if dp[j] and s[j:i] in word_set:&#10;                dp[i] = True&#10;                break&#10;    return dp[n]</code></pre></details></td>
    </tr>
    <tr>
      <td>31</td>
      <td>Dp 30 Matrix Chain Multiplication<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Minimize scalar multiplications.</td>
      <td><b>Time:</b> O(N^3)<br><b>Space:</b> O(N^2)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Standard MCM DP. `dp[i][j]` is min cost to multiply matrices from `i` to `j`. Iterate length of chain, start `i`, and partition `k`. `dp[i][j] = min(dp[i][k] + dp[k+1][j] + arr[i-1]*arr[k]*arr[j])`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def matrixMultiplication(N: int, arr: List[int]) -&gt; int:&#10;    dp = [[0]*N for _ in range(N)]&#10;    for i in range(N-1, 0, -1):&#10;        for j in range(i+1, N):&#10;            mini = float(&#x27;inf&#x27;)&#10;            for k in range(i, j):&#10;                cost = dp[i][k] + dp[k+1][j] + arr[i-1]*arr[k]*arr[j]&#10;                mini = min(mini, cost)&#10;            dp[i][j] = mini&#10;    return dp[1][N-1]</code></pre></details></td>
    </tr>
    <tr>
      <td>32</td>
      <td>Dp 31 Minimum Cost To Cut A Stick<br><br></b> <a href='https://leetcode.com/problems/minimum-cost-to-cut-a-stick/' target='_blank'>LeetCode 1547</a></td>
      <td><b>Example 1:</b> Cost depends on current stick length.</td>
      <td><b>Time:</b> O(C^3) where C is number of cuts<br><b>Space:</b> O(C^2)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Sort cuts array and prepend 0, append `n`. Use MCM pattern. `dp[i][j]` is the minimum cost to cut the stick between cuts `i` and `j`. `dp[i][j] = min(cost + cuts[j+1] - cuts[i-1])`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minCost(n: int, cuts: List[int]) -&gt; int:&#10;    cuts = [0] + sorted(cuts) + [n]&#10;    c = len(cuts) - 2&#10;    dp = [[0] * (c + 2) for _ in range(c + 2)]&#10;    for i in range(c, 0, -1):&#10;        for j in range(1, c + 1):&#10;            if i &gt; j: continue&#10;            mini = float(&#x27;inf&#x27;)&#10;            for k in range(i, j + 1):&#10;                cost = cuts[j+1] - cuts[i-1] + dp[i][k-1] + dp[k+1][j]&#10;                mini = min(mini, cost)&#10;            dp[i][j] = mini&#10;    return dp[1][c]</code></pre></details></td>
    </tr>
    <tr>
      <td>33</td>
      <td>Dp 32 Partition Array For Maximum Sum<br><br></b> <a href='https://leetcode.com/problems/partition-array-for-maximum-sum/' target='_blank'>LeetCode 1043</a></td>
      <td><b>Example 1:</b> Front partitioning DP.</td>
      <td><b>Time:</b> O(N * K)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Front partitioning. `dp[i]` is max sum for `arr[i..n-1]`. For each `i`, iterate `j` up to `i+k-1`. Find `maxi` element in this window, and add `maxi * length + dp[j+1]`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxSumAfterPartitioning(arr: List[int], k: int) -&gt; int:&#10;    n = len(arr)&#10;    dp = [0] * (n + 1)&#10;    for i in range(n - 1, -1, -1):&#10;        max_val = 0&#10;        max_ans = 0&#10;        length = 0&#10;        for j in range(i, min(n, i + k)):&#10;            length += 1&#10;            max_val = max(max_val, arr[j])&#10;            current_sum = max_val * length + dp[j+1]&#10;            max_ans = max(max_ans, current_sum)&#10;        dp[i] = max_ans&#10;    return dp[0]</code></pre></details></td>
    </tr>
    <tr>
      <td>34</td>
      <td>Dp 33 Distinct Subsequences<br><br></b> <a href='https://leetcode.com/problems/distinct-subsequences/' target='_blank'>LeetCode 115</a></td>
      <td><b>Example 1:</b> Subsequence match count.</td>
      <td><b>Time:</b> O(N * M)<br><b>Space:</b> O(M)</td>
      <td>-</td>
      <td><b>Integer Overflow:</b> Use double or long long, or cast to unsigned int.</td>
      <td><b>Explanation:</b> If characters match, `dp[i][j] = dp[i-1][j-1] + dp[i-1][j]`. If they don't, `dp[i][j] = dp[i-1][j]`. Optimize to 1D array.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def numDistinct(s: str, t: str) -&gt; int:&#10;    n, m = len(s), len(t)&#10;    dp = [0] * (m + 1)&#10;    dp[0] = 1&#10;    for i in range(1, n + 1):&#10;        for j in range(m, 0, -1):&#10;            if s[i-1] == t[j-1]:&#10;                dp[j] += dp[j-1]&#10;    return dp[m]</code></pre></details></td>
    </tr>
    <tr>
      <td>35</td>
      <td>Dp 34 Wildcard Matching<br><br></b> <a href='https://leetcode.com/problems/wildcard-matching/' target='_blank'>LeetCode 44</a></td>
      <td><b>Example 1:</b> 2D DP.</td>
      <td><b>Time:</b> O(N * M)<br><b>Space:</b> O(N * M) or O(M)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Use a 2D DP array where `dp[i][j]` means if `s[0..i-1]` matches `p[0..j-1]`. If `p[j-1] == '?'` or `s[i-1] == p[j-1]`, `dp[i][j] = dp[i-1][j-1]`. If `p[j-1] == '*'`, it can match empty (`dp[i][j-1]`) or match one character (`dp[i-1][j]`).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isMatch(s: str, p: str) -&gt; bool:&#10;    n, m = len(s), len(p)&#10;    dp = [[False] * (m + 1) for _ in range(n + 1)]&#10;    dp[0][0] = True&#10;    for j in range(1, m + 1):&#10;        if p[j-1] == &#x27;*&#x27;: dp[0][j] = dp[0][j-1]&#10;    for i in range(1, n + 1):&#10;        for j in range(1, m + 1):&#10;            if p[j-1] in {s[i-1], &#x27;?&#x27;}:&#10;                dp[i][j] = dp[i-1][j-1]&#10;            elif p[j-1] == &#x27;*&#x27;:&#10;                dp[i][j] = dp[i-1][j] or dp[i][j-1]&#10;    return dp[n][m]</code></pre></details></td>
    </tr>
    <tr>
      <td>36</td>
      <td>Dp 35 Best Time To Buy And Sell Stock Ii<br><br></b> <a href='https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/' target='_blank'>LeetCode 122</a></td>
      <td><b>Example 1:</b> Valley Peak approach.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Add the profit whenever the price is higher than the previous day. This is equivalent to capturing every upward slope.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxProfit(prices: List[int]) -&gt; int:&#10;    return sum(max(prices[i] - prices[i-1], 0) for i in range(1, len(prices)))</code></pre></details></td>
    </tr>
    <tr>
      <td>37</td>
      <td>Dp 36 Best Time To Buy And Sell Stock Iii<br><br></b> <a href='https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/' target='_blank'>LeetCode 123</a></td>
      <td><b>Example 1:</b> 3D DP / State Machine.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Maintain four variables representing the max profit after first buy, first sell, second buy, and second sell. Update them iteratively.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxProfit(prices: List[int]) -&gt; int:&#10;    buy1 = buy2 = float(&#x27;-inf&#x27;)&#10;    sell1 = sell2 = 0&#10;    for price in prices:&#10;        buy1 = max(buy1, -price)&#10;        sell1 = max(sell1, buy1 + price)&#10;        buy2 = max(buy2, sell1 - price)&#10;        sell2 = max(sell2, buy2 + price)&#10;    return sell2</code></pre></details></td>
    </tr>
    <tr>
      <td>38</td>
      <td>Dp 37 Best Time To Buy And Sell Stock Iv<br><br></b> <a href='https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/' target='_blank'>LeetCode 188</a></td>
      <td><b>Example 1:</b> DP with transactions.</td>
      <td><b>Time:</b> O(N * K)<br><b>Space:</b> O(N * K) or O(K)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> If `k >= n/2`, it's equivalent to infinite transactions (Stock II). Else, use a DP array `dp[k][n]` where `dp[i][j]` is max profit using `i` transactions up to day `j`. Optimize inner loop by tracking `maxDiff = max(maxDiff, dp[i-1][j-1] - prices[j-1])`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxProfit(k: int, prices: List[int]) -&gt; int:&#10;    n = len(prices)&#10;    if n &lt;= 1: return 0&#10;    if k &gt;= n // 2:&#10;        return sum(max(prices[i] - prices[i-1], 0) for i in range(1, n))&#10;    buy = [float(&#x27;-inf&#x27;)] * (k + 1)&#10;    sell = [0] * (k + 1)&#10;    for price in prices:&#10;        for i in range(1, k + 1):&#10;            buy[i] = max(buy[i], sell[i-1] - price)&#10;            sell[i] = max(sell[i], buy[i] + price)&#10;    return sell[k]</code></pre></details></td>
    </tr>
    <tr>
      <td>39</td>
      <td>Dp 38 Best Time To Buy And Sell Stock With Cooldown<br><br></b> <a href='https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/' target='_blank'>LeetCode 309</a></td>
      <td><b>Example 1:</b> State Machine DP.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Maintain 3 states: `hold` (holding a stock), `sold` (just sold, entering cooldown next), `rest` (not holding, not in cooldown). Transitions: `hold = max(hold, rest - price)`, `sold = hold + price`, `rest = max(rest, sold_prev)`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxProfit(prices: List[int]) -&gt; int:&#10;    hold, sold, rest = float(&#x27;-inf&#x27;), 0, 0&#10;    for price in prices:&#10;        prev_sold = sold&#10;        sold = hold + price&#10;        hold = max(hold, rest - price)&#10;        rest = max(rest, prev_sold)&#10;    return max(rest, sold)</code></pre></details></td>
    </tr>
    <tr>
      <td>40</td>
      <td>Dp 39 Best Time To Buy And Sell Stock With Transaction Fee<br><br></b> <a href='https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/' target='_blank'>LeetCode 714</a></td>
      <td><b>Example 1:</b> DP State Machine.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Similar to Stock II, but subtract `fee` when selling. Maintain `cash` (max profit not holding stock) and `hold` (max profit holding stock). `cash = max(cash, hold + price - fee)`, `hold = max(hold, cash - price)`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxProfit(prices: List[int], fee: int) -&gt; int:&#10;    cash, hold = 0, -prices[0]&#10;    for i in range(1, len(prices)):&#10;        cash = max(cash, hold + prices[i] - fee)&#10;        hold = max(hold, cash - prices[i])&#10;    return cash</code></pre></details></td>
    </tr>
    <tr>
      <td>41</td>
      <td>Dp 40 Longest Increasing Subsequence<br><br></b> <a href='https://leetcode.com/problems/longest-increasing-subsequence/' target='_blank'>LeetCode 300</a></td>
      <td><b>Example 1:</b> Binary Search with tails array.</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Maintain an array `tails` where `tails[i]` stores the smallest tail of all increasing subsequences of length `i+1`. Use binary search (`lower_bound`) to find the position to replace or append.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import bisect&#10;def lengthOfLIS(nums: List[int]) -&gt; int:&#10;    tails = []&#10;    for num in nums:&#10;        idx = bisect.bisect_left(tails, num)&#10;        if idx == len(tails): tails.append(num)&#10;        else: tails[idx] = num&#10;    return len(tails)</code></pre></details></td>
    </tr>
    <tr>
      <td>42</td>
      <td>Dp 41 Largest Divisible Subset<br><br></b> <a href='https://leetcode.com/problems/largest-divisible-subset/' target='_blank'>LeetCode 368</a></td>
      <td><b>Example 1:</b> Sort and LIS variant.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Sort the array. Then use LIS logic: `dp[i]` is max subset ending at `i`. If `nums[i] % nums[j] == 0`, `dp[i] = max(dp[i], dp[j] + 1)`. Also keep a `parent` array to reconstruct the subset.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def largestDivisibleSubset(nums: List[int]) -&gt; List[int]:&#10;    if not nums: return []&#10;    nums.sort()&#10;    n = len(nums)&#10;    dp, parent = [1] * n, [-1] * n&#10;    max_len, max_idx = 1, 0&#10;    for i in range(1, n):&#10;        for j in range(i):&#10;            if nums[i] % nums[j] == 0 and dp[i] &lt; dp[j] + 1:&#10;                dp[i] = dp[j] + 1&#10;                parent[i] = j&#10;        if dp[i] &gt; max_len:&#10;            max_len, max_idx = dp[i], i&#10;    res = []&#10;    while max_idx != -1:&#10;        res.append(nums[max_idx])&#10;        max_idx = parent[max_idx]&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td>43</td>
      <td>Dp 42 Longest String Chain<br><br></b> <a href='https://leetcode.com/problems/longest-string-chain/' target='_blank'>LeetCode 1048</a></td>
      <td><b>Example 1:</b> Sort by length and use hash map.</td>
      <td><b>Time:</b> O(N log N + N * L^2) where L is max word length<br><b>Space:</b> O(N * L)</td>
      <td><code>#include <unordered_map></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Sort words by length. Use a hash map `dp` to store the longest chain ending at `word`. For each word, try removing one character at a time to form `prev_word`. `dp[word] = max(dp[word], dp[prev_word] + 1)`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def longestStrChain(words: List[str]) -&gt; int:&#10;    words.sort(key=len)&#10;    dp = {}&#10;    max_len = 1&#10;    for word in words:&#10;        dp[word] = 1&#10;        for i in range(len(word)):&#10;            prev = word[:i] + word[i+1:]&#10;            if prev in dp:&#10;                dp[word] = max(dp[word], dp[prev] + 1)&#10;        max_len = max(max_len, dp[word])&#10;    return max_len</code></pre></details></td>
    </tr>
    <tr>
      <td>44</td>
      <td>Dp 43 Longest Bitonic Subsequence<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/longest-bitonic-subsequence0824/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> LIS from left + LIS from right.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Compute LIS ending at `i` from left to right (`inc[i]`). Compute LIS starting at `i` from right to left (`dec[i]`). The max bitonic subsequence length is `max(inc[i] + dec[i] - 1)` for all `i`. Sometimes pure increasing or pure decreasing is also bitonic depending on definition, adjust if necessary.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def LongestBitonicSequence(nums: List[int]) -&gt; int:&#10;    n = len(nums)&#10;    inc = [1] * n&#10;    dec = [1] * n&#10;    for i in range(1, n):&#10;        for j in range(i):&#10;            if nums[i] &gt; nums[j]: inc[i] = max(inc[i], inc[j] + 1)&#10;    for i in range(n - 2, -1, -1):&#10;        for j in range(n - 1, i, -1):&#10;            if nums[i] &gt; nums[j]: dec[i] = max(dec[i], dec[j] + 1)&#10;    return max(inc[i] + dec[i] - 1 for i in range(n))</code></pre></details></td>
    </tr>
    <tr>
      <td>45</td>
      <td>Dp 44 Number Of Longest Increasing Subsequence<br><br></b> <a href='https://leetcode.com/problems/number-of-longest-increasing-subsequence/' target='_blank'>LeetCode 673</a></td>
      <td><b>Example 1:</b> Two DP arrays (Length and Count).</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Maintain `lengths[i]` (length of LIS ending at i) and `counts[i]` (number of LIS ending at i). If `nums[i] > nums[j]`: if `lengths[j] + 1 > lengths[i]`, then `lengths[i] = lengths[j] + 1` and `counts[i] = counts[j]`. Else if `lengths[j] + 1 == lengths[i]`, then `counts[i] += counts[j]`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findNumberOfLIS(nums: List[int]) -&gt; int:&#10;    n = len(nums)&#10;    lengths = [1] * n&#10;    counts = [1] * n&#10;    max_len = 0&#10;    res = 0&#10;    for i in range(n):&#10;        for j in range(i):&#10;            if nums[i] &gt; nums[j]:&#10;                if lengths[j] + 1 &gt; lengths[i]:&#10;                    lengths[i] = lengths[j] + 1&#10;                    counts[i] = counts[j]&#10;                elif lengths[j] + 1 == lengths[i]:&#10;                    counts[i] += counts[j]&#10;        if lengths[i] &gt; max_len:&#10;            max_len = lengths[i]&#10;            res = counts[i]&#10;        elif lengths[i] == max_len:&#10;            res += counts[i]&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td>46</td>
      <td>Dp 45 Matrix Chain Multiplication<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Interval DP.</td>
      <td><b>Time:</b> O(N^3)<br><b>Space:</b> O(N^2)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Use DP where `dp[i][j]` is min cost to multiply matrices from `i` to `j`. `dp[i][j] = min(dp[i][k] + dp[k+1][j] + arr[i-1]*arr[k]*arr[j])` for all `i <= k < j`. Solve for subproblem lengths 2 to N.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def matrixMultiplication(N, arr):&#10;    dp = [[0] * N for _ in range(N)]&#10;    for length in range(2, N):&#10;        for i in range(1, N - length + 1):&#10;            j = i + length - 1&#10;            dp[i][j] = float(&#x27;inf&#x27;)&#10;            for k in range(i, j):&#10;                cost = dp[i][k] + dp[k+1][j] + arr[i-1] * arr[k] * arr[j]&#10;                dp[i][j] = min(dp[i][j], cost)&#10;    return dp[1][N-1]</code></pre></details></td>
    </tr>
    <tr>
      <td>47</td>
      <td>Dp 46 Minimum Cost To Cut A Stick<br><br></b> <a href='https://leetcode.com/problems/minimum-cost-to-cut-a-stick/' target='_blank'>LeetCode 1547</a></td>
      <td><b>Example 1:</b> Interval DP like Matrix Chain Multiplication.</td>
      <td><b>Time:</b> O(C^3) where C is number of cuts<br><b>Space:</b> O(C^2)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Add 0 and `n` to `cuts`, then sort. `dp[i][j]` is min cost to cut the sub-stick between `cuts[i]` and `cuts[j]`. Try all possible cuts `k` between `i` and `j`. `dp[i][j] = min(dp[i][k] + dp[k][j]) + cuts[j] - cuts[i]`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minCost(n: int, cuts: List[int]) -&gt; int:&#10;    cuts = [0] + sorted(cuts) + [n]&#10;    c = len(cuts)&#10;    dp = [[0] * c for _ in range(c)]&#10;    for length in range(2, c):&#10;        for i in range(c - length):&#10;            j = i + length&#10;            dp[i][j] = float(&#x27;inf&#x27;)&#10;            for k in range(i + 1, j):&#10;                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + cuts[j] - cuts[i])&#10;    return dp[0][c-1]</code></pre></details></td>
    </tr>
    <tr>
      <td>48</td>
      <td>Dp 47 Burst Balloons<br><br></b> <a href='https://leetcode.com/problems/burst-balloons/' target='_blank'>LeetCode 312</a></td>
      <td><b>Example 1:</b> Interval DP (Thinking backwards).</td>
      <td><b>Time:</b> O(N^3)<br><b>Space:</b> O(N^2)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Add 1 to both ends of `nums`. `dp[i][j]` is max coins from bursting balloons strictly between `i` and `j`. Guess which balloon `k` (between `i` and `j`) is the LAST one to burst. Coins gained = `nums[i] * nums[k] * nums[j]`. Total = `dp[i][k] + dp[k][j] + coins`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxCoins(nums: List[int]) -&gt; int:&#10;    a = [1] + nums + [1]&#10;    n = len(a)&#10;    dp = [[0] * n for _ in range(n)]&#10;    for length in range(2, n):&#10;        for i in range(n - length):&#10;            j = i + length&#10;            for k in range(i + 1, j):&#10;                dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + a[i] * a[k] * a[j])&#10;    return dp[0][n-1]</code></pre></details></td>
    </tr>
    <tr>
      <td>49</td>
      <td>Dp 48 Evaluate Boolean Expression To True<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/boolean-parenthesization5610/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> 3D Interval DP.</td>
      <td><b>Time:</b> O(N^3)<br><b>Space:</b> O(N^2 * 2)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> `dp[i][j][isTrue]` is number of ways to evaluate substring `i..j` to boolean `isTrue`. Iterate `k` from `i+1` to `j-1` with step 2 (k is operator). Combine left (`i..k-1`) and right (`k+1..j`) results based on the operator.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def countWays(n: int, s: str) -&gt; int:&#10;    dp = [[[0, 0] for _ in range(n)] for _ in range(n)]&#10;    for i in range(0, n, 2):&#10;        if s[i] == &#x27;T&#x27;: dp[i][i][1] = 1&#10;        else: dp[i][i][0] = 1&#10;    for length in range(3, n + 1, 2):&#10;        for i in range(0, n - length + 1, 2):&#10;            j = i + length - 1&#10;            for k in range(i + 1, j, 2):&#10;                lT, lF = dp[i][k-1][1], dp[i][k-1][0]&#10;                rT, rF = dp[k+1][j][1], dp[k+1][j][0]&#10;                if s[k] == &#x27;&amp;&#x27;:&#10;                    dp[i][j][1] = (dp[i][j][1] + lT * rT) % 1003&#10;                    dp[i][j][0] = (dp[i][j][0] + lF * rT + lT * rF + lF * rF) % 1003&#10;                elif s[k] == &#x27;|&#x27;:&#10;                    dp[i][j][1] = (dp[i][j][1] + lT * rT + lF * rT + lT * rF) % 1003&#10;                    dp[i][j][0] = (dp[i][j][0] + lF * rF) % 1003&#10;                elif s[k] == &#x27;^&#x27;:&#10;                    dp[i][j][1] = (dp[i][j][1] + lT * rF + lF * rT) % 1003&#10;                    dp[i][j][0] = (dp[i][j][0] + lT * rT + lF * rF) % 1003&#10;    return dp[0][n-1][1]</code></pre></details></td>
    </tr>
    <tr>
      <td>50</td>
      <td>Dp 49 Palindrome Partitioning Ii<br><br></b> <a href='https://leetcode.com/problems/palindrome-partitioning-ii/' target='_blank'>LeetCode 132</a></td>
      <td><b>Example 1:</b> 1D DP using Precomputed Palindrome Table.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N^2)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Precompute a 2D boolean array `isPal` indicating if `s[i..j]` is palindrome. Then use 1D DP `cuts[i]` indicating min cuts for `s[0..i]`. `cuts[i] = min(cuts[i], cuts[j-1] + 1)` for all `j <= i` where `isPal[j][i]` is true. If `isPal[0][i]` is true, `cuts[i] = 0`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minCut(s: str) -&gt; int:&#10;    n = len(s)&#10;    isPal = [[False] * n for _ in range(n)]&#10;    for i in range(n - 1, -1, -1):&#10;        for j in range(i, n):&#10;            if s[i] == s[j] and (j - i &lt;= 2 or isPal[i+1][j-1]):&#10;                isPal[i][j] = True&#10;    cuts = [0] * n&#10;    for i in range(n):&#10;        if isPal[0][i]:&#10;            cuts[i] = 0&#10;        else:&#10;            cuts[i] = i&#10;            for j in range(1, i + 1):&#10;                if isPal[j][i]:&#10;                    cuts[i] = min(cuts[i], cuts[j-1] + 1)&#10;    return cuts[n-1]</code></pre></details></td>
    </tr>
    <tr>
      <td>51</td>
      <td>Dp 50 Partition Array For Maximum Sum<br><br></b> <a href='https://leetcode.com/problems/partition-array-for-maximum-sum/' target='_blank'>LeetCode 1043</a></td>
      <td><b>Example 1:</b> 1D DP.</td>
      <td><b>Time:</b> O(N * K)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> `dp[i]` is max sum for prefix of length `i`. To find `dp[i]`, try all partition lengths `j` from 1 to `k`. Keep track of `max_val` in the last `j` elements. `dp[i] = max(dp[i], dp[i-j] + max_val * j)`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxSumAfterPartitioning(arr: List[int], k: int) -&gt; int:&#10;    n = len(arr)&#10;    dp = [0] * (n + 1)&#10;    for i in range(1, n + 1):&#10;        max_val = 0&#10;        for j in range(1, min(k, i) + 1):&#10;            max_val = max(max_val, arr[i - j])&#10;            dp[i] = max(dp[i], dp[i - j] + max_val * j)&#10;    return dp[n]</code></pre></details></td>
    </tr>
    <tr>
      <td>52</td>
      <td>Dp 51 Maximal Rectangle<br><br></b> <a href='https://leetcode.com/problems/maximal-rectangle/' target='_blank'>LeetCode 85</a></td>
      <td><b>Example 1:</b> DP to convert to Largest Rectangle in Histogram.</td>
      <td><b>Time:</b> O(R * C)<br><b>Space:</b> O(C)</td>
      <td><code>#include <stack></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Treat each row as the base of a histogram. Calculate heights for each row (`heights[j]++` if `matrix[i][j]=='1'`, else `0`). Then compute Largest Rectangle in Histogram for each row and take the maximum.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maximalRectangle(matrix: List[List[str]]) -&gt; int:&#10;    if not matrix: return 0&#10;    r, c = len(matrix), len(matrix[0])&#10;    heights = [0] * c&#10;    maxArea = 0&#10;    for i in range(r):&#10;        for j in range(c):&#10;            heights[j] = heights[j] + 1 if matrix[i][j] == &#x27;1&#x27; else 0&#10;        st = []&#10;        for j in range(c + 1):&#10;            h = 0 if j == c else heights[j]&#10;            while st and h &lt; heights[st[-1]]:&#10;                height = heights[st.pop()]&#10;                width = j if not st else j - st[-1] - 1&#10;                maxArea = max(maxArea, height * width)&#10;            st.append(j)&#10;    return maxArea</code></pre></details></td>
    </tr>
    <tr>
      <td>53</td>
      <td>Dp 52 Count Square Submatrices With All Ones<br><br></b> <a href='https://leetcode.com/problems/count-square-submatrices-with-all-ones/' target='_blank'>LeetCode 1277</a></td>
      <td><b>Example 1:</b> 2D DP.</td>
      <td><b>Time:</b> O(R * C)<br><b>Space:</b> O(R * C) or O(C) optimized</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> `dp[i][j]` represents the side length of the maximum square whose bottom-right corner is at `(i, j)`. If `matrix[i][j] == 1`, `dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1`. The number of squares ending here is exactly `dp[i][j]`. Sum all `dp[i][j]`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def countSquares(matrix: List[List[int]]) -&gt; int:&#10;    r, c = len(matrix), len(matrix[0])&#10;    dp = [[0] * c for _ in range(r)]&#10;    ans = 0&#10;    for i in range(r):&#10;        for j in range(c):&#10;            if matrix[i][j] == 1:&#10;                if i == 0 or j == 0:&#10;                    dp[i][j] = 1&#10;                else:&#10;                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1&#10;                ans += dp[i][j]&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>54</td>
      <td>Dp 53 Word Break<br><br></b> <a href='https://leetcode.com/problems/word-break/' target='_blank'>LeetCode 139</a></td>
      <td><b>Example 1:</b> 1D DP.</td>
      <td><b>Time:</b> O(N * M * L) or O(N^2)<br><b>Space:</b> O(N)</td>
      <td><code>#include <unordered_set></code></td>
      <td>-</td>
      <td><b>Explanation:</b> `dp[i]` is true if `s[0..i-1]` can be segmented. For each `i` from 1 to `N`, try each word in dictionary. If `s[i-len(word)..i-1] == word` and `dp[i-len(word)]` is true, then `dp[i] = true`. Or iterate `j` from 0 to `i` and check if `dp[j]` is true and `s[j..i-1]` is in dict.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def wordBreak(s: str, wordDict: List[str]) -&gt; bool:&#10;    dict_set = set(wordDict)&#10;    dp = [False] * (len(s) + 1)&#10;    dp[0] = True&#10;    for i in range(1, len(s) + 1):&#10;        for j in range(i):&#10;            if dp[j] and s[j:i] in dict_set:&#10;                dp[i] = True&#10;                break&#10;    return dp[len(s)]</code></pre></details></td>
    </tr>
    <tr>
      <td>55</td>
      <td>Dp 54 Count Palindromic Subsequences<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/count-palindromic-subsequences/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> 2D Interval DP.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N^2)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> If `s[i] == s[j]`, `dp[i][j] = dp[i+1][j] + dp[i][j-1] + 1`. If `s[i] != s[j]`, `dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def countPS(string: str) -&gt; int:&#10;    n = len(string)&#10;    mod = 10**9 + 7&#10;    dp = [[0] * n for _ in range(n)]&#10;    for i in range(n): dp[i][i] = 1&#10;    for length in range(2, n + 1):&#10;        for i in range(n - length + 1):&#10;            j = i + length - 1&#10;            if string[i] == string[j]:&#10;                dp[i][j] = (dp[i+1][j] + dp[i][j-1] + 1) % mod&#10;            else:&#10;                dp[i][j] = (dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]) % mod&#10;    return dp[0][n-1]</code></pre></details></td>
    </tr>
    <tr>
      <td>56</td>
      <td>Dp 55 Longest Alternating Subsequence<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/longest-alternating-subsequence5951/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Two state DP.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Maintain two lengths: `up` (ending with ascending) and `down` (ending with descending). Iterate array: if `arr[i] > arr[i-1]`, `up = down + 1`. If `arr[i] < arr[i-1]`, `down = up + 1`. Return `max(up, down)`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def AlternatingaMaxLength(nums: List[int]) -&gt; int:&#10;    if not nums: return 0&#10;    up = down = 1&#10;    for i in range(1, len(nums)):&#10;        if nums[i] &gt; nums[i-1]: up = down + 1&#10;        elif nums[i] &lt; nums[i-1]: down = up + 1&#10;    return max(up, down)</code></pre></details></td>
    </tr>
    <tr>
      <td>57</td>
      <td>Dp 56 Largest Square Formed In A Matrix<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/largest-square-formed-in-a-matrix0806/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Bottom-up DP.</td>
      <td><b>Time:</b> O(N * M)<br><b>Space:</b> O(N * M) or O(M)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> `dp[i][j]` is side of max square ending at `(i, j)`. If `mat[i][j] == 1`, `dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1`. Result is max over all `dp[i][j]`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxSquare(n: int, m: int, mat: List[List[int]]) -&gt; int:&#10;    dp = [[0] * m for _ in range(n)]&#10;    ans = 0&#10;    for i in range(n):&#10;        for j in range(m):&#10;            if mat[i][j] == 1:&#10;                if i == 0 or j == 0:&#10;                    dp[i][j] = 1&#10;                else:&#10;                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1&#10;                ans = max(ans, dp[i][j])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>58</td>
      <td>Dp 57 Pairs With Specific Difference<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/pairs-with-specific-difference1533/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Sort and DP or Greedy.</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Sort array. Iterate from end. If `arr[i] - arr[i-1] < K`, we pair them, add sum to answer, and `i -= 2`. Else, `i -= 1`. Greedy approach works because pairing larger numbers gives a larger sum.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxSumPairWithDifferenceLessThanK(arr: List[int], N: int, K: int) -&gt; int:&#10;    arr.sort()&#10;    ans = 0&#10;    i = N - 1&#10;    while i &gt; 0:&#10;        if arr[i] - arr[i-1] &lt; K:&#10;            ans += arr[i] + arr[i-1]&#10;            i -= 2&#10;        else:&#10;            i -= 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>59</td>
      <td>Dp 58 Maximum Path Sum In Matrix<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/path-in-matrix3805/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> 2D DP.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Start from bottom row up. `dp[i][j] = matrix[i][j] + max(dp[i+1][j], dp[i+1][j-1], dp[i+1][j+1])`. The answer is max value in `dp[0]`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maximumPath(N: int, Matrix: List[List[int]]) -&gt; int:&#10;    prev = Matrix[-1][:]&#10;    for i in range(N - 2, -1, -1):&#10;        curr = [0] * N&#10;        for j in range(N):&#10;            up = Matrix[i][j] + prev[j]&#10;            ld = Matrix[i][j] + prev[j-1] if j &gt; 0 else 0&#10;            rd = Matrix[i][j] + prev[j+1] if j &lt; N - 1 else 0&#10;            curr[j] = max(up, ld, rd)&#10;        prev = curr&#10;    return max(prev)</code></pre></details></td>
    </tr>
    <tr>
      <td>60</td>
      <td>Dp 59 Maximum Difference Of Zeros And Ones In Binary String<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/maximum-difference-of-zeros-and-ones-in-binary-string4111/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Kadane's Algorithm.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Convert '0' to 1 and '1' to -1. Find the maximum subarray sum using Kadane's algorithm. If max sum is negative, it means string has all 1s, return -1.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxSubstring(S: str) -&gt; int:&#10;    mx, curr = float(&#x27;-inf&#x27;), 0&#10;    for c in S:&#10;        val = 1 if c == &#x27;0&#x27; else -1&#10;        curr = max(val, curr + val)&#10;        mx = max(mx, curr)&#10;    return mx</code></pre></details></td>
    </tr>
    <tr>
      <td>61</td>
      <td>Dp 60 Minimum Number Of Jumps<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Greedy tracking bounds.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Maintain `maxReach`, `steps`, and `jumps`. At each step `i`, `maxReach = max(maxReach, i + arr[i])`. Decrement `steps`. If `steps == 0`, `jumps++` and `steps = maxReach - i`. If `i >= maxReach`, return -1.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minJumps(arr: List[int], n: int) -&gt; int:&#10;    if n &lt;= 1: return 0&#10;    if arr[0] == 0: return -1&#10;    maxReach = steps = arr[0]&#10;    jumps = 1&#10;    for i in range(1, n):&#10;        if i == n - 1: return jumps&#10;        maxReach = max(maxReach, i + arr[i])&#10;        steps -= 1&#10;        if steps == 0:&#10;            jumps += 1&#10;            if i &gt;= maxReach: return -1&#10;            steps = maxReach - i&#10;    return -1</code></pre></details></td>
    </tr>
    <tr>
      <td>62</td>
      <td>Dp 61 Minimum Removals From Array To Make Max Min K<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/minimum-removals3851/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> DP after sorting.</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Sort array. We want to find the longest subarray `arr[i..j]` such that `arr[j] - arr[i] <= K`. `dp[i]` could store the max `j` for index `i`. Or use Binary Search (`upper_bound`) for each `i` to find the valid `j`, maximizing `j - i + 1`. Total removed = `N - max_length`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import bisect&#10;def removals(arr: List[int], k: int) -&gt; int:&#10;    n = len(arr)&#10;    arr.sort()&#10;    maxLen = 0&#10;    for i in range(n):&#10;        j = bisect.bisect_right(arr, arr[i] + k) - 1&#10;        maxLen = max(maxLen, j - i + 1)&#10;    return n - maxLen</code></pre></details></td>
    </tr>
    <tr>
      <td>63</td>
      <td>Dp 62 Longest Common Substring<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/longest-common-substring1452/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> 2D DP.</td>
      <td><b>Time:</b> O(N * M)<br><b>Space:</b> O(M)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> `dp[i][j]` is the length of longest common suffix of `S1[0..i-1]` and `S2[0..j-1]`. If `S1[i-1] == S2[j-1]`, `dp[i][j] = dp[i-1][j-1] + 1`. Else, `dp[i][j] = 0`. Max value in `dp` table is answer.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def longestCommonSubstr(S1: str, S2: str, n: int, m: int) -&gt; int:&#10;    prev = [0] * (m + 1)&#10;    ans = 0&#10;    for i in range(1, n + 1):&#10;        curr = [0] * (m + 1)&#10;        for j in range(1, m + 1):&#10;            if S1[i-1] == S2[j-1]:&#10;                curr[j] = prev[j-1] + 1&#10;                ans = max(ans, curr[j])&#10;            else:&#10;                curr[j] = 0&#10;        prev = curr&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>64</td>
      <td>Dp 63 Reach A Given Score<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/reach-a-given-score-1587115621/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Unbounded Knapsack.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> `dp[i]` represents number of ways to reach score `i`. Init `dp[0] = 1`. For each score option (3, 5, 10), iterate from option to `n`, `dp[i] += dp[i - option]`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def count(n: int) -&gt; int:&#10;    dp = [0] * (n + 1)&#10;    dp[0] = 1&#10;    scores = [3, 5, 10]&#10;    for s in scores:&#10;        for i in range(s, n + 1):&#10;            dp[i] += dp[i - s]&#10;    return dp[n]</code></pre></details></td>
    </tr>
    <tr>
      <td>65</td>
      <td>Dp 14 Coin Change Minimum Coins<br><br></b> <a href='https://leetcode.com/problems/coin-change/' target='_blank'>LeetCode 322</a></td>
      <td><b>Example 1:</b> 1D Tabulation.</td>
      <td><b>Time:</b> O(amount * N)<br><b>Space:</b> O(amount)</td>
      <td>-</td>
      <td>Amount is 0</td>
      <td><b>Explanation:</b> Create an array `dp` of size `amount + 1` initialized to `amount + 1` (acting as infinity). `dp[0] = 0`. For each amount from 1 to `amount`, for each coin, if `i - coin >= 0`, `dp[i] = min(dp[i], dp[i - coin] + 1)`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def coinChange(coins: List[int], amount: int) -&gt; int:&#10;    dp = [amount + 1] * (amount + 1)&#10;    dp[0] = 0&#10;    for i in range(1, amount + 1):&#10;        for coin in coins:&#10;            if i - coin &gt;= 0:&#10;                dp[i] = min(dp[i], dp[i - coin] + 1)&#10;    return dp[amount] if dp[amount] &lt;= amount else -1</code></pre></details></td>
    </tr>
    <tr>
      <td>66</td>
      <td>Dp 15 Coin Change Maximum Ways<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/coin-change2448/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> 1D Tabulation.</td>
      <td><b>Time:</b> O(M * N)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Create a `dp` array of size `N + 1` initialized to 0. `dp[0] = 1`. For each coin, iterate through all amounts from `coin` to `N` and update `dp[j] += dp[j - coin]`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def count(coins: List[int], N: int, sum: int) -&gt; int:&#10;    dp = [0] * (sum + 1)&#10;    dp[0] = 1&#10;    for coin in coins:&#10;        for j in range(coin, sum + 1):&#10;            dp[j] += dp[j - coin]&#10;    return dp[sum]</code></pre></details></td>
    </tr>
    <tr>
      <td>67</td>
      <td>Dp 16 Longest Common Subsequence<br><br></b> <a href='https://leetcode.com/problems/longest-common-subsequence/' target='_blank'>LeetCode 1143</a></td>
      <td><b>Example 1:</b> 2D Tabulation.</td>
      <td><b>Time:</b> O(N * M)<br><b>Space:</b> O(N * M)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Create a 2D `dp` array. If `text1[i-1] == text2[j-1]`, then `dp[i][j] = 1 + dp[i-1][j-1]`. Else, `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def longestCommonSubsequence(text1: str, text2: str) -&gt; int:&#10;    n, m = len(text1), len(text2)&#10;    dp = [[0] * (m + 1) for _ in range(n + 1)]&#10;    for i in range(1, n + 1):&#10;        for j in range(1, m + 1):&#10;            if text1[i-1] == text2[j-1]:&#10;                dp[i][j] = 1 + dp[i-1][j-1]&#10;            else:&#10;                dp[i][j] = max(dp[i-1][j], dp[i][j-1])&#10;    return dp[n][m]</code></pre></details></td>
    </tr>
    <tr>
      <td>68</td>
      <td>Dp 17 Edit Distance<br><br></b> <a href='https://leetcode.com/problems/edit-distance/' target='_blank'>LeetCode 72</a></td>
      <td><b>Example 1:</b> 2D Tabulation.</td>
      <td><b>Time:</b> O(N * M)<br><b>Space:</b> O(N * M)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Create a 2D `dp` array. If `word1[i-1] == word2[j-1]`, then `dp[i][j] = dp[i-1][j-1]`. Else, `dp[i][j] = 1 + min(dp[i-1][j] (delete), min(dp[i][j-1] (insert), dp[i-1][j-1] (replace)))`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minDistance(word1: str, word2: str) -&gt; int:&#10;    n, m = len(word1), len(word2)&#10;    dp = [[0] * (m + 1) for _ in range(n + 1)]&#10;    for i in range(n + 1): dp[i][0] = i&#10;    for j in range(m + 1): dp[0][j] = j&#10;    for i in range(1, n + 1):&#10;        for j in range(1, m + 1):&#10;            if word1[i-1] == word2[j-1]:&#10;                dp[i][j] = dp[i-1][j-1]&#10;            else:&#10;                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])&#10;    return dp[n][m]</code></pre></details></td>
    </tr>
    <tr>
      <td>69</td>
      <td>Dp 18 Longest Increasing Subsequence<br><br></b> <a href='https://leetcode.com/problems/longest-increasing-subsequence/' target='_blank'>LeetCode 300</a></td>
      <td><b>Example 1:</b> O(N^2) Tabulation.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Create a `dp` array of size `n` initialized to 1. For each `i` from 1 to `n-1`, check all `j` from 0 to `i-1`. If `nums[i] > nums[j]`, update `dp[i] = max(dp[i], dp[j] + 1)`. The result is the max in `dp`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def lengthOfLIS(nums: List[int]) -&gt; int:&#10;    n = len(nums)&#10;    if n == 0: return 0&#10;    dp = [1] * n&#10;    for i in range(1, n):&#10;        for j in range(i):&#10;            if nums[i] &gt; nums[j]:&#10;                dp[i] = max(dp[i], dp[j] + 1)&#10;    return max(dp)</code></pre></details></td>
    </tr>
    <tr>
      <td>70</td>
      <td>Dp 19 0 1 Knapsack Problem<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> 1D Space Optimized DP.</td>
      <td><b>Time:</b> O(N * W)<br><b>Space:</b> O(W)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Use a 1D `dp` array of size `W + 1`. For each item, iterate backwards from `W` to `weight[i]`. `dp[w] = max(dp[w], val[i] + dp[w - weight[i]])`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def knapSack(W: int, wt: List[int], val: List[int], n: int) -&gt; int:&#10;    dp = [0] * (W + 1)&#10;    for i in range(n):&#10;        for w in range(W, wt[i] - 1, -1):&#10;            dp[w] = max(dp[w], val[i] + dp[w - wt[i]])&#10;    return dp[W]</code></pre></details></td>
    </tr>
    <tr>
      <td>71</td>
      <td>Dp 20 Maximum Product Subarray<br><br></b> <a href='https://leetcode.com/problems/maximum-product-subarray/' target='_blank'>LeetCode 152</a></td>
      <td><b>Example 1:</b> Keep track of max and min.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>Array containing zeros</td>
      <td><b>Explanation:</b> Iterate through the array while maintaining a `currMax` and `currMin`. If `nums[i] < 0`, swap `currMax` and `currMin`. `currMax = max(nums[i], currMax * nums[i])`. `currMin = min(nums[i], currMin * nums[i])`. Update `globalMax`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxProduct(nums: List[int]) -&gt; int:&#10;    if not nums: return 0&#10;    currMax = currMin = ans = nums[0]&#10;    for num in nums[1:]:&#10;        if num &lt; 0:&#10;            currMax, currMin = currMin, currMax&#10;        currMax = max(num, currMax * num)&#10;        currMin = min(num, currMin * num)&#10;        ans = max(ans, currMax)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>72</td>
      <td>Dp 21 Palindromic Partitioning<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/palindromic-patitioning4845/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> 1D DP.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N^2)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Create a `dp` array where `dp[i]` is min cuts for `str[0..i]`. Also use a 2D boolean DP to check if `str[j..i]` is a palindrome. If it is, `dp[i] = min(dp[i], dp[j-1] + 1)`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def palindromicPartition(string: str) -&gt; int:&#10;    n = len(string)&#10;    isPal = [[False] * n for _ in range(n)]&#10;    dp = [0] * n&#10;    for i in range(n):&#10;        minCut = i&#10;        for j in range(i + 1):&#10;            if string[i] == string[j] and (i - j &lt; 2 or isPal[j+1][i-1]):&#10;                isPal[j][i] = True&#10;                if j == 0:&#10;                    minCut = 0&#10;                else:&#10;                    minCut = min(minCut, dp[j-1] + 1)&#10;        dp[i] = minCut&#10;    return dp[-1]</code></pre></details></td>
    </tr>
    <tr>
      <td>73</td>
      <td>Dp 22 Partition Equal Subset Sum V2<br><br></b> <a href='https://leetcode.com/problems/partition-equal-subset-sum/' target='_blank'>LeetCode 416</a></td>
      <td><b>Example 1:</b> Target sum = Total / 2.</td>
      <td><b>Time:</b> O(N * Target)<br><b>Space:</b> O(Target)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> If total sum is odd, it's impossible. Otherwise, target is `sum / 2`. The problem reduces to subset sum. Use a boolean `dp` array of size `target + 1`. `dp[j] = dp[j] || dp[j - num]`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def canPartition(nums: List[int]) -&gt; bool:&#10;    total = sum(nums)&#10;    if total % 2 != 0: return False&#10;    target = total // 2&#10;    dp = [False] * (target + 1)&#10;    dp[0] = True&#10;    for num in nums:&#10;        for j in range(target, num - 1, -1):&#10;            dp[j] = dp[j] or dp[j - num]&#10;    return dp[target]</code></pre></details></td>
    </tr>
    <tr>
      <td>74</td>
      <td>Dp 23 Minimum Number Of Jumps<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Greedy (often grouped in DP).</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Use a greedy approach. Maintain `maxReach`, `step`, and `jump`. If `i == n - 1`, return `jump`. If `arr[0] == 0`, return -1. Otherwise, decrement `step`. If `step == 0`, `jump++`, `step = maxReach - i`. If `i >= maxReach`, it's impossible.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minJumps(arr: List[int], n: int) -&gt; int:&#10;    if n &lt;= 1: return 0&#10;    if arr[0] == 0: return -1&#10;    maxReach = arr[0]&#10;    step = arr[0]&#10;    jump = 1&#10;    for i in range(1, n):&#10;        if i == n - 1: return jump&#10;        maxReach = max(maxReach, i + arr[i])&#10;        step -= 1&#10;        if step == 0:&#10;            jump += 1&#10;            if i &gt;= maxReach: return -1&#10;            step = maxReach - i&#10;    return -1</code></pre></details></td>
    </tr>
  </tbody>
</table>
