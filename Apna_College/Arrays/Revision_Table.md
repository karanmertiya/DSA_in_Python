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
      <td rowspan="1">Arr 01 Largest Element<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/largest-element-in-array/1' target='_blank'>GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: A = [1, 8, 7, 56, 90], Output: 90</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td>-</td>
      <td><b>Initialization:</b> Initialize `max_val` with the first element or negative infinity.</td>
      <td><b>Explanation:</b> Iterate through the array maintaining a variable for the maximum element seen so far.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def largest(arr: list[int]) -&gt; int:&#10;    max_val = arr[0]&#10;    for num in arr:&#10;        if num &gt; max_val:&#10;            max_val = num&#10;    return max_val</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">2</td>
      <td rowspan="1">Arr 05 Rotate Array<br><br></b> <a href='https://leetcode.com/problems/rotate-array/' target='_blank'>LeetCode 189</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: nums = [1,2,3,4,5,6,7], k = 3, Output: [5,6,7,1,2,3,4]</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><code>std::reverse</code></td>
      <td><b>K > N:</b> k might be greater than array length, so perform `k = k % n` first.</td>
      <td><b>Explanation:</b> Reverse Algorithm. Reverse the whole array, then reverse the first `k` elements, then reverse the remaining `N-k` elements.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def rotate(nums: list[int], k: int) -&gt; None:&#10;    n = len(nums)&#10;    k = k % n&#10;    nums.reverse()&#10;    nums[:k] = reversed(nums[:k])&#10;    nums[k:] = reversed(nums[k:])</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">3</td>
      <td rowspan="1">Arr 06 Move Zeroes<br><br></b> <a href='https://leetcode.com/problems/move-zeroes/' target='_blank'>LeetCode 283</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: nums = [0,1,0,3,12], Output: [1,3,12,0,0]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><code>std::swap</code></td>
      <td><b>No zeroes:</b> Swaps element with itself initially, no overhead.</td>
      <td><b>Explanation:</b> Two-pointer approach (Snowball method). Pointer `i` tracks the first zero found, pointer `j` scans for non-zeroes to swap.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def moveZeroes(nums: list[int]) -&gt; None:&#10;    i = 0&#10;    for j in range(len(nums)):&#10;        if nums[j] != 0:&#10;            nums[i], nums[j] = nums[j], nums[i]&#10;            i += 1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">4</td>
      <td rowspan="1">Arr 08 Max Consecutive Ones<br><br></b> <a href='https://leetcode.com/problems/max-consecutive-ones/' target='_blank'>LeetCode 485</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: nums = [1,1,0,1,1,1], Output: 3</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><code>std::max</code></td>
      <td><b>Trailing Ones:</b> Must perform a final max check outside the loop or update max dynamically inside.</td>
      <td><b>Explanation:</b> Iterate while counting 1s. If a 0 is found, update max count and reset current count to 0.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findMaxConsecutiveOnes(nums: list[int]) -&gt; int:&#10;    max_cnt = current_cnt = 0&#10;    for num in nums:&#10;        if num == 1:&#10;            current_cnt += 1&#10;            max_cnt = max(max_cnt, current_cnt)&#10;        else:&#10;            current_cnt = 0&#10;    return max_cnt</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">5</td>
      <td rowspan="1">Arr 10 Sort Colors Dnf<br><br></b> <a href='https://leetcode.com/problems/sort-colors/' target='_blank'>LeetCode 75</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: nums = [2,0,2,1,1,0], Output: [0,0,1,1,2,2]<br><br><b>Note (Constraint):</b> Do not use library sort. Use single pass.</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><code>std::swap</code></td>
      <td><b>Mid pointer increment:</b> When swapping with `high`, we do NOT increment `mid` because the swapped element from `high` needs to be evaluated.</td>
      <td><b>Explanation:</b> Dutch National Flag Algorithm (3 pointers). `low` tracks 0s, `mid` scans array, `high` tracks 2s. Swap elements to maintain sections.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def sortColors(nums: list[int]) -&gt; None:&#10;    low, mid, high = 0, 0, len(nums) - 1&#10;    while mid &lt;= high:&#10;        if nums[mid] == 0:&#10;            nums[low], nums[mid] = nums[mid], nums[low]&#10;            low += 1; mid += 1&#10;        elif nums[mid] == 1:&#10;            mid += 1&#10;        else:&#10;            nums[mid], nums[high] = nums[high], nums[mid]&#10;            high -= 1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">6</td>
      <td rowspan="1">Arr 11 Majority Element<br><br></b> <a href='https://leetcode.com/problems/majority-element/' target='_blank'>LeetCode 169</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: nums = [2,2,1,1,1,2,2], Output: 2</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>Verification phase:</b> If it's not guaranteed a majority exists, a second `O(N)` pass is required to count the candidate. (Leetcode guarantees it exists).</td>
      <td><b>Explanation:</b> Moore's Voting Algorithm. Track a candidate and a counter. Increment if same as candidate, decrement if different. If zero, pick new candidate.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def majorityElement(nums: list[int]) -&gt; int:&#10;    count = candidate = 0&#10;    for num in nums:&#10;        if count == 0:&#10;            candidate = num&#10;        count += (1 if num == candidate else -1)&#10;    return candidate</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">7</td>
      <td rowspan="1">Arr 12 Kadanes Algorithm Max Subarray Sum<br><br></b> <a href='https://leetcode.com/problems/maximum-subarray/' target='_blank'>LeetCode 53</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: nums = [-2,1,-3,4,-1,2,1,-5,4], Output: 6 (Subarray [4,-1,2,1])</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><code>std::max</code></td>
      <td><b>All Negative Numbers:</b> Initialize `max_sum` with `INT_MIN` or `nums[0]` so it can correctly return the smallest negative number instead of 0.</td>
      <td><b>Explanation:</b> Kadane's Algorithm. Keep a running sum. If sum becomes negative, reset it to 0 (a negative prefix will never help a future subarray).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxSubArray(nums: list[int]) -&gt; int:&#10;    max_sum = float(&#x27;-inf&#x27;)&#10;    current_sum = 0&#10;    for num in nums:&#10;        current_sum += num&#10;        if current_sum &gt; max_sum:&#10;            max_sum = current_sum&#10;        if current_sum &lt; 0:&#10;            current_sum = 0&#10;    return int(max_sum)</code></pre></details></td>
    </tr>
  </tbody>
</table>
