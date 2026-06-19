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
      <td rowspan="1">Sw 03 Trapping Rain Water<br><br></b> <a href='https://leetcode.com/problems/trapping-rain-water/' target='_blank'>LeetCode 42</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: height = [0,1,0,2,1,0,1,3,2,1,2,1], Output: 6</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>Local Maxima:</b> Water trapped at `i` relies on the absolute minimum of the highest bars to its left and right.</td>
      <td><b>Explanation:</b> Two pointers `left` and `right`. Maintain `left_max` and `right_max`. Move the pointer pointing to the smaller max, adding trapped water.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def trap(height: list[int]) -&gt; int:&#10;    left, right = 0, len(height) - 1&#10;    res, maxLeft, maxRight = 0, 0, 0&#10;    while left &lt;= right:&#10;        if height[left] &lt;= height[right]:&#10;            if height[left] &gt;= maxLeft: maxLeft = height[left]&#10;            else: res += maxLeft - height[left]&#10;            left += 1&#10;        else:&#10;            if height[right] &gt;= maxRight: maxRight = height[right]&#10;            else: res += maxRight - height[right]&#10;            right -= 1&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">2</td>
      <td rowspan="1">Sw 4 Count Occurrences Of Anagrams<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/count-occurences-of-anagrams5839/1' target='_blank'>GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Fixed window and frequency map.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(26) = O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Maintain a frequency map of the pattern. Use a sliding window of size equal to the length of the pattern. Keep track of the number of characters fully matched (`count`). If `count` equals the number of unique characters in the pattern, an anagram is found.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def search(pat: str, txt: str) -&gt; int:&#10;    k, n = len(pat), len(txt)&#10;    if k &gt; n: return 0&#10;    count = collections.Counter(pat)&#10;    distinct = len(count)&#10;    i = j = ans = 0&#10;    while j &lt; n:&#10;        if txt[j] in count:&#10;            count[txt[j]] -= 1&#10;            if count[txt[j]] == 0:&#10;                distinct -= 1&#10;        if j - i + 1 &lt; k:&#10;            j += 1&#10;        elif j - i + 1 == k:&#10;            if distinct == 0:&#10;                ans += 1&#10;            if txt[i] in count:&#10;                count[txt[i]] += 1&#10;                if count[txt[i]] == 1:&#10;                    distinct += 1&#10;            i += 1&#10;            j += 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">3</td>
      <td rowspan="1">Sw 5 Maximum Of All Subarrays Of Size K<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/maximum-of-all-subarrays-of-size-k3101/1' target='_blank'>GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Deque.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(K)</td>
      <td><code>#include <deque></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Use a deque to store indices of elements. The deque will maintain elements in decreasing order. For each element, remove elements from the back of the deque that are smaller than the current element. Also, remove elements from the front that are out of the current window. The front of the deque will always have the maximum element of the current window.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def max_of_subarrays(arr: List[int], n: int, k: int) -&gt; List[int]:&#10;    res = []&#10;    dq = collections.deque()&#10;    for i in range(n):&#10;        if dq and dq[0] == i - k:&#10;            dq.popleft()&#10;        while dq and arr[dq[-1]] &lt;= arr[i]:&#10;            dq.pop()&#10;        dq.append(i)&#10;        if i &gt;= k - 1:&#10;            res.append(arr[dq[0]])&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">4</td>
      <td rowspan="1">Sw 6 Longest Subarray With Sum K<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1' target='_blank'>GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Prefix sum with hash map.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><code>#include <unordered_map></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Keep track of the prefix sum. Store the first occurrence of each prefix sum in a hash map. If `prefix_sum - K` exists in the hash map, calculate the length of the subarray and update the maximum length.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def lenOfLongSubarr(A: List[int], N: int, K: int) -&gt; int:&#10;    preSum = {}&#10;    currSum = 0&#10;    maxLen = 0&#10;    for i in range(N):&#10;        currSum += A[i]&#10;        if currSum == K:&#10;            maxLen = max(maxLen, i + 1)&#10;        if currSum - K in preSum:&#10;            maxLen = max(maxLen, i - preSum[currSum - K])&#10;        if currSum not in preSum:&#10;            preSum[currSum] = i&#10;    return maxLen</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">5</td>
      <td rowspan="1">Sw 7 Longest Substring Without Repeating Characters<br><br></b> <a href='https://leetcode.com/problems/longest-substring-without-repeating-characters/' target='_blank'>LeetCode 3</a></td>
      <td rowspan="1"><b>Example 1:</b> Sliding window with hash set/map.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><code>#include <unordered_set></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Use a sliding window. Keep expanding the window by adding characters. If a duplicate character is found, shrink the window from the left until the duplicate is removed.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def lengthOfLongestSubstring(s: str) -&gt; int:&#10;    seen = set()&#10;    l = 0&#10;    maxLen = 0&#10;    for r in range(len(s)):&#10;        while s[r] in seen:&#10;            seen.remove(s[l])&#10;            l += 1&#10;        seen.add(s[r])&#10;        maxLen = max(maxLen, r - l + 1)&#10;    return maxLen</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">6</td>
      <td rowspan="1">Sw 8 Minimum Window Substring<br><br></b> <a href='https://leetcode.com/problems/minimum-window-substring/' target='_blank'>LeetCode 76</a></td>
      <td rowspan="1"><b>Example 1:</b> Variable sliding window.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><code>#include <unordered_map></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Maintain a frequency map of `t`. Expand the window by moving `right`. When the window contains all characters of `t`, try to shrink it by moving `left` to find the minimum window. Keep track of the minimum window length and its starting index.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def minWindow(s: str, t: str) -&gt; str:&#10;    if len(s) &lt; len(t): return &quot;&quot;&#10;    count = collections.Counter(t)&#10;    required = len(t)&#10;    l = r = 0&#10;    minLen = float(&#x27;inf&#x27;)&#10;    minStart = 0&#10;    while r &lt; len(s):&#10;        if count[s[r]] &gt; 0:&#10;            required -= 1&#10;        count[s[r]] -= 1&#10;        r += 1&#10;        while required == 0:&#10;            if r - l &lt; minLen:&#10;                minLen = r - l&#10;                minStart = l&#10;            count[s[l]] += 1&#10;            if count[s[l]] &gt; 0:&#10;                required += 1&#10;            l += 1&#10;    return &quot;&quot; if minLen == float(&#x27;inf&#x27;) else s[minStart:minStart+minLen]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">7</td>
      <td rowspan="1">Sw 9 Sliding Window Maximum<br><br></b> <a href='https://leetcode.com/problems/sliding-window-maximum/' target='_blank'>LeetCode 239</a></td>
      <td rowspan="1"><b>Example 1:</b> Deque.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(K)</td>
      <td><code>#include <deque></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Use a deque to store indices. The deque maintains elements in decreasing order. Remove elements from the back if they are smaller than the current element. Remove elements from the front if they are out of the window. The front element is the maximum of the current window.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def maxSlidingWindow(nums: List[int], k: int) -&gt; List[int]:&#10;    res = []&#10;    dq = collections.deque()&#10;    for i in range(len(nums)):&#10;        if dq and dq[0] == i - k:&#10;            dq.popleft()&#10;        while dq and nums[dq[-1]] &lt;= nums[i]:&#10;            dq.pop()&#10;        dq.append(i)&#10;        if i &gt;= k - 1:&#10;            res.append(nums[dq[0]])&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">8</td>
      <td rowspan="1">Sw 10 Longest K Unique Characters Substring<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1' target='_blank'>GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Variable window and hash map.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(K)</td>
      <td><code>#include <unordered_map></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Maintain a hash map of character frequencies. Expand the window by moving `j`. If the number of unique characters exceeds `k`, shrink the window from the left (`i`) until the number of unique characters is `k`. Update the maximum length when exactly `k` unique characters are present.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def longestKSubstr(s: str, k: int) -&gt; int:&#10;    count = collections.defaultdict(int)&#10;    i = j = 0&#10;    maxLen = -1&#10;    while j &lt; len(s):&#10;        count[s[j]] += 1&#10;        if len(count) == k:&#10;            maxLen = max(maxLen, j - i + 1)&#10;        elif len(count) &gt; k:&#10;            while len(count) &gt; k:&#10;                count[s[i]] -= 1&#10;                if count[s[i]] == 0:&#10;                    del count[s[i]]&#10;                i += 1&#10;        j += 1&#10;    return maxLen</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">9</td>
      <td rowspan="1">Sw 11 Subarrays With K Different Integers<br><br></b> <a href='https://leetcode.com/problems/subarrays-with-k-different-integers/' target='_blank'>LeetCode 992</a></td>
      <td rowspan="1"><b>Example 1:</b> Exact K = atMost(K) - atMost(K-1).</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><code>#include <unordered_map></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Finding exact `k` distinct is hard directly. Instead, find subarrays with at most `k` distinct integers. The number of exact `k` is `atMost(k) - atMost(k - 1)`. The `atMost` function uses a sliding window.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def subarraysWithKDistinct(nums: List[int], k: int) -&gt; int:&#10;    def atMost(k):&#10;        count = collections.defaultdict(int)&#10;        res = i = 0&#10;        for j in range(len(nums)):&#10;            if count[nums[j]] == 0: k -= 1&#10;            count[nums[j]] += 1&#10;            while k &lt; 0:&#10;                count[nums[i]] -= 1&#10;                if count[nums[i]] == 0: k += 1&#10;                i += 1&#10;            res += j - i + 1&#10;        return res&#10;    return atMost(k) - atMost(k - 1)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">10</td>
      <td rowspan="1">Sw 12 Minimum Size Subarray Sum<br><br></b> <a href='https://leetcode.com/problems/minimum-size-subarray-sum/' target='_blank'>LeetCode 209</a></td>
      <td rowspan="1"><b>Example 1:</b> Variable sliding window.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Use a sliding window. Add elements to the current sum. While the sum is >= target, update the minimum length and shrink the window from the left.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minSubArrayLen(target: int, nums: List[int]) -&gt; int:&#10;    l = sum = 0&#10;    minLen = float(&#x27;inf&#x27;)&#10;    for r in range(len(nums)):&#10;        sum += nums[r]&#10;        while sum &gt;= target:&#10;            minLen = min(minLen, r - l + 1)&#10;            sum -= nums[l]&#10;            l += 1&#10;    return 0 if minLen == float(&#x27;inf&#x27;) else minLen</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">11</td>
      <td rowspan="1">Sw 13 Fruits Into Baskets<br><br></b> <a href='https://leetcode.com/problems/fruit-into-baskets/' target='_blank'>LeetCode 904</a></td>
      <td rowspan="1"><b>Example 1:</b> Longest subarray with at most 2 distinct elements.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1) (at most 3 elements in map)</td>
      <td><code>#include <unordered_map></code></td>
      <td>-</td>
      <td><b>Explanation:</b> This translates to finding the longest subarray with at most 2 distinct elements. Maintain a frequency map and use a sliding window. If distinct elements > 2, shrink the window until distinct elements <= 2.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def totalFruit(fruits: List[int]) -&gt; int:&#10;    count = collections.defaultdict(int)&#10;    l = maxFruits = 0&#10;    for r in range(len(fruits)):&#10;        count[fruits[r]] += 1&#10;        while len(count) &gt; 2:&#10;            count[fruits[l]] -= 1&#10;            if count[fruits[l]] == 0:&#10;                del count[fruits[l]]&#10;            l += 1&#10;        maxFruits = max(maxFruits, r - l + 1)&#10;    return maxFruits</code></pre></details></td>
    </tr>
  </tbody>
</table>
