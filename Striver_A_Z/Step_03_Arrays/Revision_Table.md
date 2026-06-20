# Step 03 Arrays Revision Table

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
      <td>Arr 01 Largest Element<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/largest-element-in-array/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: A = [1, 8, 7, 56, 90], Output: 90</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><b>Explanation:</b> Iterate through the array maintaining a variable for the maximum element seen so far.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def largest(arr: list[int]) -&gt; int:&#10;    max_val = arr[0]&#10;    for num in arr:&#10;        if num &gt; max_val:&#10;            max_val = num&#10;    return max_val</code></pre></details></td>
    </tr>
    <tr>
      <td>2</td>
      <td>Arr 02 Second Largest Element<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/second-largest3735/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: arr = [12, 35, 1, 10, 34, 1], Output: 34<br><br>**Note (Constraint):** Find it in a single pass O(N) time.</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><b>Explanation:</b> Maintain two variables, `largest` and `second_largest`. Update them simultaneously during a single pass.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print2largest(arr: list[int]) -&gt; int:&#10;    largest = -1&#10;    second_largest = -1&#10;    for num in arr:&#10;        if num &gt; largest:&#10;            second_largest = largest&#10;            largest = num&#10;        elif num &gt; second_largest and num != largest:&#10;            second_largest = num&#10;    return second_largest</code></pre></details></td>
    </tr>
    <tr>
      <td>3</td>
      <td>Arr 03 Check If Array Is Sorted And Rotated<br><br></b> <a href="https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/" target="_blank">LeetCode 1752</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: nums = [3,4,5,1,2], Output: true</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><b>Explanation:</b> Count the number of "breaks" where `nums[i] > nums[i+1]`. For a sorted and rotated array, there can be at most 1 break.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def check(nums: list[int]) -&gt; bool:&#10;    count = 0&#10;    n = len(nums)&#10;    for i in range(n):&#10;        if nums[i] &gt; nums[(i + 1) % n]:&#10;            count += 1&#10;    return count &lt;= 1</code></pre></details></td>
    </tr>
    <tr>
      <td>4</td>
      <td>Arr 04 Remove Duplicates From Sorted Array<br><br></b> <a href="https://leetcode.com/problems/remove-duplicates-from-sorted-array/" target="_blank">LeetCode 26</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: nums = [1,1,2], Output: 2, nums = [1,2,_]</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><b>Explanation:</b> Two-pointer approach. Pointer `i` keeps track of unique elements, pointer `j` scans the array to find new unique elements.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def removeDuplicates(nums: list[int]) -&gt; int:&#10;    if not nums: return 0&#10;    i = 0&#10;    for j in range(1, len(nums)):&#10;        if nums[j] != nums[i]:&#10;            i += 1&#10;            nums[i] = nums[j]&#10;    return i + 1</code></pre></details></td>
    </tr>
    <tr>
      <td>5</td>
      <td>Arr 05 Rotate Array<br><br></b> <a href="https://leetcode.com/problems/rotate-array/" target="_blank">LeetCode 189</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: nums = [1,2,3,4,5,6,7], k = 3, Output: [5,6,7,1,2,3,4]</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><b>Explanation:</b> Reverse Algorithm. Reverse the whole array, then reverse the first `k` elements, then reverse the remaining `N-k` elements.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def rotate(nums: list[int], k: int) -&gt; None:&#10;    n = len(nums)&#10;    k = k % n&#10;    nums.reverse()&#10;    nums[:k] = reversed(nums[:k])&#10;    nums[k:] = reversed(nums[k:])</code></pre></details></td>
    </tr>
    <tr>
      <td>6</td>
      <td>Arr 06 Move Zeroes<br><br></b> <a href="https://leetcode.com/problems/move-zeroes/" target="_blank">LeetCode 283</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: nums = [0,1,0,3,12], Output: [1,3,12,0,0]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Two-pointer approach (Snowball method). Pointer `i` tracks the first zero found, pointer `j` scans for non-zeroes to swap.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def moveZeroes(nums: list[int]) -&gt; None:&#10;    i = 0&#10;    for j in range(len(nums)):&#10;        if nums[j] != 0:&#10;            nums[i], nums[j] = nums[j], nums[i]&#10;            i += 1</code></pre></details></td>
    </tr>
    <tr>
      <td>7</td>
      <td>Arr 07 Missing Number<br><br></b> <a href="https://leetcode.com/problems/missing-number/" target="_blank">LeetCode 268</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: nums = [3,0,1], Output: 2</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><b>Explanation:</b> Using XOR: XORing a number with itself results in 0. XOR all indices `[0,n]` and all elements in `nums`. The missing number will remain.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def missingNumber(nums: list[int]) -&gt; int:&#10;    res = len(nums)&#10;    for i, num in enumerate(nums):&#10;        res ^= i ^ num&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td>8</td>
      <td>Arr 08 Max Consecutive Ones<br><br></b> <a href="https://leetcode.com/problems/max-consecutive-ones/" target="_blank">LeetCode 485</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: nums = [1,1,0,1,1,1], Output: 3</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Iterate while counting 1s. If a 0 is found, update max count and reset current count to 0.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findMaxConsecutiveOnes(nums: list[int]) -&gt; int:&#10;    max_cnt = current_cnt = 0&#10;    for num in nums:&#10;        if num == 1:&#10;            current_cnt += 1&#10;            max_cnt = max(max_cnt, current_cnt)&#10;        else:&#10;            current_cnt = 0&#10;    return max_cnt</code></pre></details></td>
    </tr>
    <tr>
      <td>9</td>
      <td>Arr 09 Sort Colors Dnf<br><br></b> <a href="https://leetcode.com/problems/sort-colors/" target="_blank">LeetCode 75</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: nums = [2,0,2,1,1,0], Output: [0,0,1,1,2,2]<br><br>**Note (Constraint):** Do not use library sort. Use single pass.</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><b>Explanation:</b> Dutch National Flag Algorithm (3 pointers). `low` tracks 0s, `mid` scans array, `high` tracks 2s. Swap elements to maintain sections.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def sortColors(nums: list[int]) -&gt; None:&#10;    low, mid, high = 0, 0, len(nums) - 1&#10;    while mid &lt;= high:&#10;        if nums[mid] == 0:&#10;            nums[low], nums[mid] = nums[mid], nums[low]&#10;            low += 1; mid += 1&#10;        elif nums[mid] == 1:&#10;            mid += 1&#10;        else:&#10;            nums[mid], nums[high] = nums[high], nums[mid]&#10;            high -= 1</code></pre></details></td>
    </tr>
    <tr>
      <td>10</td>
      <td>Arr 10 Majority Element<br><br></b> <a href="https://leetcode.com/problems/majority-element/" target="_blank">LeetCode 169</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: nums = [2,2,1,1,1,2,2], Output: 2</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Moore's Voting Algorithm. Track a candidate and a counter. Increment if same as candidate, decrement if different. If zero, pick new candidate.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def majorityElement(nums: list[int]) -&gt; int:&#10;    count = candidate = 0&#10;    for num in nums:&#10;        if count == 0:&#10;            candidate = num&#10;        count += (1 if num == candidate else -1)&#10;    return candidate</code></pre></details></td>
    </tr>
    <tr>
      <td>11</td>
      <td>Arr 11 Kadanes Algorithm Max Subarray Sum<br><br></b> <a href="https://leetcode.com/problems/maximum-subarray/" target="_blank">LeetCode 53</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: nums = [-2,1,-3,4,-1,2,1,-5,4], Output: 6 (Subarray [4,-1,2,1])</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><b>Explanation:</b> Kadane's Algorithm. Keep a running sum. If sum becomes negative, reset it to 0 (a negative prefix will never help a future subarray).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxSubArray(nums: list[int]) -&gt; int:&#10;    max_sum = float(&#x27;-inf&#x27;)&#10;    current_sum = 0&#10;    for num in nums:&#10;        current_sum += num&#10;        if current_sum &gt; max_sum:&#10;            max_sum = current_sum&#10;        if current_sum &lt; 0:&#10;            current_sum = 0&#10;    return int(max_sum)</code></pre></details></td>
    </tr>
    <tr>
      <td>12</td>
      <td>Arr 12 Best Time To Buy And Sell Stock<br><br></b> <a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock/" target="_blank">LeetCode 121</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> SDE Sheet, Love Babbar, Striver A Z</details></td>
      <td>**Example 1:** Input: prices = [7,1,5,3,6,4], Output: 5</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Iterate while keeping track of the minimum price seen so far. Subtract this min from the current price to find potential profit.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxProfit(prices: list[int]) -&gt; int:&#10;    min_price = prices[0]&#10;    max_profit = 0&#10;    for i in range(1, len(prices)):&#10;        max_profit = max(max_profit, prices[i] - min_price)&#10;        min_price = min(min_price, prices[i])&#10;    return max_profit</code></pre></details></td>
    </tr>
    <tr>
      <td>13</td>
      <td>Arr 13 Rearrange Array Elements By Sign<br><br></b> <a href="https://leetcode.com/problems/rearrange-array-elements-by-sign/" target="_blank">LeetCode 2149</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: nums = [3,1,-2,-5,2,-4], Output: [3,-2,1,-5,2,-4]<br><br>**Note (Constraint):** Maintain relative order.</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(N) (Constraint)</td>
      <td><b>Explanation:</b> Use two pointers, `pos_idx` starting at 0, `neg_idx` starting at 1. Traverse and place elements directly into a new result array.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def rearrangeArray(nums: list[int]) -&gt; list[int]:&#10;    ans = [0] * len(nums)&#10;    pos_idx, neg_idx = 0, 1&#10;    for num in nums:&#10;        if num &gt; 0:&#10;            ans[pos_idx] = num&#10;            pos_idx += 2&#10;        else:&#10;            ans[neg_idx] = num&#10;            neg_idx += 2&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>14</td>
      <td>Arr 14 Next Permutation<br><br></b> <a href="https://leetcode.com/problems/next-permutation/" target="_blank">LeetCode 31</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, SDE Sheet, Striver A Z</details></td>
      <td>**Example 1:** Input: nums = [1,2,3], Output: [1,3,2]<br>**Example 2:** Input: nums = [3,2,1], Output: [1,2,3]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> 1. Find break point (i) where arr[i] < arr[i+1]. 2. Swap it with smallest element > arr[i] from the back. 3. Reverse the right half.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def nextPermutation(nums: list[int]) -&gt; None:&#10;    n = len(nums)&#10;    i = n - 2&#10;    while i &gt;= 0 and nums[i] &gt;= nums[i + 1]:&#10;        i -= 1&#10;        &#10;    if i &gt;= 0:&#10;        j = n - 1&#10;        while nums[j] &lt;= nums[i]:&#10;            j -= 1&#10;        nums[i], nums[j] = nums[j], nums[i]&#10;        &#10;    nums[i+1:] = reversed(nums[i+1:])</code></pre></details></td>
    </tr>
    <tr>
      <td>15</td>
      <td>Arr 15 Pascals Triangle<br><br></b> <a href="https://leetcode.com/problems/pascals-triangle/" target="_blank">LeetCode 118</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: numRows = 5, Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]</td>
      <td><b>Time:</b> O(N<sup>2</sup>) (Constraint)<br><b>Space:</b> O(N<sup>2</sup>) (Constraint)</td>
      <td><b>Explanation:</b> Generate row by row. Each element `val[i][j]` is the sum of `val[i-1][j-1]` and `val[i-1][j]`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def generate(numRows: int) -&gt; list[list[int]]:&#10;    ans = []&#10;    for i in range(numRows):&#10;        row = [1] * (i + 1)&#10;        for j in range(1, i):&#10;            row[j] = ans[i-1][j-1] + ans[i-1][j]&#10;        ans.append(row)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>16</td>
      <td>Arr 16 Majority Element Ii<br><br></b> <a href="https://leetcode.com/problems/majority-element-ii/" target="_blank">LeetCode 229</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, SDE Sheet, Striver A Z</details></td>
      <td>**Example 1:** Input: nums = [3,2,3], Output: [3]<br><br>**Note (Constraint):** Time O(N), Space O(1).</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><b>Explanation:</b> Extended Moore's Voting Algorithm. At most TWO elements can appear > N/3 times. Track two candidates and two counters.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def majorityElement(nums: list[int]) -&gt; list[int]:&#10;    cnt1, cnt2, el1, el2 = 0, 0, float(&#x27;-inf&#x27;), float(&#x27;-inf&#x27;)&#10;    for num in nums:&#10;        if cnt1 == 0 and num != el2:&#10;            cnt1 = 1; el1 = num&#10;        elif cnt2 == 0 and num != el1:&#10;            cnt2 = 1; el2 = num&#10;        elif num == el1:&#10;            cnt1 += 1&#10;        elif num == el2:&#10;            cnt2 += 1&#10;        else:&#10;            cnt1 -= 1; cnt2 -= 1&#10;            &#10;    ans = []&#10;    if nums.count(el1) &gt; len(nums) // 3:&#10;        ans.append(el1)&#10;    if nums.count(el2) &gt; len(nums) // 3:&#10;        ans.append(el2)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>17</td>
      <td>Arr 17 3Sum<br><br></b> <a href="https://leetcode.com/problems/3sum/" target="_blank">LeetCode 15</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> SDE Sheet, Love Babbar, Striver A Z</details></td>
      <td>**Example 1:** Input: nums = [-1,0,1,2,-1,-4], Output: [[-1,-1,2],[-1,0,1]]<br><br>**Note (Constraint):** Solution set must not contain duplicate triplets.</td>
      <td><b>Time:</b> O(N<sup>2</sup>) (Constraint)<br><b>Space:</b> O(1) (Trade-off)</td>
      <td><b>Explanation:</b> Sort the array. Use a loop to fix `i`, then use a Two-Pointer approach (`j`, `k`) for the remaining array to find sum `0 - nums[i]`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def threeSum(nums: list[int]) -&gt; list[list[int]]:&#10;    ans = []&#10;    nums.sort()&#10;    n = len(nums)&#10;    for i in range(n):&#10;        if i &gt; 0 and nums[i] == nums[i-1]: continue&#10;        j, k = i + 1, n - 1&#10;        while j &lt; k:&#10;            s = nums[i] + nums[j] + nums[k]&#10;            if s &lt; 0:&#10;                j += 1&#10;            elif s &gt; 0:&#10;                k -= 1&#10;            else:&#10;                ans.append([nums[i], nums[j], nums[k]])&#10;                j += 1; k -= 1&#10;                while j &lt; k and nums[j] == nums[j-1]: j += 1&#10;                while j &lt; k and nums[k] == nums[k+1]: k -= 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>18</td>
      <td>Arr 18 Merge Intervals<br><br></b> <a href="https://leetcode.com/problems/merge-intervals/" target="_blank">LeetCode 56</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, SDE Sheet, Striver A Z</details></td>
      <td>**Example 1:** Input: intervals = [[1,3],[2,6],[8,10],[15,18]], Output: [[1,6],[8,10],[15,18]]</td>
      <td><b>Time:</b> O(N log N) (Constraint)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Sort the intervals based on the start time. Iterate and merge: if current start <= previous end, update previous end to `max(prev_end, curr_end)`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def merge(intervals: list[list[int]]) -&gt; list[list[int]]:&#10;    if not intervals: return []&#10;    intervals.sort(key=lambda x: x[0])&#10;    merged = [intervals[0]]&#10;    for i in range(1, len(intervals)):&#10;        if intervals[i][0] &lt;= merged[-1][1]:&#10;            merged[-1][1] = max(merged[-1][1], intervals[i][1])&#10;        else:&#10;            merged.append(intervals[i])&#10;    return merged</code></pre></details></td>
    </tr>
    <tr>
      <td>19</td>
      <td>Arr 19 Leaders In An Array<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: A = [16,17,4,3,5,2], Output: [17,5,2]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N) for output</td>
      <td><b>Explanation:</b> Traverse the array from right to left. Keep track of the maximum element seen so far. If the current element is greater than or equal to the max, it's a leader. Reverse the collected leaders at the end.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def leaders(A: List[int], N: int) -&gt; List[int]:&#10;    ans = []&#10;    maxi = A[N - 1]&#10;    ans.append(maxi)&#10;    for i in range(N - 2, -1, -1):&#10;        if A[i] &gt;= maxi:&#10;            ans.append(A[i])&#10;            maxi = A[i]&#10;    ans.reverse()&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>20</td>
      <td>Arr 20 Set Matrix Zeroes<br><br></b> <a href="https://leetcode.com/problems/set-matrix-zeroes/" target="_blank">LeetCode 73</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: matrix = [[1,1,1],[1,0,1],[1,1,1]], Output: [[1,0,1],[0,0,0],[1,0,1]]</td>
      <td><b>Time:</b> O(N * M)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Use the first row and first column as marker arrays to save space. We need a separate variable for the first column (or row) to avoid overlapping states.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def setZeroes(matrix: List[List[int]]) -&gt; None:&#10;    n, m, col0 = len(matrix), len(matrix[0]), 1&#10;    for i in range(n):&#10;        if matrix[i][0] == 0: col0 = 0&#10;        for j in range(1, m):&#10;            if matrix[i][j] == 0: matrix[i][0] = matrix[0][j] = 0&#10;    for i in range(n-1, -1, -1):&#10;        for j in range(m-1, 0, -1):&#10;            if matrix[i][0] == 0 or matrix[0][j] == 0: matrix[i][j] = 0&#10;        if col0 == 0: matrix[i][0] = 0</code></pre></details></td>
    </tr>
    <tr>
      <td>21</td>
      <td>Arr 21 Rotate Image<br><br></b> <a href="https://leetcode.com/problems/rotate-image/" target="_blank">LeetCode 48</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: matrix = [[1,2,3],[4,5,6],[7,8,9]], Output: [[7,4,1],[8,5,2],[9,6,3]]</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Transpose the matrix (swap matrix[i][j] with matrix[j][i]), then reverse every row.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def rotate(matrix: List[List[int]]) -&gt; None:&#10;    n = len(matrix)&#10;    for i in range(n):&#10;        for j in range(i):&#10;            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]&#10;    for i in range(n):&#10;        matrix[i].reverse()</code></pre></details></td>
    </tr>
    <tr>
      <td>22</td>
      <td>Arr 22 Spiral Matrix<br><br></b> <a href="https://leetcode.com/problems/spiral-matrix/" target="_blank">LeetCode 54</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: matrix = [[1,2,3],[4,5,6],[7,8,9]], Output: [1,2,3,6,9,8,7,4,5]</td>
      <td><b>Time:</b> O(N * M)<br><b>Space:</b> O(N * M) for output</td>
      <td><b>Explanation:</b> Maintain 4 pointers: top, bottom, left, right. Traverse Top row, Right col, Bottom row, Left col, shrinking boundaries inwards.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def spiralOrder(matrix: List[List[int]]) -&gt; List[int]:&#10;    ans = []&#10;    top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1&#10;    while top &lt;= bottom and left &lt;= right:&#10;        for i in range(left, right+1): ans.append(matrix[top][i])&#10;        top += 1&#10;        for i in range(top, bottom+1): ans.append(matrix[i][right])&#10;        right -= 1&#10;        if top &lt;= bottom:&#10;            for i in range(right, left-1, -1): ans.append(matrix[bottom][i])&#10;            bottom -= 1&#10;        if left &lt;= right:&#10;            for i in range(bottom, top-1, -1): ans.append(matrix[i][left])&#10;            left += 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>23</td>
      <td>Arr 23 4Sum<br><br></b> <a href="https://leetcode.com/problems/4sum/" target="_blank">LeetCode 18</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, SDE Sheet, Striver A Z</details></td>
      <td>**Example 1:** Input: nums = [1,0,-1,0,-2,2], target = 0, Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]</td>
      <td><b>Time:</b> O(N^3)<br><b>Space:</b> O(1) auxiliary</td>
      <td><b>Explanation:</b> Sort array. Use 2 nested loops (i, j) for the first two numbers, and Two Pointers (k, l) for the remaining two. Skip duplicates carefully.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def fourSum(nums: List[int], target: int) -&gt; List[List[int]]:&#10;    ans = []&#10;    n = len(nums); nums.sort()&#10;    for i in range(n):&#10;        if i &gt; 0 and nums[i] == nums[i-1]: continue&#10;        for j in range(i+1, n):&#10;            if j &gt; i+1 and nums[j] == nums[j-1]: continue&#10;            k, l = j+1, n-1&#10;            while k &lt; l:&#10;                total = nums[i] + nums[j] + nums[k] + nums[l]&#10;                if total == target:&#10;                    ans.append([nums[i], nums[j], nums[k], nums[l]])&#10;                    k += 1; l -= 1&#10;                    while k &lt; l and nums[k] == nums[k-1]: k += 1&#10;                    while k &lt; l and nums[l] == nums[l+1]: l -= 1&#10;                elif total &lt; target: k += 1&#10;                else: l -= 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>24</td>
      <td>Arr 24 Count Subarrays With Given Xor K<br><br></b> <a href="https://www.interviewbit.com/problems/subarray-with-given-xor/" target="_blank">InterviewBit</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, SDE Sheet, Striver A Z</details></td>
      <td>**Example 1:** Input: A = [4, 2, 2, 6, 4], B = 6, Output: 4</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Use a Hash Map to store the frequency of prefix XORs. For each element, current XOR `xr ^= A[i]`. We need `xr ^ B`. If it exists in map, add its frequency to count.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def solve(A: List[int], B: int) -&gt; int:&#10;    mpp = {0: 1}&#10;    xr = count = 0&#10;    for num in A:&#10;        xr ^= num&#10;        x = xr ^ B&#10;        if x in mpp: count += mpp[x]&#10;        mpp[xr] = mpp.get(xr, 0) + 1&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td>25</td>
      <td>Arr 25 Find The Duplicate Number<br><br></b> <a href="https://leetcode.com/problems/find-the-duplicate-number/" target="_blank">LeetCode 287</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, SDE Sheet, Striver A Z</details></td>
      <td>**Example 1:** Input: nums = [1,3,4,2,2], Output: 2</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Floyd's Tortoise and Hare (Cycle Detection). Fast and slow pointer. Guaranteed cycle because of Pigeonhole Principle (numbers map to index ranges).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findDuplicate(nums: List[int]) -&gt; int:&#10;    slow, fast = nums[0], nums[0]&#10;    while True:&#10;        slow = nums[slow]&#10;        fast = nums[nums[fast]]&#10;        if slow == fast: break&#10;    fast = nums[0]&#10;    while slow != fast:&#10;        slow = nums[slow]&#10;        fast = nums[fast]&#10;    return slow</code></pre></details></td>
    </tr>
    <tr>
      <td>26</td>
      <td>Arr 26 Find Missing And Repeating<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/find-missing-and-repeating2512/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> SDE Sheet, Love Babbar, Striver A Z</details></td>
      <td>**Example 1:** Input: N = 2, Arr[] = {2, 2}, Output: 2 1</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Mathematical approach. Diff = Sum_N - Sum_Arr = Missing - Repeating. SumSqDiff = SumSq_N - SumSq_Arr = Missing^2 - Repeating^2. Use formulas to solve for both.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findTwoElement(arr: List[int], n: int) -&gt; List[int]:&#10;    S_N = (n * (n+1)) // 2&#10;    Sq_N = (n * (n+1) * (2*n+1)) // 6&#10;    S, Sq = 0, 0&#10;    for num in arr:&#10;        S += num; Sq += num * num&#10;    val1 = S_N - S # X - Y&#10;    val2 = (Sq_N - Sq) // val1 # X + Y&#10;    x = (val1 + val2) // 2&#10;    y = x - val1&#10;    return [y, x] # Repeating, Missing</code></pre></details></td>
    </tr>
    <tr>
      <td>27</td>
      <td>Arr 27 Merge Two Sorted Arrays Without Extra Space<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> SDE Sheet, Love Babbar, Striver A Z</details></td>
      <td>**Example 1:** arr1=[1,3,5,7], arr2=[0,2,6,8,9], Output: arr1=[0,1,2,3], arr2=[5,6,7,8,9]</td>
      <td><b>Time:</b> O((N+M) log(N+M))<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Start pointers at end of arr1 (i) and beginning of arr2 (j). Swap if arr1[i] > arr2[j]. Afterwards, individually sort arr1 and arr2. Time is bounded by sorting.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def merge(arr1: List[int], arr2: List[int], n: int, m: int) -&gt; None:&#10;    left, right = n - 1, 0&#10;    while left &gt;= 0 and right &lt; m:&#10;        if arr1[left] &gt; arr2[right]:&#10;            arr1[left], arr2[right] = arr2[right], arr1[left]&#10;            left -= 1; right += 1&#10;        else: break&#10;    arr1.sort(); arr2.sort()</code></pre></details></td>
    </tr>
    <tr>
      <td>28</td>
      <td>Arr 28 Maximum Product Subarray<br><br></b> <a href="https://leetcode.com/problems/maximum-product-subarray/" target="_blank">LeetCode 152</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> SDE Sheet, Love Babbar, Striver A Z</details></td>
      <td>**Example 1:** Input: nums = [2,3,-2,4], Output: 6</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Maintain prefix and suffix products. If a 0 is encountered, reset the product to 1. The max overall is the answer since negatives cancel out in pairs.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxProduct(nums: List[int]) -&gt; int:&#10;    pref, suff, ans = 1, 1, float(&#x27;-inf&#x27;)&#10;    n = len(nums)&#10;    for i in range(n):&#10;        if pref == 0: pref = 1&#10;        if suff == 0: suff = 1&#10;        pref *= nums[i]&#10;        suff *= nums[n-1-i]&#10;        ans = max(ans, pref, suff)&#10;    return int(ans)</code></pre></details></td>
    </tr>
    <tr>
      <td>29</td>
      <td>Arr 29 Count Inversions<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/inversion-of-array-1587115620/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, SDE Sheet, Striver A Z</details></td>
      <td>**Example 1:** Input: N = 5, arr[] = {2, 4, 1, 3, 5}, Output: 3</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(N) auxiliary</td>
      <td><b>Explanation:</b> Merge Sort approach. While merging two sorted halves, if left[i] > right[j], it forms an inversion with all remaining elements in the left half (mid - i + 1).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def inversionCount(arr: List[int], n: int) -&gt; int:&#10;    def merge(low, mid, high):&#10;        temp, left, right, cnt = [], low, mid + 1, 0&#10;        while left &lt;= mid and right &lt;= high:&#10;            if arr[left] &lt;= arr[right]:&#10;                temp.append(arr[left]); left += 1&#10;            else:&#10;                temp.append(arr[right]); cnt += (mid - left + 1); right += 1&#10;        while left &lt;= mid: temp.append(arr[left]); left += 1&#10;        while right &lt;= high: temp.append(arr[right]); right += 1&#10;        for i in range(low, high + 1): arr[i] = temp[i - low]&#10;        return cnt&#10;    def mergeSort(low, high):&#10;        cnt = 0&#10;        if low &gt;= high: return cnt&#10;        mid = (low + high) // 2&#10;        cnt += mergeSort(low, mid)&#10;        cnt += mergeSort(mid + 1, high)&#10;        cnt += merge(low, mid, high)&#10;        return cnt&#10;    return mergeSort(0, n - 1)</code></pre></details></td>
    </tr>
    <tr>
      <td>30</td>
      <td>Arr 30 Reverse Pairs<br><br></b> <a href="https://leetcode.com/problems/reverse-pairs/" target="_blank">LeetCode 493</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> SDE Sheet, Love Babbar, Striver A Z</details></td>
      <td>**Example 1:** Input: nums = [1,3,2,3,1], Output: 2</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Modified Merge Sort. Before merging, loop through left and right halves. If left[i] > 2 * right[j], increment j. Number of pairs is (j - (mid+1)).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def reversePairs(nums: List[int]) -&gt; int:&#10;    def merge(low, mid, high):&#10;        temp, left, right = [], low, mid + 1&#10;        while left &lt;= mid and right &lt;= high:&#10;            if nums[left] &lt;= nums[right]:&#10;                temp.append(nums[left]); left += 1&#10;            else: temp.append(nums[right]); right += 1&#10;        while left &lt;= mid: temp.append(nums[left]); left += 1&#10;        while right &lt;= high: temp.append(nums[right]); right += 1&#10;        for i in range(low, high + 1): nums[i] = temp[i - low]&#10;    def countPairs(low, mid, high):&#10;        right, cnt = mid + 1, 0&#10;        for i in range(low, mid + 1):&#10;            while right &lt;= high and nums[i] &gt; 2 * nums[right]: right += 1&#10;            cnt += (right - (mid + 1))&#10;        return cnt&#10;    def mergeSort(low, high):&#10;        cnt = 0&#10;        if low &gt;= high: return cnt&#10;        mid = (low + high) // 2&#10;        cnt += mergeSort(low, mid)&#10;        cnt += mergeSort(mid + 1, high)&#10;        cnt += countPairs(low, mid, high)&#10;        merge(low, mid, high)&#10;        return cnt&#10;    return mergeSort(0, len(nums) - 1)</code></pre></details></td>
    </tr>
    <tr>
      <td>31</td>
      <td>Arr 31 Grid Unique Paths<br><br></b> <a href="https://leetcode.com/problems/unique-paths/" target="_blank">LeetCode 62</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td>**Example 1:** Input: m = 3, n = 7, Output: 28</td>
      <td><b>Time:</b> O(m-1)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Combinatorics approach. The total number of steps to reach the bottom-right corner is (m - 1) + (n - 1) = m + n - 2. Out of these steps, we need to choose (m - 1) downward steps (or n - 1 rightward steps). The number of paths is (m + n - 2) C (m - 1).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def uniquePaths(m: int, n: int) -&gt; int:&#10;    N = n + m - 2&#10;    r = m - 1&#10;    res = 1&#10;    for i in range(1, r + 1):&#10;        res = res * (N - r + i) // i&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td>32</td>
      <td>Arr 32 Search A 2D Matrix<br><br></b> <a href="https://leetcode.com/problems/search-a-2d-matrix/" target="_blank">LeetCode 74</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> SDE Sheet, Apna College, Love Babbar, Striver A Z</details></td>
      <td>**Example 1:** Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3, Output: true</td>
      <td><b>Time:</b> O(log(m * n))<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Treat the 2D matrix as a 1D array and apply binary search. The element at `mid` can be accessed using `matrix[mid / cols][mid % cols]`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def searchMatrix(matrix: List[List[int]], target: int) -&gt; bool:&#10;    if not matrix: return False&#10;    m, n = len(matrix), len(matrix[0])&#10;    low, high = 0, (m * n) - 1&#10;    while low &lt;= high:&#10;        mid = (low + high) // 2&#10;        if matrix[mid // n][mid % n] == target: return True&#10;        if matrix[mid // n][mid % n] &lt; target: low = mid + 1&#10;        else: high = mid - 1&#10;    return False</code></pre></details></td>
    </tr>
    <tr>
      <td>33</td>
      <td>Arr 33 Subarray With 0 Sum<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/subarray-with-0-sum-1587115621/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> SDE Sheet, Love Babbar, Striver A Z</details></td>
      <td>**Example 1:** Prefix Sum with HashSet.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Iterate through the array and calculate the prefix sum. If the prefix sum is 0 or it already exists in a hash set, it means a subarray with sum 0 exists.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def subArrayExists(arr, n):&#10;    sumSet = set()&#10;    curr_sum = 0&#10;    for num in arr:&#10;        curr_sum += num&#10;        if curr_sum == 0 or curr_sum in sumSet:&#10;            return True&#10;        sumSet.add(curr_sum)&#10;    return False</code></pre></details></td>
    </tr>
    <tr>
      <td>34</td>
      <td>Arr 34 Maximum Product Subarray<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/maximum-product-subarray3604/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> SDE Sheet, Love Babbar, Striver A Z</details></td>
      <td>**Example 1:** Prefix and Suffix iteration.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Iterate from left to right calculating prefix product, and right to left calculating suffix product. If either is 0, reset it to 1. The max product will be the max of all prefix and suffix products.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxProduct(arr, n):&#10;    max_prod = float(&#x27;-inf&#x27;)&#10;    pref, suff = 1, 1&#10;    for i in range(n):&#10;        if pref == 0: pref = 1&#10;        if suff == 0: suff = 1&#10;        pref *= arr[i]&#10;        suff *= arr[n - i - 1]&#10;        max_prod = max(max_prod, pref, suff)&#10;    return max_prod</code></pre></details></td>
    </tr>
    <tr>
      <td>35</td>
      <td>Arr 35 Longest Consecutive Subsequence<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/longest-consecutive-subsequence2449/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z, SDE Sheet</details></td>
      <td>**Example 1:** Hash Set.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Insert all elements into a hash set. For each element, check if `element - 1` exists. If not, it's the start of a sequence. Then increment to find consecutive elements.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findLongestConseqSubseq(arr, N):&#10;    s = set(arr)&#10;    longest = 0&#10;    for num in s:&#10;        if (num - 1) not in s:&#10;            curr = num&#10;            count = 1&#10;            while (curr + 1) in s:&#10;                curr += 1&#10;                count += 1&#10;            longest = max(longest, count)&#10;    return longest</code></pre></details></td>
    </tr>
    <tr>
      <td>36</td>
      <td>Arr 36 Fractional Knapsack<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td>**Example 1:** Sort by value/weight ratio.</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Sort items in descending order of value/weight ratio. Greedily pick items with the highest ratio first. If an item cannot fit completely, take the fraction that fits.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class Item:&#10;    def __init__(self,val,w):&#10;        self.value = val&#10;        self.weight = w&#10;&#10;def fractionalKnapsack(W, arr, n):&#10;    arr.sort(key=lambda x: x.value / x.weight, reverse=True)&#10;    finalValue = 0.0&#10;    for item in arr:&#10;        if W &gt;= item.weight:&#10;            finalValue += item.value&#10;            W -= item.weight&#10;        else:&#10;            finalValue += item.value * (W / item.weight)&#10;            break&#10;    return finalValue</code></pre></details></td>
    </tr>
    <tr>
      <td>37</td>
      <td>Arr 37 Minimum Platforms<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z, SDE Sheet</details></td>
      <td>**Example 1:** Sort arrival and departure times separately.</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Sort arrival and departure arrays separately. Use two pointers, one for arrival and one for departure. If arrival < departure, a platform is needed, so increment count. If arrival >= departure, a platform is freed, so decrement count. Track the maximum count.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findPlatform(arr, dep, n):&#10;    arr.sort()&#10;    dep.sort()&#10;    plat_needed, result = 1, 1&#10;    i, j = 1, 0&#10;    while i &lt; n and j &lt; n:&#10;        if arr[i] &lt;= dep[j]:&#10;            plat_needed += 1&#10;            i += 1&#10;        else:&#10;            plat_needed -= 1&#10;            j += 1&#10;        result = max(result, plat_needed)&#10;    return result</code></pre></details></td>
    </tr>
    <tr>
      <td>38</td>
      <td>Arr 38 Trapping Rain Water<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/trapping-rain-water-1587115621/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z, SDE Sheet</details></td>
      <td>**Example 1:** Two Pointers.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Use two pointers, left and right. Maintain left_max and right_max. If `arr[left] <= arr[right]`, the water trapped depends on left_max. If `arr[left] > left_max`, update left_max, else add `left_max - arr[left]` to answer and increment left. Repeat for right.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def trappingWater(arr, n):&#10;    left, right = 0, n - 1&#10;    left_max, right_max = 0, 0&#10;    res = 0&#10;    while left &lt;= right:&#10;        if arr[left] &lt;= arr[right]:&#10;            if arr[left] &gt;= left_max: left_max = arr[left]&#10;            else: res += left_max - arr[left]&#10;            left += 1&#10;        else:&#10;            if arr[right] &gt;= right_max: right_max = arr[right]&#10;            else: res += right_max - arr[right]&#10;            right -= 1&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td>39</td>
      <td>Arr 39 Median Of Two Sorted Arrays Of Different Sizes<br><br></b> <a href="https://leetcode.com/problems/median-of-two-sorted-arrays/" target="_blank">LeetCode 4</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> SDE Sheet, Love Babbar, Striver A Z</details></td>
      <td>**Example 1:** Binary Search.</td>
      <td><b>Time:</b> O(log(min(N, M)))<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Use Binary Search on the smaller array. Partition both arrays such that the number of elements on the left side is equal to or one more than the right side. Check if `maxLeftX <= minRightY` and `maxLeftY <= minRightX`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findMedianSortedArrays(nums1, nums2):&#10;    if len(nums1) &gt; len(nums2): return findMedianSortedArrays(nums2, nums1)&#10;    x, y = len(nums1), len(nums2)&#10;    low, high = 0, x&#10;    while low &lt;= high:&#10;        partitionX = (low + high) // 2&#10;        partitionY = (x + y + 1) // 2 - partitionX&#10;        maxLeftX = float(&#x27;-inf&#x27;) if partitionX == 0 else nums1[partitionX - 1]&#10;        minRightX = float(&#x27;inf&#x27;) if partitionX == x else nums1[partitionX]&#10;        maxLeftY = float(&#x27;-inf&#x27;) if partitionY == 0 else nums2[partitionY - 1]&#10;        minRightY = float(&#x27;inf&#x27;) if partitionY == y else nums2[partitionY]&#10;        if maxLeftX &lt;= minRightY and maxLeftY &lt;= minRightX:&#10;            if (x + y) % 2 == 0:&#10;                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0&#10;            else:&#10;                return max(maxLeftX, maxLeftY)&#10;        elif maxLeftX &gt; minRightY:&#10;            high = partitionX - 1&#10;        else:&#10;            low = partitionX + 1&#10;    return 0.0</code></pre></details></td>
    </tr>
    <tr>
      <td>40</td>
      <td>Arr 40 Count More Than N K Occurences<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/count-element-occurences/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td>**Example 1:** HashMap.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Store the frequencies of all elements in a hash map. Iterate through the hash map and count the number of elements having frequency greater than `N/k`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def countOccurence(arr, n, k):&#10;    count = collections.Counter(arr)&#10;    res = 0&#10;    target = n // k&#10;    for key, val in count.items():&#10;        if val &gt; target:&#10;            res += 1&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td>41</td>
      <td>Arr 41 Find The Missing Number<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/missing-number-in-array1416/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td>**Example 1:** Sum formula.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Calculate the sum of first N natural numbers using `N*(N+1)/2`. Subtract the sum of all elements in the array from it. The result is the missing number.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def missingNumber(array, n):&#10;    return n * (n + 1) // 2 - sum(array)</code></pre></details></td>
    </tr>
    <tr>
      <td>42</td>
      <td>Arr 42 Max Sum In Sub Arrays<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/max-sum-in-sub-arrays0824/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z</details></td>
      <td>**Example 1:** Adjacent pairs sum.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> The maximum sum of two smallest elements in any subarray will always be the maximum sum of adjacent elements. So, just iterate and find the max of `arr[i] + arr[i+1]`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def pairWithMaxSum(arr, N):&#10;    maxi = 0&#10;    for i in range(N - 1):&#10;        maxi = max(maxi, arr[i] + arr[i+1])&#10;    return maxi</code></pre></details></td>
    </tr>
    <tr>
      <td>43</td>
      <td>Arr 43 Longest Subarray With Sum K Positives<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td>**Example 1:** Sliding Window / Two Pointers.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Since all elements are positive, use two pointers (sliding window). Expand `right` and add to sum. If sum > K, shrink `left` and subtract from sum. If sum == K, update max length.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def lenOfLongSubarr(A, N, K):&#10;    left, sum_val, max_len = 0, 0, 0&#10;    for right in range(N):&#10;        sum_val += A[right]&#10;        while sum_val &gt; K and left &lt;= right:&#10;            sum_val -= A[left]&#10;            left += 1&#10;        if sum_val == K:&#10;            max_len = max(max_len, right - left + 1)&#10;    return max_len</code></pre></details></td>
    </tr>
    <tr>
      <td>44</td>
      <td>Arr 44 Merge Sorted Array Without Extra Space<br><br></b> <a href="https://leetcode.com/problems/merge-sorted-array/" target="_blank">LeetCode 88</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z, SDE Sheet</details></td>
      <td>**Example 1:** Two pointers from end.</td>
      <td><b>Time:</b> O(M + N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Since `nums1` has enough space at the end, use three pointers: `p1` at the end of valid elements in `nums1` (m-1), `p2` at the end of `nums2` (n-1), and `p` at the very end of `nums1` (m+n-1). Compare elements at `p1` and `p2`, put the larger one at `p`, and decrement pointers.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def merge(nums1, m, nums2, n):&#10;    p1, p2, p = m - 1, n - 1, m + n - 1&#10;    while p1 &gt;= 0 and p2 &gt;= 0:&#10;        if nums1[p1] &gt; nums2[p2]:&#10;            nums1[p] = nums1[p1]&#10;            p1 -= 1&#10;        else:&#10;            nums1[p] = nums2[p2]&#10;            p2 -= 1&#10;        p -= 1&#10;    while p2 &gt;= 0:&#10;        nums1[p] = nums2[p2]&#10;        p -= 1&#10;        p2 -= 1</code></pre></details></td>
    </tr>
  </tbody>
</table>
