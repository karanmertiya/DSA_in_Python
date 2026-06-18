# Strings Revision Table

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
      <td rowspan="1">Str 01 Reverse A String<br><br></b> <a href='https://leetcode.com/problems/reverse-string/' target='_blank'>LeetCode 344</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: s = ["h","e","l","l","o"], Output: ["o","l","l","e","h"]<br><br><b>Note (Constraint):</b> Must be done in O(1) extra memory.</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><code>std::swap</code></td>
      <td><b>Immutability:</b> Python strings are immutable; must convert to list first if strictly following in-place rules, or use slicing `s[::-1]` which uses `O(N)` space.</td>
      <td><b>Explanation:</b> Use two pointers, one at the beginning and one at the end, swapping characters until they meet.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def reverse_string(s: list[str]) -&gt; None:&#10;    left, right = 0, len(s) - 1&#10;    while left &lt; right:&#10;        s[left], s[right] = s[right], s[left]&#10;        left += 1&#10;        right -= 1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">2</td>
      <td rowspan="2">Str 02 Check Palindrome<br><br></b> <a href='https://leetcode.com/problems/valid-palindrome/' target='_blank'>LeetCode 125</a></td>
      <td rowspan="2"><b>Example 1:</b> Input: s = "A man, a plan, a canal: Panama", Output: true<br><br><b>Note (Constraint):</b> 1 &le; N &le; 2 * 10<sup>5</sup></td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(N) (Trade-off)</td>
      <td>Extra String Allocation</td>
      <td>-</td>
      <td><b>Explanation:</b> Clean the string to remove non-alphanumeric characters, convert to lowercase, and check if it equals its reverse.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def is_palindrome_brute(s: str) -&gt; bool:&#10;    clean = &quot;&quot;.join(c.lower() for c in s if c.isalnum())&#10;    return clean == clean[::-1]</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><code>std::isalnum</code> / <code>.isalnum()</code></td>
      <td><b>Pointer Bounds:</b> Must ensure `left < right` inside inner `while` loops to prevent out-of-bounds on entirely non-alphanumeric strings.</td>
      <td><b>Explanation:</b> Two-pointer approach skipping non-alphanumeric characters in a single pass without extra memory.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def is_palindrome_optimal(s: str) -&gt; bool:&#10;    left, right = 0, len(s) - 1&#10;    while left &lt; right:&#10;        while left &lt; right and not s[left].isalnum(): left += 1&#10;        while left &lt; right and not s[right].isalnum(): right -= 1&#10;        if s[left].lower() != s[right].lower(): return False&#10;        left += 1; right -= 1&#10;    return True</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">3</td>
      <td rowspan="1">Str 05 Longest Common Prefix<br><br></b> <a href='https://leetcode.com/problems/longest-common-prefix/' target='_blank'>LeetCode 14</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: strs = ["flower","flow","flight"], Output: "fl"<br><br><b>Note (Constraint):</b> 1 &le; strs.length &le; 200</td>
      <td><b>Time:</b> O(N log N * M) (Trade-off)<br><b>Space:</b> O(1)</td>
      <td><code>std::sort</code></td>
      <td><b>String Sorting Magic:</b> Alphabetical sorting forces the most differing strings to the ends.</td>
      <td><b>Explanation:</b> Sort the array of strings. The longest common prefix of the entire array must be the common prefix of the first and last strings in the sorted array.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def longest_common_prefix(strs: list[str]) -&gt; str:&#10;    if not strs: return &quot;&quot;&#10;    strs.sort()&#10;    first, last = strs[0], strs[-1]&#10;    i = 0&#10;    while i &lt; len(first) and i &lt; len(last) and first[i] == last[i]:&#10;        i += 1&#10;    return first[:i]</code></pre></details></td>
    </tr>
  </tbody>
</table>
