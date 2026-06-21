# Day 11 Binary Search Revision Table

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
      <td rowspan="1">1</td>
      <td rowspan="1">Arr 01 Search A 2D Matrix<br><br></b> <a href="https://leetcode.com/problems/search-a-2d-matrix/" target="_blank">LeetCode 74</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Apna College, Striver A Z, SDE Sheet, Love Babbar</details></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3<br><b>Output:</b> true</td>
      <td><b>Time:</b> O(log(m * n))<br><b>Space:</b> O(1)</td>
      <td>Optimal: Treat the 2D matrix as a 1D array and apply binary search. The element at `mid` can be accessed using `matrix[mid / cols][mid % cols]`.</td>
      <td><b>Edge Cases:</b> <b>Empty Matrix:</b> Return false.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def searchMatrix(matrix: List[List[int]], target: int) -&gt; bool:&#10;    if not matrix: return False&#10;    m, n = len(matrix), len(matrix[0])&#10;    low, high = 0, (m * n) - 1&#10;    while low &lt;= high:&#10;        mid = (low + high) // 2&#10;        if matrix[mid // n][mid % n] == target: return True&#10;        if matrix[mid // n][mid % n] &lt; target: low = mid + 1&#10;        else: high = mid - 1&#10;    return False</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">2</td>
      <td rowspan="1">Arr 02 Median Of Two Sorted Arrays Of Different Sizes<br><br></b> <a href="https://leetcode.com/problems/median-of-two-sorted-arrays/" target="_blank">LeetCode 4</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, SDE Sheet, Love Babbar</details></td>
      <td rowspan="1"><b> </b> Binary Search.</td>
      <td><b>Time:</b> O(log(min(N, M)))<br><b>Space:</b> O(1)</td>
      <td>Optimal: Use Binary Search on the smaller array. Partition both arrays such that the number of elements on the left side is equal to or one more than the right side. Check if `maxLeftX <= minRightY` and `maxLeftY <= minRightX`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findMedianSortedArrays(nums1, nums2):&#10;    if len(nums1) &gt; len(nums2): return findMedianSortedArrays(nums2, nums1)&#10;    x, y = len(nums1), len(nums2)&#10;    low, high = 0, x&#10;    while low &lt;= high:&#10;        partitionX = (low + high) // 2&#10;        partitionY = (x + y + 1) // 2 - partitionX&#10;        maxLeftX = float(&#x27;-inf&#x27;) if partitionX == 0 else nums1[partitionX - 1]&#10;        minRightX = float(&#x27;inf&#x27;) if partitionX == x else nums1[partitionX]&#10;        maxLeftY = float(&#x27;-inf&#x27;) if partitionY == 0 else nums2[partitionY - 1]&#10;        minRightY = float(&#x27;inf&#x27;) if partitionY == y else nums2[partitionY]&#10;        if maxLeftX &lt;= minRightY and maxLeftY &lt;= minRightX:&#10;            if (x + y) % 2 == 0:&#10;                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0&#10;            else:&#10;                return max(maxLeftX, maxLeftY)&#10;        elif maxLeftX &gt; minRightY:&#10;            high = partitionX - 1&#10;        else:&#10;            low = partitionX + 1&#10;    return 0.0</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">3</td>
      <td rowspan="1">Bs 03 Binary Search<br><br></b> <a href="https://leetcode.com/problems/binary-search/" target="_blank">LeetCode 704</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> nums = [-1,0,3,5,9,12], target = 9<br><b>Output:</b> 4</td>
      <td><b>Time:</b> O(log N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td>Optimal: Standard Iterative approach. Maintain `low` and `high` boundaries, shrinking the search space by half.</td>
      <td><b>Edge Cases:</b> <b>Mid Overflow:</b> Use `mid = low + (high - low) / 2` to avoid integer overflow if boundaries are large.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def search(nums: list[int], target: int) -&gt; int:&#10;    low, high = 0, len(nums) - 1&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        if nums[mid] == target:&#10;            return mid&#10;        elif nums[mid] &lt; target:&#10;            low = mid + 1&#10;        else:&#10;            high = mid - 1&#10;    return -1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">4</td>
      <td rowspan="1">Bs 04 Lower Bound<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> arr = [1,2,8,10,11,12,19], target = 0<br><b>Output:</b> 0</td>
      <td><b>Time:</b> O(log N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td>Optimal: When `nums[mid] >= target`, it is a potential answer. Store it and search left (`high = mid - 1`) for smaller potentials.<br><br><b>Dependencies:</b> <code>std::lower_bound</code> internal alternative</td>
      <td><b>Edge Cases:</b> <b>Not Found:</b> If all elements are smaller, `ans` stays `N`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def lowerBound(arr: list[int], n: int, x: int) -&gt; int:&#10;    low, high = 0, n - 1&#10;    ans = n&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        if arr[mid] &gt;= x:&#10;            ans = mid&#10;            high = mid - 1&#10;        else:&#10;            low = mid + 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">5</td>
      <td rowspan="1">Bs 05 Find First And Last Position Of Element<br><br></b> <a href="https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/" target="_blank">LeetCode 34</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> SDE Sheet, Striver A Z, Love Babbar</details></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> nums = [5,7,7,8,8,10], target = 8<br><b>Output:</b> [3,4]</td>
      <td><b>Time:</b> O(log N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td>Optimal: Run Binary Search twice. Once to find the first occurrence (bias left), once to find the last occurrence (bias right).</td>
      <td><b>Edge Cases:</b> <b>Empty Array:</b> Naturally skips loop and returns `[-1, -1]`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def searchRange(nums: list[int], target: int) -&gt; list[int]:&#10;    def findBound(isFirst):&#10;        low, high, ans = 0, len(nums) - 1, -1&#10;        while low &lt;= high:&#10;            mid = low + (high - low) // 2&#10;            if nums[mid] == target:&#10;                ans = mid&#10;                if isFirst: high = mid - 1&#10;                else: low = mid + 1&#10;            elif nums[mid] &lt; target:&#10;                low = mid + 1&#10;            else:&#10;                high = mid - 1&#10;        return ans&#10;    return [findBound(True), findBound(False)]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">6</td>
      <td rowspan="1">Bs 06 Search In Rotated Sorted Array<br><br></b> <a href="https://leetcode.com/problems/search-in-rotated-sorted-array/" target="_blank">LeetCode 33</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> SDE Sheet, Striver A Z, Love Babbar</details></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> nums = [4,5,6,7,0,1,2], target = 0<br><b>Output:</b> 4</td>
      <td><b>Time:</b> O(log N) (Constraint)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Identify the sorted half. Check if target lies within the boundaries of the sorted half. If yes, shrink to that half; else, shrink to the other.</td>
      <td><b>Edge Cases:</b> <b>Duplicate Values:</b> If duplicates existed (which they don't in this specific leetcode), we would need to handle `nums[low] == nums[mid] == nums[high]` by shrinking bounds.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def search(nums: list[int], target: int) -&gt; int:&#10;    low, high = 0, len(nums) - 1&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        if nums[mid] == target: return mid&#10;        &#10;        if nums[low] &lt;= nums[mid]:&#10;            if nums[low] &lt;= target &lt;= nums[mid]:&#10;                high = mid - 1&#10;            else:&#10;                low = mid + 1&#10;        else:&#10;            if nums[mid] &lt;= target &lt;= nums[high]:&#10;                low = mid + 1&#10;            else:&#10;                high = mid - 1&#10;    return -1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">7</td>
      <td rowspan="1">Bs 07 Koko Eating Bananas<br><br></b> <a href="https://leetcode.com/problems/koko-eating-bananas/" target="_blank">LeetCode 875</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> SDE Sheet, Striver A Z, Love Babbar</details></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> piles = [3,6,7,11], h = 8<br><b>Output:</b> 4<br><br><b>Note (Constraint):</b> Binary Search on Answers.</td>
      <td><b>Time:</b> O(N log(Max(P))) (Constraint)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Search space is `1` to `max(piles)`. For a mid `k`, calculate hours required. If `hours <= h`, it's a valid answer, but search left for smaller `k`.<br><br><b>Dependencies:</b> <code>std::ceil</code> / ceiling math</td>
      <td><b>Edge Cases:</b> <b>Ceiling Math:</b> Use `(pile + mid - 1) / mid` to simulate ceiling division without float casting overhead.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import math&#10;def minEatingSpeed(piles: list[int], h: int) -&gt; int:&#10;    def canEat(k):&#10;        hours = sum(math.ceil(pile / k) for pile in piles)&#10;        return hours &lt;= h&#10;        &#10;    low, high = 1, max(piles)&#10;    ans = high&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        if canEat(mid):&#10;            ans = mid&#10;            high = mid - 1&#10;        else:&#10;            low = mid + 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">8</td>
      <td rowspan="1">Bs 08 Find Minimum In Rotated Sorted Array<br><br></b> <a href="https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/" target="_blank">LeetCode 153</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> SDE Sheet, Apna College, Striver A Z, Love Babbar</details></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> nums = [3,4,5,1,2]<br><b>Output:</b> 1</td>
      <td><b>Time:</b> O(log N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Binary Search. Compare mid with right pointer. If nums[mid] > nums[right], the min is in the right half. Else, the min is in the left half including mid.</td>
      <td><b>Edge Cases:</b> <b>Fully sorted array:</b> Loop naturally converges to the first element.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findMin(nums: List[int]) -&gt; int:&#10;    left, right = 0, len(nums) - 1&#10;    while left &lt; right:&#10;        mid = left + (right - left) // 2&#10;        if nums[mid] &gt; nums[right]: left = mid + 1&#10;        else: right = mid&#10;    return nums[left]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">9</td>
      <td rowspan="1">Bs 09 Find Peak Element<br><br></b> <a href="https://leetcode.com/problems/find-peak-element/" target="_blank">LeetCode 162</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> SDE Sheet, Apna College, Striver A Z, Love Babbar</details></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> nums = [1,2,3,1]<br><b>Output:</b> 2</td>
      <td><b>Time:</b> O(log N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Binary Search. If nums[mid] < nums[mid+1], we are on an ascending slope, so a peak must be to the right. Otherwise, we are on a descending slope, peak is to the left (including mid).</td>
      <td><b>Edge Cases:</b> <b>Peak at boundaries:</b> The binary search logic intrinsically handles edges by shrinking bounds away from negative slopes.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findPeakElement(nums: List[int]) -&gt; int:&#10;    left, right = 0, len(nums) - 1&#10;    while left &lt; right:&#10;        mid = left + (right - left) // 2&#10;        if nums[mid] &lt; nums[mid+1]: left = mid + 1&#10;        else: right = mid&#10;    return left</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">10</td>
      <td rowspan="1">Bs 10 Kth Element Of Two Sorted Arrays<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> SDE Sheet, Striver A Z, Love Babbar</details></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> arr1 = [2, 3, 6, 7, 9], arr2 = [1, 4, 8, 10], k = 5<br><b>Output:</b> 6</td>
      <td><b>Time:</b> O(log(min(n, m)))<br><b>Space:</b> O(1)</td>
      <td>Optimal: Binary search on the smaller array. Similar to Median of two sorted arrays, but the left partition size is strictly `k`. Search space for `cut1` is `[max(0, k-m), min(k, n)]`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def kthElement(arr1: List[int], arr2: List[int], n: int, m: int, k: int) -&gt; int:&#10;    if n &gt; m: return kthElement(arr2, arr1, m, n, k)&#10;    low, high = max(0, k - m), min(k, n)&#10;    while low &lt;= high:&#10;        cut1 = (low + high) // 2&#10;        cut2 = k - cut1&#10;        left1 = float(&#x27;-inf&#x27;) if cut1 == 0 else arr1[cut1-1]&#10;        left2 = float(&#x27;-inf&#x27;) if cut2 == 0 else arr2[cut2-1]&#10;        right1 = float(&#x27;inf&#x27;) if cut1 == n else arr1[cut1]&#10;        right2 = float(&#x27;inf&#x27;) if cut2 == m else arr2[cut2]&#10;        if left1 &lt;= right2 and left2 &lt;= right1: return max(left1, left2)&#10;        elif left1 &gt; right2: high = cut1 - 1&#10;        else: low = cut1 + 1&#10;    return 1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">11</td>
      <td rowspan="1">Bs 11 Majority Element<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/majority-element-1587115620/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z, SDE Sheet</details></td>
      <td rowspan="1"><b>Example 1:</b> Moore's Voting Algorithm.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Use Moore's Voting Algorithm to find a candidate for majority element. Then count the occurrences of the candidate in the array to verify if it appears more than N/2 times.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def majorityElement(a, size):&#10;    count = 0&#10;    candidate = -1&#10;    for num in a:&#10;        if count == 0:&#10;            candidate = num&#10;            count = 1&#10;        elif num == candidate: count += 1&#10;        else: count -= 1&#10;    count = 0&#10;    for num in a:&#10;        if num == candidate: count += 1&#10;    return candidate if count &gt; size // 2 else -1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">12</td>
      <td rowspan="1">Bs 12 Find Four Elements That Sum To A Given Value<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/find-all-four-sum-numbers1732/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z, SDE Sheet</details></td>
      <td rowspan="1"><b>Example 1:</b> Two loops and two pointers.</td>
      <td><b>Time:</b> O(N^3)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Sort the array. Use two nested loops for the first two elements. Then use two pointers for the remaining two elements to find the target sum. Skip duplicates at all levels.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def fourSum(arr, k):&#10;    ans = []&#10;    n = len(arr)&#10;    arr.sort()&#10;    for i in range(n):&#10;        if i &gt; 0 and arr[i] == arr[i-1]: continue&#10;        for j in range(i + 1, n):&#10;            if j &gt; i + 1 and arr[j] == arr[j-1]: continue&#10;            left, right = j + 1, n - 1&#10;            while left &lt; right:&#10;                total = arr[i] + arr[j] + arr[left] + arr[right]&#10;                if total == k:&#10;                    ans.append([arr[i], arr[j], arr[left], arr[right]])&#10;                    left += 1; right -= 1&#10;                    while left &lt; right and arr[left] == arr[left-1]: left += 1&#10;                    while left &lt; right and arr[right] == arr[right+1]: right -= 1&#10;                elif total &lt; k: left += 1&#10;                else: right -= 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">13</td>
      <td rowspan="1">Bs 13 Find Nth Root Of M<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/find-nth-root-of-m5843/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, SDE Sheet</details></td>
      <td rowspan="1"><b>Example 1:</b> Binary Search.</td>
      <td><b>Time:</b> O(N * log M)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Search space is `[1, m]`. Check `mid^n`. Since `mid^n` can overflow, use a custom power function that returns 1 if `mid^n == m`, 0 if `< m`, and 2 if `> m`. Adjust `low` and `high` accordingly.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def NthRoot(n, m):&#10;    def func(mid, n, m):&#10;        ans = 1&#10;        for _ in range(n):&#10;            ans *= mid&#10;            if ans &gt; m: return 2&#10;        if ans == m: return 1&#10;        return 0&#10;    low, high = 1, m&#10;    while low &lt;= high:&#10;        mid = (low + high) // 2&#10;        midN = func(mid, n, m)&#10;        if midN == 1: return mid&#10;        elif midN == 0: low = mid + 1&#10;        else: high = mid - 1&#10;    return -1</code></pre></details></td>
    </tr>
  </tbody>
</table>
