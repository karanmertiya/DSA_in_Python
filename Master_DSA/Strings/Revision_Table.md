# Strings Revision Table

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
      <td>Str 01 Valid Palindrome<br><br></b> <a href="https://leetcode.com/problems/valid-palindrome/" target="_blank">LeetCode 125</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, SDE Sheet, Striver A Z</details></td>
      <td><b>Example 1:</b> <br><b>Input:</b> s = "A man, a plan, a canal: Panama"<br><b>Output:</b> true</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><b>Explanation:</b> Two-pointer approach skipping non-alphanumeric characters. Compare characters from both ends.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isPalindrome(s: str) -&gt; bool:&#10;    left, right = 0, len(s) - 1&#10;    while left &lt; right:&#10;        while left &lt; right and not s[left].isalnum(): left += 1&#10;        while left &lt; right and not s[right].isalnum(): right -= 1&#10;        if s[left].lower() != s[right].lower(): return False&#10;        left += 1; right -= 1&#10;    return True</code></pre></details></td>
    </tr>
    <tr>
      <td>2</td>
      <td>Str 02 Valid Anagram<br><br></b> <a href="https://leetcode.com/problems/valid-anagram/" target="_blank">LeetCode 242</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, SDE Sheet, Striver A Z</details></td>
      <td><b>Example 1:</b> <br><b>Input:</b> s = "anagram", t = "nagaram"<br><b>Output:</b> true</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Use a frequency array of size 26. Increment for `s`, decrement for `t`. Check if all counts are 0.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isAnagram(s: str, t: str) -&gt; bool:&#10;    if len(s) != len(t): return False&#10;    freq = [0] * 26&#10;    for i in range(len(s)):&#10;        freq[ord(s[i]) - ord(&#x27;a&#x27;)] += 1&#10;        freq[ord(t[i]) - ord(&#x27;a&#x27;)] -= 1&#10;    return all(count == 0 for count in freq)</code></pre></details></td>
    </tr>
    <tr>
      <td>3</td>
      <td>Str 03 Longest Common Prefix<br><br></b> <a href="https://leetcode.com/problems/longest-common-prefix/" target="_blank">LeetCode 14</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, SDE Sheet, Apna College, Striver A Z</details></td>
      <td><b>Example 1:</b> <br><b>Input:</b> strs = ["flower","flow","flight"]<br><b>Output:</b> "fl"</td>
      <td><b>Time:</b> O(N log N * M) (Constraint)<br><b>Space:</b> O(1) / O(M)</td>
      <td><b>Explanation:</b> Sort the array. The common prefix will be constrained by the first and last strings in the sorted array.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def longestCommonPrefix(strs: list[str]) -&gt; str:&#10;    if not strs: return &quot;&quot;&#10;    strs.sort()&#10;    first, last = strs[0], strs[-1]&#10;    i = 0&#10;    while i &lt; len(first) and i &lt; len(last) and first[i] == last[i]:&#10;        i += 1&#10;    return first[:i]</code></pre></details></td>
    </tr>
    <tr>
      <td>4</td>
      <td>Str 04 Longest Palindromic Substring<br><br></b> <a href="https://leetcode.com/problems/longest-palindromic-substring/" target="_blank">LeetCode 5</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, SDE Sheet, Apna College, Striver A Z</details></td>
      <td><b>Example 1:</b> <br><b>Input:</b> s = "babad"<br><b>Output:</b> "bab"</td>
      <td><b>Time:</b> O(N<sup>2</sup>) (Constraint)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Expand Around Center. A palindrome can have an odd (center is 1 char) or even (center is between 2 chars) length. Test both.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def longestPalindrome(s: str) -&gt; str:&#10;    def expand(left, right):&#10;        while left &gt;= 0 and right &lt; len(s) and s[left] == s[right]:&#10;            left -= 1&#10;            right += 1&#10;        return right - left - 1&#10;        &#10;    start, max_len = 0, 0&#10;    for i in range(len(s)):&#10;        len1 = expand(i, i)&#10;        len2 = expand(i, i + 1)&#10;        l = max(len1, len2)&#10;        if l &gt; max_len:&#10;            max_len = l&#10;            start = i - (l - 1) // 2&#10;    return s[start : start + max_len]</code></pre></details></td>
    </tr>
    <tr>
      <td>5</td>
      <td>Str 05 Kmp Algorithm<br><br></b> <a href="https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/" target="_blank">LeetCode 28</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td><b>Example 1:</b> <br><b>Input:</b> haystack = 'sadbutsad', needle = 'sad'<br><b>Output:</b> 0</td>
      <td><b>Time:</b> O(N + M)<br><b>Space:</b> O(M)</td>
      <td><b>Explanation:</b> Compute the LPS (Longest Proper Prefix which is also Suffix) array for the needle. Use the LPS array to skip characters while matching with the haystack, reducing time to O(N+M).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def strStr(haystack: str, needle: str) -&gt; int:&#10;    if not needle: return 0&#10;    m, n = len(needle), len(haystack)&#10;    lps = [0] * m&#10;    length, i = 0, 1&#10;    while i &lt; m:&#10;        if needle[i] == needle[length]:&#10;            length += 1&#10;            lps[i] = length; i += 1&#10;        else:&#10;            if length != 0: length = lps[length - 1]&#10;            else: lps[i] = 0; i += 1&#10;    i = j = 0&#10;    while i &lt; n:&#10;        if needle[j] == haystack[i]: i += 1; j += 1&#10;        if j == m: return i - j&#10;        elif i &lt; n and needle[j] != haystack[i]:&#10;            if j != 0: j = lps[j - 1]&#10;            else: i += 1&#10;    return -1</code></pre></details></td>
    </tr>
    <tr>
      <td>6</td>
      <td>Str 06 Rabin Karp<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/31272eef104840f7430ad9fd1d43b434a4cea159/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td><b>Example 1:</b> Return array of starting indices.</td>
      <td><b>Time:</b> O(N + M)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Compute hash for pattern and first window of text. Slide window: subtract leading char's hash contribution, shift, and add trailing char. If hashes match, explicitly check strings to avoid collisions.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def search(pat: str, txt: str) -&gt; List[int]:&#10;    d, q = 256, 101&#10;    m, n = len(pat), len(txt)&#10;    if m &gt; n: return []&#10;    res, p, t, h = [], 0, 0, 1&#10;    for i in range(m-1): h = (h * d) % q&#10;    for i in range(m):&#10;        p = (d * p + ord(pat[i])) % q&#10;        t = (d * t + ord(txt[i])) % q&#10;    for i in range(n - m + 1):&#10;        if p == t:&#10;            if txt[i:i+m] == pat:&#10;                res.append(i + 1)&#10;        if i &lt; n - m:&#10;            t = (d * (t - ord(txt[i]) * h) + ord(txt[i+m])) % q&#10;            if t &lt; 0: t += q&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td>7</td>
      <td>Str 07 Reverse A String<br><br></b> <a href="https://leetcode.com/problems/reverse-string/" target="_blank">LeetCode 344</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Two pointers swap.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Use two pointers, `left` at the beginning and `right` at the end of the string. Swap the characters at these pointers and move them towards each other until they meet.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def reverseString(s: List[str]) -&gt; None:&#10;    left, right = 0, len(s) - 1&#10;    while left &lt; right:&#10;        s[left], s[right] = s[right], s[left]&#10;        left += 1&#10;        right -= 1</code></pre></details></td>
    </tr>
    <tr>
      <td>8</td>
      <td>Str 08 Palindrome String<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/palindrome-string0817/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td><b>Example 1:</b> Two pointers.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Use two pointers, `left` at the beginning and `right` at the end of the string. Compare the characters at these pointers. If they are different, return 0. Move pointers towards each other. If all characters match, return 1.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isPalindrome(S: str) -&gt; int:&#10;    left, right = 0, len(S) - 1&#10;    while left &lt; right:&#10;        if S[left] != S[right]:&#10;            return 0&#10;        left += 1&#10;        right -= 1&#10;    return 1</code></pre></details></td>
    </tr>
    <tr>
      <td>9</td>
      <td>Str 09 Find Duplicate Characters In A String<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/find-duplicate-characters-in-a-string/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Frequency array or Hash Map.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Use a hash map or frequency array to count occurrences of each character. Then, iterate through the map/array and print characters with a count greater than 1.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def printDups(s: str):&#10;    count = collections.Counter(s)&#10;    for k, v in count.items():&#10;        if v &gt; 1:&#10;            print(f&quot;{k}, count = {v}&quot;)</code></pre></details></td>
    </tr>
    <tr>
      <td>10</td>
      <td>Str 10 A Program To Check If Strings Are Rotations Of Each Other<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/check-if-strings-are-rotations-of-each-other-or-not-1587115620/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Concatenate and find.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> If the lengths are different, return false. Otherwise, concatenate `s1` with itself (`s1 + s1`). If `s2` is a rotation of `s1`, it must be a substring of the concatenated string.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def areRotations(s1: str, s2: str) -&gt; bool:&#10;    if len(s1) != len(s2): return False&#10;    return s2 in (s1 + s1)</code></pre></details></td>
    </tr>
    <tr>
      <td>11</td>
      <td>Str 11 Check If A String Is A Valid Shuffle Of Two Distinct Strings<br><br></b> <a href="https://www.programiz.com/java-programming/examples/check-valid-shuffle-of-strings" target="_blank">Article</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Three pointers.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> If lengths don't match, return false. Use three pointers `i`, `j`, `k` for `str1`, `str2`, and `str3`. Traverse `str3`. If `str3[k] == str1[i]`, increment `i` and `k`. Else if `str3[k] == str2[j]`, increment `j` and `k`. Else, it's not a valid shuffle. After the loop, check if both `str1` and `str2` are fully traversed.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def checkShuffle(str1: str, str2: str, str3: str) -&gt; bool:&#10;    if len(str1) + len(str2) != len(str3): return False&#10;    i, j, k = 0, 0, 0&#10;    while k &lt; len(str3):&#10;        if i &lt; len(str1) and str1[i] == str3[k]: i += 1&#10;        elif j &lt; len(str2) and str2[j] == str3[k]: j += 1&#10;        else: return False&#10;        k += 1&#10;    return i == len(str1) and j == len(str2)</code></pre></details></td>
    </tr>
    <tr>
      <td>12</td>
      <td>Str 12 Count And Say<br><br></b> <a href="https://leetcode.com/problems/count-and-say/" target="_blank">LeetCode 38</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td><b>Example 1:</b> Recursive generation.</td>
      <td><b>Time:</b> O(N * L) where L is max length of string<br><b>Space:</b> O(L)</td>
      <td><b>Explanation:</b> Start with `res = '1'`. For `n-1` times, iterate through `res` and count consecutive identical characters. Append the count and the character to a new string. Replace `res` with the new string.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def countAndSay(n: int) -&gt; str:&#10;    if n == 1: return &quot;1&quot;&#10;    s = &quot;1&quot;&#10;    for _ in range(2, n + 1):&#10;        temp = &quot;&quot;&#10;        count = 1&#10;        for j in range(1, len(s)):&#10;            if s[j] == s[j - 1]:&#10;                count += 1&#10;            else:&#10;                temp += str(count) + s[j - 1]&#10;                count = 1&#10;        temp += str(count) + s[-1]&#10;        s = temp&#10;    return s</code></pre></details></td>
    </tr>
    <tr>
      <td>13</td>
      <td>Str 13 Longest Palindrome In A String<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/longest-palindrome-in-a-string3411/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Expand around center.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> For each character, treat it as the center of an odd-length palindrome and expand outwards. Also treat it and the next character as the center of an even-length palindrome and expand outwards. Keep track of the longest palindrome found.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def longestPalindrome(S: str) -&gt; str:&#10;    start = 0; maxLen = 1; n = len(S)&#10;    for i in range(n):&#10;        l = r = i&#10;        while l &gt;= 0 and r &lt; n and S[l] == S[r]:&#10;            if r - l + 1 &gt; maxLen:&#10;                start = l; maxLen = r - l + 1&#10;            l -= 1; r += 1&#10;        l = i; r = i + 1&#10;        while l &gt;= 0 and r &lt; n and S[l] == S[r]:&#10;            if r - l + 1 &gt; maxLen:&#10;                start = l; maxLen = r - l + 1&#10;            l -= 1; r += 1&#10;    return S[start:start+maxLen]</code></pre></details></td>
    </tr>
    <tr>
      <td>14</td>
      <td>Str 14 Find Longest Recurring Subsequence In String<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/longest-repeating-subsequence2004/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Modified LCS.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N^2) or O(N)</td>
      <td><b>Explanation:</b> This is a variation of Longest Common Subsequence (LCS). Find LCS of `str` with itself, but with the restriction that when characters match, their indices must not be the same (`i != j`).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def LongestRepeatingSubsequence(str: str) -&gt; int:&#10;    n = len(str)&#10;    dp = [[0] * (n + 1) for _ in range(n + 1)]&#10;    for i in range(1, n + 1):&#10;        for j in range(1, n + 1):&#10;            if str[i-1] == str[j-1] and i != j:&#10;                dp[i][j] = 1 + dp[i-1][j-1]&#10;            else:&#10;                dp[i][j] = max(dp[i][j-1], dp[i-1][j])&#10;    return dp[n][n]</code></pre></details></td>
    </tr>
    <tr>
      <td>15</td>
      <td>Str 15 Print All Subsequences Of A String<br><br></b> <a href="https://www.geeksforgeeks.org/print-subsequences-string/" target="_blank">Article</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Recursive choice (include/exclude).</td>
      <td><b>Time:</b> O(2^N)<br><b>Space:</b> O(N) recursion stack</td>
      <td><b>Explanation:</b> Use recursion. At each character, you have two choices: either include it in the current subsequence or exclude it. When you reach the end of the string, print/store the formed subsequence.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def allSubsequences(s: str) -&gt; List[str]:&#10;    res = []&#10;    def solve(i, curr):&#10;        if i == len(s):&#10;            if curr: res.append(curr)&#10;            return&#10;        solve(i + 1, curr)&#10;        solve(i + 1, curr + s[i])&#10;    solve(0, &quot;&quot;)&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td>16</td>
      <td>Str 16 Split The Binary String Into Substrings With Equal Number Of 0S And 1S<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/split-the-binary-string-into-substrings-with-equal-number-of-0s-and-1s/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Counter logic.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Iterate through the string, maintain a count that increments for '0' and decrements for '1' (or vice versa). Whenever the count becomes 0, it means we have found a balanced substring, so increment the answer.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxSubStr(str):&#10;    count0 = 0&#10;    count1 = 0&#10;    ans = 0&#10;    for c in str:&#10;        if c == &#x27;0&#x27;: count0 += 1&#10;        else: count1 += 1&#10;        if count0 == count1:&#10;            ans += 1&#10;    if count0 != count1: return -1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>17</td>
      <td>Str 17 Word Wrap<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/word-wrap1646/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> DP approach.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Use Dynamic Programming. `dp[i]` represents the minimum cost to wrap words from index `i` to the end. Iterate backward and try placing different numbers of words on the current line.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def solveWordWrap(nums, k):&#10;    n = len(nums)&#10;    dp = [0] * n&#10;    dp[n - 1] = 0&#10;    for i in range(n - 2, -1, -1):&#10;        currlen = -1&#10;        dp[i] = float(&#x27;inf&#x27;)&#10;        for j in range(i, n):&#10;            currlen += (nums[j] + 1)&#10;            if currlen &gt; k: break&#10;            if j == n - 1:&#10;                dp[i] = 0&#10;            else:&#10;                cost = (k - currlen) ** 2 + dp[j + 1]&#10;                dp[i] = min(dp[i], cost)&#10;    return dp[0]</code></pre></details></td>
    </tr>
    <tr>
      <td>18</td>
      <td>Str 18 Edit Distance<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/edit-distance3702/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td><b>Example 1:</b> DP Table.</td>
      <td><b>Time:</b> O(N * M)<br><b>Space:</b> O(N * M)</td>
      <td><b>Explanation:</b> Create a 2D DP array. If characters match, `dp[i][j] = dp[i-1][j-1]`. If not, `dp[i][j] = 1 + min(replace, insert, delete)`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def editDistance(s, t):&#10;    n, m = len(s), len(t)&#10;    dp = [[0] * (m + 1) for _ in range(n + 1)]&#10;    for i in range(n + 1): dp[i][0] = i&#10;    for j in range(m + 1): dp[0][j] = j&#10;    for i in range(1, n + 1):&#10;        for j in range(1, m + 1):&#10;            if s[i - 1] == t[j - 1]:&#10;                dp[i][j] = dp[i - 1][j - 1]&#10;            else:&#10;                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])&#10;    return dp[n][m]</code></pre></details></td>
    </tr>
    <tr>
      <td>19</td>
      <td>Str 19 Next Permutation<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/next-permutation5226/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z, SDE Sheet</details></td>
      <td><b>Example 1:</b> Swap and Reverse.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Traverse from right to find the first element smaller than the element to its right. Then, find the smallest element to its right that is greater than it. Swap them, and reverse the subarray after the first element's index.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def nextPermutation(N, arr):&#10;    i = N - 2&#10;    while i &gt;= 0 and arr[i] &gt;= arr[i + 1]:&#10;        i -= 1&#10;    if i &gt;= 0:&#10;        j = N - 1&#10;        while arr[j] &lt;= arr[i]:&#10;            j -= 1&#10;        arr[i], arr[j] = arr[j], arr[i]&#10;    arr[i+1:] = reversed(arr[i+1:])&#10;    return arr</code></pre></details></td>
    </tr>
    <tr>
      <td>20</td>
      <td>Str 20 Parenthesis Checker<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/parenthesis-checker2744/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z, SDE Sheet</details></td>
      <td><b>Example 1:</b> Stack approach.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Use a stack to keep track of opening brackets. If a closing bracket is encountered, check if it matches the top of the stack.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def ispar(x):&#10;    stack = []&#10;    for c in x:&#10;        if c in &#x27;({[&#x27;:&#10;            stack.append(c)&#10;        else:&#10;            if not stack: return False&#10;            if c == &#x27;)&#x27; and stack[-1] != &#x27;(&#x27;: return False&#10;            if c == &#x27;}&#x27; and stack[-1] != &#x27;{&#x27;: return False&#10;            if c == &#x27;]&#x27; and stack[-1] != &#x27;[&#x27;: return False&#10;            stack.pop()&#10;    return len(stack) == 0</code></pre></details></td>
    </tr>
    <tr>
      <td>21</td>
      <td>Str 21 Word Break<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/word-break1352/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, SDE Sheet, Striver A Z</details></td>
      <td><b>Example 1:</b> DP.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Use `dp[i]` to indicate if `A[0..i]` can be segmented. For each `i`, check all prefixes `A[0..j]`. If `dp[j]` is true and `A[j..i]` is in the dictionary, then `dp[i]` is true.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def wordBreak(A, B):&#10;    word_set = set(B)&#10;    n = len(A)&#10;    dp = [False] * (n + 1)&#10;    dp[0] = True&#10;    for i in range(1, n + 1):&#10;        for j in range(i):&#10;            if dp[j] and A[j:i] in word_set:&#10;                dp[i] = True&#10;                break&#10;    return 1 if dp[n] else 0</code></pre></details></td>
    </tr>
    <tr>
      <td>22</td>
      <td>Str 22 Rabin Karp Algorithm<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/31272eef104840f7430ad9fd1d43b434a4b9596b/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z, SDE Sheet</details></td>
      <td><b>Example 1:</b> Rolling Hash.</td>
      <td><b>Time:</b> O(N + M)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Compute the hash for the pattern and for the first window of text. Slide the window by removing the leading character's hash and adding the trailing character's hash. If hashes match, check the characters one by one.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def search(pat, txt):&#10;    d, q = 256, 101&#10;    M, N = len(pat), len(txt)&#10;    p, t, h = 0, 0, 1&#10;    res = []&#10;    for i in range(M - 1): h = (h * d) % q&#10;    for i in range(M):&#10;        p = (d * p + ord(pat[i])) % q&#10;        t = (d * t + ord(txt[i])) % q&#10;    for i in range(N - M + 1):&#10;        if p == t:&#10;            match = True&#10;            for j in range(M):&#10;                if txt[i + j] != pat[j]:&#10;                    match = False&#10;                    break&#10;            if match: res.append(i + 1)&#10;        if i &lt; N - M:&#10;            t = (d * (t - ord(txt[i]) * h) + ord(txt[i + M])) % q&#10;            if t &lt; 0: t = t + q&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td>23</td>
      <td>Str 23 Kmp Algorithm<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/search-pattern0205/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z, SDE Sheet</details></td>
      <td><b>Example 1:</b> LPS Array.</td>
      <td><b>Time:</b> O(N + M)<br><b>Space:</b> O(M)</td>
      <td><b>Explanation:</b> Construct an LPS (Longest Proper Prefix which is also Suffix) array for the pattern. Use it to skip unnecessary comparisons while traversing the text.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def computeLPS(pat, M, lps):&#10;    length = 0&#10;    lps[0] = 0&#10;    i = 1&#10;    while i &lt; M:&#10;        if pat[i] == pat[length]:&#10;            length += 1&#10;            lps[i] = length&#10;            i += 1&#10;        else:&#10;            if length != 0:&#10;                length = lps[length - 1]&#10;            else:&#10;                lps[i] = 0&#10;                i += 1&#10;&#10;def search(pat, txt):&#10;    M, N = len(pat), len(txt)&#10;    lps = [0] * M&#10;    computeLPS(pat, M, lps)&#10;    i, j = 0, 0&#10;    res = []&#10;    while (N - i) &gt;= (M - j):&#10;        if pat[j] == txt[i]:&#10;            j += 1; i += 1&#10;        if j == M:&#10;            res.append(i - j + 1)&#10;            j = lps[j - 1]&#10;        elif i &lt; N and pat[j] != txt[i]:&#10;            if j != 0: j = lps[j - 1]&#10;            else: i += 1&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td>24</td>
      <td>Str 24 Convert A Sentence Into Its Equivalent Mobile Numeric Keypad Sequence<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/convert-a-sentence-into-its-equivalent-mobile-numeric-keypad-sequence0547/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Dictionary Mapping.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Store the sequence for every character in an array from A to Z, and for space. For each character in the input string, append its corresponding sequence to the result.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def printSequence(S):&#10;    str_arr = [&quot;2&quot;, &quot;22&quot;, &quot;222&quot;, &quot;3&quot;, &quot;33&quot;, &quot;333&quot;, &quot;4&quot;, &quot;44&quot;, &quot;444&quot;, &quot;5&quot;, &quot;55&quot;, &quot;555&quot;, &quot;6&quot;, &quot;66&quot;, &quot;666&quot;, &quot;7&quot;, &quot;77&quot;, &quot;777&quot;, &quot;7777&quot;, &quot;8&quot;, &quot;88&quot;, &quot;888&quot;, &quot;9&quot;, &quot;99&quot;, &quot;999&quot;, &quot;9999&quot;]&#10;    output = &quot;&quot;&#10;    for char in S:&#10;        if char == &#x27; &#x27;: output += &quot;0&quot;&#10;        else: output += str_arr[ord(char) - ord(&#x27;A&#x27;)]&#10;    return output</code></pre></details></td>
    </tr>
    <tr>
      <td>25</td>
      <td>Str 25 Count The Reversals<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/count-the-reversals0401/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Stack approach.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Remove all balanced brackets using a stack. The remaining string will be of the form `}}...{{...`. The required reversals will be `ceil(open_count/2) + ceil(close_count/2)`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import math&#10;def countRev(s):&#10;    if len(s) % 2 != 0: return -1&#10;    stack = []&#10;    for c in s:&#10;        if c == &#x27;{&#x27;: stack.append(c)&#10;        else:&#10;            if stack and stack[-1] == &#x27;{&#x27;: stack.pop()&#10;            else: stack.append(c)&#10;    open_count = stack.count(&#x27;{&#x27;)&#10;    close_count = len(stack) - open_count&#10;    return math.ceil(open_count / 2) + math.ceil(close_count / 2)</code></pre></details></td>
    </tr>
    <tr>
      <td>26</td>
      <td>Str 26 Count Palindromic Subsequences<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/count-palindromic-subsequences/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Dynamic Programming.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N^2)</td>
      <td><b>Explanation:</b> Use DP. `dp[i][j]` stores the count of palindromic subsequences in `str[i..j]`. If `str[i] == str[j]`, `dp[i][j] = dp[i+1][j] + dp[i][j-1] + 1`. Else, `dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def countPS(str_val):&#10;    MOD = 10**9 + 7&#10;    n = len(str_val)&#10;    dp = [[0]*n for _ in range(n)]&#10;    for i in range(n): dp[i][i] = 1&#10;    for length in range(2, n + 1):&#10;        for i in range(n - length + 1):&#10;            j = i + length - 1&#10;            if str_val[i] == str_val[j]:&#10;                dp[i][j] = (dp[i+1][j] + dp[i][j-1] + 1) % MOD&#10;            else:&#10;                dp[i][j] = (dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]) % MOD&#10;    return dp[0][n - 1]</code></pre></details></td>
    </tr>
    <tr>
      <td>27</td>
      <td>Str 27 Count Of Number Of Given String In 2D Character Array<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/count-occurences-of-a-given-word-in-a-2-d-array/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> DFS.</td>
      <td><b>Time:</b> O(R * C * 4^L)<br><b>Space:</b> O(L)</td>
      <td><b>Explanation:</b> Use DFS. For each cell, if it matches the first character of the word, start a DFS to look for the rest of the word in all 4 directions. Keep track of visited cells.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findOccurrence(mat, target):&#10;    def dfs(r, c, idx):&#10;        if idx == len(target): return 1&#10;        if r &lt; 0 or r &gt;= len(mat) or c &lt; 0 or c &gt;= len(mat[0]) or mat[r][c] != target[idx]: return 0&#10;        temp = mat[r][c]&#10;        mat[r][c] = &#x27;#&#x27;&#10;        found = (dfs(r + 1, c, idx + 1) +&#10;                 dfs(r - 1, c, idx + 1) +&#10;                 dfs(r, c + 1, idx + 1) +&#10;                 dfs(r, c - 1, idx + 1))&#10;        mat[r][c] = temp&#10;        return found&#10;    count = 0&#10;    for i in range(len(mat)):&#10;        for j in range(len(mat[0])):&#10;            if mat[i][j] == target[0]:&#10;                count += dfs(i, j, 0)&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td>28</td>
      <td>Str 28 Search A Word In A 2D Grid Of Characters<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/find-the-string-in-grid0111/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> 8 Directions Loop.</td>
      <td><b>Time:</b> O(N * M * 8 * L)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Iterate through the grid. For each matching starting character, check all 8 directions to see if the full word exists in a straight line.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def searchWord(grid, word):&#10;    R, C, L = len(grid), len(grid[0]), len(word)&#10;    dr = [-1, -1, -1, 0, 0, 1, 1, 1]&#10;    dc = [-1, 0, 1, -1, 1, -1, 0, 1]&#10;    ans = []&#10;    for r in range(R):&#10;        for c in range(C):&#10;            if grid[r][c] == word[0]:&#10;                for dir in range(8):&#10;                    currR, currC = r + dr[dir], c + dc[dir]&#10;                    k = 1&#10;                    while k &lt; L:&#10;                        if currR &lt; 0 or currR &gt;= R or currC &lt; 0 or currC &gt;= C: break&#10;                        if grid[currR][currC] != word[k]: break&#10;                        currR += dr[dir]&#10;                        currC += dc[dir]&#10;                        k += 1&#10;                    if k == L:&#10;                        ans.append([r, c])&#10;                        break&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>29</td>
      <td>Str 29 Boyer Moore Algorithm For Pattern Searching<br><br></b> <a href="https://www.geeksforgeeks.org/boyer-moore-algorithm-for-pattern-searching/" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Bad Character Heuristic.</td>
      <td><b>Time:</b> O(N * M)<br><b>Space:</b> O(256)</td>
      <td><b>Explanation:</b> Create a Bad Character table for the pattern, which stores the last occurrence of each character. Align pattern with text. Compare from right to left. If mismatch, shift the pattern so that the mismatched character in text aligns with its last occurrence in the pattern. If not present, shift pattern past it.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def search(txt, pat):&#10;    m, n = len(pat), len(txt)&#10;    badChar = [-1] * 256&#10;    for i in range(m): badChar[ord(pat[i])] = i&#10;    s = 0&#10;    while s &lt;= n - m:&#10;        j = m - 1&#10;        while j &gt;= 0 and pat[j] == txt[s + j]: j -= 1&#10;        if j &lt; 0:&#10;            print(f&quot;Pattern occurs at shift = {s}&quot;)&#10;            s += (m - badChar[ord(txt[s + m])] if s + m &lt; n else 1)&#10;        else:&#10;            s += max(1, j - badChar[ord(txt[s + j])])</code></pre></details></td>
    </tr>
    <tr>
      <td>30</td>
      <td>Str 30 Roman Number To Integer<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/roman-number-to-integer3201/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z, SDE Sheet</details></td>
      <td><b>Example 1:</b> Value mapping.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Map each Roman numeral to its integer value. Iterate from right to left. If a character is smaller than its right character, subtract its value, else add it.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def romanToDecimal(S):&#10;    m = {&#x27;I&#x27;: 1, &#x27;V&#x27;: 5, &#x27;X&#x27;: 10, &#x27;L&#x27;: 50, &#x27;C&#x27;: 100, &#x27;D&#x27;: 500, &#x27;M&#x27;: 1000}&#10;    ans = 0&#10;    for i in range(len(S)):&#10;        if i + 1 &lt; len(S) and m[S[i]] &lt; m[S[i+1]]:&#10;            ans -= m[S[i]]&#10;        else:&#10;            ans += m[S[i]]&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>31</td>
      <td>Str 31 Number Of Flips To Make Binary String Alternate<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/min-number-of-flips3210/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Two target strings.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> There are only two possible alternating strings for length N: starting with '0' (`010101...`) and starting with '1' (`101010...`). Count the differences between the given string and both of these. The minimum count is the answer.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minFlips(S):&#10;    count1, count2 = 0, 0&#10;    for i in range(len(S)):&#10;        if i % 2 == 0:&#10;            if S[i] != &#x27;0&#x27;: count1 += 1&#10;            if S[i] != &#x27;1&#x27;: count2 += 1&#10;        else:&#10;            if S[i] != &#x27;1&#x27;: count1 += 1&#10;            if S[i] != &#x27;0&#x27;: count2 += 1&#10;    return min(count1, count2)</code></pre></details></td>
    </tr>
    <tr>
      <td>32</td>
      <td>Str 32 Find The First Repeated Word In String<br><br></b> <a href="https://www.geeksforgeeks.org/find-first-repeated-word-string/" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> HashSet.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Split the string into words. Iterate through the words. If a word is already in the hash set, it is the first repeated word. Return it. Else, add it to the hash set.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def firstRepeatedWord(s):&#10;    import re&#10;    words = re.findall(r&#x27;\w+&#x27;, s)&#10;    st = set()&#10;    for word in words:&#10;        if word in st: return word&#10;        st.add(word)&#10;    return &quot;No Repetition&quot;</code></pre></details></td>
    </tr>
    <tr>
      <td>33</td>
      <td>Str 33 Minimum Swaps For Bracket Balancing<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/minimum-swaps-for-bracket-balancing2704/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Track balance.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Keep track of the number of opening and closing brackets, and an `imbalance` counter. When encountering `[`, decrease imbalance. When encountering `]`, increase imbalance. The number of swaps is updated when an imbalance is found and we find the next `[`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minimumNumberOfSwaps(S):&#10;    open_count = 0&#10;    close_count = 0&#10;    fault = 0&#10;    ans = 0&#10;    for char in S:&#10;        if char == &#x27;]&#x27;:&#10;            close_count += 1&#10;            fault = close_count - open_count&#10;        else:&#10;            open_count += 1&#10;            if fault &gt; 0:&#10;                ans += fault&#10;                fault -= 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>34</td>
      <td>Str 34 Isomorphic Strings<br><br></b> <a href="https://leetcode.com/problems/isomorphic-strings/" target="_blank">LeetCode 205</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td><b>Example 1:</b> Hash Maps.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Use two arrays to map characters from `s` to `t` and `t` to `s`. If `s[i]` is mapped to a character other than `t[i]`, or `t[i]` is mapped to a character other than `s[i]`, return false. Else, create the mappings.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isIsomorphic(s, t):&#10;    m1, m2 = [-1] * 256, [-1] * 256&#10;    for i in range(len(s)):&#10;        if m1[ord(s[i])] != m2[ord(t[i])]: return False&#10;        m1[ord(s[i])] = i&#10;        m2[ord(t[i])] = i&#10;    return True</code></pre></details></td>
    </tr>
    <tr>
      <td>35</td>
      <td>Str 35 Reverse Words In A String<br><br></b> <a href="https://leetcode.com/problems/reverse-words-in-a-string/" target="_blank">LeetCode 151</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z, SDE Sheet</details></td>
      <td><b>Example 1:</b> Two Pointers.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N) for output string</td>
      <td><b>Explanation:</b> Iterate from right to left. Find the end of a word, then the start of a word. Extract the word and append it to the result string along with a space. Finally, remove the trailing space.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def reverseWords(s):&#10;    return &quot; &quot;.join(s.split()[::-1])</code></pre></details></td>
    </tr>
    <tr>
      <td>36</td>
      <td>Str 36 Rotate String<br><br></b> <a href="https://leetcode.com/problems/rotate-string/" target="_blank">LeetCode 796</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td><b>Example 1:</b> String Concatenation.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> If the lengths of `s` and `goal` are not equal, return false. Otherwise, concatenate `s` with itself (`s + s`). If `goal` is a substring of `s + s`, then it's a rotated string.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def rotateString(s, goal):&#10;    if len(s) != len(goal): return False&#10;    return goal in (s + s)</code></pre></details></td>
    </tr>
    <tr>
      <td>37</td>
      <td>Str 37 Largest Odd Number In String<br><br></b> <a href="https://leetcode.com/problems/largest-odd-number-in-string/" target="_blank">LeetCode 1903</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z</details></td>
      <td><b>Example 1:</b> Iterate from right.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1) excluding output</td>
      <td><b>Explanation:</b> Iterate from the end of the string. The first odd digit found marks the end of the largest odd integer (since picking all digits from index 0 to this odd digit yields the largest value). Return the substring `num[0..i]`. If no odd digit is found, return empty string.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def largestOddNumber(num):&#10;    for i in range(len(num) - 1, -1, -1):&#10;        if int(num[i]) % 2 != 0: return num[:i+1]&#10;    return &quot;&quot;</code></pre></details></td>
    </tr>
    <tr>
      <td>38</td>
      <td>Str 38 Maximum Nesting Depth Of The Parentheses<br><br></b> <a href="https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/" target="_blank">LeetCode 1614</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z</details></td>
      <td><b>Example 1:</b> Counter tracking.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Iterate through the string. Maintain a `current_depth` counter. If we see `(`, increment the counter and update `max_depth`. If we see `)`, decrement the counter. Ignore other characters.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxDepth(s):&#10;    max_d = cur_d = 0&#10;    for c in s:&#10;        if c == &#x27;(&#x27;:&#10;            cur_d += 1&#10;            max_d = max(max_d, cur_d)&#10;        elif c == &#x27;)&#x27;:&#10;            cur_d -= 1&#10;    return max_d</code></pre></details></td>
    </tr>
    <tr>
      <td>39</td>
      <td>Str 39 String To Integer Atoi<br><br></b> <a href="https://leetcode.com/problems/string-to-integer-atoi/" target="_blank">LeetCode 8</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z, SDE Sheet</details></td>
      <td><b>Example 1:</b> Step-by-step parsing.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> 1. Ignore leading whitespaces. 2. Check for optional '+' or '-'. 3. Read digits until a non-digit or end of string. 4. Build the integer, checking for 32-bit integer overflow/underflow at each step.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def myAtoi(s):&#10;    s = s.lstrip()&#10;    if not s: return 0&#10;    sign = -1 if s[0] == &#x27;-&#x27; else 1&#10;    if s[0] in [&#x27;-&#x27;, &#x27;+&#x27;]: s = s[1:]&#10;    ans = 0&#10;    for c in s:&#10;        if not c.isdigit(): break&#10;        ans = ans * 10 + int(c)&#10;    ans *= sign&#10;    ans = max(-2**31, min(ans, 2**31 - 1))&#10;    return ans</code></pre></details></td>
    </tr>
  </tbody>
</table>
