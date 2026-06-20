# Step 10 Sliding Window Revision Table

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
      <td>Sw 01 Longest Substring Without Repeating Characters<br><br></b> <a href="https://leetcode.com/problems/longest-substring-without-repeating-characters/" target="_blank">LeetCode 3</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, SDE Sheet, Love Babbar</details><br><br><details><summary>🧠 Context & Variants</summary><i>(Variants and similar questions to be added later)</i></details></td>
      <td>**Example 1:** Input: s = "abcabcbb", Output: 3 ("abc")</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(min(N, M))</td>
      <td><b>Explanation:</b> Sliding window with a Hash Map storing the latest index of each character. Move `left` pointer to `max(left, map[char] + 1)`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def lengthOfLongestSubstring(s: str) -&gt; int:&#10;    mpp = {}&#10;    left = max_len = 0&#10;    for right, char in enumerate(s):&#10;        if char in mpp:&#10;            left = max(left, mpp[char] + 1)&#10;        mpp[char] = right&#10;        max_len = max(max_len, right - left + 1)&#10;    return max_len</code></pre></details></td>
    </tr>
    <tr>
      <td>2</td>
      <td>Sw 02 Trapping Rain Water<br><br></b> <a href="https://leetcode.com/problems/trapping-rain-water/" target="_blank">LeetCode 42</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details><br><br><details><summary>🧠 Context & Variants</summary><i>(Variants and similar questions to be added later)</i></details></td>
      <td>**Example 1:** Input: height = [0,1,0,2,1,0,1,3,2,1,2,1], Output: 6</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Two pointers `left` and `right`. Maintain `left_max` and `right_max`. Move the pointer pointing to the smaller max, adding trapped water.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def trap(height: list[int]) -&gt; int:&#10;    left, right = 0, len(height) - 1&#10;    res, maxLeft, maxRight = 0, 0, 0&#10;    while left &lt;= right:&#10;        if height[left] &lt;= height[right]:&#10;            if height[left] &gt;= maxLeft: maxLeft = height[left]&#10;            else: res += maxLeft - height[left]&#10;            left += 1&#10;        else:&#10;            if height[right] &gt;= maxRight: maxRight = height[right]&#10;            else: res += maxRight - height[right]&#10;            right -= 1&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td>3</td>
      <td>Sw 03 Container With Most Water<br><br></b> <a href="https://leetcode.com/problems/container-with-most-water/" target="_blank">LeetCode 11</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, SDE Sheet</details><br><br><details><summary>🧠 Context & Variants</summary><i>(Variants and similar questions to be added later)</i></details></td>
      <td>**Example 1:** Input: height = [1,8,6,2,5,4,8,3,7], Output: 49</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Two Pointers from ends. Area is `min(h[left], h[right]) * width`. Move the pointer with the smaller height to seek a potentially taller line.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxArea(height: list[int]) -&gt; int:&#10;    left, right = 0, len(height) - 1&#10;    max_area = 0&#10;    while left &lt; right:&#10;        area = min(height[left], height[right]) * (right - left)&#10;        max_area = max(max_area, area)&#10;        if height[left] &lt; height[right]:&#10;            left += 1&#10;        else:&#10;            right -= 1&#10;    return max_area</code></pre></details></td>
    </tr>
    <tr>
      <td>4</td>
      <td>Sw 04 Minimum Window Substring<br><br></b> <a href="https://leetcode.com/problems/minimum-window-substring/" target="_blank">LeetCode 76</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details><br><br><details><summary>🧠 Context & Variants</summary><i>(Variants and similar questions to be added later)</i></details></td>
      <td>**Example 1:** Variable sliding window.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Maintain a frequency map of `t`. Expand the window by moving `right`. When the window contains all characters of `t`, try to shrink it by moving `left` to find the minimum window. Keep track of the minimum window length and its starting index.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def minWindow(s: str, t: str) -&gt; str:&#10;    if len(s) &lt; len(t): return &quot;&quot;&#10;    count = collections.Counter(t)&#10;    required = len(t)&#10;    l = r = 0&#10;    minLen = float(&#x27;inf&#x27;)&#10;    minStart = 0&#10;    while r &lt; len(s):&#10;        if count[s[r]] &gt; 0:&#10;            required -= 1&#10;        count[s[r]] -= 1&#10;        r += 1&#10;        while required == 0:&#10;            if r - l &lt; minLen:&#10;                minLen = r - l&#10;                minStart = l&#10;            count[s[l]] += 1&#10;            if count[s[l]] &gt; 0:&#10;                required += 1&#10;            l += 1&#10;    return &quot;&quot; if minLen == float(&#x27;inf&#x27;) else s[minStart:minStart+minLen]</code></pre></details></td>
    </tr>
    <tr>
      <td>5</td>
      <td>Sw 05 Sliding Window Maximum<br><br></b> <a href="https://leetcode.com/problems/sliding-window-maximum/" target="_blank">LeetCode 239</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet, Apna College</details><br><br><details><summary>🧠 Context & Variants</summary><i>(Variants and similar questions to be added later)</i></details></td>
      <td>**Example 1:** Deque.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(K)</td>
      <td><b>Explanation:</b> Use a deque to store indices. The deque maintains elements in decreasing order. Remove elements from the back if they are smaller than the current element. Remove elements from the front if they are out of the window. The front element is the maximum of the current window.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def maxSlidingWindow(nums: List[int], k: int) -&gt; List[int]:&#10;    res = []&#10;    dq = collections.deque()&#10;    for i in range(len(nums)):&#10;        if dq and dq[0] == i - k:&#10;            dq.popleft()&#10;        while dq and nums[dq[-1]] &lt;= nums[i]:&#10;            dq.pop()&#10;        dq.append(i)&#10;        if i &gt;= k - 1:&#10;            res.append(nums[dq[0]])&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td>6</td>
      <td>Sw 06 Longest K Unique Characters Substring<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details><br><br><details><summary>🧠 Context & Variants</summary><i>(Variants and similar questions to be added later)</i></details></td>
      <td>**Example 1:** Variable window and hash map.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(K)</td>
      <td><b>Explanation:</b> Maintain a hash map of character frequencies. Expand the window by moving `j`. If the number of unique characters exceeds `k`, shrink the window from the left (`i`) until the number of unique characters is `k`. Update the maximum length when exactly `k` unique characters are present.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def longestKSubstr(s: str, k: int) -&gt; int:&#10;    count = collections.defaultdict(int)&#10;    i = j = 0&#10;    maxLen = -1&#10;    while j &lt; len(s):&#10;        count[s[j]] += 1&#10;        if len(count) == k:&#10;            maxLen = max(maxLen, j - i + 1)&#10;        elif len(count) &gt; k:&#10;            while len(count) &gt; k:&#10;                count[s[i]] -= 1&#10;                if count[s[i]] == 0:&#10;                    del count[s[i]]&#10;                i += 1&#10;        j += 1&#10;    return maxLen</code></pre></details></td>
    </tr>
    <tr>
      <td>7</td>
      <td>Sw 07 Subarrays With K Different Integers<br><br></b> <a href="https://leetcode.com/problems/subarrays-with-k-different-integers/" target="_blank">LeetCode 992</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details><br><br><details><summary>🧠 Context & Variants</summary><i>(Variants and similar questions to be added later)</i></details></td>
      <td>**Example 1:** Exact K = atMost(K) - atMost(K-1).</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Finding exact `k` distinct is hard directly. Instead, find subarrays with at most `k` distinct integers. The number of exact `k` is `atMost(k) - atMost(k - 1)`. The `atMost` function uses a sliding window.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def subarraysWithKDistinct(nums: List[int], k: int) -&gt; int:&#10;    def atMost(k):&#10;        count = collections.defaultdict(int)&#10;        res = i = 0&#10;        for j in range(len(nums)):&#10;            if count[nums[j]] == 0: k -= 1&#10;            count[nums[j]] += 1&#10;            while k &lt; 0:&#10;                count[nums[i]] -= 1&#10;                if count[nums[i]] == 0: k += 1&#10;                i += 1&#10;            res += j - i + 1&#10;        return res&#10;    return atMost(k) - atMost(k - 1)</code></pre></details></td>
    </tr>
    <tr>
      <td>8</td>
      <td>Sw 08 Fruits Into Baskets<br><br></b> <a href="https://leetcode.com/problems/fruit-into-baskets/" target="_blank">LeetCode 904</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details><br><br><details><summary>🧠 Context & Variants</summary><i>(Variants and similar questions to be added later)</i></details></td>
      <td>**Example 1:** Longest subarray with at most 2 distinct elements.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1) (at most 3 elements in map)</td>
      <td><b>Explanation:</b> This translates to finding the longest subarray with at most 2 distinct elements. Maintain a frequency map and use a sliding window. If distinct elements > 2, shrink the window until distinct elements <= 2.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def totalFruit(fruits: List[int]) -&gt; int:&#10;    count = collections.defaultdict(int)&#10;    l = maxFruits = 0&#10;    for r in range(len(fruits)):&#10;        count[fruits[r]] += 1&#10;        while len(count) &gt; 2:&#10;            count[fruits[l]] -= 1&#10;            if count[fruits[l]] == 0:&#10;                del count[fruits[l]]&#10;            l += 1&#10;        maxFruits = max(maxFruits, r - l + 1)&#10;    return maxFruits</code></pre></details></td>
    </tr>
    <tr>
      <td>9</td>
      <td>Sw 09 Max Consecutive Ones Iii<br><br></b> <a href="https://leetcode.com/problems/max-consecutive-ones-iii/" target="_blank">LeetCode 1004</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details><br><br><details><summary>🧠 Context & Variants</summary><i>(Variants and similar questions to be added later)</i></details></td>
      <td>**Example 1:** Sliding Window.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Use a sliding window. Expand the right pointer. If the element is 0, increment a zero counter. While the zero counter > k, shrink the window from the left by moving the left pointer and decrementing the zero counter if left element is 0. The max window size is the answer.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def longestOnes(nums, k):&#10;    left = 0&#10;    zeroes = 0&#10;    max_len = 0&#10;    for right in range(len(nums)):&#10;        if nums[right] == 0: zeroes += 1&#10;        while zeroes &gt; k:&#10;            if nums[left] == 0: zeroes -= 1&#10;            left += 1&#10;        max_len = max(max_len, right - left + 1)&#10;    return max_len</code></pre></details></td>
    </tr>
    <tr>
      <td>10</td>
      <td>Sw 10 Longest Repeating Character Replacement<br><br></b> <a href="https://leetcode.com/problems/longest-repeating-character-replacement/" target="_blank">LeetCode 424</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details><br><br><details><summary>🧠 Context & Variants</summary><i>(Variants and similar questions to be added later)</i></details></td>
      <td>**Example 1:** Sliding Window + Max Freq.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Use a sliding window. Maintain the character frequencies and the `max_freq` in the window. The number of replacements needed is `window_size - max_freq`. If this is > k, shrink the window from left and decrement the corresponding frequency.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def characterReplacement(s, k):&#10;    count = [0] * 26&#10;    left = 0&#10;    max_freq = 0&#10;    max_len = 0&#10;    for right in range(len(s)):&#10;        count[ord(s[right]) - ord(&#x27;A&#x27;)] += 1&#10;        max_freq = max(max_freq, count[ord(s[right]) - ord(&#x27;A&#x27;)])&#10;        if (right - left + 1) - max_freq &gt; k:&#10;            count[ord(s[left]) - ord(&#x27;A&#x27;)] -= 1&#10;            left += 1&#10;        max_len = max(max_len, right - left + 1)&#10;    return max_len</code></pre></details></td>
    </tr>
    <tr>
      <td>11</td>
      <td>Sw 11 Binary Subarrays With Sum<br><br></b> <a href="https://leetcode.com/problems/binary-subarrays-with-sum/" target="_blank">LeetCode 930</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details><br><br><details><summary>🧠 Context & Variants</summary><i>(Variants and similar questions to be added later)</i></details></td>
      <td>**Example 1:** atMost(goal) - atMost(goal - 1).</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Use the helper function `atMost(goal)` which finds the number of subarrays with sum <= goal. The answer is `atMost(goal) - atMost(goal - 1)`. In `atMost`, use a sliding window to maintain the sum.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def numSubarraysWithSum(nums, goal):&#10;    def atMost(k):&#10;        if k &lt; 0: return 0&#10;        left, sum_val, count = 0, 0, 0&#10;        for right in range(len(nums)):&#10;            sum_val += nums[right]&#10;            while sum_val &gt; k:&#10;                sum_val -= nums[left]&#10;                left += 1&#10;            count += (right - left + 1)&#10;        return count&#10;    return atMost(goal) - atMost(goal - 1)</code></pre></details></td>
    </tr>
    <tr>
      <td>12</td>
      <td>Sw 12 Count Number Of Nice Subarrays<br><br></b> <a href="https://leetcode.com/problems/count-number-of-nice-subarrays/" target="_blank">LeetCode 1248</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details><br><br><details><summary>🧠 Context & Variants</summary><i>(Variants and similar questions to be added later)</i></details></td>
      <td>**Example 1:** atMost(k) - atMost(k - 1).</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Replace all odd numbers with 1 and even numbers with 0. The problem then reduces to finding the number of subarrays with a sum equal to k. Use the `atMost(k) - atMost(k - 1)` sliding window approach.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def numberOfSubarrays(nums, k):&#10;    def atMost(limit):&#10;        if limit &lt; 0: return 0&#10;        left, count, res = 0, 0, 0&#10;        for right in range(len(nums)):&#10;            if nums[right] % 2 != 0: count += 1&#10;            while count &gt; limit:&#10;                if nums[left] % 2 != 0: count -= 1&#10;                left += 1&#10;            res += (right - left + 1)&#10;        return res&#10;    return atMost(k) - atMost(k - 1)</code></pre></details></td>
    </tr>
    <tr>
      <td>13</td>
      <td>Sw 13 Number Of Substrings Containing All Three Characters<br><br></b> <a href="https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/" target="_blank">LeetCode 1358</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details><br><br><details><summary>🧠 Context & Variants</summary><i>(Variants and similar questions to be added later)</i></details></td>
      <td>**Example 1:** Store last seen indices.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Iterate through the string. Track the last seen indices of 'a', 'b', and 'c'. If all three have been seen, the number of valid substrings ending at the current index `i` is `1 + min(last_a, last_b, last_c)`. Add this to the total count.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def numberOfSubstrings(s):&#10;    last = [-1, -1, -1]&#10;    count = 0&#10;    for i in range(len(s)):&#10;        last[ord(s[i]) - ord(&#x27;a&#x27;)] = i&#10;        if last[0] != -1 and last[1] != -1 and last[2] != -1:&#10;            count += 1 + min(last)&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td>14</td>
      <td>Sw 14 Maximum Points You Can Obtain From Cards<br><br></b> <a href="https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/" target="_blank">LeetCode 1423</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details><br><br><details><summary>🧠 Context & Variants</summary><i>(Variants and similar questions to be added later)</i></details></td>
      <td>**Example 1:** Sliding Window on remaining cards.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Instead of picking cards from the ends, find the subarray of length `N - K` that has the minimum sum. Subtract this minimum sum from the total sum of the array. That gives the maximum score.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxScore(cardPoints, k):&#10;    n = len(cardPoints)&#10;    total_sum = sum(cardPoints)&#10;    window_size = n - k&#10;    window_sum = sum(cardPoints[:window_size])&#10;    min_window_sum = window_sum&#10;    for i in range(window_size, n):&#10;        window_sum += cardPoints[i] - cardPoints[i - window_size]&#10;        min_window_sum = min(min_window_sum, window_sum)&#10;    return total_sum - min_window_sum</code></pre></details></td>
    </tr>
    <tr>
      <td>15</td>
      <td>Sw 15 Find All Anagrams In A String<br><br></b> <a href="https://leetcode.com/problems/find-all-anagrams-in-a-string/" target="_blank">LeetCode 438</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details><br><br><details><summary>🧠 Context & Variants</summary><i>(Variants and similar questions to be added later)</i></details></td>
      <td>**Example 1:** Fixed Window + Hash Map.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Create frequency arrays for `p` and a window of size `p.length()` in `s`. Slide the window across `s`, updating the window frequencies. If the arrays match, add the window's start index to the result.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findAnagrams(s, p):&#10;    ans = []&#10;    if len(p) &gt; len(s): return ans&#10;    countP, countS = [0]*26, [0]*26&#10;    for i in range(len(p)):&#10;        countP[ord(p[i]) - ord(&#x27;a&#x27;)] += 1&#10;        countS[ord(s[i]) - ord(&#x27;a&#x27;)] += 1&#10;    if countP == countS: ans.append(0)&#10;    for i in range(len(p), len(s)):&#10;        countS[ord(s[i]) - ord(&#x27;a&#x27;)] += 1&#10;        countS[ord(s[i - len(p)]) - ord(&#x27;a&#x27;)] -= 1&#10;        if countP == countS: ans.append(i - len(p) + 1)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>16</td>
      <td>Sw 16 Longest Substring With At Most K Distinct Characters<br><br></b> <a href="https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/" target="_blank">LeetCode 340</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z</details><br><br><details><summary>🧠 Context & Variants</summary><i>(Variants and similar questions to be added later)</i></details></td>
      <td>**Example 1:** Sliding Window.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(K)</td>
      <td><b>Explanation:</b> Sliding window with hash map to count characters. While map size > k, shrink window from left.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def lengthOfLongestSubstringKDistinct(s, k):&#10;    m = {}&#10;    left, max_len = 0, 0&#10;    for right in range(len(s)):&#10;        m[s[right]] = m.get(s[right], 0) + 1&#10;        while len(m) &gt; k:&#10;            m[s[left]] -= 1&#10;            if m[s[left]] == 0: del m[s[left]]&#10;            left += 1&#10;        max_len = max(max_len, right - left + 1)&#10;    return max_len</code></pre></details></td>
    </tr>
  </tbody>
</table>
