# Day 30 Misc Revision Table

<table border="1">
  <thead>
    <tr>
      <th style="width: 5%;">S.No</th>
      <th style="width: 15%;">Problem Name</th>
      <th style="width: 20%;">Example & Constraints</th>
      <th style="width: 10%;">Complexity</th>
      <th style="width: 20%;">Approach & Dependencies</th>
      <th style="width: 30%;">Logic & Edge Cases</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">1</td>
      <td rowspan="3">Math 01 Count Digits<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/count-digits5716/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td rowspan="3"><b>Example 1:</b> <br><b>Input:</b> N = 12345<br><b>Output:</b> 5</td>
      <td><b>Time:</b> O(log<sub>10</sub> N)<br><b>Space:</b> O(log<sub>10</sub> N)</td>
      <td><b>Approach 1:</b><br>Convert the absolute value of the number to a string and return its length.<br><br><b>Dependencies:</b> <code>#include &lt;string&gt;</code>
<code>#include &lt;cmath&gt;</code></td>
      <td><b>Edge Cases:</b> <b>Negative Numbers:</b> Use abs(n) to avoid counting the minus sign.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def countDigits(n: int) -&gt; int:&#10;    return len(str(abs(n)))</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(log<sub>10</sub> N)<br><b>Space:</b> O(1)</td>
      <td><b>Approach 2:</b><br>Use a while loop to repeatedly divide the number by 10 and increment a counter.</td>
      <td><b>Edge Cases:</b> <b>Zero Case:</b> Handle 0 explicitly.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def countDigits(n: int) -&gt; int:&#10;    if n == 0: return 1&#10;    count = 0&#10;    # Use int(n/10) to truncate toward zero in Python&#10;    while n != 0:&#10;        count += 1&#10;        n = int(n / 10)&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(log<sub>10</sub> N)<br><b>Space:</b> O(1)</td>
      <td><b>Approach 3:</b><br>Use the base-10 logarithm function to find the number of digits mathematically.<br><br><b>Dependencies:</b> <code>#include &lt;cmath&gt;</code></td>
      <td><b>Edge Cases:</b> <b>Zero Case:</b> Handle 0 explicitly since log10(0) is undefined.<br><b>Negative Numbers:</b> Use abs(n) before logarithm.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import math&#10;def countDigits(n: int) -&gt; int:&#10;    if n == 0: return 1&#10;    return int(math.log10(abs(n)) + 1)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">2</td>
      <td rowspan="2">Math 02 Reverse Integer<br><br></b> <a href="https://leetcode.com/problems/reverse-integer/" target="_blank">LeetCode 7</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td rowspan="2"><b>Example 1:</b> <br><b>Input:</b> x = 123<br><b>Output:</b> 321</td>
      <td><b>Time:</b> O(log<sub>10</sub> x)<br><b>Space:</b> O(1)</td>
      <td><b>Approach 1:</b><br>Optimal Approach: Use a 64-bit integer to naturally store the reversed number. A variant note explains how to do this strictly with 32-bit integers if long is not allowed.<br><br><b>Dependencies:</b> <code>#include &lt;limits.h&gt;</code></td>
      <td><b>Edge Cases:</b> <b>Overflow:</b> Checked using 64-bit bounds or 32-bit variants.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def reverse(x: int) -&gt; int:&#10;    ans = 0&#10;    sign = -1 if x &lt; 0 else 1&#10;    x = abs(x)&#10;    while x != 0:&#10;        digit = x % 10&#10;        ans = ans * 10 + digit&#10;        x //= 10&#10;    ans *= sign&#10;    if ans &gt; 2**31 - 1 or ans &lt; -2**31:&#10;        return 0&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(log<sub>10</sub> x)<br><b>Space:</b> O(log<sub>10</sub> x)</td>
      <td><b>Approach 2:</b><br>Brute Force / String Approach: Convert to string, reverse, and then parse back to integer.<br><br><b>Dependencies:</b> <code>#include &lt;string&gt;</code>
