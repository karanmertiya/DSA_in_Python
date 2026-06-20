# Step 04 Binary Search Revision Table

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
      <td>Bs 01 Binary Search<br><br></b> <a href="https://leetcode.com/problems/binary-search/" target="_blank">LeetCode 704</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: nums = [-1,0,3,5,9,12], target = 9, Output: 4</td>
      <td><b>Time:</b> O(log N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><b>Explanation:</b> Standard Iterative approach. Maintain `low` and `high` boundaries, shrinking the search space by half.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def search(nums: list[int], target: int) -&gt; int:&#10;    low, high = 0, len(nums) - 1&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        if nums[mid] == target:&#10;            return mid&#10;        elif nums[mid] &lt; target:&#10;            low = mid + 1&#10;        else:&#10;            high = mid - 1&#10;    return -1</code></pre></details></td>
    </tr>
    <tr>
      <td>2</td>
      <td>Bs 02 Lower Bound<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: arr = [1,2,8,10,11,12,19], target = 0, Output: 0</td>
      <td><b>Time:</b> O(log N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><b>Explanation:</b> When `nums[mid] >= target`, it is a potential answer. Store it and search left (`high = mid - 1`) for smaller potentials.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def lowerBound(arr: list[int], n: int, x: int) -&gt; int:&#10;    low, high = 0, n - 1&#10;    ans = n&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        if arr[mid] &gt;= x:&#10;            ans = mid&#10;            high = mid - 1&#10;        else:&#10;            low = mid + 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>3</td>
      <td>Bs 03 Find First And Last Position Of Element<br><br></b> <a href="https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/" target="_blank">LeetCode 34</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, SDE Sheet, Striver A Z</details></td>
      <td>**Example 1:** Input: nums = [5,7,7,8,8,10], target = 8, Output: [3,4]</td>
      <td><b>Time:</b> O(log N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><b>Explanation:</b> Run Binary Search twice. Once to find the first occurrence (bias left), once to find the last occurrence (bias right).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def searchRange(nums: list[int], target: int) -&gt; list[int]:&#10;    def findBound(isFirst):&#10;        low, high, ans = 0, len(nums) - 1, -1&#10;        while low &lt;= high:&#10;            mid = low + (high - low) // 2&#10;            if nums[mid] == target:&#10;                ans = mid&#10;                if isFirst: high = mid - 1&#10;                else: low = mid + 1&#10;            elif nums[mid] &lt; target:&#10;                low = mid + 1&#10;            else:&#10;                high = mid - 1&#10;        return ans&#10;    return [findBound(True), findBound(False)]</code></pre></details></td>
    </tr>
    <tr>
      <td>4</td>
      <td>Bs 04 Search In Rotated Sorted Array<br><br></b> <a href="https://leetcode.com/problems/search-in-rotated-sorted-array/" target="_blank">LeetCode 33</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, SDE Sheet, Striver A Z</details></td>
      <td>**Example 1:** Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4</td>
      <td><b>Time:</b> O(log N) (Constraint)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Identify the sorted half. Check if target lies within the boundaries of the sorted half. If yes, shrink to that half; else, shrink to the other.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def search(nums: list[int], target: int) -&gt; int:&#10;    low, high = 0, len(nums) - 1&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        if nums[mid] == target: return mid&#10;        &#10;        if nums[low] &lt;= nums[mid]:&#10;            if nums[low] &lt;= target &lt;= nums[mid]:&#10;                high = mid - 1&#10;            else:&#10;                low = mid + 1&#10;        else:&#10;            if nums[mid] &lt;= target &lt;= nums[high]:&#10;                low = mid + 1&#10;            else:&#10;                high = mid - 1&#10;    return -1</code></pre></details></td>
    </tr>
    <tr>
      <td>5</td>
      <td>Bs 05 Koko Eating Bananas<br><br></b> <a href="https://leetcode.com/problems/koko-eating-bananas/" target="_blank">LeetCode 875</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, SDE Sheet, Striver A Z</details></td>
      <td>**Example 1:** Input: piles = [3,6,7,11], h = 8, Output: 4<br><br>**Note (Constraint):** Binary Search on Answers.</td>
      <td><b>Time:</b> O(N log(Max(P))) (Constraint)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Search space is `1` to `max(piles)`. For a mid `k`, calculate hours required. If `hours <= h`, it's a valid answer, but search left for smaller `k`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import math&#10;def minEatingSpeed(piles: list[int], h: int) -&gt; int:&#10;    def canEat(k):&#10;        hours = sum(math.ceil(pile / k) for pile in piles)&#10;        return hours &lt;= h&#10;        &#10;    low, high = 1, max(piles)&#10;    ans = high&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        if canEat(mid):&#10;            ans = mid&#10;            high = mid - 1&#10;        else:&#10;            low = mid + 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>6</td>
      <td>Bs 06 Find Minimum In Rotated Sorted Array<br><br></b> <a href="https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/" target="_blank">LeetCode 153</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> SDE Sheet, Apna College, Love Babbar, Striver A Z</details></td>
      <td>**Example 1:** Input: nums = [3,4,5,1,2], Output: 1</td>
      <td><b>Time:</b> O(log N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Binary Search. Compare mid with right pointer. If nums[mid] > nums[right], the min is in the right half. Else, the min is in the left half including mid.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findMin(nums: List[int]) -&gt; int:&#10;    left, right = 0, len(nums) - 1&#10;    while left &lt; right:&#10;        mid = left + (right - left) // 2&#10;        if nums[mid] &gt; nums[right]: left = mid + 1&#10;        else: right = mid&#10;    return nums[left]</code></pre></details></td>
    </tr>
    <tr>
      <td>7</td>
      <td>Bs 07 Find Peak Element<br><br></b> <a href="https://leetcode.com/problems/find-peak-element/" target="_blank">LeetCode 162</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> SDE Sheet, Apna College, Love Babbar, Striver A Z</details></td>
      <td>**Example 1:** Input: nums = [1,2,3,1], Output: 2</td>
      <td><b>Time:</b> O(log N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Binary Search. If nums[mid] < nums[mid+1], we are on an ascending slope, so a peak must be to the right. Otherwise, we are on a descending slope, peak is to the left (including mid).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findPeakElement(nums: List[int]) -&gt; int:&#10;    left, right = 0, len(nums) - 1&#10;    while left &lt; right:&#10;        mid = left + (right - left) // 2&#10;        if nums[mid] &lt; nums[mid+1]: left = mid + 1&#10;        else: right = mid&#10;    return left</code></pre></details></td>
    </tr>
    <tr>
      <td>8</td>
      <td>Bs 08 Allocate Minimum Number Of Pages<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td>**Example 1:** Input: N=4, A=[12,34,67,90], M=2, Output: 113</td>
      <td><b>Time:</b> O(N * log(sum(A) - max(A)))<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Binary Search on Answer. The search space for pages is from `max(A)` to `sum(A)`. For a given `mid`, check if books can be allocated to `<= M` students without any student exceeding `mid` pages.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findPages(A: List[int], N: int, M: int) -&gt; int:&#10;    if M &gt; N: return -1&#10;    def isPossible(maxPages):&#10;        students, currentPages = 1, 0&#10;        for pages in A:&#10;            if pages &gt; maxPages: return False&#10;            if currentPages + pages &gt; maxPages:&#10;                students += 1&#10;                currentPages = pages&#10;            else:&#10;                currentPages += pages&#10;        return students &lt;= M&#10;    low, high = max(A), sum(A)&#10;    ans = -1&#10;    while low &lt;= high:&#10;        mid = (low + high) // 2&#10;        if isPossible(mid):&#10;            ans = mid; high = mid - 1&#10;        else: low = mid + 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>9</td>
      <td>Bs 09 Kth Element Of Two Sorted Arrays<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> SDE Sheet, Love Babbar, Striver A Z</details></td>
      <td>**Example 1:** Input: arr1 = [2, 3, 6, 7, 9], arr2 = [1, 4, 8, 10], k = 5, Output: 6</td>
      <td><b>Time:</b> O(log(min(n, m)))<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Binary search on the smaller array. Similar to Median of two sorted arrays, but the left partition size is strictly `k`. Search space for `cut1` is `[max(0, k-m), min(k, n)]`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def kthElement(arr1: List[int], arr2: List[int], n: int, m: int, k: int) -&gt; int:&#10;    if n &gt; m: return kthElement(arr2, arr1, m, n, k)&#10;    low, high = max(0, k - m), min(k, n)&#10;    while low &lt;= high:&#10;        cut1 = (low + high) // 2&#10;        cut2 = k - cut1&#10;        left1 = float(&#x27;-inf&#x27;) if cut1 == 0 else arr1[cut1-1]&#10;        left2 = float(&#x27;-inf&#x27;) if cut2 == 0 else arr2[cut2-1]&#10;        right1 = float(&#x27;inf&#x27;) if cut1 == n else arr1[cut1]&#10;        right2 = float(&#x27;inf&#x27;) if cut2 == m else arr2[cut2]&#10;        if left1 &lt;= right2 and left2 &lt;= right1: return max(left1, left2)&#10;        elif left1 &gt; right2: high = cut1 - 1&#10;        else: low = cut1 + 1&#10;    return 1</code></pre></details></td>
    </tr>
    <tr>
      <td>10</td>
      <td>Bs 10 Search In Rotated Sorted Array Ii<br><br></b> <a href="https://leetcode.com/problems/search-in-rotated-sorted-array-ii/" target="_blank">LeetCode 81</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td>**Example 1:** Input: nums = [2,5,6,0,0,1,2], target = 0, Output: true</td>
      <td><b>Time:</b> O(log N) average, O(N) worst case<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> If `nums[low] == nums[mid] == nums[high]`, shrink the search space by `low++` and `high--`. Otherwise, proceed with the standard rotated binary search.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def search(nums: List[int], target: int) -&gt; bool:&#10;    low, high = 0, len(nums) - 1&#10;    while low &lt;= high:&#10;        mid = (low + high) // 2&#10;        if nums[mid] == target: return True&#10;        if nums[low] == nums[mid] == nums[high]:&#10;            low += 1; high -= 1; continue&#10;        if nums[low] &lt;= nums[mid]:&#10;            if nums[low] &lt;= target &lt;= nums[mid]: high = mid - 1&#10;            else: low = mid + 1&#10;        else:&#10;            if nums[mid] &lt;= target &lt;= nums[high]: low = mid + 1&#10;            else: high = mid - 1&#10;    return False</code></pre></details></td>
    </tr>
    <tr>
      <td>11</td>
      <td>Bs 11 Minimum Days To Make M Bouquets<br><br></b> <a href="https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/" target="_blank">LeetCode 1482</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td>**Example 1:** Find day threshold.</td>
      <td><b>Time:</b> O(N log(maxD - minD))<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Binary search on days from `min(bloom)` to `max(bloom)`. Count consecutive bloomed flowers, if it reaches `k`, form a bouquet. Return minimum valid day.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minDays(bloomDay: List[int], m: int, k: int) -&gt; int:&#10;    if m * k &gt; len(bloomDay): return -1&#10;    def isPossible(day):&#10;        count, bouquets = 0, 0&#10;        for d in bloomDay:&#10;            if d &lt;= day: count += 1&#10;            else: bouquets += count // k; count = 0&#10;        bouquets += count // k&#10;        return bouquets &gt;= m&#10;    low, high = min(bloomDay), max(bloomDay)&#10;    ans = -1&#10;    while low &lt;= high:&#10;        mid = (low + high) // 2&#10;        if isPossible(mid): ans = mid; high = mid - 1&#10;        else: low = mid + 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>12</td>
      <td>Bs 12 Find The Smallest Divisor Given A Threshold<br><br></b> <a href="https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/" target="_blank">LeetCode 1283</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td>**Example 1:** Summing ceils.</td>
      <td><b>Time:</b> O(N log(max(nums)))<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Binary search the divisor from 1 to `max(nums)`. Compute `sum(ceil(num / mid))`. If sum <= threshold, shrink high.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import math&#10;def smallestDivisor(nums: List[int], threshold: int) -&gt; int:&#10;    low, high = 1, max(nums)&#10;    while low &lt;= high:&#10;        mid = (low + high) // 2&#10;        total = sum(math.ceil(num / mid) for num in nums)&#10;        if total &lt;= threshold: high = mid - 1&#10;        else: low = mid + 1&#10;    return low</code></pre></details></td>
    </tr>
    <tr>
      <td>13</td>
      <td>Bs 13 Capacity To Ship Packages Within D Days<br><br></b> <a href="https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/" target="_blank">LeetCode 1011</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td>**Example 1:** Find ship capacity.</td>
      <td><b>Time:</b> O(N log(sum - max))<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Binary search on capacity. Low = `max(weights)`, High = `sum(weights)`. Iterate through packages and accumulate weight, increment day if limit is exceeded.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def shipWithinDays(weights: List[int], days: int) -&gt; int:&#10;    def canShip(cap):&#10;        d, load = 1, 0&#10;        for w in weights:&#10;            if load + w &gt; cap: d += 1; load = w&#10;            else: load += w&#10;        return d &lt;= days&#10;    low, high = max(weights), sum(weights)&#10;    while low &lt;= high:&#10;        mid = (low + high) // 2&#10;        if canShip(mid): high = mid - 1&#10;        else: low = mid + 1&#10;    return low</code></pre></details></td>
    </tr>
    <tr>
      <td>14</td>
      <td>Bs 14 Kth Missing Positive Number<br><br></b> <a href="https://leetcode.com/problems/kth-missing-positive-number/" target="_blank">LeetCode 1539</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td>**Example 1:** Calculate missing.</td>
      <td><b>Time:</b> O(log N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Binary search. At index `mid`, the number of missing elements before `arr[mid]` is `arr[mid] - (mid + 1)`. If this is < `k`, search right `low = mid + 1`. Else search left `high = mid - 1`. Ans is `high + 1 + k` or `low + k`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findKthPositive(arr: List[int], k: int) -&gt; int:&#10;    low, high = 0, len(arr) - 1&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        missing = arr[mid] - (mid + 1)&#10;        if missing &lt; k: low = mid + 1&#10;        else: high = mid - 1&#10;    return low + k</code></pre></details></td>
    </tr>
    <tr>
      <td>15</td>
      <td>Bs 15 Aggressive Cows<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/aggressive-cows/0" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td>**Example 1:** Minimax binary search.</td>
      <td><b>Time:</b> O(N log N + N log(Max-Min))<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Sort the stalls. Binary search for distance from `1` to `max-min`. For a distance `mid`, check if we can place all `C` cows such that distance between any two is >= `mid`. If possible, move `low = mid + 1` to maximize it, else `high = mid - 1`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def aggressiveCows(stalls: List[int], k: int) -&gt; int:&#10;    stalls.sort()&#10;    def can_place(dist):&#10;        cnt_cows = 1&#10;        last = stalls[0]&#10;        for i in range(1, len(stalls)):&#10;            if stalls[i] - last &gt;= dist:&#10;                cnt_cows += 1&#10;                last = stalls[i]&#10;        return cnt_cows &gt;= k&#10;    low, high = 1, stalls[-1] - stalls[0]&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        if can_place(mid): low = mid + 1&#10;        else: high = mid - 1&#10;    return high</code></pre></details></td>
    </tr>
    <tr>
      <td>16</td>
      <td>Bs 16 Split Array Largest Sum<br><br></b> <a href="https://leetcode.com/problems/split-array-largest-sum/" target="_blank">LeetCode 410</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td>**Example 1:** Equivalent to allocate books.</td>
      <td><b>Time:</b> O(N log(Sum-Max))<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Identical logic to Allocate Books. Binary search from `max(nums)` to `sum(nums)`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def splitArray(nums: List[int], k: int) -&gt; int:&#10;    def count_partitions(max_sum):&#10;        partitions, subarray_sum = 1, 0&#10;        for num in nums:&#10;            if subarray_sum + num &lt;= max_sum:&#10;                subarray_sum += num&#10;            else:&#10;                partitions += 1&#10;                subarray_sum = num&#10;        return partitions&#10;    low, high = max(nums), sum(nums)&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        if count_partitions(mid) &gt; k: low = mid + 1&#10;        else: high = mid - 1&#10;    return low</code></pre></details></td>
    </tr>
    <tr>
      <td>17</td>
      <td>Bs 17 Painters Partition Problem<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/the-painters-partition-problem1535/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td>**Example 1:** Minimax identical to book allocation.</td>
      <td><b>Time:</b> O(N log(Sum-Max))<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Identical to Allocate Books and Split Array Largest Sum. Binary search `max(boards)` to `sum(boards)`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findLargestMinDistance(boards: List[int], k: int) -&gt; int:&#10;    def count_painters(time):&#10;        painters, boards_painter = 1, 0&#10;        for b in boards:&#10;            if boards_painter + b &lt;= time:&#10;                boards_painter += b&#10;            else:&#10;                painters += 1&#10;                boards_painter = b&#10;        return painters&#10;    low, high = max(boards), sum(boards)&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        if count_painters(mid) &gt; k: low = mid + 1&#10;        else: high = mid - 1&#10;    return low</code></pre></details></td>
    </tr>
    <tr>
      <td>18</td>
      <td>Bs 18 Minimize Max Distance To Gas Station<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/minimize-max-distance-to-gas-station/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td>**Example 1:** Double binary search.</td>
      <td><b>Time:</b> O(N log(MaxDist / 1e-6))<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Binary search on the real answer (distance) with a precision (e.g., 1e-6). For a given `mid` distance, count how many gas stations need to be inserted in each gap: `ceil((stations[i+1] - stations[i]) / mid) - 1`. If total needed > k, `low = mid`, else `high = mid`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findSmallestMaxDist(stations: List[int], k: int) -&gt; float:&#10;    def num_required(dist):&#10;        cnt = 0&#10;        for i in range(1, len(stations)):&#10;            number_in_between = int((stations[i] - stations[i-1]) / dist)&#10;            if (stations[i] - stations[i-1]) == (dist * number_in_between):&#10;                number_in_between -= 1&#10;            cnt += number_in_between&#10;        return cnt&#10;    low, high = 0, 0&#10;    for i in range(len(stations) - 1):&#10;        high = max(high, float(stations[i+1] - stations[i]))&#10;    diff = 1e-6&#10;    while high - low &gt; diff:&#10;        mid = low + (high - low) / 2.0&#10;        if num_required(mid) &gt; k: low = mid&#10;        else: high = mid&#10;    return high</code></pre></details></td>
    </tr>
    <tr>
      <td>19</td>
      <td>Bs 19 Search In A 2D Matrix Ii<br><br></b> <a href="https://leetcode.com/problems/search-a-2d-matrix-ii/" target="_blank">LeetCode 240</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td>**Example 1:** Start from top right.</td>
      <td><b>Time:</b> O(N + M)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Start from the top-right corner. If `target == current`, return true. If `target < current`, move left (`c--`). If `target > current`, move down (`r++`).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def searchMatrix(matrix: List[List[int]], target: int) -&gt; bool:&#10;    r, c = 0, len(matrix[0]) - 1&#10;    while r &lt; len(matrix) and c &gt;= 0:&#10;        if matrix[r][c] == target: return True&#10;        elif matrix[r][c] &gt; target: c -= 1&#10;        else: r += 1&#10;    return False</code></pre></details></td>
    </tr>
    <tr>
      <td>20</td>
      <td>Bs 20 Find A Peak Element Ii<br><br></b> <a href="https://leetcode.com/problems/find-a-peak-element-ii/" target="_blank">LeetCode 1901</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td>**Example 1:** Binary search on columns.</td>
      <td><b>Time:</b> O(N log M)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Binary search on columns. Find middle column, find max element in this column. Compare it with its left and right neighbors. If it's > both, it's a peak. If left is greater, peak exists in left half. Else, peak exists in right half.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findPeakGrid(mat: List[List[int]]) -&gt; List[int]:&#10;    n, m = len(mat), len(mat[0])&#10;    low, high = 0, m - 1&#10;    while low &lt;= high:&#10;        mid = (low + high) // 2&#10;        max_row = 0&#10;        for i in range(n):&#10;            if mat[i][mid] &gt; mat[max_row][mid]: max_row = i&#10;        left = mat[max_row][mid-1] if mid - 1 &gt;= 0 else -1&#10;        right = mat[max_row][mid+1] if mid + 1 &lt; m else -1&#10;        if mat[max_row][mid] &gt; left and mat[max_row][mid] &gt; right:&#10;            return [max_row, mid]&#10;        elif mat[max_row][mid] &lt; left:&#10;            high = mid - 1&#10;        else:&#10;            low = mid + 1&#10;    return [-1, -1]</code></pre></details></td>
    </tr>
    <tr>
      <td>21</td>
      <td>Bs 21 Matrix Median<br><br></b> <a href="https://www.interviewbit.com/problems/matrix-median/" target="_blank">InterviewBit</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td>**Example 1:** Binary search on answer range.</td>
      <td><b>Time:</b> O(32 * N log M)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Binary search on the value range `[1, 10^9]`. For a candidate `mid`, count how many numbers are `<= mid` across all rows using `upper_bound`. If count `> (N*M)/2`, `mid` could be median, search lower. Else search higher.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import bisect&#10;def findMedian(A: List[List[int]]) -&gt; int:&#10;    low, high = 1, int(1e9)&#10;    n, m = len(A), len(A[0])&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        cnt = sum(bisect.bisect_right(row, mid) for row in A)&#10;        if cnt &lt;= (n * m) // 2:&#10;            low = mid + 1&#10;        else:&#10;            high = mid - 1&#10;    return low</code></pre></details></td>
    </tr>
    <tr>
      <td>22</td>
      <td>Bs 22 Kth Smallest Number In Multiplication Table<br><br></b> <a href="https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/" target="_blank">LeetCode 668</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td>**Example 1:** Binary Search on answer.</td>
      <td><b>Time:</b> O(m * log(m*n))<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Binary search on range `[1, m*n]`. For a value `mid`, the number of elements `<= mid` in row `i` is `min(mid / i, n)`. Sum this for all rows to get total count. If count >= k, search left. Else search right.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findKthNumber(m: int, n: int, k: int) -&gt; int:&#10;    low, high = 1, m * n&#10;    while low &lt; high:&#10;        mid = low + (high - low) // 2&#10;        count = sum(min(mid // i, n) for i in range(1, m + 1))&#10;        if count &gt;= k:&#10;            high = mid&#10;        else:&#10;            low = mid + 1&#10;    return low</code></pre></details></td>
    </tr>
    <tr>
      <td>23</td>
      <td>Bs 23 Find K Th Smallest Pair Distance<br><br></b> <a href="https://leetcode.com/problems/find-k-th-smallest-pair-distance/" target="_blank">LeetCode 719</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td>**Example 1:** Sort and binary search on distance.</td>
      <td><b>Time:</b> O(N log N + N log(max_dist))<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Sort array. Binary search on distance `[0, nums.back() - nums.front()]`. For a candidate `mid`, count pairs with distance `<= mid` using a sliding window. If count >= k, search left. Else search right.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def smallestDistancePair(nums: List[int], k: int) -&gt; int:&#10;    nums.sort()&#10;    low, high = 0, nums[-1] - nums[0]&#10;    def countPairs(mid):&#10;        count, l = 0, 0&#10;        for r in range(len(nums)):&#10;            while nums[r] - nums[l] &gt; mid: l += 1&#10;            count += (r - l)&#10;        return count&#10;    while low &lt; high:&#10;        mid = low + (high - low) // 2&#10;        if countPairs(mid) &gt;= k:&#10;            high = mid&#10;        else:&#10;            low = mid + 1&#10;    return low</code></pre></details></td>
    </tr>
    <tr>
      <td>24</td>
      <td>Bs 24 Majority Element<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/majority-element-1587115620/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z, SDE Sheet</details></td>
      <td>**Example 1:** Moore's Voting Algorithm.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Use Moore's Voting Algorithm to find a candidate for majority element. Then count the occurrences of the candidate in the array to verify if it appears more than N/2 times.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def majorityElement(a, size):&#10;    count = 0&#10;    candidate = -1&#10;    for num in a:&#10;        if count == 0:&#10;            candidate = num&#10;            count = 1&#10;        elif num == candidate: count += 1&#10;        else: count -= 1&#10;    count = 0&#10;    for num in a:&#10;        if num == candidate: count += 1&#10;    return candidate if count &gt; size // 2 else -1</code></pre></details></td>
    </tr>
    <tr>
      <td>25</td>
      <td>Bs 25 Find Four Elements That Sum To A Given Value<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/find-all-four-sum-numbers1732/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z, SDE Sheet</details></td>
      <td>**Example 1:** Two loops and two pointers.</td>
      <td><b>Time:</b> O(N^3)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Sort the array. Use two nested loops for the first two elements. Then use two pointers for the remaining two elements to find the target sum. Skip duplicates at all levels.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def fourSum(arr, k):&#10;    ans = []&#10;    n = len(arr)&#10;    arr.sort()&#10;    for i in range(n):&#10;        if i &gt; 0 and arr[i] == arr[i-1]: continue&#10;        for j in range(i + 1, n):&#10;            if j &gt; i + 1 and arr[j] == arr[j-1]: continue&#10;            left, right = j + 1, n - 1&#10;            while left &lt; right:&#10;                total = arr[i] + arr[j] + arr[left] + arr[right]&#10;                if total == k:&#10;                    ans.append([arr[i], arr[j], arr[left], arr[right]])&#10;                    left += 1; right -= 1&#10;                    while left &lt; right and arr[left] == arr[left-1]: left += 1&#10;                    while left &lt; right and arr[right] == arr[right+1]: right -= 1&#10;                elif total &lt; k: left += 1&#10;                else: right -= 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>26</td>
      <td>Bs 26 Find Nth Root Of M<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/find-nth-root-of-m5843/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, SDE Sheet</details></td>
      <td>**Example 1:** Binary Search.</td>
      <td><b>Time:</b> O(N * log M)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Search space is `[1, m]`. Check `mid^n`. Since `mid^n` can overflow, use a custom power function that returns 1 if `mid^n == m`, 0 if `< m`, and 2 if `> m`. Adjust `low` and `high` accordingly.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def NthRoot(n, m):&#10;    def func(mid, n, m):&#10;        ans = 1&#10;        for _ in range(n):&#10;            ans *= mid&#10;            if ans &gt; m: return 2&#10;        if ans == m: return 1&#10;        return 0&#10;    low, high = 1, m&#10;    while low &lt;= high:&#10;        mid = (low + high) // 2&#10;        midN = func(mid, n, m)&#10;        if midN == 1: return mid&#10;        elif midN == 0: low = mid + 1&#10;        else: high = mid - 1&#10;    return -1</code></pre></details></td>
    </tr>
    <tr>
      <td>27</td>
      <td>Bs 27 Row With Max 1S<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/row-with-max-1s0023/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td>**Example 1:** Lower Bound per row.</td>
      <td><b>Time:</b> O(N log M)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Since rows are sorted, use binary search (`lower_bound` of 1) to find the first index of 1 in each row. The number of 1s is `m - index`. Keep track of the row with the maximum 1s.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def rowWithMax1s(arr, n, m):&#10;    def lowerBound(a, m, x):&#10;        low, high, ans = 0, m - 1, m&#10;        while low &lt;= high:&#10;            mid = (low + high) // 2&#10;            if a[mid] &gt;= x:&#10;                ans = mid&#10;                high = mid - 1&#10;            else:&#10;                low = mid + 1&#10;        return ans&#10;    max_cnt = 0&#10;    index = -1&#10;    for i in range(n):&#10;        cnt_ones = m - lowerBound(arr[i], m, 1)&#10;        if cnt_ones &gt; max_cnt:&#10;            max_cnt = cnt_ones&#10;            index = i&#10;    return index</code></pre></details></td>
    </tr>
  </tbody>
</table>
