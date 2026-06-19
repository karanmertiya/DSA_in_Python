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
      <td>Sw 02 Longest Substring Without Repeating Characters<br><br></b> <a href='https://leetcode.com/problems/longest-substring-without-repeating-characters/' target='_blank'>LeetCode 3</a></td>
      <td><b>Example 1:</b> Input: s = "abcabcbb", Output: 3 ("abc")</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(min(N, M))</td>
      <td><code>std::vector</code> for frequency array</td>
      <td><b>Pointer Leap:</b> `left` can only jump forward, thus `std::max(left, ...)` prevents `left` from going backward if an old duplicate is found.</td>
      <td><b>Explanation:</b> Sliding window with a Hash Map storing the latest index of each character. Move `left` pointer to `max(left, map[char] + 1)`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def lengthOfLongestSubstring(s: str) -&gt; int:&#10;    mpp = {}&#10;    left = max_len = 0&#10;    for right, char in enumerate(s):&#10;        if char in mpp:&#10;            left = max(left, mpp[char] + 1)&#10;        mpp[char] = right&#10;        max_len = max(max_len, right - left + 1)&#10;    return max_len</code></pre></details></td>
    </tr>
    <tr>
      <td>2</td>
      <td>Sw 03 Trapping Rain Water<br><br></b> <a href='https://leetcode.com/problems/trapping-rain-water/' target='_blank'>LeetCode 42</a></td>
      <td><b>Example 1:</b> Input: height = [0,1,0,2,1,0,1,3,2,1,2,1], Output: 6</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>Local Maxima:</b> Water trapped at `i` relies on the absolute minimum of the highest bars to its left and right.</td>
      <td><b>Explanation:</b> Two pointers `left` and `right`. Maintain `left_max` and `right_max`. Move the pointer pointing to the smaller max, adding trapped water.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def trap(height: list[int]) -&gt; int:&#10;    left, right = 0, len(height) - 1&#10;    res, maxLeft, maxRight = 0, 0, 0&#10;    while left &lt;= right:&#10;        if height[left] &lt;= height[right]:&#10;            if height[left] &gt;= maxLeft: maxLeft = height[left]&#10;            else: res += maxLeft - height[left]&#10;            left += 1&#10;        else:&#10;            if height[right] &gt;= maxRight: maxRight = height[right]&#10;            else: res += maxRight - height[right]&#10;            right -= 1&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td>3</td>
      <td>Sw 04 Container With Most Water<br><br></b> <a href='https://leetcode.com/problems/container-with-most-water/' target='_blank'>LeetCode 11</a></td>
      <td><b>Example 1:</b> Input: height = [1,8,6,2,5,4,8,3,7], Output: 49</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><code>std::max</code>, <code>std::min</code></td>
      <td><b>Width vs Height Tradeoff:</b> By starting at maximum width, we only decrease width. Thus, we must only abandon a height if we hope to find a taller one.</td>
      <td><b>Explanation:</b> Two Pointers from ends. Area is `min(h[left], h[right]) * width`. Move the pointer with the smaller height to seek a potentially taller line.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxArea(height: list[int]) -&gt; int:&#10;    left, right = 0, len(height) - 1&#10;    max_area = 0&#10;    while left &lt; right:&#10;        area = min(height[left], height[right]) * (right - left)&#10;        max_area = max(max_area, area)&#10;        if height[left] &lt; height[right]:&#10;            left += 1&#10;        else:&#10;            right -= 1&#10;    return max_area</code></pre></details></td>
    </tr>
  </tbody>
</table>
