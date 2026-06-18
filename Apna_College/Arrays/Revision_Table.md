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
      <td rowspan="2">Arr 01 Largest Element<br><br></b> <a href='https://www.geeksforgeeks.org/problems/largest-element-in-array/1' target='_blank'>GeeksforGeeks</a></td>
      <td rowspan="2"><b>Example 1:</b> Input: arr = [1, 8, 7, 56, 90], Output: 90<br><br><b>Note (Constraint):</b> 1 &le; N &le; 10<sup>5</sup></td>
      <td><b>Time:</b> O(N log N) (Trade-off)<br><b>Space:</b> O(1)</td>
      <td><code>std::sort</code> / <code>.sort()</code></td>
      <td>-</td>
      <td><b>Explanation:</b> Sort the array and return the last element.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def largest_element_brute(arr: list[int]) -&gt; int:&#10;    arr.sort()&#10;    return arr[-1]</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>Initialization:</b> Set max to `arr[0]` to handle negative arrays natively without relying on `INT_MIN`.</td>
      <td><b>Explanation:</b> Maintain a max variable and linearly scan the array updating it.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def largest_element_optimal(arr: list[int]) -&gt; int:&#10;    max_val = arr[0]&#10;    for i in range(1, len(arr)):&#10;        if arr[i] &gt; max_val:&#10;            max_val = arr[i]&#10;    return max_val</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">2</td>
      <td rowspan="2">Arr 04 Rotate Array<br><br></b> <a href='https://leetcode.com/problems/rotate-array/' target='_blank'>LeetCode 189</a></td>
      <td rowspan="2"><b>Example 1:</b> Input: nums = [1,2,3,4,5,6,7], k = 3, Output: [5,6,7,1,2,3,4]<br><br><b>Note (Constraint):</b> 1 &le; N &le; 10<sup>5</sup>, 0 &le; k &le; 10<sup>5</sup></td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(N) (Trade-off)</td>
      <td>Extra Space</td>
      <td><b>Modulus Magic:</b> `(i + k) % n` wraps the index around safely.</td>
      <td><b>Explanation:</b> Use an extra array to place elements at `(i + k) % N`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def rotate_brute(nums: list[int], k: int) -&gt; None:&#10;    n = len(nums)&#10;    k = k % n&#10;    temp = [0] * n&#10;    for i in range(n):&#10;        temp[(i + k) % n] = nums[i]&#10;    for i in range(n):&#10;        nums[i] = temp[i]</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><code>std::reverse</code></td>
      <td><b>`k > N` Handle:</b> `k = k % n` strictly required if `k` exceeds array length.</td>
      <td><b>Explanation:</b> Reverse parts of the array: Reverse full array, reverse first `k`, reverse rest.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def rotate_optimal(nums: list[int], k: int) -&gt; None:&#10;    n = len(nums)&#10;    k = k % n&#10;    nums.reverse()&#10;    nums[:k] = reversed(nums[:k])&#10;    nums[k:] = reversed(nums[k:])</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">3</td>
      <td rowspan="1">Arr 05 Move Zeros<br><br></b> <a href='https://leetcode.com/problems/move-zeroes/' target='_blank'>LeetCode 283</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: nums = [0,1,0,3,12], Output: [1,3,12,0,0]<br><br><b>Note (Constraint):</b> Must be done in-place.</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1)</td>
      <td><code>std::swap</code></td>
      <td><b>Swapping:</b> Natively handles cases where array has no zeros.</td>
      <td><b>Explanation:</b> Two-pointer approach. Swap non-zero elements with the `zero_pointer`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def move_zeroes(nums: list[int]) -&gt; None:&#10;    zero_idx = 0&#10;    for i in range(len(nums)):&#10;        if nums[i] != 0:&#10;            nums[zero_idx], nums[i] = nums[i], nums[zero_idx]&#10;            zero_idx += 1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">4</td>
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
  </tbody>
</table>
