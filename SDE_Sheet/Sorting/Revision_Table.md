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
      <td rowspan="1">1</td>
      <td rowspan="1">Sort 04 Merge Sort<br><br></b> <a href='https://www.geeksforgeeks.org/problems/merge-sort/1' target='_blank'>GeeksforGeeks</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: N = 5, arr[] = {4, 1, 3, 9, 7}, Output: 1 3 4 7 9</td>
      <td><b>Time:</b> O(N log N) (Constraint)<br><b>Space:</b> O(N) (Trade-off)</td>
      <td>Extra array for merging</td>
      <td><b>Stable Sort:</b> Maintains relative order of equal elements. Requires `O(N)` extra space to merge.</td>
      <td><b>Explanation:</b> Recursively split array in half, sort them, and merge the sorted halves.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def merge_sort(arr: list[int]) -&gt; None:&#10;    def merge(low, mid, high):&#10;        temp = []&#10;        left, right = low, mid + 1&#10;        while left &lt;= mid and right &lt;= high:&#10;            if arr[left] &lt;= arr[right]:&#10;                temp.append(arr[left])&#10;                left += 1&#10;            else:&#10;                temp.append(arr[right])&#10;                right += 1&#10;        while left &lt;= mid:&#10;            temp.append(arr[left]); left += 1&#10;        while right &lt;= high:&#10;            temp.append(arr[right]); right += 1&#10;        for i in range(len(temp)):&#10;            arr[low + i] = temp[i]&#10;            &#10;    def helper(low, high):&#10;        if low &gt;= high: return&#10;        mid = (low + high) // 2&#10;        helper(low, mid)&#10;        helper(mid + 1, high)&#10;        merge(low, mid, high)&#10;        &#10;    helper(0, len(arr) - 1)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">2</td>
      <td rowspan="1">Sort 05 Quick Sort<br><br></b> <a href='https://www.geeksforgeeks.org/problems/quick-sort/1' target='_blank'>GeeksforGeeks</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: N = 5, arr[] = {4, 1, 3, 9, 7}, Output: 1 3 4 7 9</td>
      <td><b>Time:</b> O(N log N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td>-</td>
      <td><b>Worst Case:</b> `O(N^2)` if array is already sorted and pivot is extreme. Avoided by randomized pivot.</td>
      <td><b>Explanation:</b> Pick a pivot. Place smaller elements left and larger right. Recursively sort partitions.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def quick_sort(arr: list[int]) -&gt; None:&#10;    def partition(low, high):&#10;        pivot = arr[low]&#10;        i, j = low, high&#10;        while i &lt; j:&#10;            while i &lt;= high - 1 and arr[i] &lt;= pivot: i += 1&#10;            while j &gt;= low + 1 and arr[j] &gt; pivot: j -= 1&#10;            if i &lt; j: arr[i], arr[j] = arr[j], arr[i]&#10;        arr[low], arr[j] = arr[j], arr[low]&#10;        return j&#10;        &#10;    def helper(low, high):&#10;        if low &lt; high:&#10;            p_idx = partition(low, high)&#10;            helper(low, p_idx - 1)&#10;            helper(p_idx + 1, high)&#10;            &#10;    helper(0, len(arr) - 1)</code></pre></details></td>
    </tr>
  </tbody>
</table>
