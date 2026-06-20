# 03 Searching and Sorting Revision Table

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
      <td>Sort 01 Selection Sort<br><br></b> <a href="https://www.geeksforgeeks.org/problems/selection-sort/1" target="_blank">GeeksforGeeks</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: N = 5, arr[] = {4, 1, 3, 9, 7}, Output: 1 3 4 7 9<br><br>**Note (Constraint):** In-place sorting.</td>
      <td><b>Time:</b> O(N<sup>2</sup>) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><b>Explanation:</b> Find the minimum element in the unsorted array and swap it with the element at the beginning.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def selection_sort(arr: list[int]) -&gt; None:&#10;    n = len(arr)&#10;    for i in range(n - 1):&#10;        min_idx = i&#10;        for j in range(i + 1, n):&#10;            if arr[j] &lt; arr[min_idx]:&#10;                min_idx = j&#10;        arr[i], arr[min_idx] = arr[min_idx], arr[i]</code></pre></details></td>
    </tr>
    <tr>
      <td>2</td>
      <td>Sort 02 Bubble Sort<br><br></b> <a href="https://www.geeksforgeeks.org/problems/bubble-sort/1" target="_blank">GeeksforGeeks</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: N = 5, arr[] = {4, 1, 3, 9, 7}, Output: 1 3 4 7 9</td>
      <td><b>Time:</b> O(N<sup>2</sup>) (Trade-off)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Repeatedly swap adjacent elements if they are in the wrong order. Push the maximum element to the end.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def bubble_sort(arr: list[int]) -&gt; None:&#10;    n = len(arr)&#10;    for i in range(n - 1, -1, -1):&#10;        did_swap = False&#10;        for j in range(i):&#10;            if arr[j] &gt; arr[j + 1]:&#10;                arr[j], arr[j + 1] = arr[j + 1], arr[j]&#10;                did_swap = True&#10;        if not did_swap: break</code></pre></details></td>
    </tr>
    <tr>
      <td>3</td>
      <td>Sort 03 Insertion Sort<br><br></b> <a href="https://www.geeksforgeeks.org/problems/insertion-sort/1" target="_blank">GeeksforGeeks</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: N = 5, arr[] = {4, 1, 3, 9, 7}, Output: 1 3 4 7 9</td>
      <td><b>Time:</b> O(N<sup>2</sup>) (Constraint)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Takes an element and places it in its correct position within the previously sorted part of the array.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def insertion_sort(arr: list[int]) -&gt; None:&#10;    n = len(arr)&#10;    for i in range(n):&#10;        j = i&#10;        while j &gt; 0 and arr[j - 1] &gt; arr[j]:&#10;            arr[j - 1], arr[j] = arr[j], arr[j - 1]&#10;            j -= 1</code></pre></details></td>
    </tr>
    <tr>
      <td>4</td>
      <td>Sort 04 Merge Sort<br><br></b> <a href="https://www.geeksforgeeks.org/problems/merge-sort/1" target="_blank">GeeksforGeeks</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: N = 5, arr[] = {4, 1, 3, 9, 7}, Output: 1 3 4 7 9</td>
      <td><b>Time:</b> O(N log N) (Constraint)<br><b>Space:</b> O(N) (Trade-off)</td>
      <td><b>Explanation:</b> Recursively split array in half, sort them, and merge the sorted halves.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def merge_sort(arr: list[int]) -&gt; None:&#10;    def merge(low, mid, high):&#10;        temp = []&#10;        left, right = low, mid + 1&#10;        while left &lt;= mid and right &lt;= high:&#10;            if arr[left] &lt;= arr[right]:&#10;                temp.append(arr[left])&#10;                left += 1&#10;            else:&#10;                temp.append(arr[right])&#10;                right += 1&#10;        while left &lt;= mid:&#10;            temp.append(arr[left]); left += 1&#10;        while right &lt;= high:&#10;            temp.append(arr[right]); right += 1&#10;        for i in range(len(temp)):&#10;            arr[low + i] = temp[i]&#10;            &#10;    def helper(low, high):&#10;        if low &gt;= high: return&#10;        mid = (low + high) // 2&#10;        helper(low, mid)&#10;        helper(mid + 1, high)&#10;        merge(low, mid, high)&#10;        &#10;    helper(0, len(arr) - 1)</code></pre></details></td>
    </tr>
    <tr>
      <td>5</td>
      <td>Sort 05 Quick Sort<br><br></b> <a href="https://www.geeksforgeeks.org/problems/quick-sort/1" target="_blank">GeeksforGeeks</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: N = 5, arr[] = {4, 1, 3, 9, 7}, Output: 1 3 4 7 9</td>
      <td><b>Time:</b> O(N log N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><b>Explanation:</b> Pick a pivot. Place smaller elements left and larger right. Recursively sort partitions.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def quick_sort(arr: list[int]) -&gt; None:&#10;    def partition(low, high):&#10;        pivot = arr[low]&#10;        i, j = low, high&#10;        while i &lt; j:&#10;            while i &lt;= high - 1 and arr[i] &lt;= pivot: i += 1&#10;            while j &gt;= low + 1 and arr[j] &gt; pivot: j -= 1&#10;            if i &lt; j: arr[i], arr[j] = arr[j], arr[i]&#10;        arr[low], arr[j] = arr[j], arr[low]&#10;        return j&#10;        &#10;    def helper(low, high):&#10;        if low &lt; high:&#10;            p_idx = partition(low, high)&#10;            helper(low, p_idx - 1)&#10;            helper(p_idx + 1, high)&#10;            &#10;    helper(0, len(arr) - 1)</code></pre></details></td>
    </tr>
    <tr>
      <td>6</td>
      <td>Sort 06 Merge Sort<br><br></b> <a href="https://leetcode.com/problems/sort-an-array/" target="_blank">LeetCode 912</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, Apna College</details></td>
      <td>**Example 1:** Input: nums = [5,2,3,1], Output: [1,2,3,5]</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Divide and Conquer. Split array into halves until size 1. Merge sorted halves using a temporary array.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def mergeSort(arr: list[int]) -&gt; list[int]:&#10;    if len(arr) &lt;= 1: return arr&#10;    mid = len(arr) // 2&#10;    left = mergeSort(arr[:mid])&#10;    right = mergeSort(arr[mid:])&#10;    &#10;    res = []&#10;    i = j = 0&#10;    while i &lt; len(left) and j &lt; len(right):&#10;        if left[i] &lt;= right[j]:&#10;            res.append(left[i]); i += 1&#10;        else:&#10;            res.append(right[j]); j += 1&#10;    res.extend(left[i:])&#10;    res.extend(right[j:])&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td>7</td>
      <td>Bs 07 Binary Search<br><br></b> <a href="https://leetcode.com/problems/binary-search/" target="_blank">LeetCode 704</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: nums = [-1,0,3,5,9,12], target = 9, Output: 4</td>
      <td><b>Time:</b> O(log N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><b>Explanation:</b> Standard Iterative approach. Maintain `low` and `high` boundaries, shrinking the search space by half.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def search(nums: list[int], target: int) -&gt; int:&#10;    low, high = 0, len(nums) - 1&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        if nums[mid] == target:&#10;            return mid&#10;        elif nums[mid] &lt; target:&#10;            low = mid + 1&#10;        else:&#10;            high = mid - 1&#10;    return -1</code></pre></details></td>
    </tr>
    <tr>
      <td>8</td>
      <td>Bs 08 Lower Bound<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: arr = [1,2,8,10,11,12,19], target = 0, Output: 0</td>
      <td><b>Time:</b> O(log N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><b>Explanation:</b> When `nums[mid] >= target`, it is a potential answer. Store it and search left (`high = mid - 1`) for smaller potentials.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def lowerBound(arr: list[int], n: int, x: int) -&gt; int:&#10;    low, high = 0, n - 1&#10;    ans = n&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        if arr[mid] &gt;= x:&#10;            ans = mid&#10;            high = mid - 1&#10;        else:&#10;            low = mid + 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>9</td>
      <td>Bs 09 Find First And Last Position Of Element<br><br></b> <a href="https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/" target="_blank">LeetCode 34</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: nums = [5,7,7,8,8,10], target = 8, Output: [3,4]</td>
      <td><b>Time:</b> O(log N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><b>Explanation:</b> Run Binary Search twice. Once to find the first occurrence (bias left), once to find the last occurrence (bias right).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def searchRange(nums: list[int], target: int) -&gt; list[int]:&#10;    def findBound(isFirst):&#10;        low, high, ans = 0, len(nums) - 1, -1&#10;        while low &lt;= high:&#10;            mid = low + (high - low) // 2&#10;            if nums[mid] == target:&#10;                ans = mid&#10;                if isFirst: high = mid - 1&#10;                else: low = mid + 1&#10;            elif nums[mid] &lt; target:&#10;                low = mid + 1&#10;            else:&#10;                high = mid - 1&#10;        return ans&#10;    return [findBound(True), findBound(False)]</code></pre></details></td>
    </tr>
    <tr>
      <td>10</td>
      <td>Bs 10 Search In Rotated Sorted Array<br><br></b> <a href="https://leetcode.com/problems/search-in-rotated-sorted-array/" target="_blank">LeetCode 33</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4</td>
      <td><b>Time:</b> O(log N) (Constraint)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Identify the sorted half. Check if target lies within the boundaries of the sorted half. If yes, shrink to that half; else, shrink to the other.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def search(nums: list[int], target: int) -&gt; int:&#10;    low, high = 0, len(nums) - 1&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        if nums[mid] == target: return mid&#10;        &#10;        if nums[low] &lt;= nums[mid]:&#10;            if nums[low] &lt;= target &lt;= nums[mid]:&#10;                high = mid - 1&#10;            else:&#10;                low = mid + 1&#10;        else:&#10;            if nums[mid] &lt;= target &lt;= nums[high]:&#10;                low = mid + 1&#10;            else:&#10;                high = mid - 1&#10;    return -1</code></pre></details></td>
    </tr>
    <tr>
      <td>11</td>
      <td>Bs 11 Koko Eating Bananas<br><br></b> <a href="https://leetcode.com/problems/koko-eating-bananas/" target="_blank">LeetCode 875</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: piles = [3,6,7,11], h = 8, Output: 4<br><br>**Note (Constraint):** Binary Search on Answers.</td>
      <td><b>Time:</b> O(N log(Max(P))) (Constraint)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Search space is `1` to `max(piles)`. For a mid `k`, calculate hours required. If `hours <= h`, it's a valid answer, but search left for smaller `k`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import math&#10;def minEatingSpeed(piles: list[int], h: int) -&gt; int:&#10;    def canEat(k):&#10;        hours = sum(math.ceil(pile / k) for pile in piles)&#10;        return hours &lt;= h&#10;        &#10;    low, high = 1, max(piles)&#10;    ans = high&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        if canEat(mid):&#10;            ans = mid&#10;            high = mid - 1&#10;        else:&#10;            low = mid + 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>12</td>
      <td>Bs 12 Find Minimum In Rotated Sorted Array<br><br></b> <a href="https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/" target="_blank">LeetCode 153</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet, Apna College</details></td>
      <td>**Example 1:** Input: nums = [3,4,5,1,2], Output: 1</td>
      <td><b>Time:</b> O(log N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Binary Search. Compare mid with right pointer. If nums[mid] > nums[right], the min is in the right half. Else, the min is in the left half including mid.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findMin(nums: List[int]) -&gt; int:&#10;    left, right = 0, len(nums) - 1&#10;    while left &lt; right:&#10;        mid = left + (right - left) // 2&#10;        if nums[mid] &gt; nums[right]: left = mid + 1&#10;        else: right = mid&#10;    return nums[left]</code></pre></details></td>
    </tr>
    <tr>
      <td>13</td>
      <td>Bs 13 Find Peak Element<br><br></b> <a href="https://leetcode.com/problems/find-peak-element/" target="_blank">LeetCode 162</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet, Apna College</details></td>
      <td>**Example 1:** Input: nums = [1,2,3,1], Output: 2</td>
      <td><b>Time:</b> O(log N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Binary Search. If nums[mid] < nums[mid+1], we are on an ascending slope, so a peak must be to the right. Otherwise, we are on a descending slope, peak is to the left (including mid).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findPeakElement(nums: List[int]) -&gt; int:&#10;    left, right = 0, len(nums) - 1&#10;    while left &lt; right:&#10;        mid = left + (right - left) // 2&#10;        if nums[mid] &lt; nums[mid+1]: left = mid + 1&#10;        else: right = mid&#10;    return left</code></pre></details></td>
    </tr>
    <tr>
      <td>14</td>
      <td>Bs 14 Allocate Minimum Number Of Pages<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td>**Example 1:** Input: N=4, A=[12,34,67,90], M=2, Output: 113</td>
      <td><b>Time:</b> O(N * log(sum(A) - max(A)))<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Binary Search on Answer. The search space for pages is from `max(A)` to `sum(A)`. For a given `mid`, check if books can be allocated to `<= M` students without any student exceeding `mid` pages.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findPages(A: List[int], N: int, M: int) -&gt; int:&#10;    if M &gt; N: return -1&#10;    def isPossible(maxPages):&#10;        students, currentPages = 1, 0&#10;        for pages in A:&#10;            if pages &gt; maxPages: return False&#10;            if currentPages + pages &gt; maxPages:&#10;                students += 1&#10;                currentPages = pages&#10;            else:&#10;                currentPages += pages&#10;        return students &lt;= M&#10;    low, high = max(A), sum(A)&#10;    ans = -1&#10;    while low &lt;= high:&#10;        mid = (low + high) // 2&#10;        if isPossible(mid):&#10;            ans = mid; high = mid - 1&#10;        else: low = mid + 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>15</td>
      <td>Bs 15 Kth Element Of Two Sorted Arrays<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: arr1 = [2, 3, 6, 7, 9], arr2 = [1, 4, 8, 10], k = 5, Output: 6</td>
      <td><b>Time:</b> O(log(min(n, m)))<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Binary search on the smaller array. Similar to Median of two sorted arrays, but the left partition size is strictly `k`. Search space for `cut1` is `[max(0, k-m), min(k, n)]`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def kthElement(arr1: List[int], arr2: List[int], n: int, m: int, k: int) -&gt; int:&#10;    if n &gt; m: return kthElement(arr2, arr1, m, n, k)&#10;    low, high = max(0, k - m), min(k, n)&#10;    while low &lt;= high:&#10;        cut1 = (low + high) // 2&#10;        cut2 = k - cut1&#10;        left1 = float(&#x27;-inf&#x27;) if cut1 == 0 else arr1[cut1-1]&#10;        left2 = float(&#x27;-inf&#x27;) if cut2 == 0 else arr2[cut2-1]&#10;        right1 = float(&#x27;inf&#x27;) if cut1 == n else arr1[cut1]&#10;        right2 = float(&#x27;inf&#x27;) if cut2 == m else arr2[cut2]&#10;        if left1 &lt;= right2 and left2 &lt;= right1: return max(left1, left2)&#10;        elif left1 &gt; right2: high = cut1 - 1&#10;        else: low = cut1 + 1&#10;    return 1</code></pre></details></td>
    </tr>
    <tr>
      <td>16</td>
      <td>Bs 16 Search In Rotated Sorted Array Ii<br><br></b> <a href="https://leetcode.com/problems/search-in-rotated-sorted-array-ii/" target="_blank">LeetCode 81</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td>**Example 1:** Input: nums = [2,5,6,0,0,1,2], target = 0, Output: true</td>
      <td><b>Time:</b> O(log N) average, O(N) worst case<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> If `nums[low] == nums[mid] == nums[high]`, shrink the search space by `low++` and `high--`. Otherwise, proceed with the standard rotated binary search.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def search(nums: List[int], target: int) -&gt; bool:&#10;    low, high = 0, len(nums) - 1&#10;    while low &lt;= high:&#10;        mid = (low + high) // 2&#10;        if nums[mid] == target: return True&#10;        if nums[low] == nums[mid] == nums[high]:&#10;            low += 1; high -= 1; continue&#10;        if nums[low] &lt;= nums[mid]:&#10;            if nums[low] &lt;= target &lt;= nums[mid]: high = mid - 1&#10;            else: low = mid + 1&#10;        else:&#10;            if nums[mid] &lt;= target &lt;= nums[high]: low = mid + 1&#10;            else: high = mid - 1&#10;    return False</code></pre></details></td>
    </tr>
    <tr>
      <td>17</td>
      <td>Bs 17 Minimum Days To Make M Bouquets<br><br></b> <a href="https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/" target="_blank">LeetCode 1482</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td>**Example 1:** Find day threshold.</td>
      <td><b>Time:</b> O(N log(maxD - minD))<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Binary search on days from `min(bloom)` to `max(bloom)`. Count consecutive bloomed flowers, if it reaches `k`, form a bouquet. Return minimum valid day.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minDays(bloomDay: List[int], m: int, k: int) -&gt; int:&#10;    if m * k &gt; len(bloomDay): return -1&#10;    def isPossible(day):&#10;        count, bouquets = 0, 0&#10;        for d in bloomDay:&#10;            if d &lt;= day: count += 1&#10;            else: bouquets += count // k; count = 0&#10;        bouquets += count // k&#10;        return bouquets &gt;= m&#10;    low, high = min(bloomDay), max(bloomDay)&#10;    ans = -1&#10;    while low &lt;= high:&#10;        mid = (low + high) // 2&#10;        if isPossible(mid): ans = mid; high = mid - 1&#10;        else: low = mid + 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>18</td>
      <td>Bs 18 Find The Smallest Divisor Given A Threshold<br><br></b> <a href="https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/" target="_blank">LeetCode 1283</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td>**Example 1:** Summing ceils.</td>
      <td><b>Time:</b> O(N log(max(nums)))<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Binary search the divisor from 1 to `max(nums)`. Compute `sum(ceil(num / mid))`. If sum <= threshold, shrink high.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import math&#10;def smallestDivisor(nums: List[int], threshold: int) -&gt; int:&#10;    low, high = 1, max(nums)&#10;    while low &lt;= high:&#10;        mid = (low + high) // 2&#10;        total = sum(math.ceil(num / mid) for num in nums)&#10;        if total &lt;= threshold: high = mid - 1&#10;        else: low = mid + 1&#10;    return low</code></pre></details></td>
    </tr>
    <tr>
      <td>19</td>
      <td>Bs 19 Capacity To Ship Packages Within D Days<br><br></b> <a href="https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/" target="_blank">LeetCode 1011</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td>**Example 1:** Find ship capacity.</td>
      <td><b>Time:</b> O(N log(sum - max))<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Binary search on capacity. Low = `max(weights)`, High = `sum(weights)`. Iterate through packages and accumulate weight, increment day if limit is exceeded.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def shipWithinDays(weights: List[int], days: int) -&gt; int:&#10;    def canShip(cap):&#10;        d, load = 1, 0&#10;        for w in weights:&#10;            if load + w &gt; cap: d += 1; load = w&#10;            else: load += w&#10;        return d &lt;= days&#10;    low, high = max(weights), sum(weights)&#10;    while low &lt;= high:&#10;        mid = (low + high) // 2&#10;        if canShip(mid): high = mid - 1&#10;        else: low = mid + 1&#10;    return low</code></pre></details></td>
    </tr>
    <tr>
      <td>20</td>
      <td>Bs 20 Kth Missing Positive Number<br><br></b> <a href="https://leetcode.com/problems/kth-missing-positive-number/" target="_blank">LeetCode 1539</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td>**Example 1:** Calculate missing.</td>
      <td><b>Time:</b> O(log N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Binary search. At index `mid`, the number of missing elements before `arr[mid]` is `arr[mid] - (mid + 1)`. If this is < `k`, search right `low = mid + 1`. Else search left `high = mid - 1`. Ans is `high + 1 + k` or `low + k`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findKthPositive(arr: List[int], k: int) -&gt; int:&#10;    low, high = 0, len(arr) - 1&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        missing = arr[mid] - (mid + 1)&#10;        if missing &lt; k: low = mid + 1&#10;        else: high = mid - 1&#10;    return low + k</code></pre></details></td>
    </tr>
    <tr>
      <td>21</td>
      <td>Bs 21 Aggressive Cows<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/aggressive-cows/0" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td>**Example 1:** Minimax binary search.</td>
      <td><b>Time:</b> O(N log N + N log(Max-Min))<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Sort the stalls. Binary search for distance from `1` to `max-min`. For a distance `mid`, check if we can place all `C` cows such that distance between any two is >= `mid`. If possible, move `low = mid + 1` to maximize it, else `high = mid - 1`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def aggressiveCows(stalls: List[int], k: int) -&gt; int:&#10;    stalls.sort()&#10;    def can_place(dist):&#10;        cnt_cows = 1&#10;        last = stalls[0]&#10;        for i in range(1, len(stalls)):&#10;            if stalls[i] - last &gt;= dist:&#10;                cnt_cows += 1&#10;                last = stalls[i]&#10;        return cnt_cows &gt;= k&#10;    low, high = 1, stalls[-1] - stalls[0]&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        if can_place(mid): low = mid + 1&#10;        else: high = mid - 1&#10;    return high</code></pre></details></td>
    </tr>
    <tr>
      <td>22</td>
      <td>Bs 22 Split Array Largest Sum<br><br></b> <a href="https://leetcode.com/problems/split-array-largest-sum/" target="_blank">LeetCode 410</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td>**Example 1:** Equivalent to allocate books.</td>
      <td><b>Time:</b> O(N log(Sum-Max))<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Identical logic to Allocate Books. Binary search from `max(nums)` to `sum(nums)`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def splitArray(nums: List[int], k: int) -&gt; int:&#10;    def count_partitions(max_sum):&#10;        partitions, subarray_sum = 1, 0&#10;        for num in nums:&#10;            if subarray_sum + num &lt;= max_sum:&#10;                subarray_sum += num&#10;            else:&#10;                partitions += 1&#10;                subarray_sum = num&#10;        return partitions&#10;    low, high = max(nums), sum(nums)&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        if count_partitions(mid) &gt; k: low = mid + 1&#10;        else: high = mid - 1&#10;    return low</code></pre></details></td>
    </tr>
    <tr>
      <td>23</td>
      <td>Bs 23 Painters Partition Problem<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/the-painters-partition-problem1535/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td>**Example 1:** Minimax identical to book allocation.</td>
      <td><b>Time:</b> O(N log(Sum-Max))<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Identical to Allocate Books and Split Array Largest Sum. Binary search `max(boards)` to `sum(boards)`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findLargestMinDistance(boards: List[int], k: int) -&gt; int:&#10;    def count_painters(time):&#10;        painters, boards_painter = 1, 0&#10;        for b in boards:&#10;            if boards_painter + b &lt;= time:&#10;                boards_painter += b&#10;            else:&#10;                painters += 1&#10;                boards_painter = b&#10;        return painters&#10;    low, high = max(boards), sum(boards)&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        if count_painters(mid) &gt; k: low = mid + 1&#10;        else: high = mid - 1&#10;    return low</code></pre></details></td>
    </tr>
    <tr>
      <td>24</td>
      <td>Bs 24 Minimize Max Distance To Gas Station<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/minimize-max-distance-to-gas-station/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td>**Example 1:** Double binary search.</td>
      <td><b>Time:</b> O(N log(MaxDist / 1e-6))<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Binary search on the real answer (distance) with a precision (e.g., 1e-6). For a given `mid` distance, count how many gas stations need to be inserted in each gap: `ceil((stations[i+1] - stations[i]) / mid) - 1`. If total needed > k, `low = mid`, else `high = mid`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findSmallestMaxDist(stations: List[int], k: int) -&gt; float:&#10;    def num_required(dist):&#10;        cnt = 0&#10;        for i in range(1, len(stations)):&#10;            number_in_between = int((stations[i] - stations[i-1]) / dist)&#10;            if (stations[i] - stations[i-1]) == (dist * number_in_between):&#10;                number_in_between -= 1&#10;            cnt += number_in_between&#10;        return cnt&#10;    low, high = 0, 0&#10;    for i in range(len(stations) - 1):&#10;        high = max(high, float(stations[i+1] - stations[i]))&#10;    diff = 1e-6&#10;    while high - low &gt; diff:&#10;        mid = low + (high - low) / 2.0&#10;        if num_required(mid) &gt; k: low = mid&#10;        else: high = mid&#10;    return high</code></pre></details></td>
    </tr>
    <tr>
      <td>25</td>
      <td>Bs 25 Search In A 2D Matrix Ii<br><br></b> <a href="https://leetcode.com/problems/search-a-2d-matrix-ii/" target="_blank">LeetCode 240</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td>**Example 1:** Start from top right.</td>
      <td><b>Time:</b> O(N + M)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Start from the top-right corner. If `target == current`, return true. If `target < current`, move left (`c--`). If `target > current`, move down (`r++`).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def searchMatrix(matrix: List[List[int]], target: int) -&gt; bool:&#10;    r, c = 0, len(matrix[0]) - 1&#10;    while r &lt; len(matrix) and c &gt;= 0:&#10;        if matrix[r][c] == target: return True&#10;        elif matrix[r][c] &gt; target: c -= 1&#10;        else: r += 1&#10;    return False</code></pre></details></td>
    </tr>
    <tr>
      <td>26</td>
      <td>Bs 26 Find A Peak Element Ii<br><br></b> <a href="https://leetcode.com/problems/find-a-peak-element-ii/" target="_blank">LeetCode 1901</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td>**Example 1:** Binary search on columns.</td>
      <td><b>Time:</b> O(N log M)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Binary search on columns. Find middle column, find max element in this column. Compare it with its left and right neighbors. If it's > both, it's a peak. If left is greater, peak exists in left half. Else, peak exists in right half.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findPeakGrid(mat: List[List[int]]) -&gt; List[int]:&#10;    n, m = len(mat), len(mat[0])&#10;    low, high = 0, m - 1&#10;    while low &lt;= high:&#10;        mid = (low + high) // 2&#10;        max_row = 0&#10;        for i in range(n):&#10;            if mat[i][mid] &gt; mat[max_row][mid]: max_row = i&#10;        left = mat[max_row][mid-1] if mid - 1 &gt;= 0 else -1&#10;        right = mat[max_row][mid+1] if mid + 1 &lt; m else -1&#10;        if mat[max_row][mid] &gt; left and mat[max_row][mid] &gt; right:&#10;            return [max_row, mid]&#10;        elif mat[max_row][mid] &lt; left:&#10;            high = mid - 1&#10;        else:&#10;            low = mid + 1&#10;    return [-1, -1]</code></pre></details></td>
    </tr>
    <tr>
      <td>27</td>
      <td>Bs 27 Matrix Median<br><br></b> <a href="https://www.interviewbit.com/problems/matrix-median/" target="_blank">InterviewBit</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td>**Example 1:** Binary search on answer range.</td>
      <td><b>Time:</b> O(32 * N log M)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Binary search on the value range `[1, 10^9]`. For a candidate `mid`, count how many numbers are `<= mid` across all rows using `upper_bound`. If count `> (N*M)/2`, `mid` could be median, search lower. Else search higher.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import bisect&#10;def findMedian(A: List[List[int]]) -&gt; int:&#10;    low, high = 1, int(1e9)&#10;    n, m = len(A), len(A[0])&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        cnt = sum(bisect.bisect_right(row, mid) for row in A)&#10;        if cnt &lt;= (n * m) // 2:&#10;            low = mid + 1&#10;        else:&#10;            high = mid - 1&#10;    return low</code></pre></details></td>
    </tr>
    <tr>
      <td>28</td>
      <td>Bs 28 Kth Smallest Number In Multiplication Table<br><br></b> <a href="https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/" target="_blank">LeetCode 668</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td>**Example 1:** Binary Search on answer.</td>
      <td><b>Time:</b> O(m * log(m*n))<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Binary search on range `[1, m*n]`. For a value `mid`, the number of elements `<= mid` in row `i` is `min(mid / i, n)`. Sum this for all rows to get total count. If count >= k, search left. Else search right.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findKthNumber(m: int, n: int, k: int) -&gt; int:&#10;    low, high = 1, m * n&#10;    while low &lt; high:&#10;        mid = low + (high - low) // 2&#10;        count = sum(min(mid // i, n) for i in range(1, m + 1))&#10;        if count &gt;= k:&#10;            high = mid&#10;        else:&#10;            low = mid + 1&#10;    return low</code></pre></details></td>
    </tr>
    <tr>
      <td>29</td>
      <td>Bs 29 Find K Th Smallest Pair Distance<br><br></b> <a href="https://leetcode.com/problems/find-k-th-smallest-pair-distance/" target="_blank">LeetCode 719</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td>**Example 1:** Sort and binary search on distance.</td>
      <td><b>Time:</b> O(N log N + N log(max_dist))<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Sort array. Binary search on distance `[0, nums.back() - nums.front()]`. For a candidate `mid`, count pairs with distance `<= mid` using a sliding window. If count >= k, search left. Else search right.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def smallestDistancePair(nums: List[int], k: int) -&gt; int:&#10;    nums.sort()&#10;    low, high = 0, nums[-1] - nums[0]&#10;    def countPairs(mid):&#10;        count, l = 0, 0&#10;        for r in range(len(nums)):&#10;            while nums[r] - nums[l] &gt; mid: l += 1&#10;            count += (r - l)&#10;        return count&#10;    while low &lt; high:&#10;        mid = low + (high - low) // 2&#10;        if countPairs(mid) &gt;= k:&#10;            high = mid&#10;        else:&#10;            low = mid + 1&#10;    return low</code></pre></details></td>
    </tr>
    <tr>
      <td>30</td>
      <td>Bs 30 Aggressive Cows<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/aggressive-cows/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td>**Example 1:** Binary Search on Answer.</td>
      <td><b>Time:</b> O(N log N + N log(max_val))<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Sort array. Maximize the minimum distance. Search space from `1` to `max(arr) - min(arr)`. Function `isPossible(mid)` checks if we can place `K` cows such that distance between any two is at least `mid`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def solve(n: int, k: int, stalls: List[int]) -&gt; int:&#10;    stalls.sort()&#10;    def isPossible(mid):&#10;        cows, lastPos = 1, stalls[0]&#10;        for i in range(1, n):&#10;            if stalls[i] - lastPos &gt;= mid:&#10;                cows += 1&#10;                lastPos = stalls[i]&#10;                if cows == k: return True&#10;        return False&#10;    low, high = 1, stalls[-1] - stalls[0]&#10;    ans = -1&#10;    while low &lt;= high:&#10;        mid = (low + high) // 2&#10;        if isPossible(mid):&#10;            ans = mid&#10;            low = mid + 1&#10;        else:&#10;            high = mid - 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>31</td>
      <td>Bs 31 Roti Prata Spoj<br><br></b> <a href="https://www.spoj.com/problems/PRATA/" target="_blank">SPOJ</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td>**Example 1:** Binary Search on Answer.</td>
      <td><b>Time:</b> O(L * log(max_time))<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Search space is `0` to `max_time`, where `max_time` is the time taken by the fastest cook to make all `P` pratas alone. `isPossible(mid)` checks if the total pratas made by all cooks in `mid` time is at least `P`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minTime(p: int, rank: List[int]) -&gt; int:&#10;    def isPossible(mid):&#10;        count = 0&#10;        for r in rank:&#10;            time, j = 0, 1&#10;            while time + r * j &lt;= mid:&#10;                count += 1&#10;                time += r * j&#10;                j += 1&#10;            if count &gt;= p: return True&#10;        return count &gt;= p&#10;    low, high = 0, 10**8&#10;    ans = -1&#10;    while low &lt;= high:&#10;        mid = (low + high) // 2&#10;        if isPossible(mid):&#10;            ans = mid&#10;            high = mid - 1&#10;        else:&#10;            low = mid + 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>32</td>
      <td>Bs 32 Double Helix Spoj<br><br></b> <a href="https://www.spoj.com/problems/ANARC05B/" target="_blank">SPOJ</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td>**Example 1:** Two Pointers / Binary Search.</td>
      <td><b>Time:</b> O(N + M)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Use two pointers to traverse both sorted arrays simultaneously. Accumulate sums `sum1` and `sum2`. When elements match (intersection), add `max(sum1, sum2) + element` to the total answer and reset `sum1` and `sum2`. After the loop, add the remaining max sum.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxPathSum(arr1: List[int], arr2: List[int]) -&gt; int:&#10;    sum1 = sum2 = ans = 0&#10;    i = j = 0&#10;    n, m = len(arr1), len(arr2)&#10;    while i &lt; n and j &lt; m:&#10;        if arr1[i] &lt; arr2[j]:&#10;            sum1 += arr1[i]&#10;            i += 1&#10;        elif arr1[i] &gt; arr2[j]:&#10;            sum2 += arr2[j]&#10;            j += 1&#10;        else:&#10;            ans += max(sum1, sum2) + arr1[i]&#10;            sum1, sum2 = 0, 0&#10;            i += 1; j += 1&#10;    while i &lt; n:&#10;        sum1 += arr1[i]&#10;        i += 1&#10;    while j &lt; m:&#10;        sum2 += arr2[j]&#10;        j += 1&#10;    ans += max(sum1, sum2)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>33</td>
      <td>Bs 33 Subset Sums Spoj<br><br></b> <a href="https://www.spoj.com/problems/SUBSUMS/" target="_blank">SPOJ</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td>**Example 1:** Meet in the Middle.</td>
      <td><b>Time:</b> O(2^(N/2) * log(2^(N/2)))<br><b>Space:</b> O(2^(N/2))</td>
      <td><b>Explanation:</b> Divide the array into two halves. Find all possible subset sums for both halves (`sum1` and `sum2`). Sort `sum2`. For each sum in `sum1`, we need to find the number of elements in `sum2` that satisfy `A - sum <= x <= B - sum`. This can be done using Binary Search (`upper_bound` - `lower_bound`).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import bisect&#10;def solve(arr: List[int], A: int, B: int) -&gt; int:&#10;    n = len(arr)&#10;    def get_sums(arr_slice):&#10;        sums = [0]&#10;        for x in arr_slice:&#10;            sums += [s + x for s in sums]&#10;        return sums&#10;    left = get_sums(arr[:n//2])&#10;    right = sorted(get_sums(arr[n//2:]))&#10;    count = 0&#10;    for x in left:&#10;        low = bisect.bisect_left(right, A - x)&#10;        high = bisect.bisect_right(right, B - x)&#10;        count += (high - low)&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td>34</td>
      <td>Bs 34 Smallest Factorial Number<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/smallest-factorial-number5929/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td>**Example 1:** Binary Search.</td>
      <td><b>Time:</b> O(log_5(N) * log(5*N))<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Trailing zeros depend on number of 5s. Find count of 5s in `mid!`. Use binary search on the number. Low = 0, high = 5*N. If `check(mid) >= n`, `ans = mid` and `high = mid - 1`. Else `low = mid + 1`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findNum(n: int) -&gt; int:&#10;    if n == 1: return 5&#10;    def check(p):&#10;        count, f = 0, 5&#10;        while f &lt;= p:&#10;            count += p // f&#10;            f *= 5&#10;        return count &gt;= n&#10;    low, high = 0, 5 * n&#10;    ans = 0&#10;    while low &lt;= high:&#10;        mid = (low + high) // 2&#10;        if check(mid):&#10;            ans = mid&#10;            high = mid - 1&#10;        else:&#10;            low = mid + 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>35</td>
      <td>Bs 35 Value Equal To Index Value<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/value-equal-to-index-value1330/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td>**Example 1:** Linear scan.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Iterate through the array. If the value at `i` is equal to `i + 1`, append it to the result array.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def valueEqualToIndex(arr, n):&#10;    ans = []&#10;    for i in range(n):&#10;        if arr[i] == i + 1:&#10;            ans.append(arr[i])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>36</td>
      <td>Bs 36 Count Squares<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/count-squares3649/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td>**Example 1:** Square root.</td>
      <td><b>Time:</b> O(1)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> The number of perfect squares less than `N` is equal to `sqrt(N - 1)` rounded down.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import math&#10;def countSquares(N):&#10;    return int(math.sqrt(N - 1))</code></pre></details></td>
    </tr>
    <tr>
      <td>37</td>
      <td>Bs 37 Middle Of Three<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/middle-of-three2926/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td>**Example 1:** Simple if-else.</td>
      <td><b>Time:</b> O(1)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Compare the numbers. If A is between B and C, return A. If B is between A and C, return B. Else return C.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def middle(A, B, C):&#10;    if (A &lt; B and B &lt; C) or (C &lt; B and B &lt; A): return B&#10;    if (B &lt; A and A &lt; C) or (C &lt; A and A &lt; B): return A&#10;    return C</code></pre></details></td>
    </tr>
    <tr>
      <td>38</td>
      <td>Bs 38 Majority Element<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/majority-element-1587115620/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z, SDE Sheet</details></td>
      <td>**Example 1:** Moore's Voting Algorithm.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Use Moore's Voting Algorithm to find a candidate for majority element. Then count the occurrences of the candidate in the array to verify if it appears more than N/2 times.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def majorityElement(a, size):&#10;    count = 0&#10;    candidate = -1&#10;    for num in a:&#10;        if count == 0:&#10;            candidate = num&#10;            count = 1&#10;        elif num == candidate: count += 1&#10;        else: count -= 1&#10;    count = 0&#10;    for num in a:&#10;        if num == candidate: count += 1&#10;    return candidate if count &gt; size // 2 else -1</code></pre></details></td>
    </tr>
    <tr>
      <td>39</td>
      <td>Bs 39 Searching In An Array Where Adjacent Differ By At Most K<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/searching-in-an-array-where-adjacent-differ-by-at-most-k0456/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td>**Example 1:** Jump Search.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Instead of linear search, we can jump ahead. The minimum jump we can make from index `i` to reach `x` is `abs(arr[i] - x) / k`. We jump this amount and check if we found it. Make sure jump is at least 1.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def search(arr, n, x, k):&#10;    i = 0&#10;    while i &lt; n:&#10;        if arr[i] == x: return i&#10;        i = i + max(1, abs(arr[i] - x) // k)&#10;    return -1</code></pre></details></td>
    </tr>
    <tr>
      <td>40</td>
      <td>Bs 40 Find A Pair With The Given Difference<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/find-pair-given-difference1559/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td>**Example 1:** Sort and two pointers.</td>
      <td><b>Time:</b> O(L log L)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Sort the array. Use two pointers `i = 0` and `j = 1`. If `arr[j] - arr[i] == N` and `i != j`, return true. If difference < N, `j++`. Else `i++`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findPair(arr, size, n):&#10;    arr.sort()&#10;    i, j = 0, 1&#10;    while i &lt; size and j &lt; size:&#10;        if i != j and arr[j] - arr[i] == n: return True&#10;        elif arr[j] - arr[i] &lt; n: j += 1&#10;        else: i += 1&#10;    return False</code></pre></details></td>
    </tr>
    <tr>
      <td>41</td>
      <td>Bs 41 Find Four Elements That Sum To A Given Value<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/find-all-four-sum-numbers1732/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z, SDE Sheet</details></td>
      <td>**Example 1:** Two loops and two pointers.</td>
      <td><b>Time:</b> O(N^3)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Sort the array. Use two nested loops for the first two elements. Then use two pointers for the remaining two elements to find the target sum. Skip duplicates at all levels.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def fourSum(arr, k):&#10;    ans = []&#10;    n = len(arr)&#10;    arr.sort()&#10;    for i in range(n):&#10;        if i &gt; 0 and arr[i] == arr[i-1]: continue&#10;        for j in range(i + 1, n):&#10;            if j &gt; i + 1 and arr[j] == arr[j-1]: continue&#10;            left, right = j + 1, n - 1&#10;            while left &lt; right:&#10;                total = arr[i] + arr[j] + arr[left] + arr[right]&#10;                if total == k:&#10;                    ans.append([arr[i], arr[j], arr[left], arr[right]])&#10;                    left += 1; right -= 1&#10;                    while left &lt; right and arr[left] == arr[left-1]: left += 1&#10;                    while left &lt; right and arr[right] == arr[right+1]: right -= 1&#10;                elif total &lt; k: left += 1&#10;                else: right -= 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>42</td>
      <td>Bs 42 Row With Max 1S<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/row-with-max-1s0023/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td>**Example 1:** Lower Bound per row.</td>
      <td><b>Time:</b> O(N log M)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Since rows are sorted, use binary search (`lower_bound` of 1) to find the first index of 1 in each row. The number of 1s is `m - index`. Keep track of the row with the maximum 1s.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def rowWithMax1s(arr, n, m):&#10;    def lowerBound(a, m, x):&#10;        low, high, ans = 0, m - 1, m&#10;        while low &lt;= high:&#10;            mid = (low + high) // 2&#10;            if a[mid] &gt;= x:&#10;                ans = mid&#10;                high = mid - 1&#10;            else:&#10;                low = mid + 1&#10;        return ans&#10;    max_cnt = 0&#10;    index = -1&#10;    for i in range(n):&#10;        cnt_ones = m - lowerBound(arr[i], m, 1)&#10;        if cnt_ones &gt; max_cnt:&#10;            max_cnt = cnt_ones&#10;            index = i&#10;    return index</code></pre></details></td>
    </tr>
  </tbody>
</table>
