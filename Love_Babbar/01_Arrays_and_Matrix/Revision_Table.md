# 01 Arrays and Matrix Revision Table

<table border="1">
  <thead>
    <tr>
      <th style="width: 5%;">S.No</th>
      <th style="width: 15%;">Problem Name</th>
      <th style="width: 20%;">Example & Constraints</th>
      <th style="width: 10%;">Complexity</th>
      <th style="width: 20%;">Approach & Dependencies</th>
      <th style="width: 30%;">Logic & Edge Cases</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">1</td>
      <td rowspan="2">Math 01 Pow X N<br><br></b> <a href="https://leetcode.com/problems/powx-n/" target="_blank">LeetCode 50</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, SDE Sheet, Love Babbar</details></td>
      <td rowspan="2"><b>Example 1:</b> Binary Exponentiation.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Approach 1:</b><br>Brute Force: Loop n times and multiply ans by x.</td>
      <td><b>Edge Cases:</b> TLE for large N.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def myPow(x: float, n: int) -&gt; float:&#10;    ans = 1.0&#10;    nn = abs(n)&#10;    for _ in range(nn):&#10;        ans *= x&#10;    return 1.0 / ans if n &lt; 0 else ans</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(log N)<br><b>Space:</b> O(1)</td>
      <td><b>Approach 2:</b><br>Optimal: Binary Exponentiation. If n is even, x = x*x, n = n/2. If odd, ans = ans*x, n = n-1.</td>
      <td><b>Edge Cases:</b> Negative power, n = INT_MIN<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def myPow(x, n):&#10;    ans, nn = 1.0, abs(n)&#10;    while nn &gt; 0:&#10;        if nn % 2 == 1:&#10;            ans *= x&#10;            nn -= 1&#10;        else:&#10;            x *= x&#10;            nn //= 2&#10;    return ans if n &gt;= 0 else 1.0 / ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">2</td>
      <td rowspan="2">Arr 02 Largest Element<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/largest-element-in-array/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td rowspan="2"><b> </b> <br><b>Input:</b> A = [1, 8, 7, 56, 90]<br><b>Output:</b> 90</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(1) or O(N) depending on sort</td>
      <td><b>Approach 1:</b><br>Brute Force: Sort the array and return the last element.<br><br><b>Dependencies:</b> std::sort</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def largest(arr: list[int]) -&gt; int:&#10;    arr.sort()&#10;    return arr[-1]</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><b>Approach 2:</b><br>Optimal: Iterate through the array maintaining a variable for the maximum element seen so far.</td>
      <td><b>Edge Cases:</b> <b>Initialization:</b> Initialize `max_val` with the first element or negative infinity.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def largest(arr: list[int]) -&gt; int:&#10;    max_val = arr[0]&#10;    for num in arr:&#10;        if num &gt; max_val:&#10;            max_val = num&#10;    return max_val</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">3</td>
      <td rowspan="2">Arr 03 Second Largest Element<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/second-largest3735/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td rowspan="2"><b> </b> <br><b>Input:</b> arr = [12, 35, 1, 10, 34, 1]<br><b>Output:</b> 34<br><br><b> </b> Find it in a single pass O(N) time.</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(1)</td>
      <td><b>Approach 1:</b><br>Brute Force: Sort the array, then iterate from the back to find the first element smaller than the largest.<br><br><b>Dependencies:</b> std::sort</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print2largest(arr, n):&#10;    arr.sort()&#10;    for i in range(n-2, -1, -1):&#10;        if arr[i] != arr[n-1]: return arr[i]&#10;    return -1</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><b>Approach 2:</b><br>Optimal: Maintain two variables, `largest` and `second_largest`. Update them simultaneously during a single pass.</td>
      <td><b>Edge Cases:</b> <b>No Second Largest:</b> If all elements are same or array size < 2, return -1.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print2largest(arr: list[int]) -&gt; int:&#10;    largest = -1&#10;    second_largest = -1&#10;    for num in arr:&#10;        if num &gt; largest:&#10;            second_largest = largest&#10;            largest = num&#10;        elif num &gt; second_largest and num != largest:&#10;            second_largest = num&#10;    return second_largest</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">4</td>
      <td rowspan="1">Arr 04 Check If Array Is Sorted And Rotated<br><br></b> <a href="https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/" target="_blank">LeetCode 1752</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> nums = [3,4,5,1,2]<br><b>Output:</b> true</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td>Optimal: Count the number of "breaks" where `nums[i] > nums[i+1]`. For a sorted and rotated array, there can be at most 1 break.</td>
      <td><b>Edge Cases:</b> <b>Circular Check:</b> We must also check the boundary between the last and first element `nums[n-1] > nums[0]`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def check(nums: list[int]) -&gt; bool:&#10;    count = 0&#10;    n = len(nums)&#10;    for i in range(n):&#10;        if nums[i] &gt; nums[(i + 1) % n]:&#10;            count += 1&#10;    return count &lt;= 1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">5</td>
      <td rowspan="2">Arr 05 Remove Duplicates From Sorted Array<br><br></b> <a href="https://leetcode.com/problems/remove-duplicates-from-sorted-array/" target="_blank">LeetCode 26</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td rowspan="2"><b> </b> <br><b>Input:</b> nums = [1,1,2]<br><b>Output:</b> 2, nums = [1,2,_]</td>
      <td><b>Time:</b> O(N log N) or O(N)<br><b>Space:</b> O(N)</td>
      <td><b>Approach 1:</b><br>Brute Force: Use a HashSet to store unique elements, then put them back into the array.<br><br><b>Dependencies:</b> std::set</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def removeDuplicates(nums):&#10;    unique_nums = sorted(list(set(nums)))&#10;    for i in range(len(unique_nums)):&#10;        nums[i] = unique_nums[i]&#10;    return len(unique_nums)</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><b>Approach 2:</b><br>Optimal: Two-pointer approach. Pointer `i` keeps track of unique elements, pointer `j` scans the array to find new unique elements.</td>
      <td><b>Edge Cases:</b> <b>Empty Array:</b> Handled automatically if `n=0`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def removeDuplicates(nums: list[int]) -&gt; int:&#10;    if not nums: return 0&#10;    i = 0&#10;    for j in range(1, len(nums)):&#10;        if nums[j] != nums[i]:&#10;            i += 1&#10;            nums[i] = nums[j]&#10;    return i + 1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">6</td>
      <td rowspan="2">Arr 06 Rotate Array<br><br></b> <a href="https://leetcode.com/problems/rotate-array/" target="_blank">LeetCode 189</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td rowspan="2"><b> </b> <br><b>Input:</b> nums = [1,2,3,4,5,6,7], k = 3<br><b>Output:</b> [5,6,7,1,2,3,4]</td>
      <td><b>Time:</b> O(N * K) or O(N)<br><b>Space:</b> O(1) or O(N)</td>
      <td><b>Approach 1:</b><br>Brute Force: Rotate the array one by one, k times. Or use a temporary array of size N.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def rotate(nums, k):&#10;    n = len(nums)&#10;    k = k % n&#10;    temp = [0] * n&#10;    for i in range(n):&#10;        temp[(i+k)%n] = nums[i]&#10;    for i in range(n):&#10;        nums[i] = temp[i]</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><b>Approach 2:</b><br>Optimal: Reverse Algorithm. Reverse the whole array, then reverse the first `k` elements, then reverse the remaining `N-k` elements.<br><br><b>Dependencies:</b> <code>std::reverse</code></td>
      <td><b>Edge Cases:</b> <b>K > N:</b> k might be greater than array length, so perform `k = k % n` first.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def rotate(nums: list[int], k: int) -&gt; None:&#10;    n = len(nums)&#10;    k = k % n&#10;    nums.reverse()&#10;    nums[:k] = reversed(nums[:k])&#10;    nums[k:] = reversed(nums[k:])</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">7</td>
      <td rowspan="1">Arr 07 Move Zeroes<br><br></b> <a href="https://leetcode.com/problems/move-zeroes/" target="_blank">LeetCode 283</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> nums = [0,1,0,3,12]<br><b>Output:</b> [1,3,12,0,0]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Two-pointer approach (Snowball method). Pointer `i` tracks the first zero found, pointer `j` scans for non-zeroes to swap.<br><br><b>Dependencies:</b> <code>std::swap</code></td>
      <td><b>Edge Cases:</b> <b>No zeroes:</b> Swaps element with itself initially, no overhead.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def moveZeroes(nums: list[int]) -&gt; None:&#10;    i = 0&#10;    for j in range(len(nums)):&#10;        if nums[j] != 0:&#10;            nums[i], nums[j] = nums[j], nums[i]&#10;            i += 1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">8</td>
      <td rowspan="2">Arr 08 Missing Number<br><br></b> <a href="https://leetcode.com/problems/missing-number/" target="_blank">LeetCode 268</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td rowspan="2"><b> </b> <br><b>Input:</b> nums = [3,0,1]<br><b>Output:</b> 2</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(1)</td>
      <td><b>Approach 1:</b><br>Brute Force: Linear search for each number from 0 to N inside the array.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def missingNumber(nums):&#10;    for i in range(len(nums) + 1):&#10;        if i not in nums:&#10;            return i&#10;    return -1</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><b>Approach 2:</b><br>Optimal: Using XOR: XORing a number with itself results in 0. XOR all indices `[0,n]` and all elements in `nums`. The missing number will remain.</td>
      <td><b>Edge Cases:</b> <b>Mathematical Sum alternative:</b> Gaussian sum formula `N*(N+1)/2` can cause integer overflow, XOR completely bypasses overflow risks.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def missingNumber(nums: list[int]) -&gt; int:&#10;    res = len(nums)&#10;    for i, num in enumerate(nums):&#10;        res ^= i ^ num&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">9</td>
      <td rowspan="1">Arr 09 Max Consecutive Ones<br><br></b> <a href="https://leetcode.com/problems/max-consecutive-ones/" target="_blank">LeetCode 485</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> nums = [1,1,0,1,1,1]<br><b>Output:</b> 3</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Iterate while counting 1s. If a 0 is found, update max count and reset current count to 0.<br><br><b>Dependencies:</b> <code>std::max</code></td>
      <td><b>Edge Cases:</b> <b>Trailing Ones:</b> Must perform a final max check outside the loop or update max dynamically inside.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findMaxConsecutiveOnes(nums: list[int]) -&gt; int:&#10;    max_cnt = current_cnt = 0&#10;    for num in nums:&#10;        if num == 1:&#10;            current_cnt += 1&#10;            max_cnt = max(max_cnt, current_cnt)&#10;        else:&#10;            current_cnt = 0&#10;    return max_cnt</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">10</td>
      <td rowspan="2">Arr 10 Sort Colors Dnf<br><br></b> <a href="https://leetcode.com/problems/sort-colors/" target="_blank">LeetCode 75</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td rowspan="2"><b> </b> <br><b>Input:</b> nums = [2,0,2,1,1,0]<br><b>Output:</b> [0,0,1,1,2,2]<br><br><b> </b> Do not use library sort. Use single pass.</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(N)</td>
      <td><b>Approach 1:</b><br>Brute Force: Use any standard sorting algorithm like Merge Sort.<br><br><b>Dependencies:</b> std::sort</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def sortColors(nums):&#10;    nums.sort()</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><b>Approach 2:</b><br>Optimal: Dutch National Flag Algorithm (3 pointers). `low` tracks 0s, `mid` scans array, `high` tracks 2s. Swap elements to maintain sections.<br><br><b>Dependencies:</b> <code>std::swap</code></td>
      <td><b>Edge Cases:</b> <b>Mid pointer increment:</b> When swapping with `high`, we do NOT increment `mid` because the swapped element from `high` needs to be evaluated.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def sortColors(nums: list[int]) -&gt; None:&#10;    low, mid, high = 0, 0, len(nums) - 1&#10;    while mid &lt;= high:&#10;        if nums[mid] == 0:&#10;            nums[low], nums[mid] = nums[mid], nums[low]&#10;            low += 1; mid += 1&#10;        elif nums[mid] == 1:&#10;            mid += 1&#10;        else:&#10;            nums[mid], nums[high] = nums[high], nums[mid]&#10;            high -= 1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">11</td>
      <td rowspan="2">Arr 11 Majority Element<br><br></b> <a href="https://leetcode.com/problems/majority-element/" target="_blank">LeetCode 169</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td rowspan="2"><b> </b> <br><b>Input:</b> nums = [2,2,1,1,1,2,2]<br><b>Output:</b> 2</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(1)</td>
      <td><b>Approach 1:</b><br>Brute Force: Use two nested loops to count occurrences of each element.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def majorityElement(nums):&#10;    n = len(nums)&#10;    for num in nums:&#10;        if nums.count(num) &gt; n // 2:&#10;            return num&#10;    return -1</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1)</td>
      <td><b>Approach 2:</b><br>Optimal: Moore's Voting Algorithm. Track a candidate and a counter. Increment if same as candidate, decrement if different. If zero, pick new candidate.</td>
      <td><b>Edge Cases:</b> <b>Verification phase:</b> If it's not guaranteed a majority exists, a second `O(N)` pass is required to count the candidate. (Leetcode guarantees it exists).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def majorityElement(nums: list[int]) -&gt; int:&#10;    count = candidate = 0&#10;    for num in nums:&#10;        if count == 0:&#10;            candidate = num&#10;        count += (1 if num == candidate else -1)&#10;    return candidate</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">12</td>
      <td rowspan="2">Arr 12 Kadanes Algorithm Max Subarray Sum<br><br></b> <a href="https://leetcode.com/problems/maximum-subarray/" target="_blank">LeetCode 53</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td rowspan="2"><b> </b> <br><b>Input:</b> nums = [-2,1,-3,4,-1,2,1,-5,4]<br><b>Output:</b> 6 (Subarray [4,-1,2,1])</td>
      <td><b>Time:</b> O(N^3)<br><b>Space:</b> O(1)</td>
      <td><b>Approach 1:</b><br>Brute Force: Generate all possible subarrays using three nested loops and find the maximum sum.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxSubArray(nums):&#10;    maxi = float(&#x27;-inf&#x27;)&#10;    n = len(nums)&#10;    for i in range(n):&#10;        for j in range(i, n):&#10;            current_sum = sum(nums[i:j+1])&#10;            maxi = max(maxi, current_sum)&#10;    return maxi</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><b>Approach 2:</b><br>Optimal: Kadane's Algorithm. Keep a running sum. If sum becomes negative, reset it to 0 (a negative prefix will never help a future subarray).<br><br><b>Dependencies:</b> <code>std::max</code></td>
      <td><b>Edge Cases:</b> <b>All Negative Numbers:</b> Initialize `max_sum` with `INT_MIN` or `nums[0]` so it can correctly return the smallest negative number instead of 0.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxSubArray(nums: list[int]) -&gt; int:&#10;    max_sum = float(&#x27;-inf&#x27;)&#10;    current_sum = 0&#10;    for num in nums:&#10;        current_sum += num&#10;        if current_sum &gt; max_sum:&#10;            max_sum = current_sum&#10;        if current_sum &lt; 0:&#10;            current_sum = 0&#10;    return int(max_sum)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">13</td>
      <td rowspan="1">Arr 13 Best Time To Buy And Sell Stock<br><br></b> <a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock/" target="_blank">LeetCode 121</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z, SDE Sheet</details></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> prices = [7,1,5,3,6,4]<br><b>Output:</b> 5</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Iterate while keeping track of the minimum price seen so far. Subtract this min from the current price to find potential profit.<br><br><b>Dependencies:</b> <code>std::max</code>, <code>std::min</code></td>
      <td><b>Edge Cases:</b> <b>No Profit Possible:</b> `max_profit` initializes at 0. If price strictly decreases, it never updates and naturally returns 0.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxProfit(prices: list[int]) -&gt; int:&#10;    min_price = prices[0]&#10;    max_profit = 0&#10;    for i in range(1, len(prices)):&#10;        max_profit = max(max_profit, prices[i] - min_price)&#10;        min_price = min(min_price, prices[i])&#10;    return max_profit</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">14</td>
      <td rowspan="1">Arr 14 Rearrange Array Elements By Sign<br><br></b> <a href="https://leetcode.com/problems/rearrange-array-elements-by-sign/" target="_blank">LeetCode 2149</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> nums = [3,1,-2,-5,2,-4]<br><b>Output:</b> [3,-2,1,-5,2,-4]<br><br><b> </b> Maintain relative order.</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(N) (Constraint)</td>
      <td>Optimal: Use two pointers, `pos_idx` starting at 0, `neg_idx` starting at 1. Traverse and place elements directly into a new result array.</td>
      <td><b>Edge Cases:</b> <b>In-Place Attempt:</b> Doing this in-place `O(1)` space while maintaining relative order drops Time to `O(N^2)`. The optimal tradeoff is `O(N)` space.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def rearrangeArray(nums: list[int]) -&gt; list[int]:&#10;    ans = [0] * len(nums)&#10;    pos_idx, neg_idx = 0, 1&#10;    for num in nums:&#10;        if num &gt; 0:&#10;            ans[pos_idx] = num&#10;            pos_idx += 2&#10;        else:&#10;            ans[neg_idx] = num&#10;            neg_idx += 2&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">15</td>
      <td rowspan="1">Arr 15 Next Permutation<br><br></b> <a href="https://leetcode.com/problems/next-permutation/" target="_blank">LeetCode 31</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z, SDE Sheet</details></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> nums = [1,2,3]<br><b>Output:</b> [1,3,2]<br><b> </b> <br><b>Input:</b> nums = [3,2,1]<br><b>Output:</b> [1,2,3]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: 1. Find break point (i) where arr[i] < arr[i+1]. 2. Swap it with smallest element > arr[i] from the back. 3. Reverse the right half.<br><br><b>Dependencies:</b> <code>std::reverse</code></td>
      <td><b>Edge Cases:</b> <b>Last Permutation:</b> If break point is not found (`i < 0`), it means the array is sorted descending. Just reverse the entire array to get the lowest permutation.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def nextPermutation(nums: list[int]) -&gt; None:&#10;    n = len(nums)&#10;    i = n - 2&#10;    while i &gt;= 0 and nums[i] &gt;= nums[i + 1]:&#10;        i -= 1&#10;        &#10;    if i &gt;= 0:&#10;        j = n - 1&#10;        while nums[j] &lt;= nums[i]:&#10;            j -= 1&#10;        nums[i], nums[j] = nums[j], nums[i]&#10;        &#10;    nums[i+1:] = reversed(nums[i+1:])</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">16</td>
      <td rowspan="1">Arr 16 Pascals Triangle<br><br></b> <a href="https://leetcode.com/problems/pascals-triangle/" target="_blank">LeetCode 118</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> numRows = 5<br><b>Output:</b> [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]</td>
      <td><b>Time:</b> O(N<sup>2</sup>) (Constraint)<br><b>Space:</b> O(N<sup>2</sup>) (Constraint)</td>
      <td>Optimal: Generate row by row. Each element `val[i][j]` is the sum of `val[i-1][j-1]` and `val[i-1][j]`.</td>
      <td><b>Edge Cases:</b> <b>Boundary 1s:</b> First and last elements of every row are always 1. Pre-filling row with 1s avoids out-of-bounds checks.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def generate(numRows: int) -&gt; list[list[int]]:&#10;    ans = []&#10;    for i in range(numRows):&#10;        row = [1] * (i + 1)&#10;        for j in range(1, i):&#10;            row[j] = ans[i-1][j-1] + ans[i-1][j]&#10;        ans.append(row)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">17</td>
      <td rowspan="1">Arr 17 Majority Element II<br><br></b> <a href="https://leetcode.com/problems/majority-element-ii/" target="_blank">LeetCode 229</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z, SDE Sheet</details></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> nums = [3,2,3]<br><b>Output:</b> [3]<br><br><b> </b> Time O(N), Space O(1).</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td>Optimal: Extended Moore's Voting Algorithm. At most TWO elements can appear > N/3 times. Track two candidates and two counters.</td>
      <td><b>Edge Cases:</b> <b>Verification phase required:</b> We MUST perform a second pass to count occurrences of `candidate1` and `candidate2` because it's not guaranteed they appear > N/3 times.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def majorityElement(nums: list[int]) -&gt; list[int]:&#10;    cnt1, cnt2, el1, el2 = 0, 0, float(&#x27;-inf&#x27;), float(&#x27;-inf&#x27;)&#10;    for num in nums:&#10;        if cnt1 == 0 and num != el2:&#10;            cnt1 = 1; el1 = num&#10;        elif cnt2 == 0 and num != el1:&#10;            cnt2 = 1; el2 = num&#10;        elif num == el1:&#10;            cnt1 += 1&#10;        elif num == el2:&#10;            cnt2 += 1&#10;        else:&#10;            cnt1 -= 1; cnt2 -= 1&#10;            &#10;    ans = []&#10;    if nums.count(el1) &gt; len(nums) // 3:&#10;        ans.append(el1)&#10;    if nums.count(el2) &gt; len(nums) // 3:&#10;        ans.append(el2)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">18</td>
      <td rowspan="1">Arr 18 3Sum<br><br></b> <a href="https://leetcode.com/problems/3sum/" target="_blank">LeetCode 15</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z, SDE Sheet</details></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> nums = [-1,0,1,2,-1,-4]<br><b>Output:</b> [[-1,-1,2],[-1,0,1]]<br><br><b> </b> Solution set must not contain duplicate triplets.</td>
      <td><b>Time:</b> O(N<sup>2</sup>) (Constraint)<br><b>Space:</b> O(1) (Trade-off)</td>
      <td>Optimal: Sort the array. Use a loop to fix `i`, then use a Two-Pointer approach (`j`, `k`) for the remaining array to find sum `0 - nums[i]`.<br><br><b>Dependencies:</b> <code>std::sort</code></td>
      <td><b>Edge Cases:</b> <b>Duplicate skipping:</b> To prevent duplicate triplets, skip identical adjacent elements for `i`, `j`, and `k`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def threeSum(nums: list[int]) -&gt; list[list[int]]:&#10;    ans = []&#10;    nums.sort()&#10;    n = len(nums)&#10;    for i in range(n):&#10;        if i &gt; 0 and nums[i] == nums[i-1]: continue&#10;        j, k = i + 1, n - 1&#10;        while j &lt; k:&#10;            s = nums[i] + nums[j] + nums[k]&#10;            if s &lt; 0:&#10;                j += 1&#10;            elif s &gt; 0:&#10;                k -= 1&#10;            else:&#10;                ans.append([nums[i], nums[j], nums[k]])&#10;                j += 1; k -= 1&#10;                while j &lt; k and nums[j] == nums[j-1]: j += 1&#10;                while j &lt; k and nums[k] == nums[k+1]: k -= 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">19</td>
      <td rowspan="1">Arr 19 Merge Intervals<br><br></b> <a href="https://leetcode.com/problems/merge-intervals/" target="_blank">LeetCode 56</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, SDE Sheet, Love Babbar</details></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> intervals = [[1,3],[2,6],[8,10],[15,18]]<br><b>Output:</b> [[1,6],[8,10],[15,18]]</td>
      <td><b>Time:</b> O(N log N) (Constraint)<br><b>Space:</b> O(N)</td>
      <td>Optimal: Sort the intervals based on the start time. Iterate and merge: if current start <= previous end, update previous end to `max(prev_end, curr_end)`.<br><br><b>Dependencies:</b> <code>std::sort</code></td>
      <td><b>Edge Cases:</b> <b>Subsumed Intervals:</b> `[1,4]` and `[2,3]` -> using `max()` prevents shrinking the end time to `3`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def merge(intervals: list[list[int]]) -&gt; list[list[int]]:&#10;    if not intervals: return []&#10;    intervals.sort(key=lambda x: x[0])&#10;    merged = [intervals[0]]&#10;    for i in range(1, len(intervals)):&#10;        if intervals[i][0] &lt;= merged[-1][1]:&#10;            merged[-1][1] = max(merged[-1][1], intervals[i][1])&#10;        else:&#10;            merged.append(intervals[i])&#10;    return merged</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">20</td>
      <td rowspan="1">Arr 20 Leaders In An Array<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> A = [16,17,4,3,5,2]<br><b>Output:</b> [17,5,2]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N) for output</td>
      <td>Optimal: Traverse the array from right to left. Keep track of the maximum element seen so far. If the current element is greater than or equal to the max, it's a leader. Reverse the collected leaders at the end.<br><br><b>Dependencies:</b> <code>#include <algorithm></code></td>
      <td><b>Edge Cases:</b> <b>Rightmost element:</b> Always a leader.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def leaders(A: List[int], N: int) -&gt; List[int]:&#10;    ans = []&#10;    maxi = A[N - 1]&#10;    ans.append(maxi)&#10;    for i in range(N - 2, -1, -1):&#10;        if A[i] &gt;= maxi:&#10;            ans.append(A[i])&#10;            maxi = A[i]&#10;    ans.reverse()&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">21</td>
      <td rowspan="1">Arr 21 Set Matrix Zeroes<br><br></b> <a href="https://leetcode.com/problems/set-matrix-zeroes/" target="_blank">LeetCode 73</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> matrix = [[1,1,1],[1,0,1],[1,1,1]]<br><b>Output:</b> [[1,0,1],[0,0,0],[1,0,1]]</td>
      <td><b>Time:</b> O(N * M)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Use the first row and first column as marker arrays to save space. We need a separate variable for the first column (or row) to avoid overlapping states.</td>
      <td><b>Edge Cases:</b> <b>Zeros in first row/col:</b> Handled accurately by checking `col0` flag at the end.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def setZeroes(matrix: List[List[int]]) -&gt; None:&#10;    n, m, col0 = len(matrix), len(matrix[0]), 1&#10;    for i in range(n):&#10;        if matrix[i][0] == 0: col0 = 0&#10;        for j in range(1, m):&#10;            if matrix[i][j] == 0: matrix[i][0] = matrix[0][j] = 0&#10;    for i in range(n-1, -1, -1):&#10;        for j in range(m-1, 0, -1):&#10;            if matrix[i][0] == 0 or matrix[0][j] == 0: matrix[i][j] = 0&#10;        if col0 == 0: matrix[i][0] = 0</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">22</td>
      <td rowspan="1">Arr 22 Rotate Image<br><br></b> <a href="https://leetcode.com/problems/rotate-image/" target="_blank">LeetCode 48</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> matrix = [[1,2,3],[4,5,6],[7,8,9]]<br><b>Output:</b> [[7,4,1],[8,5,2],[9,6,3]]</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Transpose the matrix (swap matrix[i][j] with matrix[j][i]), then reverse every row.<br><br><b>Dependencies:</b> <code>#include <algorithm></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def rotate(matrix: List[List[int]]) -&gt; None:&#10;    n = len(matrix)&#10;    for i in range(n):&#10;        for j in range(i):&#10;            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]&#10;    for i in range(n):&#10;        matrix[i].reverse()</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">23</td>
      <td rowspan="1">Arr 23 Spiral Matrix<br><br></b> <a href="https://leetcode.com/problems/spiral-matrix/" target="_blank">LeetCode 54</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> matrix = [[1,2,3],[4,5,6],[7,8,9]]<br><b>Output:</b> [1,2,3,6,9,8,7,4,5]</td>
      <td><b>Time:</b> O(N * M)<br><b>Space:</b> O(N * M) for output</td>
      <td>Optimal: Maintain 4 pointers: top, bottom, left, right. Traverse Top row, Right col, Bottom row, Left col, shrinking boundaries inwards.</td>
      <td><b>Edge Cases:</b> <b>Single row/col matrix:</b> Internal boundary checks prevent duplicate counting.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def spiralOrder(matrix: List[List[int]]) -&gt; List[int]:&#10;    ans = []&#10;    top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1&#10;    while top &lt;= bottom and left &lt;= right:&#10;        for i in range(left, right+1): ans.append(matrix[top][i])&#10;        top += 1&#10;        for i in range(top, bottom+1): ans.append(matrix[i][right])&#10;        right -= 1&#10;        if top &lt;= bottom:&#10;            for i in range(right, left-1, -1): ans.append(matrix[bottom][i])&#10;            bottom -= 1&#10;        if left &lt;= right:&#10;            for i in range(bottom, top-1, -1): ans.append(matrix[i][left])&#10;            left += 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">24</td>
      <td rowspan="1">Arr 24 4Sum<br><br></b> <a href="https://leetcode.com/problems/4sum/" target="_blank">LeetCode 18</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, SDE Sheet, Love Babbar</details></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> nums = [1,0,-1,0,-2,2], target = 0<br><b>Output:</b> [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]</td>
      <td><b>Time:</b> O(N^3)<br><b>Space:</b> O(1) auxiliary</td>
      <td>Optimal: Sort array. Use 2 nested loops (i, j) for the first two numbers, and Two Pointers (k, l) for the remaining two. Skip duplicates carefully.<br><br><b>Dependencies:</b> <code>#include <algorithm></code></td>
      <td><b>Edge Cases:</b> <b>Integer Overflow:</b> Use `long long` when computing sum of 4 integers.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def fourSum(nums: List[int], target: int) -&gt; List[List[int]]:&#10;    ans = []&#10;    n = len(nums); nums.sort()&#10;    for i in range(n):&#10;        if i &gt; 0 and nums[i] == nums[i-1]: continue&#10;        for j in range(i+1, n):&#10;            if j &gt; i+1 and nums[j] == nums[j-1]: continue&#10;            k, l = j+1, n-1&#10;            while k &lt; l:&#10;                total = nums[i] + nums[j] + nums[k] + nums[l]&#10;                if total == target:&#10;                    ans.append([nums[i], nums[j], nums[k], nums[l]])&#10;                    k += 1; l -= 1&#10;                    while k &lt; l and nums[k] == nums[k-1]: k += 1&#10;                    while k &lt; l and nums[l] == nums[l+1]: l -= 1&#10;                elif total &lt; target: k += 1&#10;                else: l -= 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">25</td>
      <td rowspan="1">Arr 25 Count Subarrays With Given Xor K<br><br></b> <a href="https://www.interviewbit.com/problems/subarray-with-given-xor/" target="_blank">InterviewBit</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, SDE Sheet, Love Babbar</details></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> A = [4, 2, 2, 6, 4], B = 6<br><b>Output:</b> 4</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Optimal: Use a Hash Map to store the frequency of prefix XORs. For each element, current XOR `xr ^= A[i]`. We need `xr ^ B`. If it exists in map, add its frequency to count.<br><br><b>Dependencies:</b> <code>#include <unordered_map></code></td>
      <td><b>Edge Cases:</b> <b>XOR exactly equals B:</b> Insert `mpp[0] = 1` initially to cover subarrays starting from index 0.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def solve(A: List[int], B: int) -&gt; int:&#10;    mpp = {0: 1}&#10;    xr = count = 0&#10;    for num in A:&#10;        xr ^= num&#10;        x = xr ^ B&#10;        if x in mpp: count += mpp[x]&#10;        mpp[xr] = mpp.get(xr, 0) + 1&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">26</td>
      <td rowspan="1">Arr 26 Find The Duplicate Number<br><br></b> <a href="https://leetcode.com/problems/find-the-duplicate-number/" target="_blank">LeetCode 287</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z, SDE Sheet</details></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> nums = [1,3,4,2,2]<br><b>Output:</b> 2</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Floyd's Tortoise and Hare (Cycle Detection). Fast and slow pointer. Guaranteed cycle because of Pigeonhole Principle (numbers map to index ranges).</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findDuplicate(nums: List[int]) -&gt; int:&#10;    slow, fast = nums[0], nums[0]&#10;    while True:&#10;        slow = nums[slow]&#10;        fast = nums[nums[fast]]&#10;        if slow == fast: break&#10;    fast = nums[0]&#10;    while slow != fast:&#10;        slow = nums[slow]&#10;        fast = nums[fast]&#10;    return slow</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">27</td>
      <td rowspan="1">Arr 27 Find Missing And Repeating<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/find-missing-and-repeating2512/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, SDE Sheet, Love Babbar</details></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> N = 2, Arr[] = {2, 2}<br><b>Output:</b> 2 1</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Mathematical approach. Diff = Sum_N - Sum_Arr = Missing - Repeating. SumSqDiff = SumSq_N - SumSq_Arr = Missing^2 - Repeating^2. Use formulas to solve for both.</td>
      <td><b>Edge Cases:</b> <b>Integer Overflow:</b> Summing squares of 10^5 elements exceeds 32-bit INT, requiring long long.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findTwoElement(arr: List[int], n: int) -&gt; List[int]:&#10;    S_N = (n * (n+1)) // 2&#10;    Sq_N = (n * (n+1) * (2*n+1)) // 6&#10;    S, Sq = 0, 0&#10;    for num in arr:&#10;        S += num; Sq += num * num&#10;    val1 = S_N - S # X - Y&#10;    val2 = (Sq_N - Sq) // val1 # X + Y&#10;    x = (val1 + val2) // 2&#10;    y = x - val1&#10;    return [y, x] # Repeating, Missing</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">28</td>
      <td rowspan="1">Arr 28 Merge Two Sorted Arrays Without Extra Space<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z, SDE Sheet</details></td>
      <td rowspan="1"><b> </b> arr1=[1,3,5,7], arr2=[0,2,6,8,9]<br><b>Output:</b> arr1=[0,1,2,3], arr2=[5,6,7,8,9]</td>
      <td><b>Time:</b> O((N+M) log(N+M))<br><b>Space:</b> O(1)</td>
      <td>Optimal: Start pointers at end of arr1 (i) and beginning of arr2 (j). Swap if arr1[i] > arr2[j]. Afterwards, individually sort arr1 and arr2. Time is bounded by sorting.<br><br><b>Dependencies:</b> <code>#include <algorithm></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def merge(arr1: List[int], arr2: List[int], n: int, m: int) -&gt; None:&#10;    left, right = n - 1, 0&#10;    while left &gt;= 0 and right &lt; m:&#10;        if arr1[left] &gt; arr2[right]:&#10;            arr1[left], arr2[right] = arr2[right], arr1[left]&#10;            left -= 1; right += 1&#10;        else: break&#10;    arr1.sort(); arr2.sort()</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">29</td>
      <td rowspan="1">Arr 29 Maximum Product Subarray<br><br></b> <a href="https://leetcode.com/problems/maximum-product-subarray/" target="_blank">LeetCode 152</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, SDE Sheet, Love Babbar</details></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> nums = [2,3,-2,4]<br><b>Output:</b> 6</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Maintain prefix and suffix products. If a 0 is encountered, reset the product to 1. The max overall is the answer since negatives cancel out in pairs.<br><br><b>Dependencies:</b> <code>#include <limits.h></code></td>
      <td><b>Edge Cases:</b> <b>Odd negative numbers:</b> Checking both prefix and suffix elegantly covers the case where we drop one negative.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxProduct(nums: List[int]) -&gt; int:&#10;    pref, suff, ans = 1, 1, float(&#x27;-inf&#x27;)&#10;    n = len(nums)&#10;    for i in range(n):&#10;        if pref == 0: pref = 1&#10;        if suff == 0: suff = 1&#10;        pref *= nums[i]&#10;        suff *= nums[n-1-i]&#10;        ans = max(ans, pref, suff)&#10;    return int(ans)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">30</td>
      <td rowspan="1">Arr 30 Count Inversions<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/inversion-of-array-1587115620/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, SDE Sheet, Love Babbar</details></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> N = 5, arr[] = {2, 4, 1, 3, 5}<br><b>Output:</b> 3</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(N) auxiliary</td>
      <td>Optimal: Merge Sort approach. While merging two sorted halves, if left[i] > right[j], it forms an inversion with all remaining elements in the left half (mid - i + 1).</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def inversionCount(arr: List[int], n: int) -&gt; int:&#10;    def merge(low, mid, high):&#10;        temp, left, right, cnt = [], low, mid + 1, 0&#10;        while left &lt;= mid and right &lt;= high:&#10;            if arr[left] &lt;= arr[right]:&#10;                temp.append(arr[left]); left += 1&#10;            else:&#10;                temp.append(arr[right]); cnt += (mid - left + 1); right += 1&#10;        while left &lt;= mid: temp.append(arr[left]); left += 1&#10;        while right &lt;= high: temp.append(arr[right]); right += 1&#10;        for i in range(low, high + 1): arr[i] = temp[i - low]&#10;        return cnt&#10;    def mergeSort(low, high):&#10;        cnt = 0&#10;        if low &gt;= high: return cnt&#10;        mid = (low + high) // 2&#10;        cnt += mergeSort(low, mid)&#10;        cnt += mergeSort(mid + 1, high)&#10;        cnt += merge(low, mid, high)&#10;        return cnt&#10;    return mergeSort(0, n - 1)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">31</td>
      <td rowspan="1">Arr 31 Reverse Pairs<br><br></b> <a href="https://leetcode.com/problems/reverse-pairs/" target="_blank">LeetCode 493</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z, SDE Sheet</details></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> nums = [1,3,2,3,1]<br><b>Output:</b> 2</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(N)</td>
      <td>Optimal: Modified Merge Sort. Before merging, loop through left and right halves. If left[i] > 2 * right[j], increment j. Number of pairs is (j - (mid+1)).</td>
      <td><b>Edge Cases:</b> <b>Integer Overflow:</b> Use long long when doubling nums[j].<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def reversePairs(nums: List[int]) -&gt; int:&#10;    def merge(low, mid, high):&#10;        temp, left, right = [], low, mid + 1&#10;        while left &lt;= mid and right &lt;= high:&#10;            if nums[left] &lt;= nums[right]:&#10;                temp.append(nums[left]); left += 1&#10;            else: temp.append(nums[right]); right += 1&#10;        while left &lt;= mid: temp.append(nums[left]); left += 1&#10;        while right &lt;= high: temp.append(nums[right]); right += 1&#10;        for i in range(low, high + 1): nums[i] = temp[i - low]&#10;    def countPairs(low, mid, high):&#10;        right, cnt = mid + 1, 0&#10;        for i in range(low, mid + 1):&#10;            while right &lt;= high and nums[i] &gt; 2 * nums[right]: right += 1&#10;            cnt += (right - (mid + 1))&#10;        return cnt&#10;    def mergeSort(low, high):&#10;        cnt = 0&#10;        if low &gt;= high: return cnt&#10;        mid = (low + high) // 2&#10;        cnt += mergeSort(low, mid)&#10;        cnt += mergeSort(mid + 1, high)&#10;        cnt += countPairs(low, mid, high)&#10;        merge(low, mid, high)&#10;        return cnt&#10;    return mergeSort(0, len(nums) - 1)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">32</td>
      <td rowspan="1">Arr 32 Grid Unique Paths<br><br></b> <a href="https://leetcode.com/problems/unique-paths/" target="_blank">LeetCode 62</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> m = 3, n = 7<br><b>Output:</b> 28</td>
      <td><b>Time:</b> O(m-1)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Combinatorics approach. The total number of steps to reach the bottom-right corner is (m - 1) + (n - 1) = m + n - 2. Out of these steps, we need to choose (m - 1) downward steps (or n - 1 rightward steps). The number of paths is (m + n - 2) C (m - 1).</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def uniquePaths(m: int, n: int) -&gt; int:&#10;    N = n + m - 2&#10;    r = m - 1&#10;    res = 1&#10;    for i in range(1, r + 1):&#10;        res = res * (N - r + i) // i&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">33</td>
      <td rowspan="1">Arr 33 Search A 2D Matrix<br><br></b> <a href="https://leetcode.com/problems/search-a-2d-matrix/" target="_blank">LeetCode 74</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, SDE Sheet, Love Babbar, Apna College</details></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3<br><b>Output:</b> true</td>
      <td><b>Time:</b> O(log(m * n))<br><b>Space:</b> O(1)</td>
      <td>Optimal: Treat the 2D matrix as a 1D array and apply binary search. The element at `mid` can be accessed using `matrix[mid / cols][mid % cols]`.</td>
      <td><b>Edge Cases:</b> <b>Empty Matrix:</b> Return false.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def searchMatrix(matrix: List[List[int]], target: int) -&gt; bool:&#10;    if not matrix: return False&#10;    m, n = len(matrix), len(matrix[0])&#10;    low, high = 0, (m * n) - 1&#10;    while low &lt;= high:&#10;        mid = (low + high) // 2&#10;        if matrix[mid // n][mid % n] == target: return True&#10;        if matrix[mid // n][mid % n] &lt; target: low = mid + 1&#10;        else: high = mid - 1&#10;    return False</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">34</td>
      <td rowspan="1">Arr 34 Minimum Number Of Jumps<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td rowspan="1"><b> </b> Greedy tracking bounds.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Maintain `maxReach`, `steps`, and `jumps`. At each step `i`, `maxReach = max(maxReach, i + arr[i])`. Decrement `steps`. If `steps == 0`, `jumps++` and `steps = maxReach - i`. If `i >= maxReach`, return -1.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minJumps(arr: List[int], n: int) -&gt; int:&#10;    if n &lt;= 1: return 0&#10;    if arr[0] == 0: return -1&#10;    maxReach = steps = arr[0]&#10;    jumps = 1&#10;    for i in range(1, n):&#10;        if i == n - 1: return jumps&#10;        maxReach = max(maxReach, i + arr[i])&#10;        steps -= 1&#10;        if steps == 0:&#10;            jumps += 1&#10;            if i &gt;= maxReach: return -1&#10;            steps = maxReach - i&#10;    return -1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">35</td>
      <td rowspan="1">Arr 35 Kadanes Algorithm<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td rowspan="1"><b> </b> Keep tracking current sum.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Maintain `max_sum` and `curr_sum`. For each element, `curr_sum = max(element, curr_sum + element)`. `max_sum = max(max_sum, curr_sum)`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxSubarraySum(arr: List[int], n: int) -&gt; int:&#10;    maxSum = currSum = arr[0]&#10;    for i in range(1, n):&#10;        currSum = max(arr[i], currSum + arr[i])&#10;        maxSum = max(maxSum, currSum)&#10;    return maxSum</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">36</td>
      <td rowspan="1">Arr 36 Count Pairs With Given Sum<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td rowspan="1"><b> </b> Hash Map.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Optimal: Use a hash map to store the frequencies of the elements seen so far. For each element `x`, check if `K - x` is in the hash map. If it is, add its frequency to the `count`. Finally, increment the frequency of `x` in the hash map.<br><br><b>Dependencies:</b> <code>#include <unordered_map></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def getPairsCount(arr: List[int], n: int, k: int) -&gt; int:&#10;    m = collections.defaultdict(int)&#10;    count = 0&#10;    for x in arr:&#10;        if k - x in m:&#10;            count += m[k - x]&#10;        m[x] += 1&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">37</td>
      <td rowspan="1">Arr 37 Common Elements In Three Sorted Arrays<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/common-elements1132/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td rowspan="1"><b> </b> Three pointers.</td>
      <td><b>Time:</b> O(N1 + N2 + N3)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Use three pointers `i`, `j`, `k` for the three arrays. If `A[i] == B[j] == C[k]`, it's a common element, add it to the result (handling duplicates), and increment all three pointers. Else, increment the pointer that points to the smallest value.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def commonElements(A: List[int], B: List[int], C: List[int], n1: int, n2: int, n3: int) -&gt; List[int]:&#10;    res = []&#10;    i = j = k = 0&#10;    while i &lt; n1 and j &lt; n2 and k &lt; n3:&#10;        if A[i] == B[j] == C[k]:&#10;            if not res or res[-1] != A[i]:&#10;                res.append(A[i])&#10;            i += 1; j += 1; k += 1&#10;        elif A[i] &lt;= B[j] and A[i] &lt;= C[k]: i += 1&#10;        elif B[j] &lt;= A[i] and B[j] &lt;= C[k]: j += 1&#10;        else: k += 1&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">38</td>
      <td rowspan="1">Arr 38 Rearrange Array Alternately<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/rearrange-array-alternately-1587115620/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, SDE Sheet</details></td>
      <td rowspan="1"><b> </b> Math-based encoding O(1) space.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: To achieve O(1) space, encode two values into one using `arr[i] += (arr[max_idx] % max_elem) * max_elem`. Iterate with two pointers `max_idx` and `min_idx`. At the end, divide every element by `max_elem`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def rearrange(arr, n):&#10;    min_idx, max_idx = 0, n - 1&#10;    max_elem = arr[n - 1] + 1&#10;    for i in range(n):&#10;        if i % 2 == 0:&#10;            arr[i] += (arr[max_idx] % max_elem) * max_elem&#10;            max_idx -= 1&#10;        else:&#10;            arr[i] += (arr[min_idx] % max_elem) * max_elem&#10;            min_idx += 1&#10;    for i in range(n):&#10;        arr[i] = arr[i] // max_elem</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">39</td>
      <td rowspan="1">Arr 39 Rearrange Array In Alternating Positive And Negative Items<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/array-of-alternate-ve-and--ve-nos1401/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td rowspan="1"><b> </b> Extra Space Array.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Optimal: Collect all positive numbers in one array and all negative numbers in another. Overwrite the original array by picking elements alternatively from the two arrays.</td>
      <td><b>Edge Cases:</b> Unequal count of positive and negative<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def rearrange(arr, n):&#10;    pos = [x for x in arr if x &gt;= 0]&#10;    neg = [x for x in arr if x &lt; 0]&#10;    i, j, k = 0, 0, 0&#10;    while i &lt; len(pos) and j &lt; len(neg):&#10;        arr[k] = pos[i]; k += 1; i += 1&#10;        arr[k] = neg[j]; k += 1; j += 1&#10;    while i &lt; len(pos):&#10;        arr[k] = pos[i]; k += 1; i += 1&#10;    while j &lt; len(neg):&#10;        arr[k] = neg[j]; k += 1; j += 1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">40</td>
      <td rowspan="1">Arr 40 Subarray With 0 Sum<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/subarray-with-0-sum-1587115621/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, SDE Sheet, Love Babbar</details></td>
      <td rowspan="1"><b> </b> Prefix Sum with HashSet.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Optimal: Iterate through the array and calculate the prefix sum. If the prefix sum is 0 or it already exists in a hash set, it means a subarray with sum 0 exists.<br><br><b>Dependencies:</b> Hash Set</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def subArrayExists(arr, n):&#10;    sumSet = set()&#10;    curr_sum = 0&#10;    for num in arr:&#10;        curr_sum += num&#10;        if curr_sum == 0 or curr_sum in sumSet:&#10;            return True&#10;        sumSet.add(curr_sum)&#10;    return False</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">41</td>
      <td rowspan="1">Arr 41 Factorial Of A Large Number<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/factorials-of-large-numbers2508/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td rowspan="1"><b> </b> Array based multiplication.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N log(N!))</td>
      <td>Optimal: Use an array to store the result. Initially, it holds 1. Multiply the array by numbers from 2 to N. The multiplication is done school-style by carrying over remainders to the next index.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def factorial(N):&#10;    # Python handles large integers automatically&#10;    import math&#10;    fact = math.factorial(N)&#10;    return [int(x) for x in str(fact)]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">42</td>
      <td rowspan="1">Arr 42 Maximum Product Subarray<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/maximum-product-subarray3604/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z, SDE Sheet</details></td>
      <td rowspan="1"><b> </b> Prefix and Suffix iteration.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Iterate from left to right calculating prefix product, and right to left calculating suffix product. If either is 0, reset it to 1. The max product will be the max of all prefix and suffix products.</td>
      <td><b>Edge Cases:</b> Zero elements<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxProduct(arr, n):&#10;    max_prod = float(&#x27;-inf&#x27;)&#10;    pref, suff = 1, 1&#10;    for i in range(n):&#10;        if pref == 0: pref = 1&#10;        if suff == 0: suff = 1&#10;        pref *= arr[i]&#10;        suff *= arr[n - i - 1]&#10;        max_prod = max(max_prod, pref, suff)&#10;    return max_prod</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">43</td>
      <td rowspan="1">Arr 43 Longest Consecutive Subsequence<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/longest-consecutive-subsequence2449/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z, SDE Sheet</details></td>
      <td rowspan="1"><b> </b> Hash Set.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Optimal: Insert all elements into a hash set. For each element, check if `element - 1` exists. If not, it's the start of a sequence. Then increment to find consecutive elements.<br><br><b>Dependencies:</b> Hash Set</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findLongestConseqSubseq(arr, N):&#10;    s = set(arr)&#10;    longest = 0&#10;    for num in s:&#10;        if (num - 1) not in s:&#10;            curr = num&#10;            count = 1&#10;            while (curr + 1) in s:&#10;                curr += 1&#10;                count += 1&#10;            longest = max(longest, count)&#10;    return longest</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">44</td>
      <td rowspan="1">Arr 44 Minimum Swaps And K Together<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/minimum-swaps-required-to-bring-all-elements-less-than-or-equal-to-k-together4847/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td rowspan="1"><b> </b> Sliding Window.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: First count all elements <= k (let's say `cnt`). This will be the window size. Find elements > k in the first window. Then slide the window, updating the number of elements > k. The minimum among all windows is the answer.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minSwap(arr, n, k):&#10;    cnt = sum(1 for x in arr if x &lt;= k)&#10;    bad = sum(1 for i in range(cnt) if arr[i] &gt; k)&#10;    ans = bad&#10;    for i in range(n - cnt):&#10;        if arr[i] &gt; k: bad -= 1&#10;        if arr[i + cnt] &gt; k: bad += 1&#10;        ans = min(ans, bad)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">45</td>
      <td rowspan="1">Arr 45 Greedy 05 Fractional Knapsack<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td rowspan="1"><b> </b> Sort by value/weight ratio.</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Sort items in descending order of value/weight ratio. Greedily pick items with the highest ratio first. If an item cannot fit completely, take the fraction that fits.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class Item:&#10;    def __init__(self,val,w):&#10;        self.value = val&#10;        self.weight = w&#10;&#10;def fractionalKnapsack(W, arr, n):&#10;    arr.sort(key=lambda x: x.value / x.weight, reverse=True)&#10;    finalValue = 0.0&#10;    for item in arr:&#10;        if W &gt;= item.weight:&#10;            finalValue += item.value&#10;            W -= item.weight&#10;        else:&#10;            finalValue += item.value * (W / item.weight)&#10;            break&#10;    return finalValue</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">46</td>
      <td rowspan="1">Arr 46 Greedy 06 Choose And Swap<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/choose-and-swap0531/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td rowspan="1"><b> </b> Track first occurrences.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Store the first occurrence index of all characters. Iterate the string, for each character check if there is a lexicographically smaller character that appears later in the string. If so, swap them and break.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def chooseandswap(a):&#10;    s = set(a)&#10;    for i in range(len(a)):&#10;        if a[i] in s: s.remove(a[i])&#10;        if not s: break&#10;        min_char = min(s)&#10;        if min_char &lt; a[i]:&#10;            ch1, ch2 = a[i], min_char&#10;            a = a.replace(ch1, &#x27;#&#x27;)&#10;            a = a.replace(ch2, ch1)&#10;            a = a.replace(&#x27;#&#x27;, ch2)&#10;            break&#10;    return a</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">47</td>
      <td rowspan="1">Arr 47 Greedy 07 Maximum Trains For Which Stoppage Can Be Provided<br><br></b> <a href="https://www.geeksforgeeks.org/maximum-trains-stoppage-can-provided/" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td rowspan="1"><b> </b> Activity Selection on each platform.</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(N)</td>
      <td>Optimal: Group trains by platform. For each platform, this reduces to the Activity Selection Problem. Sort the trains by departure time and greedily pick non-overlapping trains.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxStop(trains, n, m):&#10;    platforms = [[] for _ in range(m + 1)]&#10;    for arr, dep, plat in trains:&#10;        platforms[plat].append((dep, arr))&#10;    count = 0&#10;    for i in range(1, m + 1):&#10;        if not platforms[i]: continue&#10;        platforms[i].sort()&#10;        count += 1&#10;        lastDep = platforms[i][0][0]&#10;        for j in range(1, len(platforms[i])):&#10;            if platforms[i][j][1] &gt;= lastDep:&#10;                count += 1&#10;                lastDep = platforms[i][j][0]&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">48</td>
      <td rowspan="1">Arr 48 Greedy 08 Minimum Platforms<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z, SDE Sheet</details></td>
      <td rowspan="1"><b> </b> Sort arrival and departure times separately.</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Sort arrival and departure arrays separately. Use two pointers, one for arrival and one for departure. If arrival < departure, a platform is needed, so increment count. If arrival >= departure, a platform is freed, so decrement count. Track the maximum count.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findPlatform(arr, dep, n):&#10;    arr.sort()&#10;    dep.sort()&#10;    plat_needed, result = 1, 1&#10;    i, j = 1, 0&#10;    while i &lt; n and j &lt; n:&#10;        if arr[i] &lt;= dep[j]:&#10;            plat_needed += 1&#10;            i += 1&#10;        else:&#10;            plat_needed -= 1&#10;            j += 1&#10;        result = max(result, plat_needed)&#10;    return result</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">49</td>
      <td rowspan="1">Arr 49 Greedy 09 Buy Maximum Stocks If I Stocks Can Be Bought On I Th Day<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/buy-maximum-stocks-if-i-stocks-can-be-bought-on-i-th-day/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td rowspan="1"><b> </b> Sort by price.</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(N)</td>
      <td>Optimal: Store pairs of (price, day). Sort by price. Greedily buy as many stocks as possible on the day with the lowest price, bounded by the maximum allowed on that day (which is 'day') and the remaining money.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def buyMaximumProducts(n, k, price):&#10;    v = [(price[i], i + 1) for i in range(n)]&#10;    v.sort()&#10;    ans = 0&#10;    for p, d in v:&#10;        amount = min(d, k // p)&#10;        ans += amount&#10;        k -= amount * p&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">50</td>
      <td rowspan="1">Arr 50 Greedy 10 Shop In Candy Store<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/shop-in-candy-store1145/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td rowspan="1"><b> </b> Sort and pick from ends.</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Sort the candies by price. For minimum cost, buy the cheapest and take K most expensive for free. For maximum cost, buy the most expensive and take K cheapest for free.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def candyStore(candies, N, K):&#10;    candies.sort()&#10;    minCost, maxCost = 0, 0&#10;    i, j = 0, N - 1&#10;    while i &lt;= j:&#10;        minCost += candies[i]&#10;        i += 1; j -= K&#10;    i, j = N - 1, 0&#10;    while j &lt;= i:&#10;        maxCost += candies[i]&#10;        i -= 1; j += K&#10;    return [minCost, maxCost]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">51</td>
      <td rowspan="1">Arr 51 Greedy 11 Minimize Cash Flow Among A Given Set Of Friends Who Have Borrowed Money From Each Other<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/minimize-cash-flow/0" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td rowspan="1"><b> </b> Net amounts.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N)</td>
      <td>Optimal: Calculate the net amount for each person by subtracting incoming debts from outgoing debts. Find the person with maximum net credit and maximum net debit. Settle their amounts, and repeat recursively or iteratively until all net amounts are zero.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minCashFlow(graph, n):&#10;    amount = [0] * n&#10;    for p in range(n):&#10;        for i in range(n):&#10;            amount[p] += (graph[i][p] - graph[p][i])&#10;    ans = [[0]*n for _ in range(n)]&#10;    def rec(amount):&#10;        mxCredit = amount.index(max(amount))&#10;        mxDebit = amount.index(min(amount))&#10;        if amount[mxCredit] == 0 and amount[mxDebit] == 0: return&#10;        minVal = min(-amount[mxDebit], amount[mxCredit])&#10;        amount[mxCredit] -= minVal&#10;        amount[mxDebit] += minVal&#10;        ans[mxDebit][mxCredit] = minVal&#10;        rec(amount)&#10;    rec(amount)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">52</td>
      <td rowspan="1">Arr 52 Greedy 12 Minimum Cost To Cut A Board Into Squares<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/minimum-cost-to-cut-a-board-into-squares/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td rowspan="1"><b> </b> Sort costs.</td>
      <td><b>Time:</b> O(M log M + N log N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Sort all vertical and horizontal cuts in descending order. Maintain counts of horizontal and vertical pieces. Greedily pick the cut with the highest cost. If a horizontal cut is made, its total cost is `cut_cost * vertical_pieces`. Update the counts.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minimumCostOfBreaking(X, Y, M, N):&#10;    X.sort(reverse=True)&#10;    Y.sort(reverse=True)&#10;    hzntl, vert = 1, 1&#10;    i, j, res = 0, 0, 0&#10;    while i &lt; M - 1 and j &lt; N - 1:&#10;        if X[i] &gt; Y[j]:&#10;            res += X[i] * vert&#10;            hzntl += 1; i += 1&#10;        else:&#10;            res += Y[j] * hzntl&#10;            vert += 1; j += 1&#10;    while i &lt; M - 1:&#10;        res += X[i] * vert; i += 1&#10;    while j &lt; N - 1:&#10;        res += Y[j] * hzntl; j += 1&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">53</td>
      <td rowspan="1">Arr 53 Greedy 13 Survival On Island<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/check-if-it-is-possible-to-survive-on-island4922/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td rowspan="1"><b> </b> Math.</td>
      <td><b>Time:</b> O(1)<br><b>Space:</b> O(1)</td>
      <td>Optimal: If total required food > max food you can buy in S days excluding Sundays, return -1. Else, total required food is `S * M`. Minimum days = `ceil((S * M) / N)`. Also handle the edge case where `N < M` or if survival > 6 days and `(N * 6) < (M * 7)`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import math&#10;def minimumDays(S, N, M):&#10;    if M &gt; N: return -1&#10;    if S &gt; 6 and (N * 6) &lt; (M * 7): return -1&#10;    return math.ceil((S * M) / N)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">54</td>
      <td rowspan="1">Arr 54 Greedy 14 Maximum Meetings In One Room<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/maximum-meetings-in-one-room/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td rowspan="1"><b> </b> Activity Selection.</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(N)</td>
      <td>Optimal: Store `(start, end, index)`. Sort by end time. Pick the first meeting. For subsequent meetings, if `start > last_picked_end`, pick it and update `last_picked_end`. Return sorted indices.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxMeetings(N, S, F):&#10;    m = [(S[i], F[i], i + 1) for i in range(N)]&#10;    m.sort(key=lambda x: (x[1], x[2]))&#10;    ans = [m[0][2]]&#10;    last_e = m[0][1]&#10;    for i in range(1, N):&#10;        if m[i][0] &gt; last_e:&#10;            ans.append(m[i][2])&#10;            last_e = m[i][1]&#10;    ans.sort()&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">55</td>
      <td rowspan="1">Arr 55 Trapping Rain Water<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/trapping-rain-water-1587115621/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z, SDE Sheet</details></td>
      <td rowspan="1"><b> </b> Two Pointers.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Use two pointers, left and right. Maintain left_max and right_max. If `arr[left] <= arr[right]`, the water trapped depends on left_max. If `arr[left] > left_max`, update left_max, else add `left_max - arr[left]` to answer and increment left. Repeat for right.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def trappingWater(arr, n):&#10;    left, right = 0, n - 1&#10;    left_max, right_max = 0, 0&#10;    res = 0&#10;    while left &lt;= right:&#10;        if arr[left] &lt;= arr[right]:&#10;            if arr[left] &gt;= left_max: left_max = arr[left]&#10;            else: res += left_max - arr[left]&#10;            left += 1&#10;        else:&#10;            if arr[right] &gt;= right_max: right_max = arr[right]&#10;            else: res += right_max - arr[right]&#10;            right -= 1&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">56</td>
      <td rowspan="1">Arr 56 Chocolate Distribution Problem<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/chocolate-distribution-problem3825/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td rowspan="1"><b> </b> Sort and Slide.</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Sort the array. Find the minimum difference between `A[i+M-1]` and `A[i]` for all possible `i` from `0` to `N-M`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findMinDiff(a, n, m):&#10;    a.sort()&#10;    min_diff = float(&#x27;inf&#x27;)&#10;    for i in range(n - m + 1):&#10;        diff = a[i + m - 1] - a[i]&#10;        if diff &lt; min_diff:&#10;            min_diff = diff&#10;    return min_diff</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">57</td>
      <td rowspan="1">Arr 57 Smallest Subarray With Sum Greater Than X<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/smallest-subarray-with-sum-greater-than-x5651/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td rowspan="1"><b> </b> Sliding Window.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Use a sliding window. Add elements to `curr_sum` and increment `end`. When `curr_sum > x`, update `min_len` and subtract `arr[start]`, increment `start`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def smallestSubWithSum(arr, n, x):&#10;    curr_sum = 0&#10;    min_len = n + 1&#10;    start, end = 0, 0&#10;    while end &lt; n:&#10;        while curr_sum &lt;= x and end &lt; n:&#10;            curr_sum += arr[end]&#10;            end += 1&#10;        while curr_sum &gt; x and start &lt; n:&#10;            min_len = min(min_len, end - start)&#10;            curr_sum -= arr[start]&#10;            start += 1&#10;    return 0 if min_len == n + 1 else min_len</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">58</td>
      <td rowspan="1">Arr 58 Three Way Partitioning<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/three-way-partitioning/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td rowspan="1"><b> </b> Dutch National Flag algorithm.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Use three pointers: `low`, `mid`, `high`. If `arr[mid] < a`, swap `arr[low]` and `arr[mid]`, increment both. If `arr[mid] > b`, swap `arr[mid]` and `arr[high]`, decrement `high`. Else increment `mid`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def threeWayPartition(array, a, b):&#10;    low, mid, high = 0, 0, len(array) - 1&#10;    while mid &lt;= high:&#10;        if array[mid] &lt; a:&#10;            array[low], array[mid] = array[mid], array[low]&#10;            low += 1&#10;            mid += 1&#10;        elif array[mid] &gt; b:&#10;            array[mid], array[high] = array[high], array[mid]&#10;            high -= 1&#10;        else:&#10;            mid += 1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">59</td>
      <td rowspan="1">Arr 59 Palindromic Array<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/palindromic-array-1587115620/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td rowspan="1"><b> </b> Check individual numbers.</td>
      <td><b>Time:</b> O(N * d)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Iterate through each number in the array. For each number, reverse its digits to check if it's a palindrome. If any number is not, return 0. If all are, return 1.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def PalinArray(arr, n):&#10;    for num in arr:&#10;        if str(num) != str(num)[::-1]:&#10;            return 0&#10;    return 1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">60</td>
      <td rowspan="1">Arr 60 Find The Median<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/find-the-median0527/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td rowspan="1"><b> </b> Sort array.</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Sort the array. If the size is odd, the median is the middle element. If the size is even, the median is the average of the two middle elements.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def find_median(v):&#10;    v.sort()&#10;    n = len(v)&#10;    if n % 2 != 0:&#10;        return v[n // 2]&#10;    else:&#10;        return (v[n // 2 - 1] + v[n // 2]) // 2</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">61</td>
      <td rowspan="1">Arr 61 Median Of Two Sorted Arrays Of Different Sizes<br><br></b> <a href="https://leetcode.com/problems/median-of-two-sorted-arrays/" target="_blank">LeetCode 4</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, SDE Sheet, Love Babbar</details></td>
      <td rowspan="1"><b> </b> Binary Search.</td>
      <td><b>Time:</b> O(log(min(N, M)))<br><b>Space:</b> O(1)</td>
      <td>Optimal: Use Binary Search on the smaller array. Partition both arrays such that the number of elements on the left side is equal to or one more than the right side. Check if `maxLeftX <= minRightY` and `maxLeftY <= minRightX`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findMedianSortedArrays(nums1, nums2):&#10;    if len(nums1) &gt; len(nums2): return findMedianSortedArrays(nums2, nums1)&#10;    x, y = len(nums1), len(nums2)&#10;    low, high = 0, x&#10;    while low &lt;= high:&#10;        partitionX = (low + high) // 2&#10;        partitionY = (x + y + 1) // 2 - partitionX&#10;        maxLeftX = float(&#x27;-inf&#x27;) if partitionX == 0 else nums1[partitionX - 1]&#10;        minRightX = float(&#x27;inf&#x27;) if partitionX == x else nums1[partitionX]&#10;        maxLeftY = float(&#x27;-inf&#x27;) if partitionY == 0 else nums2[partitionY - 1]&#10;        minRightY = float(&#x27;inf&#x27;) if partitionY == y else nums2[partitionY]&#10;        if maxLeftX &lt;= minRightY and maxLeftY &lt;= minRightX:&#10;            if (x + y) % 2 == 0:&#10;                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0&#10;            else:&#10;                return max(maxLeftX, maxLeftY)&#10;        elif maxLeftX &gt; minRightY:&#10;            high = partitionX - 1&#10;        else:&#10;            low = partitionX + 1&#10;    return 0.0</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">62</td>
      <td rowspan="1">Arr 62 Count More Than N K Occurences<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/count-element-occurences/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td rowspan="1"><b> </b> HashMap.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Optimal: Store the frequencies of all elements in a hash map. Iterate through the hash map and count the number of elements having frequency greater than `N/k`.<br><br><b>Dependencies:</b> Hash Map</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def countOccurence(arr, n, k):&#10;    count = collections.Counter(arr)&#10;    res = 0&#10;    target = n // k&#10;    for key, val in count.items():&#10;        if val &gt; target:&#10;            res += 1&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">63</td>
      <td rowspan="1">Arr 63 Find The Missing Number<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/missing-number-in-array1416/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td rowspan="1"><b> </b> Sum formula.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Calculate the sum of first N natural numbers using `N*(N+1)/2`. Subtract the sum of all elements in the array from it. The result is the missing number.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def missingNumber(array, n):&#10;    return n * (n + 1) // 2 - sum(array)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">64</td>
      <td rowspan="1">Arr 64 Longest Subarray With Sum K Positives<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td rowspan="1"><b> </b> Sliding Window / Two Pointers.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Since all elements are positive, use two pointers (sliding window). Expand `right` and add to sum. If sum > K, shrink `left` and subtract from sum. If sum == K, update max length.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def lenOfLongSubarr(A, N, K):&#10;    left, sum_val, max_len = 0, 0, 0&#10;    for right in range(N):&#10;        sum_val += A[right]&#10;        while sum_val &gt; K and left &lt;= right:&#10;            sum_val -= A[left]&#10;            left += 1&#10;        if sum_val == K:&#10;            max_len = max(max_len, right - left + 1)&#10;    return max_len</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">65</td>
      <td rowspan="1">Arr 65 Merge Sorted Array Without Extra Space<br><br></b> <a href="https://leetcode.com/problems/merge-sorted-array/" target="_blank">LeetCode 88</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z, SDE Sheet</details></td>
      <td rowspan="1"><b> </b> Two pointers from end.</td>
      <td><b>Time:</b> O(M + N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Since `nums1` has enough space at the end, use three pointers: `p1` at the end of valid elements in `nums1` (m-1), `p2` at the end of `nums2` (n-1), and `p` at the very end of `nums1` (m+n-1). Compare elements at `p1` and `p2`, put the larger one at `p`, and decrement pointers.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def merge(nums1, m, nums2, n):&#10;    p1, p2, p = m - 1, n - 1, m + n - 1&#10;    while p1 &gt;= 0 and p2 &gt;= 0:&#10;        if nums1[p1] &gt; nums2[p2]:&#10;            nums1[p] = nums1[p1]&#10;            p1 -= 1&#10;        else:&#10;            nums1[p] = nums2[p2]&#10;            p2 -= 1&#10;        p -= 1&#10;    while p2 &gt;= 0:&#10;        nums1[p] = nums2[p2]&#10;        p -= 1&#10;        p2 -= 1</code></pre></details></td>
    </tr>
  </tbody>
</table>
