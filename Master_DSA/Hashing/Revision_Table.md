# Hashing Revision Table

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
      <td>Hash 01 Count Frequencies<br><br></b> <a href="https://www.geeksforgeeks.org/problems/frequency-of-array-elements-1587115620/1" target="_blank">GeeksforGeeks</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: arr = [10, 5, 10, 15, 10, 5], Output: 10->3, 5->2, 15->1<br><br>**Note (Constraint):** 1 &le; N &le; 10<sup>5</sup></td>
      <td><b>Time:</b> O(N<sup>2</sup>) (Trade-off)<br><b>Space:</b> O(N) (Trade-off)</td>
      <td><b>Explanation:</b> Use two nested loops to count occurrences. Mark visited elements to avoid recounting.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def count_freq(arr: list[int]) -&gt; None:\n    freq = {}\n    for num in arr:\n        freq[num] = freq.get(num, 0) + 1\n    for key, val in freq.items():\n        print(f&#x27;{key} {val}&#x27;)</code></pre></details></td>
    </tr>
    <tr>
      <td>2</td>
      <td>Hash 02 Highest Lowest Frequency<br><br></b> <a href="https://leetcode.com/problems/sort-array-by-increasing-frequency/" target="_blank">LeetCode 1636</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: arr = [10, 5, 10, 15, 10, 5], Output: Highest=10, Lowest=15<br><br>**Note (Constraint):** 1 &le; N &le; 10<sup>5</sup></td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(N) (Trade-off)</td>
      <td><b>Explanation:</b> Build a frequency map, then iterate through the map to find the max and min frequencies.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def find_high_low_freq(arr: list[int]) -&gt; tuple:&#10;    freq = {}&#10;    for num in arr:&#10;        freq[num] = freq.get(num, 0) + 1&#10;    &#10;    max_f, min_f = 0, float(&#x27;inf&#x27;)&#10;    max_ele, min_ele = 0, 0&#10;    &#10;    for ele, count in freq.items():&#10;        if count &gt; max_f:&#10;            max_f, max_ele = count, ele&#10;        if count &lt; min_f:&#10;            min_f, min_ele = count, ele&#10;    return max_ele, min_ele</code></pre></details></td>
    </tr>
    <tr>
      <td>3</td>
      <td>Hash 03 Intersection Of Two Arrays<br><br></b> <a href="https://leetcode.com/problems/intersection-of-two-arrays/" target="_blank">LeetCode 349</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: nums1 = [1,2,2,1], nums2 = [2,2], Output: [2]<br><br>**Note (Constraint):** 1 &le; N, M &le; 1000</td>
      <td><b>Time:</b> O(N + M) (Constraint)<br><b>Space:</b> O(N) (Trade-off)</td>
      <td><b>Explanation:</b> Store elements of the first array in a Hash Set, then iterate over the second array to find matches.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def intersection(nums1: list[int], nums2: list[int]) -&gt; list[int]:&#10;    set1 = set(nums1)&#10;    res = []&#10;    for num in nums2:&#10;        if num in set1:&#10;            res.append(num)&#10;            set1.remove(num) # Ensure uniqueness&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td>4</td>
      <td>Hash 04 Union Of Two Arrays<br><br></b> <a href="https://www.geeksforgeeks.org/problems/union-of-two-arrays3538/1" target="_blank">GeeksforGeeks</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: a = [1, 2, 3], b = [2, 3, 4], Output: [1, 2, 3, 4]<br><br>**Note (Constraint):** Arrays may not be sorted.</td>
      <td><b>Time:</b> O(N + M) (Constraint)<br><b>Space:</b> O(N + M) (Trade-off)</td>
      <td><b>Explanation:</b> Insert all elements from both arrays into a Hash Set. The Set natively drops duplicates.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def find_union(a: list[int], b: list[int]) -&gt; list[int]:&#10;    # Set union operator implicitly merges and drops duplicates&#10;    s = set(a) | set(b)&#10;    return list(s)</code></pre></details></td>
    </tr>
    <tr>
      <td>5</td>
      <td>Hash 05 Subarray With 0 Sum<br><br></b> <a href="https://www.geeksforgeeks.org/problems/subarray-with-0-sum-1587115621/1" target="_blank">GeeksforGeeks</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: arr = [4, 2, -3, 1, 6], Output: true (2, -3, 1)<br><br>**Note (Constraint):** Array contains positive and negative integers.</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(N) (Trade-off)</td>
      <td><b>Explanation:</b> Use a Prefix Sum and a Hash Set. If a prefix sum repeats, or equals 0, a 0-sum subarray exists between the identical prefix sums.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def has_zero_sum_subarray(arr: list[int]) -&gt; bool:&#10;    prefix_sums = set()&#10;    curr_sum = 0&#10;    for num in arr:&#10;        curr_sum += num&#10;        if curr_sum == 0 or curr_sum in prefix_sums:&#10;            return True&#10;        prefix_sums.add(curr_sum)&#10;    return False</code></pre></details></td>
    </tr>
    <tr>
      <td>6</td>
      <td>Hash 06 Subarray Sum Equals K<br><br></b> <a href="https://leetcode.com/problems/subarray-sum-equals-k/" target="_blank">LeetCode 560</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: nums = [1,1,1], k = 2, Output: 2<br><br>**Note (Constraint):** Negative numbers allowed, preventing pure Sliding Window approaches.</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(N) (Trade-off)</td>
      <td><b>Explanation:</b> Maintain a Hash Map of `prefix_sum` -> `frequency`. If `curr_sum - k` exists in the map, add its frequency to the count.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def subarray_sum(nums: list[int], k: int) -&gt; int:&#10;    prefix_freq = {0: 1}&#10;    count = 0&#10;    curr_sum = 0&#10;    for num in nums:&#10;        curr_sum += num&#10;        remove = curr_sum - k&#10;        if remove in prefix_freq:&#10;            count += prefix_freq[remove]&#10;        prefix_freq[curr_sum] = prefix_freq.get(curr_sum, 0) + 1&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td>7</td>
      <td>Hash 07 Longest Subarray With 0 Sum<br><br></b> <a href="https://www.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1" target="_blank">GeeksforGeeks</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: arr = [15,-2,2,-8,1,7,10,23], Output: 5<br><br>**Note (Constraint):** 1 &le; N &le; 10<sup>5</sup></td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(N) (Trade-off)</td>
      <td><b>Explanation:</b> Store `prefix_sum` -> `index` in Hash Map. If sum repeats, calculate distance `i - hash[sum]`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def max_len(arr: list[int]) -&gt; int:&#10;    prefix_index = {}&#10;    max_len = sum = 0&#10;    for i, num in enumerate(arr):&#10;        sum += num&#10;        if sum == 0:&#10;            max_len = i + 1&#10;        elif sum in prefix_index:&#10;            max_len = max(max_len, i - prefix_index[sum])&#10;        else:&#10;            prefix_index[sum] = i&#10;    return max_len</code></pre></details></td>
    </tr>
    <tr>
      <td>8</td>
      <td>Hash 08 Longest Subarray With Sum K<br><br></b> <a href="https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1" target="_blank">GeeksforGeeks</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: arr = [10, 5, 2, 7, 1, 9], k = 15, Output: 4<br><br>**Note (Constraint):** 1 &le; N &le; 10<sup>5</sup></td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(N) (Trade-off)</td>
      <td><b>Explanation:</b> Prefix Sum Map storing indices. Check if `sum - K` exists in map and calculate index difference.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def len_of_long_subarr(arr: list[int], k: int) -&gt; int:&#10;    prefix_index = {}&#10;    max_len = sum = 0&#10;    for i, num in enumerate(arr):&#10;        sum += num&#10;        if sum == k:&#10;            max_len = i + 1&#10;        needed = sum - k&#10;        if needed in prefix_index:&#10;            max_len = max(max_len, i - prefix_index[needed])&#10;        if sum not in prefix_index:&#10;            prefix_index[sum] = i&#10;    return max_len</code></pre></details></td>
    </tr>
    <tr>
      <td>9</td>
      <td>Hash 09 Two Sum<br><br></b> <a href="https://leetcode.com/problems/two-sum/" target="_blank">LeetCode 1</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: nums = [2,7,11,15], target = 9, Output: [0,1]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Iterate while storing numbers and their indices in a hash map. Check if `target - num` already exists.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def twoSum(nums: list[int], target: int) -&gt; list[int]:&#10;    mpp = {}&#10;    for i, num in enumerate(nums):&#10;        needed = target - num&#10;        if needed in mpp:&#10;            return [mpp[needed], i]&#10;        mpp[num] = i&#10;    return []</code></pre></details></td>
    </tr>
    <tr>
      <td>10</td>
      <td>Hash 10 Group Anagrams<br><br></b> <a href="https://leetcode.com/problems/group-anagrams/" target="_blank">LeetCode 49</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: strs = ["eat","tea","tan","ate","nat","bat"], Output: [["bat"],["nat","tan"],["ate","eat","tea"]]</td>
      <td><b>Time:</b> O(N * K log K)<br><b>Space:</b> O(N * K)</td>
      <td><b>Explanation:</b> Use a hash map where the key is the sorted version of the string, and the value is a list of anagrams.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">from collections import defaultdict&#10;def groupAnagrams(strs: list[str]) -&gt; list[list[str]]:&#10;    mpp = defaultdict(list)&#10;    for s in strs:&#10;        mpp[tuple(sorted(s))].append(s)&#10;    return list(mpp.values())</code></pre></details></td>
    </tr>
    <tr>
      <td>11</td>
      <td>Hash 11 Longest Consecutive Sequence<br><br></b> <a href="https://leetcode.com/problems/longest-consecutive-sequence/" target="_blank">LeetCode 128</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: nums = [100,4,200,1,3,2], Output: 4 (The sequence is [1, 2, 3, 4])</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Insert all elements into a Hash Set. Iterate through elements. If `num - 1` is NOT in the set, it's the start of a sequence. Count forwards.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def longestConsecutive(nums: list[int]) -&gt; int:&#10;    num_set = set(nums)&#10;    max_len = 0&#10;    for num in num_set:&#10;        if num - 1 not in num_set:&#10;            curr_num = num&#10;            curr_len = 1&#10;            while curr_num + 1 in num_set:&#10;                curr_num += 1&#10;                curr_len += 1&#10;            max_len = max(max_len, curr_len)&#10;    return max_len</code></pre></details></td>
    </tr>
    <tr>
      <td>12</td>
      <td>Hash 12 Longest Subarray With 0 Sum<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Hash Map.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Maintain the prefix sum and a hash map storing the first occurrence index of each prefix sum. If sum is 0, length is `i+1`. If sum is in the map, length is `i - map[sum]`. Update max length.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxLen(n, arr):&#10;    m = {}&#10;    maxi, sum_val = 0, 0&#10;    for i in range(n):&#10;        sum_val += arr[i]&#10;        if sum_val == 0: maxi = i + 1&#10;        else:&#10;            if sum_val in m:&#10;                maxi = max(maxi, i - m[sum_val])&#10;            else:&#10;                m[sum_val] = i&#10;    return maxi</code></pre></details></td>
    </tr>
    <tr>
      <td>13</td>
      <td>Hash 13 Sort Characters By Frequency<br><br></b> <a href="https://leetcode.com/problems/sort-characters-by-frequency/" target="_blank">LeetCode 451</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td>**Example 1:** Hash Map + Priority Queue / Sorting.</td>
      <td><b>Time:</b> O(N log K) where K is unique chars<br><b>Space:</b> O(K)</td>
      <td><b>Explanation:</b> Count frequencies using a hash map. Add pairs `(freq, char)` to a max heap or vector and sort. Reconstruct string.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">from collections import Counter&#10;def frequencySort(s):&#10;    counts = Counter(s)&#10;    return &quot;&quot;.join(char * count for char, count in counts.most_common())</code></pre></details></td>
    </tr>
    <tr>
      <td>14</td>
      <td>Hash 14 Count Distinct Elements In Every Window<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/count-distinct-elements-in-every-window/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td>**Example 1:** Sliding Window + Hash Map.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(K)</td>
      <td><b>Explanation:</b> Use a hash map to keep track of element frequencies in the window of size K. The number of distinct elements is the size of the hash map. As window slides, increment frequency of new element, decrement frequency of outgoing element. If frequency becomes 0, remove it from map.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def countDistinct(arr, n, k):&#10;    m = {}&#10;    ans = []&#10;    for i in range(k):&#10;        m[arr[i]] = m.get(arr[i], 0) + 1&#10;    ans.append(len(m))&#10;    for i in range(k, n):&#10;        m[arr[i - k]] -= 1&#10;        if m[arr[i - k]] == 0: del m[arr[i - k]]&#10;        m[arr[i]] = m.get(arr[i], 0) + 1&#10;        ans.append(len(m))&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>15</td>
      <td>Hash 15 Design Hashset<br><br></b> <a href="https://leetcode.com/problems/design-hashset/" target="_blank">LeetCode 705</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td>**Example 1:** Array of Linked Lists (Chaining).</td>
      <td><b>Time:</b> O(1) average, O(N) worst case<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Use a large array (e.g., size 10000) of linked lists or vectors. The hash function maps `key` to `key % 10000`. To add, if not present in the bucket, append it. To remove, find and erase. To contain, iterate through bucket.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class MyHashSet:&#10;    def __init__(self):&#10;        self.size = 10000&#10;        self.buckets = [[] for _ in range(self.size)]&#10;    def add(self, key: int) -&gt; None:&#10;        i = key % self.size&#10;        if key not in self.buckets[i]:&#10;            self.buckets[i].append(key)&#10;    def remove(self, key: int) -&gt; None:&#10;        i = key % self.size&#10;        if key in self.buckets[i]:&#10;            self.buckets[i].remove(key)&#10;    def contains(self, key: int) -&gt; bool:&#10;        return key in self.buckets[key % self.size]</code></pre></details></td>
    </tr>
  </tbody>
</table>
