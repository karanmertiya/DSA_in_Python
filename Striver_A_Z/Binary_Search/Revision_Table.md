# Binary Search Revision Table

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
      <td rowspan="1">Bs 01 Binary Search<br><br></b> <a href='https://leetcode.com/problems/binary-search/' target='_blank'>LeetCode 704</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: nums = [-1,0,3,5,9,12], target = 9, Output: 4<br><br><b>Note (Constraint):</b> 1 &le; N &le; 10<sup>4</sup></td>
      <td><b>Time:</b> O(log N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td>-</td>
      <td><b>Mid Overflow:</b> Calculate mid as `low + (high - low) / 2` to prevent integer overflow for large arrays.</td>
      <td><b>Explanation:</b> Compare target with the middle element. If smaller, search the left half. If larger, search the right half.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def search(nums: list[int], target: int) -&gt; int:&#10;    low, high = 0, len(nums) - 1&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        if nums[mid] == target: return mid&#10;        elif nums[mid] &lt; target: low = mid + 1&#10;        else: high = mid - 1&#10;    return -1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">2</td>
      <td rowspan="1">Bs 02 Lower Bound And Upper Bound<br><br></b> <a href='https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/' target='_blank'>LeetCode 34</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: nums = [5,7,7,8,8,10], target = 8, Output: [3,4]<br><br><b>Note (Constraint):</b> Must be `O(log N)`.</td>
      <td><b>Time:</b> O(log N) (Constraint)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>Biasing:</b> If `nums[mid] == target`, don't return. Record the index and continue searching left (for lower) or right (for upper).</td>
      <td><b>Explanation:</b> Perform two separate binary searches: one for the first occurrence (bias left) and one for the last (bias right).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def search_range(nums: list[int], target: int) -&gt; list[int]:&#10;    def find_bound(is_first):&#10;        low, high, res = 0, len(nums) - 1, -1&#10;        while low &lt;= high:&#10;            mid = low + (high - low) // 2&#10;            if nums[mid] == target:&#10;                res = mid&#10;                if is_first: high = mid - 1&#10;                else: low = mid + 1&#10;            elif nums[mid] &lt; target: low = mid + 1&#10;            else: high = mid - 1&#10;        return res&#10;    return [find_bound(True), find_bound(False)]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">3</td>
      <td rowspan="1">Bs 03 Search In Rotated Sorted Array<br><br></b> <a href='https://leetcode.com/problems/search-in-rotated-sorted-array/' target='_blank'>LeetCode 33</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4<br><br><b>Note (Constraint):</b> Array has distinct values.</td>
      <td><b>Time:</b> O(log N) (Constraint)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>Half Isolation:</b> One half of a rotated array is *always* perfectly sorted. Identify it using `nums[low] <= nums[mid]`.</td>
      <td><b>Explanation:</b> Identify which half of the array is strictly sorted. Then check if the target lies within that sorted half.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def search_rotated(nums: list[int], target: int) -&gt; int:&#10;    low, high = 0, len(nums) - 1&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        if nums[mid] == target: return mid&#10;        &#10;        if nums[low] &lt;= nums[mid]:&#10;            if nums[low] &lt;= target &lt;= nums[mid]: high = mid - 1&#10;            else: low = mid + 1&#10;        else:&#10;            if nums[mid] &lt;= target &lt;= nums[high]: low = mid + 1&#10;            else: high = mid - 1&#10;    return -1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">4</td>
      <td rowspan="1">Bs 04 Binary Search On Answers Koko Eating Bananas<br><br></b> <a href='https://leetcode.com/problems/koko-eating-bananas/' target='_blank'>LeetCode 875</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: piles = [3,6,7,11], h = 8, Output: 4<br><br><b>Note (Constraint):</b> Binary Search on Answers.</td>
      <td><b>Time:</b> O(N log(Max(Pile))) (Constraint)<br><b>Space:</b> O(1)</td>
      <td><code>std::ceil</code> / <code>math.ceil</code></td>
      <td><b>Answer Range:</b> The minimum speed is 1, and the maximum speed needed is the largest pile size (which finishes every pile in 1 hour).</td>
      <td><b>Explanation:</b> Search space is `1` to `max(piles)`. Calculate total hours for `mid`. If possible, try a slower speed (left half).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import math&#10;def min_eating_speed(piles: list[int], h: int) -&gt; int:&#10;    def can_eat(speed):&#10;        hours = 0&#10;        for p in piles:&#10;            hours += math.ceil(p / speed)&#10;        return hours &lt;= h&#10;        &#10;    low, high = 1, max(piles)&#10;    ans = high&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        if can_eat(mid):&#10;            ans = mid&#10;            high = mid - 1&#10;        else:&#10;            low = mid + 1&#10;    return ans</code></pre></details></td>
    </tr>
  </tbody>
</table>
