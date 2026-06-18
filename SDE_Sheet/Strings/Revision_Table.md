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
      <td rowspan="2">1</td>
      <td rowspan="2">Str 03 Valid Anagram<br><br></b> <a href='https://leetcode.com/problems/valid-anagram/' target='_blank'>LeetCode 242</a></td>
      <td rowspan="2"><b>Example 1:</b> Input: s = "anagram", t = "nagaram", Output: true<br><br><b>Note (Constraint):</b> Strings consist of lowercase English letters.</td>
      <td><b>Time:</b> O(N log N) (Trade-off)<br><b>Space:</b> O(1) or O(N) (Language dependent)</td>
      <td><code>std::sort</code></td>
      <td><b>Length Check:</b> Immediately return false if lengths differ.</td>
      <td><b>Explanation:</b> Sort both strings and compare if they are identical.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def is_anagram_brute(s: str, t: str) -&gt; bool:&#10;    if len(s) != len(t): return False&#10;    return sorted(s) == sorted(t)</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td>-</td>
      <td><b>ASCII Mapping:</b> `char - 'a'` safely maps lowercase letters to `0-25`.</td>
      <td><b>Explanation:</b> Use a fixed size frequency array (Hash Map) to count character occurrences.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def is_anagram_optimal(s: str, t: str) -&gt; bool:&#10;    if len(s) != len(t): return False&#10;    count = [0] * 26&#10;    for i in range(len(s)):&#10;        count[ord(s[i]) - ord(&#x27;a&#x27;)] += 1&#10;        count[ord(t[i]) - ord(&#x27;a&#x27;)] -= 1&#10;    for c in count:&#10;        if c != 0: return False&#10;    return True</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">2</td>
      <td rowspan="1">Str 05 Longest Common Prefix<br><br></b> <a href='https://leetcode.com/problems/longest-common-prefix/' target='_blank'>LeetCode 14</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: strs = ["flower","flow","flight"], Output: "fl"<br><br><b>Note (Constraint):</b> 1 &le; strs.length &le; 200</td>
      <td><b>Time:</b> O(N log N * M) (Trade-off)<br><b>Space:</b> O(1)</td>
      <td><code>std::sort</code></td>
      <td><b>String Sorting Magic:</b> Alphabetical sorting forces the most differing strings to the ends.</td>
      <td><b>Explanation:</b> Sort the array of strings. The longest common prefix of the entire array must be the common prefix of the first and last strings in the sorted array.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def longest_common_prefix(strs: list[str]) -&gt; str:&#10;    if not strs: return &quot;&quot;&#10;    strs.sort()&#10;    first, last = strs[0], strs[-1]&#10;    i = 0&#10;    while i &lt; len(first) and i &lt; len(last) and first[i] == last[i]:&#10;        i += 1&#10;    return first[:i]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">3</td>
      <td rowspan="1">Str 07 Longest Palindromic Substring<br><br></b> <a href='https://leetcode.com/problems/longest-palindromic-substring/' target='_blank'>LeetCode 5</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: s = "babad", Output: "bab" (or "aba")<br><br><b>Note (Constraint):</b> 1 &le; s.length &le; 1000</td>
      <td><b>Time:</b> O(N<sup>2</sup>) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td>-</td>
      <td><b>Even/Odd Centers:</b> Must check `i, i` (odd) and `i, i+1` (even) to catch all palindrome types.</td>
      <td><b>Explanation:</b> Expand Around Center: For each character, treat it as the center of an odd and even length palindrome and expand outwards.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def longest_palindrome(s: str) -&gt; str:&#10;    if not s: return &quot;&quot;&#10;    start, max_len = 0, 0&#10;    def expand(l, r):&#10;        nonlocal start, max_len&#10;        while l &gt;= 0 and r &lt; len(s) and s[l] == s[r]:&#10;            if r - l + 1 &gt; max_len:&#10;                max_len = r - l + 1&#10;                start = l&#10;            l -= 1; r += 1&#10;            &#10;    for i in range(len(s)):&#10;        expand(i, i)     # Odd length&#10;        expand(i, i + 1) # Even length&#10;    return s[start:start+max_len]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">4</td>
      <td rowspan="1">Str 08 String To Integer Atoi<br><br></b> <a href='https://leetcode.com/problems/string-to-integer-atoi/' target='_blank'>LeetCode 8</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: s = "   -42", Output: -42<br><br><b>Note (Constraint):</b> Prevent overflow using `INT_MAX/10` logic.</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1)</td>
      <td><code>INT_MAX</code> / <code>INT_MIN</code></td>
      <td><b>Math Overflow check:</b> Check `res > INT_MAX / 10` before multiplying, same as Basic Maths chapter.</td>
      <td><b>Explanation:</b> Skip whitespaces, parse sign, and construct integer utilizing math bound checks before applying `x10`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def my_atoi(s: str) -&gt; int:&#10;    s = s.lstrip()&#10;    if not s: return 0&#10;    sign = -1 if s[0] == &#x27;-&#x27; else 1&#10;    if s[0] in [&#x27;-&#x27;, &#x27;+&#x27;]: s = s[1:]&#10;    &#10;    res = 0&#10;    for char in s:&#10;        if not char.isdigit(): break&#10;        res = res * 10 + int(char)&#10;        &#10;    res = sign * res&#10;    INT_MIN, INT_MAX = -2**31, 2**31 - 1&#10;    if res &lt; INT_MIN: return INT_MIN&#10;    if res &gt; INT_MAX: return INT_MAX&#10;    return res</code></pre></details></td>
    </tr>
  </tbody>
</table>
