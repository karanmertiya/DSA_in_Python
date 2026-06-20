# Day 30 Misc Revision Table

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
      <td>Math 01 Count Digits<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/count-digits5716/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: N = 12345, Output: 5</td>
      <td><details><summary><b>Approach 1</b></summary><b>Time:</b> O(1)<br><b>Space:</b> O(1)</details><details><summary><b>Approach 2</b></summary><b>Time:</b> O(log10 N)<br><b>Space:</b> O(1)</details><details><summary><b>Approach 3</b></summary><b>Time:</b> O(1)<br><b>Space:</b> O(1)</details></td>
      <td><details><summary><b>Approach 1</b></summary><b>Explanation:</b> Convert the number to a string and return its length.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def countDigits(n: int) -&gt; int:&#10;    return len(str(n))</code></pre></details></details><details><summary><b>Approach 2</b></summary><b>Explanation:</b> Use a while loop to repeatedly divide the number by 10 and increment a counter.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def countDigits(n: int) -&gt; int:&#10;    if n == 0: return 1&#10;    count = 0&#10;    while n &gt; 0:&#10;        count += 1&#10;        n //= 10&#10;    return count</code></pre></details></details><details><summary><b>Approach 3</b></summary><b>Explanation:</b> Use the base-10 logarithm function to find the number of digits mathematically.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import math&#10;def countDigits(n: int) -&gt; int:&#10;    if n == 0: return 1&#10;    return int(math.log10(n) + 1)</code></pre></details></details></td>
    </tr>
    <tr>
      <td>2</td>
      <td>Math 02 Reverse Integer<br><br></b> <a href="https://leetcode.com/problems/reverse-integer/" target="_blank">LeetCode 7</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: x = 123, Output: 321</td>
      <td><details><summary><b>Approach 1</b></summary><b>Time:</b> O(log10 x)<br><b>Space:</b> O(1)</details><details><summary><b>Approach 2</b></summary><b>Time:</b> O(log10 x)<br><b>Space:</b> O(1)</details></td>
      <td><details><summary><b>Approach 1</b></summary><b>Explanation:</b> Strict 32-bit environment (LeetCode standard): Extract digit, check for overflow against INT_MAX/10 and INT_MIN/10 *before* multiplying ans by 10.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def reverse(x: int) -&gt; int:&#10;    sign = [1, -1][x &lt; 0]&#10;    ans = int(str(abs(x))[::-1])&#10;    return sign * ans if ans &lt;= 2**31 - 1 else 0</code></pre></details></details><details><summary><b>Approach 2</b></summary><b>Explanation:</b> Relaxed 64-bit environment: Store answer in a 64-bit integer (`long long`). At the end, check if it exceeds 32-bit bounds and return 0 if it does.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def reverse(x: int) -&gt; int:&#10;    # Python handles arbitrarily large integers natively.&#10;    # So we simply reverse and check against 32-bit bounds.&#10;    ans = int(str(abs(x))[::-1])&#10;    if x &lt; 0: ans = -ans&#10;    if ans &gt; 2**31 - 1 or ans &lt; -2**31: return 0&#10;    return ans</code></pre></details></details></td>
    </tr>
    <tr>
      <td>3</td>
      <td>Math 03 Palindrome Number<br><br></b> <a href="https://leetcode.com/problems/palindrome-number/" target="_blank">LeetCode 9</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: x = 121, Output: true</td>
      <td><b>Time:</b> O(log10 x)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Negative numbers are false. Reverse half the number. If original equals reversed, it is a palindrome.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isPalindrome(x: int) -&gt; bool:&#10;    if x &lt; 0 or (x % 10 == 0 and x != 0): return False&#10;    rev = 0&#10;    while x &gt; rev:&#10;        rev = rev * 10 + x % 10&#10;        x //= 10&#10;    return x == rev or x == rev // 10</code></pre></details></td>
    </tr>
    <tr>
      <td>4</td>
      <td>Math 04 Gcd Or Hcf<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/lcm-and-gcd4551/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: A = 4, B = 8, Output: 4</td>
      <td><details><summary><b>Approach 1</b></summary><b>Time:</b> O(min(a, b))<br><b>Space:</b> O(1)</details><details><summary><b>Approach 2</b></summary><b>Time:</b> O(log(min(a, b)))<br><b>Space:</b> O(1)</details></td>
      <td><details><summary><b>Approach 1</b></summary><b>Explanation:</b> Brute Force: Iterate from 1 to min(a, b) and find the highest number that divides both.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def gcd(a: int, b: int) -&gt; int:&#10;    ans = 1&#10;    for i in range(1, min(a, b) + 1):&#10;        if a % i == 0 and b % i == 0:&#10;            ans = i&#10;    return ans</code></pre></details></details><details><summary><b>Approach 2</b></summary><b>Explanation:</b> Euclidean Algorithm (Optimal): Repeatedly replace max(a,b) with max(a,b) % min(a,b). The final non-zero value is the GCD. Note: LCM can be found in O(1) extra time using formula: LCM(a,b) = (a*b) / GCD(a,b)<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def calcGCD(n: int, m: int) -&gt; int:&#10;    while n &gt; 0 and m &gt; 0:&#10;        if n &gt; m: n = n % m&#10;        else: m = m % n&#10;    return m if n == 0 else n&#10;&#10;    # LCM Calculation&#10;    # lcm = (n * m) // calcGCD(n, m)</code></pre></details></details></td>
    </tr>
    <tr>
      <td>5</td>
      <td>Math 05 Check For Prime<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/prime-number2314/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: N = 5, Output: 1</td>
      <td><details><summary><b>Approach 1</b></summary><b>Time:</b> O(N)<br><b>Space:</b> O(1)</details><details><summary><b>Approach 2</b></summary><b>Time:</b> O(sqrt(N))<br><b>Space:</b> O(1)</details></td>
      <td><details><summary><b>Approach 1</b></summary><b>Explanation:</b> Brute Force: Iterate from 2 to N-1 and check if N is divisible.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isPrime(N: int) -&gt; int:&#10;    if N &lt;= 1: return 0&#10;    for i in range(2, N):&#10;        if N % i == 0: return 0&#10;    return 1</code></pre></details></details><details><summary><b>Approach 2</b></summary><b>Explanation:</b> Optimal: Check divisibility up to sqrt(N). Factors appear in pairs.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isPrime(N: int) -&gt; int:&#10;    if N &lt;= 1: return 0&#10;    for i in range(2, int(N**0.5) + 1):&#10;        if N % i == 0: return 0&#10;    return 1</code></pre></details></details></td>
    </tr>
    <tr>
      <td>6</td>
      <td>Math 06 Power Of Two<br><br></b> <a href="https://leetcode.com/problems/power-of-two/" target="_blank">LeetCode 231</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> SDE Sheet, Love Babbar, Striver A Z</details></td>
      <td>**Example 1:** Bit Manipulation.</td>
      <td><b>Time:</b> O(1)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> If a number is a power of two, it has exactly one bit set in its binary representation. The expression `n & (n - 1)` clears the lowest set bit. Thus, if `n > 0` and `(n & (n - 1)) == 0`, it is a power of two.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isPowerOfTwo(n: int) -&gt; bool:&#10;    return n &gt; 0 and (n &amp; (n - 1)) == 0</code></pre></details></td>
    </tr>
    <tr>
      <td>7</td>
      <td>Math 07 Pow X N<br><br></b> <a href="https://leetcode.com/problems/powx-n/" target="_blank">LeetCode 50</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> SDE Sheet, Love Babbar, Striver A Z</details></td>
      <td>**Example 1:** Binary Exponentiation.</td>
      <td><details><summary><b>Approach 1</b></summary><b>Time:</b> O(N)<br><b>Space:</b> O(1)</details><details><summary><b>Approach 2</b></summary><b>Time:</b> O(log N)<br><b>Space:</b> O(1)</details></td>
      <td><details><summary><b>Approach 1</b></summary><b>Explanation:</b> Brute Force: Loop n times and multiply ans by x.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def myPow(x: float, n: int) -&gt; float:&#10;    ans = 1.0&#10;    nn = abs(n)&#10;    for _ in range(nn):&#10;        ans *= x&#10;    return 1.0 / ans if n &lt; 0 else ans</code></pre></details></details><details><summary><b>Approach 2</b></summary><b>Explanation:</b> Optimal: Binary Exponentiation. If n is even, x = x*x, n = n/2. If odd, ans = ans*x, n = n-1.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def myPow(x, n):&#10;    ans, nn = 1.0, abs(n)&#10;    while nn &gt; 0:&#10;        if nn % 2 == 1:&#10;            ans *= x&#10;            nn -= 1&#10;        else:&#10;            x *= x&#10;            nn //= 2&#10;    return ans if n &gt;= 0 else 1.0 / ans</code></pre></details></details></td>
    </tr>
    <tr>
      <td>8</td>
      <td>Bit 08 Swap Two Numbers<br><br></b> <a href="https://www.geeksforgeeks.org/problems/swap-two-numbers3844/1" target="_blank">GeeksforGeeks</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:**
