# Arrays Revision Table

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
      <td rowspan="1">Arr 07 Missing Number<br><br></b> <a href='https://leetcode.com/problems/missing-number/' target='_blank'>LeetCode 268</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: nums = [3,0,1], Output: 2</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td>-</td>
      <td><b>Mathematical Sum alternative:</b> Gaussian sum formula `N*(N+1)/2` can cause integer overflow, XOR completely bypasses overflow risks.</td>
      <td><b>Explanation:</b> Using XOR: XORing a number with itself results in 0. XOR all indices `[0,n]` and all elements in `nums`. The missing number will remain.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def missingNumber(nums: list[int]) -&gt; int:&#10;    res = len(nums)&#10;    for i, num in enumerate(nums):&#10;        res ^= i ^ num&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">2</td>
      <td rowspan="1">Arr 09 Single Number<br><br></b> <a href='https://leetcode.com/problems/single-number/' target='_blank'>LeetCode 136</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: nums = [4,1,2,1,2], Output: 4<br><br><b>Note (Constraint):</b> Linear runtime and constant extra space.</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td>-</td>
      <td><b>Single Element array:</b> The loop just processes one element and returns it.</td>
      <td><b>Explanation:</b> XOR property: `A ^ A = 0` and `A ^ 0 = A`. XOR all elements together, duplicates cancel out, leaving only the single element.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def singleNumber(nums: list[int]) -&gt; int:&#10;    result = 0&#10;    for num in nums:&#10;        result ^= num&#10;    return result</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">3</td>
      <td rowspan="1">Arr 10 Sort Colors Dnf<br><br></b> <a href='https://leetcode.com/problems/sort-colors/' target='_blank'>LeetCode 75</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: nums = [2,0,2,1,1,0], Output: [0,0,1,1,2,2]<br><br><b>Note (Constraint):</b> Do not use library sort. Use single pass.</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><code>std::swap</code></td>
      <td><b>Mid pointer increment:</b> When swapping with `high`, we do NOT increment `mid` because the swapped element from `high` needs to be evaluated.</td>
      <td><b>Explanation:</b> Dutch National Flag Algorithm (3 pointers). `low` tracks 0s, `mid` scans array, `high` tracks 2s. Swap elements to maintain sections.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def sortColors(nums: list[int]) -&gt; None:&#10;    low, mid, high = 0, 0, len(nums) - 1&#10;    while mid &lt;= high:&#10;        if nums[mid] == 0:&#10;            nums[low], nums[mid] = nums[mid], nums[low]&#10;            low += 1; mid += 1&#10;        elif nums[mid] == 1:&#10;            mid += 1&#10;        else:&#10;            nums[mid], nums[high] = nums[high], nums[mid]&#10;            high -= 1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">4</td>
      <td rowspan="1">Arr 12 Kadanes Algorithm Max Subarray Sum<br><br></b> <a href='https://leetcode.com/problems/maximum-subarray/' target='_blank'>LeetCode 53</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: nums = [-2,1,-3,4,-1,2,1,-5,4], Output: 6 (Subarray [4,-1,2,1])</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><code>std::max</code></td>
      <td><b>All Negative Numbers:</b> Initialize `max_sum` with `INT_MIN` or `nums[0]` so it can correctly return the smallest negative number instead of 0.</td>
      <td><b>Explanation:</b> Kadane's Algorithm. Keep a running sum. If sum becomes negative, reset it to 0 (a negative prefix will never help a future subarray).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxSubArray(nums: list[int]) -&gt; int:&#10;    max_sum = float(&#x27;-inf&#x27;)&#10;    current_sum = 0&#10;    for num in nums:&#10;        current_sum += num&#10;        if current_sum &gt; max_sum:&#10;            max_sum = current_sum&#10;        if current_sum &lt; 0:&#10;            current_sum = 0&#10;    return int(max_sum)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">5</td>
      <td rowspan="1">Arr 13 Best Time To Buy And Sell Stock<br><br></b> <a href='https://leetcode.com/problems/best-time-to-buy-and-sell-stock/' target='_blank'>LeetCode 121</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: prices = [7,1,5,3,6,4], Output: 5</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1)</td>
      <td><code>std::max</code>, <code>std::min</code></td>
      <td><b>No Profit Possible:</b> `max_profit` initializes at 0. If price strictly decreases, it never updates and naturally returns 0.</td>
      <td><b>Explanation:</b> Iterate while keeping track of the minimum price seen so far. Subtract this min from the current price to find potential profit.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxProfit(prices: list[int]) -&gt; int:&#10;    min_price = prices[0]&#10;    max_profit = 0&#10;    for i in range(1, len(prices)):&#10;        max_profit = max(max_profit, prices[i] - min_price)&#10;        min_price = min(min_price, prices[i])&#10;    return max_profit</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">6</td>
      <td rowspan="1">Arr 15 Next Permutation<br><br></b> <a href='https://leetcode.com/problems/next-permutation/' target='_blank'>LeetCode 31</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: nums = [1,2,3], Output: [1,3,2]<br><b>Example 2:</b> Input: nums = [3,2,1], Output: [1,2,3]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><code>std::reverse</code></td>
      <td><b>Last Permutation:</b> If break point is not found (`i < 0`), it means the array is sorted descending. Just reverse the entire array to get the lowest permutation.</td>
      <td><b>Explanation:</b> 1. Find break point (i) where arr[i] < arr[i+1]. 2. Swap it with smallest element > arr[i] from the back. 3. Reverse the right half.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def nextPermutation(nums: list[int]) -&gt; None:&#10;    n = len(nums)&#10;    i = n - 2&#10;    while i &gt;= 0 and nums[i] &gt;= nums[i + 1]:&#10;        i -= 1&#10;        &#10;    if i &gt;= 0:&#10;        j = n - 1&#10;        while nums[j] &lt;= nums[i]:&#10;            j -= 1&#10;        nums[i], nums[j] = nums[j], nums[i]&#10;        &#10;    nums[i+1:] = reversed(nums[i+1:])</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">7</td>
      <td rowspan="1">Arr 18 3Sum<br><br></b> <a href='https://leetcode.com/problems/3sum/' target='_blank'>LeetCode 15</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: nums = [-1,0,1,2,-1,-4], Output: [[-1,-1,2],[-1,0,1]]<br><br><b>Note (Constraint):</b> Solution set must not contain duplicate triplets.</td>
      <td><b>Time:</b> O(N<sup>2</sup>) (Constraint)<br><b>Space:</b> O(1) (Trade-off)</td>
      <td><code>std::sort</code></td>
      <td><b>Duplicate skipping:</b> To prevent duplicate triplets, skip identical adjacent elements for `i`, `j`, and `k`.</td>
      <td><b>Explanation:</b> Sort the array. Use a loop to fix `i`, then use a Two-Pointer approach (`j`, `k`) for the remaining array to find sum `0 - nums[i]`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def threeSum(nums: list[int]) -&gt; list[list[int]]:&#10;    ans = []&#10;    nums.sort()&#10;    n = len(nums)&#10;    for i in range(n):&#10;        if i &gt; 0 and nums[i] == nums[i-1]: continue&#10;        j, k = i + 1, n - 1&#10;        while j &lt; k:&#10;            s = nums[i] + nums[j] + nums[k]&#10;            if s &lt; 0:&#10;                j += 1&#10;            elif s &gt; 0:&#10;                k -= 1&#10;            else:&#10;                ans.append([nums[i], nums[j], nums[k]])&#10;                j += 1; k -= 1&#10;                while j &lt; k and nums[j] == nums[j-1]: j += 1&#10;                while j &lt; k and nums[k] == nums[k+1]: k -= 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">8</td>
      <td rowspan="1">Arr 19 Merge Intervals<br><br></b> <a href='https://leetcode.com/problems/merge-intervals/' target='_blank'>LeetCode 56</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: intervals = [[1,3],[2,6],[8,10],[15,18]], Output: [[1,6],[8,10],[15,18]]</td>
      <td><b>Time:</b> O(N log N) (Constraint)<br><b>Space:</b> O(N)</td>
      <td><code>std::sort</code></td>
      <td><b>Subsumed Intervals:</b> `[1,4]` and `[2,3]` -> using `max()` prevents shrinking the end time to `3`.</td>
      <td><b>Explanation:</b> Sort the intervals based on the start time. Iterate and merge: if current start <= previous end, update previous end to `max(prev_end, curr_end)`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def merge(intervals: list[list[int]]) -&gt; list[list[int]]:&#10;    if not intervals: return []&#10;    intervals.sort(key=lambda x: x[0])&#10;    merged = [intervals[0]]&#10;    for i in range(1, len(intervals)):&#10;        if intervals[i][0] &lt;= merged[-1][1]:&#10;            merged[-1][1] = max(merged[-1][1], intervals[i][1])&#10;        else:&#10;            merged.append(intervals[i])&#10;    return merged</code></pre></details></td>
    </tr>
  </tbody>
</table>
