# 03 Searching Sorting Revision Table

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
      <td>Arr 01 Search A 2D Matrix<br><br></b> <a href="https://leetcode.com/problems/search-a-2d-matrix/" target="_blank">LeetCode 74</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Apna College, Striver A Z, SDE Sheet</details></td>
      <td>**Example 1:** Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3, Output: true</td>
      <td><details><summary><b>Approach 1</b></summary><b>Time:</b> O(N^2) or worse<br><b>Space:</b> O(N) or O(1)</details><details><summary><b>Approach 2</b></summary><b>Time:</b> O(log(m * n))<br><b>Space:</b> O(1)</details></td>
      <td><details><summary><b>Approach 1</b></summary><b>Explanation:</b> Brute Force: Standard unoptimized approach. (TODO: Implement specific logic)<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python"># TODO: Implement Brute Force&#10;def searchMatrix(matrix: List[List[int]], target: int) -&gt; bool:&#10;    if not matrix: return False&#10;    m, n = len(matrix), len(matrix[0])&#10;    low, high = 0, (m * n) - 1&#10;    while low &lt;= high:&#10;        mid = (low + high) // 2&#10;        if matrix[mid // n][mid % n] == target: return True&#10;        if matrix[mid // n][mid % n] &lt; target: low = mid + 1&#10;        else: high = mid - 1&#10;    return False</code></pre></details></details><details><summary><b>Approach 2</b></summary><b>Explanation:</b> Optimal: Treat the 2D matrix as a 1D array and apply binary search. The element at `mid` can be accessed using `matrix[mid / cols][mid % cols]`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def searchMatrix(matrix: List[List[int]], target: int) -&gt; bool:&#10;    if not matrix: return False&#10;    m, n = len(matrix), len(matrix[0])&#10;    low, high = 0, (m * n) - 1&#10;    while low &lt;= high:&#10;        mid = (low + high) // 2&#10;        if matrix[mid // n][mid % n] == target: return True&#10;        if matrix[mid // n][mid % n] &lt; target: low = mid + 1&#10;        else: high = mid - 1&#10;    return False</code></pre></details></details></td>
    </tr>
    <tr>
      <td>2</td>
      <td>Sort 02 Merge Sort<br><br></b> <a href="https://leetcode.com/problems/sort-an-array/" target="_blank">LeetCode 912</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, Apna College</details></td>
      <td>**Example 1:** Input: nums = [5,2,3,1], Output: [1,2,3,5]</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Divide and Conquer. Split array into halves until size 1. Merge sorted halves using a temporary array.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def mergeSort(arr: list[int]) -&gt; list[int]:&#10;    if len(arr) &lt;= 1: return arr&#10;    mid = len(arr) // 2&#10;    left = mergeSort(arr[:mid])&#10;    right = mergeSort(arr[mid:])&#10;    &#10;    res = []&#10;    i = j = 0&#10;    while i &lt; len(left) and j &lt; len(right):&#10;        if left[i] &lt;= right[j]:&#10;            res.append(left[i]); i += 1&#10;        else:&#10;            res.append(right[j]); j += 1&#10;    res.extend(left[i:])&#10;    res.extend(right[j:])&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td>3</td>
      <td>Bs 03 Find Minimum In Rotated Sorted Array<br><br></b> <a href="https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/" target="_blank">LeetCode 153</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Apna College, Striver A Z, SDE Sheet</details></td>
      <td>**Example 1:** Input: nums = [3,4,5,1,2], Output: 1</td>
      <td><b>Time:</b> O(log N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Binary Search. Compare mid with right pointer. If nums[mid] > nums[right], the min is in the right half. Else, the min is in the left half including mid.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findMin(nums: List[int]) -&gt; int:&#10;    left, right = 0, len(nums) - 1&#10;    while left &lt; right:&#10;        mid = left + (right - left) // 2&#10;        if nums[mid] &gt; nums[right]: left = mid + 1&#10;        else: right = mid&#10;    return nums[left]</code></pre></details></td>
    </tr>
    <tr>
      <td>4</td>
      <td>Bs 04 Find Peak Element<br><br></b> <a href="https://leetcode.com/problems/find-peak-element/" target="_blank">LeetCode 162</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Apna College, Striver A Z, SDE Sheet</details></td>
      <td>**Example 1:** Input: nums = [1,2,3,1], Output: 2</td>
      <td><b>Time:</b> O(log N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Binary Search. If nums[mid] < nums[mid+1], we are on an ascending slope, so a peak must be to the right. Otherwise, we are on a descending slope, peak is to the left (including mid).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findPeakElement(nums: List[int]) -&gt; int:&#10;    left, right = 0, len(nums) - 1&#10;    while left &lt; right:&#10;        mid = left + (right - left) // 2&#10;        if nums[mid] &lt; nums[mid+1]: left = mid + 1&#10;        else: right = mid&#10;    return left</code></pre></details></td>
    </tr>
  </tbody>
</table>