Input: a=5, b=7
Output: a=7, b=5

**Note (Constraint):** 1 &le; a, b &le; 10<sup>9</sup></td>
      <td><details><summary><b>Approach 1</b></summary><b>Time:</b> O(1)<br><b>Space:</b> O(1)</details><details><summary><b>Approach 2</b></summary><b>Time:</b> O(1)<br><b>Space:</b> O(1)</details></td>
      <td><details><summary><b>Approach 1</b></summary><b>Explanation:</b> Use basic arithmetic (addition and subtraction) to swap.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def swap_arithmetic(a: int, b: int) -&gt; tuple:&#10;    a = a + b&#10;    b = a - b&#10;    a = a - b&#10;    return a, b</code></pre></details></details><details><summary><b>Approach 2</b></summary><b>Explanation:</b> Use XOR bitwise operation. XORing a number with itself is 0, and XORing with 0 is the number itself.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def get(a: int, b: int) -&gt; list:&#10;    a = a ^ b&#10;    b = a ^ b&#10;    a = a ^ b&#10;    return [a, b]</code></pre></details></details></td>
    </tr>
    <tr>
      <td>9</td>
      <td>Bit 09 Check Ith Bit Set<br><br></b> <a href="https://www.geeksforgeeks.org/problems/check-whether-k-th-bit-is-set-or-not-1587115620/1" target="_blank">GeeksforGeeks</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:**
