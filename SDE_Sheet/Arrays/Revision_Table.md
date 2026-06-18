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
      <td rowspan="2">1</td>
      <td rowspan="2">Arr 03 Remove Duplicates<br><br></b> <a href='https://leetcode.com/problems/remove-duplicates-from-sorted-array/' target='_blank'>LeetCode 26</a></td>
      <td rowspan="2"><b>Example 1:</b> Input: arr = [1, 1, 2], Output: 2, arr = [1, 2, _]<br><br><b>Note (Constraint):</b> Array is sorted.</td>
      <td><b>Time:</b> O(N log N) (Trade-off)<br><b>Space:</b> O(N) (Trade-off)</td>
      <td><code>std::set</code> / <code>set()</code></td>
      <td><b>Set Ordering:</b> Uses ordered Set to maintain array sort order when writing back.</td>
      <td><b>Explanation:</b> Use an auxiliary HashSet to store unique elements, then put them back.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def remove_duplicates_brute(arr: list[int]) -&gt; int:&#10;    unique_set = sorted(set(arr))&#10;    for i in range(len(unique_set)):&#10;        arr[i] = unique_set[i]&#10;    return len(unique_set)</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td>-</td>
      <td><b>In-place Edit:</b> Mutates exactly up to index `i`, leaving trailing garbage intact as per standard.</td>
      <td><b>Explanation:</b> Two-pointer approach: Place unique elements at the `i` pointer while `j` scans.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def remove_duplicates_optimal(arr: list[int]) -&gt; int:&#10;    if not arr: return 0&#10;    i = 0&#10;    for j in range(1, len(arr)):&#10;        if arr[i] != arr[j]:&#10;            i += 1&#10;            arr[i] = arr[j]&#10;    return i + 1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">2</td>
      <td rowspan="2">Arr 06 Two Sum<br><br></b> <a href='https://leetcode.com/problems/two-sum/' target='_blank'>LeetCode 1</a></td>
      <td rowspan="2"><b>Example 1:</b> Input: nums = [2,7,11,15], target = 9, Output: [0,1]<br><br><b>Note (Constraint):</b> 2 &le; N &le; 10<sup>4</sup></td>
      <td><b>Time:</b> O(N<sup>2</sup>) (Trade-off)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Nested loops to check all possible pairs.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def two_sum_brute(nums: list[int], target: int) -&gt; list[int]:&#10;    for i in range(len(nums)):&#10;        for j in range(i + 1, len(nums)):&#10;            if nums[i] + nums[j] == target:&#10;                return [i, j]&#10;    return []</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(N) (Trade-off)</td>
      <td><code>std::unordered_map</code> / <code>dict</code></td>
      <td><b>One Pass:</b> Storing elements *after* checking ensures a number isn't used twice for itself.</td>
      <td><b>Explanation:</b> Use a Hash Map to store elements and their indices. Check for `target - current`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def two_sum_optimal(nums: list[int], target: int) -&gt; list[int]:&#10;    hash_map = {}&#10;    for i, num in enumerate(nums):&#10;        needed = target - num&#10;        if needed in hash_map:&#10;            return [hash_map[needed], i]&#10;        hash_map[num] = i&#10;    return []</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">3</td>
      <td rowspan="2">Arr 07 Kadanes Algorithm<br><br></b> <a href='https://leetcode.com/problems/maximum-subarray/' target='_blank'>LeetCode 53</a></td>
      <td rowspan="2"><b>Example 1:</b> Input: [-2,1,-3,4,-1,2,1,-5,4], Output: 6 ([4,-1,2,1])<br><br><b>Note (Constraint):</b> 1 &le; N &le; 10<sup>5</sup></td>
      <td><b>Time:</b> O(N<sup>2</sup>) (Trade-off)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>Negative Array Check:</b> Initialize `max_sum` with `INT_MIN` for arrays of all negative numbers.</td>
      <td><b>Explanation:</b> Check all possible subarrays and calculate their sum.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def max_sub_array_brute(nums: list[int]) -&gt; int:&#10;    maxi = float(&#x27;-inf&#x27;)&#10;    for i in range(len(nums)):&#10;        curr_sum = 0&#10;        for j in range(i, len(nums)):&#10;            curr_sum += nums[j]&#10;            maxi = max(maxi, curr_sum)&#10;    return maxi</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>Reset Logic:</b> If subarray becomes a net negative, extending it will only harm the sum.</td>
      <td><b>Explanation:</b> Kadane's: Maintain `curr_sum`. If `curr_sum` drops below zero, reset it. Track maximum.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def max_sub_array_optimal(nums: list[int]) -&gt; int:&#10;    maxi = float(&#x27;-inf&#x27;)&#10;    curr_sum = 0&#10;    for num in nums:&#10;        curr_sum += num&#10;        maxi = max(maxi, curr_sum)&#10;        if curr_sum &lt; 0: curr_sum = 0&#10;    return maxi</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">4</td>
      <td rowspan="2">Arr 08 Sort Colors<br><br></b> <a href='https://leetcode.com/problems/sort-colors/' target='_blank'>LeetCode 75</a></td>
      <td rowspan="2"><b>Example 1:</b> Input: nums = [2,0,2,1,1,0], Output: [0,0,1,1,2,2]<br><br><b>Note (Constraint):</b> 1 &le; N &le; 300</td>
      <td><b>Time:</b> O(2N) &cong; O(N) (Trade-off)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>Two Passes:</b> Forces a double iteration through the memory block.</td>
      <td><b>Explanation:</b> Count 0s, 1s, and 2s, then overwrite the array linearly.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def sort_colors_better(nums: list[int]) -&gt; None:&#10;    c0 = c1 = c2 = 0&#10;    for num in nums:&#10;        if num == 0: c0 += 1&#10;        elif num == 1: c1 += 1&#10;        else: c2 += 1&#10;    for i in range(c0): nums[i] = 0&#10;    for i in range(c0, c0+c1): nums[i] = 1&#10;    for i in range(c0+c1, len(nums)): nums[i] = 2</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1)</td>
      <td><code>std::swap</code></td>
      <td><b>Strict Single Pass:</b> Swaps values into correct zones in exactly N steps.</td>
      <td><b>Explanation:</b> Dutch National Flag Algorithm: 3 Pointers (low, mid, high) sorting in a single pass.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def sort_colors_optimal(nums: list[int]) -&gt; None:&#10;    low, mid, high = 0, 0, len(nums) - 1&#10;    while mid &lt;= high:&#10;        if nums[mid] == 0:&#10;            nums[low], nums[mid] = nums[mid], nums[low]&#10;            low += 1; mid += 1&#10;        elif nums[mid] == 1:&#10;            mid += 1&#10;        else:&#10;            nums[mid], nums[high] = nums[high], nums[mid]&#10;            high -= 1</code></pre></details></td>
    </tr>
  </tbody>
</table>
