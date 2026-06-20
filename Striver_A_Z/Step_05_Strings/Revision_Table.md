# Step 05 Strings Revision Table

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
      <td>Str 01 Valid Palindrome<br><br></b> <a href='https://leetcode.com/problems/valid-palindrome/' target='_blank'>LeetCode 125</a></td>
      <td><b>Example 1:</b> Input: s = "A man, a plan, a canal: Panama", Output: true</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><b>Explanation:</b> Two-pointer approach skipping non-alphanumeric characters. Compare characters from both ends.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isPalindrome(s: str) -&gt; bool:&#10;    left, right = 0, len(s) - 1&#10;    while left &lt; right:&#10;        while left &lt; right and not s[left].isalnum(): left += 1&#10;        while left &lt; right and not s[right].isalnum(): right -= 1&#10;        if s[left].lower() != s[right].lower(): return False&#10;        left += 1; right -= 1&#10;    return True</code></pre></details></td>
    </tr>
    <tr>
      <td>2</td>
      <td>Str 02 Valid Anagram<br><br></b> <a href='https://leetcode.com/problems/valid-anagram/' target='_blank'>LeetCode 242</a></td>
      <td><b>Example 1:</b> Input: s = "anagram", t = "nagaram", Output: true</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Use a frequency array of size 26. Increment for `s`, decrement for `t`. Check if all counts are 0.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isAnagram(s: str, t: str) -&gt; bool:&#10;    if len(s) != len(t): return False&#10;    freq = [0] * 26&#10;    for i in range(len(s)):&#10;        freq[ord(s[i]) - ord(&#x27;a&#x27;)] += 1&#10;        freq[ord(t[i]) - ord(&#x27;a&#x27;)] -= 1&#10;    return all(count == 0 for count in freq)</code></pre></details></td>
    </tr>
    <tr>
      <td>3</td>
      <td>Str 03 Longest Common Prefix<br><br></b> <a href='https://leetcode.com/problems/longest-common-prefix/' target='_blank'>LeetCode 14</a></td>
      <td><b>Example 1:</b> Input: strs = ["flower","flow","flight"], Output: "fl"</td>
      <td><b>Time:</b> O(N log N * M) (Constraint)<br><b>Space:</b> O(1) / O(M)</td>
      <td><b>Explanation:</b> Sort the array. The common prefix will be constrained by the first and last strings in the sorted array.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def longestCommonPrefix(strs: list[str]) -&gt; str:&#10;    if not strs: return &quot;&quot;&#10;    strs.sort()&#10;    first, last = strs[0], strs[-1]&#10;    i = 0&#10;    while i &lt; len(first) and i &lt; len(last) and first[i] == last[i]:&#10;        i += 1&#10;    return first[:i]</code></pre></details></td>
    </tr>
    <tr>
      <td>4</td>
      <td>Str 04 Longest Palindromic Substring<br><br></b> <a href='https://leetcode.com/problems/longest-palindromic-substring/' target='_blank'>LeetCode 5</a></td>
      <td><b>Example 1:</b> Input: s = "babad", Output: "bab"</td>
      <td><b>Time:</b> O(N<sup>2</sup>) (Constraint)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Expand Around Center. A palindrome can have an odd (center is 1 char) or even (center is between 2 chars) length. Test both.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def longestPalindrome(s: str) -&gt; str:&#10;    def expand(left, right):&#10;        while left &gt;= 0 and right &lt; len(s) and s[left] == s[right]:&#10;            left -= 1&#10;            right += 1&#10;        return right - left - 1&#10;        &#10;    start, max_len = 0, 0&#10;    for i in range(len(s)):&#10;        len1 = expand(i, i)&#10;        len2 = expand(i, i + 1)&#10;        l = max(len1, len2)&#10;        if l &gt; max_len:&#10;            max_len = l&#10;            start = i - (l - 1) // 2&#10;    return s[start : start + max_len]</code></pre></details></td>
    </tr>
    <tr>
      <td>5</td>
      <td>Str 05 Kmp Algorithm<br><br></b> <a href='https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/' target='_blank'>LeetCode 28</a></td>
      <td><b>Example 1:</b> Input: haystack = 'sadbutsad', needle = 'sad', Output: 0</td>
      <td><b>Time:</b> O(N + M)<br><b>Space:</b> O(M)</td>
      <td><b>Explanation:</b> Compute the LPS (Longest Proper Prefix which is also Suffix) array for the needle. Use the LPS array to skip characters while matching with the haystack, reducing time to O(N+M).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def strStr(haystack: str, needle: str) -&gt; int:&#10;    if not needle: return 0&#10;    m, n = len(needle), len(haystack)&#10;    lps = [0] * m&#10;    length, i = 0, 1&#10;    while i &lt; m:&#10;        if needle[i] == needle[length]:&#10;            length += 1&#10;            lps[i] = length; i += 1&#10;        else:&#10;            if length != 0: length = lps[length - 1]&#10;            else: lps[i] = 0; i += 1&#10;    i = j = 0&#10;    while i &lt; n:&#10;        if needle[j] == haystack[i]: i += 1; j += 1&#10;        if j == m: return i - j&#10;        elif i &lt; n and needle[j] != haystack[i]:&#10;            if j != 0: j = lps[j - 1]&#10;            else: i += 1&#10;    return -1</code></pre></details></td>
    </tr>
    <tr>
      <td>6</td>
      <td>Str 06 Rabin Karp<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/31272eef104840f7430ad9fd1d43b434a4cea159/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Return array of starting indices.</td>
      <td><b>Time:</b> O(N + M)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Compute hash for pattern and first window of text. Slide window: subtract leading char's hash contribution, shift, and add trailing char. If hashes match, explicitly check strings to avoid collisions.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def search(pat: str, txt: str) -&gt; List[int]:&#10;    d, q = 256, 101&#10;    m, n = len(pat), len(txt)&#10;    if m &gt; n: return []&#10;    res, p, t, h = [], 0, 0, 1&#10;    for i in range(m-1): h = (h * d) % q&#10;    for i in range(m):&#10;        p = (d * p + ord(pat[i])) % q&#10;        t = (d * t + ord(txt[i])) % q&#10;    for i in range(n - m + 1):&#10;        if p == t:&#10;            if txt[i:i+m] == pat:&#10;                res.append(i + 1)&#10;        if i &lt; n - m:&#10;            t = (d * (t - ord(txt[i]) * h) + ord(txt[i+m])) % q&#10;            if t &lt; 0: t += q&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td>7</td>
      <td>Str 07 Count And Say<br><br></b> <a href='https://leetcode.com/problems/count-and-say/' target='_blank'>LeetCode 38</a></td>
      <td><b>Example 1:</b> Recursive generation.</td>
      <td><b>Time:</b> O(N * L) where L is max length of string<br><b>Space:</b> O(L)</td>
      <td><b>Explanation:</b> Start with `res = '1'`. For `n-1` times, iterate through `res` and count consecutive identical characters. Append the count and the character to a new string. Replace `res` with the new string.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def countAndSay(n: int) -&gt; str:&#10;    if n == 1: return &quot;1&quot;&#10;    s = &quot;1&quot;&#10;    for _ in range(2, n + 1):&#10;        temp = &quot;&quot;&#10;        count = 1&#10;        for j in range(1, len(s)):&#10;            if s[j] == s[j - 1]:&#10;                count += 1&#10;            else:&#10;                temp += str(count) + s[j - 1]&#10;                count = 1&#10;        temp += str(count) + s[-1]&#10;        s = temp&#10;    return s</code></pre></details></td>
    </tr>
    <tr>
      <td>8</td>
      <td>Str 08 Edit Distance<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/edit-distance3702/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> DP Table.</td>
      <td><b>Time:</b> O(N * M)<br><b>Space:</b> O(N * M)</td>
      <td><b>Explanation:</b> Create a 2D DP array. If characters match, `dp[i][j] = dp[i-1][j-1]`. If not, `dp[i][j] = 1 + min(replace, insert, delete)`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def editDistance(s, t):&#10;    n, m = len(s), len(t)&#10;    dp = [[0] * (m + 1) for _ in range(n + 1)]&#10;    for i in range(n + 1): dp[i][0] = i&#10;    for j in range(m + 1): dp[0][j] = j&#10;    for i in range(1, n + 1):&#10;        for j in range(1, m + 1):&#10;            if s[i - 1] == t[j - 1]:&#10;                dp[i][j] = dp[i - 1][j - 1]&#10;            else:&#10;                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])&#10;    return dp[n][m]</code></pre></details></td>
    </tr>
    <tr>
      <td>9</td>
      <td>Str 09 Next Permutation<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/next-permutation5226/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Swap and Reverse.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Traverse from right to find the first element smaller than the element to its right. Then, find the smallest element to its right that is greater than it. Swap them, and reverse the subarray after the first element's index.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def nextPermutation(N, arr):&#10;    i = N - 2&#10;    while i &gt;= 0 and arr[i] &gt;= arr[i + 1]:&#10;        i -= 1&#10;    if i &gt;= 0:&#10;        j = N - 1&#10;        while arr[j] &lt;= arr[i]:&#10;            j -= 1&#10;        arr[i], arr[j] = arr[j], arr[i]&#10;    arr[i+1:] = reversed(arr[i+1:])&#10;    return arr</code></pre></details></td>
    </tr>
    <tr>
      <td>10</td>
      <td>Str 10 Parenthesis Checker<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/parenthesis-checker2744/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Stack approach.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Use a stack to keep track of opening brackets. If a closing bracket is encountered, check if it matches the top of the stack.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def ispar(x):&#10;    stack = []&#10;    for c in x:&#10;        if c in &#x27;({[&#x27;:&#10;            stack.append(c)&#10;        else:&#10;            if not stack: return False&#10;            if c == &#x27;)&#x27; and stack[-1] != &#x27;(&#x27;: return False&#10;            if c == &#x27;}&#x27; and stack[-1] != &#x27;{&#x27;: return False&#10;            if c == &#x27;]&#x27; and stack[-1] != &#x27;[&#x27;: return False&#10;            stack.pop()&#10;    return len(stack) == 0</code></pre></details></td>
    </tr>
    <tr>
      <td>11</td>
      <td>Str 11 Word Break<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/word-break1352/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> DP.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Use `dp[i]` to indicate if `A[0..i]` can be segmented. For each `i`, check all prefixes `A[0..j]`. If `dp[j]` is true and `A[j..i]` is in the dictionary, then `dp[i]` is true.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def wordBreak(A, B):&#10;    word_set = set(B)&#10;    n = len(A)&#10;    dp = [False] * (n + 1)&#10;    dp[0] = True&#10;    for i in range(1, n + 1):&#10;        for j in range(i):&#10;            if dp[j] and A[j:i] in word_set:&#10;                dp[i] = True&#10;                break&#10;    return 1 if dp[n] else 0</code></pre></details></td>
    </tr>
    <tr>
      <td>12</td>
      <td>Str 12 Rabin Karp Algorithm<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/31272eef104840f7430ad9fd1d43b434a4b9596b/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Rolling Hash.</td>
      <td><b>Time:</b> O(N + M)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Compute the hash for the pattern and for the first window of text. Slide the window by removing the leading character's hash and adding the trailing character's hash. If hashes match, check the characters one by one.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def search(pat, txt):&#10;    d, q = 256, 101&#10;    M, N = len(pat), len(txt)&#10;    p, t, h = 0, 0, 1&#10;    res = []&#10;    for i in range(M - 1): h = (h * d) % q&#10;    for i in range(M):&#10;        p = (d * p + ord(pat[i])) % q&#10;        t = (d * t + ord(txt[i])) % q&#10;    for i in range(N - M + 1):&#10;        if p == t:&#10;            match = True&#10;            for j in range(M):&#10;                if txt[i + j] != pat[j]:&#10;                    match = False&#10;                    break&#10;            if match: res.append(i + 1)&#10;        if i &lt; N - M:&#10;            t = (d * (t - ord(txt[i]) * h) + ord(txt[i + M])) % q&#10;            if t &lt; 0: t = t + q&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td>13</td>
      <td>Str 13 Kmp Algorithm<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/search-pattern0205/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> LPS Array.</td>
      <td><b>Time:</b> O(N + M)<br><b>Space:</b> O(M)</td>
      <td><b>Explanation:</b> Construct an LPS (Longest Proper Prefix which is also Suffix) array for the pattern. Use it to skip unnecessary comparisons while traversing the text.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def computeLPS(pat, M, lps):&#10;    length = 0&#10;    lps[0] = 0&#10;    i = 1&#10;    while i &lt; M:&#10;        if pat[i] == pat[length]:&#10;            length += 1&#10;            lps[i] = length&#10;            i += 1&#10;        else:&#10;            if length != 0:&#10;                length = lps[length - 1]&#10;            else:&#10;                lps[i] = 0&#10;                i += 1&#10;&#10;def search(pat, txt):&#10;    M, N = len(pat), len(txt)&#10;    lps = [0] * M&#10;    computeLPS(pat, M, lps)&#10;    i, j = 0, 0&#10;    res = []&#10;    while (N - i) &gt;= (M - j):&#10;        if pat[j] == txt[i]:&#10;            j += 1; i += 1&#10;        if j == M:&#10;            res.append(i - j + 1)&#10;            j = lps[j - 1]&#10;        elif i &lt; N and pat[j] != txt[i]:&#10;            if j != 0: j = lps[j - 1]&#10;            else: i += 1&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td>14</td>
      <td>Str 14 Roman Number To Integer<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/roman-number-to-integer3201/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Value mapping.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Map each Roman numeral to its integer value. Iterate from right to left. If a character is smaller than its right character, subtract its value, else add it.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def romanToDecimal(S):&#10;    m = {&#x27;I&#x27;: 1, &#x27;V&#x27;: 5, &#x27;X&#x27;: 10, &#x27;L&#x27;: 50, &#x27;C&#x27;: 100, &#x27;D&#x27;: 500, &#x27;M&#x27;: 1000}&#10;    ans = 0&#10;    for i in range(len(S)):&#10;        if i + 1 &lt; len(S) and m[S[i]] &lt; m[S[i+1]]:&#10;            ans -= m[S[i]]&#10;        else:&#10;            ans += m[S[i]]&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>15</td>
      <td>Str 15 Isomorphic Strings<br><br></b> <a href='https://leetcode.com/problems/isomorphic-strings/' target='_blank'>LeetCode 205</a></td>
      <td><b>Example 1:</b> Hash Maps.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Use two arrays to map characters from `s` to `t` and `t` to `s`. If `s[i]` is mapped to a character other than `t[i]`, or `t[i]` is mapped to a character other than `s[i]`, return false. Else, create the mappings.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isIsomorphic(s, t):&#10;    m1, m2 = [-1] * 256, [-1] * 256&#10;    for i in range(len(s)):&#10;        if m1[ord(s[i])] != m2[ord(t[i])]: return False&#10;        m1[ord(s[i])] = i&#10;        m2[ord(t[i])] = i&#10;    return True</code></pre></details></td>
    </tr>
    <tr>
      <td>16</td>
      <td>Str 16 Reverse Words In A String<br><br></b> <a href='https://leetcode.com/problems/reverse-words-in-a-string/' target='_blank'>LeetCode 151</a></td>
      <td><b>Example 1:</b> Two Pointers.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N) for output string</td>
      <td><b>Explanation:</b> Iterate from right to left. Find the end of a word, then the start of a word. Extract the word and append it to the result string along with a space. Finally, remove the trailing space.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def reverseWords(s):&#10;    return &quot; &quot;.join(s.split()[::-1])</code></pre></details></td>
    </tr>
    <tr>
      <td>17</td>
      <td>Str 17 Rotate String<br><br></b> <a href='https://leetcode.com/problems/rotate-string/' target='_blank'>LeetCode 796</a></td>
      <td><b>Example 1:</b> String Concatenation.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> If the lengths of `s` and `goal` are not equal, return false. Otherwise, concatenate `s` with itself (`s + s`). If `goal` is a substring of `s + s`, then it's a rotated string.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def rotateString(s, goal):&#10;    if len(s) != len(goal): return False&#10;    return goal in (s + s)</code></pre></details></td>
    </tr>
    <tr>
      <td>18</td>
      <td>Str 18 Largest Odd Number In String<br><br></b> <a href='https://leetcode.com/problems/largest-odd-number-in-string/' target='_blank'>LeetCode 1903</a></td>
      <td><b>Example 1:</b> Iterate from right.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1) excluding output</td>
      <td><b>Explanation:</b> Iterate from the end of the string. The first odd digit found marks the end of the largest odd integer (since picking all digits from index 0 to this odd digit yields the largest value). Return the substring `num[0..i]`. If no odd digit is found, return empty string.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def largestOddNumber(num):&#10;    for i in range(len(num) - 1, -1, -1):&#10;        if int(num[i]) % 2 != 0: return num[:i+1]&#10;    return &quot;&quot;</code></pre></details></td>
    </tr>
    <tr>
      <td>19</td>
      <td>Str 19 Maximum Nesting Depth Of The Parentheses<br><br></b> <a href='https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/' target='_blank'>LeetCode 1614</a></td>
      <td><b>Example 1:</b> Counter tracking.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Iterate through the string. Maintain a `current_depth` counter. If we see `(`, increment the counter and update `max_depth`. If we see `)`, decrement the counter. Ignore other characters.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxDepth(s):&#10;    max_d = cur_d = 0&#10;    for c in s:&#10;        if c == &#x27;(&#x27;:&#10;            cur_d += 1&#10;            max_d = max(max_d, cur_d)&#10;        elif c == &#x27;)&#x27;:&#10;            cur_d -= 1&#10;    return max_d</code></pre></details></td>
    </tr>
    <tr>
      <td>20</td>
      <td>Str 20 String To Integer Atoi<br><br></b> <a href='https://leetcode.com/problems/string-to-integer-atoi/' target='_blank'>LeetCode 8</a></td>
      <td><b>Example 1:</b> Step-by-step parsing.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> 1. Ignore leading whitespaces. 2. Check for optional '+' or '-'. 3. Read digits until a non-digit or end of string. 4. Build the integer, checking for 32-bit integer overflow/underflow at each step.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def myAtoi(s):&#10;    s = s.lstrip()&#10;    if not s: return 0&#10;    sign = -1 if s[0] == &#x27;-&#x27; else 1&#10;    if s[0] in [&#x27;-&#x27;, &#x27;+&#x27;]: s = s[1:]&#10;    ans = 0&#10;    for c in s:&#10;        if not c.isdigit(): break&#10;        ans = ans * 10 + int(c)&#10;    ans *= sign&#10;    ans = max(-2**31, min(ans, 2**31 - 1))&#10;    return ans</code></pre></details></td>
    </tr>
  </tbody>
</table>