Input: N=4 (100 in binary), i=2
Output: true

**Note (Constraint):** 1 &le; N &le; 10<sup>9</sup>, 0 &le; i &le; 31</td>
      <td><details><summary><b>Approach 1</b></summary><b>Time:</b> O(1)<br><b>Space:</b> O(1)</details><details><summary><b>Approach 2</b></summary><b>Time:</b> O(1)<br><b>Space:</b> O(1)</details></td>
      <td><details><summary><b>Approach 1</b></summary><b>Explanation:</b> Right shift N by K times and check if the least significant bit is 1.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def check_kth_bit_right_shift(n: int, k: int) -&gt; bool:&#10;    return ((n &gt;&gt; k) &amp; 1) != 0</code></pre></details></details><details><summary><b>Approach 2</b></summary><b>Explanation:</b> Create a mask by left shifting 1 by K times and check if the bitwise AND with N is non-zero.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def check_kth_bit(n: int, k: int) -&gt; bool:&#10;    return (n &amp; (1 &lt;&lt; k)) != 0</code></pre></details></details></td>
    </tr>
    <tr>
      <td>10</td>
      <td>Bit 10 Operations Set Clear Toggle<br><br></b> <a href="https://www.geeksforgeeks.org/problems/bit-manipulation-1666686020/1" target="_blank">GeeksforGeeks</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:**
N=70, i=3 -> Set:78, Clear:62, Toggle:78

**Note (Constraint):** 1 &le; N &le; 10<sup>9</sup></td>
      <td><b>Time:</b> O(1)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Use OR (`|`) to set, AND with NOT (`& ~`) to clear, and XOR (`^`) to toggle.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def bit_operations(n: int, i: int) -&gt; list:&#10;    set_bit = n | (1 &lt;&lt; i)&#10;    clear_bit = n &amp; ~(1 &lt;&lt; i)&#10;    toggle_bit = n ^ (1 &lt;&lt; i)&#10;    return [set_bit, clear_bit, toggle_bit]</code></pre></details></td>
    </tr>
    <tr>
      <td>11</td>
      <td>Bit 11 Count Set Bits<br><br></b> <a href="https://leetcode.com/problems/number-of-1-bits/" target="_blank">LeetCode 191</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:**
Input: N=11 (1011)
Output: 3</td>
      <td><details><summary><b>Approach 1</b></summary><b>Time:</b> O(32) &cong; O(1)<br><b>Space:</b> O(1)</details><details><summary><b>Approach 2</b></summary><b>Time:</b> O(Set Bits)<br><b>Space:</b> O(1)</details></td>
      <td><details><summary><b>Approach 1</b></summary><b>Explanation:</b> Iterate through all 32 bits and check if each is set by right shifting N and checking the 0th bit.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def hamming_weight_loop(n: int) -&gt; int:&#10;    count = 0&#10;    while n:&#10;        count += (n &amp; 1)&#10;        n &gt;&gt;= 1&#10;    return count</code></pre></details></details><details><summary><b>Approach 2</b></summary><b>Explanation:</b> Use Brian Kernighan's algorithm: `n = n & (n - 1)` unsets the rightmost set bit. Keep doing this until `n` becomes 0.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def hamming_weight(n: int) -&gt; int:&#10;    count = 0&#10;    while n:&#10;        n &amp;= (n - 1)&#10;        count += 1&#10;    return count</code></pre></details></details></td>
    </tr>
    <tr>
      <td>12</td>
      <td>Bit 12 Minimum Bit Flips To Convert Number<br><br></b> <a href="https://leetcode.com/problems/minimum-bit-flips-to-convert-number/" target="_blank">LeetCode 2220</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:**
