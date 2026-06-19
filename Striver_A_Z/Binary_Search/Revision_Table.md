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
      <td>1</td>
      <td>Bs 01 Binary Search<br><br></b> <a href='https://leetcode.com/problems/binary-search/' target='_blank'>LeetCode 704</a></td>
      <td><b>Example 1:</b> Input: nums = [-1,0,3,5,9,12], target = 9, Output: 4</td>
      <td><b>Time:</b> O(log N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td>-</td>
      <td><b>Mid Overflow:</b> Use `mid = low + (high - low) / 2` to avoid integer overflow if boundaries are large.</td>
      <td><b>Explanation:</b> Standard Iterative approach. Maintain `low` and `high` boundaries, shrinking the search space by half.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def search(nums: list[int], target: int) -&gt; int:&#10;    low, high = 0, len(nums) - 1&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        if nums[mid] == target:&#10;            return mid&#10;        elif nums[mid] &lt; target:&#10;            low = mid + 1&#10;        else:&#10;            high = mid - 1&#10;    return -1</code></pre></details></td>
    </tr>
    <tr>
      <td>2</td>
      <td>Bs 02 Lower Bound<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Input: arr = [1,2,8,10,11,12,19], target = 0, Output: 0</td>
      <td><b>Time:</b> O(log N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><code>std::lower_bound</code> internal alternative</td>
      <td><b>Not Found:</b> If all elements are smaller, `ans` stays `N`.</td>
      <td><b>Explanation:</b> When `nums[mid] >= target`, it is a potential answer. Store it and search left (`high = mid - 1`) for smaller potentials.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def lowerBound(arr: list[int], n: int, x: int) -&gt; int:&#10;    low, high = 0, n - 1&#10;    ans = n&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        if arr[mid] &gt;= x:&#10;            ans = mid&#10;            high = mid - 1&#10;        else:&#10;            low = mid + 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>3</td>
      <td>Bs 03 Find First And Last Position Of Element<br><br></b> <a href='https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/' target='_blank'>LeetCode 34</a></td>
      <td><b>Example 1:</b> Input: nums = [5,7,7,8,8,10], target = 8, Output: [3,4]</td>
      <td><b>Time:</b> O(log N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td>-</td>
      <td><b>Empty Array:</b> Naturally skips loop and returns `[-1, -1]`.</td>
      <td><b>Explanation:</b> Run Binary Search twice. Once to find the first occurrence (bias left), once to find the last occurrence (bias right).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def searchRange(nums: list[int], target: int) -&gt; list[int]:&#10;    def findBound(isFirst):&#10;        low, high, ans = 0, len(nums) - 1, -1&#10;        while low &lt;= high:&#10;            mid = low + (high - low) // 2&#10;            if nums[mid] == target:&#10;                ans = mid&#10;                if isFirst: high = mid - 1&#10;                else: low = mid + 1&#10;            elif nums[mid] &lt; target:&#10;                low = mid + 1&#10;            else:&#10;                high = mid - 1&#10;        return ans&#10;    return [findBound(True), findBound(False)]</code></pre></details></td>
    </tr>
    <tr>
      <td>4</td>
      <td>Bs 04 Search In Rotated Sorted Array<br><br></b> <a href='https://leetcode.com/problems/search-in-rotated-sorted-array/' target='_blank'>LeetCode 33</a></td>
      <td><b>Example 1:</b> Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4</td>
      <td><b>Time:</b> O(log N) (Constraint)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>Duplicate Values:</b> If duplicates existed (which they don't in this specific leetcode), we would need to handle `nums[low] == nums[mid] == nums[high]` by shrinking bounds.</td>
      <td><b>Explanation:</b> Identify the sorted half. Check if target lies within the boundaries of the sorted half. If yes, shrink to that half; else, shrink to the other.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def search(nums: list[int], target: int) -&gt; int:&#10;    low, high = 0, len(nums) - 1&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        if nums[mid] == target: return mid&#10;        &#10;        if nums[low] &lt;= nums[mid]:&#10;            if nums[low] &lt;= target &lt;= nums[mid]:&#10;                high = mid - 1&#10;            else:&#10;                low = mid + 1&#10;        else:&#10;            if nums[mid] &lt;= target &lt;= nums[high]:&#10;                low = mid + 1&#10;            else:&#10;                high = mid - 1&#10;    return -1</code></pre></details></td>
    </tr>
    <tr>
      <td>5</td>
      <td>Bs 05 Koko Eating Bananas<br><br></b> <a href='https://leetcode.com/problems/koko-eating-bananas/' target='_blank'>LeetCode 875</a></td>
      <td><b>Example 1:</b> Input: piles = [3,6,7,11], h = 8, Output: 4<br><br><b>Note (Constraint):</b> Binary Search on Answers.</td>
      <td><b>Time:</b> O(N log(Max(P))) (Constraint)<br><b>Space:</b> O(1)</td>
      <td><code>std::ceil</code> / ceiling math</td>
      <td><b>Ceiling Math:</b> Use `(pile + mid - 1) / mid` to simulate ceiling division without float casting overhead.</td>
      <td><b>Explanation:</b> Search space is `1` to `max(piles)`. For a mid `k`, calculate hours required. If `hours <= h`, it's a valid answer, but search left for smaller `k`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import math&#10;def minEatingSpeed(piles: list[int], h: int) -&gt; int:&#10;    def canEat(k):&#10;        hours = sum(math.ceil(pile / k) for pile in piles)&#10;        return hours &lt;= h&#10;        &#10;    low, high = 1, max(piles)&#10;    ans = high&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        if canEat(mid):&#10;            ans = mid&#10;            high = mid - 1&#10;        else:&#10;            low = mid + 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>6</td>
      <td>Bs 06 Find Minimum In Rotated Sorted Array<br><br></b> <a href='https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/' target='_blank'>LeetCode 153</a></td>
      <td><b>Example 1:</b> Input: nums = [3,4,5,1,2], Output: 1</td>
      <td><b>Time:</b> O(log N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>Fully sorted array:</b> Loop naturally converges to the first element.</td>
      <td><b>Explanation:</b> Binary Search. Compare mid with right pointer. If nums[mid] > nums[right], the min is in the right half. Else, the min is in the left half including mid.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findMin(nums: List[int]) -&gt; int:&#10;    left, right = 0, len(nums) - 1&#10;    while left &lt; right:&#10;        mid = left + (right - left) // 2&#10;        if nums[mid] &gt; nums[right]: left = mid + 1&#10;        else: right = mid&#10;    return nums[left]</code></pre></details></td>
    </tr>
    <tr>
      <td>7</td>
      <td>Bs 07 Find Peak Element<br><br></b> <a href='https://leetcode.com/problems/find-peak-element/' target='_blank'>LeetCode 162</a></td>
      <td><b>Example 1:</b> Input: nums = [1,2,3,1], Output: 2</td>
      <td><b>Time:</b> O(log N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>Peak at boundaries:</b> The binary search logic intrinsically handles edges by shrinking bounds away from negative slopes.</td>
      <td><b>Explanation:</b> Binary Search. If nums[mid] < nums[mid+1], we are on an ascending slope, so a peak must be to the right. Otherwise, we are on a descending slope, peak is to the left (including mid).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findPeakElement(nums: List[int]) -&gt; int:&#10;    left, right = 0, len(nums) - 1&#10;    while left &lt; right:&#10;        mid = left + (right - left) // 2&#10;        if nums[mid] &lt; nums[mid+1]: left = mid + 1&#10;        else: right = mid&#10;    return left</code></pre></details></td>
    </tr>
    <tr>
      <td>8</td>
      <td>Bs 08 Search A 2D Matrix<br><br></b> <a href='https://leetcode.com/problems/search-a-2d-matrix/' target='_blank'>LeetCode 74</a></td>
      <td><b>Example 1:</b> Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3, Output: true</td>
      <td><b>Time:</b> O(log(M * N))<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Treat the 2D matrix as a 1D flattened array. The element at `index` is at `matrix[index / cols][index % cols]`. Perform standard binary search.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def searchMatrix(matrix: List[List[int]], target: int) -&gt; bool:&#10;    if not matrix or not matrix[0]: return False&#10;    m, n = len(matrix), len(matrix[0])&#10;    left, right = 0, m * n - 1&#10;    while left &lt;= right:&#10;        mid = left + (right - left) // 2&#10;        val = matrix[mid // n][mid % n]&#10;        if val == target: return True&#10;        if val &lt; target: left = mid + 1&#10;        else: right = mid - 1&#10;    return False</code></pre></details></td>
    </tr>
    <tr>
      <td>9</td>
      <td>Bs 07 Median Of Two Sorted Arrays<br><br></b> <a href='https://leetcode.com/problems/median-of-two-sorted-arrays/' target='_blank'>LeetCode 4</a></td>
      <td><b>Example 1:</b> Input: nums1 = [1,3], nums2 = [2], Output: 2.00000</td>
      <td><b>Time:</b> O(log(min(m, n)))<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>Different sizes / One empty:</b> Always binary search on the smaller array to avoid out-of-bounds.</td>
      <td><b>Explanation:</b> Binary Search on the smaller array. Partition both arrays such that the left half has `(m+n+1)/2` elements. Find the valid partition where `max(left1) <= min(right2)` and `max(left2) <= min(right1)`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -&gt; float:&#10;    if len(nums1) &gt; len(nums2): return self.findMedianSortedArrays(nums2, nums1)&#10;    n1, n2 = len(nums1), len(nums2)&#10;    low, high = 0, n1&#10;    while low &lt;= high:&#10;        cut1 = (low + high) // 2&#10;        cut2 = (n1 + n2 + 1) // 2 - cut1&#10;        left1 = float(&#x27;-inf&#x27;) if cut1 == 0 else nums1[cut1 - 1]&#10;        left2 = float(&#x27;-inf&#x27;) if cut2 == 0 else nums2[cut2 - 1]&#10;        right1 = float(&#x27;inf&#x27;) if cut1 == n1 else nums1[cut1]&#10;        right2 = float(&#x27;inf&#x27;) if cut2 == n2 else nums2[cut2]&#10;        if left1 &lt;= right2 and left2 &lt;= right1:&#10;            if (n1 + n2) % 2 == 0:&#10;                return (max(left1, left2) + min(right1, right2)) / 2.0&#10;            else:&#10;                return max(left1, left2)&#10;        elif left1 &gt; right2:&#10;            high = cut1 - 1&#10;        else:&#10;            low = cut1 + 1&#10;    return 0.0</code></pre></details></td>
    </tr>
    <tr>
      <td>10</td>
      <td>Bs 08 Allocate Minimum Number Of Pages<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Input: N=4, A=[12,34,67,90], M=2, Output: 113</td>
      <td><b>Time:</b> O(N * log(sum(A) - max(A)))<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>M > N:</b> Impossible to allocate at least one book to each student, return -1.</td>
      <td><b>Explanation:</b> Binary Search on Answer. The search space for pages is from `max(A)` to `sum(A)`. For a given `mid`, check if books can be allocated to `<= M` students without any student exceeding `mid` pages.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findPages(A: List[int], N: int, M: int) -&gt; int:&#10;    if M &gt; N: return -1&#10;    def isPossible(maxPages):&#10;        students, currentPages = 1, 0&#10;        for pages in A:&#10;            if pages &gt; maxPages: return False&#10;            if currentPages + pages &gt; maxPages:&#10;                students += 1&#10;                currentPages = pages&#10;            else:&#10;                currentPages += pages&#10;        return students &lt;= M&#10;    low, high = max(A), sum(A)&#10;    ans = -1&#10;    while low &lt;= high:&#10;        mid = (low + high) // 2&#10;        if isPossible(mid):&#10;            ans = mid; high = mid - 1&#10;        else: low = mid + 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>11</td>
      <td>Bs 10 Kth Element Of Two Sorted Arrays<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Input: arr1 = [2, 3, 6, 7, 9], arr2 = [1, 4, 8, 10], k = 5, Output: 6</td>
      <td><b>Time:</b> O(log(min(n, m)))<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Binary search on the smaller array. Similar to Median of two sorted arrays, but the left partition size is strictly `k`. Search space for `cut1` is `[max(0, k-m), min(k, n)]`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def kthElement(arr1: List[int], arr2: List[int], n: int, m: int, k: int) -&gt; int:&#10;    if n &gt; m: return kthElement(arr2, arr1, m, n, k)&#10;    low, high = max(0, k - m), min(k, n)&#10;    while low &lt;= high:&#10;        cut1 = (low + high) // 2&#10;        cut2 = k - cut1&#10;        left1 = float(&#x27;-inf&#x27;) if cut1 == 0 else arr1[cut1-1]&#10;        left2 = float(&#x27;-inf&#x27;) if cut2 == 0 else arr2[cut2-1]&#10;        right1 = float(&#x27;inf&#x27;) if cut1 == n else arr1[cut1]&#10;        right2 = float(&#x27;inf&#x27;) if cut2 == m else arr2[cut2]&#10;        if left1 &lt;= right2 and left2 &lt;= right1: return max(left1, left2)&#10;        elif left1 &gt; right2: high = cut1 - 1&#10;        else: low = cut1 + 1&#10;    return 1</code></pre></details></td>
    </tr>
    <tr>
      <td>12</td>
      <td>Bs 11 Find Minimum In Rotated Sorted Array<br><br></b> <a href='https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/' target='_blank'>LeetCode 153</a></td>
      <td><b>Example 1:</b> Input: nums = [3,4,5,1,2], Output: 1</td>
      <td><b>Time:</b> O(log N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Binary Search. If `nums[low] <= nums[high]`, the array is sorted, return `nums[low]`. Else, if `nums[low] <= nums[mid]`, the left half is sorted, the minimum is in the right half.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findMin(nums: List[int]) -&gt; int:&#10;    low, high = 0, len(nums) - 1&#10;    ans = float(&#x27;inf&#x27;)&#10;    while low &lt;= high:&#10;        mid = (low + high) // 2&#10;        if nums[low] &lt;= nums[high]:&#10;            ans = min(ans, nums[low])&#10;            break&#10;        if nums[low] &lt;= nums[mid]:&#10;            ans = min(ans, nums[low])&#10;            low = mid + 1&#10;        else:&#10;            ans = min(ans, nums[mid])&#10;            high = mid - 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>13</td>
      <td>Bs 12 Search In Rotated Sorted Array<br><br></b> <a href='https://leetcode.com/problems/search-in-rotated-sorted-array/' target='_blank'>LeetCode 33</a></td>
      <td><b>Example 1:</b> Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4</td>
      <td><b>Time:</b> O(log N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Binary Search. Identify which half is sorted. If left half is sorted and target is in its range, move `high = mid - 1`, else `low = mid + 1`. Symmetrically for right half.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def search(nums: List[int], target: int) -&gt; int:&#10;    low, high = 0, len(nums) - 1&#10;    while low &lt;= high:&#10;        mid = (low + high) // 2&#10;        if nums[mid] == target: return mid&#10;        if nums[low] &lt;= nums[mid]:&#10;            if nums[low] &lt;= target &lt;= nums[mid]: high = mid - 1&#10;            else: low = mid + 1&#10;        else:&#10;            if nums[mid] &lt;= target &lt;= nums[high]: low = mid + 1&#10;            else: high = mid - 1&#10;    return -1</code></pre></details></td>
    </tr>
    <tr>
      <td>14</td>
      <td>Bs 13 Search In Rotated Sorted Array Ii<br><br></b> <a href='https://leetcode.com/problems/search-in-rotated-sorted-array-ii/' target='_blank'>LeetCode 81</a></td>
      <td><b>Example 1:</b> Input: nums = [2,5,6,0,0,1,2], target = 0, Output: true</td>
      <td><b>Time:</b> O(log N) average, O(N) worst case<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>Duplicates causing ambiguity:</b> Shrink bounds safely.</td>
      <td><b>Explanation:</b> If `nums[low] == nums[mid] == nums[high]`, shrink the search space by `low++` and `high--`. Otherwise, proceed with the standard rotated binary search.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def search(nums: List[int], target: int) -&gt; bool:&#10;    low, high = 0, len(nums) - 1&#10;    while low &lt;= high:&#10;        mid = (low + high) // 2&#10;        if nums[mid] == target: return True&#10;        if nums[low] == nums[mid] == nums[high]:&#10;            low += 1; high -= 1; continue&#10;        if nums[low] &lt;= nums[mid]:&#10;            if nums[low] &lt;= target &lt;= nums[mid]: high = mid - 1&#10;            else: low = mid + 1&#10;        else:&#10;            if nums[mid] &lt;= target &lt;= nums[high]: low = mid + 1&#10;            else: high = mid - 1&#10;    return False</code></pre></details></td>
    </tr>
    <tr>
      <td>15</td>
      <td>Bs 14 Find Peak Element<br><br></b> <a href='https://leetcode.com/problems/find-peak-element/' target='_blank'>LeetCode 162</a></td>
      <td><b>Example 1:</b> Input: nums = [1,2,3,1], Output: 2</td>
      <td><b>Time:</b> O(log N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Binary Search. If `nums[mid] > nums[mid + 1]`, we are on a descending slope, so a peak must be to the left (or is `mid`). Else, we are on an ascending slope, peak is to the right.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findPeakElement(nums: List[int]) -&gt; int:&#10;    low, high = 0, len(nums) - 1&#10;    while low &lt; high:&#10;        mid = (low + high) // 2&#10;        if nums[mid] &gt; nums[mid + 1]: high = mid&#10;        else: low = mid + 1&#10;    return low</code></pre></details></td>
    </tr>
    <tr>
      <td>16</td>
      <td>Bs 15 Find First And Last Position Of Element In Sorted Array<br><br></b> <a href='https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/' target='_blank'>LeetCode 34</a></td>
      <td><b>Example 1:</b> Input: nums = [5,7,7,8,8,10], target = 8, Output: [3,4]</td>
      <td><b>Time:</b> O(log N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Use lower_bound for the first occurrence. Use upper_bound - 1 for the last occurrence. Validate if the target actually exists at the lower_bound index.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import bisect&#10;def searchRange(nums: List[int], target: int) -&gt; List[int]:&#10;    lb = bisect.bisect_left(nums, target)&#10;    ub = bisect.bisect_right(nums, target)&#10;    if lb == len(nums) or nums[lb] != target: return [-1, -1]&#10;    return [lb, ub - 1]</code></pre></details></td>
    </tr>
    <tr>
      <td>17</td>
      <td>Bs 16 Koko Eating Bananas<br><br></b> <a href='https://leetcode.com/problems/koko-eating-bananas/' target='_blank'>LeetCode 875</a></td>
      <td><b>Example 1:</b> Input: piles = [3,6,7,11], h = 8, Output: 4</td>
      <td><b>Time:</b> O(N log(max(P)))<br><b>Space:</b> O(1)</td>
      <td><code>#include <math.h></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Binary search on the answer. Minimum speed is 1, maximum is `max(piles)`. For a given speed `mid`, calculate total hours `sum(ceil(pile / mid))`. If `<= h`, search lower half.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import math&#10;def minEatingSpeed(piles: List[int], h: int) -&gt; int:&#10;    low, high = 1, max(piles)&#10;    while low &lt;= high:&#10;        mid = (low + high) // 2&#10;        total = sum(math.ceil(p / mid) for p in piles)&#10;        if total &lt;= h: high = mid - 1&#10;        else: low = mid + 1&#10;    return low</code></pre></details></td>
    </tr>
    <tr>
      <td>18</td>
      <td>Bs 17 Minimum Days To Make M Bouquets<br><br></b> <a href='https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/' target='_blank'>LeetCode 1482</a></td>
      <td><b>Example 1:</b> Find day threshold.</td>
      <td><b>Time:</b> O(N log(maxD - minD))<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Binary search on days from `min(bloom)` to `max(bloom)`. Count consecutive bloomed flowers, if it reaches `k`, form a bouquet. Return minimum valid day.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minDays(bloomDay: List[int], m: int, k: int) -&gt; int:&#10;    if m * k &gt; len(bloomDay): return -1&#10;    def isPossible(day):&#10;        count, bouquets = 0, 0&#10;        for d in bloomDay:&#10;            if d &lt;= day: count += 1&#10;            else: bouquets += count // k; count = 0&#10;        bouquets += count // k&#10;        return bouquets &gt;= m&#10;    low, high = min(bloomDay), max(bloomDay)&#10;    ans = -1&#10;    while low &lt;= high:&#10;        mid = (low + high) // 2&#10;        if isPossible(mid): ans = mid; high = mid - 1&#10;        else: low = mid + 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>19</td>
      <td>Bs 18 Find The Smallest Divisor Given A Threshold<br><br></b> <a href='https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/' target='_blank'>LeetCode 1283</a></td>
      <td><b>Example 1:</b> Summing ceils.</td>
      <td><b>Time:</b> O(N log(max(nums)))<br><b>Space:</b> O(1)</td>
      <td><code>#include <math.h></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Binary search the divisor from 1 to `max(nums)`. Compute `sum(ceil(num / mid))`. If sum <= threshold, shrink high.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import math&#10;def smallestDivisor(nums: List[int], threshold: int) -&gt; int:&#10;    low, high = 1, max(nums)&#10;    while low &lt;= high:&#10;        mid = (low + high) // 2&#10;        total = sum(math.ceil(num / mid) for num in nums)&#10;        if total &lt;= threshold: high = mid - 1&#10;        else: low = mid + 1&#10;    return low</code></pre></details></td>
    </tr>
    <tr>
      <td>20</td>
      <td>Bs 19 Capacity To Ship Packages Within D Days<br><br></b> <a href='https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/' target='_blank'>LeetCode 1011</a></td>
      <td><b>Example 1:</b> Find ship capacity.</td>
      <td><b>Time:</b> O(N log(sum - max))<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Binary search on capacity. Low = `max(weights)`, High = `sum(weights)`. Iterate through packages and accumulate weight, increment day if limit is exceeded.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def shipWithinDays(weights: List[int], days: int) -&gt; int:&#10;    def canShip(cap):&#10;        d, load = 1, 0&#10;        for w in weights:&#10;            if load + w &gt; cap: d += 1; load = w&#10;            else: load += w&#10;        return d &lt;= days&#10;    low, high = max(weights), sum(weights)&#10;    while low &lt;= high:&#10;        mid = (low + high) // 2&#10;        if canShip(mid): high = mid - 1&#10;        else: low = mid + 1&#10;    return low</code></pre></details></td>
    </tr>
    <tr>
      <td>21</td>
      <td>Bs 25 Minimum Number Of Days To Make M Bouquets<br><br></b> <a href='https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/' target='_blank'>LeetCode 1482</a></td>
      <td><b>Example 1:</b> Binary search on answer.</td>
      <td><b>Time:</b> O(N log(Max-Min))<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>Impossible:</b> If m * k > n, return -1.</td>
      <td><b>Explanation:</b> Binary search on days from `min(bloomDay)` to `max(bloomDay)`. For a given `day`, count consecutive flowers that have bloomed. If count reaches `k`, increment bouquet count and reset flower count. If `bouquets >= m`, move `high = mid - 1`, else `low = mid + 1`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minDays(bloomDay: List[int], m: int, k: int) -&gt; int:&#10;    if m * k &gt; len(bloomDay): return -1&#10;    def possible(day):&#10;        count, bouquets = 0, 0&#10;        for bd in bloomDay:&#10;            if bd &lt;= day:&#10;                count += 1&#10;            else:&#10;                bouquets += count // k&#10;                count = 0&#10;        bouquets += count // k&#10;        return bouquets &gt;= m&#10;    low, high = min(bloomDay), max(bloomDay)&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        if possible(mid): high = mid - 1&#10;        else: low = mid + 1&#10;    return low</code></pre></details></td>
    </tr>
    <tr>
      <td>22</td>
      <td>Bs 26 Find The Smallest Divisor Given A Threshold<br><br></b> <a href='https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/' target='_blank'>LeetCode 1283</a></td>
      <td><b>Example 1:</b> Binary search divisor.</td>
      <td><b>Time:</b> O(N log(Max))<br><b>Space:</b> O(1)</td>
      <td><code>#include <cmath></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Binary search for divisor from `1` to `max(nums)`. For a divisor `mid`, sum `ceil(num / mid)`. If sum <= threshold, move `high = mid - 1`, else `low = mid + 1`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import math&#10;def smallestDivisor(nums: List[int], threshold: int) -&gt; int:&#10;    def sum_by_d(d):&#10;        return sum(math.ceil(num / d) for num in nums)&#10;    low, high = 1, max(nums)&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        if sum_by_d(mid) &lt;= threshold: high = mid - 1&#10;        else: low = mid + 1&#10;    return low</code></pre></details></td>
    </tr>
    <tr>
      <td>23</td>
      <td>Bs 27 Capacity To Ship Packages Within D Days<br><br></b> <a href='https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/' target='_blank'>LeetCode 1011</a></td>
      <td><b>Example 1:</b> Binary search capacity.</td>
      <td><b>Time:</b> O(N log(Sum-Max))<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Binary search for capacity from `max(weights)` to `sum(weights)`. For a capacity `mid`, calculate days required to ship. If required days <= D, move `high = mid - 1`, else `low = mid + 1`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def shipWithinDays(weights: List[int], days: int) -&gt; int:&#10;    def find_days(cap):&#10;        d, load = 1, 0&#10;        for weight in weights:&#10;            if load + weight &gt; cap:&#10;                d += 1&#10;                load = weight&#10;            else:&#10;                load += weight&#10;        return d&#10;    low, high = max(weights), sum(weights)&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        if find_days(mid) &lt;= days: high = mid - 1&#10;        else: low = mid + 1&#10;    return low</code></pre></details></td>
    </tr>
    <tr>
      <td>24</td>
      <td>Bs 28 Kth Missing Positive Number<br><br></b> <a href='https://leetcode.com/problems/kth-missing-positive-number/' target='_blank'>LeetCode 1539</a></td>
      <td><b>Example 1:</b> Calculate missing.</td>
      <td><b>Time:</b> O(log N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Binary search. At index `mid`, the number of missing elements before `arr[mid]` is `arr[mid] - (mid + 1)`. If this is < `k`, search right `low = mid + 1`. Else search left `high = mid - 1`. Ans is `high + 1 + k` or `low + k`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findKthPositive(arr: List[int], k: int) -&gt; int:&#10;    low, high = 0, len(arr) - 1&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        missing = arr[mid] - (mid + 1)&#10;        if missing &lt; k: low = mid + 1&#10;        else: high = mid - 1&#10;    return low + k</code></pre></details></td>
    </tr>
    <tr>
      <td>25</td>
      <td>Bs 29 Aggressive Cows<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/aggressive-cows/0' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Minimax binary search.</td>
      <td><b>Time:</b> O(N log N + N log(Max-Min))<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Sort the stalls. Binary search for distance from `1` to `max-min`. For a distance `mid`, check if we can place all `C` cows such that distance between any two is >= `mid`. If possible, move `low = mid + 1` to maximize it, else `high = mid - 1`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def aggressiveCows(stalls: List[int], k: int) -&gt; int:&#10;    stalls.sort()&#10;    def can_place(dist):&#10;        cnt_cows = 1&#10;        last = stalls[0]&#10;        for i in range(1, len(stalls)):&#10;            if stalls[i] - last &gt;= dist:&#10;                cnt_cows += 1&#10;                last = stalls[i]&#10;        return cnt_cows &gt;= k&#10;    low, high = 1, stalls[-1] - stalls[0]&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        if can_place(mid): low = mid + 1&#10;        else: high = mid - 1&#10;    return high</code></pre></details></td>
    </tr>
    <tr>
      <td>26</td>
      <td>Bs 30 Allocate Books<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Minimizing max pages.</td>
      <td><b>Time:</b> O(N log(Sum-Max))<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>Impossible:</b> If m > n, return -1.</td>
      <td><b>Explanation:</b> Binary search on max pages from `max(arr)` to `sum(arr)`. For a `mid` value, count how many students are needed. If `students > m`, we need to increase limit `low = mid + 1`. Else, `high = mid - 1`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findPages(arr: List[int], n: int, m: int) -&gt; int:&#10;    if m &gt; n: return -1&#10;    def count_students(pages):&#10;        students, pages_student = 1, 0&#10;        for p in arr:&#10;            if pages_student + p &lt;= pages:&#10;                pages_student += p&#10;            else:&#10;                students += 1&#10;                pages_student = p&#10;        return students&#10;    low, high = max(arr), sum(arr)&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        if count_students(mid) &gt; m: low = mid + 1&#10;        else: high = mid - 1&#10;    return low</code></pre></details></td>
    </tr>
    <tr>
      <td>27</td>
      <td>Bs 31 Split Array Largest Sum<br><br></b> <a href='https://leetcode.com/problems/split-array-largest-sum/' target='_blank'>LeetCode 410</a></td>
      <td><b>Example 1:</b> Equivalent to allocate books.</td>
      <td><b>Time:</b> O(N log(Sum-Max))<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Identical logic to Allocate Books. Binary search from `max(nums)` to `sum(nums)`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def splitArray(nums: List[int], k: int) -&gt; int:&#10;    def count_partitions(max_sum):&#10;        partitions, subarray_sum = 1, 0&#10;        for num in nums:&#10;            if subarray_sum + num &lt;= max_sum:&#10;                subarray_sum += num&#10;            else:&#10;                partitions += 1&#10;                subarray_sum = num&#10;        return partitions&#10;    low, high = max(nums), sum(nums)&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        if count_partitions(mid) &gt; k: low = mid + 1&#10;        else: high = mid - 1&#10;    return low</code></pre></details></td>
    </tr>
    <tr>
      <td>28</td>
      <td>Bs 32 Painters Partition Problem<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/the-painters-partition-problem1535/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Minimax identical to book allocation.</td>
      <td><b>Time:</b> O(N log(Sum-Max))<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Identical to Allocate Books and Split Array Largest Sum. Binary search `max(boards)` to `sum(boards)`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findLargestMinDistance(boards: List[int], k: int) -&gt; int:&#10;    def count_painters(time):&#10;        painters, boards_painter = 1, 0&#10;        for b in boards:&#10;            if boards_painter + b &lt;= time:&#10;                boards_painter += b&#10;            else:&#10;                painters += 1&#10;                boards_painter = b&#10;        return painters&#10;    low, high = max(boards), sum(boards)&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        if count_painters(mid) &gt; k: low = mid + 1&#10;        else: high = mid - 1&#10;    return low</code></pre></details></td>
    </tr>
    <tr>
      <td>29</td>
      <td>Bs 33 Minimize Max Distance To Gas Station<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/minimize-max-distance-to-gas-station/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Double binary search.</td>
      <td><b>Time:</b> O(N log(MaxDist / 1e-6))<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Binary search on the real answer (distance) with a precision (e.g., 1e-6). For a given `mid` distance, count how many gas stations need to be inserted in each gap: `ceil((stations[i+1] - stations[i]) / mid) - 1`. If total needed > k, `low = mid`, else `high = mid`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findSmallestMaxDist(stations: List[int], k: int) -&gt; float:&#10;    def num_required(dist):&#10;        cnt = 0&#10;        for i in range(1, len(stations)):&#10;            number_in_between = int((stations[i] - stations[i-1]) / dist)&#10;            if (stations[i] - stations[i-1]) == (dist * number_in_between):&#10;                number_in_between -= 1&#10;            cnt += number_in_between&#10;        return cnt&#10;    low, high = 0, 0&#10;    for i in range(len(stations) - 1):&#10;        high = max(high, float(stations[i+1] - stations[i]))&#10;    diff = 1e-6&#10;    while high - low &gt; diff:&#10;        mid = low + (high - low) / 2.0&#10;        if num_required(mid) &gt; k: low = mid&#10;        else: high = mid&#10;    return high</code></pre></details></td>
    </tr>
    <tr>
      <td>30</td>
      <td>Bs 34 Median Of Two Sorted Arrays<br><br></b> <a href='https://leetcode.com/problems/median-of-two-sorted-arrays/' target='_blank'>LeetCode 4</a></td>
      <td><b>Example 1:</b> Input: nums1 = [1,3], nums2 = [2], Output: 2.0</td>
      <td><b>Time:</b> O(log(min(N, M)))<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>Odd/Even Length:</b> Handle average for even total length.</td>
      <td><b>Explanation:</b> Binary search on the smaller array to find a partition such that left halves of both arrays contain half of total elements, and `maxLeft <= minRight`. Use `INT_MIN` and `INT_MAX` for out-of-bound partitions.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -&gt; float:&#10;    if len(nums1) &gt; len(nums2): return findMedianSortedArrays(nums2, nums1)&#10;    n1, n2 = len(nums1), len(nums2)&#10;    low, high = 0, n1&#10;    while low &lt;= high:&#10;        cut1 = (low + high) // 2&#10;        cut2 = (n1 + n2 + 1) // 2 - cut1&#10;        left1 = float(&#x27;-inf&#x27;) if cut1 == 0 else nums1[cut1-1]&#10;        left2 = float(&#x27;-inf&#x27;) if cut2 == 0 else nums2[cut2-1]&#10;        right1 = float(&#x27;inf&#x27;) if cut1 == n1 else nums1[cut1]&#10;        right2 = float(&#x27;inf&#x27;) if cut2 == n2 else nums2[cut2]&#10;        if left1 &lt;= right2 and left2 &lt;= right1:&#10;            if (n1 + n2) % 2 == 0:&#10;                return (max(left1, left2) + min(right1, right2)) / 2.0&#10;            else:&#10;                return max(left1, left2)&#10;        elif left1 &gt; right2:&#10;            high = cut1 - 1&#10;        else:&#10;            low = cut1 + 1&#10;    return 0.0</code></pre></details></td>
    </tr>
    <tr>
      <td>31</td>
      <td>Bs 35 Median Of Two Sorted Arrays<br><br></b> <a href='https://leetcode.com/problems/median-of-two-sorted-arrays/' target='_blank'>LeetCode 4</a></td>
      <td><b>Example 1:</b> Binary search on smaller array.</td>
      <td><b>Time:</b> O(log(min(N, M)))<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Ensure `nums1` is the smaller array. Partition both arrays such that the left half has `(n+m+1)/2` elements. Use binary search on `nums1` to find the correct partition where `max(left1) <= min(right2)` and `max(left2) <= min(right1)`. The median depends on whether total elements is odd or even.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -&gt; float:&#10;    if len(nums1) &gt; len(nums2): return findMedianSortedArrays(nums2, nums1)&#10;    n, m = len(nums1), len(nums2)&#10;    low, high = 0, n&#10;    while low &lt;= high:&#10;        cut1 = (low + high) // 2&#10;        cut2 = (n + m + 1) // 2 - cut1&#10;        left1 = float(&#x27;-inf&#x27;) if cut1 == 0 else nums1[cut1-1]&#10;        left2 = float(&#x27;-inf&#x27;) if cut2 == 0 else nums2[cut2-1]&#10;        right1 = float(&#x27;inf&#x27;) if cut1 == n else nums1[cut1]&#10;        right2 = float(&#x27;inf&#x27;) if cut2 == m else nums2[cut2]&#10;        if left1 &lt;= right2 and left2 &lt;= right1:&#10;            if (n + m) % 2 == 0:&#10;                return (max(left1, left2) + min(right1, right2)) / 2.0&#10;            else:&#10;                return max(left1, left2)&#10;        elif left1 &gt; right2:&#10;            high = cut1 - 1&#10;        else:&#10;            low = cut1 + 1&#10;    return 0.0</code></pre></details></td>
    </tr>
    <tr>
      <td>32</td>
      <td>Bs 36 Kth Element Of Two Sorted Arrays<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Generalization of median.</td>
      <td><b>Time:</b> O(log(min(N, M, K)))<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Similar to Median of 2 sorted arrays. Apply binary search on the smaller array. The partition requires `cut1 + cut2 = k`. Boundaries for `cut1` are `max(0, k - m)` and `min(k, n)`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def kthElement(arr1: List[int], arr2: List[int], n: int, m: int, k: int) -&gt; int:&#10;    if n &gt; m: return kthElement(arr2, arr1, m, n, k)&#10;    low, high = max(0, k - m), min(k, n)&#10;    while low &lt;= high:&#10;        cut1 = (low + high) // 2&#10;        cut2 = k - cut1&#10;        left1 = float(&#x27;-inf&#x27;) if cut1 == 0 else arr1[cut1-1]&#10;        left2 = float(&#x27;-inf&#x27;) if cut2 == 0 else arr2[cut2-1]&#10;        right1 = float(&#x27;inf&#x27;) if cut1 == n else arr1[cut1]&#10;        right2 = float(&#x27;inf&#x27;) if cut2 == m else arr2[cut2]&#10;        if left1 &lt;= right2 and left2 &lt;= right1:&#10;            return max(left1, left2)&#10;        elif left1 &gt; right2:&#10;            high = cut1 - 1&#10;        else:&#10;            low = cut1 + 1&#10;    return 1</code></pre></details></td>
    </tr>
    <tr>
      <td>33</td>
      <td>Bs 37 Search In A 2D Matrix Ii<br><br></b> <a href='https://leetcode.com/problems/search-a-2d-matrix-ii/' target='_blank'>LeetCode 240</a></td>
      <td><b>Example 1:</b> Start from top right.</td>
      <td><b>Time:</b> O(N + M)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Start from the top-right corner. If `target == current`, return true. If `target < current`, move left (`c--`). If `target > current`, move down (`r++`).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def searchMatrix(matrix: List[List[int]], target: int) -&gt; bool:&#10;    r, c = 0, len(matrix[0]) - 1&#10;    while r &lt; len(matrix) and c &gt;= 0:&#10;        if matrix[r][c] == target: return True&#10;        elif matrix[r][c] &gt; target: c -= 1&#10;        else: r += 1&#10;    return False</code></pre></details></td>
    </tr>
    <tr>
      <td>34</td>
      <td>Bs 38 Find A Peak Element Ii<br><br></b> <a href='https://leetcode.com/problems/find-a-peak-element-ii/' target='_blank'>LeetCode 1901</a></td>
      <td><b>Example 1:</b> Binary search on columns.</td>
      <td><b>Time:</b> O(N log M)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Binary search on columns. Find middle column, find max element in this column. Compare it with its left and right neighbors. If it's > both, it's a peak. If left is greater, peak exists in left half. Else, peak exists in right half.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findPeakGrid(mat: List[List[int]]) -&gt; List[int]:&#10;    n, m = len(mat), len(mat[0])&#10;    low, high = 0, m - 1&#10;    while low &lt;= high:&#10;        mid = (low + high) // 2&#10;        max_row = 0&#10;        for i in range(n):&#10;            if mat[i][mid] &gt; mat[max_row][mid]: max_row = i&#10;        left = mat[max_row][mid-1] if mid - 1 &gt;= 0 else -1&#10;        right = mat[max_row][mid+1] if mid + 1 &lt; m else -1&#10;        if mat[max_row][mid] &gt; left and mat[max_row][mid] &gt; right:&#10;            return [max_row, mid]&#10;        elif mat[max_row][mid] &lt; left:&#10;            high = mid - 1&#10;        else:&#10;            low = mid + 1&#10;    return [-1, -1]</code></pre></details></td>
    </tr>
    <tr>
      <td>35</td>
      <td>Bs 39 Matrix Median<br><br></b> <a href='https://www.interviewbit.com/problems/matrix-median/' target='_blank'>InterviewBit</a></td>
      <td><b>Example 1:</b> Binary search on answer range.</td>
      <td><b>Time:</b> O(32 * N log M)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Binary search on the value range `[1, 10^9]`. For a candidate `mid`, count how many numbers are `<= mid` across all rows using `upper_bound`. If count `> (N*M)/2`, `mid` could be median, search lower. Else search higher.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import bisect&#10;def findMedian(A: List[List[int]]) -&gt; int:&#10;    low, high = 1, int(1e9)&#10;    n, m = len(A), len(A[0])&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        cnt = sum(bisect.bisect_right(row, mid) for row in A)&#10;        if cnt &lt;= (n * m) // 2:&#10;            low = mid + 1&#10;        else:&#10;            high = mid - 1&#10;    return low</code></pre></details></td>
    </tr>
    <tr>
      <td>36</td>
      <td>Bs 40 Kth Smallest Number In Multiplication Table<br><br></b> <a href='https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/' target='_blank'>LeetCode 668</a></td>
      <td><b>Example 1:</b> Binary Search on answer.</td>
      <td><b>Time:</b> O(m * log(m*n))<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Binary search on range `[1, m*n]`. For a value `mid`, the number of elements `<= mid` in row `i` is `min(mid / i, n)`. Sum this for all rows to get total count. If count >= k, search left. Else search right.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findKthNumber(m: int, n: int, k: int) -&gt; int:&#10;    low, high = 1, m * n&#10;    while low &lt; high:&#10;        mid = low + (high - low) // 2&#10;        count = sum(min(mid // i, n) for i in range(1, m + 1))&#10;        if count &gt;= k:&#10;            high = mid&#10;        else:&#10;            low = mid + 1&#10;    return low</code></pre></details></td>
    </tr>
    <tr>
      <td>37</td>
      <td>Bs 41 Find K Th Smallest Pair Distance<br><br></b> <a href='https://leetcode.com/problems/find-k-th-smallest-pair-distance/' target='_blank'>LeetCode 719</a></td>
      <td><b>Example 1:</b> Sort and binary search on distance.</td>
      <td><b>Time:</b> O(N log N + N log(max_dist))<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Sort array. Binary search on distance `[0, nums.back() - nums.front()]`. For a candidate `mid`, count pairs with distance `<= mid` using a sliding window. If count >= k, search left. Else search right.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def smallestDistancePair(nums: List[int], k: int) -&gt; int:&#10;    nums.sort()&#10;    low, high = 0, nums[-1] - nums[0]&#10;    def countPairs(mid):&#10;        count, l = 0, 0&#10;        for r in range(len(nums)):&#10;            while nums[r] - nums[l] &gt; mid: l += 1&#10;            count += (r - l)&#10;        return count&#10;    while low &lt; high:&#10;        mid = low + (high - low) // 2&#10;        if countPairs(mid) &gt;= k:&#10;            high = mid&#10;        else:&#10;            low = mid + 1&#10;    return low</code></pre></details></td>
    </tr>
    <tr>
      <td>38</td>
      <td>Bs 42 Split Array Largest Sum<br><br></b> <a href='https://leetcode.com/problems/split-array-largest-sum/' target='_blank'>LeetCode 410</a></td>
      <td><b>Example 1:</b> Binary search on answer.</td>
      <td><b>Time:</b> O(N log(sum - max))<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Binary search the max subarray sum `[max(nums), sum(nums)]`. For a `mid`, greedily split array. If subarrays needed `<= k`, `mid` is possible, search lower. Else search higher.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def splitArray(nums: List[int], k: int) -&gt; int:&#10;    low, high = max(nums), sum(nums)&#10;    while low &lt; high:&#10;        mid = low + (high - low) // 2&#10;        pieces, currentSum = 1, 0&#10;        for n in nums:&#10;            if currentSum + n &gt; mid:&#10;                currentSum = n&#10;                pieces += 1&#10;            else:&#10;                currentSum += n&#10;        if pieces &lt;= k:&#10;            high = mid&#10;        else:&#10;            low = mid + 1&#10;    return low</code></pre></details></td>
    </tr>
    <tr>
      <td>39</td>
      <td>Bs 43 Minimum Number Of Days To Make M Bouquets<br><br></b> <a href='https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/' target='_blank'>LeetCode 1482</a></td>
      <td><b>Example 1:</b> Binary search on days.</td>
      <td><b>Time:</b> O(N log(max_day))<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> If `m * k > n`, return -1. Binary search on days `[min(bloomDay), max(bloomDay)]`. For a given day, count adjacent bloomed flowers. Every `k` consecutive bloomed flowers make 1 bouquet. If total bouquets >= m, search left. Else search right.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minDays(bloomDay: List[int], m: int, k: int) -&gt; int:&#10;    if m * k &gt; len(bloomDay): return -1&#10;    low, high = min(bloomDay), max(bloomDay)&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        bouquets, count = 0, 0&#10;        for day in bloomDay:&#10;            if day &lt;= mid:&#10;                count += 1&#10;                if count == k:&#10;                    bouquets += 1&#10;                    count = 0&#10;            else:&#10;                count = 0&#10;        if bouquets &gt;= m:&#10;            high = mid - 1&#10;        else:&#10;            low = mid + 1&#10;    return low</code></pre></details></td>
    </tr>
    <tr>
      <td>40</td>
      <td>Bs 44 Capacity To Ship Packages Within D Days<br><br></b> <a href='https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/' target='_blank'>LeetCode 1011</a></td>
      <td><b>Example 1:</b> Same as split array.</td>
      <td><b>Time:</b> O(N log(sum - max))<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Binary search on capacity `[max(weights), sum(weights)]`. For a `mid` capacity, greedily load packages. If a package makes sum > capacity, increment days and start new load. If `days <= D`, search left. Else search right.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def shipWithinDays(weights: List[int], days: int) -&gt; int:&#10;    low, high = max(weights), sum(weights)&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        d, load = 1, 0&#10;        for w in weights:&#10;            if load + w &gt; mid:&#10;                d += 1&#10;                load = w&#10;            else:&#10;                load += w&#10;        if d &lt;= days:&#10;            high = mid - 1&#10;        else:&#10;            low = mid + 1&#10;    return low</code></pre></details></td>
    </tr>
  </tbody>
</table>
