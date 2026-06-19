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
      <td rowspan="1">1</td>
      <td rowspan="1">Dp 01 Climbing Stairs<br><br></b> <a href='https://leetcode.com/problems/climbing-stairs/' target='_blank'>LeetCode 70</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: n = 3, Output: 3 (1+1+1, 1+2, 2+1)</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1) (Constraint)</td>
      <td>-</td>
      <td><b>Variable Swapping:</b> `prev2` becomes `prev`, and `prev` becomes the new `curr`.</td>
      <td><b>Explanation:</b> Space Optimization (Bottom-Up): Since state `n` only depends on `n-1` and `n-2`, we only need two variables.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def climbStairs(n: int) -&gt; int:&#10;    if n &lt;= 1: return 1&#10;    prev2, prev = 1, 1&#10;    for i in range(2, n + 1):&#10;        curr = prev + prev2&#10;        prev2, prev = prev, curr&#10;    return prev</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">2</td>
      <td rowspan="1">Dp 02 Longest Common Subsequence<br><br></b> <a href='https://leetcode.com/problems/longest-common-subsequence/' target='_blank'>LeetCode 1143</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: text1 = "abcde", text2 = "ace", Output: 3 ("ace")</td>
      <td><b>Time:</b> O(M * N) (Constraint)<br><b>Space:</b> O(M * N) (Trade-off)</td>
      <td><code>std::max</code></td>
      <td><b>1-Based Indexing:</b> Shifting indices by 1 prevents out-of-bounds checks and elegantly handles the 0-length prefix base case.</td>
      <td><b>Explanation:</b> Tabulation (Bottom-Up). Use a 2D array where `dp[i][j]` represents the LCS of prefixes of length `i` and `j`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def longestCommonSubsequence(text1: str, text2: str) -&gt; int:&#10;    n, m = len(text1), len(text2)&#10;    dp = [[0] * (m + 1) for _ in range(n + 1)]&#10;    for i in range(1, n + 1):&#10;        for j in range(1, m + 1):&#10;            if text1[i - 1] == text2[j - 1]:&#10;                dp[i][j] = 1 + dp[i - 1][j - 1]&#10;            else:&#10;                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])&#10;    return dp[n][m]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">3</td>
      <td rowspan="1">Dp 03 Coin Change<br><br></b> <a href='https://leetcode.com/problems/coin-change/' target='_blank'>LeetCode 322</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: coins = [1,2,5], amount = 11, Output: 3 (5+5+1)</td>
      <td><b>Time:</b> O(Amount * N)<br><b>Space:</b> O(Amount)</td>
      <td><code>std::min</code></td>
      <td><b>Initialization:</b> Fill array with `Amount + 1` (acting as infinity). If `dp[Amount]` remains `Amount + 1`, return `-1`.</td>
      <td><b>Explanation:</b> Unbounded Knapsack. State `dp[i]` is the min coins needed to make amount `i`. `dp[i] = min(dp[i], 1 + dp[i - coin])`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def coinChange(coins: list[int], amount: int) -&gt; int:&#10;    dp = [amount + 1] * (amount + 1)&#10;    dp[0] = 0&#10;    for i in range(1, amount + 1):&#10;        for coin in coins:&#10;            if i - coin &gt;= 0:&#10;                dp[i] = min(dp[i], 1 + dp[i - coin])&#10;    return dp[amount] if dp[amount] &lt;= amount else -1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">4</td>
      <td rowspan="1">Dp 04 Longest Increasing Subsequence<br><br></b> <a href='https://leetcode.com/problems/longest-increasing-subsequence/' target='_blank'>LeetCode 300</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: nums = [10,9,2,5,3,7,101,18], Output: 4 ([2,3,7,101])</td>
      <td><b>Time:</b> O(N log N) (Constraint)<br><b>Space:</b> O(N)</td>
      <td><code>std::lower_bound</code> / <code>bisect_left</code></td>
      <td><b>Temp Array:</b> `temp` does NOT store the actual LIS, but its length correctly represents the LIS length.</td>
      <td><b>Explanation:</b> Binary Search Patience Sorting method. Maintain a `temp` array. If current element is larger than `temp.back()`, append. Else, replace the first element >= current.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import bisect&#10;def lengthOfLIS(nums: list[int]) -&gt; int:&#10;    temp = []&#10;    for num in nums:&#10;        idx = bisect.bisect_left(temp, num)&#10;        if idx == len(temp):&#10;            temp.append(num)&#10;        else:&#10;            temp[idx] = num&#10;    return len(temp)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">5</td>
      <td rowspan="1">Dp 05 House Robber<br><br></b> <a href='https://leetcode.com/problems/house-robber/' target='_blank'>LeetCode 198</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: nums = [1,2,3,1], Output: 4 (Rob house 1 and 3)</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><code>std::max</code></td>
      <td><b>Array length < 2:</b> Automatically handled if initialized properly and loop condition ensures no out-of-bounds.</td>
      <td><b>Explanation:</b> Space Optimized DP. Maintain two variables: `prev1` (max up to previous house) and `prev2` (max up to the house before previous). `curr = max(num + prev2, prev1)`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def rob(nums: list[int]) -&gt; int:&#10;    prev1, prev2 = 0, 0&#10;    for num in nums:&#10;        curr = max(num + prev2, prev1)&#10;        prev2 = prev1&#10;        prev1 = curr&#10;    return prev1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">6</td>
      <td rowspan="1">Dp 06 Maximum Product Subarray<br><br></b> <a href='https://leetcode.com/problems/maximum-product-subarray/' target='_blank'>LeetCode 152</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: nums = [2,3,-2,4], Output: 6 ([2,3])</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><code>std::max</code></td>
      <td><b>Zero Element:</b> A zero resets the contiguous product segment. We restart the prefix/suffix product from `1`.</td>
      <td><b>Explanation:</b> Prefix and Suffix product approach. Calculate product from left to right and right to left. Reset product to 1 when a zero is encountered.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxProduct(nums: list[int]) -&gt; int:&#10;    max_prod = float(&#x27;-inf&#x27;)&#10;    pref, suff = 1, 1&#10;    n = len(nums)&#10;    for i in range(n):&#10;        if pref == 0: pref = 1&#10;        if suff == 0: suff = 1&#10;        pref *= nums[i]&#10;        suff *= nums[n - 1 - i]&#10;        max_prod = max(max_prod, pref, suff)&#10;    return int(max_prod)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">7</td>
      <td rowspan="1">Dp 06 Longest Increasing Subsequence<br><br></b> <a href='https://leetcode.com/problems/longest-increasing-subsequence/' target='_blank'>LeetCode 300</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: nums = [10,9,2,5,3,7,101,18], Output: 4 (LIS is [2,3,7,101])</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td><b>Empty Array:</b> Handled appropriately.</td>
      <td><b>Explanation:</b> Create a dp array where dp[i] is the length of LIS ending at index i. For each i, check all j < i to see if nums[i] > nums[j] and update dp[i] = max(dp[i], dp[j] + 1). O(N log N) patience sorting approach is better but standard DP is O(N^2).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def lengthOfLIS(nums: List[int]) -&gt; int:&#10;    if not nums: return 0&#10;    dp = [1] * len(nums)&#10;    for i in range(1, len(nums)):&#10;        for j in range(i):&#10;            if nums[i] &gt; nums[j]: dp[i] = max(dp[i], dp[j] + 1)&#10;    return max(dp)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">8</td>
      <td rowspan="1">Dp 07 Coin Change<br><br></b> <a href='https://leetcode.com/problems/coin-change/' target='_blank'>LeetCode 322</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: coins = [1,2,5], amount = 11, Output: 3 (5+5+1)</td>
      <td><b>Time:</b> O(amount * N)<br><b>Space:</b> O(amount)</td>
      <td>-</td>
      <td><b>Cannot make amount:</b> Check if dp[amount] > amount, return -1.</td>
      <td><b>Explanation:</b> Bottom-up DP. dp[i] = min coins for amount i. Initialize dp array with amount + 1. dp[i] = min(dp[i], dp[i - coin] + 1).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def coinChange(coins: List[int], amount: int) -&gt; int:&#10;    dp = [amount + 1] * (amount + 1)&#10;    dp[0] = 0&#10;    for i in range(1, amount + 1):&#10;        for c in coins:&#10;            if i - c &gt;= 0: dp[i] = min(dp[i], dp[i - c] + 1)&#10;    return dp[amount] if dp[amount] != amount + 1 else -1</code></pre></details></td>
    </tr>
  </tbody>
</table>