Input: start=10 (1010), goal=7 (0111)
Output: 3 flips</td>
      <td><b>Time:</b> O(Set Bits)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> XOR `start` and `goal` to isolate differing bits, then count the set bits in the result.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def min_bit_flips(start: int, goal: int) -&gt; int:&#10;    xor_res = start ^ goal&#10;    count = 0&#10;    while xor_res &gt; 0:&#10;        xor_res &amp;= (xor_res - 1)&#10;        count += 1&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td>13</td>
      <td>Sw 13 Longest Substring Without Repeating Characters<br><br></b> <a href="https://leetcode.com/problems/longest-substring-without-repeating-characters/" target="_blank">LeetCode 3</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> SDE Sheet, Love Babbar, Striver A Z</details></td>
      <td>**Example 1:** Input: s = "abcabcbb", Output: 3 ("abc")</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(min(N, M))</td>
      <td><b>Explanation:</b> Sliding window with a Hash Map storing the latest index of each character. Move `left` pointer to `max(left, map[char] + 1)`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def lengthOfLongestSubstring(s: str) -&gt; int:&#10;    mpp = {}&#10;    left = max_len = 0&#10;    for right, char in enumerate(s):&#10;        if char in mpp:&#10;            left = max(left, mpp[char] + 1)&#10;        mpp[char] = right&#10;        max_len = max(max_len, right - left + 1)&#10;    return max_len</code></pre></details></td>
    </tr>
    <tr>
      <td>14</td>
      <td>Sw 14 Trapping Rain Water<br><br></b> <a href="https://leetcode.com/problems/trapping-rain-water/" target="_blank">LeetCode 42</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>**Example 1:** Input: height = [0,1,0,2,1,0,1,3,2,1,2,1], Output: 6</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Two pointers `left` and `right`. Maintain `left_max` and `right_max`. Move the pointer pointing to the smaller max, adding trapped water.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def trap(height: list[int]) -&gt; int:&#10;    left, right = 0, len(height) - 1&#10;    res, maxLeft, maxRight = 0, 0, 0&#10;    while left &lt;= right:&#10;        if height[left] &lt;= height[right]:&#10;            if height[left] &gt;= maxLeft: maxLeft = height[left]&#10;            else: res += maxLeft - height[left]&#10;            left += 1&#10;        else:&#10;            if height[right] &gt;= maxRight: maxRight = height[right]&#10;            else: res += maxRight - height[right]&#10;            right -= 1&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td>15</td>
      <td>Sw 15 Container With Most Water<br><br></b> <a href="https://leetcode.com/problems/container-with-most-water/" target="_blank">LeetCode 11</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, SDE Sheet</details></td>
      <td>**Example 1:** Input: height = [1,8,6,2,5,4,8,3,7], Output: 49</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Two Pointers from ends. Area is `min(h[left], h[right]) * width`. Move the pointer with the smaller height to seek a potentially taller line.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxArea(height: list[int]) -&gt; int:&#10;    left, right = 0, len(height) - 1&#10;    max_area = 0&#10;    while left &lt; right:&#10;        area = min(height[left], height[right]) * (right - left)&#10;        max_area = max(max_area, area)&#10;        if height[left] &lt; height[right]:&#10;            left += 1&#10;        else:&#10;            right -= 1&#10;    return max_area</code></pre></details></td>
    </tr>
    <tr>
      <td>16</td>
      <td>Sort 16 Selection Sort<br><br></b> <a href="https://www.geeksforgeeks.org/problems/selection-sort/1" target="_blank">GeeksforGeeks</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>N/A</td>
      <td><b>Time:</b> O(N<sup>2</sup>) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><b>Explanation:</b> Find the minimum element in the unsorted array and swap it with the element at the beginning.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def selection_sort(arr: list[int]) -&gt; None:&#10;    n = len(arr)&#10;    for i in range(n - 1):&#10;        min_idx = i&#10;        for j in range(i + 1, n):&#10;            if arr[j] &lt; arr[min_idx]:&#10;                min_idx = j&#10;        arr[i], arr[min_idx] = arr[min_idx], arr[i]</code></pre></details></td>
    </tr>
    <tr>
      <td>17</td>
      <td>Sort 17 Bubble Sort<br><br></b> <a href="https://www.geeksforgeeks.org/problems/bubble-sort/1" target="_blank">GeeksforGeeks</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>N/A</td>
      <td><b>Time:</b> O(N<sup>2</sup>) (Trade-off)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Repeatedly swap adjacent elements if they are in the wrong order. Push the maximum element to the end.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def bubble_sort(arr: list[int]) -&gt; None:&#10;    n = len(arr)&#10;    for i in range(n - 1, -1, -1):&#10;        did_swap = False&#10;        for j in range(i):&#10;            if arr[j] &gt; arr[j + 1]:&#10;                arr[j], arr[j + 1] = arr[j + 1], arr[j]&#10;                did_swap = True&#10;        if not did_swap: break</code></pre></details></td>
    </tr>
    <tr>
      <td>18</td>
      <td>Sort 18 Insertion Sort<br><br></b> <a href="https://www.geeksforgeeks.org/problems/insertion-sort/1" target="_blank">GeeksforGeeks</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>N/A</td>
      <td><b>Time:</b> O(N<sup>2</sup>) (Constraint)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Takes an element and places it in its correct position within the previously sorted part of the array.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def insertion_sort(arr: list[int]) -&gt; None:&#10;    n = len(arr)&#10;    for i in range(n):&#10;        j = i&#10;        while j &gt; 0 and arr[j - 1] &gt; arr[j]:&#10;            arr[j - 1], arr[j] = arr[j], arr[j - 1]&#10;            j -= 1</code></pre></details></td>
    </tr>
    <tr>
      <td>19</td>
      <td>Sort 19 Merge Sort<br><br></b> <a href="https://www.geeksforgeeks.org/problems/merge-sort/1" target="_blank">GeeksforGeeks</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>N/A</td>
      <td><b>Time:</b> O(N log N) (Constraint)<br><b>Space:</b> O(N) (Trade-off)</td>
      <td><b>Explanation:</b> Recursively split array in half, sort them, and merge the sorted halves.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def merge_sort(arr: list[int]) -&gt; None:&#10;    def merge(low, mid, high):&#10;        temp = []&#10;        left, right = low, mid + 1&#10;        while left &lt;= mid and right &lt;= high:&#10;            if arr[left] &lt;= arr[right]:&#10;                temp.append(arr[left])&#10;                left += 1&#10;            else:&#10;                temp.append(arr[right])&#10;                right += 1&#10;        while left &lt;= mid:&#10;            temp.append(arr[left]); left += 1&#10;        while right &lt;= high:&#10;            temp.append(arr[right]); right += 1&#10;        for i in range(len(temp)):&#10;            arr[low + i] = temp[i]&#10;            &#10;    def helper(low, high):&#10;        if low &gt;= high: return&#10;        mid = (low + high) // 2&#10;        helper(low, mid)&#10;        helper(mid + 1, high)&#10;        merge(low, mid, high)&#10;        &#10;    helper(0, len(arr) - 1)</code></pre></details></td>
    </tr>
    <tr>
      <td>20</td>
      <td>Sort 20 Quick Sort<br><br></b> <a href="https://www.geeksforgeeks.org/problems/quick-sort/1" target="_blank">GeeksforGeeks</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td>N/A</td>
      <td><b>Time:</b> O(N log N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><b>Explanation:</b> Pick a pivot. Place smaller elements left and larger right. Recursively sort partitions.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def quick_sort(arr: list[int]) -&gt; None:&#10;    def partition(low, high):&#10;        pivot = arr[low]&#10;        i, j = low, high&#10;        while i &lt; j:&#10;            while i &lt;= high - 1 and arr[i] &lt;= pivot: i += 1&#10;            while j &gt;= low + 1 and arr[j] &gt; pivot: j -= 1&#10;            if i &lt; j: arr[i], arr[j] = arr[j], arr[i]&#10;        arr[low], arr[j] = arr[j], arr[low]&#10;        return j&#10;        &#10;    def helper(low, high):&#10;        if low &lt; high:&#10;            p_idx = partition(low, high)&#10;            helper(low, p_idx - 1)&#10;            helper(p_idx + 1, high)&#10;            &#10;    helper(0, len(arr) - 1)</code></pre></details></td>
    </tr>
  </tbody>
</table>
