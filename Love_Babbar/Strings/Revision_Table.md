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
      <td rowspan="1">Str 01 Valid Palindrome<br><br></b> <a href='https://leetcode.com/problems/valid-palindrome/' target='_blank'>LeetCode 125</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: s = "A man, a plan, a canal: Panama", Output: true</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><code>std::isalnum</code>, <code>std::tolower</code></td>
      <td><b>All Non-Alphanumeric:</b> Pointers might cross without any comparisons. Loop condition `left < right` safely handles it.</td>
      <td><b>Explanation:</b> Two-pointer approach skipping non-alphanumeric characters. Compare characters from both ends.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isPalindrome(s: str) -&gt; bool:&#10;    left, right = 0, len(s) - 1&#10;    while left &lt; right:&#10;        while left &lt; right and not s[left].isalnum(): left += 1&#10;        while left &lt; right and not s[right].isalnum(): right -= 1&#10;        if s[left].lower() != s[right].lower(): return False&#10;        left += 1; right -= 1&#10;    return True</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">2</td>
      <td rowspan="1">Str 02 Valid Anagram<br><br></b> <a href='https://leetcode.com/problems/valid-anagram/' target='_blank'>LeetCode 242</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: s = "anagram", t = "nagaram", Output: true</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>Length Mismatch:</b> If lengths differ, return false immediately to prevent boundary issues.</td>
      <td><b>Explanation:</b> Use a frequency array of size 26. Increment for `s`, decrement for `t`. Check if all counts are 0.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isAnagram(s: str, t: str) -&gt; bool:&#10;    if len(s) != len(t): return False&#10;    freq = [0] * 26&#10;    for i in range(len(s)):&#10;        freq[ord(s[i]) - ord(&#x27;a&#x27;)] += 1&#10;        freq[ord(t[i]) - ord(&#x27;a&#x27;)] -= 1&#10;    return all(count == 0 for count in freq)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">3</td>
      <td rowspan="1">Str 03 Longest Common Prefix<br><br></b> <a href='https://leetcode.com/problems/longest-common-prefix/' target='_blank'>LeetCode 14</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: strs = ["flower","flow","flight"], Output: "fl"</td>
      <td><b>Time:</b> O(N log N * M) (Constraint)<br><b>Space:</b> O(1) / O(M)</td>
      <td><code>std::sort</code></td>
      <td><b>No Match:</b> If the first character of `first` and `last` string doesn't match, loop breaks immediately, returning "".</td>
      <td><b>Explanation:</b> Sort the array. The common prefix will be constrained by the first and last strings in the sorted array.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def longestCommonPrefix(strs: list[str]) -&gt; str:&#10;    if not strs: return &quot;&quot;&#10;    strs.sort()&#10;    first, last = strs[0], strs[-1]&#10;    i = 0&#10;    while i &lt; len(first) and i &lt; len(last) and first[i] == last[i]:&#10;        i += 1&#10;    return first[:i]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">4</td>
      <td rowspan="1">Str 04 Longest Palindromic Substring<br><br></b> <a href='https://leetcode.com/problems/longest-palindromic-substring/' target='_blank'>LeetCode 5</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: s = "babad", Output: "bab"</td>
      <td><b>Time:</b> O(N<sup>2</sup>) (Constraint)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>Substr Math:</b> `start` is calculated as `i - (len - 1) / 2` to safely encompass both odd and even length centers.</td>
      <td><b>Explanation:</b> Expand Around Center. A palindrome can have an odd (center is 1 char) or even (center is between 2 chars) length. Test both.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def longestPalindrome(s: str) -&gt; str:&#10;    def expand(left, right):&#10;        while left &gt;= 0 and right &lt; len(s) and s[left] == s[right]:&#10;            left -= 1&#10;            right += 1&#10;        return right - left - 1&#10;        &#10;    start, max_len = 0, 0&#10;    for i in range(len(s)):&#10;        len1 = expand(i, i)&#10;        len2 = expand(i, i + 1)&#10;        l = max(len1, len2)&#10;        if l &gt; max_len:&#10;            max_len = l&#10;            start = i - (l - 1) // 2&#10;    return s[start : start + max_len]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">5</td>
      <td rowspan="1">Str 05 Longest Palindromic Substring<br><br></b> <a href='https://leetcode.com/problems/longest-palindromic-substring/' target='_blank'>LeetCode 5</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: s = 'babad', Output: 'bab'</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(1)</td>
      <td><code>#include <string></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Expand Around Center. A palindrome mirrors around its center. There are 2N-1 centers (each letter, and between each pair of letters). Expand outward as long as it remains a palindrome.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def longestPalindrome(s: str) -&gt; str:&#10;    if not s: return &quot;&quot;&#10;    start, end = 0, 0&#10;    def expandAroundCenter(left: int, right: int) -&gt; int:&#10;        while left &gt;= 0 and right &lt; len(s) and s[left] == s[right]:&#10;            left -= 1&#10;            right += 1&#10;        return right - left - 1&#10;    for i in range(len(s)):&#10;        len1 = expandAroundCenter(i, i)&#10;        len2 = expandAroundCenter(i, i + 1)&#10;        length = max(len1, len2)&#10;        if length &gt; end - start:&#10;            start = i - (length - 1) // 2&#10;            end = i + length // 2&#10;    return s[start:end+1]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">6</td>
      <td rowspan="1">Str 06 Longest Common Prefix<br><br></b> <a href='https://leetcode.com/problems/longest-common-prefix/' target='_blank'>LeetCode 14</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: strs = ['flower','flow','flight'], Output: 'fl'</td>
      <td><b>Time:</b> O(N log N * M)<br><b>Space:</b> O(1) auxiliary</td>
      <td><code>#include <algorithm></code></td>
      <td><b>Empty array:</b> Handled with an initial emptiness check.</td>
      <td><b>Explanation:</b> Sort the array of strings. Compare only the first and last strings in the sorted array, as they will have the most differing characters.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def longestCommonPrefix(strs: List[str]) -&gt; str:&#10;    if not strs: return &quot;&quot;&#10;    strs.sort()&#10;    first, last = strs[0], strs[-1]&#10;    i = 0&#10;    while i &lt; len(first) and i &lt; len(last) and first[i] == last[i]:&#10;        i += 1&#10;    return first[:i]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">7</td>
      <td rowspan="1">Str 07 Kmp Algorithm<br><br></b> <a href='https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/' target='_blank'>LeetCode 28</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: haystack = 'sadbutsad', needle = 'sad', Output: 0</td>
      <td><b>Time:</b> O(N + M)<br><b>Space:</b> O(M)</td>
      <td><code>#include <vector></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Compute the LPS (Longest Proper Prefix which is also Suffix) array for the needle. Use the LPS array to skip characters while matching with the haystack, reducing time to O(N+M).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def strStr(haystack: str, needle: str) -&gt; int:&#10;    if not needle: return 0&#10;    m, n = len(needle), len(haystack)&#10;    lps = [0] * m&#10;    length, i = 0, 1&#10;    while i &lt; m:&#10;        if needle[i] == needle[length]:&#10;            length += 1&#10;            lps[i] = length; i += 1&#10;        else:&#10;            if length != 0: length = lps[length - 1]&#10;            else: lps[i] = 0; i += 1&#10;    i = j = 0&#10;    while i &lt; n:&#10;        if needle[j] == haystack[i]: i += 1; j += 1&#10;        if j == m: return i - j&#10;        elif i &lt; n and needle[j] != haystack[i]:&#10;            if j != 0: j = lps[j - 1]&#10;            else: i += 1&#10;    return -1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">8</td>
      <td rowspan="1">Str 08 Rabin Karp<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/31272eef104840f7430ad9fd1d43b434a4cea159/1' target='_blank'>GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Return array of starting indices.</td>
      <td><b>Time:</b> O(N + M)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Compute hash for pattern and first window of text. Slide window: subtract leading char's hash contribution, shift, and add trailing char. If hashes match, explicitly check strings to avoid collisions.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def search(pat: str, txt: str) -&gt; List[int]:&#10;    d, q = 256, 101&#10;    m, n = len(pat), len(txt)&#10;    if m &gt; n: return []&#10;    res, p, t, h = [], 0, 0, 1&#10;    for i in range(m-1): h = (h * d) % q&#10;    for i in range(m):&#10;        p = (d * p + ord(pat[i])) % q&#10;        t = (d * t + ord(txt[i])) % q&#10;    for i in range(n - m + 1):&#10;        if p == t:&#10;            if txt[i:i+m] == pat:&#10;                res.append(i + 1)&#10;        if i &lt; n - m:&#10;            t = (d * (t - ord(txt[i]) * h) + ord(txt[i+m])) % q&#10;            if t &lt; 0: t += q&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">9</td>
      <td rowspan="1">Str 9 Reverse A String<br><br></b> <a href='https://leetcode.com/problems/reverse-string/' target='_blank'>LeetCode 344</a></td>
      <td rowspan="1"><b>Example 1:</b> Two pointers swap.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Use two pointers, `left` at the beginning and `right` at the end of the string. Swap the characters at these pointers and move them towards each other until they meet.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def reverseString(s: List[str]) -&gt; None:&#10;    left, right = 0, len(s) - 1&#10;    while left &lt; right:&#10;        s[left], s[right] = s[right], s[left]&#10;        left += 1&#10;        right -= 1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">10</td>
      <td rowspan="1">Str 10 Palindrome String<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/palindrome-string0817/1' target='_blank'>GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Two pointers.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Use two pointers, `left` at the beginning and `right` at the end of the string. Compare the characters at these pointers. If they are different, return 0. Move pointers towards each other. If all characters match, return 1.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isPalindrome(S: str) -&gt; int:&#10;    left, right = 0, len(S) - 1&#10;    while left &lt; right:&#10;        if S[left] != S[right]:&#10;            return 0&#10;        left += 1&#10;        right -= 1&#10;    return 1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">11</td>
      <td rowspan="1">Str 11 Find Duplicate Characters In A String<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/find-duplicate-characters-in-a-string/1' target='_blank'>GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Frequency array or Hash Map.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><code>#include <unordered_map></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Use a hash map or frequency array to count occurrences of each character. Then, iterate through the map/array and print characters with a count greater than 1.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def printDups(s: str):&#10;    count = collections.Counter(s)&#10;    for k, v in count.items():&#10;        if v &gt; 1:&#10;            print(f&quot;{k}, count = {v}&quot;)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">12</td>
      <td rowspan="1">Str 12 Why Strings Are Immutable In Java<br><br></b> <a href='https://www.geeksforgeeks.org/java-string-is-immutable-what-exactly-is-the-meaning/' target='_blank'>Article</a></td>
      <td rowspan="1"><b>Example 1:</b> String Pool, Security, Thread Safety.</td>
      <td><b>Time:</b> -<br><b>Space:</b> -</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> 1. **String Pool**: Allows caching of string literals, saving memory. 2. **Security**: Strings are used as arguments for network connections, database URLs, etc. Immutability prevents malicious tampering. 3. **Thread Safety**: Immutable objects are inherently thread-safe and can be shared among multiple threads without synchronization. 4. **Caching Hashcode**: Immutability guarantees the hashcode will never change, making it suitable for keys in HashMaps.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python"># Conceptual topic</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">13</td>
      <td rowspan="1">Str 13 A Program To Check If Strings Are Rotations Of Each Other<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/check-if-strings-are-rotations-of-each-other-or-not-1587115620/1' target='_blank'>GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Concatenate and find.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> If the lengths are different, return false. Otherwise, concatenate `s1` with itself (`s1 + s1`). If `s2` is a rotation of `s1`, it must be a substring of the concatenated string.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def areRotations(s1: str, s2: str) -&gt; bool:&#10;    if len(s1) != len(s2): return False&#10;    return s2 in (s1 + s1)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">14</td>
      <td rowspan="1">Str 14 Check If A String Is A Valid Shuffle Of Two Distinct Strings<br><br></b> <a href='https://www.programiz.com/java-programming/examples/check-valid-shuffle-of-strings' target='_blank'>Article</a></td>
      <td rowspan="1"><b>Example 1:</b> Three pointers.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> If lengths don't match, return false. Use three pointers `i`, `j`, `k` for `str1`, `str2`, and `str3`. Traverse `str3`. If `str3[k] == str1[i]`, increment `i` and `k`. Else if `str3[k] == str2[j]`, increment `j` and `k`. Else, it's not a valid shuffle. After the loop, check if both `str1` and `str2` are fully traversed.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def checkShuffle(str1: str, str2: str, str3: str) -&gt; bool:&#10;    if len(str1) + len(str2) != len(str3): return False&#10;    i, j, k = 0, 0, 0&#10;    while k &lt; len(str3):&#10;        if i &lt; len(str1) and str1[i] == str3[k]: i += 1&#10;        elif j &lt; len(str2) and str2[j] == str3[k]: j += 1&#10;        else: return False&#10;        k += 1&#10;    return i == len(str1) and j == len(str2)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">15</td>
      <td rowspan="1">Str 15 Count And Say<br><br></b> <a href='https://leetcode.com/problems/count-and-say/' target='_blank'>LeetCode 38</a></td>
      <td rowspan="1"><b>Example 1:</b> Recursive generation.</td>
      <td><b>Time:</b> O(N * L) where L is max length of string<br><b>Space:</b> O(L)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Start with `res = '1'`. For `n-1` times, iterate through `res` and count consecutive identical characters. Append the count and the character to a new string. Replace `res` with the new string.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def countAndSay(n: int) -&gt; str:&#10;    if n == 1: return &quot;1&quot;&#10;    s = &quot;1&quot;&#10;    for _ in range(2, n + 1):&#10;        temp = &quot;&quot;&#10;        count = 1&#10;        for j in range(1, len(s)):&#10;            if s[j] == s[j - 1]:&#10;                count += 1&#10;            else:&#10;                temp += str(count) + s[j - 1]&#10;                count = 1&#10;        temp += str(count) + s[-1]&#10;        s = temp&#10;    return s</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">16</td>
      <td rowspan="1">Str 16 Longest Palindrome In A String<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/longest-palindrome-in-a-string3411/1' target='_blank'>GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Expand around center.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> For each character, treat it as the center of an odd-length palindrome and expand outwards. Also treat it and the next character as the center of an even-length palindrome and expand outwards. Keep track of the longest palindrome found.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def longestPalindrome(S: str) -&gt; str:&#10;    start = 0; maxLen = 1; n = len(S)&#10;    for i in range(n):&#10;        l = r = i&#10;        while l &gt;= 0 and r &lt; n and S[l] == S[r]:&#10;            if r - l + 1 &gt; maxLen:&#10;                start = l; maxLen = r - l + 1&#10;            l -= 1; r += 1&#10;        l = i; r = i + 1&#10;        while l &gt;= 0 and r &lt; n and S[l] == S[r]:&#10;            if r - l + 1 &gt; maxLen:&#10;                start = l; maxLen = r - l + 1&#10;            l -= 1; r += 1&#10;    return S[start:start+maxLen]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">17</td>
      <td rowspan="1">Str 17 Find Longest Recurring Subsequence In String<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/longest-repeating-subsequence2004/1' target='_blank'>GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Modified LCS.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N^2) or O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> This is a variation of Longest Common Subsequence (LCS). Find LCS of `str` with itself, but with the restriction that when characters match, their indices must not be the same (`i != j`).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def LongestRepeatingSubsequence(str: str) -&gt; int:&#10;    n = len(str)&#10;    dp = [[0] * (n + 1) for _ in range(n + 1)]&#10;    for i in range(1, n + 1):&#10;        for j in range(1, n + 1):&#10;            if str[i-1] == str[j-1] and i != j:&#10;                dp[i][j] = 1 + dp[i-1][j-1]&#10;            else:&#10;                dp[i][j] = max(dp[i][j-1], dp[i-1][j])&#10;    return dp[n][n]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">18</td>
      <td rowspan="1">Str 18 Print All Subsequences Of A String<br><br></b> <a href='https://www.geeksforgeeks.org/print-subsequences-string/' target='_blank'>Article</a></td>
      <td rowspan="1"><b>Example 1:</b> Recursive choice (include/exclude).</td>
      <td><b>Time:</b> O(2^N)<br><b>Space:</b> O(N) recursion stack</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Use recursion. At each character, you have two choices: either include it in the current subsequence or exclude it. When you reach the end of the string, print/store the formed subsequence.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def allSubsequences(s: str) -&gt; List[str]:&#10;    res = []&#10;    def solve(i, curr):&#10;        if i == len(s):&#10;            if curr: res.append(curr)&#10;            return&#10;        solve(i + 1, curr)&#10;        solve(i + 1, curr + s[i])&#10;    solve(0, &quot;&quot;)&#10;    return res</code></pre></details></td>
    </tr>
  </tbody>
</table>
