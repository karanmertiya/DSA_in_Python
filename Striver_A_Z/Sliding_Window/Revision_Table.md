# Sliding Window Revision Table

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
      <td rowspan="1">Sw 01 Max Sum Subarray Size K<br><br></b> <a href='https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1' target='_blank'>GeeksforGeeks</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: arr = [2, 1, 5, 1, 3, 2], K = 3, Output: 9 ([5, 1, 3])<br><br><b>Note (Constraint):</b> Fixed size sliding window.</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td>-</td>
      <td><b>Initial Window:</b> Calculate the first K elements manually before starting the sliding loop.</td>
      <td><b>Explanation:</b> Fixed Sliding Window: Maintain a window of size K. Slide it by adding the next element and subtracting the first element of the previous window.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maximum_sum_subarray(K: int, arr: list[int]) -&gt; int:&#10;    if len(arr) &lt; K: return 0&#10;    current_sum = sum(arr[:K])&#10;    max_sum = current_sum&#10;    for i in range(K, len(arr)):&#10;        current_sum += arr[i] - arr[i-K]&#10;        max_sum = max(max_sum, current_sum)&#10;    return max_sum</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">2</td>
      <td rowspan="2">Sw 02 Longest Substring Without Repeating<br><br></b> <a href='https://leetcode.com/problems/longest-substring-without-repeating-characters/' target='_blank'>LeetCode 3</a></td>
      <td rowspan="2"><b>Example 1:</b> Input: s = "abcabcbb", Output: 3 ("abc")<br><br><b>Note (Constraint):</b> Variable size sliding window.</td>
      <td><b>Time:</b> O(2N) &cong; O(N) (Trade-off)<br><b>Space:</b> O(N) (Trade-off)</td>
      <td><code>std::unordered_set</code></td>
      <td><b>Shrink Loop:</b> `while(set.contains)` ensures all characters up to the duplicate are removed from the left pointer.</td>
      <td><b>Explanation:</b> Use a Hash Set to track characters in the current window. If a duplicate is found, shrink the window from the left.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def length_of_longest_substring_better(s: str) -&gt; int:&#10;    char_set = set()&#10;    left = max_len = 0&#10;    for right in range(len(s)):&#10;        while s[right] in char_set:&#10;            char_set.remove(s[left])&#10;            left += 1&#10;        char_set.add(s[right])&#10;        max_len = max(max_len, right - left + 1)&#10;    return max_len</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td>Fixed Array size 256</td>
      <td><b>Direct Jump:</b> Only jump `left` if the found duplicate index is within the current window (`>= left`).</td>
      <td><b>Explanation:</b> Optimal: Store the latest index of each character in a Hash Map. Jump `left` directly to `map[char] + 1`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def length_of_longest_substring_optimal(s: str) -&gt; int:&#10;    char_index = {}&#10;    left = max_len = 0&#10;    for right, char in enumerate(s):&#10;        if char in char_index:&#10;            left = max(left, char_index[char] + 1)&#10;        char_index[char] = right&#10;        max_len = max(max_len, right - left + 1)&#10;    return max_len</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">3</td>
      <td rowspan="2">Sw 03 Max Consecutive Ones Iii<br><br></b> <a href='https://leetcode.com/problems/max-consecutive-ones-iii/' target='_blank'>LeetCode 1004</a></td>
      <td rowspan="2"><b>Example 1:</b> Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2, Output: 6<br><br><b>Note (Constraint):</b> Sliding window maintaining at most K zeros.</td>
      <td><b>Time:</b> O(2N) (Trade-off)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>While Loop Shrink:</b> Inner loop safely processes `O(N)` times across the entire algorithm lifecycle.</td>
      <td><b>Explanation:</b> Maintain a window counting zeros. If zeros exceed K, shrink from left.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def longest_ones_better(nums: list[int], k: int) -&gt; int:&#10;    left = zeros = max_len = 0&#10;    for right in range(len(nums)):&#10;        if nums[right] == 0: zeros += 1&#10;        while zeros &gt; k:&#10;            if nums[left] == 0: zeros -= 1&#10;            left += 1&#10;        max_len = max(max_len, right - left + 1)&#10;    return max_len</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>Non-shrinking Window:</b> By changing `while` to `if`, the window stops growing but never shrinks, ending perfectly on the max length.</td>
      <td><b>Explanation:</b> Optimal: Never shrink the window, only slide it when invalid. This retains the `max_len` automatically.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def longest_ones_optimal(nums: list[int], k: int) -&gt; int:&#10;    left = zeros = 0&#10;    for right in range(len(nums)):&#10;        if nums[right] == 0: zeros += 1&#10;        if zeros &gt; k:&#10;            if nums[left] == 0: zeros -= 1&#10;            left += 1&#10;    return len(nums) - left</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">4</td>
      <td rowspan="1">Sw 04 Longest Repeating Character Replacement<br><br></b> <a href='https://leetcode.com/problems/longest-repeating-character-replacement/' target='_blank'>LeetCode 424</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: s = "AABABBA", k = 1, Output: 4 ("AABA" -> "AAAA")<br><br><b>Note (Constraint):</b> All Uppercase English letters.</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td>Fixed Array size 26</td>
      <td><b>Max Freq Preservation:</b> Even if the character drops out, keeping the historical `max_freq` prevents the window from shrinking, acting identically to Max Consecutive Ones logic.</td>
      <td><b>Explanation:</b> Sliding window tracking the `max_frequency_count` inside the window. If `window_len - max_freq > k`, slide the window.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def character_replacement(s: str, k: int) -&gt; int:&#10;    count = [0] * 26&#10;    left = max_freq = 0&#10;    for right in range(len(s)):&#10;        count[ord(s[right]) - 65] += 1&#10;        max_freq = max(max_freq, count[ord(s[right]) - 65])&#10;        &#10;        if (right - left + 1) - max_freq &gt; k:&#10;            count[ord(s[left]) - 65] -= 1&#10;            left += 1&#10;    return len(s) - left</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">5</td>
      <td rowspan="1">Sw 05 Minimum Window Substring<br><br></b> <a href='https://leetcode.com/problems/minimum-window-substring/' target='_blank'>LeetCode 76</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: s = "ADOBECODEBANC", t = "ABC", Output: "BANC"<br><br><b>Note (Constraint):</b> Hardest sliding window. Require tracking multiple character requirements.</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1)</td>
      <td>Fixed Array size 256</td>
      <td><b>Negative Counts:</b> When expanding, unneeded characters get negative counts in the map. Shrinking recovers them.</td>
      <td><b>Explanation:</b> Use a map to count required characters of `t`. Expand right pointer until `required == 0`. Then shrink left pointer to find minimum valid window.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def min_window(s: str, t: str) -&gt; str:&#10;    char_map = [0] * 256&#10;    for char in t: char_map[ord(char)] += 1&#10;    &#10;    left = 0; required = len(t)&#10;    min_len = float(&#x27;inf&#x27;); start_idx = -1&#10;    &#10;    for right in range(len(s)):&#10;        if char_map[ord(s[right])] &gt; 0: required -= 1&#10;        char_map[ord(s[right])] -= 1&#10;        &#10;        while required == 0:&#10;            if right - left + 1 &lt; min_len:&#10;                min_len = right - left + 1&#10;                start_idx = left&#10;            char_map[ord(s[left])] += 1&#10;            if char_map[ord(s[left])] &gt; 0: required += 1&#10;            left += 1&#10;            &#10;    return &quot;&quot; if start_idx == -1 else s[start_idx:start_idx+min_len]</code></pre></details></td>
    </tr>
  </tbody>
</table>
