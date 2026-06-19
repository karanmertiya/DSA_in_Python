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
      <td>1</td>
      <td>Sw 03 Trapping Rain Water<br><br></b> <a href='https://leetcode.com/problems/trapping-rain-water/' target='_blank'>LeetCode 42</a></td>
      <td><b>Example 1:</b> Input: height = [0,1,0,2,1,0,1,3,2,1,2,1], Output: 6</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>Local Maxima:</b> Water trapped at `i` relies on the absolute minimum of the highest bars to its left and right.</td>
      <td><b>Explanation:</b> Two pointers `left` and `right`. Maintain `left_max` and `right_max`. Move the pointer pointing to the smaller max, adding trapped water.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def trap(height: list[int]) -&gt; int:&#10;    left, right = 0, len(height) - 1&#10;    res, maxLeft, maxRight = 0, 0, 0&#10;    while left &lt;= right:&#10;        if height[left] &lt;= height[right]:&#10;            if height[left] &gt;= maxLeft: maxLeft = height[left]&#10;            else: res += maxLeft - height[left]&#10;            left += 1&#10;        else:&#10;            if height[right] &gt;= maxRight: maxRight = height[right]&#10;            else: res += maxRight - height[right]&#10;            right -= 1&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td>2</td>
      <td>Sw 4 Count Occurrences Of Anagrams<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/count-occurences-of-anagrams5839/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Fixed window and frequency map.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(26) = O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Maintain a frequency map of the pattern. Use a sliding window of size equal to the length of the pattern. Keep track of the number of characters fully matched (`count`). If `count` equals the number of unique characters in the pattern, an anagram is found.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def search(pat: str, txt: str) -&gt; int:&#10;    k, n = len(pat), len(txt)&#10;    if k &gt; n: return 0&#10;    count = collections.Counter(pat)&#10;    distinct = len(count)&#10;    i = j = ans = 0&#10;    while j &lt; n:&#10;        if txt[j] in count:&#10;            count[txt[j]] -= 1&#10;            if count[txt[j]] == 0:&#10;                distinct -= 1&#10;        if j - i + 1 &lt; k:&#10;            j += 1&#10;        elif j - i + 1 == k:&#10;            if distinct == 0:&#10;                ans += 1&#10;            if txt[i] in count:&#10;                count[txt[i]] += 1&#10;                if count[txt[i]] == 1:&#10;                    distinct += 1&#10;            i += 1&#10;            j += 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>3</td>
      <td>Sw 5 Maximum Of All Subarrays Of Size K<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/maximum-of-all-subarrays-of-size-k3101/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Deque.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(K)</td>
      <td><code>#include <deque></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Use a deque to store indices of elements. The deque will maintain elements in decreasing order. For each element, remove elements from the back of the deque that are smaller than the current element. Also, remove elements from the front that are out of the current window. The front of the deque will always have the maximum element of the current window.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def max_of_subarrays(arr: List[int], n: int, k: int) -&gt; List[int]:&#10;    res = []&#10;    dq = collections.deque()&#10;    for i in range(n):&#10;        if dq and dq[0] == i - k:&#10;            dq.popleft()&#10;        while dq and arr[dq[-1]] &lt;= arr[i]:&#10;            dq.pop()&#10;        dq.append(i)&#10;        if i &gt;= k - 1:&#10;            res.append(arr[dq[0]])&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td>4</td>
      <td>Sw 6 Longest Subarray With Sum K<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Prefix sum with hash map.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><code>#include <unordered_map></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Keep track of the prefix sum. Store the first occurrence of each prefix sum in a hash map. If `prefix_sum - K` exists in the hash map, calculate the length of the subarray and update the maximum length.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def lenOfLongSubarr(A: List[int], N: int, K: int) -&gt; int:&#10;    preSum = {}&#10;    currSum = 0&#10;    maxLen = 0&#10;    for i in range(N):&#10;        currSum += A[i]&#10;        if currSum == K:&#10;            maxLen = max(maxLen, i + 1)&#10;        if currSum - K in preSum:&#10;            maxLen = max(maxLen, i - preSum[currSum - K])&#10;        if currSum not in preSum:&#10;            preSum[currSum] = i&#10;    return maxLen</code></pre></details></td>
    </tr>
    <tr>
      <td>5</td>
      <td>Sw 7 Longest Substring Without Repeating Characters<br><br></b> <a href='https://leetcode.com/problems/longest-substring-without-repeating-characters/' target='_blank'>LeetCode 3</a></td>
      <td><b>Example 1:</b> Sliding window with hash set/map.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><code>#include <unordered_set></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Use a sliding window. Keep expanding the window by adding characters. If a duplicate character is found, shrink the window from the left until the duplicate is removed.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def lengthOfLongestSubstring(s: str) -&gt; int:&#10;    seen = set()&#10;    l = 0&#10;    maxLen = 0&#10;    for r in range(len(s)):&#10;        while s[r] in seen:&#10;            seen.remove(s[l])&#10;            l += 1&#10;        seen.add(s[r])&#10;        maxLen = max(maxLen, r - l + 1)&#10;    return maxLen</code></pre></details></td>
    </tr>
    <tr>
      <td>6</td>
      <td>Sw 8 Minimum Window Substring<br><br></b> <a href='https://leetcode.com/problems/minimum-window-substring/' target='_blank'>LeetCode 76</a></td>
      <td><b>Example 1:</b> Variable sliding window.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><code>#include <unordered_map></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Maintain a frequency map of `t`. Expand the window by moving `right`. When the window contains all characters of `t`, try to shrink it by moving `left` to find the minimum window. Keep track of the minimum window length and its starting index.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def minWindow(s: str, t: str) -&gt; str:&#10;    if len(s) &lt; len(t): return &quot;&quot;&#10;    count = collections.Counter(t)&#10;    required = len(t)&#10;    l = r = 0&#10;    minLen = float(&#x27;inf&#x27;)&#10;    minStart = 0&#10;    while r &lt; len(s):&#10;        if count[s[r]] &gt; 0:&#10;            required -= 1&#10;        count[s[r]] -= 1&#10;        r += 1&#10;        while required == 0:&#10;            if r - l &lt; minLen:&#10;                minLen = r - l&#10;                minStart = l&#10;            count[s[l]] += 1&#10;            if count[s[l]] &gt; 0:&#10;                required += 1&#10;            l += 1&#10;    return &quot;&quot; if minLen == float(&#x27;inf&#x27;) else s[minStart:minStart+minLen]</code></pre></details></td>
    </tr>
    <tr>
      <td>7</td>
      <td>Sw 9 Sliding Window Maximum<br><br></b> <a href='https://leetcode.com/problems/sliding-window-maximum/' target='_blank'>LeetCode 239</a></td>
      <td><b>Example 1:</b> Deque.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(K)</td>
      <td><code>#include <deque></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Use a deque to store indices. The deque maintains elements in decreasing order. Remove elements from the back if they are smaller than the current element. Remove elements from the front if they are out of the window. The front element is the maximum of the current window.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def maxSlidingWindow(nums: List[int], k: int) -&gt; List[int]:&#10;    res = []&#10;    dq = collections.deque()&#10;    for i in range(len(nums)):&#10;        if dq and dq[0] == i - k:&#10;            dq.popleft()&#10;        while dq and nums[dq[-1]] &lt;= nums[i]:&#10;            dq.pop()&#10;        dq.append(i)&#10;        if i &gt;= k - 1:&#10;            res.append(nums[dq[0]])&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td>8</td>
      <td>Sw 10 Longest K Unique Characters Substring<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Variable window and hash map.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(K)</td>
      <td><code>#include <unordered_map></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Maintain a hash map of character frequencies. Expand the window by moving `j`. If the number of unique characters exceeds `k`, shrink the window from the left (`i`) until the number of unique characters is `k`. Update the maximum length when exactly `k` unique characters are present.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def longestKSubstr(s: str, k: int) -&gt; int:&#10;    count = collections.defaultdict(int)&#10;    i = j = 0&#10;    maxLen = -1&#10;    while j &lt; len(s):&#10;        count[s[j]] += 1&#10;        if len(count) == k:&#10;            maxLen = max(maxLen, j - i + 1)&#10;        elif len(count) &gt; k:&#10;            while len(count) &gt; k:&#10;                count[s[i]] -= 1&#10;                if count[s[i]] == 0:&#10;                    del count[s[i]]&#10;                i += 1&#10;        j += 1&#10;    return maxLen</code></pre></details></td>
    </tr>
    <tr>
      <td>9</td>
      <td>Sw 11 Subarrays With K Different Integers<br><br></b> <a href='https://leetcode.com/problems/subarrays-with-k-different-integers/' target='_blank'>LeetCode 992</a></td>
      <td><b>Example 1:</b> Exact K = atMost(K) - atMost(K-1).</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><code>#include <unordered_map></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Finding exact `k` distinct is hard directly. Instead, find subarrays with at most `k` distinct integers. The number of exact `k` is `atMost(k) - atMost(k - 1)`. The `atMost` function uses a sliding window.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def subarraysWithKDistinct(nums: List[int], k: int) -&gt; int:&#10;    def atMost(k):&#10;        count = collections.defaultdict(int)&#10;        res = i = 0&#10;        for j in range(len(nums)):&#10;            if count[nums[j]] == 0: k -= 1&#10;            count[nums[j]] += 1&#10;            while k &lt; 0:&#10;                count[nums[i]] -= 1&#10;                if count[nums[i]] == 0: k += 1&#10;                i += 1&#10;            res += j - i + 1&#10;        return res&#10;    return atMost(k) - atMost(k - 1)</code></pre></details></td>
    </tr>
    <tr>
      <td>10</td>
      <td>Sw 12 Minimum Size Subarray Sum<br><br></b> <a href='https://leetcode.com/problems/minimum-size-subarray-sum/' target='_blank'>LeetCode 209</a></td>
      <td><b>Example 1:</b> Variable sliding window.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Use a sliding window. Add elements to the current sum. While the sum is >= target, update the minimum length and shrink the window from the left.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minSubArrayLen(target: int, nums: List[int]) -&gt; int:&#10;    l = sum = 0&#10;    minLen = float(&#x27;inf&#x27;)&#10;    for r in range(len(nums)):&#10;        sum += nums[r]&#10;        while sum &gt;= target:&#10;            minLen = min(minLen, r - l + 1)&#10;            sum -= nums[l]&#10;            l += 1&#10;    return 0 if minLen == float(&#x27;inf&#x27;) else minLen</code></pre></details></td>
    </tr>
    <tr>
      <td>11</td>
      <td>Sw 13 Fruits Into Baskets<br><br></b> <a href='https://leetcode.com/problems/fruit-into-baskets/' target='_blank'>LeetCode 904</a></td>
      <td><b>Example 1:</b> Longest subarray with at most 2 distinct elements.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1) (at most 3 elements in map)</td>
      <td><code>#include <unordered_map></code></td>
      <td>-</td>
      <td><b>Explanation:</b> This translates to finding the longest subarray with at most 2 distinct elements. Maintain a frequency map and use a sliding window. If distinct elements > 2, shrink the window until distinct elements <= 2.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def totalFruit(fruits: List[int]) -&gt; int:&#10;    count = collections.defaultdict(int)&#10;    l = maxFruits = 0&#10;    for r in range(len(fruits)):&#10;        count[fruits[r]] += 1&#10;        while len(count) &gt; 2:&#10;            count[fruits[l]] -= 1&#10;            if count[fruits[l]] == 0:&#10;                del count[fruits[l]]&#10;            l += 1&#10;        maxFruits = max(maxFruits, r - l + 1)&#10;    return maxFruits</code></pre></details></td>
    </tr>
    <tr>
      <td>12</td>
      <td>Sw 08 Max Consecutive Ones Iii<br><br></b> <a href='https://leetcode.com/problems/max-consecutive-ones-iii/' target='_blank'>LeetCode 1004</a></td>
      <td><b>Example 1:</b> Sliding Window.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Use a sliding window. Expand the right pointer. If the element is 0, increment a zero counter. While the zero counter > k, shrink the window from the left by moving the left pointer and decrementing the zero counter if left element is 0. The max window size is the answer.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def longestOnes(nums, k):&#10;    left = 0&#10;    zeroes = 0&#10;    max_len = 0&#10;    for right in range(len(nums)):&#10;        if nums[right] == 0: zeroes += 1&#10;        while zeroes &gt; k:&#10;            if nums[left] == 0: zeroes -= 1&#10;            left += 1&#10;        max_len = max(max_len, right - left + 1)&#10;    return max_len</code></pre></details></td>
    </tr>
    <tr>
      <td>13</td>
      <td>Sw 09 Fruit Into Baskets<br><br></b> <a href='https://leetcode.com/problems/fruit-into-baskets/' target='_blank'>LeetCode 904</a></td>
      <td><b>Example 1:</b> Longest Subarray with at most 2 distinct elements.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Hash Map</td>
      <td>-</td>
      <td><b>Explanation:</b> This translates to finding the longest subarray with at most 2 distinct elements. Use a hash map to keep track of fruit counts in the current window. Expand right, update map. If map size > 2, shrink from left until map size is 2.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def totalFruit(fruits):&#10;    count = {}&#10;    left = 0&#10;    max_len = 0&#10;    for right in range(len(fruits)):&#10;        count[fruits[right]] = count.get(fruits[right], 0) + 1&#10;        while len(count) &gt; 2:&#10;            count[fruits[left]] -= 1&#10;            if count[fruits[left]] == 0: del count[fruits[left]]&#10;            left += 1&#10;        max_len = max(max_len, right - left + 1)&#10;    return max_len</code></pre></details></td>
    </tr>
    <tr>
      <td>14</td>
      <td>Sw 10 Longest Repeating Character Replacement<br><br></b> <a href='https://leetcode.com/problems/longest-repeating-character-replacement/' target='_blank'>LeetCode 424</a></td>
      <td><b>Example 1:</b> Sliding Window + Max Freq.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Use a sliding window. Maintain the character frequencies and the `max_freq` in the window. The number of replacements needed is `window_size - max_freq`. If this is > k, shrink the window from left and decrement the corresponding frequency.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def characterReplacement(s, k):&#10;    count = [0] * 26&#10;    left = 0&#10;    max_freq = 0&#10;    max_len = 0&#10;    for right in range(len(s)):&#10;        count[ord(s[right]) - ord(&#x27;A&#x27;)] += 1&#10;        max_freq = max(max_freq, count[ord(s[right]) - ord(&#x27;A&#x27;)])&#10;        if (right - left + 1) - max_freq &gt; k:&#10;            count[ord(s[left]) - ord(&#x27;A&#x27;)] -= 1&#10;            left += 1&#10;        max_len = max(max_len, right - left + 1)&#10;    return max_len</code></pre></details></td>
    </tr>
    <tr>
      <td>15</td>
      <td>Sw 11 Binary Subarrays With Sum<br><br></b> <a href='https://leetcode.com/problems/binary-subarrays-with-sum/' target='_blank'>LeetCode 930</a></td>
      <td><b>Example 1:</b> atMost(goal) - atMost(goal - 1).</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Use the helper function `atMost(goal)` which finds the number of subarrays with sum <= goal. The answer is `atMost(goal) - atMost(goal - 1)`. In `atMost`, use a sliding window to maintain the sum.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def numSubarraysWithSum(nums, goal):&#10;    def atMost(k):&#10;        if k &lt; 0: return 0&#10;        left, sum_val, count = 0, 0, 0&#10;        for right in range(len(nums)):&#10;            sum_val += nums[right]&#10;            while sum_val &gt; k:&#10;                sum_val -= nums[left]&#10;                left += 1&#10;            count += (right - left + 1)&#10;        return count&#10;    return atMost(goal) - atMost(goal - 1)</code></pre></details></td>
    </tr>
    <tr>
      <td>16</td>
      <td>Sw 12 Count Number Of Nice Subarrays<br><br></b> <a href='https://leetcode.com/problems/count-number-of-nice-subarrays/' target='_blank'>LeetCode 1248</a></td>
      <td><b>Example 1:</b> atMost(k) - atMost(k - 1).</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Replace all odd numbers with 1 and even numbers with 0. The problem then reduces to finding the number of subarrays with a sum equal to k. Use the `atMost(k) - atMost(k - 1)` sliding window approach.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def numberOfSubarrays(nums, k):&#10;    def atMost(limit):&#10;        if limit &lt; 0: return 0&#10;        left, count, res = 0, 0, 0&#10;        for right in range(len(nums)):&#10;            if nums[right] % 2 != 0: count += 1&#10;            while count &gt; limit:&#10;                if nums[left] % 2 != 0: count -= 1&#10;                left += 1&#10;            res += (right - left + 1)&#10;        return res&#10;    return atMost(k) - atMost(k - 1)</code></pre></details></td>
    </tr>
    <tr>
      <td>17</td>
      <td>Sw 13 Number Of Substrings Containing All Three Characters<br><br></b> <a href='https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/' target='_blank'>LeetCode 1358</a></td>
      <td><b>Example 1:</b> Store last seen indices.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Iterate through the string. Track the last seen indices of 'a', 'b', and 'c'. If all three have been seen, the number of valid substrings ending at the current index `i` is `1 + min(last_a, last_b, last_c)`. Add this to the total count.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def numberOfSubstrings(s):&#10;    last = [-1, -1, -1]&#10;    count = 0&#10;    for i in range(len(s)):&#10;        last[ord(s[i]) - ord(&#x27;a&#x27;)] = i&#10;        if last[0] != -1 and last[1] != -1 and last[2] != -1:&#10;            count += 1 + min(last)&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td>18</td>
      <td>Sw 14 Maximum Points You Can Obtain From Cards<br><br></b> <a href='https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/' target='_blank'>LeetCode 1423</a></td>
      <td><b>Example 1:</b> Sliding Window on remaining cards.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Instead of picking cards from the ends, find the subarray of length `N - K` that has the minimum sum. Subtract this minimum sum from the total sum of the array. That gives the maximum score.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxScore(cardPoints, k):&#10;    n = len(cardPoints)&#10;    total_sum = sum(cardPoints)&#10;    window_size = n - k&#10;    window_sum = sum(cardPoints[:window_size])&#10;    min_window_sum = window_sum&#10;    for i in range(window_size, n):&#10;        window_sum += cardPoints[i] - cardPoints[i - window_size]&#10;        min_window_sum = min(min_window_sum, window_sum)&#10;    return total_sum - min_window_sum</code></pre></details></td>
    </tr>
    <tr>
      <td>19</td>
      <td>Sw 15 Subarrays With K Different Integers<br><br></b> <a href='https://leetcode.com/problems/subarrays-with-k-different-integers/' target='_blank'>LeetCode 992</a></td>
      <td><b>Example 1:</b> atMost(k) - atMost(k - 1).</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Hash Map</td>
      <td>-</td>
      <td><b>Explanation:</b> Like "Binary Subarrays With Sum", the number of subarrays with exactly k distinct integers is `atMost(k) - atMost(k-1)`. The `atMost` function uses a sliding window with a hash map to track the frequencies of elements.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def subarraysWithKDistinct(nums, k):&#10;    def atMost(limit):&#10;        if limit == 0: return 0&#10;        count = {}&#10;        left, res = 0, 0&#10;        for right in range(len(nums)):&#10;            count[nums[right]] = count.get(nums[right], 0) + 1&#10;            while len(count) &gt; limit:&#10;                count[nums[left]] -= 1&#10;                if count[nums[left]] == 0: del count[nums[left]]&#10;                left += 1&#10;            res += (right - left + 1)&#10;        return res&#10;    return atMost(k) - atMost(k - 1)</code></pre></details></td>
    </tr>
    <tr>
      <td>20</td>
      <td>Sw 16 Minimum Window Substring<br><br></b> <a href='https://leetcode.com/problems/minimum-window-substring/' target='_blank'>LeetCode 76</a></td>
      <td><b>Example 1:</b> Hash map + Sliding Window.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>t > s length</td>
      <td><b>Explanation:</b> Store frequency of chars in `t`. Use `left` and `right` pointers. Expand `right`, if the character is in `t`, decrease its required count. If all characters are found, update the minimum length and start shrinking from `left`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minWindow(s, t):&#10;    count = [0] * 128&#10;    for c in t: count[ord(c)] += 1&#10;    required = len(t)&#10;    left, min_len, min_start = 0, float(&#x27;inf&#x27;), 0&#10;    for right in range(len(s)):&#10;        if count[ord(s[right])] &gt; 0: required -= 1&#10;        count[ord(s[right])] -= 1&#10;        while required == 0:&#10;            if right - left + 1 &lt; min_len:&#10;                min_len = right - left + 1&#10;                min_start = left&#10;            count[ord(s[left])] += 1&#10;            if count[ord(s[left])] &gt; 0: required += 1&#10;            left += 1&#10;    return &quot;&quot; if min_len == float(&#x27;inf&#x27;) else s[min_start:min_start + min_len]</code></pre></details></td>
    </tr>
    <tr>
      <td>21</td>
      <td>Sw 17 Find All Anagrams In A String<br><br></b> <a href='https://leetcode.com/problems/find-all-anagrams-in-a-string/' target='_blank'>LeetCode 438</a></td>
      <td><b>Example 1:</b> Fixed Window + Hash Map.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Create frequency arrays for `p` and a window of size `p.length()` in `s`. Slide the window across `s`, updating the window frequencies. If the arrays match, add the window's start index to the result.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findAnagrams(s, p):&#10;    ans = []&#10;    if len(p) &gt; len(s): return ans&#10;    countP, countS = [0]*26, [0]*26&#10;    for i in range(len(p)):&#10;        countP[ord(p[i]) - ord(&#x27;a&#x27;)] += 1&#10;        countS[ord(s[i]) - ord(&#x27;a&#x27;)] += 1&#10;    if countP == countS: ans.append(0)&#10;    for i in range(len(p), len(s)):&#10;        countS[ord(s[i]) - ord(&#x27;a&#x27;)] += 1&#10;        countS[ord(s[i - len(p)]) - ord(&#x27;a&#x27;)] -= 1&#10;        if countP == countS: ans.append(i - len(p) + 1)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>22</td>
      <td>Sw 18 Longest K Unique Characters Substring<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Sliding Window + Hash Map.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(K)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Use a sliding window `[left, right]` and a hash map to count characters. If map size > K, shrink window from `left` until map size == K. If map size == K, update max length.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def longestKSubstr(s, k):&#10;    m = {}&#10;    left, max_len = 0, -1&#10;    for right in range(len(s)):&#10;        m[s[right]] = m.get(s[right], 0) + 1&#10;        if len(m) == k: max_len = max(max_len, right - left + 1)&#10;        elif len(m) &gt; k:&#10;            while len(m) &gt; k:&#10;                m[s[left]] -= 1&#10;                if m[s[left]] == 0: del m[s[left]]&#10;                left += 1&#10;    return max_len</code></pre></details></td>
    </tr>
    <tr>
      <td>23</td>
      <td>Sw 19 Permutation In String<br><br></b> <a href='https://leetcode.com/problems/permutation-in-string/' target='_blank'>LeetCode 567</a></td>
      <td><b>Example 1:</b> Sliding Window + Frequency Array.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Use a sliding window of size `len(s1)` over `s2`. Maintain frequency arrays for `s1` and the current window in `s2`. Compare arrays at each step.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def checkInclusion(s1, s2):&#10;    if len(s1) &gt; len(s2): return False&#10;    c1, c2 = [0]*26, [0]*26&#10;    for i in range(len(s1)):&#10;        c1[ord(s1[i]) - 97] += 1&#10;        c2[ord(s2[i]) - 97] += 1&#10;    if c1 == c2: return True&#10;    for i in range(len(s1), len(s2)):&#10;        c2[ord(s2[i]) - 97] += 1&#10;        c2[ord(s2[i - len(s1)]) - 97] -= 1&#10;        if c1 == c2: return True&#10;    return False</code></pre></details></td>
    </tr>
    <tr>
      <td>24</td>
      <td>Sw 20 Sliding Window Maximum<br><br></b> <a href='https://leetcode.com/problems/sliding-window-maximum/' target='_blank'>LeetCode 239</a></td>
      <td><b>Example 1:</b> Deque.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(K)</td>
      <td>Deque</td>
      <td>-</td>
      <td><b>Explanation:</b> Use a double-ended queue (deque) to store indices. Maintain indices in the deque such that the elements they correspond to are in decreasing order. The front of the deque will always be the maximum for the current window. Remove indices from the front if they are out of the window (`i - k`).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">from collections import deque&#10;def maxSlidingWindow(nums, k):&#10;    dq = deque()&#10;    ans = []&#10;    for i in range(len(nums)):&#10;        if dq and dq[0] == i - k: dq.popleft()&#10;        while dq and nums[dq[-1]] &lt; nums[i]: dq.pop()&#10;        dq.append(i)&#10;        if i &gt;= k - 1: ans.append(nums[dq[0]])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>25</td>
      <td>Sw 21 Minimum Size Subarray Sum<br><br></b> <a href='https://leetcode.com/problems/minimum-size-subarray-sum/' target='_blank'>LeetCode 209</a></td>
      <td><b>Example 1:</b> Sliding Window.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Use a sliding window. Add elements to `sum`. While `sum >= target`, update `min_len` and subtract `nums[left]` from `sum`, incrementing `left`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minSubArrayLen(target, nums):&#10;    left, minLen, sum_val = 0, float(&#x27;inf&#x27;), 0&#10;    for right in range(len(nums)):&#10;        sum_val += nums[right]&#10;        while sum_val &gt;= target:&#10;            minLen = min(minLen, right - left + 1)&#10;            sum_val -= nums[left]&#10;            left += 1&#10;    return 0 if minLen == float(&#x27;inf&#x27;) else minLen</code></pre></details></td>
    </tr>
    <tr>
      <td>26</td>
      <td>Sw 22 First Negative Integer In Every Window Of Size K<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Queue.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(K)</td>
      <td>Queue</td>
      <td>-</td>
      <td><b>Explanation:</b> Maintain a queue of negative integers in the current window. While moving the window, add new negative integers, remove old ones out of window. The front of queue is the first negative.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">from collections import deque&#10;def printFirstNegativeInteger(A, N, K):&#10;    ans = []&#10;    q = deque()&#10;    for i in range(K - 1):&#10;        if A[i] &lt; 0: q.append(A[i])&#10;    for i in range(K - 1, N):&#10;        if A[i] &lt; 0: q.append(A[i])&#10;        ans.append(q[0] if q else 0)&#10;        if A[i - K + 1] &lt; 0 and q and q[0] == A[i - K + 1]: q.popleft()&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>27</td>
      <td>Sw 23 Count Occurrences Of Anagrams<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/count-occurences-of-anagrams1536/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Sliding Window + Frequency Map.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Use a sliding window of size `pat.length()`. Keep frequency map of `pat`. Track `count` of distinct characters to match. While moving window, decrease `count` if char frequency matches. If `count == 0`, increment answer.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def search(pat, txt):&#10;    m = {}&#10;    for c in pat: m[c] = m.get(c, 0) + 1&#10;    count, ans, k = len(m), 0, len(pat)&#10;    i = 0&#10;    for j in range(len(txt)):&#10;        if txt[j] in m:&#10;            m[txt[j]] -= 1&#10;            if m[txt[j]] == 0: count -= 1&#10;        if j - i + 1 == k:&#10;            if count == 0: ans += 1&#10;            if txt[i] in m:&#10;                m[txt[i]] += 1&#10;                if m[txt[i]] == 1: count += 1&#10;            i += 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>28</td>
      <td>Sw 24 Maximum Of All Subarrays Of Size K<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/maximum-of-all-subarrays-of-size-k3101/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Deque.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(K)</td>
      <td>Deque</td>
      <td>-</td>
      <td><b>Explanation:</b> Same as LeetCode 239. Use a deque to maintain decreasing order of elements in the current window.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">from collections import deque&#10;def max_of_subarrays(arr, n, k):&#10;    dq = deque()&#10;    ans = []&#10;    for i in range(n):&#10;        if dq and dq[0] == i - k: dq.popleft()&#10;        while dq and arr[dq[-1]] &lt;= arr[i]: dq.pop()&#10;        dq.append(i)&#10;        if i &gt;= k - 1: ans.append(arr[dq[0]])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>29</td>
      <td>Sw 25 Smallest Window In A String Containing All The Characters Of Another String<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/smallest-window-in-a-string-containing-all-the-characters-of-another-string-1587115621/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Sliding Window.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Same as Minimum Window Substring. Use frequency map of `P` and a sliding window over `S`. Shrink window from left when all characters match to find the minimum length.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def smallestWindow(s, p):&#10;    if len(p) &gt; len(s): return &quot;-1&quot;&#10;    m = {}&#10;    for c in p: m[c] = m.get(c, 0) + 1&#10;    count, minLen, start, i = len(m), float(&#x27;inf&#x27;), 0, 0&#10;    for j in range(len(s)):&#10;        if s[j] in m:&#10;            m[s[j]] -= 1&#10;            if m[s[j]] == 0: count -= 1&#10;        while count == 0:&#10;            if j - i + 1 &lt; minLen:&#10;                minLen = j - i + 1&#10;                start = i&#10;            if s[i] in m:&#10;                m[s[i]] += 1&#10;                if m[s[i]] &gt; 0: count += 1&#10;            i += 1&#10;    return &quot;-1&quot; if minLen == float(&#x27;inf&#x27;) else s[start:start+minLen]</code></pre></details></td>
    </tr>
  </tbody>
</table>
