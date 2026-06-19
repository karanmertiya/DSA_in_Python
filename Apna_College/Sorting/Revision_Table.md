# Sorting Revision Table

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
      <td>Sort 02 Merge Sort<br><br></b> <a href='https://leetcode.com/problems/sort-an-array/' target='_blank'>LeetCode 912</a></td>
      <td><b>Example 1:</b> Input: nums = [5,2,3,1], Output: [1,2,3,5]</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td><b>In-place illusion:</b> True Merge Sort requires `O(N)` auxiliary space for the `temp` merge array. An in-place version exists but degrades time complexity.</td>
      <td><b>Explanation:</b> Divide and Conquer. Split array into halves until size 1. Merge sorted halves using a temporary array.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def mergeSort(arr: list[int]) -&gt; list[int]:&#10;    if len(arr) &lt;= 1: return arr&#10;    mid = len(arr) // 2&#10;    left = mergeSort(arr[:mid])&#10;    right = mergeSort(arr[mid:])&#10;    &#10;    res = []&#10;    i = j = 0&#10;    while i &lt; len(left) and j &lt; len(right):&#10;        if left[i] &lt;= right[j]:&#10;            res.append(left[i]); i += 1&#10;        else:&#10;            res.append(right[j]); j += 1&#10;    res.extend(left[i:])&#10;    res.extend(right[j:])&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td>2</td>
      <td>Sort 03 Quick Sort<br><br></b> <a href='https://leetcode.com/problems/sort-an-array/' target='_blank'>LeetCode 912</a></td>
      <td><b>Example 1:</b> Input: nums = [5,2,3,1], Output: [1,2,3,5]</td>
      <td><b>Time:</b> O(N log N) Avg, O(N<sup>2</sup>) Worst<br><b>Space:</b> O(log N)</td>
      <td><code>std::swap</code></td>
      <td><b>Worst Case:</b> If array is already sorted and we pick the first element as pivot, it devolves to `O(N^2)`. Randomizing the pivot mitigates this.</td>
      <td><b>Explanation:</b> Divide and Conquer. Pick a pivot (e.g., first element), partition elements smaller to the left and larger to the right. Recurse.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def quickSort(arr: list[int], low: int, high: int):&#10;    if low &lt; high:&#10;        pivot = arr[low]&#10;        i, j = low, high&#10;        while i &lt; j:&#10;            while arr[i] &lt;= pivot and i &lt;= high - 1: i += 1&#10;            while arr[j] &gt; pivot and j &gt;= low + 1: j -= 1&#10;            if i &lt; j: arr[i], arr[j] = arr[j], arr[i]&#10;        arr[low], arr[j] = arr[j], arr[low]&#10;        quickSort(arr, low, j - 1)&#10;        quickSort(arr, j + 1, high)&#10;    return arr</code></pre></details></td>
    </tr>
  </tbody>
</table>