<code>#include &lt;algorithm&gt;</code></td>
      <td><b>Edge Cases:</b> <b>Overflow:</b> Must be caught via exception handling (stoll).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def reverse(x: int) -&gt; int:&#10;    sign = [1, -1][x &lt; 0]&#10;    ans = int(str(abs(x))[::-1])&#10;    return sign * ans if ans &lt;= 2**31 - 1 else 0</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">3</td>
      <td rowspan="1">Math 03 Palindrome Number<br><br></b> <a href="https://leetcode.com/problems/palindrome-number/" target="_blank">LeetCode 9</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> x = 121<br><b>Output:</b> true</td>
      <td><b>Time:</b> O(log<sub>10</sub> x)<br><b>Space:</b> O(1)</td>
      <td>Negative numbers are false. Reverse half the number. If original equals reversed, it is a palindrome.</td>
      <td><b>Edge Cases:</b> <b>Negative Numbers:</b> Instant false. Trailing zeroes instant false.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isPalindrome(x: int) -&gt; bool:&#10;    if x &lt; 0 or (x % 10 == 0 and x != 0): return False&#10;    rev = 0&#10;    while x &gt; rev:&#10;        rev = rev * 10 + x % 10&#10;        x //= 10&#10;    return x == rev or x == rev // 10</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">4</td>
      <td rowspan="2">Math 04 Gcd Or Hcf<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/lcm-and-gcd4551/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td rowspan="2"><b>Example 1:</b> <br><b>Input:</b> A = 4, B = 8<br><b>Output:</b> 4</td>
      <td><b>Time:</b> O(min(a, b))<br><b>Space:</b> O(1)</td>
      <td><b>Approach 1:</b><br>Brute Force: Iterate from 1 to min(a, b) and find the highest number that divides both.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def lcmAndGcd(a: int, b: int) -&gt; list[int]:&#10;    gcd = 1&#10;    for i in range(1, min(a, b) + 1):&#10;        if a % i == 0 and b % i == 0:&#10;            gcd = i&#10;    lcm = (a // gcd) * b  # Divide first to prevent overflow&#10;    return [lcm, gcd]</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(log(min(a, b)))<br><b>Space:</b> O(1)</td>
      <td><b>Approach 2:</b><br>Euclidean Algorithm (Optimal): Repeatedly replace max(a,b) with max(a,b) % min(a,b). The final non-zero value is the GCD. Note: LCM can be found in O(1) extra time using formula: LCM(a,b) = (a*b) / GCD(a,b)<br><br><b>Dependencies:</b> <code>#include &lt;algorithm&gt;</code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def lcmAndGcd(a: int, b: int) -&gt; list[int]:&#10;    original_a, original_b = a, b&#10;    while a &gt; 0 and b &gt; 0:&#10;        if a &gt; b:&#10;            a = a % b&#10;        else:&#10;            b = b % a&#10;    # m if n == 0 else n can be replaced by a + b since one is 0&#10;    gcd = a + b&#10;    lcm = (original_a // gcd) * original_b  # Divide first to prevent overflow&#10;    return [lcm, gcd]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">5</td>
      <td rowspan="1">Math 05 Check For Prime<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/prime-number2314/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> N = 5<br><b>Output:</b> 1</td>
      <td><b>Time:</b> O(sqrt(N))<br><b>Space:</b> O(1)</td>
      <td>Check divisibility up to sqrt(N). Iterating up to N (O(N) time) is unnecessary and inefficient since factors always appear in pairs.</td>
      <td><b>Edge Cases:</b> <b>N=1:</b> Not prime.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isPrime(N: int) -&gt; int:&#10;    if N &lt;= 1: return 0&#10;    for i in range(2, int(N**0.5) + 1):&#10;        if N % i == 0: return 0&#10;    return 1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">6</td>
      <td rowspan="1">Math 06 Power Of Two<br><br></b> <a href="https://leetcode.com/problems/power-of-two/" target="_blank">LeetCode 231</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, SDE Sheet, Love Babbar</details></td>
      <td rowspan="1"><b>Example 1:</b> Bit Manipulation.</td>
      <td><b>Time:</b> O(1)<br><b>Space:</b> O(1)</td>
      <td>If a number is a power of two, it has exactly one bit set in its binary representation. The expression `n & (n - 1)` clears the lowest set bit. Thus, if `n > 0` and `(n & (n - 1)) == 0`, it is a power of two.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isPowerOfTwo(n: int) -&gt; bool:&#10;    return n &gt; 0 and (n &amp; (n - 1)) == 0</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">7</td>
      <td rowspan="2">Math 07 Pow X N<br><br></b> <a href="https://leetcode.com/problems/powx-n/" target="_blank">LeetCode 50</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, SDE Sheet, Love Babbar</details></td>
      <td rowspan="2"><b>Example 1:</b> Binary Exponentiation.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Approach 1:</b><br>Brute Force: Loop n times and multiply ans by x.</td>
      <td><b>Edge Cases:</b> TLE for large N.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def myPow(x: float, n: int) -&gt; float:&#10;    ans = 1.0&#10;    nn = abs(n)&#10;    for _ in range(nn):&#10;        ans *= x&#10;    return 1.0 / ans if n &lt; 0 else ans</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(log N)<br><b>Space:</b> O(1)</td>
      <td><b>Approach 2:</b><br>Optimal: Binary Exponentiation. If n is even, x = x*x, n = n/2. If odd, ans = ans*x, n = n-1.</td>
      <td><b>Edge Cases:</b> Negative power, n = INT_MIN<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def myPow(x, n):&#10;    ans, nn = 1.0, abs(n)&#10;    while nn &gt; 0:&#10;        if nn % 2 == 1:&#10;            ans *= x&#10;            nn -= 1&#10;        else:&#10;            x *= x&#10;            nn //= 2&#10;    return ans if n &gt;= 0 else 1.0 / ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">8</td>
      <td rowspan="2">Bit 08 Swap Two Numbers<br><br></b> <a href="https://www.geeksforgeeks.org/problems/swap-two-numbers3844/1" target="_blank">GeeksforGeeks</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td rowspan="2"><b> </b><br><br><b>Input:</b> a=5, b=7<br><b>Output:</b> a=7, b=5<br><br><b> </b> 1 &le; a, b &le; 10<sup>9</sup></td>
      <td><b>Time:</b> O(1)<br><b>Space:</b> O(1)</td>
      <td><b>Approach 1:</b><br>Use basic arithmetic (addition and subtraction) to swap.</td>
      <td><b>Edge Cases:</b> **Integer Overflow:** Addition `a + b` can overflow if numbers are near `INT_MAX`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def swap_arithmetic(a: int, b: int) -&gt; tuple:&#10;    a = a + b&#10;    b = a - b&#10;    a = a - b&#10;    return a, b</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(1)<br><b>Space:</b> O(1)</td>
      <td><b>Approach 2:</b><br>Use XOR bitwise operation. XORing a number with itself is 0, and XORing with 0 is the number itself.</td>
      <td><b>Edge Cases:</b> **Optimal:** No overflow risk compared to arithmetic addition.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def get(a: int, b: int) -&gt; list:&#10;    a = a ^ b&#10;    b = a ^ b&#10;    a = a ^ b&#10;    return [a, b]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">9</td>
      <td rowspan="2">Bit 09 Check Ith Bit Set<br><br></b> <a href="https://www.geeksforgeeks.org/problems/check-whether-k-th-bit-is-set-or-not-1587115620/1" target="_blank">GeeksforGeeks</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td rowspan="2"><b> </b><br><br><b>Input:</b> N=4 (100 in binary), i=2<br><b>Output:</b> true<br><br><b> </b> 1 &le; N &le; 10<sup>9</sup>, 0 &le; i &le; 31</td>
      <td><b>Time:</b> O(1)<br><b>Space:</b> O(1)</td>
      <td><b>Approach 1:</b><br>Right shift N by K times and check if the least significant bit is 1.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def check_kth_bit_right_shift(n: int, k: int) -&gt; bool:&#10;    return ((n &gt;&gt; k) &amp; 1) != 0</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(1)<br><b>Space:</b> O(1)</td>
      <td><b>Approach 2:</b><br>Create a mask by left shifting 1 by K times and check if the bitwise AND with N is non-zero.</td>
      <td><b>Edge Cases:</b> **Shift Overflow:** Use `1LL` if K can exceed 31.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def check_kth_bit(n: int, k: int) -&gt; bool:&#10;    return (n &amp; (1 &lt;&lt; k)) != 0</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">10</td>
      <td rowspan="1">Bit 10 Operations Set Clear Toggle<br><br></b> <a href="https://www.geeksforgeeks.org/problems/bit-manipulation-1666686020/1" target="_blank">GeeksforGeeks</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td rowspan="1"><b> </b><br>N=70, i=3 -> Set:78, Clear:62, Toggle:78<br><br><b> </b> 1 &le; N &le; 10<sup>9</sup></td>
      <td><b>Time:</b> O(1)<br><b>Space:</b> O(1)</td>
      <td>Use OR (`|`) to set, AND with NOT (`& ~`) to clear, and XOR (`^`) to toggle.</td>
      <td><b>Edge Cases:</b> **Shift Overflow:** `1LL` used strictly to prevent overflow beyond 31 bits.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def bit_operations(n: int, i: int) -&gt; list:&#10;    set_bit = n | (1 &lt;&lt; i)&#10;    clear_bit = n &amp; ~(1 &lt;&lt; i)&#10;    toggle_bit = n ^ (1 &lt;&lt; i)&#10;    return [set_bit, clear_bit, toggle_bit]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">11</td>
      <td rowspan="2">Bit 11 Count Set Bits<br><br></b> <a href="https://leetcode.com/problems/number-of-1-bits/" target="_blank">LeetCode 191</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td rowspan="2"><b> </b><br><br><b>Input:</b> N=11 (1011)<br><b>Output:</b> 3</td>
      <td><b>Time:</b> O(32) &cong; O(1)<br><b>Space:</b> O(1)</td>
      <td><b>Approach 1:</b><br>Iterate through all 32 bits and check if each is set by right shifting N and checking the 0th bit.</td>
      <td><b>Edge Cases:</b> **Static Loop Iterations:** Loop always runs 32 times regardless of number size.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def hamming_weight_loop(n: int) -&gt; int:&#10;    count = 0&#10;    while n:&#10;        count += (n &amp; 1)&#10;        n &gt;&gt;= 1&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(Set Bits)<br><b>Space:</b> O(1)</td>
      <td><b>Approach 2:</b><br>Use Brian Kernighan's algorithm: `n = n & (n - 1)` unsets the rightmost set bit. Keep doing this until `n` becomes 0.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def hamming_weight(n: int) -&gt; int:&#10;    count = 0&#10;    while n:&#10;        n &amp;= (n - 1)&#10;        count += 1&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">12</td>
      <td rowspan="1">Bit 12 Minimum Bit Flips To Convert Number<br><br></b> <a href="https://leetcode.com/problems/minimum-bit-flips-to-convert-number/" target="_blank">LeetCode 2220</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td rowspan="1"><b> </b><br><br><b>Input:</b> start=10 (1010), goal=7 (0111)<br><b>Output:</b> 3 flips</td>
      <td><b>Time:</b> O(Set Bits)<br><b>Space:</b> O(1)</td>
      <td>XOR `start` and `goal` to isolate differing bits, then count the set bits in the result.</td>
      <td><b>Edge Cases:</b> **XOR Magic:** XOR inherently maps identical bits to 0 and different bits to 1, instantly mapping the problem to Hamming Weight.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def min_bit_flips(start: int, goal: int) -&gt; int:&#10;    xor_res = start ^ goal&#10;    count = 0&#10;    while xor_res &gt; 0:&#10;        xor_res &amp;= (xor_res - 1)&#10;        count += 1&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">13</td>
      <td rowspan="1">Sw 13 Longest Substring Without Repeating Characters<br><br></b> <a href="https://leetcode.com/problems/longest-substring-without-repeating-characters/" target="_blank">LeetCode 3</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> SDE Sheet, Love Babbar, Striver A Z</details></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> s = "abcabcbb"<br><b>Output:</b> 3 ("abc")</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(min(N, M))</td>
      <td>Sliding window with a Hash Map storing the latest index of each character. Move `left` pointer to `max(left, map[char] + 1)`.<br><br><b>Dependencies:</b> <code>std::vector</code> for frequency array</td>
      <td><b>Edge Cases:</b> <b>Pointer Leap:</b> `left` can only jump forward, thus `std::max(left, ...)` prevents `left` from going backward if an old duplicate is found.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def lengthOfLongestSubstring(s: str) -&gt; int:&#10;    mpp = {}&#10;    left = max_len = 0&#10;    for right, char in enumerate(s):&#10;        if char in mpp:&#10;            left = max(left, mpp[char] + 1)&#10;        mpp[char] = right&#10;        max_len = max(max_len, right - left + 1)&#10;    return max_len</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">14</td>
      <td rowspan="1">Sw 14 Trapping Rain Water<br><br></b> <a href="https://leetcode.com/problems/trapping-rain-water/" target="_blank">LeetCode 42</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> height = [0,1,0,2,1,0,1,3,2,1,2,1]<br><b>Output:</b> 6</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Two pointers `left` and `right`. Maintain `left_max` and `right_max`. Move the pointer pointing to the smaller max, adding trapped water.</td>
      <td><b>Edge Cases:</b> <b>Local Maxima:</b> Water trapped at `i` relies on the absolute minimum of the highest bars to its left and right.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def trap(height: list[int]) -&gt; int:&#10;    left, right = 0, len(height) - 1&#10;    res, maxLeft, maxRight = 0, 0, 0&#10;    while left &lt;= right:&#10;        if height[left] &lt;= height[right]:&#10;            if height[left] &gt;= maxLeft: maxLeft = height[left]&#10;            else: res += maxLeft - height[left]&#10;            left += 1&#10;        else:&#10;            if height[right] &gt;= maxRight: maxRight = height[right]&#10;            else: res += maxRight - height[right]&#10;            right -= 1&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">15</td>
      <td rowspan="1">Sw 15 Container With Most Water<br><br></b> <a href="https://leetcode.com/problems/container-with-most-water/" target="_blank">LeetCode 11</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, SDE Sheet</details></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> height = [1,8,6,2,5,4,8,3,7]<br><b>Output:</b> 49</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Two Pointers from ends. Area is `min(h[left], h[right]) * width`. Move the pointer with the smaller height to seek a potentially taller line.<br><br><b>Dependencies:</b> <code>std::max</code>, <code>std::min</code></td>
      <td><b>Edge Cases:</b> <b>Width vs Height Tradeoff:</b> By starting at maximum width, we only decrease width. Thus, we must only abandon a height if we hope to find a taller one.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxArea(height: list[int]) -&gt; int:&#10;    left, right = 0, len(height) - 1&#10;    max_area = 0&#10;    while left &lt; right:&#10;        area = min(height[left], height[right]) * (right - left)&#10;        max_area = max(max_area, area)&#10;        if height[left] &lt; height[right]:&#10;            left += 1&#10;        else:&#10;            right -= 1&#10;    return max_area</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">16</td>
      <td rowspan="1">Sort 16 Selection Sort<br><br></b> <a href="https://www.geeksforgeeks.org/problems/selection-sort/1" target="_blank">GeeksforGeeks</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> N = 5, arr[] = {4, 1, 3, 9, 7}<br><b>Output:</b> 1 3 4 7 9<br><br><b> </b> In-place sorting.</td>
      <td><b>Time:</b> O(N<sup>2</sup>) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td>Find the minimum element in the unsorted array and swap it with the element at the beginning.<br><br><b>Dependencies:</b> <code>std::swap</code></td>
      <td><b>Edge Cases:</b> <b>Worst Case:</b> Always `O(N^2)` even if the array is already sorted.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def selection_sort(arr: list[int]) -&gt; None:&#10;    n = len(arr)&#10;    for i in range(n - 1):&#10;        min_idx = i&#10;        for j in range(i + 1, n):&#10;            if arr[j] &lt; arr[min_idx]:&#10;                min_idx = j&#10;        arr[i], arr[min_idx] = arr[min_idx], arr[i]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">17</td>
      <td rowspan="1">Sort 17 Bubble Sort<br><br></b> <a href="https://www.geeksforgeeks.org/problems/bubble-sort/1" target="_blank">GeeksforGeeks</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> N = 5, arr[] = {4, 1, 3, 9, 7}<br><b>Output:</b> 1 3 4 7 9</td>
      <td><b>Time:</b> O(N<sup>2</sup>) (Trade-off)<br><b>Space:</b> O(1)</td>
      <td>Repeatedly swap adjacent elements if they are in the wrong order. Push the maximum element to the end.</td>
      <td><b>Edge Cases:</b> <b>Best Case Check:</b> Adding `did_swap` flag makes Best Case time `O(N)` for already sorted arrays.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def bubble_sort(arr: list[int]) -&gt; None:&#10;    n = len(arr)&#10;    for i in range(n - 1, -1, -1):&#10;        did_swap = False&#10;        for j in range(i):&#10;            if arr[j] &gt; arr[j + 1]:&#10;                arr[j], arr[j + 1] = arr[j + 1], arr[j]&#10;                did_swap = True&#10;        if not did_swap: break</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">18</td>
      <td rowspan="1">Sort 18 Insertion Sort<br><br></b> <a href="https://www.geeksforgeeks.org/problems/insertion-sort/1" target="_blank">GeeksforGeeks</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> N = 5, arr[] = {4, 1, 3, 9, 7}<br><b>Output:</b> 1 3 4 7 9</td>
      <td><b>Time:</b> O(N<sup>2</sup>) (Constraint)<br><b>Space:</b> O(1)</td>
      <td>Takes an element and places it in its correct position within the previously sorted part of the array.</td>
      <td><b>Edge Cases:</b> <b>Online Algorithm:</b> Good for data coming in one by one. `O(N)` best case time.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def insertion_sort(arr: list[int]) -&gt; None:&#10;    n = len(arr)&#10;    for i in range(n):&#10;        j = i&#10;        while j &gt; 0 and arr[j - 1] &gt; arr[j]:&#10;            arr[j - 1], arr[j] = arr[j], arr[j - 1]&#10;            j -= 1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">19</td>
      <td rowspan="1">Sort 19 Merge Sort<br><br></b> <a href="https://www.geeksforgeeks.org/problems/merge-sort/1" target="_blank">GeeksforGeeks</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> N = 5, arr[] = {4, 1, 3, 9, 7}<br><b>Output:</b> 1 3 4 7 9</td>
      <td><b>Time:</b> O(N log N) (Constraint)<br><b>Space:</b> O(N) (Trade-off)</td>
      <td>Recursively split array in half, sort them, and merge the sorted halves.<br><br><b>Dependencies:</b> Extra array for merging</td>
      <td><b>Edge Cases:</b> <b>Stable Sort:</b> Maintains relative order of equal elements. Requires `O(N)` extra space to merge.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def merge_sort(arr: list[int]) -&gt; None:&#10;    def merge(low, mid, high):&#10;        temp = []&#10;        left, right = low, mid + 1&#10;        while left &lt;= mid and right &lt;= high:&#10;            if arr[left] &lt;= arr[right]:&#10;                temp.append(arr[left])&#10;                left += 1&#10;            else:&#10;                temp.append(arr[right])&#10;                right += 1&#10;        while left &lt;= mid:&#10;            temp.append(arr[left]); left += 1&#10;        while right &lt;= high:&#10;            temp.append(arr[right]); right += 1&#10;        for i in range(len(temp)):&#10;            arr[low + i] = temp[i]&#10;            &#10;    def helper(low, high):&#10;        if low &gt;= high: return&#10;        mid = (low + high) // 2&#10;        helper(low, mid)&#10;        helper(mid + 1, high)&#10;        merge(low, mid, high)&#10;        &#10;    helper(0, len(arr) - 1)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">20</td>
      <td rowspan="1">Sort 20 Quick Sort<br><br></b> <a href="https://www.geeksforgeeks.org/problems/quick-sort/1" target="_blank">GeeksforGeeks</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> N = 5, arr[] = {4, 1, 3, 9, 7}<br><b>Output:</b> 1 3 4 7 9</td>
      <td><b>Time:</b> O(N log N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td>Pick a pivot. Place smaller elements left and larger right. Recursively sort partitions.</td>
      <td><b>Edge Cases:</b> <b>Worst Case:</b> `O(N^2)` if array is already sorted and pivot is extreme. Avoided by randomized pivot.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def quick_sort(arr: list[int]) -&gt; None:&#10;    def partition(low, high):&#10;        pivot = arr[low]&#10;        i, j = low, high&#10;        while i &lt; j:&#10;            while i &lt;= high - 1 and arr[i] &lt;= pivot: i += 1&#10;            while j &gt;= low + 1 and arr[j] &gt; pivot: j -= 1&#10;            if i &lt; j: arr[i], arr[j] = arr[j], arr[i]&#10;        arr[low], arr[j] = arr[j], arr[low]&#10;        return j&#10;        &#10;    def helper(low, high):&#10;        if low &lt; high:&#10;            p_idx = partition(low, high)&#10;            helper(low, p_idx - 1)&#10;            helper(p_idx + 1, high)&#10;            &#10;    helper(0, len(arr) - 1)</code></pre></details></td>
    </tr>
  </tbody>
</table>
