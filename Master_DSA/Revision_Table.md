# Master DSA Master Revision Table

## Basic Maths

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
      <td rowspan="3">Math 01 Count Digits<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/count-digits5716/1" target="_blank">GFG</a></td>
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
      <td rowspan="2">Math 02 Reverse Integer<br><br></b> <a href="https://leetcode.com/problems/reverse-integer/" target="_blank">LeetCode 7</a></td>
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
      <td rowspan="1">Math 03 Palindrome Number<br><br></b> <a href="https://leetcode.com/problems/palindrome-number/" target="_blank">LeetCode 9</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> x = 121<br><b>Output:</b> true</td>
      <td><b>Time:</b> O(log<sub>10</sub> x)<br><b>Space:</b> O(1)</td>
      <td>Negative numbers are false. Reverse half the number. If original equals reversed, it is a palindrome.</td>
      <td><b>Edge Cases:</b> <b>Negative Numbers:</b> Instant false. Trailing zeroes instant false.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isPalindrome(x: int) -&gt; bool:&#10;    if x &lt; 0 or (x % 10 == 0 and x != 0): return False&#10;    rev = 0&#10;    while x &gt; rev:&#10;        rev = rev * 10 + x % 10&#10;        x //= 10&#10;    return x == rev or x == rev // 10</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">4</td>
      <td rowspan="2">Math 04 Gcd Or Hcf<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/lcm-and-gcd4551/1" target="_blank">GFG</a></td>
      <td rowspan="2"><b>Example 1:</b> <br><b>Input:</b> A = 4, B = 8<br><b>Output:</b> 4</td>
      <td><b>Time:</b> O(min(a, b))<br><b>Space:</b> O(1)</td>
      <td><b>Approach 1:</b><br>Brute Force: Iterate from 1 to min(a, b) and find the highest number that divides both.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def lcmAndGcd(a: int, b: int) -&gt; list[int]:&#10;    gcd = 1&#10;    for i in range(1, min(a, b) + 1):&#10;        if a % i == 0 and b % i == 0:&#10;            gcd = i&#10;    lcm = (a // gcd) * b  # Divide first to prevent overflow&#10;    return [lcm, gcd]</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(log(min(a, b)))<br><b>Space:</b> O(1)</td>
      <td><b>Approach 2:</b><br>Euclidean Algorithm (Optimal): Repeatedly replace max(a,b) with max(a,b) % min(a,b). The final non-zero value is the GCD. Note: LCM can be found in O(1) extra time using formula: LCM(a,b) = (a*b) / GCD(a,b)<br><br><b>Dependencies:</b> <code>#include &lt;algorithm&gt;</code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def lcmAndGcd(a: int, b: int) -&gt; list[int]:&#10;    original_a, original_b = a, b&#10;    while a &gt; 0 and b &gt; 0:&#10;        if a &gt; b:&#10;            a = a % b&#10;        else:&#10;            b = b % a&#10;    # The non-zero value is the GCD. Since one of them is 0, we can just return a + b&#10;    gcd = a + b&#10;    lcm = (original_a // gcd) * original_b  # Divide first to prevent overflow&#10;    return [lcm, gcd]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">5</td>
      <td rowspan="1">Math 05 Check For Prime<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/prime-number2314/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> N = 5<br><b>Output:</b> 1</td>
      <td><b>Time:</b> O(sqrt(N))<br><b>Space:</b> O(1)</td>
      <td>Check divisibility up to sqrt(N). Iterating up to N (O(N) time) is unnecessary and inefficient since factors always appear in pairs.</td>
      <td><b>Edge Cases:</b> <b>N=1:</b> Not prime.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isPrime(N: int) -&gt; int:&#10;    if N &lt;= 1: return 0&#10;    for i in range(2, int(N**0.5) + 1):&#10;        if N % i == 0: return 0&#10;    return 1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">6</td>
      <td rowspan="1">Math 06 Factorial Trailing Zeroes<br><br></b> <a href="https://leetcode.com/problems/factorial-trailing-zeroes/" target="_blank">LeetCode 172</a><br><br><details><summary>ℹ️ Concept / Details</summary>A trailing zero is produced by a factor of 10. Since 10 = 2 * 5, and 2s are more abundant than 5s in factorials, we only need to count the number of 5s.</details></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> n = 5<br><b>Output:</b> 1</td>
      <td><b>Time:</b> O(log_5(N))<br><b>Space:</b> O(1)</td>
      <td>Trailing zeroes are produced by 10s, which are pairs of 2 and 5. Since 2s are more frequent, we just count the number of 5s in prime factors of numbers up to N. This is `N/5 + N/25 + N/125 + ...`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def trailingZeroes(n: int) -&gt; int:&#10;    count = 0&#10;    while n &gt; 0:&#10;        count += n // 5&#10;        n //= 5&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">7</td>
      <td rowspan="1">Math 07 Count Primes<br><br></b> <a href="https://leetcode.com/problems/count-primes/" target="_blank">LeetCode 204</a><br><br><details><summary>ℹ️ Concept / Details</summary><b>Sieve of Eratosthenes:</b> An ancient algorithm for finding all prime numbers up to any given limit. It iteratively marks as composite (i.e., not prime) the multiples of each prime.</details></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> n = 10<br><b>Output:</b> 4</td>
      <td><b>Time:</b> O(N log(log N))<br><b>Space:</b> O(N)</td>
      <td>Use the Sieve of Eratosthenes. Initialize a boolean array of size `n` with `true`. Mark `0` and `1` as `false`. For each `i` from `2` to `sqrt(n)`, if `i` is prime, mark its multiples as `false` starting from `i*i`. Finally, count the number of `true`s.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def countPrimes(n: int) -&gt; int:&#10;    if n &lt;= 2: return 0&#10;    isPrime = [True] * n&#10;    isPrime[0] = isPrime[1] = False&#10;    for i in range(2, int(n ** 0.5) + 1):&#10;        if isPrime[i]:&#10;            for j in range(i * i, n, i):&#10;                isPrime[j] = False&#10;    return sum(isPrime)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">8</td>
      <td rowspan="1">Math 08 Valid Perfect Square<br><br></b> <a href="https://leetcode.com/problems/valid-perfect-square/" target="_blank">LeetCode 367</a><br><br><details><summary>ℹ️ Concept / Details</summary>A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself (e.g., 1, 4, 9, 16).</details></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> num = 16<br><b>Output:</b> true</td>
      <td><b>Time:</b> O(log N)<br><b>Space:</b> O(1)</td>
      <td>Use binary search from `1` to `num/2` or up to `46340` (sqrt of INT_MAX). If `mid * mid == num`, return true. Else if `mid * mid < num`, `low = mid + 1`. Else `high = mid - 1`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isPerfectSquare(num: int) -&gt; bool:&#10;    if num == 1: return True&#10;    low, high = 1, num // 2&#10;    while low &lt;= high:&#10;        mid = (low + high) // 2&#10;        sq = mid * mid&#10;        if sq == num: return True&#10;        elif sq &lt; num: low = mid + 1&#10;        else: high = mid - 1&#10;    return False</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">9</td>
      <td rowspan="1">Math 09 Power Of Two<br><br></b> <a href="https://leetcode.com/problems/power-of-two/" target="_blank">LeetCode 231</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> n = 1<br><b>Output:</b> true</td>
      <td><b>Time:</b> O(1)<br><b>Space:</b> O(1)</td>
      <td>If a number is a power of two, it has exactly one bit set in its binary representation. The expression `n & (n - 1)` clears the lowest set bit. Thus, if `n > 0` and `(n & (n - 1)) == 0`, it is a power of two.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isPowerOfTwo(n: int) -&gt; bool:&#10;    return n &gt; 0 and (n &amp; (n - 1)) == 0</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">10</td>
      <td rowspan="2">Math 10 Power Of Three<br><br></b> <a href="https://leetcode.com/problems/power-of-three/" target="_blank">LeetCode 326</a></td>
      <td rowspan="2"><b>Example 1:</b> <br><b>Input:</b> n = 27<br><b>Output:</b> true</td>
      <td><b>Time:</b> O(log_3 N)<br><b>Space:</b> O(1)</td>
      <td><b>Approach 1:</b><br>General Method: Repeatedly divide the number by 3 as long as it is divisible by 3. If it becomes 1, it's a power of 3.</td>
      <td><b>Edge Cases:</b> <b>N <= 0:</b> Not a power of 3.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isPowerOfThree(n: int) -&gt; bool:&#10;    if n &lt;= 0: return False&#10;    while n % 3 == 0: n //= 3&#10;    return n == 1</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(1)<br><b>Space:</b> O(1)</td>
      <td><b>Approach 2:</b><br>Since `n` is a 32-bit signed integer, the largest power of 3 that fits is `3^19 = 1162261467`. A number `n` is a power of 3 if `n > 0` and `1162261467 % n == 0`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isPowerOfThree(n: int) -&gt; bool:&#10;    return n &gt; 0 and 1162261467 % n == 0</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">11</td>
      <td rowspan="1">Math 11 Power Of Four<br><br></b> <a href="https://leetcode.com/problems/power-of-four/" target="_blank">LeetCode 342</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> n = 16<br><b>Output:</b> true</td>
      <td><b>Time:</b> O(1)<br><b>Space:</b> O(1)</td>
      <td>A power of 4 is also a power of 2, so `n > 0 && (n & (n-1)) == 0` must hold. Also, the single set bit must be at an even position (0-indexed). The mask `0x55555555` has 1s at all even positions. So `(n & 0x55555555) != 0`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isPowerOfFour(n: int) -&gt; bool:&#10;    return n &gt; 0 and (n &amp; (n - 1)) == 0 and (n &amp; 0x55555555) != 0</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">12</td>
      <td rowspan="1">Math 12 Add Digits<br><br></b> <a href="https://leetcode.com/problems/add-digits/" target="_blank">LeetCode 258</a><br><br><details><summary>ℹ️ Concept / Details</summary><b>Digital Root:</b> The digital root of a non-negative integer is the single-digit value obtained by an iterative process of summing digits. Formula: `1 + (n - 1) % 9`.</details></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> num = 38<br><b>Output:</b> 2</td>
      <td><b>Time:</b> O(1)<br><b>Space:</b> O(1)</td>
      <td>This is known as the digital root. The formula is `1 + (n - 1) % 9`. If `n == 0`, return `0`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def addDigits(num: int) -&gt; int:&#10;    if num == 0: return 0&#10;    return 1 + (num - 1) % 9</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">13</td>
      <td rowspan="1">Math 13 Ugly Number<br><br></b> <a href="https://leetcode.com/problems/ugly-number/" target="_blank">LeetCode 263</a><br><br><details><summary>ℹ️ Concept / Details</summary>An ugly number is a number whose only prime factors are 2, 3, and 5.</details></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> n = 6<br><b>Output:</b> true</td>
      <td><b>Time:</b> O(log N)<br><b>Space:</b> O(1)</td>
      <td>If `n <= 0`, return false. Divide `n` by 2, 3, and 5 as long as it is divisible. If the remaining number is 1, it's an ugly number, else false.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isUgly(n: int) -&gt; bool:&#10;    if n &lt;= 0: return False&#10;    for p in [2, 3, 5]:&#10;        while n % p == 0:&#10;            n //= p&#10;    return n == 1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">14</td>
      <td rowspan="1">Math 14 Perfect Number<br><br></b> <a href="https://leetcode.com/problems/perfect-number/" target="_blank">LeetCode 507</a><br><br><details><summary>ℹ️ Concept / Details</summary>A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. For example, 28 = 1 + 2 + 4 + 7 + 14.</details></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> num = 28<br><b>Output:</b> true</td>
      <td><b>Time:</b> O(sqrt(N))<br><b>Space:</b> O(1)</td>
      <td>If `num <= 1`, return false. Iterate up to `sqrt(num)`. If `i` divides `num`, add `i` and `num/i` to the sum. After the loop, compare sum with `num`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def checkPerfectNumber(num: int) -&gt; bool:&#10;    if num &lt;= 1: return False&#10;    total = 1&#10;    for i in range(2, int(num ** 0.5) + 1):&#10;        if num % i == 0:&#10;            total += i&#10;            if i * i != num: total += num // i&#10;    return total == num</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">15</td>
      <td rowspan="1">Math 15 Excel Sheet Column Title<br><br></b> <a href="https://leetcode.com/problems/excel-sheet-column-title/" target="_blank">LeetCode 168</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> columnNumber = 28<br><b>Output:</b> "AB"</td>
      <td><b>Time:</b> O(log_26(N))<br><b>Space:</b> O(1)</td>
      <td>This is essentially base 26 conversion, but 1-indexed (A=1, B=2, Z=26). To make it 0-indexed, decrement `columnNumber` by 1 at each step, get the remainder modulo 26, convert to character, and divide by 26.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def convertToTitle(columnNumber: int) -&gt; str:&#10;    res = []&#10;    while columnNumber &gt; 0:&#10;        columnNumber -= 1&#10;        res.append(chr(ord(&#x27;A&#x27;) + (columnNumber % 26)))&#10;        columnNumber //= 26&#10;    return &quot;&quot;.join(res[::-1])</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">16</td>
      <td rowspan="2">Math 16 Pow X N<br><br></b> <a href="https://leetcode.com/problems/powx-n/" target="_blank">LeetCode 50</a></td>
      <td rowspan="2"><b>Example 1:</b> <br><b>Input:</b> x = 2.00000, n = 10<br><b>Output:</b> 1024.00000</td>
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
      <td rowspan="1">17</td>
      <td rowspan="1">Math 17 Sieve Of Eratosthenes<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/sieve-of-eratosthenes5242/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> N = 10<br><b>Output:</b> 2 3 5 7</td>
      <td><b>Time:</b> O(N log(log N))<br><b>Space:</b> O(N)</td>
      <td>Same as `countPrimes`, but return the actual prime numbers in a list instead of just the count.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def sieveOfEratosthenes(N):&#10;    is_prime = [True] * (N + 1)&#10;    is_prime[0] = is_prime[1] = False&#10;    for i in range(2, int(N**0.5) + 1):&#10;        if is_prime[i]:&#10;            for j in range(i*i, N + 1, i):&#10;                is_prime[j] = False&#10;    return [i for i in range(2, N + 1) if is_prime[i]]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">18</td>
      <td rowspan="1">Math 18 Prime Factors<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/prime-factors5052/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> N = 100<br><b>Output:</b> 2 2 5 5</td>
      <td><b>Time:</b> O(sqrt(N))<br><b>Space:</b> O(1) excluding output</td>
      <td>Iterate from `i = 2` to `sqrt(N)`. If `N % i == 0`, `i` is a prime factor. Add `i` to result, and repeatedly divide `N` by `i` until it's no longer divisible. After the loop, if `N > 1`, then `N` itself is a prime factor and should be added.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def AllPrimeFactors(N):&#10;    ans = []&#10;    for i in range(2, int(N**0.5) + 1):&#10;        if N % i == 0:&#10;            ans.append(i)&#10;            while N % i == 0: N //= i&#10;    if N &gt; 1: ans.append(N)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">19</td>
      <td rowspan="1">Math 19 Print All Divisors<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/print-all-divisors-of-a-number/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> N = 36<br><b>Output:</b> 1 2 3 4 6 9 12 18 36</td>
      <td><b>Time:</b> O(sqrt(N) + k log k)<br><b>Space:</b> O(k)</td>
      <td>Iterate up to sqrt(N). If 'i' divides N, then 'N/i' is also a divisor. Iterating up to N (O(N) time) is unnecessary and inefficient.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_divisors(n):&#10;    ans = []&#10;    for i in range(1, int(n**0.5) + 1):&#10;        if n % i == 0:&#10;            ans.append(i)&#10;            if n // i != i: ans.append(n // i)&#10;    ans.sort()&#10;    print(*(ans))</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">20</td>
      <td rowspan="1">Math 20 Armstrong Number<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/armstrong-numbers2727/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> n = 153<br><b>Output:</b> true</td>
      <td><b>Time:</b> O(log<sub>10</sub>(N))<br><b>Space:</b> O(1)</td>
      <td>Extract each digit, cube it, and sum them up. If the sum equals the original number, it's an Armstrong number.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def armstrongNumber(n):&#10;    return &quot;Yes&quot; if sum(int(d)**3 for d in str(n)) == n else &quot;No&quot;</code></pre></details></td>
    </tr>
  </tbody>
</table>


## Bit Manipulation

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
      <td rowspan="2">1</td>
      <td rowspan="2">Bit 01 Swap Two Numbers<br><br></b> <a href="https://www.geeksforgeeks.org/problems/swap-two-numbers3844/1" target="_blank">GeeksforGeeks</a></td>
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
      <td rowspan="2">2</td>
      <td rowspan="2">Bit 02 Check Ith Bit Set<br><br></b> <a href="https://www.geeksforgeeks.org/problems/check-whether-k-th-bit-is-set-or-not-1587115620/1" target="_blank">GeeksforGeeks</a></td>
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
      <td rowspan="1">3</td>
      <td rowspan="1">Bit 03 Operations Set Clear Toggle<br><br></b> <a href="https://www.geeksforgeeks.org/problems/bit-manipulation-1666686020/1" target="_blank">GeeksforGeeks</a></td>
      <td rowspan="1"><b> </b><br>N=70, i=3 -> Set:78, Clear:62, Toggle:78<br><br><b> </b> 1 &le; N &le; 10<sup>9</sup></td>
      <td><b>Time:</b> O(1)<br><b>Space:</b> O(1)</td>
      <td>Use OR (`|`) to set, AND with NOT (`& ~`) to clear, and XOR (`^`) to toggle.</td>
      <td><b>Edge Cases:</b> **Shift Overflow:** `1LL` used strictly to prevent overflow beyond 31 bits.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def bit_operations(n: int, i: int) -&gt; list:&#10;    set_bit = n | (1 &lt;&lt; i)&#10;    clear_bit = n &amp; ~(1 &lt;&lt; i)&#10;    toggle_bit = n ^ (1 &lt;&lt; i)&#10;    return [set_bit, clear_bit, toggle_bit]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">4</td>
      <td rowspan="1">Bit 04 Copy Set Bits In Range<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/copy-set-bits-in-range0623/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b> </b><br>X=44, Y=3, L=1, R=5<br><b>Output:</b> 47</td>
      <td><b>Time:</b> O(1)<br><b>Space:</b> O(1)</td>
      <td>Create a mask of length (R - L + 1) with all 1s. Shift this mask to the left by (L - 1). AND this mask with Y to isolate the bits to be copied. Finally, OR this isolated value with X.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def setSetBit(x: int, y: int, l: int, r: int) -&gt; int:&#10;    mask = (1 &lt;&lt; (r - l + 1)) - 1&#10;    mask = (mask &lt;&lt; (l - 1))&#10;    mask = mask &amp; y&#10;    return x | mask</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">5</td>
      <td rowspan="2">Bit 05 Divide Two Integers<br><br></b> <a href="https://leetcode.com/problems/divide-two-integers/" target="_blank">LeetCode 29</a></td>
      <td rowspan="2"><b> </b><br><br><b>Input:</b> dividend = 10, divisor = 3<br><b>Output:</b> 3</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Approach 1:</b><br>Iterative subtraction. Subtract divisor from dividend until dividend is smaller than divisor. Count the number of subtractions.</td>
      <td><b>Edge Cases:</b> **Time Limit Exceeded:** Too slow when dividend is `INT_MAX` and divisor is `1`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def divide_brute(dividend: int, divisor: int) -&gt; int:&#10;    if dividend == -2147483648 and divisor == -1: return 2147483647&#10;    a, b = abs(dividend), abs(divisor)&#10;    res = 0&#10;    while a &gt;= b:&#10;        a -= b&#10;        res += 1&#10;    return res if (dividend &gt; 0) == (divisor &gt; 0) else -res</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(log^2 N)<br><b>Space:</b> O(1)</td>
      <td><b>Approach 2:</b><br>Use left shift to find the largest multiple of divisor that fits into dividend. Subtract it and add the shifted value to quotient. Repeat until dividend < divisor.</td>
      <td><b>Edge Cases:</b> **INT_MIN:** Handle edge case `-2147483648 / -1 = 2147483647`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def divide(dividend: int, divisor: int) -&gt; int:&#10;    if dividend == -2147483648 and divisor == -1: return 2147483647&#10;    n, d = abs(dividend), abs(divisor)&#10;    sign = (dividend &lt; 0) == (divisor &lt; 0)&#10;    quotient = 0&#10;    while n &gt;= d:&#10;        temp, multiple = d, 1&#10;        while n &gt;= (temp &lt;&lt; 1):&#10;            temp &lt;&lt;= 1&#10;            multiple &lt;&lt;= 1&#10;        n -= temp&#10;        quotient += multiple&#10;    return quotient if sign else -quotient</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">6</td>
      <td rowspan="2">Bit 06 Calculate Square<br><br></b> <a href="https://www.geeksforgeeks.org/calculate-square-of-a-number-without-using-and-pow/" target="_blank">GeeksforGeeks</a></td>
      <td rowspan="2"><b> </b><br><br><b>Input:</b> n = 5<br><b>Output:</b> 25</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Approach 1:</b><br>Repeated addition. Add `n` to a sum `n` times.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def square_brute(n: int) -&gt; int:&#10;    return sum(abs(n) for _ in range(abs(n)))</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(log N)<br><b>Space:</b> O(log N) (Call stack)</td>
      <td><b>Approach 2:</b><br>If `n` is even, `n = 2*x`, then `n^2 = 4*x^2 = (x^2) << 2`. If `n` is odd, `n = 2*x + 1`, then `n^2 = 4*x^2 + 4*x + 1 = ((x^2 + x) << 2) + 1`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def square(n: int) -&gt; int:&#10;    if n == 0: return 0&#10;    n = abs(n)&#10;    x = n &gt;&gt; 1&#10;    if n &amp; 1:&#10;        return (square(x) &lt;&lt; 2) + (x &lt;&lt; 2) + 1&#10;    else:&#10;        return square(x) &lt;&lt; 2</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">7</td>
      <td rowspan="2">Bit 07 Find Position Of Only Set Bit<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/find-position-of-set-bit3706/1" target="_blank">GFG</a></td>
      <td rowspan="2"><b> </b><br><br><b>Input:</b> N = 2<br><b>Output:</b> 2</td>
      <td><b>Time:</b> O(32)<br><b>Space:</b> O(1)</td>
      <td><b>Approach 1:</b><br>Loop through all 32 bits, count set bits, and record the position. If count is strictly 1, return position, else -1.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findPositionBrute(N: int) -&gt; int:&#10;    count, pos, curr = 0, -1, 1&#10;    while N &gt; 0:&#10;        if N &amp; 1:&#10;            count += 1&#10;            pos = curr&#10;        N &gt;&gt;= 1&#10;        curr += 1&#10;    return pos if count == 1 else -1</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(1)<br><b>Space:</b> O(1)</td>
      <td><b>Approach 2:</b><br>First, check if `N` is a power of 2 using `N & (N - 1) == 0`. If yes, the position is `log2(N) + 1`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import math&#10;def findPosition(N: int) -&gt; int:&#10;    if N &lt;= 0 or (N &amp; (N - 1)) != 0: return -1&#10;    return int(math.log2(N)) + 1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">8</td>
      <td rowspan="2">Bit 08 Count Set Bits<br><br></b> <a href="https://leetcode.com/problems/number-of-1-bits/" target="_blank">LeetCode 191</a></td>
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
      <td rowspan="1">9</td>
      <td rowspan="1">Bit 09 Minimum Bit Flips To Convert Number<br><br></b> <a href="https://leetcode.com/problems/minimum-bit-flips-to-convert-number/" target="_blank">LeetCode 2220</a></td>
      <td rowspan="1"><b> </b><br><br><b>Input:</b> start=10 (1010), goal=7 (0111)<br><b>Output:</b> 3 flips</td>
      <td><b>Time:</b> O(Set Bits)<br><b>Space:</b> O(1)</td>
      <td>XOR `start` and `goal` to isolate differing bits, then count the set bits in the result.</td>
      <td><b>Edge Cases:</b> **XOR Magic:** XOR inherently maps identical bits to 0 and different bits to 1, instantly mapping the problem to Hamming Weight.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def min_bit_flips(start: int, goal: int) -&gt; int:&#10;    xor_res = start ^ goal&#10;    count = 0&#10;    while xor_res &gt; 0:&#10;        xor_res &amp;= (xor_res - 1)&#10;        count += 1&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">10</td>
      <td rowspan="2">Bit 10 Single Number<br><br></b> <a href="https://leetcode.com/problems/single-number/" target="_blank">LeetCode 136</a></td>
      <td rowspan="2"><b> </b><br><br><b>Input:</b> nums = [4,1,2,1,2]<br><b>Output:</b> 4</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><b>Approach 1:</b><br>Use a Hash Map to count occurrences. Return the element with count 1.<br><br><b>Dependencies:</b> **Data Structure:**<br><code>std::unordered_map</code> / <code>dict</code></td>
      <td><b>Edge Cases:</b> **Memory Heavy:** Fails optimal space constraint due to dynamic hash mapping allocation.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">from collections import Counter&#10;def single_number_hash(nums: list[int]) -&gt; int:&#10;    counts = Counter(nums)&#10;    for num, count in counts.items():&#10;        if count == 1: return num&#10;    return -1</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Approach 2:</b><br>Use XOR bitwise operation. `X ^ X = 0` and `X ^ 0 = X`. XORing all elements pairs up the duplicates to 0, leaving the single element.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def single_number(nums: list[int]) -&gt; int:&#10;    ans = 0&#10;    for num in nums:&#10;        ans ^= num&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">11</td>
      <td rowspan="2">Bit 11 Single Number II<br><br></b> <a href="https://leetcode.com/problems/single-number-ii/" target="_blank">LeetCode 137</a></td>
      <td rowspan="2"><b> </b><br><br><b>Input:</b> nums = [2,2,3,2]<br><b>Output:</b> 3</td>
      <td><b>Time:</b> O(32 * N)<br><b>Space:</b> O(1)</td>
      <td><b>Approach 1:</b><br>Count bits: For each bit position, count how many numbers have it set. If count is not divisible by 3, the single number has this bit set.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def single_number_count(nums: list[int]) -&gt; int:&#10;    ans = 0&#10;    for i in range(32):&#10;        total = sum((num &gt;&gt; i) &amp; 1 for num in nums)&#10;        if total % 3:&#10;            # Handle negative numbers in Python&#10;            if i == 31: ans -= (1 &lt;&lt; 31)&#10;            else: ans |= (1 &lt;&lt; i)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Approach 2:</b><br>Use bitmask magic with `ones` and `twos`. `ones` keeps track of bits that appeared exactly once. `twos` tracks bits that appeared exactly twice. When a bit appears 3 times, both `ones` and `twos` are cleared.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def singleNumber(nums: list[int]) -&gt; int:&#10;    ones, twos = 0, 0&#10;    for n in nums:&#10;        ones = (ones ^ n) &amp; ~twos&#10;        twos = (twos ^ n) &amp; ~ones&#10;    return ones</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">12</td>
      <td rowspan="1">Bit 12 Single Number III<br><br></b> <a href="https://leetcode.com/problems/single-number-iii/" target="_blank">LeetCode 260</a></td>
      <td rowspan="1"><b> </b><br><br><b>Input:</b> nums = [1,2,1,3,2,5]<br><b>Output:</b> [3,5]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>XOR all elements to get `x ^ y`. Find the rightmost set bit in this XOR result. This bit distinguishes `x` and `y`. Iterate through array again, divide numbers into two groups based on this bit, and XOR each group. The results are `x` and `y`.</td>
      <td><b>Edge Cases:</b> **Overflow:** Rightmost set bit can be found using `val & -(unsigned int)val`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def singleNumber(nums: list[int]) -&gt; list[int]:&#10;    xor_all = 0&#10;    for n in nums: xor_all ^= n&#10;    rightmost_set_bit = xor_all &amp; -xor_all&#10;    x, y = 0, 0&#10;    for n in nums:&#10;        if n &amp; rightmost_set_bit: x ^= n&#10;        else: y ^= n&#10;    return [x, y]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">13</td>
      <td rowspan="2">Bit 13 Subsets<br><br></b> <a href="https://leetcode.com/problems/subsets/" target="_blank">LeetCode 78</a></td>
      <td rowspan="2"><b> </b><br><br><b>Input:</b> nums = [1,2,3]<br><b>Output:</b> [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]</td>
      <td><b>Time:</b> O(N * 2^N)<br><b>Space:</b> O(N * 2^N)</td>
      <td><b>Approach 1:</b><br>Recursive backtracking (include/exclude pattern).</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def subsets_rec(nums: list[int]) -&gt; list[list[int]]:&#10;    ans, curr = [], []&#10;    def solve(idx):&#10;        if idx == len(nums):&#10;            ans.append(curr[:])&#10;            return&#10;        curr.append(nums[idx])&#10;        solve(idx + 1)&#10;        curr.pop()&#10;        solve(idx + 1)&#10;    solve(0)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(N * 2^N)<br><b>Space:</b> O(N * 2^N)</td>
      <td><b>Approach 2:</b><br>Bit manipulation technique. For N elements, there are 2^N subsets. Count from 0 to 2^N - 1. For each number, its binary representation indicates which elements to include.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def subsets(nums: list[int]) -&gt; list[list[int]]:&#10;    n = len(nums)&#10;    subsets_count = 1 &lt;&lt; n&#10;    ans = []&#10;    for i in range(subsets_count):&#10;        subset = []&#10;        for j in range(n):&#10;            if i &amp; (1 &lt;&lt; j):&#10;                subset.append(nums[j])&#10;        ans.append(subset)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">14</td>
      <td rowspan="2">Bit 14 Count Total Set Bits 1 To N<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/count-total-set-bits-1587115620/1" target="_blank">GFG</a></td>
      <td rowspan="2"><b> </b><br><br><b>Input:</b> N=4<br><b>Output:</b> 5<br>Explanation: 1(01) + 2(10) + 3(11) + 4(100) -> 1+1+2+1 = 5</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(1)</td>
      <td><b>Approach 1:</b><br>Loop from 1 to N and count set bits using Brian Kernighan's.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def countSetBitsBrute(N: int) -&gt; int:&#10;    total = 0&#10;    for i in range(1, N+1):&#10;        while i:&#10;            i &amp;= (i - 1)&#10;            total += 1&#10;    return total</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(log N)<br><b>Space:</b> O(log N)</td>
      <td><b>Approach 2:</b><br>Find largest power of 2 <= n (`x`). Bits up to `2^x - 1` are `x * 2^(x-1)`. The MSB of remaining numbers is `n - 2^x + 1`. Then recursively call for `n - 2^x`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def countSetBits(n: int) -&gt; int:&#10;    if n &lt;= 0: return 0&#10;    x = 0&#10;    while (1 &lt;&lt; x) &lt;= n:&#10;        x += 1&#10;    x -= 1&#10;    bitsUpTo2x = x * (1 &lt;&lt; (x - 1))&#10;    msbOfRest = n - (1 &lt;&lt; x) + 1&#10;    rest = n - (1 &lt;&lt; x)&#10;    return bitsUpTo2x + msbOfRest + countSetBits(rest)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">15</td>
      <td rowspan="1">Bit 15 Find The Original Array Of Prefix Xor<br><br></b> <a href="https://leetcode.com/problems/find-the-original-array-of-prefix-xor/" target="_blank">LeetCode 2433</a></td>
      <td rowspan="1"><b> </b> `pref = [5,2,0,3,1]`.<br><b>Output:</b> `[5,7,2,3,2]`.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Since `pref[i] = pref[i-1] ^ arr[i]`, we can find `arr[i]` by doing `pref[i-1] ^ pref[i]`. `arr[0] = pref[0]`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findArray(pref: list[int]) -&gt; list[int]:&#10;    arr = [0] * len(pref)&#10;    arr[0] = pref[0]&#10;    for i in range(1, len(pref)):&#10;        arr[i] = pref[i-1] ^ pref[i]&#10;    return arr</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">16</td>
      <td rowspan="1">Bit 16 Maximum Xor For Each Query<br><br></b> <a href="https://leetcode.com/problems/maximum-xor-for-each-query/" target="_blank">LeetCode 1829</a></td>
      <td rowspan="1"><b> </b> `nums = [0,1,1,3], maximumBit = 2`.<br><b>Output:</b> `[0,3,2,3]`.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>The maximum possible value is `(1 << maximumBit) - 1`. If current running XOR is `curr`, we want `k` such that `curr ^ k = max_val`. Thus `k = curr ^ max_val`. Do this iteratively backwards.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def getMaximumXor(nums: list[int], maximumBit: int) -&gt; list[int]:&#10;    curr = 0&#10;    for n in nums: curr ^= n&#10;    max_val = (1 &lt;&lt; maximumBit) - 1&#10;    ans = []&#10;    for i in range(len(nums)-1, -1, -1):&#10;        ans.append(curr ^ max_val)&#10;        curr ^= nums[i]&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">17</td>
      <td rowspan="1">Bit 17 Minimum Flips To Make A Or B Equal To C<br><br></b> <a href="https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/" target="_blank">LeetCode 1318</a></td>
      <td rowspan="1"><b> </b><br><br><b>Input:</b> a=2, b=6, c=5<br><b>Output:</b> 3</td>
      <td><b>Time:</b> O(1)<br><b>Space:</b> O(1)</td>
      <td>Iterate through 32 bits. If bit in `c` is 1, at least one of `a` or `b` needs to be 1. If both are 0, flip one (1 flip). If bit in `c` is 0, both `a` and `b` must be 0. Flips needed = bit of `a` + bit of `b`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minFlips(a: int, b: int, c: int) -&gt; int:&#10;    flips = 0&#10;    for i in range(32):&#10;        bit_a = (a &gt;&gt; i) &amp; 1&#10;        bit_b = (b &gt;&gt; i) &amp; 1&#10;        bit_c = (c &gt;&gt; i) &amp; 1&#10;        if bit_c == 1:&#10;            if bit_a == 0 and bit_b == 0: flips += 1&#10;        else:&#10;            flips += bit_a + bit_b&#10;    return flips</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">18</td>
      <td rowspan="1">Bit 18 Number Of Steps To Reduce To Zero<br><br></b> <a href="https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/" target="_blank">LeetCode 1342</a></td>
      <td rowspan="1"><b> </b><br><br><b>Input:</b> num = 14<br><b>Output:</b> 6</td>
      <td><b>Time:</b> O(log N)<br><b>Space:</b> O(1)</td>
      <td>If `num` is odd, subtract 1 (equivalent to clearing rightmost bit). If even, divide by 2 (equivalent to right shift).</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def numberOfSteps(num: int) -&gt; int:&#10;    if num == 0: return 0&#10;    steps = 0&#10;    while num &gt; 0:&#10;        if num &amp; 1: num -= 1&#10;        else: num &gt;&gt;= 1&#10;        steps += 1&#10;    return steps</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">19</td>
      <td rowspan="1">Bit 19 Decode Xored Array<br><br></b> <a href="https://leetcode.com/problems/decode-xored-array/" target="_blank">LeetCode 1720</a></td>
      <td rowspan="1"><b> </b><br><br><b>Input:</b> encoded=[1,2,3], first=1<br><b>Output:</b> [1,0,2,1]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Since `encoded[i] = arr[i] ^ arr[i+1]`, it implies `arr[i+1] = arr[i] ^ encoded[i]`. We have `arr[0]`, so we can iteratively find the rest.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def decode(encoded: list[int], first: int) -&gt; list[int]:&#10;    arr = [0] * (len(encoded) + 1)&#10;    arr[0] = first&#10;    for i in range(len(encoded)):&#10;        arr[i+1] = arr[i] ^ encoded[i]&#10;    return arr</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">20</td>
      <td rowspan="1">Bit 20 Longest Substring Vowels Even Counts<br><br></b> <a href="https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/" target="_blank">LeetCode 1371</a></td>
      <td rowspan="1"><b> </b><br><br><b>Input:</b> s = "eleetminicoworoep"<br><b>Output:</b> 13</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(32) since only 5 bits used</td>
      <td>Use a 5-bit mask to represent the parity of counts for 'a','e','i','o','u'. If we encounter a vowel, flip its bit. If the same mask is seen again at index `i` (was previously seen at `j`), then the substring `s[j+1...i]` has even vowel counts. Use a hash map to store first occurrence of each mask.<br><br><b>Dependencies:</b> <code>#include <unordered_map></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findTheLongestSubstring(s: str) -&gt; int:&#10;    m = {0: -1}&#10;    mask, maxLen = 0, 0&#10;    vowels = {&#x27;a&#x27;: 0, &#x27;e&#x27;: 1, &#x27;i&#x27;: 2, &#x27;o&#x27;: 3, &#x27;u&#x27;: 4}&#10;    for i, char in enumerate(s):&#10;        if char in vowels:&#10;            mask ^= (1 &lt;&lt; vowels[char])&#10;        if mask in m:&#10;            maxLen = max(maxLen, i - m[mask])&#10;        else:&#10;            m[mask] = i&#10;    return maxLen</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">21</td>
      <td rowspan="1">Bit 21 Xor Queries Of A Subarray<br><br></b> <a href="https://leetcode.com/problems/xor-queries-of-a-subarray/" target="_blank">LeetCode 1310</a></td>
      <td rowspan="1"><b> </b><br><br><b>Input:</b> arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]<br><b>Output:</b> [2,7,14,8]</td>
      <td><b>Time:</b> O(N + Q)<br><b>Space:</b> O(N)</td>
      <td>Create a prefix XOR array. Query answer for `[L, R]` is `prefix[R] ^ prefix[L-1]`. If `L == 0`, answer is `prefix[R]`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def xorQueries(arr: list[int], queries: list[list[int]]) -&gt; list[int]:&#10;    pref = [0] * len(arr)&#10;    pref[0] = arr[0]&#10;    for i in range(1, len(arr)):&#10;        pref[i] = pref[i-1] ^ arr[i]&#10;    ans = []&#10;    for l, r in queries:&#10;        if l == 0: ans.append(pref[r])&#10;        else: ans.append(pref[r] ^ pref[l-1])&#10;    return ans</code></pre></details></td>
    </tr>
  </tbody>
</table>


## Arrays

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
      <td rowspan="2">1</td>
      <td rowspan="2">Arr 01 Largest Element<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/largest-element-in-array/1" target="_blank">GFG</a></td>
      <td rowspan="2"><b> </b> <br><b>Input:</b> A = [1, 8, 7, 56, 90]<br><b>Output:</b> 90</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(1) or O(N) depending on sort</td>
      <td><b>Approach 1:</b><br>Brute Force: Sort the array and return the last element.<br><br><b>Dependencies:</b> std::sort</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def largest(arr: list[int]) -&gt; int:&#10;    arr.sort()&#10;    return arr[-1]</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><b>Approach 2:</b><br>Optimal: Iterate through the array maintaining a variable for the maximum element seen so far.</td>
      <td><b>Edge Cases:</b> <b>Initialization:</b> Initialize `max_val` with the first element or negative infinity.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def largest(arr: list[int]) -&gt; int:&#10;    max_val = arr[0]&#10;    for num in arr:&#10;        if num &gt; max_val:&#10;            max_val = num&#10;    return max_val</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">2</td>
      <td rowspan="2">Arr 02 Second Largest Element<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/second-largest3735/1" target="_blank">GFG</a></td>
      <td rowspan="2"><b> </b> <br><b>Input:</b> arr = [12, 35, 1, 10, 34, 1]<br><b>Output:</b> 34<br><br><b> </b> Find it in a single pass O(N) time.</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(1)</td>
      <td><b>Approach 1:</b><br>Brute Force: Sort the array, then iterate from the back to find the first element smaller than the largest.<br><br><b>Dependencies:</b> std::sort</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print2largest(arr, n):&#10;    arr.sort()&#10;    for i in range(n-2, -1, -1):&#10;        if arr[i] != arr[n-1]: return arr[i]&#10;    return -1</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><b>Approach 2:</b><br>Optimal: Maintain two variables, `largest` and `second_largest`. Update them simultaneously during a single pass.</td>
      <td><b>Edge Cases:</b> <b>No Second Largest:</b> If all elements are same or array size < 2, return -1.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print2largest(arr: list[int]) -&gt; int:&#10;    largest = -1&#10;    second_largest = -1&#10;    for num in arr:&#10;        if num &gt; largest:&#10;            second_largest = largest&#10;            largest = num&#10;        elif num &gt; second_largest and num != largest:&#10;            second_largest = num&#10;    return second_largest</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">3</td>
      <td rowspan="1">Arr 03 Check If Array Is Sorted And Rotated<br><br></b> <a href="https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/" target="_blank">LeetCode 1752</a></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> nums = [3,4,5,1,2]<br><b>Output:</b> true</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td>Optimal: Count the number of "breaks" where `nums[i] > nums[i+1]`. For a sorted and rotated array, there can be at most 1 break.</td>
      <td><b>Edge Cases:</b> <b>Circular Check:</b> We must also check the boundary between the last and first element `nums[n-1] > nums[0]`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def check(nums: list[int]) -&gt; bool:&#10;    count = 0&#10;    n = len(nums)&#10;    for i in range(n):&#10;        if nums[i] &gt; nums[(i + 1) % n]:&#10;            count += 1&#10;    return count &lt;= 1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">4</td>
      <td rowspan="2">Arr 04 Remove Duplicates From Sorted Array<br><br></b> <a href="https://leetcode.com/problems/remove-duplicates-from-sorted-array/" target="_blank">LeetCode 26</a></td>
      <td rowspan="2"><b> </b> <br><b>Input:</b> nums = [1,1,2]<br><b>Output:</b> 2, nums = [1,2,_]</td>
      <td><b>Time:</b> O(N log N) or O(N)<br><b>Space:</b> O(N)</td>
      <td><b>Approach 1:</b><br>Brute Force: Use a HashSet to store unique elements, then put them back into the array.<br><br><b>Dependencies:</b> std::set</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def removeDuplicates(nums):&#10;    unique_nums = sorted(list(set(nums)))&#10;    for i in range(len(unique_nums)):&#10;        nums[i] = unique_nums[i]&#10;    return len(unique_nums)</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><b>Approach 2:</b><br>Optimal: Two-pointer approach. Pointer `i` keeps track of unique elements, pointer `j` scans the array to find new unique elements.</td>
      <td><b>Edge Cases:</b> <b>Empty Array:</b> Handled automatically if `n=0`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def removeDuplicates(nums: list[int]) -&gt; int:&#10;    if not nums: return 0&#10;    i = 0&#10;    for j in range(1, len(nums)):&#10;        if nums[j] != nums[i]:&#10;            i += 1&#10;            nums[i] = nums[j]&#10;    return i + 1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">5</td>
      <td rowspan="2">Arr 05 Rotate Array<br><br></b> <a href="https://leetcode.com/problems/rotate-array/" target="_blank">LeetCode 189</a></td>
      <td rowspan="2"><b> </b> <br><b>Input:</b> nums = [1,2,3,4,5,6,7], k = 3<br><b>Output:</b> [5,6,7,1,2,3,4]</td>
      <td><b>Time:</b> O(N * K) or O(N)<br><b>Space:</b> O(1) or O(N)</td>
      <td><b>Approach 1:</b><br>Brute Force: Rotate the array one by one, k times. Or use a temporary array of size N.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def rotate(nums, k):&#10;    n = len(nums)&#10;    k = k % n&#10;    temp = [0] * n&#10;    for i in range(n):&#10;        temp[(i+k)%n] = nums[i]&#10;    for i in range(n):&#10;        nums[i] = temp[i]</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><b>Approach 2:</b><br>Optimal: Reverse Algorithm. Reverse the whole array, then reverse the first `k` elements, then reverse the remaining `N-k` elements.<br><br><b>Dependencies:</b> <code>std::reverse</code></td>
      <td><b>Edge Cases:</b> <b>K > N:</b> k might be greater than array length, so perform `k = k % n` first.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def rotate(nums: list[int], k: int) -&gt; None:&#10;    n = len(nums)&#10;    k = k % n&#10;    nums.reverse()&#10;    nums[:k] = reversed(nums[:k])&#10;    nums[k:] = reversed(nums[k:])</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">6</td>
      <td rowspan="1">Arr 06 Move Zeroes<br><br></b> <a href="https://leetcode.com/problems/move-zeroes/" target="_blank">LeetCode 283</a></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> nums = [0,1,0,3,12]<br><b>Output:</b> [1,3,12,0,0]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Two-pointer approach (Snowball method). Pointer `i` tracks the first zero found, pointer `j` scans for non-zeroes to swap.<br><br><b>Dependencies:</b> <code>std::swap</code></td>
      <td><b>Edge Cases:</b> <b>No zeroes:</b> Swaps element with itself initially, no overhead.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def moveZeroes(nums: list[int]) -&gt; None:&#10;    i = 0&#10;    for j in range(len(nums)):&#10;        if nums[j] != 0:&#10;            nums[i], nums[j] = nums[j], nums[i]&#10;            i += 1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">7</td>
      <td rowspan="2">Arr 07 Missing Number<br><br></b> <a href="https://leetcode.com/problems/missing-number/" target="_blank">LeetCode 268</a></td>
      <td rowspan="2"><b> </b> <br><b>Input:</b> nums = [3,0,1]<br><b>Output:</b> 2</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(1)</td>
      <td><b>Approach 1:</b><br>Brute Force: Linear search for each number from 0 to N inside the array.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def missingNumber(nums):&#10;    for i in range(len(nums) + 1):&#10;        if i not in nums:&#10;            return i&#10;    return -1</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><b>Approach 2:</b><br>Optimal: Using XOR: XORing a number with itself results in 0. XOR all indices `[0,n]` and all elements in `nums`. The missing number will remain.</td>
      <td><b>Edge Cases:</b> <b>Mathematical Sum alternative:</b> Gaussian sum formula `N*(N+1)/2` can cause integer overflow, XOR completely bypasses overflow risks.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def missingNumber(nums: list[int]) -&gt; int:&#10;    res = len(nums)&#10;    for i, num in enumerate(nums):&#10;        res ^= i ^ num&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">8</td>
      <td rowspan="1">Arr 08 Max Consecutive Ones<br><br></b> <a href="https://leetcode.com/problems/max-consecutive-ones/" target="_blank">LeetCode 485</a></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> nums = [1,1,0,1,1,1]<br><b>Output:</b> 3</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Iterate while counting 1s. If a 0 is found, update max count and reset current count to 0.<br><br><b>Dependencies:</b> <code>std::max</code></td>
      <td><b>Edge Cases:</b> <b>Trailing Ones:</b> Must perform a final max check outside the loop or update max dynamically inside.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findMaxConsecutiveOnes(nums: list[int]) -&gt; int:&#10;    max_cnt = current_cnt = 0&#10;    for num in nums:&#10;        if num == 1:&#10;            current_cnt += 1&#10;            max_cnt = max(max_cnt, current_cnt)&#10;        else:&#10;            current_cnt = 0&#10;    return max_cnt</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">9</td>
      <td rowspan="2">Arr 09 Sort Colors Dnf<br><br></b> <a href="https://leetcode.com/problems/sort-colors/" target="_blank">LeetCode 75</a></td>
      <td rowspan="2"><b> </b> <br><b>Input:</b> nums = [2,0,2,1,1,0]<br><b>Output:</b> [0,0,1,1,2,2]<br><br><b> </b> Do not use library sort. Use single pass.</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(N)</td>
      <td><b>Approach 1:</b><br>Brute Force: Use any standard sorting algorithm like Merge Sort.<br><br><b>Dependencies:</b> std::sort</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def sortColors(nums):&#10;    nums.sort()</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><b>Approach 2:</b><br>Optimal: Dutch National Flag Algorithm (3 pointers). `low` tracks 0s, `mid` scans array, `high` tracks 2s. Swap elements to maintain sections.<br><br><b>Dependencies:</b> <code>std::swap</code></td>
      <td><b>Edge Cases:</b> <b>Mid pointer increment:</b> When swapping with `high`, we do NOT increment `mid` because the swapped element from `high` needs to be evaluated.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def sortColors(nums: list[int]) -&gt; None:&#10;    low, mid, high = 0, 0, len(nums) - 1&#10;    while mid &lt;= high:&#10;        if nums[mid] == 0:&#10;            nums[low], nums[mid] = nums[mid], nums[low]&#10;            low += 1; mid += 1&#10;        elif nums[mid] == 1:&#10;            mid += 1&#10;        else:&#10;            nums[mid], nums[high] = nums[high], nums[mid]&#10;            high -= 1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">10</td>
      <td rowspan="2">Arr 10 Majority Element<br><br></b> <a href="https://leetcode.com/problems/majority-element/" target="_blank">LeetCode 169</a></td>
      <td rowspan="2"><b> </b> <br><b>Input:</b> nums = [2,2,1,1,1,2,2]<br><b>Output:</b> 2</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(1)</td>
      <td><b>Approach 1:</b><br>Brute Force: Use two nested loops to count occurrences of each element.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def majorityElement(nums):&#10;    n = len(nums)&#10;    for num in nums:&#10;        if nums.count(num) &gt; n // 2:&#10;            return num&#10;    return -1</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1)</td>
      <td><b>Approach 2:</b><br>Optimal: Moore's Voting Algorithm. Track a candidate and a counter. Increment if same as candidate, decrement if different. If zero, pick new candidate.</td>
      <td><b>Edge Cases:</b> <b>Verification phase:</b> If it's not guaranteed a majority exists, a second `O(N)` pass is required to count the candidate. (Leetcode guarantees it exists).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def majorityElement(nums: list[int]) -&gt; int:&#10;    count = candidate = 0&#10;    for num in nums:&#10;        if count == 0:&#10;            candidate = num&#10;        count += (1 if num == candidate else -1)&#10;    return candidate</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">11</td>
      <td rowspan="2">Arr 11 Kadanes Algorithm Max Subarray Sum<br><br></b> <a href="https://leetcode.com/problems/maximum-subarray/" target="_blank">LeetCode 53</a></td>
      <td rowspan="2"><b> </b> <br><b>Input:</b> nums = [-2,1,-3,4,-1,2,1,-5,4]<br><b>Output:</b> 6 (Subarray [4,-1,2,1])</td>
      <td><b>Time:</b> O(N^3)<br><b>Space:</b> O(1)</td>
      <td><b>Approach 1:</b><br>Brute Force: Generate all possible subarrays using three nested loops and find the maximum sum.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxSubArray(nums):&#10;    maxi = float(&#x27;-inf&#x27;)&#10;    n = len(nums)&#10;    for i in range(n):&#10;        for j in range(i, n):&#10;            current_sum = sum(nums[i:j+1])&#10;            maxi = max(maxi, current_sum)&#10;    return maxi</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td><b>Approach 2:</b><br>Optimal: Kadane's Algorithm. Keep a running sum. If sum becomes negative, reset it to 0 (a negative prefix will never help a future subarray).<br><br><b>Dependencies:</b> <code>std::max</code></td>
      <td><b>Edge Cases:</b> <b>All Negative Numbers:</b> Initialize `max_sum` with `INT_MIN` or `nums[0]` so it can correctly return the smallest negative number instead of 0.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxSubArray(nums: list[int]) -&gt; int:&#10;    max_sum = float(&#x27;-inf&#x27;)&#10;    current_sum = 0&#10;    for num in nums:&#10;        current_sum += num&#10;        if current_sum &gt; max_sum:&#10;            max_sum = current_sum&#10;        if current_sum &lt; 0:&#10;            current_sum = 0&#10;    return int(max_sum)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">12</td>
      <td rowspan="1">Arr 12 Best Time To Buy And Sell Stock<br><br></b> <a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock/" target="_blank">LeetCode 121</a></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> prices = [7,1,5,3,6,4]<br><b>Output:</b> 5</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Iterate while keeping track of the minimum price seen so far. Subtract this min from the current price to find potential profit.<br><br><b>Dependencies:</b> <code>std::max</code>, <code>std::min</code></td>
      <td><b>Edge Cases:</b> <b>No Profit Possible:</b> `max_profit` initializes at 0. If price strictly decreases, it never updates and naturally returns 0.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxProfit(prices: list[int]) -&gt; int:&#10;    min_price = prices[0]&#10;    max_profit = 0&#10;    for i in range(1, len(prices)):&#10;        max_profit = max(max_profit, prices[i] - min_price)&#10;        min_price = min(min_price, prices[i])&#10;    return max_profit</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">13</td>
      <td rowspan="1">Arr 13 Rearrange Array Elements By Sign<br><br></b> <a href="https://leetcode.com/problems/rearrange-array-elements-by-sign/" target="_blank">LeetCode 2149</a></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> nums = [3,1,-2,-5,2,-4]<br><b>Output:</b> [3,-2,1,-5,2,-4]<br><br><b> </b> Maintain relative order.</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(N) (Constraint)</td>
      <td>Optimal: Use two pointers, `pos_idx` starting at 0, `neg_idx` starting at 1. Traverse and place elements directly into a new result array.</td>
      <td><b>Edge Cases:</b> <b>In-Place Attempt:</b> Doing this in-place `O(1)` space while maintaining relative order drops Time to `O(N^2)`. The optimal tradeoff is `O(N)` space.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def rearrangeArray(nums: list[int]) -&gt; list[int]:&#10;    ans = [0] * len(nums)&#10;    pos_idx, neg_idx = 0, 1&#10;    for num in nums:&#10;        if num &gt; 0:&#10;            ans[pos_idx] = num&#10;            pos_idx += 2&#10;        else:&#10;            ans[neg_idx] = num&#10;            neg_idx += 2&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">14</td>
      <td rowspan="1">Arr 14 Next Permutation<br><br></b> <a href="https://leetcode.com/problems/next-permutation/" target="_blank">LeetCode 31</a></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> nums = [1,2,3]<br><b>Output:</b> [1,3,2]<br><b> </b> <br><b>Input:</b> nums = [3,2,1]<br><b>Output:</b> [1,2,3]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: 1. Find break point (i) where arr[i] < arr[i+1]. 2. Swap it with smallest element > arr[i] from the back. 3. Reverse the right half.<br><br><b>Dependencies:</b> <code>std::reverse</code></td>
      <td><b>Edge Cases:</b> <b>Last Permutation:</b> If break point is not found (`i < 0`), it means the array is sorted descending. Just reverse the entire array to get the lowest permutation.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def nextPermutation(nums: list[int]) -&gt; None:&#10;    n = len(nums)&#10;    i = n - 2&#10;    while i &gt;= 0 and nums[i] &gt;= nums[i + 1]:&#10;        i -= 1&#10;        &#10;    if i &gt;= 0:&#10;        j = n - 1&#10;        while nums[j] &lt;= nums[i]:&#10;            j -= 1&#10;        nums[i], nums[j] = nums[j], nums[i]&#10;        &#10;    nums[i+1:] = reversed(nums[i+1:])</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">15</td>
      <td rowspan="1">Arr 15 Pascals Triangle<br><br></b> <a href="https://leetcode.com/problems/pascals-triangle/" target="_blank">LeetCode 118</a></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> numRows = 5<br><b>Output:</b> [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]</td>
      <td><b>Time:</b> O(N<sup>2</sup>) (Constraint)<br><b>Space:</b> O(N<sup>2</sup>) (Constraint)</td>
      <td>Optimal: Generate row by row. Each element `val[i][j]` is the sum of `val[i-1][j-1]` and `val[i-1][j]`.</td>
      <td><b>Edge Cases:</b> <b>Boundary 1s:</b> First and last elements of every row are always 1. Pre-filling row with 1s avoids out-of-bounds checks.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def generate(numRows: int) -&gt; list[list[int]]:&#10;    ans = []&#10;    for i in range(numRows):&#10;        row = [1] * (i + 1)&#10;        for j in range(1, i):&#10;            row[j] = ans[i-1][j-1] + ans[i-1][j]&#10;        ans.append(row)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">16</td>
      <td rowspan="1">Arr 16 Majority Element II<br><br></b> <a href="https://leetcode.com/problems/majority-element-ii/" target="_blank">LeetCode 229</a></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> nums = [3,2,3]<br><b>Output:</b> [3]<br><br><b> </b> Time O(N), Space O(1).</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td>Optimal: Extended Moore's Voting Algorithm. At most TWO elements can appear > N/3 times. Track two candidates and two counters.</td>
      <td><b>Edge Cases:</b> <b>Verification phase required:</b> We MUST perform a second pass to count occurrences of `candidate1` and `candidate2` because it's not guaranteed they appear > N/3 times.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def majorityElement(nums: list[int]) -&gt; list[int]:&#10;    cnt1, cnt2, el1, el2 = 0, 0, float(&#x27;-inf&#x27;), float(&#x27;-inf&#x27;)&#10;    for num in nums:&#10;        if cnt1 == 0 and num != el2:&#10;            cnt1 = 1; el1 = num&#10;        elif cnt2 == 0 and num != el1:&#10;            cnt2 = 1; el2 = num&#10;        elif num == el1:&#10;            cnt1 += 1&#10;        elif num == el2:&#10;            cnt2 += 1&#10;        else:&#10;            cnt1 -= 1; cnt2 -= 1&#10;            &#10;    ans = []&#10;    if nums.count(el1) &gt; len(nums) // 3:&#10;        ans.append(el1)&#10;    if nums.count(el2) &gt; len(nums) // 3:&#10;        ans.append(el2)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">17</td>
      <td rowspan="1">Arr 17 3Sum<br><br></b> <a href="https://leetcode.com/problems/3sum/" target="_blank">LeetCode 15</a></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> nums = [-1,0,1,2,-1,-4]<br><b>Output:</b> [[-1,-1,2],[-1,0,1]]<br><br><b> </b> Solution set must not contain duplicate triplets.</td>
      <td><b>Time:</b> O(N<sup>2</sup>) (Constraint)<br><b>Space:</b> O(1) (Trade-off)</td>
      <td>Optimal: Sort the array. Use a loop to fix `i`, then use a Two-Pointer approach (`j`, `k`) for the remaining array to find sum `0 - nums[i]`.<br><br><b>Dependencies:</b> <code>std::sort</code></td>
      <td><b>Edge Cases:</b> <b>Duplicate skipping:</b> To prevent duplicate triplets, skip identical adjacent elements for `i`, `j`, and `k`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def threeSum(nums: list[int]) -&gt; list[list[int]]:&#10;    ans = []&#10;    nums.sort()&#10;    n = len(nums)&#10;    for i in range(n):&#10;        if i &gt; 0 and nums[i] == nums[i-1]: continue&#10;        j, k = i + 1, n - 1&#10;        while j &lt; k:&#10;            s = nums[i] + nums[j] + nums[k]&#10;            if s &lt; 0:&#10;                j += 1&#10;            elif s &gt; 0:&#10;                k -= 1&#10;            else:&#10;                ans.append([nums[i], nums[j], nums[k]])&#10;                j += 1; k -= 1&#10;                while j &lt; k and nums[j] == nums[j-1]: j += 1&#10;                while j &lt; k and nums[k] == nums[k+1]: k -= 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">18</td>
      <td rowspan="1">Arr 18 Merge Intervals<br><br></b> <a href="https://leetcode.com/problems/merge-intervals/" target="_blank">LeetCode 56</a></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> intervals = [[1,3],[2,6],[8,10],[15,18]]<br><b>Output:</b> [[1,6],[8,10],[15,18]]</td>
      <td><b>Time:</b> O(N log N) (Constraint)<br><b>Space:</b> O(N)</td>
      <td>Optimal: Sort the intervals based on the start time. Iterate and merge: if current start <= previous end, update previous end to `max(prev_end, curr_end)`.<br><br><b>Dependencies:</b> <code>std::sort</code></td>
      <td><b>Edge Cases:</b> <b>Subsumed Intervals:</b> `[1,4]` and `[2,3]` -> using `max()` prevents shrinking the end time to `3`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def merge(intervals: list[list[int]]) -&gt; list[list[int]]:&#10;    if not intervals: return []&#10;    intervals.sort(key=lambda x: x[0])&#10;    merged = [intervals[0]]&#10;    for i in range(1, len(intervals)):&#10;        if intervals[i][0] &lt;= merged[-1][1]:&#10;            merged[-1][1] = max(merged[-1][1], intervals[i][1])&#10;        else:&#10;            merged.append(intervals[i])&#10;    return merged</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">19</td>
      <td rowspan="1">Arr 19 Leaders In An Array<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> A = [16,17,4,3,5,2]<br><b>Output:</b> [17,5,2]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N) for output</td>
      <td>Optimal: Traverse the array from right to left. Keep track of the maximum element seen so far. If the current element is greater than or equal to the max, it's a leader. Reverse the collected leaders at the end.<br><br><b>Dependencies:</b> <code>#include <algorithm></code></td>
      <td><b>Edge Cases:</b> <b>Rightmost element:</b> Always a leader.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def leaders(A: List[int], N: int) -&gt; List[int]:&#10;    ans = []&#10;    maxi = A[N - 1]&#10;    ans.append(maxi)&#10;    for i in range(N - 2, -1, -1):&#10;        if A[i] &gt;= maxi:&#10;            ans.append(A[i])&#10;            maxi = A[i]&#10;    ans.reverse()&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">20</td>
      <td rowspan="1">Arr 20 Set Matrix Zeroes<br><br></b> <a href="https://leetcode.com/problems/set-matrix-zeroes/" target="_blank">LeetCode 73</a></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> matrix = [[1,1,1],[1,0,1],[1,1,1]]<br><b>Output:</b> [[1,0,1],[0,0,0],[1,0,1]]</td>
      <td><b>Time:</b> O(N * M)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Use the first row and first column as marker arrays to save space. We need a separate variable for the first column (or row) to avoid overlapping states.</td>
      <td><b>Edge Cases:</b> <b>Zeros in first row/col:</b> Handled accurately by checking `col0` flag at the end.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def setZeroes(matrix: List[List[int]]) -&gt; None:&#10;    n, m, col0 = len(matrix), len(matrix[0]), 1&#10;    for i in range(n):&#10;        if matrix[i][0] == 0: col0 = 0&#10;        for j in range(1, m):&#10;            if matrix[i][j] == 0: matrix[i][0] = matrix[0][j] = 0&#10;    for i in range(n-1, -1, -1):&#10;        for j in range(m-1, 0, -1):&#10;            if matrix[i][0] == 0 or matrix[0][j] == 0: matrix[i][j] = 0&#10;        if col0 == 0: matrix[i][0] = 0</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">21</td>
      <td rowspan="1">Arr 21 Rotate Image<br><br></b> <a href="https://leetcode.com/problems/rotate-image/" target="_blank">LeetCode 48</a></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> matrix = [[1,2,3],[4,5,6],[7,8,9]]<br><b>Output:</b> [[7,4,1],[8,5,2],[9,6,3]]</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Transpose the matrix (swap matrix[i][j] with matrix[j][i]), then reverse every row.<br><br><b>Dependencies:</b> <code>#include <algorithm></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def rotate(matrix: List[List[int]]) -&gt; None:&#10;    n = len(matrix)&#10;    for i in range(n):&#10;        for j in range(i):&#10;            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]&#10;    for i in range(n):&#10;        matrix[i].reverse()</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">22</td>
      <td rowspan="1">Arr 22 Spiral Matrix<br><br></b> <a href="https://leetcode.com/problems/spiral-matrix/" target="_blank">LeetCode 54</a></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> matrix = [[1,2,3],[4,5,6],[7,8,9]]<br><b>Output:</b> [1,2,3,6,9,8,7,4,5]</td>
      <td><b>Time:</b> O(N * M)<br><b>Space:</b> O(N * M) for output</td>
      <td>Optimal: Maintain 4 pointers: top, bottom, left, right. Traverse Top row, Right col, Bottom row, Left col, shrinking boundaries inwards.</td>
      <td><b>Edge Cases:</b> <b>Single row/col matrix:</b> Internal boundary checks prevent duplicate counting.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def spiralOrder(matrix: List[List[int]]) -&gt; List[int]:&#10;    ans = []&#10;    top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1&#10;    while top &lt;= bottom and left &lt;= right:&#10;        for i in range(left, right+1): ans.append(matrix[top][i])&#10;        top += 1&#10;        for i in range(top, bottom+1): ans.append(matrix[i][right])&#10;        right -= 1&#10;        if top &lt;= bottom:&#10;            for i in range(right, left-1, -1): ans.append(matrix[bottom][i])&#10;            bottom -= 1&#10;        if left &lt;= right:&#10;            for i in range(bottom, top-1, -1): ans.append(matrix[i][left])&#10;            left += 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">23</td>
      <td rowspan="1">Arr 23 4Sum<br><br></b> <a href="https://leetcode.com/problems/4sum/" target="_blank">LeetCode 18</a></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> nums = [1,0,-1,0,-2,2], target = 0<br><b>Output:</b> [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]</td>
      <td><b>Time:</b> O(N^3)<br><b>Space:</b> O(1) auxiliary</td>
      <td>Optimal: Sort array. Use 2 nested loops (i, j) for the first two numbers, and Two Pointers (k, l) for the remaining two. Skip duplicates carefully.<br><br><b>Dependencies:</b> <code>#include <algorithm></code></td>
      <td><b>Edge Cases:</b> <b>Integer Overflow:</b> Use `long long` when computing sum of 4 integers.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def fourSum(nums: List[int], target: int) -&gt; List[List[int]]:&#10;    ans = []&#10;    n = len(nums); nums.sort()&#10;    for i in range(n):&#10;        if i &gt; 0 and nums[i] == nums[i-1]: continue&#10;        for j in range(i+1, n):&#10;            if j &gt; i+1 and nums[j] == nums[j-1]: continue&#10;            k, l = j+1, n-1&#10;            while k &lt; l:&#10;                total = nums[i] + nums[j] + nums[k] + nums[l]&#10;                if total == target:&#10;                    ans.append([nums[i], nums[j], nums[k], nums[l]])&#10;                    k += 1; l -= 1&#10;                    while k &lt; l and nums[k] == nums[k-1]: k += 1&#10;                    while k &lt; l and nums[l] == nums[l+1]: l -= 1&#10;                elif total &lt; target: k += 1&#10;                else: l -= 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">24</td>
      <td rowspan="1">Arr 24 Count Subarrays With Given Xor K<br><br></b> <a href="https://www.interviewbit.com/problems/subarray-with-given-xor/" target="_blank">InterviewBit</a></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> A = [4, 2, 2, 6, 4], B = 6<br><b>Output:</b> 4</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Optimal: Use a Hash Map to store the frequency of prefix XORs. For each element, current XOR `xr ^= A[i]`. We need `xr ^ B`. If it exists in map, add its frequency to count.<br><br><b>Dependencies:</b> <code>#include <unordered_map></code></td>
      <td><b>Edge Cases:</b> <b>XOR exactly equals B:</b> Insert `mpp[0] = 1` initially to cover subarrays starting from index 0.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def solve(A: List[int], B: int) -&gt; int:&#10;    mpp = {0: 1}&#10;    xr = count = 0&#10;    for num in A:&#10;        xr ^= num&#10;        x = xr ^ B&#10;        if x in mpp: count += mpp[x]&#10;        mpp[xr] = mpp.get(xr, 0) + 1&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">25</td>
      <td rowspan="1">Arr 25 Find The Duplicate Number<br><br></b> <a href="https://leetcode.com/problems/find-the-duplicate-number/" target="_blank">LeetCode 287</a></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> nums = [1,3,4,2,2]<br><b>Output:</b> 2</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Floyd's Tortoise and Hare (Cycle Detection). Fast and slow pointer. Guaranteed cycle because of Pigeonhole Principle (numbers map to index ranges).</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findDuplicate(nums: List[int]) -&gt; int:&#10;    slow, fast = nums[0], nums[0]&#10;    while True:&#10;        slow = nums[slow]&#10;        fast = nums[nums[fast]]&#10;        if slow == fast: break&#10;    fast = nums[0]&#10;    while slow != fast:&#10;        slow = nums[slow]&#10;        fast = nums[fast]&#10;    return slow</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">26</td>
      <td rowspan="1">Arr 26 Find Missing And Repeating<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/find-missing-and-repeating2512/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> N = 2, Arr[] = {2, 2}<br><b>Output:</b> 2 1</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Mathematical approach. Diff = Sum_N - Sum_Arr = Missing - Repeating. SumSqDiff = SumSq_N - SumSq_Arr = Missing^2 - Repeating^2. Use formulas to solve for both.</td>
      <td><b>Edge Cases:</b> <b>Integer Overflow:</b> Summing squares of 10^5 elements exceeds 32-bit INT, requiring long long.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findTwoElement(arr: List[int], n: int) -&gt; List[int]:&#10;    S_N = (n * (n+1)) // 2&#10;    Sq_N = (n * (n+1) * (2*n+1)) // 6&#10;    S, Sq = 0, 0&#10;    for num in arr:&#10;        S += num; Sq += num * num&#10;    val1 = S_N - S # X - Y&#10;    val2 = (Sq_N - Sq) // val1 # X + Y&#10;    x = (val1 + val2) // 2&#10;    y = x - val1&#10;    return [y, x] # Repeating, Missing</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">27</td>
      <td rowspan="1">Arr 27 Merge Two Sorted Arrays Without Extra Space<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b> </b> arr1=[1,3,5,7], arr2=[0,2,6,8,9]<br><b>Output:</b> arr1=[0,1,2,3], arr2=[5,6,7,8,9]</td>
      <td><b>Time:</b> O((N+M) log(N+M))<br><b>Space:</b> O(1)</td>
      <td>Optimal: Start pointers at end of arr1 (i) and beginning of arr2 (j). Swap if arr1[i] > arr2[j]. Afterwards, individually sort arr1 and arr2. Time is bounded by sorting.<br><br><b>Dependencies:</b> <code>#include <algorithm></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def merge(arr1: List[int], arr2: List[int], n: int, m: int) -&gt; None:&#10;    left, right = n - 1, 0&#10;    while left &gt;= 0 and right &lt; m:&#10;        if arr1[left] &gt; arr2[right]:&#10;            arr1[left], arr2[right] = arr2[right], arr1[left]&#10;            left -= 1; right += 1&#10;        else: break&#10;    arr1.sort(); arr2.sort()</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">28</td>
      <td rowspan="1">Arr 28 Maximum Product Subarray<br><br></b> <a href="https://leetcode.com/problems/maximum-product-subarray/" target="_blank">LeetCode 152</a></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> nums = [2,3,-2,4]<br><b>Output:</b> 6</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Maintain prefix and suffix products. If a 0 is encountered, reset the product to 1. The max overall is the answer since negatives cancel out in pairs.<br><br><b>Dependencies:</b> <code>#include <limits.h></code></td>
      <td><b>Edge Cases:</b> <b>Odd negative numbers:</b> Checking both prefix and suffix elegantly covers the case where we drop one negative.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxProduct(nums: List[int]) -&gt; int:&#10;    pref, suff, ans = 1, 1, float(&#x27;-inf&#x27;)&#10;    n = len(nums)&#10;    for i in range(n):&#10;        if pref == 0: pref = 1&#10;        if suff == 0: suff = 1&#10;        pref *= nums[i]&#10;        suff *= nums[n-1-i]&#10;        ans = max(ans, pref, suff)&#10;    return int(ans)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">29</td>
      <td rowspan="1">Arr 29 Count Inversions<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/inversion-of-array-1587115620/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> N = 5, arr[] = {2, 4, 1, 3, 5}<br><b>Output:</b> 3</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(N) auxiliary</td>
      <td>Optimal: Merge Sort approach. While merging two sorted halves, if left[i] > right[j], it forms an inversion with all remaining elements in the left half (mid - i + 1).</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def inversionCount(arr: List[int], n: int) -&gt; int:&#10;    def merge(low, mid, high):&#10;        temp, left, right, cnt = [], low, mid + 1, 0&#10;        while left &lt;= mid and right &lt;= high:&#10;            if arr[left] &lt;= arr[right]:&#10;                temp.append(arr[left]); left += 1&#10;            else:&#10;                temp.append(arr[right]); cnt += (mid - left + 1); right += 1&#10;        while left &lt;= mid: temp.append(arr[left]); left += 1&#10;        while right &lt;= high: temp.append(arr[right]); right += 1&#10;        for i in range(low, high + 1): arr[i] = temp[i - low]&#10;        return cnt&#10;    def mergeSort(low, high):&#10;        cnt = 0&#10;        if low &gt;= high: return cnt&#10;        mid = (low + high) // 2&#10;        cnt += mergeSort(low, mid)&#10;        cnt += mergeSort(mid + 1, high)&#10;        cnt += merge(low, mid, high)&#10;        return cnt&#10;    return mergeSort(0, n - 1)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">30</td>
      <td rowspan="1">Arr 30 Reverse Pairs<br><br></b> <a href="https://leetcode.com/problems/reverse-pairs/" target="_blank">LeetCode 493</a></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> nums = [1,3,2,3,1]<br><b>Output:</b> 2</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(N)</td>
      <td>Optimal: Modified Merge Sort. Before merging, loop through left and right halves. If left[i] > 2 * right[j], increment j. Number of pairs is (j - (mid+1)).</td>
      <td><b>Edge Cases:</b> <b>Integer Overflow:</b> Use long long when doubling nums[j].<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def reversePairs(nums: List[int]) -&gt; int:&#10;    def merge(low, mid, high):&#10;        temp, left, right = [], low, mid + 1&#10;        while left &lt;= mid and right &lt;= high:&#10;            if nums[left] &lt;= nums[right]:&#10;                temp.append(nums[left]); left += 1&#10;            else: temp.append(nums[right]); right += 1&#10;        while left &lt;= mid: temp.append(nums[left]); left += 1&#10;        while right &lt;= high: temp.append(nums[right]); right += 1&#10;        for i in range(low, high + 1): nums[i] = temp[i - low]&#10;    def countPairs(low, mid, high):&#10;        right, cnt = mid + 1, 0&#10;        for i in range(low, mid + 1):&#10;            while right &lt;= high and nums[i] &gt; 2 * nums[right]: right += 1&#10;            cnt += (right - (mid + 1))&#10;        return cnt&#10;    def mergeSort(low, high):&#10;        cnt = 0&#10;        if low &gt;= high: return cnt&#10;        mid = (low + high) // 2&#10;        cnt += mergeSort(low, mid)&#10;        cnt += mergeSort(mid + 1, high)&#10;        cnt += countPairs(low, mid, high)&#10;        merge(low, mid, high)&#10;        return cnt&#10;    return mergeSort(0, len(nums) - 1)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">31</td>
      <td rowspan="1">Arr 31 Grid Unique Paths<br><br></b> <a href="https://leetcode.com/problems/unique-paths/" target="_blank">LeetCode 62</a></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> m = 3, n = 7<br><b>Output:</b> 28</td>
      <td><b>Time:</b> O(m-1)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Combinatorics approach. The total number of steps to reach the bottom-right corner is (m - 1) + (n - 1) = m + n - 2. Out of these steps, we need to choose (m - 1) downward steps (or n - 1 rightward steps). The number of paths is (m + n - 2) C (m - 1).</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def uniquePaths(m: int, n: int) -&gt; int:&#10;    N = n + m - 2&#10;    r = m - 1&#10;    res = 1&#10;    for i in range(1, r + 1):&#10;        res = res * (N - r + i) // i&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">32</td>
      <td rowspan="1">Arr 32 Search A 2D Matrix<br><br></b> <a href="https://leetcode.com/problems/search-a-2d-matrix/" target="_blank">LeetCode 74</a></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3<br><b>Output:</b> true</td>
      <td><b>Time:</b> O(log(m * n))<br><b>Space:</b> O(1)</td>
      <td>Optimal: Treat the 2D matrix as a 1D array and apply binary search. The element at `mid` can be accessed using `matrix[mid / cols][mid % cols]`.</td>
      <td><b>Edge Cases:</b> <b>Empty Matrix:</b> Return false.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def searchMatrix(matrix: List[List[int]], target: int) -&gt; bool:&#10;    if not matrix: return False&#10;    m, n = len(matrix), len(matrix[0])&#10;    low, high = 0, (m * n) - 1&#10;    while low &lt;= high:&#10;        mid = (low + high) // 2&#10;        if matrix[mid // n][mid % n] == target: return True&#10;        if matrix[mid // n][mid % n] &lt; target: low = mid + 1&#10;        else: high = mid - 1&#10;    return False</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">33</td>
      <td rowspan="1">Arr 33 Minimum Number Of Jumps<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b> </b> Greedy tracking bounds.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Maintain `maxReach`, `steps`, and `jumps`. At each step `i`, `maxReach = max(maxReach, i + arr[i])`. Decrement `steps`. If `steps == 0`, `jumps++` and `steps = maxReach - i`. If `i >= maxReach`, return -1.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minJumps(arr: List[int], n: int) -&gt; int:&#10;    if n &lt;= 1: return 0&#10;    if arr[0] == 0: return -1&#10;    maxReach = steps = arr[0]&#10;    jumps = 1&#10;    for i in range(1, n):&#10;        if i == n - 1: return jumps&#10;        maxReach = max(maxReach, i + arr[i])&#10;        steps -= 1&#10;        if steps == 0:&#10;            jumps += 1&#10;            if i &gt;= maxReach: return -1&#10;            steps = maxReach - i&#10;    return -1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">34</td>
      <td rowspan="1">Arr 34 Kadanes Algorithm<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b> </b> Keep tracking current sum.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Maintain `max_sum` and `curr_sum`. For each element, `curr_sum = max(element, curr_sum + element)`. `max_sum = max(max_sum, curr_sum)`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxSubarraySum(arr: List[int], n: int) -&gt; int:&#10;    maxSum = currSum = arr[0]&#10;    for i in range(1, n):&#10;        currSum = max(arr[i], currSum + arr[i])&#10;        maxSum = max(maxSum, currSum)&#10;    return maxSum</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">35</td>
      <td rowspan="1">Arr 35 Count Pairs With Given Sum<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b> </b> Hash Map.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Optimal: Use a hash map to store the frequencies of the elements seen so far. For each element `x`, check if `K - x` is in the hash map. If it is, add its frequency to the `count`. Finally, increment the frequency of `x` in the hash map.<br><br><b>Dependencies:</b> <code>#include <unordered_map></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def getPairsCount(arr: List[int], n: int, k: int) -&gt; int:&#10;    m = collections.defaultdict(int)&#10;    count = 0&#10;    for x in arr:&#10;        if k - x in m:&#10;            count += m[k - x]&#10;        m[x] += 1&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">36</td>
      <td rowspan="1">Arr 36 Common Elements In Three Sorted Arrays<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/common-elements1132/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b> </b> Three pointers.</td>
      <td><b>Time:</b> O(N1 + N2 + N3)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Use three pointers `i`, `j`, `k` for the three arrays. If `A[i] == B[j] == C[k]`, it's a common element, add it to the result (handling duplicates), and increment all three pointers. Else, increment the pointer that points to the smallest value.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def commonElements(A: List[int], B: List[int], C: List[int], n1: int, n2: int, n3: int) -&gt; List[int]:&#10;    res = []&#10;    i = j = k = 0&#10;    while i &lt; n1 and j &lt; n2 and k &lt; n3:&#10;        if A[i] == B[j] == C[k]:&#10;            if not res or res[-1] != A[i]:&#10;                res.append(A[i])&#10;            i += 1; j += 1; k += 1&#10;        elif A[i] &lt;= B[j] and A[i] &lt;= C[k]: i += 1&#10;        elif B[j] &lt;= A[i] and B[j] &lt;= C[k]: j += 1&#10;        else: k += 1&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">37</td>
      <td rowspan="1">Arr 37 Rearrange Array Alternately<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/rearrange-array-alternately-1587115620/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b> </b> Math-based encoding O(1) space.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: To achieve O(1) space, encode two values into one using `arr[i] += (arr[max_idx] % max_elem) * max_elem`. Iterate with two pointers `max_idx` and `min_idx`. At the end, divide every element by `max_elem`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def rearrange(arr, n):&#10;    min_idx, max_idx = 0, n - 1&#10;    max_elem = arr[n - 1] + 1&#10;    for i in range(n):&#10;        if i % 2 == 0:&#10;            arr[i] += (arr[max_idx] % max_elem) * max_elem&#10;            max_idx -= 1&#10;        else:&#10;            arr[i] += (arr[min_idx] % max_elem) * max_elem&#10;            min_idx += 1&#10;    for i in range(n):&#10;        arr[i] = arr[i] // max_elem</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">38</td>
      <td rowspan="1">Arr 38 Rearrange Array In Alternating Positive And Negative Items<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/array-of-alternate-ve-and--ve-nos1401/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b> </b> Extra Space Array.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Optimal: Collect all positive numbers in one array and all negative numbers in another. Overwrite the original array by picking elements alternatively from the two arrays.</td>
      <td><b>Edge Cases:</b> Unequal count of positive and negative<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def rearrange(arr, n):&#10;    pos = [x for x in arr if x &gt;= 0]&#10;    neg = [x for x in arr if x &lt; 0]&#10;    i, j, k = 0, 0, 0&#10;    while i &lt; len(pos) and j &lt; len(neg):&#10;        arr[k] = pos[i]; k += 1; i += 1&#10;        arr[k] = neg[j]; k += 1; j += 1&#10;    while i &lt; len(pos):&#10;        arr[k] = pos[i]; k += 1; i += 1&#10;    while j &lt; len(neg):&#10;        arr[k] = neg[j]; k += 1; j += 1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">39</td>
      <td rowspan="1">Arr 39 Subarray With 0 Sum<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/subarray-with-0-sum-1587115621/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b> </b> Prefix Sum with HashSet.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Optimal: Iterate through the array and calculate the prefix sum. If the prefix sum is 0 or it already exists in a hash set, it means a subarray with sum 0 exists.<br><br><b>Dependencies:</b> Hash Set</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def subArrayExists(arr, n):&#10;    sumSet = set()&#10;    curr_sum = 0&#10;    for num in arr:&#10;        curr_sum += num&#10;        if curr_sum == 0 or curr_sum in sumSet:&#10;            return True&#10;        sumSet.add(curr_sum)&#10;    return False</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">40</td>
      <td rowspan="1">Arr 40 Factorial Of A Large Number<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/factorials-of-large-numbers2508/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b> </b> Array based multiplication.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N log(N!))</td>
      <td>Optimal: Use an array to store the result. Initially, it holds 1. Multiply the array by numbers from 2 to N. The multiplication is done school-style by carrying over remainders to the next index.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def factorial(N):&#10;    # Python handles large integers automatically&#10;    import math&#10;    fact = math.factorial(N)&#10;    return [int(x) for x in str(fact)]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">41</td>
      <td rowspan="1">Arr 41 Maximum Product Subarray<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/maximum-product-subarray3604/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b> </b> Prefix and Suffix iteration.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Iterate from left to right calculating prefix product, and right to left calculating suffix product. If either is 0, reset it to 1. The max product will be the max of all prefix and suffix products.</td>
      <td><b>Edge Cases:</b> Zero elements<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxProduct(arr, n):&#10;    max_prod = float(&#x27;-inf&#x27;)&#10;    pref, suff = 1, 1&#10;    for i in range(n):&#10;        if pref == 0: pref = 1&#10;        if suff == 0: suff = 1&#10;        pref *= arr[i]&#10;        suff *= arr[n - i - 1]&#10;        max_prod = max(max_prod, pref, suff)&#10;    return max_prod</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">42</td>
      <td rowspan="1">Arr 42 Longest Consecutive Subsequence<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/longest-consecutive-subsequence2449/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b> </b> Hash Set.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Optimal: Insert all elements into a hash set. For each element, check if `element - 1` exists. If not, it's the start of a sequence. Then increment to find consecutive elements.<br><br><b>Dependencies:</b> Hash Set</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findLongestConseqSubseq(arr, N):&#10;    s = set(arr)&#10;    longest = 0&#10;    for num in s:&#10;        if (num - 1) not in s:&#10;            curr = num&#10;            count = 1&#10;            while (curr + 1) in s:&#10;                curr += 1&#10;                count += 1&#10;            longest = max(longest, count)&#10;    return longest</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">43</td>
      <td rowspan="1">Arr 43 Minimum Swaps And K Together<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/minimum-swaps-required-to-bring-all-elements-less-than-or-equal-to-k-together4847/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b> </b> Sliding Window.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: First count all elements <= k (let's say `cnt`). This will be the window size. Find elements > k in the first window. Then slide the window, updating the number of elements > k. The minimum among all windows is the answer.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minSwap(arr, n, k):&#10;    cnt = sum(1 for x in arr if x &lt;= k)&#10;    bad = sum(1 for i in range(cnt) if arr[i] &gt; k)&#10;    ans = bad&#10;    for i in range(n - cnt):&#10;        if arr[i] &gt; k: bad -= 1&#10;        if arr[i + cnt] &gt; k: bad += 1&#10;        ans = min(ans, bad)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">44</td>
      <td rowspan="1">Arr 44 Greedy 05 Fractional Knapsack<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b> </b> Sort by value/weight ratio.</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Sort items in descending order of value/weight ratio. Greedily pick items with the highest ratio first. If an item cannot fit completely, take the fraction that fits.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class Item:&#10;    def __init__(self,val,w):&#10;        self.value = val&#10;        self.weight = w&#10;&#10;def fractionalKnapsack(W, arr, n):&#10;    arr.sort(key=lambda x: x.value / x.weight, reverse=True)&#10;    finalValue = 0.0&#10;    for item in arr:&#10;        if W &gt;= item.weight:&#10;            finalValue += item.value&#10;            W -= item.weight&#10;        else:&#10;            finalValue += item.value * (W / item.weight)&#10;            break&#10;    return finalValue</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">45</td>
      <td rowspan="1">Arr 45 Greedy 06 Choose And Swap<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/choose-and-swap0531/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b> </b> Track first occurrences.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Store the first occurrence index of all characters. Iterate the string, for each character check if there is a lexicographically smaller character that appears later in the string. If so, swap them and break.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def chooseandswap(a):&#10;    s = set(a)&#10;    for i in range(len(a)):&#10;        if a[i] in s: s.remove(a[i])&#10;        if not s: break&#10;        min_char = min(s)&#10;        if min_char &lt; a[i]:&#10;            ch1, ch2 = a[i], min_char&#10;            a = a.replace(ch1, &#x27;#&#x27;)&#10;            a = a.replace(ch2, ch1)&#10;            a = a.replace(&#x27;#&#x27;, ch2)&#10;            break&#10;    return a</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">46</td>
      <td rowspan="1">Arr 46 Greedy 07 Maximum Trains For Which Stoppage Can Be Provided<br><br></b> <a href="https://www.geeksforgeeks.org/maximum-trains-stoppage-can-provided/" target="_blank">GFG</a></td>
      <td rowspan="1"><b> </b> Activity Selection on each platform.</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(N)</td>
      <td>Optimal: Group trains by platform. For each platform, this reduces to the Activity Selection Problem. Sort the trains by departure time and greedily pick non-overlapping trains.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxStop(trains, n, m):&#10;    platforms = [[] for _ in range(m + 1)]&#10;    for arr, dep, plat in trains:&#10;        platforms[plat].append((dep, arr))&#10;    count = 0&#10;    for i in range(1, m + 1):&#10;        if not platforms[i]: continue&#10;        platforms[i].sort()&#10;        count += 1&#10;        lastDep = platforms[i][0][0]&#10;        for j in range(1, len(platforms[i])):&#10;            if platforms[i][j][1] &gt;= lastDep:&#10;                count += 1&#10;                lastDep = platforms[i][j][0]&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">47</td>
      <td rowspan="1">Arr 47 Greedy 08 Minimum Platforms<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b> </b> Sort arrival and departure times separately.</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Sort arrival and departure arrays separately. Use two pointers, one for arrival and one for departure. If arrival < departure, a platform is needed, so increment count. If arrival >= departure, a platform is freed, so decrement count. Track the maximum count.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findPlatform(arr, dep, n):&#10;    arr.sort()&#10;    dep.sort()&#10;    plat_needed, result = 1, 1&#10;    i, j = 1, 0&#10;    while i &lt; n and j &lt; n:&#10;        if arr[i] &lt;= dep[j]:&#10;            plat_needed += 1&#10;            i += 1&#10;        else:&#10;            plat_needed -= 1&#10;            j += 1&#10;        result = max(result, plat_needed)&#10;    return result</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">48</td>
      <td rowspan="1">Arr 48 Greedy 09 Buy Maximum Stocks If I Stocks Can Be Bought On I Th Day<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/buy-maximum-stocks-if-i-stocks-can-be-bought-on-i-th-day/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b> </b> Sort by price.</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(N)</td>
      <td>Optimal: Store pairs of (price, day). Sort by price. Greedily buy as many stocks as possible on the day with the lowest price, bounded by the maximum allowed on that day (which is 'day') and the remaining money.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def buyMaximumProducts(n, k, price):&#10;    v = [(price[i], i + 1) for i in range(n)]&#10;    v.sort()&#10;    ans = 0&#10;    for p, d in v:&#10;        amount = min(d, k // p)&#10;        ans += amount&#10;        k -= amount * p&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">49</td>
      <td rowspan="1">Arr 49 Greedy 10 Shop In Candy Store<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/shop-in-candy-store1145/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b> </b> Sort and pick from ends.</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Sort the candies by price. For minimum cost, buy the cheapest and take K most expensive for free. For maximum cost, buy the most expensive and take K cheapest for free.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def candyStore(candies, N, K):&#10;    candies.sort()&#10;    minCost, maxCost = 0, 0&#10;    i, j = 0, N - 1&#10;    while i &lt;= j:&#10;        minCost += candies[i]&#10;        i += 1; j -= K&#10;    i, j = N - 1, 0&#10;    while j &lt;= i:&#10;        maxCost += candies[i]&#10;        i -= 1; j += K&#10;    return [minCost, maxCost]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">50</td>
      <td rowspan="1">Arr 50 Greedy 11 Minimize Cash Flow Among A Given Set Of Friends Who Have Borrowed Money From Each Other<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/minimize-cash-flow/0" target="_blank">GFG</a></td>
      <td rowspan="1"><b> </b> Net amounts.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N)</td>
      <td>Optimal: Calculate the net amount for each person by subtracting incoming debts from outgoing debts. Find the person with maximum net credit and maximum net debit. Settle their amounts, and repeat recursively or iteratively until all net amounts are zero.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minCashFlow(graph, n):&#10;    amount = [0] * n&#10;    for p in range(n):&#10;        for i in range(n):&#10;            amount[p] += (graph[i][p] - graph[p][i])&#10;    ans = [[0]*n for _ in range(n)]&#10;    def rec(amount):&#10;        mxCredit = amount.index(max(amount))&#10;        mxDebit = amount.index(min(amount))&#10;        if amount[mxCredit] == 0 and amount[mxDebit] == 0: return&#10;        minVal = min(-amount[mxDebit], amount[mxCredit])&#10;        amount[mxCredit] -= minVal&#10;        amount[mxDebit] += minVal&#10;        ans[mxDebit][mxCredit] = minVal&#10;        rec(amount)&#10;    rec(amount)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">51</td>
      <td rowspan="1">Arr 51 Greedy 12 Minimum Cost To Cut A Board Into Squares<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/minimum-cost-to-cut-a-board-into-squares/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b> </b> Sort costs.</td>
      <td><b>Time:</b> O(M log M + N log N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Sort all vertical and horizontal cuts in descending order. Maintain counts of horizontal and vertical pieces. Greedily pick the cut with the highest cost. If a horizontal cut is made, its total cost is `cut_cost * vertical_pieces`. Update the counts.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minimumCostOfBreaking(X, Y, M, N):&#10;    X.sort(reverse=True)&#10;    Y.sort(reverse=True)&#10;    hzntl, vert = 1, 1&#10;    i, j, res = 0, 0, 0&#10;    while i &lt; M - 1 and j &lt; N - 1:&#10;        if X[i] &gt; Y[j]:&#10;            res += X[i] * vert&#10;            hzntl += 1; i += 1&#10;        else:&#10;            res += Y[j] * hzntl&#10;            vert += 1; j += 1&#10;    while i &lt; M - 1:&#10;        res += X[i] * vert; i += 1&#10;    while j &lt; N - 1:&#10;        res += Y[j] * hzntl; j += 1&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">52</td>
      <td rowspan="1">Arr 52 Greedy 13 Survival On Island<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/check-if-it-is-possible-to-survive-on-island4922/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b> </b> Math.</td>
      <td><b>Time:</b> O(1)<br><b>Space:</b> O(1)</td>
      <td>Optimal: If total required food > max food you can buy in S days excluding Sundays, return -1. Else, total required food is `S * M`. Minimum days = `ceil((S * M) / N)`. Also handle the edge case where `N < M` or if survival > 6 days and `(N * 6) < (M * 7)`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import math&#10;def minimumDays(S, N, M):&#10;    if M &gt; N: return -1&#10;    if S &gt; 6 and (N * 6) &lt; (M * 7): return -1&#10;    return math.ceil((S * M) / N)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">53</td>
      <td rowspan="1">Arr 53 Greedy 14 Maximum Meetings In One Room<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/maximum-meetings-in-one-room/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b> </b> Activity Selection.</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(N)</td>
      <td>Optimal: Store `(start, end, index)`. Sort by end time. Pick the first meeting. For subsequent meetings, if `start > last_picked_end`, pick it and update `last_picked_end`. Return sorted indices.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxMeetings(N, S, F):&#10;    m = [(S[i], F[i], i + 1) for i in range(N)]&#10;    m.sort(key=lambda x: (x[1], x[2]))&#10;    ans = [m[0][2]]&#10;    last_e = m[0][1]&#10;    for i in range(1, N):&#10;        if m[i][0] &gt; last_e:&#10;            ans.append(m[i][2])&#10;            last_e = m[i][1]&#10;    ans.sort()&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">54</td>
      <td rowspan="1">Arr 54 Trapping Rain Water<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/trapping-rain-water-1587115621/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b> </b> Two Pointers.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Use two pointers, left and right. Maintain left_max and right_max. If `arr[left] <= arr[right]`, the water trapped depends on left_max. If `arr[left] > left_max`, update left_max, else add `left_max - arr[left]` to answer and increment left. Repeat for right.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def trappingWater(arr, n):&#10;    left, right = 0, n - 1&#10;    left_max, right_max = 0, 0&#10;    res = 0&#10;    while left &lt;= right:&#10;        if arr[left] &lt;= arr[right]:&#10;            if arr[left] &gt;= left_max: left_max = arr[left]&#10;            else: res += left_max - arr[left]&#10;            left += 1&#10;        else:&#10;            if arr[right] &gt;= right_max: right_max = arr[right]&#10;            else: res += right_max - arr[right]&#10;            right -= 1&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">55</td>
      <td rowspan="1">Arr 55 Chocolate Distribution Problem<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/chocolate-distribution-problem3825/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b> </b> Sort and Slide.</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Sort the array. Find the minimum difference between `A[i+M-1]` and `A[i]` for all possible `i` from `0` to `N-M`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findMinDiff(a, n, m):&#10;    a.sort()&#10;    min_diff = float(&#x27;inf&#x27;)&#10;    for i in range(n - m + 1):&#10;        diff = a[i + m - 1] - a[i]&#10;        if diff &lt; min_diff:&#10;            min_diff = diff&#10;    return min_diff</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">56</td>
      <td rowspan="1">Arr 56 Smallest Subarray With Sum Greater Than X<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/smallest-subarray-with-sum-greater-than-x5651/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b> </b> Sliding Window.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Use a sliding window. Add elements to `curr_sum` and increment `end`. When `curr_sum > x`, update `min_len` and subtract `arr[start]`, increment `start`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def smallestSubWithSum(arr, n, x):&#10;    curr_sum = 0&#10;    min_len = n + 1&#10;    start, end = 0, 0&#10;    while end &lt; n:&#10;        while curr_sum &lt;= x and end &lt; n:&#10;            curr_sum += arr[end]&#10;            end += 1&#10;        while curr_sum &gt; x and start &lt; n:&#10;            min_len = min(min_len, end - start)&#10;            curr_sum -= arr[start]&#10;            start += 1&#10;    return 0 if min_len == n + 1 else min_len</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">57</td>
      <td rowspan="1">Arr 57 Three Way Partitioning<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/three-way-partitioning/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b> </b> Dutch National Flag algorithm.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Use three pointers: `low`, `mid`, `high`. If `arr[mid] < a`, swap `arr[low]` and `arr[mid]`, increment both. If `arr[mid] > b`, swap `arr[mid]` and `arr[high]`, decrement `high`. Else increment `mid`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def threeWayPartition(array, a, b):&#10;    low, mid, high = 0, 0, len(array) - 1&#10;    while mid &lt;= high:&#10;        if array[mid] &lt; a:&#10;            array[low], array[mid] = array[mid], array[low]&#10;            low += 1&#10;            mid += 1&#10;        elif array[mid] &gt; b:&#10;            array[mid], array[high] = array[high], array[mid]&#10;            high -= 1&#10;        else:&#10;            mid += 1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">58</td>
      <td rowspan="1">Arr 58 Palindromic Array<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/palindromic-array-1587115620/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b> </b> Check individual numbers.</td>
      <td><b>Time:</b> O(N * d)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Iterate through each number in the array. For each number, reverse its digits to check if it's a palindrome. If any number is not, return 0. If all are, return 1.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def PalinArray(arr, n):&#10;    for num in arr:&#10;        if str(num) != str(num)[::-1]:&#10;            return 0&#10;    return 1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">59</td>
      <td rowspan="1">Arr 59 Find The Median<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/find-the-median0527/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b> </b> Sort array.</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Sort the array. If the size is odd, the median is the middle element. If the size is even, the median is the average of the two middle elements.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def find_median(v):&#10;    v.sort()&#10;    n = len(v)&#10;    if n % 2 != 0:&#10;        return v[n // 2]&#10;    else:&#10;        return (v[n // 2 - 1] + v[n // 2]) // 2</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">60</td>
      <td rowspan="1">Arr 60 Median Of Two Sorted Arrays Of Different Sizes<br><br></b> <a href="https://leetcode.com/problems/median-of-two-sorted-arrays/" target="_blank">LeetCode 4</a></td>
      <td rowspan="1"><b> </b> Binary Search.</td>
      <td><b>Time:</b> O(log(min(N, M)))<br><b>Space:</b> O(1)</td>
      <td>Optimal: Use Binary Search on the smaller array. Partition both arrays such that the number of elements on the left side is equal to or one more than the right side. Check if `maxLeftX <= minRightY` and `maxLeftY <= minRightX`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findMedianSortedArrays(nums1, nums2):&#10;    if len(nums1) &gt; len(nums2): return findMedianSortedArrays(nums2, nums1)&#10;    x, y = len(nums1), len(nums2)&#10;    low, high = 0, x&#10;    while low &lt;= high:&#10;        partitionX = (low + high) // 2&#10;        partitionY = (x + y + 1) // 2 - partitionX&#10;        maxLeftX = float(&#x27;-inf&#x27;) if partitionX == 0 else nums1[partitionX - 1]&#10;        minRightX = float(&#x27;inf&#x27;) if partitionX == x else nums1[partitionX]&#10;        maxLeftY = float(&#x27;-inf&#x27;) if partitionY == 0 else nums2[partitionY - 1]&#10;        minRightY = float(&#x27;inf&#x27;) if partitionY == y else nums2[partitionY]&#10;        if maxLeftX &lt;= minRightY and maxLeftY &lt;= minRightX:&#10;            if (x + y) % 2 == 0:&#10;                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0&#10;            else:&#10;                return max(maxLeftX, maxLeftY)&#10;        elif maxLeftX &gt; minRightY:&#10;            high = partitionX - 1&#10;        else:&#10;            low = partitionX + 1&#10;    return 0.0</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">61</td>
      <td rowspan="1">Arr 61 Count More Than N K Occurences<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/count-element-occurences/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b> </b> HashMap.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Optimal: Store the frequencies of all elements in a hash map. Iterate through the hash map and count the number of elements having frequency greater than `N/k`.<br><br><b>Dependencies:</b> Hash Map</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def countOccurence(arr, n, k):&#10;    count = collections.Counter(arr)&#10;    res = 0&#10;    target = n // k&#10;    for key, val in count.items():&#10;        if val &gt; target:&#10;            res += 1&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">62</td>
      <td rowspan="1">Arr 62 Find The Missing Number<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/missing-number-in-array1416/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b> </b> Sum formula.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Calculate the sum of first N natural numbers using `N*(N+1)/2`. Subtract the sum of all elements in the array from it. The result is the missing number.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def missingNumber(array, n):&#10;    return n * (n + 1) // 2 - sum(array)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">63</td>
      <td rowspan="1">Arr 63 Max Sum In Sub Arrays<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/max-sum-in-sub-arrays0824/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b> </b> Adjacent pairs sum.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: The maximum sum of two smallest elements in any subarray will always be the maximum sum of adjacent elements. So, just iterate and find the max of `arr[i] + arr[i+1]`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def pairWithMaxSum(arr, N):&#10;    maxi = 0&#10;    for i in range(N - 1):&#10;        maxi = max(maxi, arr[i] + arr[i+1])&#10;    return maxi</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">64</td>
      <td rowspan="1">Arr 64 Longest Subarray With Sum K Positives<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b> </b> Sliding Window / Two Pointers.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Since all elements are positive, use two pointers (sliding window). Expand `right` and add to sum. If sum > K, shrink `left` and subtract from sum. If sum == K, update max length.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def lenOfLongSubarr(A, N, K):&#10;    left, sum_val, max_len = 0, 0, 0&#10;    for right in range(N):&#10;        sum_val += A[right]&#10;        while sum_val &gt; K and left &lt;= right:&#10;            sum_val -= A[left]&#10;            left += 1&#10;        if sum_val == K:&#10;            max_len = max(max_len, right - left + 1)&#10;    return max_len</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">65</td>
      <td rowspan="1">Arr 65 Merge Sorted Array Without Extra Space<br><br></b> <a href="https://leetcode.com/problems/merge-sorted-array/" target="_blank">LeetCode 88</a></td>
      <td rowspan="1"><b> </b> Two pointers from end.</td>
      <td><b>Time:</b> O(M + N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Since `nums1` has enough space at the end, use three pointers: `p1` at the end of valid elements in `nums1` (m-1), `p2` at the end of `nums2` (n-1), and `p` at the very end of `nums1` (m+n-1). Compare elements at `p1` and `p2`, put the larger one at `p`, and decrement pointers.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def merge(nums1, m, nums2, n):&#10;    p1, p2, p = m - 1, n - 1, m + n - 1&#10;    while p1 &gt;= 0 and p2 &gt;= 0:&#10;        if nums1[p1] &gt; nums2[p2]:&#10;            nums1[p] = nums1[p1]&#10;            p1 -= 1&#10;        else:&#10;            nums1[p] = nums2[p2]&#10;            p2 -= 1&#10;        p -= 1&#10;    while p2 &gt;= 0:&#10;        nums1[p] = nums2[p2]&#10;        p -= 1&#10;        p2 -= 1</code></pre></details></td>
    </tr>
  </tbody>
</table>


## Hashing

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
      <td rowspan="2">1</td>
      <td rowspan="2">Hash 01 Count Frequencies<br><br></b> <a href="https://www.geeksforgeeks.org/problems/frequency-of-array-elements-1587115620/1" target="_blank">GeeksforGeeks</a></td>
      <td rowspan="2"><b> </b> <br><b>Input:</b> arr = [10, 5, 10, 15, 10, 5]<br><b>Output:</b> 10->3, 5->2, 15->1<br><br><b> </b> 1 &le; N &le; 10<sup>5</sup></td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N)</td>
      <td><b>Approach 1:</b><br>Brute Force: Use two nested loops to count frequency of each element, marking visited ones.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def countFreq(arr):&#10;    n = len(arr)&#10;    visited = [False] * n&#10;    for i in range(n):&#10;        if visited[i]: continue&#10;        count = 1&#10;        for j in range(i+1, n):&#10;            if arr[i] == arr[j]:&#10;                visited[j] = True&#10;                count += 1&#10;        print(arr[i], count)</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(N<sup>2</sup>) (Trade-off)<br><b>Space:</b> O(N) (Trade-off)</td>
      <td><b>Approach 2:</b><br>Optimal: Use two nested loops to count occurrences. Mark visited elements to avoid recounting.</td>
      <td><b>Edge Cases:</b> <b>Marking Checked:</b> Requires mutating array or extra boolean array to track checked elements.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def count_freq(arr: list[int]) -&gt; None:\n    freq = {}\n    for num in arr:\n        freq[num] = freq.get(num, 0) + 1\n    for key, val in freq.items():\n        print(f&#x27;{key} {val}&#x27;)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">2</td>
      <td rowspan="1">Hash 02 Highest Lowest Frequency<br><br></b> <a href="https://leetcode.com/problems/sort-array-by-increasing-frequency/" target="_blank">LeetCode 1636</a></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> arr = [10, 5, 10, 15, 10, 5]<br><b>Output:</b> Highest=10, Lowest=15<br><br><b> </b> 1 &le; N &le; 10<sup>5</sup></td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(N) (Trade-off)</td>
      <td>Optimal: Build a frequency map, then iterate through the map to find the max and min frequencies.<br><br><b>Dependencies:</b> <code>std::unordered_map</code></td>
      <td><b>Edge Cases:</b> <b>Initialization:</b> Set min_freq to `INT_MAX` properly to allow map values to overwrite it.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def find_high_low_freq(arr: list[int]) -&gt; tuple:&#10;    freq = {}&#10;    for num in arr:&#10;        freq[num] = freq.get(num, 0) + 1&#10;    &#10;    max_f, min_f = 0, float(&#x27;inf&#x27;)&#10;    max_ele, min_ele = 0, 0&#10;    &#10;    for ele, count in freq.items():&#10;        if count &gt; max_f:&#10;            max_f, max_ele = count, ele&#10;        if count &lt; min_f:&#10;            min_f, min_ele = count, ele&#10;    return max_ele, min_ele</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">3</td>
      <td rowspan="2">Hash 03 Intersection Of Two Arrays<br><br></b> <a href="https://leetcode.com/problems/intersection-of-two-arrays/" target="_blank">LeetCode 349</a></td>
      <td rowspan="2"><b> </b> <br><b>Input:</b> nums1 = [1,2,2,1], nums2 = [2,2]<br><b>Output:</b> [2]<br><br><b> </b> 1 &le; N, M &le; 1000</td>
      <td><b>Time:</b> O(N * M)<br><b>Space:</b> O(min(N, M))</td>
      <td><b>Approach 1:</b><br>Brute Force: Iterate through the first array and check each element in the second array.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def intersection(nums1, nums2):&#10;    res = []&#10;    for x in nums1:&#10;        if x in nums2 and x not in res:&#10;            res.append(x)&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(N + M) (Constraint)<br><b>Space:</b> O(N) (Trade-off)</td>
      <td><b>Approach 2:</b><br>Optimal: Store elements of the first array in a Hash Set, then iterate over the second array to find matches.<br><br><b>Dependencies:</b> <code>std::unordered_set</code> / <code>set()</code></td>
      <td><b>Edge Cases:</b> <b>Duplicate Match Prevention:</b> Erase matched elements from the set immediately to prevent duplicate intersections.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def intersection(nums1: list[int], nums2: list[int]) -&gt; list[int]:&#10;    set1 = set(nums1)&#10;    res = []&#10;    for num in nums2:&#10;        if num in set1:&#10;            res.append(num)&#10;            set1.remove(num) # Ensure uniqueness&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">4</td>
      <td rowspan="1">Hash 04 Union Of Two Arrays<br><br></b> <a href="https://www.geeksforgeeks.org/problems/union-of-two-arrays3538/1" target="_blank">GeeksforGeeks</a></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> a = [1, 2, 3], b = [2, 3, 4]<br><b>Output:</b> [1, 2, 3, 4]<br><br><b> </b> Arrays may not be sorted.</td>
      <td><b>Time:</b> O(N + M) (Constraint)<br><b>Space:</b> O(N + M) (Trade-off)</td>
      <td>Optimal: Insert all elements from both arrays into a Hash Set. The Set natively drops duplicates.<br><br><b>Dependencies:</b> <code>std::unordered_set</code> / <code>set()</code></td>
      <td><b>Edge Cases:</b> <b>Unordered Limitation:</b> If the problem expects sorted union, `std::set` must be used increasing time to `O((N+M)log(N+M))`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def find_union(a: list[int], b: list[int]) -&gt; list[int]:&#10;    # Set union operator implicitly merges and drops duplicates&#10;    s = set(a) | set(b)&#10;    return list(s)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">5</td>
      <td rowspan="1">Hash 05 Subarray With 0 Sum<br><br></b> <a href="https://www.geeksforgeeks.org/problems/subarray-with-0-sum-1587115621/1" target="_blank">GeeksforGeeks</a></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> arr = [4, 2, -3, 1, 6]<br><b>Output:</b> true (2, -3, 1)<br><br><b> </b> Array contains positive and negative integers.</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(N) (Trade-off)</td>
      <td>Optimal: Use a Prefix Sum and a Hash Set. If a prefix sum repeats, or equals 0, a 0-sum subarray exists between the identical prefix sums.<br><br><b>Dependencies:</b> <code>std::unordered_set</code></td>
      <td><b>Edge Cases:</b> <b>Zero Prefix Edge Case:</b> If `sum == 0` during traversal, the subarray naturally started from index 0.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def has_zero_sum_subarray(arr: list[int]) -&gt; bool:&#10;    prefix_sums = set()&#10;    curr_sum = 0&#10;    for num in arr:&#10;        curr_sum += num&#10;        if curr_sum == 0 or curr_sum in prefix_sums:&#10;            return True&#10;        prefix_sums.add(curr_sum)&#10;    return False</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">6</td>
      <td rowspan="2">Hash 06 Subarray Sum Equals K<br><br></b> <a href="https://leetcode.com/problems/subarray-sum-equals-k/" target="_blank">LeetCode 560</a></td>
      <td rowspan="2"><b> </b> <br><b>Input:</b> nums = [1,1,1], k = 2<br><b>Output:</b> 2<br><br><b> </b> Negative numbers allowed, preventing pure Sliding Window approaches.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(1)</td>
      <td><b>Approach 1:</b><br>Brute Force: Generate all possible subarrays and compute their sums.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def subarraySum(nums, k):&#10;    count = 0&#10;    for i in range(len(nums)):&#10;        current_sum = 0&#10;        for j in range(i, len(nums)):&#10;            current_sum += nums[j]&#10;            if current_sum == k:&#10;                count += 1&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(N) (Trade-off)</td>
      <td><b>Approach 2:</b><br>Optimal: Maintain a Hash Map of `prefix_sum` -> `frequency`. If `curr_sum - k` exists in the map, add its frequency to the count.<br><br><b>Dependencies:</b> <code>std::unordered_map</code></td>
      <td><b>Edge Cases:</b> <b>Base Case Injection:</b> Must initialize map with `(0, 1)` to correctly count subarrays starting natively from index 0.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def subarray_sum(nums: list[int], k: int) -&gt; int:&#10;    prefix_freq = {0: 1}&#10;    count = 0&#10;    curr_sum = 0&#10;    for num in nums:&#10;        curr_sum += num&#10;        remove = curr_sum - k&#10;        if remove in prefix_freq:&#10;            count += prefix_freq[remove]&#10;        prefix_freq[curr_sum] = prefix_freq.get(curr_sum, 0) + 1&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">7</td>
      <td rowspan="1">Hash 07 Longest Subarray With 0 Sum<br><br></b> <a href="https://www.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1" target="_blank">GeeksforGeeks</a></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> arr = [15,-2,2,-8,1,7,10,23]<br><b>Output:</b> 5<br><br><b> </b> 1 &le; N &le; 10<sup>5</sup></td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(N) (Trade-off)</td>
      <td>Optimal: Store `prefix_sum` -> `index` in Hash Map. If sum repeats, calculate distance `i - hash[sum]`.<br><br><b>Dependencies:</b> <code>std::unordered_map</code></td>
      <td><b>Edge Cases:</b> <b>Longest Policy:</b> We only insert `sum` into the map if it doesn't exist to preserve the earliest index and maximize distance.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def max_len(arr: list[int]) -&gt; int:&#10;    prefix_index = {}&#10;    max_len = sum = 0&#10;    for i, num in enumerate(arr):&#10;        sum += num&#10;        if sum == 0:&#10;            max_len = i + 1&#10;        elif sum in prefix_index:&#10;            max_len = max(max_len, i - prefix_index[sum])&#10;        else:&#10;            prefix_index[sum] = i&#10;    return max_len</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">8</td>
      <td rowspan="1">Hash 08 Longest Subarray With Sum K<br><br></b> <a href="https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1" target="_blank">GeeksforGeeks</a></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> arr = [10, 5, 2, 7, 1, 9], k = 15<br><b>Output:</b> 4<br><br><b> </b> 1 &le; N &le; 10<sup>5</sup></td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(N) (Trade-off)</td>
      <td>Optimal: Prefix Sum Map storing indices. Check if `sum - K` exists in map and calculate index difference.<br><br><b>Dependencies:</b> <code>std::unordered_map</code></td>
      <td><b>Edge Cases:</b> <b>Zero Elements Rule:</b> Never overwrite existing prefix sums in the map, otherwise arrays with zero elements will shorten the max length.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def len_of_long_subarr(arr: list[int], k: int) -&gt; int:&#10;    prefix_index = {}&#10;    max_len = sum = 0&#10;    for i, num in enumerate(arr):&#10;        sum += num&#10;        if sum == k:&#10;            max_len = i + 1&#10;        needed = sum - k&#10;        if needed in prefix_index:&#10;            max_len = max(max_len, i - prefix_index[needed])&#10;        if sum not in prefix_index:&#10;            prefix_index[sum] = i&#10;    return max_len</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">9</td>
      <td rowspan="1">Hash 09 Two Sum<br><br></b> <a href="https://leetcode.com/problems/two-sum/" target="_blank">LeetCode 1</a></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> nums = [2,7,11,15], target = 9<br><b>Output:</b> [0,1]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Optimal: Iterate while storing numbers and their indices in a hash map. Check if `target - num` already exists.<br><br><b>Dependencies:</b> <code>std::unordered_map</code></td>
      <td><b>Edge Cases:</b> <b>Duplicate Elements:</b> Storing elements as we iterate safely handles duplicates (e.g., target 6, array [3,3]).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def twoSum(nums: list[int], target: int) -&gt; list[int]:&#10;    mpp = {}&#10;    for i, num in enumerate(nums):&#10;        needed = target - num&#10;        if needed in mpp:&#10;            return [mpp[needed], i]&#10;        mpp[num] = i&#10;    return []</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">10</td>
      <td rowspan="1">Hash 10 Group Anagrams<br><br></b> <a href="https://leetcode.com/problems/group-anagrams/" target="_blank">LeetCode 49</a></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> strs = ["eat","tea","tan","ate","nat","bat"]<br><b>Output:</b> [["bat"],["nat","tan"],["ate","eat","tea"]]</td>
      <td><b>Time:</b> O(N * K log K)<br><b>Space:</b> O(N * K)</td>
      <td>Optimal: Use a hash map where the key is the sorted version of the string, and the value is a list of anagrams.<br><br><b>Dependencies:</b> <code>std::unordered_map</code>, <code>std::sort</code></td>
      <td><b>Edge Cases:</b> <b>Empty Strings:</b> Safely handled since an empty string sorted is still empty, forming a valid key.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">from collections import defaultdict&#10;def groupAnagrams(strs: list[str]) -&gt; list[list[str]]:&#10;    mpp = defaultdict(list)&#10;    for s in strs:&#10;        mpp[tuple(sorted(s))].append(s)&#10;    return list(mpp.values())</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">11</td>
      <td rowspan="2">Hash 11 Longest Consecutive Sequence<br><br></b> <a href="https://leetcode.com/problems/longest-consecutive-sequence/" target="_blank">LeetCode 128</a></td>
      <td rowspan="2"><b> </b> <br><b>Input:</b> nums = [100,4,200,1,3,2]<br><b>Output:</b> 4 (The sequence is [1, 2, 3, 4])</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(1)</td>
      <td><b>Approach 1:</b><br>Brute Force: Sort the array first, then count consecutive elements linearly.<br><br><b>Dependencies:</b> std::sort</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def longestConsecutive(nums):&#10;    if not nums: return 0&#10;    nums.sort()&#10;    longest, current = 1, 1&#10;    for i in range(1, len(nums)):&#10;        if nums[i] == nums[i-1]: continue&#10;        if nums[i] == nums[i-1] + 1:&#10;            current += 1&#10;        else:&#10;            longest = max(longest, current)&#10;            current = 1&#10;    return max(longest, current)</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(N)</td>
      <td><b>Approach 2:</b><br>Optimal: Insert all elements into a Hash Set. Iterate through elements. If `num - 1` is NOT in the set, it's the start of a sequence. Count forwards.<br><br><b>Dependencies:</b> <code>std::unordered_set</code></td>
      <td><b>Edge Cases:</b> <b>Duplicate Elements:</b> Handled automatically by the Set.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def longestConsecutive(nums: list[int]) -&gt; int:&#10;    num_set = set(nums)&#10;    max_len = 0&#10;    for num in num_set:&#10;        if num - 1 not in num_set:&#10;            curr_num = num&#10;            curr_len = 1&#10;            while curr_num + 1 in num_set:&#10;                curr_num += 1&#10;                curr_len += 1&#10;            max_len = max(max_len, curr_len)&#10;    return max_len</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">12</td>
      <td rowspan="1">Hash 12 Longest Subarray With 0 Sum<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b> </b> Hash Map.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Optimal: Maintain the prefix sum and a hash map storing the first occurrence index of each prefix sum. If sum is 0, length is `i+1`. If sum is in the map, length is `i - map[sum]`. Update max length.<br><br><b>Dependencies:</b> Hash Map</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxLen(n, arr):&#10;    m = {}&#10;    maxi, sum_val = 0, 0&#10;    for i in range(n):&#10;        sum_val += arr[i]&#10;        if sum_val == 0: maxi = i + 1&#10;        else:&#10;            if sum_val in m:&#10;                maxi = max(maxi, i - m[sum_val])&#10;            else:&#10;                m[sum_val] = i&#10;    return maxi</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">13</td>
      <td rowspan="1">Hash 13 Sort Characters By Frequency<br><br></b> <a href="https://leetcode.com/problems/sort-characters-by-frequency/" target="_blank">LeetCode 451</a></td>
      <td rowspan="1"><b> </b> Hash Map + Priority Queue / Sorting.</td>
      <td><b>Time:</b> O(N log K) where K is unique chars<br><b>Space:</b> O(K)</td>
      <td>Optimal: Count frequencies using a hash map. Add pairs `(freq, char)` to a max heap or vector and sort. Reconstruct string.<br><br><b>Dependencies:</b> Hash Map</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">from collections import Counter&#10;def frequencySort(s):&#10;    counts = Counter(s)&#10;    return &quot;&quot;.join(char * count for char, count in counts.most_common())</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">14</td>
      <td rowspan="1">Hash 14 Count Distinct Elements In Every Window<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/count-distinct-elements-in-every-window/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b> </b> Sliding Window + Hash Map.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(K)</td>
      <td>Optimal: Use a hash map to keep track of element frequencies in the window of size K. The number of distinct elements is the size of the hash map. As window slides, increment frequency of new element, decrement frequency of outgoing element. If frequency becomes 0, remove it from map.<br><br><b>Dependencies:</b> Hash Map</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def countDistinct(arr, n, k):&#10;    m = {}&#10;    ans = []&#10;    for i in range(k):&#10;        m[arr[i]] = m.get(arr[i], 0) + 1&#10;    ans.append(len(m))&#10;    for i in range(k, n):&#10;        m[arr[i - k]] -= 1&#10;        if m[arr[i - k]] == 0: del m[arr[i - k]]&#10;        m[arr[i]] = m.get(arr[i], 0) + 1&#10;        ans.append(len(m))&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">15</td>
      <td rowspan="1">Hash 15 Design Hashset<br><br></b> <a href="https://leetcode.com/problems/design-hashset/" target="_blank">LeetCode 705</a></td>
      <td rowspan="1"><b> </b> Array of Linked Lists (Chaining).</td>
      <td><b>Time:</b> O(1) average, O(N) worst case<br><b>Space:</b> O(N)</td>
      <td>Optimal: Use a large array (e.g., size 10000) of linked lists or vectors. The hash function maps `key` to `key % 10000`. To add, if not present in the bucket, append it. To remove, find and erase. To contain, iterate through bucket.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class MyHashSet:&#10;    def __init__(self):&#10;        self.size = 10000&#10;        self.buckets = [[] for _ in range(self.size)]&#10;    def add(self, key: int) -&gt; None:&#10;        i = key % self.size&#10;        if key not in self.buckets[i]:&#10;            self.buckets[i].append(key)&#10;    def remove(self, key: int) -&gt; None:&#10;        i = key % self.size&#10;        if key in self.buckets[i]:&#10;            self.buckets[i].remove(key)&#10;    def contains(self, key: int) -&gt; bool:&#10;        return key in self.buckets[key % self.size]</code></pre></details></td>
    </tr>
  </tbody>
</table>


## Strings

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
      <td rowspan="1">1</td>
      <td rowspan="1">Str 01 Valid Palindrome<br><br></b> <a href="https://leetcode.com/problems/valid-palindrome/" target="_blank">LeetCode 125</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> s = "A man, a plan, a canal: Panama"<br><b>Output:</b> true</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td>Two-pointer approach skipping non-alphanumeric characters. Compare characters from both ends.<br><br><b>Dependencies:</b> <code>std::isalnum</code>, <code>std::tolower</code></td>
      <td><b>Edge Cases:</b> <b>All Non-Alphanumeric:</b> Pointers might cross without any comparisons. Loop condition `left < right` safely handles it.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isPalindrome(s: str) -&gt; bool:&#10;    left, right = 0, len(s) - 1&#10;    while left &lt; right:&#10;        while left &lt; right and not s[left].isalnum(): left += 1&#10;        while left &lt; right and not s[right].isalnum(): right -= 1&#10;        if s[left].lower() != s[right].lower(): return False&#10;        left += 1; right -= 1&#10;    return True</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">2</td>
      <td rowspan="1">Str 02 Valid Anagram<br><br></b> <a href="https://leetcode.com/problems/valid-anagram/" target="_blank">LeetCode 242</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> s = "anagram", t = "nagaram"<br><b>Output:</b> true</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Use a frequency array of size 26. Increment for `s`, decrement for `t`. Check if all counts are 0.</td>
      <td><b>Edge Cases:</b> <b>Length Mismatch:</b> If lengths differ, return false immediately to prevent boundary issues.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isAnagram(s: str, t: str) -&gt; bool:&#10;    if len(s) != len(t): return False&#10;    freq = [0] * 26&#10;    for i in range(len(s)):&#10;        freq[ord(s[i]) - ord(&#x27;a&#x27;)] += 1&#10;        freq[ord(t[i]) - ord(&#x27;a&#x27;)] -= 1&#10;    return all(count == 0 for count in freq)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">3</td>
      <td rowspan="1">Str 03 Longest Common Prefix<br><br></b> <a href="https://leetcode.com/problems/longest-common-prefix/" target="_blank">LeetCode 14</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> strs = ["flower","flow","flight"]<br><b>Output:</b> "fl"</td>
      <td><b>Time:</b> O(N log N * M) (Constraint)<br><b>Space:</b> O(1) / O(M)</td>
      <td>Sort the array. The common prefix will be constrained by the first and last strings in the sorted array.<br><br><b>Dependencies:</b> <code>std::sort</code></td>
      <td><b>Edge Cases:</b> <b>No Match:</b> If the first character of `first` and `last` string doesn't match, loop breaks immediately, returning "".<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def longestCommonPrefix(strs: list[str]) -&gt; str:&#10;    if not strs: return &quot;&quot;&#10;    strs.sort()&#10;    first, last = strs[0], strs[-1]&#10;    i = 0&#10;    while i &lt; len(first) and i &lt; len(last) and first[i] == last[i]:&#10;        i += 1&#10;    return first[:i]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">4</td>
      <td rowspan="1">Str 04 Longest Palindromic Substring<br><br></b> <a href="https://leetcode.com/problems/longest-palindromic-substring/" target="_blank">LeetCode 5</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> s = "babad"<br><b>Output:</b> "bab"</td>
      <td><b>Time:</b> O(N<sup>2</sup>) (Constraint)<br><b>Space:</b> O(1)</td>
      <td>Expand Around Center. A palindrome can have an odd (center is 1 char) or even (center is between 2 chars) length. Test both.</td>
      <td><b>Edge Cases:</b> <b>Substr Math:</b> `start` is calculated as `i - (len - 1) / 2` to safely encompass both odd and even length centers.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def longestPalindrome(s: str) -&gt; str:&#10;    def expand(left, right):&#10;        while left &gt;= 0 and right &lt; len(s) and s[left] == s[right]:&#10;            left -= 1&#10;            right += 1&#10;        return right - left - 1&#10;        &#10;    start, max_len = 0, 0&#10;    for i in range(len(s)):&#10;        len1 = expand(i, i)&#10;        len2 = expand(i, i + 1)&#10;        l = max(len1, len2)&#10;        if l &gt; max_len:&#10;            max_len = l&#10;            start = i - (l - 1) // 2&#10;    return s[start : start + max_len]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">5</td>
      <td rowspan="1">Str 05 Kmp Algorithm<br><br></b> <a href="https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/" target="_blank">LeetCode 28</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> haystack = 'sadbutsad', needle = 'sad'<br><b>Output:</b> 0</td>
      <td><b>Time:</b> O(N + M)<br><b>Space:</b> O(M)</td>
      <td>Compute the LPS (Longest Proper Prefix which is also Suffix) array for the needle. Use the LPS array to skip characters while matching with the haystack, reducing time to O(N+M).<br><br><b>Dependencies:</b> <code>#include <vector></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def strStr(haystack: str, needle: str) -&gt; int:&#10;    if not needle: return 0&#10;    m, n = len(needle), len(haystack)&#10;    lps = [0] * m&#10;    length, i = 0, 1&#10;    while i &lt; m:&#10;        if needle[i] == needle[length]:&#10;            length += 1&#10;            lps[i] = length; i += 1&#10;        else:&#10;            if length != 0: length = lps[length - 1]&#10;            else: lps[i] = 0; i += 1&#10;    i = j = 0&#10;    while i &lt; n:&#10;        if needle[j] == haystack[i]: i += 1; j += 1&#10;        if j == m: return i - j&#10;        elif i &lt; n and needle[j] != haystack[i]:&#10;            if j != 0: j = lps[j - 1]&#10;            else: i += 1&#10;    return -1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">6</td>
      <td rowspan="1">Str 06 Rabin Karp<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/31272eef104840f7430ad9fd1d43b434a4cea159/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Return array of starting indices.</td>
      <td><b>Time:</b> O(N + M)<br><b>Space:</b> O(1)</td>
      <td>Compute hash for pattern and first window of text. Slide window: subtract leading char's hash contribution, shift, and add trailing char. If hashes match, explicitly check strings to avoid collisions.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def search(pat: str, txt: str) -&gt; List[int]:&#10;    d, q = 256, 101&#10;    m, n = len(pat), len(txt)&#10;    if m &gt; n: return []&#10;    res, p, t, h = [], 0, 0, 1&#10;    for i in range(m-1): h = (h * d) % q&#10;    for i in range(m):&#10;        p = (d * p + ord(pat[i])) % q&#10;        t = (d * t + ord(txt[i])) % q&#10;    for i in range(n - m + 1):&#10;        if p == t:&#10;            if txt[i:i+m] == pat:&#10;                res.append(i + 1)&#10;        if i &lt; n - m:&#10;            t = (d * (t - ord(txt[i]) * h) + ord(txt[i+m])) % q&#10;            if t &lt; 0: t += q&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">7</td>
      <td rowspan="1">Str 07 Reverse A String<br><br></b> <a href="https://leetcode.com/problems/reverse-string/" target="_blank">LeetCode 344</a></td>
      <td rowspan="1"><b>Example 1:</b> Two pointers swap.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Use two pointers, `left` at the beginning and `right` at the end of the string. Swap the characters at these pointers and move them towards each other until they meet.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def reverseString(s: List[str]) -&gt; None:&#10;    left, right = 0, len(s) - 1&#10;    while left &lt; right:&#10;        s[left], s[right] = s[right], s[left]&#10;        left += 1&#10;        right -= 1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">8</td>
      <td rowspan="1">Str 08 Palindrome String<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/palindrome-string0817/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Two pointers.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Use two pointers, `left` at the beginning and `right` at the end of the string. Compare the characters at these pointers. If they are different, return 0. Move pointers towards each other. If all characters match, return 1.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isPalindrome(S: str) -&gt; int:&#10;    left, right = 0, len(S) - 1&#10;    while left &lt; right:&#10;        if S[left] != S[right]:&#10;            return 0&#10;        left += 1&#10;        right -= 1&#10;    return 1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">9</td>
      <td rowspan="1">Str 09 Find Duplicate Characters In A String<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/find-duplicate-characters-in-a-string/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Frequency array or Hash Map.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Use a hash map or frequency array to count occurrences of each character. Then, iterate through the map/array and print characters with a count greater than 1.<br><br><b>Dependencies:</b> <code>#include <unordered_map></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def printDups(s: str):&#10;    count = collections.Counter(s)&#10;    for k, v in count.items():&#10;        if v &gt; 1:&#10;            print(f&quot;{k}, count = {v}&quot;)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">10</td>
      <td rowspan="1">Str 10 A Program To Check If Strings Are Rotations Of Each Other<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/check-if-strings-are-rotations-of-each-other-or-not-1587115620/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Concatenate and find.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>If the lengths are different, return false. Otherwise, concatenate `s1` with itself (`s1 + s1`). If `s2` is a rotation of `s1`, it must be a substring of the concatenated string.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def areRotations(s1: str, s2: str) -&gt; bool:&#10;    if len(s1) != len(s2): return False&#10;    return s2 in (s1 + s1)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">11</td>
      <td rowspan="1">Str 11 Check If A String Is A Valid Shuffle Of Two Distinct Strings<br><br></b> <a href="https://www.programiz.com/java-programming/examples/check-valid-shuffle-of-strings" target="_blank">Article</a></td>
      <td rowspan="1"><b>Example 1:</b> Three pointers.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>If lengths don't match, return false. Use three pointers `i`, `j`, `k` for `str1`, `str2`, and `str3`. Traverse `str3`. If `str3[k] == str1[i]`, increment `i` and `k`. Else if `str3[k] == str2[j]`, increment `j` and `k`. Else, it's not a valid shuffle. After the loop, check if both `str1` and `str2` are fully traversed.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def checkShuffle(str1: str, str2: str, str3: str) -&gt; bool:&#10;    if len(str1) + len(str2) != len(str3): return False&#10;    i, j, k = 0, 0, 0&#10;    while k &lt; len(str3):&#10;        if i &lt; len(str1) and str1[i] == str3[k]: i += 1&#10;        elif j &lt; len(str2) and str2[j] == str3[k]: j += 1&#10;        else: return False&#10;        k += 1&#10;    return i == len(str1) and j == len(str2)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">12</td>
      <td rowspan="1">Str 12 Count And Say<br><br></b> <a href="https://leetcode.com/problems/count-and-say/" target="_blank">LeetCode 38</a></td>
      <td rowspan="1"><b>Example 1:</b> Recursive generation.</td>
      <td><b>Time:</b> O(N * L) where L is max length of string<br><b>Space:</b> O(L)</td>
      <td>Start with `res = '1'`. For `n-1` times, iterate through `res` and count consecutive identical characters. Append the count and the character to a new string. Replace `res` with the new string.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def countAndSay(n: int) -&gt; str:&#10;    if n == 1: return &quot;1&quot;&#10;    s = &quot;1&quot;&#10;    for _ in range(2, n + 1):&#10;        temp = &quot;&quot;&#10;        count = 1&#10;        for j in range(1, len(s)):&#10;            if s[j] == s[j - 1]:&#10;                count += 1&#10;            else:&#10;                temp += str(count) + s[j - 1]&#10;                count = 1&#10;        temp += str(count) + s[-1]&#10;        s = temp&#10;    return s</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">13</td>
      <td rowspan="1">Str 13 Longest Palindrome In A String<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/longest-palindrome-in-a-string3411/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Expand around center.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(1)</td>
      <td>For each character, treat it as the center of an odd-length palindrome and expand outwards. Also treat it and the next character as the center of an even-length palindrome and expand outwards. Keep track of the longest palindrome found.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def longestPalindrome(S: str) -&gt; str:&#10;    start = 0; maxLen = 1; n = len(S)&#10;    for i in range(n):&#10;        l = r = i&#10;        while l &gt;= 0 and r &lt; n and S[l] == S[r]:&#10;            if r - l + 1 &gt; maxLen:&#10;                start = l; maxLen = r - l + 1&#10;            l -= 1; r += 1&#10;        l = i; r = i + 1&#10;        while l &gt;= 0 and r &lt; n and S[l] == S[r]:&#10;            if r - l + 1 &gt; maxLen:&#10;                start = l; maxLen = r - l + 1&#10;            l -= 1; r += 1&#10;    return S[start:start+maxLen]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">14</td>
      <td rowspan="1">Str 14 Find Longest Recurring Subsequence In String<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/longest-repeating-subsequence2004/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Modified LCS.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N^2) or O(N)</td>
      <td>This is a variation of Longest Common Subsequence (LCS). Find LCS of `str` with itself, but with the restriction that when characters match, their indices must not be the same (`i != j`).</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def LongestRepeatingSubsequence(str: str) -&gt; int:&#10;    n = len(str)&#10;    dp = [[0] * (n + 1) for _ in range(n + 1)]&#10;    for i in range(1, n + 1):&#10;        for j in range(1, n + 1):&#10;            if str[i-1] == str[j-1] and i != j:&#10;                dp[i][j] = 1 + dp[i-1][j-1]&#10;            else:&#10;                dp[i][j] = max(dp[i][j-1], dp[i-1][j])&#10;    return dp[n][n]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">15</td>
      <td rowspan="1">Str 15 Print All Subsequences Of A String<br><br></b> <a href="https://www.geeksforgeeks.org/print-subsequences-string/" target="_blank">Article</a></td>
      <td rowspan="1"><b>Example 1:</b> Recursive choice (include/exclude).</td>
      <td><b>Time:</b> O(2^N)<br><b>Space:</b> O(N) recursion stack</td>
      <td>Use recursion. At each character, you have two choices: either include it in the current subsequence or exclude it. When you reach the end of the string, print/store the formed subsequence.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def allSubsequences(s: str) -&gt; List[str]:&#10;    res = []&#10;    def solve(i, curr):&#10;        if i == len(s):&#10;            if curr: res.append(curr)&#10;            return&#10;        solve(i + 1, curr)&#10;        solve(i + 1, curr + s[i])&#10;    solve(0, &quot;&quot;)&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">16</td>
      <td rowspan="1">Str 16 Split The Binary String Into Substrings With Equal Number Of 0S And 1S<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/split-the-binary-string-into-substrings-with-equal-number-of-0s-and-1s/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Counter logic.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Iterate through the string, maintain a count that increments for '0' and decrements for '1' (or vice versa). Whenever the count becomes 0, it means we have found a balanced substring, so increment the answer.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxSubStr(str):&#10;    count0 = 0&#10;    count1 = 0&#10;    ans = 0&#10;    for c in str:&#10;        if c == &#x27;0&#x27;: count0 += 1&#10;        else: count1 += 1&#10;        if count0 == count1:&#10;            ans += 1&#10;    if count0 != count1: return -1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">17</td>
      <td rowspan="1">Str 17 Word Wrap<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/word-wrap1646/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> DP approach.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N)</td>
      <td>Use Dynamic Programming. `dp[i]` represents the minimum cost to wrap words from index `i` to the end. Iterate backward and try placing different numbers of words on the current line.<br><br><b>Dependencies:</b> DP</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def solveWordWrap(nums, k):&#10;    n = len(nums)&#10;    dp = [0] * n&#10;    dp[n - 1] = 0&#10;    for i in range(n - 2, -1, -1):&#10;        currlen = -1&#10;        dp[i] = float(&#x27;inf&#x27;)&#10;        for j in range(i, n):&#10;            currlen += (nums[j] + 1)&#10;            if currlen &gt; k: break&#10;            if j == n - 1:&#10;                dp[i] = 0&#10;            else:&#10;                cost = (k - currlen) ** 2 + dp[j + 1]&#10;                dp[i] = min(dp[i], cost)&#10;    return dp[0]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">18</td>
      <td rowspan="1">Str 18 Edit Distance<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/edit-distance3702/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> DP Table.</td>
      <td><b>Time:</b> O(N * M)<br><b>Space:</b> O(N * M)</td>
      <td>Create a 2D DP array. If characters match, `dp[i][j] = dp[i-1][j-1]`. If not, `dp[i][j] = 1 + min(replace, insert, delete)`.<br><br><b>Dependencies:</b> DP</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def editDistance(s, t):&#10;    n, m = len(s), len(t)&#10;    dp = [[0] * (m + 1) for _ in range(n + 1)]&#10;    for i in range(n + 1): dp[i][0] = i&#10;    for j in range(m + 1): dp[0][j] = j&#10;    for i in range(1, n + 1):&#10;        for j in range(1, m + 1):&#10;            if s[i - 1] == t[j - 1]:&#10;                dp[i][j] = dp[i - 1][j - 1]&#10;            else:&#10;                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])&#10;    return dp[n][m]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">19</td>
      <td rowspan="1">Str 19 Next Permutation<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/next-permutation5226/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Swap and Reverse.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Traverse from right to find the first element smaller than the element to its right. Then, find the smallest element to its right that is greater than it. Swap them, and reverse the subarray after the first element's index.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def nextPermutation(N, arr):&#10;    i = N - 2&#10;    while i &gt;= 0 and arr[i] &gt;= arr[i + 1]:&#10;        i -= 1&#10;    if i &gt;= 0:&#10;        j = N - 1&#10;        while arr[j] &lt;= arr[i]:&#10;            j -= 1&#10;        arr[i], arr[j] = arr[j], arr[i]&#10;    arr[i+1:] = reversed(arr[i+1:])&#10;    return arr</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">20</td>
      <td rowspan="1">Str 20 Parenthesis Checker<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/parenthesis-checker2744/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Stack approach.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Use a stack to keep track of opening brackets. If a closing bracket is encountered, check if it matches the top of the stack.<br><br><b>Dependencies:</b> Stack</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def ispar(x):&#10;    stack = []&#10;    for c in x:&#10;        if c in &#x27;({[&#x27;:&#10;            stack.append(c)&#10;        else:&#10;            if not stack: return False&#10;            if c == &#x27;)&#x27; and stack[-1] != &#x27;(&#x27;: return False&#10;            if c == &#x27;}&#x27; and stack[-1] != &#x27;{&#x27;: return False&#10;            if c == &#x27;]&#x27; and stack[-1] != &#x27;[&#x27;: return False&#10;            stack.pop()&#10;    return len(stack) == 0</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">21</td>
      <td rowspan="1">Str 21 Word Break<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/word-break1352/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> DP.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N)</td>
      <td>Use `dp[i]` to indicate if `A[0..i]` can be segmented. For each `i`, check all prefixes `A[0..j]`. If `dp[j]` is true and `A[j..i]` is in the dictionary, then `dp[i]` is true.<br><br><b>Dependencies:</b> DP, Hash Set</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def wordBreak(A, B):&#10;    word_set = set(B)&#10;    n = len(A)&#10;    dp = [False] * (n + 1)&#10;    dp[0] = True&#10;    for i in range(1, n + 1):&#10;        for j in range(i):&#10;            if dp[j] and A[j:i] in word_set:&#10;                dp[i] = True&#10;                break&#10;    return 1 if dp[n] else 0</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">22</td>
      <td rowspan="1">Str 22 Rabin Karp Algorithm<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/31272eef104840f7430ad9fd1d43b434a4b9596b/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Rolling Hash.</td>
      <td><b>Time:</b> O(N + M)<br><b>Space:</b> O(1)</td>
      <td>Compute the hash for the pattern and for the first window of text. Slide the window by removing the leading character's hash and adding the trailing character's hash. If hashes match, check the characters one by one.</td>
      <td><b>Edge Cases:</b> Collisions in Hash<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def search(pat, txt):&#10;    d, q = 256, 101&#10;    M, N = len(pat), len(txt)&#10;    p, t, h = 0, 0, 1&#10;    res = []&#10;    for i in range(M - 1): h = (h * d) % q&#10;    for i in range(M):&#10;        p = (d * p + ord(pat[i])) % q&#10;        t = (d * t + ord(txt[i])) % q&#10;    for i in range(N - M + 1):&#10;        if p == t:&#10;            match = True&#10;            for j in range(M):&#10;                if txt[i + j] != pat[j]:&#10;                    match = False&#10;                    break&#10;            if match: res.append(i + 1)&#10;        if i &lt; N - M:&#10;            t = (d * (t - ord(txt[i]) * h) + ord(txt[i + M])) % q&#10;            if t &lt; 0: t = t + q&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">23</td>
      <td rowspan="1">Str 23 Kmp Algorithm<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/search-pattern0205/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> LPS Array.</td>
      <td><b>Time:</b> O(N + M)<br><b>Space:</b> O(M)</td>
      <td>Construct an LPS (Longest Proper Prefix which is also Suffix) array for the pattern. Use it to skip unnecessary comparisons while traversing the text.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def computeLPS(pat, M, lps):&#10;    length = 0&#10;    lps[0] = 0&#10;    i = 1&#10;    while i &lt; M:&#10;        if pat[i] == pat[length]:&#10;            length += 1&#10;            lps[i] = length&#10;            i += 1&#10;        else:&#10;            if length != 0:&#10;                length = lps[length - 1]&#10;            else:&#10;                lps[i] = 0&#10;                i += 1&#10;&#10;def search(pat, txt):&#10;    M, N = len(pat), len(txt)&#10;    lps = [0] * M&#10;    computeLPS(pat, M, lps)&#10;    i, j = 0, 0&#10;    res = []&#10;    while (N - i) &gt;= (M - j):&#10;        if pat[j] == txt[i]:&#10;            j += 1; i += 1&#10;        if j == M:&#10;            res.append(i - j + 1)&#10;            j = lps[j - 1]&#10;        elif i &lt; N and pat[j] != txt[i]:&#10;            if j != 0: j = lps[j - 1]&#10;            else: i += 1&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">24</td>
      <td rowspan="1">Str 24 Convert A Sentence Into Its Equivalent Mobile Numeric Keypad Sequence<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/convert-a-sentence-into-its-equivalent-mobile-numeric-keypad-sequence0547/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Dictionary Mapping.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Store the sequence for every character in an array from A to Z, and for space. For each character in the input string, append its corresponding sequence to the result.</td>
      <td><b>Edge Cases:</b> Spaces<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def printSequence(S):&#10;    str_arr = [&quot;2&quot;, &quot;22&quot;, &quot;222&quot;, &quot;3&quot;, &quot;33&quot;, &quot;333&quot;, &quot;4&quot;, &quot;44&quot;, &quot;444&quot;, &quot;5&quot;, &quot;55&quot;, &quot;555&quot;, &quot;6&quot;, &quot;66&quot;, &quot;666&quot;, &quot;7&quot;, &quot;77&quot;, &quot;777&quot;, &quot;7777&quot;, &quot;8&quot;, &quot;88&quot;, &quot;888&quot;, &quot;9&quot;, &quot;99&quot;, &quot;999&quot;, &quot;9999&quot;]&#10;    output = &quot;&quot;&#10;    for char in S:&#10;        if char == &#x27; &#x27;: output += &quot;0&quot;&#10;        else: output += str_arr[ord(char) - ord(&#x27;A&#x27;)]&#10;    return output</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">25</td>
      <td rowspan="1">Str 25 Count The Reversals<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/count-the-reversals0401/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Stack approach.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Remove all balanced brackets using a stack. The remaining string will be of the form `}}...{{...`. The required reversals will be `ceil(open_count/2) + ceil(close_count/2)`.<br><br><b>Dependencies:</b> Stack</td>
      <td><b>Edge Cases:</b> Odd length string<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import math&#10;def countRev(s):&#10;    if len(s) % 2 != 0: return -1&#10;    stack = []&#10;    for c in s:&#10;        if c == &#x27;{&#x27;: stack.append(c)&#10;        else:&#10;            if stack and stack[-1] == &#x27;{&#x27;: stack.pop()&#10;            else: stack.append(c)&#10;    open_count = stack.count(&#x27;{&#x27;)&#10;    close_count = len(stack) - open_count&#10;    return math.ceil(open_count / 2) + math.ceil(close_count / 2)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">26</td>
      <td rowspan="1">Str 26 Count Palindromic Subsequences<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/count-palindromic-subsequences/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Dynamic Programming.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N^2)</td>
      <td>Use DP. `dp[i][j]` stores the count of palindromic subsequences in `str[i..j]`. If `str[i] == str[j]`, `dp[i][j] = dp[i+1][j] + dp[i][j-1] + 1`. Else, `dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]`.<br><br><b>Dependencies:</b> DP</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def countPS(str_val):&#10;    MOD = 10**9 + 7&#10;    n = len(str_val)&#10;    dp = [[0]*n for _ in range(n)]&#10;    for i in range(n): dp[i][i] = 1&#10;    for length in range(2, n + 1):&#10;        for i in range(n - length + 1):&#10;            j = i + length - 1&#10;            if str_val[i] == str_val[j]:&#10;                dp[i][j] = (dp[i+1][j] + dp[i][j-1] + 1) % MOD&#10;            else:&#10;                dp[i][j] = (dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]) % MOD&#10;    return dp[0][n - 1]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">27</td>
      <td rowspan="1">Str 27 Count Of Number Of Given String In 2D Character Array<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/count-occurences-of-a-given-word-in-a-2-d-array/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> DFS.</td>
      <td><b>Time:</b> O(R * C * 4^L)<br><b>Space:</b> O(L)</td>
      <td>Use DFS. For each cell, if it matches the first character of the word, start a DFS to look for the rest of the word in all 4 directions. Keep track of visited cells.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findOccurrence(mat, target):&#10;    def dfs(r, c, idx):&#10;        if idx == len(target): return 1&#10;        if r &lt; 0 or r &gt;= len(mat) or c &lt; 0 or c &gt;= len(mat[0]) or mat[r][c] != target[idx]: return 0&#10;        temp = mat[r][c]&#10;        mat[r][c] = &#x27;#&#x27;&#10;        found = (dfs(r + 1, c, idx + 1) +&#10;                 dfs(r - 1, c, idx + 1) +&#10;                 dfs(r, c + 1, idx + 1) +&#10;                 dfs(r, c - 1, idx + 1))&#10;        mat[r][c] = temp&#10;        return found&#10;    count = 0&#10;    for i in range(len(mat)):&#10;        for j in range(len(mat[0])):&#10;            if mat[i][j] == target[0]:&#10;                count += dfs(i, j, 0)&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">28</td>
      <td rowspan="1">Str 28 Search A Word In A 2D Grid Of Characters<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/find-the-string-in-grid0111/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> 8 Directions Loop.</td>
      <td><b>Time:</b> O(N * M * 8 * L)<br><b>Space:</b> O(1)</td>
      <td>Iterate through the grid. For each matching starting character, check all 8 directions to see if the full word exists in a straight line.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def searchWord(grid, word):&#10;    R, C, L = len(grid), len(grid[0]), len(word)&#10;    dr = [-1, -1, -1, 0, 0, 1, 1, 1]&#10;    dc = [-1, 0, 1, -1, 1, -1, 0, 1]&#10;    ans = []&#10;    for r in range(R):&#10;        for c in range(C):&#10;            if grid[r][c] == word[0]:&#10;                for dir in range(8):&#10;                    currR, currC = r + dr[dir], c + dc[dir]&#10;                    k = 1&#10;                    while k &lt; L:&#10;                        if currR &lt; 0 or currR &gt;= R or currC &lt; 0 or currC &gt;= C: break&#10;                        if grid[currR][currC] != word[k]: break&#10;                        currR += dr[dir]&#10;                        currC += dc[dir]&#10;                        k += 1&#10;                    if k == L:&#10;                        ans.append([r, c])&#10;                        break&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">29</td>
      <td rowspan="1">Str 29 Boyer Moore Algorithm For Pattern Searching<br><br></b> <a href="https://www.geeksforgeeks.org/boyer-moore-algorithm-for-pattern-searching/" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Bad Character Heuristic.</td>
      <td><b>Time:</b> O(N * M)<br><b>Space:</b> O(256)</td>
      <td>Create a Bad Character table for the pattern, which stores the last occurrence of each character. Align pattern with text. Compare from right to left. If mismatch, shift the pattern so that the mismatched character in text aligns with its last occurrence in the pattern. If not present, shift pattern past it.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def search(txt, pat):&#10;    m, n = len(pat), len(txt)&#10;    badChar = [-1] * 256&#10;    for i in range(m): badChar[ord(pat[i])] = i&#10;    s = 0&#10;    while s &lt;= n - m:&#10;        j = m - 1&#10;        while j &gt;= 0 and pat[j] == txt[s + j]: j -= 1&#10;        if j &lt; 0:&#10;            print(f&quot;Pattern occurs at shift = {s}&quot;)&#10;            s += (m - badChar[ord(txt[s + m])] if s + m &lt; n else 1)&#10;        else:&#10;            s += max(1, j - badChar[ord(txt[s + j])])</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">30</td>
      <td rowspan="1">Str 30 Roman Number To Integer<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/roman-number-to-integer3201/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Value mapping.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Map each Roman numeral to its integer value. Iterate from right to left. If a character is smaller than its right character, subtract its value, else add it.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def romanToDecimal(S):&#10;    m = {&#x27;I&#x27;: 1, &#x27;V&#x27;: 5, &#x27;X&#x27;: 10, &#x27;L&#x27;: 50, &#x27;C&#x27;: 100, &#x27;D&#x27;: 500, &#x27;M&#x27;: 1000}&#10;    ans = 0&#10;    for i in range(len(S)):&#10;        if i + 1 &lt; len(S) and m[S[i]] &lt; m[S[i+1]]:&#10;            ans -= m[S[i]]&#10;        else:&#10;            ans += m[S[i]]&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">31</td>
      <td rowspan="1">Str 31 Number Of Flips To Make Binary String Alternate<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/min-number-of-flips3210/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Two target strings.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>There are only two possible alternating strings for length N: starting with '0' (`010101...`) and starting with '1' (`101010...`). Count the differences between the given string and both of these. The minimum count is the answer.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minFlips(S):&#10;    count1, count2 = 0, 0&#10;    for i in range(len(S)):&#10;        if i % 2 == 0:&#10;            if S[i] != &#x27;0&#x27;: count1 += 1&#10;            if S[i] != &#x27;1&#x27;: count2 += 1&#10;        else:&#10;            if S[i] != &#x27;1&#x27;: count1 += 1&#10;            if S[i] != &#x27;0&#x27;: count2 += 1&#10;    return min(count1, count2)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">32</td>
      <td rowspan="1">Str 32 Find The First Repeated Word In String<br><br></b> <a href="https://www.geeksforgeeks.org/find-first-repeated-word-string/" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> HashSet.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Split the string into words. Iterate through the words. If a word is already in the hash set, it is the first repeated word. Return it. Else, add it to the hash set.<br><br><b>Dependencies:</b> Hash Set</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def firstRepeatedWord(s):&#10;    import re&#10;    words = re.findall(r&#x27;\w+&#x27;, s)&#10;    st = set()&#10;    for word in words:&#10;        if word in st: return word&#10;        st.add(word)&#10;    return &quot;No Repetition&quot;</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">33</td>
      <td rowspan="1">Str 33 Minimum Swaps For Bracket Balancing<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/minimum-swaps-for-bracket-balancing2704/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Track balance.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Keep track of the number of opening and closing brackets, and an `imbalance` counter. When encountering `[`, decrease imbalance. When encountering `]`, increase imbalance. The number of swaps is updated when an imbalance is found and we find the next `[`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minimumNumberOfSwaps(S):&#10;    open_count = 0&#10;    close_count = 0&#10;    fault = 0&#10;    ans = 0&#10;    for char in S:&#10;        if char == &#x27;]&#x27;:&#10;            close_count += 1&#10;            fault = close_count - open_count&#10;        else:&#10;            open_count += 1&#10;            if fault &gt; 0:&#10;                ans += fault&#10;                fault -= 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">34</td>
      <td rowspan="1">Str 34 Isomorphic Strings<br><br></b> <a href="https://leetcode.com/problems/isomorphic-strings/" target="_blank">LeetCode 205</a></td>
      <td rowspan="1"><b>Example 1:</b> Hash Maps.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Use two arrays to map characters from `s` to `t` and `t` to `s`. If `s[i]` is mapped to a character other than `t[i]`, or `t[i]` is mapped to a character other than `s[i]`, return false. Else, create the mappings.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isIsomorphic(s, t):&#10;    m1, m2 = [-1] * 256, [-1] * 256&#10;    for i in range(len(s)):&#10;        if m1[ord(s[i])] != m2[ord(t[i])]: return False&#10;        m1[ord(s[i])] = i&#10;        m2[ord(t[i])] = i&#10;    return True</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">35</td>
      <td rowspan="1">Str 35 Reverse Words In A String<br><br></b> <a href="https://leetcode.com/problems/reverse-words-in-a-string/" target="_blank">LeetCode 151</a></td>
      <td rowspan="1"><b>Example 1:</b> Two Pointers.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N) for output string</td>
      <td>Iterate from right to left. Find the end of a word, then the start of a word. Extract the word and append it to the result string along with a space. Finally, remove the trailing space.</td>
      <td><b>Edge Cases:</b> Multiple spaces between words<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def reverseWords(s):&#10;    return &quot; &quot;.join(s.split()[::-1])</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">36</td>
      <td rowspan="1">Str 36 Rotate String<br><br></b> <a href="https://leetcode.com/problems/rotate-string/" target="_blank">LeetCode 796</a></td>
      <td rowspan="1"><b>Example 1:</b> String Concatenation.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>If the lengths of `s` and `goal` are not equal, return false. Otherwise, concatenate `s` with itself (`s + s`). If `goal` is a substring of `s + s`, then it's a rotated string.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def rotateString(s, goal):&#10;    if len(s) != len(goal): return False&#10;    return goal in (s + s)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">37</td>
      <td rowspan="1">Str 37 Largest Odd Number In String<br><br></b> <a href="https://leetcode.com/problems/largest-odd-number-in-string/" target="_blank">LeetCode 1903</a></td>
      <td rowspan="1"><b>Example 1:</b> Iterate from right.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1) excluding output</td>
      <td>Iterate from the end of the string. The first odd digit found marks the end of the largest odd integer (since picking all digits from index 0 to this odd digit yields the largest value). Return the substring `num[0..i]`. If no odd digit is found, return empty string.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def largestOddNumber(num):&#10;    for i in range(len(num) - 1, -1, -1):&#10;        if int(num[i]) % 2 != 0: return num[:i+1]&#10;    return &quot;&quot;</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">38</td>
      <td rowspan="1">Str 38 Maximum Nesting Depth Of The Parentheses<br><br></b> <a href="https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/" target="_blank">LeetCode 1614</a></td>
      <td rowspan="1"><b>Example 1:</b> Counter tracking.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Iterate through the string. Maintain a `current_depth` counter. If we see `(`, increment the counter and update `max_depth`. If we see `)`, decrement the counter. Ignore other characters.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxDepth(s):&#10;    max_d = cur_d = 0&#10;    for c in s:&#10;        if c == &#x27;(&#x27;:&#10;            cur_d += 1&#10;            max_d = max(max_d, cur_d)&#10;        elif c == &#x27;)&#x27;:&#10;            cur_d -= 1&#10;    return max_d</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">39</td>
      <td rowspan="1">Str 39 String To Integer Atoi<br><br></b> <a href="https://leetcode.com/problems/string-to-integer-atoi/" target="_blank">LeetCode 8</a></td>
      <td rowspan="1"><b>Example 1:</b> Step-by-step parsing.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>1. Ignore leading whitespaces. 2. Check for optional '+' or '-'. 3. Read digits until a non-digit or end of string. 4. Build the integer, checking for 32-bit integer overflow/underflow at each step.</td>
      <td><b>Edge Cases:</b> Overflow/Underflow<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def myAtoi(s):&#10;    s = s.lstrip()&#10;    if not s: return 0&#10;    sign = -1 if s[0] == &#x27;-&#x27; else 1&#10;    if s[0] in [&#x27;-&#x27;, &#x27;+&#x27;]: s = s[1:]&#10;    ans = 0&#10;    for c in s:&#10;        if not c.isdigit(): break&#10;        ans = ans * 10 + int(c)&#10;    ans *= sign&#10;    ans = max(-2**31, min(ans, 2**31 - 1))&#10;    return ans</code></pre></details></td>
    </tr>
  </tbody>
</table>


## Sliding Window

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
      <td rowspan="1">1</td>
      <td rowspan="1">Sw 01 Longest Substring Without Repeating Characters<br><br></b> <a href="https://leetcode.com/problems/longest-substring-without-repeating-characters/" target="_blank">LeetCode 3</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> s = "abcabcbb"<br><b>Output:</b> 3 ("abc")</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(min(N, M))</td>
      <td>Sliding window with a Hash Map storing the latest index of each character. Move `left` pointer to `max(left, map[char] + 1)`.<br><br><b>Dependencies:</b> <code>std::vector</code> for frequency array</td>
      <td><b>Edge Cases:</b> <b>Pointer Leap:</b> `left` can only jump forward, thus `std::max(left, ...)` prevents `left` from going backward if an old duplicate is found.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def lengthOfLongestSubstring(s: str) -&gt; int:&#10;    mpp = {}&#10;    left = max_len = 0&#10;    for right, char in enumerate(s):&#10;        if char in mpp:&#10;            left = max(left, mpp[char] + 1)&#10;        mpp[char] = right&#10;        max_len = max(max_len, right - left + 1)&#10;    return max_len</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">2</td>
      <td rowspan="1">Sw 02 Trapping Rain Water<br><br></b> <a href="https://leetcode.com/problems/trapping-rain-water/" target="_blank">LeetCode 42</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> height = [0,1,0,2,1,0,1,3,2,1,2,1]<br><b>Output:</b> 6</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Two pointers `left` and `right`. Maintain `left_max` and `right_max`. Move the pointer pointing to the smaller max, adding trapped water.</td>
      <td><b>Edge Cases:</b> <b>Local Maxima:</b> Water trapped at `i` relies on the absolute minimum of the highest bars to its left and right.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def trap(height: list[int]) -&gt; int:&#10;    left, right = 0, len(height) - 1&#10;    res, maxLeft, maxRight = 0, 0, 0&#10;    while left &lt;= right:&#10;        if height[left] &lt;= height[right]:&#10;            if height[left] &gt;= maxLeft: maxLeft = height[left]&#10;            else: res += maxLeft - height[left]&#10;            left += 1&#10;        else:&#10;            if height[right] &gt;= maxRight: maxRight = height[right]&#10;            else: res += maxRight - height[right]&#10;            right -= 1&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">3</td>
      <td rowspan="1">Sw 03 Container With Most Water<br><br></b> <a href="https://leetcode.com/problems/container-with-most-water/" target="_blank">LeetCode 11</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> height = [1,8,6,2,5,4,8,3,7]<br><b>Output:</b> 49</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Two Pointers from ends. Area is `min(h[left], h[right]) * width`. Move the pointer with the smaller height to seek a potentially taller line.<br><br><b>Dependencies:</b> <code>std::max</code>, <code>std::min</code></td>
      <td><b>Edge Cases:</b> <b>Width vs Height Tradeoff:</b> By starting at maximum width, we only decrease width. Thus, we must only abandon a height if we hope to find a taller one.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxArea(height: list[int]) -&gt; int:&#10;    left, right = 0, len(height) - 1&#10;    max_area = 0&#10;    while left &lt; right:&#10;        area = min(height[left], height[right]) * (right - left)&#10;        max_area = max(max_area, area)&#10;        if height[left] &lt; height[right]:&#10;            left += 1&#10;        else:&#10;            right -= 1&#10;    return max_area</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">4</td>
      <td rowspan="1">Sw 04 Count Occurrences Of Anagrams<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/count-occurences-of-anagrams5839/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Fixed window and frequency map.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(26) = O(1)</td>
      <td>Maintain a frequency map of the pattern. Use a sliding window of size equal to the length of the pattern. Keep track of the number of characters fully matched (`count`). If `count` equals the number of unique characters in the pattern, an anagram is found.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def search(pat: str, txt: str) -&gt; int:&#10;    k, n = len(pat), len(txt)&#10;    if k &gt; n: return 0&#10;    count = collections.Counter(pat)&#10;    distinct = len(count)&#10;    i = j = ans = 0&#10;    while j &lt; n:&#10;        if txt[j] in count:&#10;            count[txt[j]] -= 1&#10;            if count[txt[j]] == 0:&#10;                distinct -= 1&#10;        if j - i + 1 &lt; k:&#10;            j += 1&#10;        elif j - i + 1 == k:&#10;            if distinct == 0:&#10;                ans += 1&#10;            if txt[i] in count:&#10;                count[txt[i]] += 1&#10;                if count[txt[i]] == 1:&#10;                    distinct += 1&#10;            i += 1&#10;            j += 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">5</td>
      <td rowspan="1">Sw 05 Maximum Of All Subarrays Of Size K<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/maximum-of-all-subarrays-of-size-k3101/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Deque.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(K)</td>
      <td>Use a deque to store indices of elements. The deque will maintain elements in decreasing order. For each element, remove elements from the back of the deque that are smaller than the current element. Also, remove elements from the front that are out of the current window. The front of the deque will always have the maximum element of the current window.<br><br><b>Dependencies:</b> <code>#include <deque></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def max_of_subarrays(arr: List[int], n: int, k: int) -&gt; List[int]:&#10;    res = []&#10;    dq = collections.deque()&#10;    for i in range(n):&#10;        if dq and dq[0] == i - k:&#10;            dq.popleft()&#10;        while dq and arr[dq[-1]] &lt;= arr[i]:&#10;            dq.pop()&#10;        dq.append(i)&#10;        if i &gt;= k - 1:&#10;            res.append(arr[dq[0]])&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">6</td>
      <td rowspan="1">Sw 06 Minimum Window Substring<br><br></b> <a href="https://leetcode.com/problems/minimum-window-substring/" target="_blank">LeetCode 76</a></td>
      <td rowspan="1"><b>Example 1:</b> Variable sliding window.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Maintain a frequency map of `t`. Expand the window by moving `right`. When the window contains all characters of `t`, try to shrink it by moving `left` to find the minimum window. Keep track of the minimum window length and its starting index.<br><br><b>Dependencies:</b> <code>#include <unordered_map></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def minWindow(s: str, t: str) -&gt; str:&#10;    if len(s) &lt; len(t): return &quot;&quot;&#10;    count = collections.Counter(t)&#10;    required = len(t)&#10;    l = r = 0&#10;    minLen = float(&#x27;inf&#x27;)&#10;    minStart = 0&#10;    while r &lt; len(s):&#10;        if count[s[r]] &gt; 0:&#10;            required -= 1&#10;        count[s[r]] -= 1&#10;        r += 1&#10;        while required == 0:&#10;            if r - l &lt; minLen:&#10;                minLen = r - l&#10;                minStart = l&#10;            count[s[l]] += 1&#10;            if count[s[l]] &gt; 0:&#10;                required += 1&#10;            l += 1&#10;    return &quot;&quot; if minLen == float(&#x27;inf&#x27;) else s[minStart:minStart+minLen]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">7</td>
      <td rowspan="1">Sw 07 Sliding Window Maximum<br><br></b> <a href="https://leetcode.com/problems/sliding-window-maximum/" target="_blank">LeetCode 239</a></td>
      <td rowspan="1"><b>Example 1:</b> Deque.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(K)</td>
      <td>Use a deque to store indices. The deque maintains elements in decreasing order. Remove elements from the back if they are smaller than the current element. Remove elements from the front if they are out of the window. The front element is the maximum of the current window.<br><br><b>Dependencies:</b> <code>#include <deque></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def maxSlidingWindow(nums: List[int], k: int) -&gt; List[int]:&#10;    res = []&#10;    dq = collections.deque()&#10;    for i in range(len(nums)):&#10;        if dq and dq[0] == i - k:&#10;            dq.popleft()&#10;        while dq and nums[dq[-1]] &lt;= nums[i]:&#10;            dq.pop()&#10;        dq.append(i)&#10;        if i &gt;= k - 1:&#10;            res.append(nums[dq[0]])&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">8</td>
      <td rowspan="1">Sw 08 Longest K Unique Characters Substring<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Variable window and hash map.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(K)</td>
      <td>Maintain a hash map of character frequencies. Expand the window by moving `j`. If the number of unique characters exceeds `k`, shrink the window from the left (`i`) until the number of unique characters is `k`. Update the maximum length when exactly `k` unique characters are present.<br><br><b>Dependencies:</b> <code>#include <unordered_map></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def longestKSubstr(s: str, k: int) -&gt; int:&#10;    count = collections.defaultdict(int)&#10;    i = j = 0&#10;    maxLen = -1&#10;    while j &lt; len(s):&#10;        count[s[j]] += 1&#10;        if len(count) == k:&#10;            maxLen = max(maxLen, j - i + 1)&#10;        elif len(count) &gt; k:&#10;            while len(count) &gt; k:&#10;                count[s[i]] -= 1&#10;                if count[s[i]] == 0:&#10;                    del count[s[i]]&#10;                i += 1&#10;        j += 1&#10;    return maxLen</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">9</td>
      <td rowspan="1">Sw 09 Subarrays With K Different Integers<br><br></b> <a href="https://leetcode.com/problems/subarrays-with-k-different-integers/" target="_blank">LeetCode 992</a></td>
      <td rowspan="1"><b>Example 1:</b> Exact K = atMost(K) - atMost(K-1).</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Finding exact `k` distinct is hard directly. Instead, find subarrays with at most `k` distinct integers. The number of exact `k` is `atMost(k) - atMost(k - 1)`. The `atMost` function uses a sliding window.<br><br><b>Dependencies:</b> <code>#include <unordered_map></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def subarraysWithKDistinct(nums: List[int], k: int) -&gt; int:&#10;    def atMost(k):&#10;        count = collections.defaultdict(int)&#10;        res = i = 0&#10;        for j in range(len(nums)):&#10;            if count[nums[j]] == 0: k -= 1&#10;            count[nums[j]] += 1&#10;            while k &lt; 0:&#10;                count[nums[i]] -= 1&#10;                if count[nums[i]] == 0: k += 1&#10;                i += 1&#10;            res += j - i + 1&#10;        return res&#10;    return atMost(k) - atMost(k - 1)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">10</td>
      <td rowspan="1">Sw 10 Minimum Size Subarray Sum<br><br></b> <a href="https://leetcode.com/problems/minimum-size-subarray-sum/" target="_blank">LeetCode 209</a></td>
      <td rowspan="1"><b>Example 1:</b> Variable sliding window.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Use a sliding window. Add elements to the current sum. While the sum is >= target, update the minimum length and shrink the window from the left.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minSubArrayLen(target: int, nums: List[int]) -&gt; int:&#10;    l = sum = 0&#10;    minLen = float(&#x27;inf&#x27;)&#10;    for r in range(len(nums)):&#10;        sum += nums[r]&#10;        while sum &gt;= target:&#10;            minLen = min(minLen, r - l + 1)&#10;            sum -= nums[l]&#10;            l += 1&#10;    return 0 if minLen == float(&#x27;inf&#x27;) else minLen</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">11</td>
      <td rowspan="1">Sw 11 Fruits Into Baskets<br><br></b> <a href="https://leetcode.com/problems/fruit-into-baskets/" target="_blank">LeetCode 904</a></td>
      <td rowspan="1"><b>Example 1:</b> Longest subarray with at most 2 distinct elements.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1) (at most 3 elements in map)</td>
      <td>This translates to finding the longest subarray with at most 2 distinct elements. Maintain a frequency map and use a sliding window. If distinct elements > 2, shrink the window until distinct elements <= 2.<br><br><b>Dependencies:</b> <code>#include <unordered_map></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def totalFruit(fruits: List[int]) -&gt; int:&#10;    count = collections.defaultdict(int)&#10;    l = maxFruits = 0&#10;    for r in range(len(fruits)):&#10;        count[fruits[r]] += 1&#10;        while len(count) &gt; 2:&#10;            count[fruits[l]] -= 1&#10;            if count[fruits[l]] == 0:&#10;                del count[fruits[l]]&#10;            l += 1&#10;        maxFruits = max(maxFruits, r - l + 1)&#10;    return maxFruits</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">12</td>
      <td rowspan="1">Sw 12 Max Consecutive Ones III<br><br></b> <a href="https://leetcode.com/problems/max-consecutive-ones-iii/" target="_blank">LeetCode 1004</a></td>
      <td rowspan="1"><b>Example 1:</b> Sliding Window.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Use a sliding window. Expand the right pointer. If the element is 0, increment a zero counter. While the zero counter > k, shrink the window from the left by moving the left pointer and decrementing the zero counter if left element is 0. The max window size is the answer.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def longestOnes(nums, k):&#10;    left = 0&#10;    zeroes = 0&#10;    max_len = 0&#10;    for right in range(len(nums)):&#10;        if nums[right] == 0: zeroes += 1&#10;        while zeroes &gt; k:&#10;            if nums[left] == 0: zeroes -= 1&#10;            left += 1&#10;        max_len = max(max_len, right - left + 1)&#10;    return max_len</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">13</td>
      <td rowspan="1">Sw 13 Longest Repeating Character Replacement<br><br></b> <a href="https://leetcode.com/problems/longest-repeating-character-replacement/" target="_blank">LeetCode 424</a></td>
      <td rowspan="1"><b>Example 1:</b> Sliding Window + Max Freq.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Use a sliding window. Maintain the character frequencies and the `max_freq` in the window. The number of replacements needed is `window_size - max_freq`. If this is > k, shrink the window from left and decrement the corresponding frequency.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def characterReplacement(s, k):&#10;    count = [0] * 26&#10;    left = 0&#10;    max_freq = 0&#10;    max_len = 0&#10;    for right in range(len(s)):&#10;        count[ord(s[right]) - ord(&#x27;A&#x27;)] += 1&#10;        max_freq = max(max_freq, count[ord(s[right]) - ord(&#x27;A&#x27;)])&#10;        if (right - left + 1) - max_freq &gt; k:&#10;            count[ord(s[left]) - ord(&#x27;A&#x27;)] -= 1&#10;            left += 1&#10;        max_len = max(max_len, right - left + 1)&#10;    return max_len</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">14</td>
      <td rowspan="1">Sw 14 Binary Subarrays With Sum<br><br></b> <a href="https://leetcode.com/problems/binary-subarrays-with-sum/" target="_blank">LeetCode 930</a></td>
      <td rowspan="1"><b>Example 1:</b> atMost(goal) - atMost(goal - 1).</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Use the helper function `atMost(goal)` which finds the number of subarrays with sum <= goal. The answer is `atMost(goal) - atMost(goal - 1)`. In `atMost`, use a sliding window to maintain the sum.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def numSubarraysWithSum(nums, goal):&#10;    def atMost(k):&#10;        if k &lt; 0: return 0&#10;        left, sum_val, count = 0, 0, 0&#10;        for right in range(len(nums)):&#10;            sum_val += nums[right]&#10;            while sum_val &gt; k:&#10;                sum_val -= nums[left]&#10;                left += 1&#10;            count += (right - left + 1)&#10;        return count&#10;    return atMost(goal) - atMost(goal - 1)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">15</td>
      <td rowspan="1">Sw 15 Count Number Of Nice Subarrays<br><br></b> <a href="https://leetcode.com/problems/count-number-of-nice-subarrays/" target="_blank">LeetCode 1248</a></td>
      <td rowspan="1"><b>Example 1:</b> atMost(k) - atMost(k - 1).</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Replace all odd numbers with 1 and even numbers with 0. The problem then reduces to finding the number of subarrays with a sum equal to k. Use the `atMost(k) - atMost(k - 1)` sliding window approach.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def numberOfSubarrays(nums, k):&#10;    def atMost(limit):&#10;        if limit &lt; 0: return 0&#10;        left, count, res = 0, 0, 0&#10;        for right in range(len(nums)):&#10;            if nums[right] % 2 != 0: count += 1&#10;            while count &gt; limit:&#10;                if nums[left] % 2 != 0: count -= 1&#10;                left += 1&#10;            res += (right - left + 1)&#10;        return res&#10;    return atMost(k) - atMost(k - 1)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">16</td>
      <td rowspan="1">Sw 16 Number Of Substrings Containing All Three Characters<br><br></b> <a href="https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/" target="_blank">LeetCode 1358</a></td>
      <td rowspan="1"><b>Example 1:</b> Store last seen indices.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Iterate through the string. Track the last seen indices of 'a', 'b', and 'c'. If all three have been seen, the number of valid substrings ending at the current index `i` is `1 + min(last_a, last_b, last_c)`. Add this to the total count.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def numberOfSubstrings(s):&#10;    last = [-1, -1, -1]&#10;    count = 0&#10;    for i in range(len(s)):&#10;        last[ord(s[i]) - ord(&#x27;a&#x27;)] = i&#10;        if last[0] != -1 and last[1] != -1 and last[2] != -1:&#10;            count += 1 + min(last)&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">17</td>
      <td rowspan="1">Sw 17 Maximum Points You Can Obtain From Cards<br><br></b> <a href="https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/" target="_blank">LeetCode 1423</a></td>
      <td rowspan="1"><b>Example 1:</b> Sliding Window on remaining cards.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Instead of picking cards from the ends, find the subarray of length `N - K` that has the minimum sum. Subtract this minimum sum from the total sum of the array. That gives the maximum score.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxScore(cardPoints, k):&#10;    n = len(cardPoints)&#10;    total_sum = sum(cardPoints)&#10;    window_size = n - k&#10;    window_sum = sum(cardPoints[:window_size])&#10;    min_window_sum = window_sum&#10;    for i in range(window_size, n):&#10;        window_sum += cardPoints[i] - cardPoints[i - window_size]&#10;        min_window_sum = min(min_window_sum, window_sum)&#10;    return total_sum - min_window_sum</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">18</td>
      <td rowspan="1">Sw 18 Find All Anagrams In A String<br><br></b> <a href="https://leetcode.com/problems/find-all-anagrams-in-a-string/" target="_blank">LeetCode 438</a></td>
      <td rowspan="1"><b>Example 1:</b> Fixed Window + Hash Map.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Create frequency arrays for `p` and a window of size `p.length()` in `s`. Slide the window across `s`, updating the window frequencies. If the arrays match, add the window's start index to the result.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findAnagrams(s, p):&#10;    ans = []&#10;    if len(p) &gt; len(s): return ans&#10;    countP, countS = [0]*26, [0]*26&#10;    for i in range(len(p)):&#10;        countP[ord(p[i]) - ord(&#x27;a&#x27;)] += 1&#10;        countS[ord(s[i]) - ord(&#x27;a&#x27;)] += 1&#10;    if countP == countS: ans.append(0)&#10;    for i in range(len(p), len(s)):&#10;        countS[ord(s[i]) - ord(&#x27;a&#x27;)] += 1&#10;        countS[ord(s[i - len(p)]) - ord(&#x27;a&#x27;)] -= 1&#10;        if countP == countS: ans.append(i - len(p) + 1)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">19</td>
      <td rowspan="1">Sw 19 Permutation In String<br><br></b> <a href="https://leetcode.com/problems/permutation-in-string/" target="_blank">LeetCode 567</a></td>
      <td rowspan="1"><b>Example 1:</b> Sliding Window + Frequency Array.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Use a sliding window of size `len(s1)` over `s2`. Maintain frequency arrays for `s1` and the current window in `s2`. Compare arrays at each step.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def checkInclusion(s1, s2):&#10;    if len(s1) &gt; len(s2): return False&#10;    c1, c2 = [0]*26, [0]*26&#10;    for i in range(len(s1)):&#10;        c1[ord(s1[i]) - 97] += 1&#10;        c2[ord(s2[i]) - 97] += 1&#10;    if c1 == c2: return True&#10;    for i in range(len(s1), len(s2)):&#10;        c2[ord(s2[i]) - 97] += 1&#10;        c2[ord(s2[i - len(s1)]) - 97] -= 1&#10;        if c1 == c2: return True&#10;    return False</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">20</td>
      <td rowspan="1">Sw 20 First Negative Integer In Every Window Of Size K<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Queue.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(K)</td>
      <td>Maintain a queue of negative integers in the current window. While moving the window, add new negative integers, remove old ones out of window. The front of queue is the first negative.<br><br><b>Dependencies:</b> Queue</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">from collections import deque&#10;def printFirstNegativeInteger(A, N, K):&#10;    ans = []&#10;    q = deque()&#10;    for i in range(K - 1):&#10;        if A[i] &lt; 0: q.append(A[i])&#10;    for i in range(K - 1, N):&#10;        if A[i] &lt; 0: q.append(A[i])&#10;        ans.append(q[0] if q else 0)&#10;        if A[i - K + 1] &lt; 0 and q and q[0] == A[i - K + 1]: q.popleft()&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">21</td>
      <td rowspan="1">Sw 21 Count Occurrences Of Anagrams<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/count-occurences-of-anagrams1536/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Sliding Window + Frequency Map.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Use a sliding window of size `pat.length()`. Keep frequency map of `pat`. Track `count` of distinct characters to match. While moving window, decrease `count` if char frequency matches. If `count == 0`, increment answer.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def search(pat, txt):&#10;    m = {}&#10;    for c in pat: m[c] = m.get(c, 0) + 1&#10;    count, ans, k = len(m), 0, len(pat)&#10;    i = 0&#10;    for j in range(len(txt)):&#10;        if txt[j] in m:&#10;            m[txt[j]] -= 1&#10;            if m[txt[j]] == 0: count -= 1&#10;        if j - i + 1 == k:&#10;            if count == 0: ans += 1&#10;            if txt[i] in m:&#10;                m[txt[i]] += 1&#10;                if m[txt[i]] == 1: count += 1&#10;            i += 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">22</td>
      <td rowspan="1">Sw 22 Smallest Window In A String Containing All The Characters Of Another String<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/smallest-window-in-a-string-containing-all-the-characters-of-another-string-1587115621/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Sliding Window.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Same as Minimum Window Substring. Use frequency map of `P` and a sliding window over `S`. Shrink window from left when all characters match to find the minimum length.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def smallestWindow(s, p):&#10;    if len(p) &gt; len(s): return &quot;-1&quot;&#10;    m = {}&#10;    for c in p: m[c] = m.get(c, 0) + 1&#10;    count, minLen, start, i = len(m), float(&#x27;inf&#x27;), 0, 0&#10;    for j in range(len(s)):&#10;        if s[j] in m:&#10;            m[s[j]] -= 1&#10;            if m[s[j]] == 0: count -= 1&#10;        while count == 0:&#10;            if j - i + 1 &lt; minLen:&#10;                minLen = j - i + 1&#10;                start = i&#10;            if s[i] in m:&#10;                m[s[i]] += 1&#10;                if m[s[i]] &gt; 0: count += 1&#10;            i += 1&#10;    return &quot;-1&quot; if minLen == float(&#x27;inf&#x27;) else s[start:start+minLen]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">23</td>
      <td rowspan="1">Sw 23 Longest Substring With At Most K Distinct Characters<br><br></b> <a href="https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/" target="_blank">LeetCode 340</a></td>
      <td rowspan="1"><b>Example 1:</b> Sliding Window.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(K)</td>
      <td>Sliding window with hash map to count characters. While map size > k, shrink window from left.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def lengthOfLongestSubstringKDistinct(s, k):&#10;    m = {}&#10;    left, max_len = 0, 0&#10;    for right in range(len(s)):&#10;        m[s[right]] = m.get(s[right], 0) + 1&#10;        while len(m) &gt; k:&#10;            m[s[left]] -= 1&#10;            if m[s[left]] == 0: del m[s[left]]&#10;            left += 1&#10;        max_len = max(max_len, right - left + 1)&#10;    return max_len</code></pre></details></td>
    </tr>
  </tbody>
</table>


## Sorting

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
      <td rowspan="1">1</td>
      <td rowspan="1">Sort 01 Selection Sort<br><br></b> <a href="https://www.geeksforgeeks.org/problems/selection-sort/1" target="_blank">GeeksforGeeks</a></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> N = 5, arr[] = {4, 1, 3, 9, 7}<br><b>Output:</b> 1 3 4 7 9<br><br><b> </b> In-place sorting.</td>
      <td><b>Time:</b> O(N<sup>2</sup>) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td>Find the minimum element in the unsorted array and swap it with the element at the beginning.<br><br><b>Dependencies:</b> <code>std::swap</code></td>
      <td><b>Edge Cases:</b> <b>Worst Case:</b> Always `O(N^2)` even if the array is already sorted.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def selection_sort(arr: list[int]) -&gt; None:&#10;    n = len(arr)&#10;    for i in range(n - 1):&#10;        min_idx = i&#10;        for j in range(i + 1, n):&#10;            if arr[j] &lt; arr[min_idx]:&#10;                min_idx = j&#10;        arr[i], arr[min_idx] = arr[min_idx], arr[i]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">2</td>
      <td rowspan="1">Sort 02 Bubble Sort<br><br></b> <a href="https://www.geeksforgeeks.org/problems/bubble-sort/1" target="_blank">GeeksforGeeks</a></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> N = 5, arr[] = {4, 1, 3, 9, 7}<br><b>Output:</b> 1 3 4 7 9</td>
      <td><b>Time:</b> O(N<sup>2</sup>) (Trade-off)<br><b>Space:</b> O(1)</td>
      <td>Repeatedly swap adjacent elements if they are in the wrong order. Push the maximum element to the end.</td>
      <td><b>Edge Cases:</b> <b>Best Case Check:</b> Adding `did_swap` flag makes Best Case time `O(N)` for already sorted arrays.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def bubble_sort(arr: list[int]) -&gt; None:&#10;    n = len(arr)&#10;    for i in range(n - 1, -1, -1):&#10;        did_swap = False&#10;        for j in range(i):&#10;            if arr[j] &gt; arr[j + 1]:&#10;                arr[j], arr[j + 1] = arr[j + 1], arr[j]&#10;                did_swap = True&#10;        if not did_swap: break</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">3</td>
      <td rowspan="1">Sort 03 Insertion Sort<br><br></b> <a href="https://www.geeksforgeeks.org/problems/insertion-sort/1" target="_blank">GeeksforGeeks</a></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> N = 5, arr[] = {4, 1, 3, 9, 7}<br><b>Output:</b> 1 3 4 7 9</td>
      <td><b>Time:</b> O(N<sup>2</sup>) (Constraint)<br><b>Space:</b> O(1)</td>
      <td>Takes an element and places it in its correct position within the previously sorted part of the array.</td>
      <td><b>Edge Cases:</b> <b>Online Algorithm:</b> Good for data coming in one by one. `O(N)` best case time.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def insertion_sort(arr: list[int]) -&gt; None:&#10;    n = len(arr)&#10;    for i in range(n):&#10;        j = i&#10;        while j &gt; 0 and arr[j - 1] &gt; arr[j]:&#10;            arr[j - 1], arr[j] = arr[j], arr[j - 1]&#10;            j -= 1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">4</td>
      <td rowspan="1">Sort 04 Merge Sort<br><br></b> <a href="https://www.geeksforgeeks.org/problems/merge-sort/1" target="_blank">GeeksforGeeks</a></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> N = 5, arr[] = {4, 1, 3, 9, 7}<br><b>Output:</b> 1 3 4 7 9</td>
      <td><b>Time:</b> O(N log N) (Constraint)<br><b>Space:</b> O(N) (Trade-off)</td>
      <td>Recursively split array in half, sort them, and merge the sorted halves.<br><br><b>Dependencies:</b> Extra array for merging</td>
      <td><b>Edge Cases:</b> <b>Stable Sort:</b> Maintains relative order of equal elements. Requires `O(N)` extra space to merge.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def merge_sort(arr: list[int]) -&gt; None:&#10;    def merge(low, mid, high):&#10;        temp = []&#10;        left, right = low, mid + 1&#10;        while left &lt;= mid and right &lt;= high:&#10;            if arr[left] &lt;= arr[right]:&#10;                temp.append(arr[left])&#10;                left += 1&#10;            else:&#10;                temp.append(arr[right])&#10;                right += 1&#10;        while left &lt;= mid:&#10;            temp.append(arr[left]); left += 1&#10;        while right &lt;= high:&#10;            temp.append(arr[right]); right += 1&#10;        for i in range(len(temp)):&#10;            arr[low + i] = temp[i]&#10;            &#10;    def helper(low, high):&#10;        if low &gt;= high: return&#10;        mid = (low + high) // 2&#10;        helper(low, mid)&#10;        helper(mid + 1, high)&#10;        merge(low, mid, high)&#10;        &#10;    helper(0, len(arr) - 1)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">5</td>
      <td rowspan="1">Sort 05 Quick Sort<br><br></b> <a href="https://www.geeksforgeeks.org/problems/quick-sort/1" target="_blank">GeeksforGeeks</a></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> N = 5, arr[] = {4, 1, 3, 9, 7}<br><b>Output:</b> 1 3 4 7 9</td>
      <td><b>Time:</b> O(N log N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td>Pick a pivot. Place smaller elements left and larger right. Recursively sort partitions.</td>
      <td><b>Edge Cases:</b> <b>Worst Case:</b> `O(N^2)` if array is already sorted and pivot is extreme. Avoided by randomized pivot.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def quick_sort(arr: list[int]) -&gt; None:&#10;    def partition(low, high):&#10;        pivot = arr[low]&#10;        i, j = low, high&#10;        while i &lt; j:&#10;            while i &lt;= high - 1 and arr[i] &lt;= pivot: i += 1&#10;            while j &gt;= low + 1 and arr[j] &gt; pivot: j -= 1&#10;            if i &lt; j: arr[i], arr[j] = arr[j], arr[i]&#10;        arr[low], arr[j] = arr[j], arr[low]&#10;        return j&#10;        &#10;    def helper(low, high):&#10;        if low &lt; high:&#10;            p_idx = partition(low, high)&#10;            helper(low, p_idx - 1)&#10;            helper(p_idx + 1, high)&#10;            &#10;    helper(0, len(arr) - 1)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">6</td>
      <td rowspan="1">Sort 06 Merge Sort<br><br></b> <a href="https://leetcode.com/problems/sort-an-array/" target="_blank">LeetCode 912</a></td>
      <td rowspan="1"><b> </b> <br><b>Input:</b> nums = [5,2,3,1]<br><b>Output:</b> [1,2,3,5]</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(N)</td>
      <td>Divide and Conquer. Split array into halves until size 1. Merge sorted halves using a temporary array.</td>
      <td><b>Edge Cases:</b> <b>In-place illusion:</b> True Merge Sort requires `O(N)` auxiliary space for the `temp` merge array. An in-place version exists but degrades time complexity.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def mergeSort(arr: list[int]) -&gt; list[int]:&#10;    if len(arr) &lt;= 1: return arr&#10;    mid = len(arr) // 2&#10;    left = mergeSort(arr[:mid])&#10;    right = mergeSort(arr[mid:])&#10;    &#10;    res = []&#10;    i = j = 0&#10;    while i &lt; len(left) and j &lt; len(right):&#10;        if left[i] &lt;= right[j]:&#10;            res.append(left[i]); i += 1&#10;        else:&#10;            res.append(right[j]); j += 1&#10;    res.extend(left[i:])&#10;    res.extend(right[j:])&#10;    return res</code></pre></details></td>
    </tr>
  </tbody>
</table>


## Binary Search

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
      <td rowspan="1">1</td>
      <td rowspan="1">Bs 01 Binary Search<br><br></b> <a href="https://leetcode.com/problems/binary-search/" target="_blank">LeetCode 704</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> nums = [-1,0,3,5,9,12], target = 9<br><b>Output:</b> 4</td>
      <td><b>Time:</b> O(log N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td>Optimal: Standard Iterative approach. Maintain `low` and `high` boundaries, shrinking the search space by half.</td>
      <td><b>Edge Cases:</b> <b>Mid Overflow:</b> Use `mid = low + (high - low) / 2` to avoid integer overflow if boundaries are large.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def search(nums: list[int], target: int) -&gt; int:&#10;    low, high = 0, len(nums) - 1&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        if nums[mid] == target:&#10;            return mid&#10;        elif nums[mid] &lt; target:&#10;            low = mid + 1&#10;        else:&#10;            high = mid - 1&#10;    return -1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">2</td>
      <td rowspan="1">Bs 02 Lower Bound<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> arr = [1,2,8,10,11,12,19], target = 0<br><b>Output:</b> 0</td>
      <td><b>Time:</b> O(log N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td>Optimal: When `nums[mid] >= target`, it is a potential answer. Store it and search left (`high = mid - 1`) for smaller potentials.<br><br><b>Dependencies:</b> <code>std::lower_bound</code> internal alternative</td>
      <td><b>Edge Cases:</b> <b>Not Found:</b> If all elements are smaller, `ans` stays `N`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def lowerBound(arr: list[int], n: int, x: int) -&gt; int:&#10;    low, high = 0, n - 1&#10;    ans = n&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        if arr[mid] &gt;= x:&#10;            ans = mid&#10;            high = mid - 1&#10;        else:&#10;            low = mid + 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">3</td>
      <td rowspan="1">Bs 03 Find First And Last Position Of Element<br><br></b> <a href="https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/" target="_blank">LeetCode 34</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> nums = [5,7,7,8,8,10], target = 8<br><b>Output:</b> [3,4]</td>
      <td><b>Time:</b> O(log N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td>Optimal: Run Binary Search twice. Once to find the first occurrence (bias left), once to find the last occurrence (bias right).</td>
      <td><b>Edge Cases:</b> <b>Empty Array:</b> Naturally skips loop and returns `[-1, -1]`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def searchRange(nums: list[int], target: int) -&gt; list[int]:&#10;    def findBound(isFirst):&#10;        low, high, ans = 0, len(nums) - 1, -1&#10;        while low &lt;= high:&#10;            mid = low + (high - low) // 2&#10;            if nums[mid] == target:&#10;                ans = mid&#10;                if isFirst: high = mid - 1&#10;                else: low = mid + 1&#10;            elif nums[mid] &lt; target:&#10;                low = mid + 1&#10;            else:&#10;                high = mid - 1&#10;        return ans&#10;    return [findBound(True), findBound(False)]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">4</td>
      <td rowspan="1">Bs 04 Search In Rotated Sorted Array<br><br></b> <a href="https://leetcode.com/problems/search-in-rotated-sorted-array/" target="_blank">LeetCode 33</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> nums = [4,5,6,7,0,1,2], target = 0<br><b>Output:</b> 4</td>
      <td><b>Time:</b> O(log N) (Constraint)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Identify the sorted half. Check if target lies within the boundaries of the sorted half. If yes, shrink to that half; else, shrink to the other.</td>
      <td><b>Edge Cases:</b> <b>Duplicate Values:</b> If duplicates existed (which they don't in this specific leetcode), we would need to handle `nums[low] == nums[mid] == nums[high]` by shrinking bounds.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def search(nums: list[int], target: int) -&gt; int:&#10;    low, high = 0, len(nums) - 1&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        if nums[mid] == target: return mid&#10;        &#10;        if nums[low] &lt;= nums[mid]:&#10;            if nums[low] &lt;= target &lt;= nums[mid]:&#10;                high = mid - 1&#10;            else:&#10;                low = mid + 1&#10;        else:&#10;            if nums[mid] &lt;= target &lt;= nums[high]:&#10;                low = mid + 1&#10;            else:&#10;                high = mid - 1&#10;    return -1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">5</td>
      <td rowspan="1">Bs 05 Koko Eating Bananas<br><br></b> <a href="https://leetcode.com/problems/koko-eating-bananas/" target="_blank">LeetCode 875</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> piles = [3,6,7,11], h = 8<br><b>Output:</b> 4<br><br><b>Note (Constraint):</b> Binary Search on Answers.</td>
      <td><b>Time:</b> O(N log(Max(P))) (Constraint)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Search space is `1` to `max(piles)`. For a mid `k`, calculate hours required. If `hours <= h`, it's a valid answer, but search left for smaller `k`.<br><br><b>Dependencies:</b> <code>std::ceil</code> / ceiling math</td>
      <td><b>Edge Cases:</b> <b>Ceiling Math:</b> Use `(pile + mid - 1) / mid` to simulate ceiling division without float casting overhead.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import math&#10;def minEatingSpeed(piles: list[int], h: int) -&gt; int:&#10;    def canEat(k):&#10;        hours = sum(math.ceil(pile / k) for pile in piles)&#10;        return hours &lt;= h&#10;        &#10;    low, high = 1, max(piles)&#10;    ans = high&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        if canEat(mid):&#10;            ans = mid&#10;            high = mid - 1&#10;        else:&#10;            low = mid + 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">6</td>
      <td rowspan="1">Bs 06 Find Minimum In Rotated Sorted Array<br><br></b> <a href="https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/" target="_blank">LeetCode 153</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> nums = [3,4,5,1,2]<br><b>Output:</b> 1</td>
      <td><b>Time:</b> O(log N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Binary Search. Compare mid with right pointer. If nums[mid] > nums[right], the min is in the right half. Else, the min is in the left half including mid.</td>
      <td><b>Edge Cases:</b> <b>Fully sorted array:</b> Loop naturally converges to the first element.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findMin(nums: List[int]) -&gt; int:&#10;    left, right = 0, len(nums) - 1&#10;    while left &lt; right:&#10;        mid = left + (right - left) // 2&#10;        if nums[mid] &gt; nums[right]: left = mid + 1&#10;        else: right = mid&#10;    return nums[left]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">7</td>
      <td rowspan="1">Bs 07 Find Peak Element<br><br></b> <a href="https://leetcode.com/problems/find-peak-element/" target="_blank">LeetCode 162</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> nums = [1,2,3,1]<br><b>Output:</b> 2</td>
      <td><b>Time:</b> O(log N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Binary Search. If nums[mid] < nums[mid+1], we are on an ascending slope, so a peak must be to the right. Otherwise, we are on a descending slope, peak is to the left (including mid).</td>
      <td><b>Edge Cases:</b> <b>Peak at boundaries:</b> The binary search logic intrinsically handles edges by shrinking bounds away from negative slopes.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findPeakElement(nums: List[int]) -&gt; int:&#10;    left, right = 0, len(nums) - 1&#10;    while left &lt; right:&#10;        mid = left + (right - left) // 2&#10;        if nums[mid] &lt; nums[mid+1]: left = mid + 1&#10;        else: right = mid&#10;    return left</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">8</td>
      <td rowspan="1">Bs 08 Allocate Minimum Number Of Pages<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> N=4, A=[12,34,67,90], M=2<br><b>Output:</b> 113</td>
      <td><b>Time:</b> O(N * log(sum(A) - max(A)))<br><b>Space:</b> O(1)</td>
      <td>Optimal: Binary Search on Answer. The search space for pages is from `max(A)` to `sum(A)`. For a given `mid`, check if books can be allocated to `<= M` students without any student exceeding `mid` pages.</td>
      <td><b>Edge Cases:</b> <b>M > N:</b> Impossible to allocate at least one book to each student, return -1.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findPages(A: List[int], N: int, M: int) -&gt; int:&#10;    if M &gt; N: return -1&#10;    def isPossible(maxPages):&#10;        students, currentPages = 1, 0&#10;        for pages in A:&#10;            if pages &gt; maxPages: return False&#10;            if currentPages + pages &gt; maxPages:&#10;                students += 1&#10;                currentPages = pages&#10;            else:&#10;                currentPages += pages&#10;        return students &lt;= M&#10;    low, high = max(A), sum(A)&#10;    ans = -1&#10;    while low &lt;= high:&#10;        mid = (low + high) // 2&#10;        if isPossible(mid):&#10;            ans = mid; high = mid - 1&#10;        else: low = mid + 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">9</td>
      <td rowspan="1">Bs 09 Kth Element Of Two Sorted Arrays<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> arr1 = [2, 3, 6, 7, 9], arr2 = [1, 4, 8, 10], k = 5<br><b>Output:</b> 6</td>
      <td><b>Time:</b> O(log(min(n, m)))<br><b>Space:</b> O(1)</td>
      <td>Optimal: Binary search on the smaller array. Similar to Median of two sorted arrays, but the left partition size is strictly `k`. Search space for `cut1` is `[max(0, k-m), min(k, n)]`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def kthElement(arr1: List[int], arr2: List[int], n: int, m: int, k: int) -&gt; int:&#10;    if n &gt; m: return kthElement(arr2, arr1, m, n, k)&#10;    low, high = max(0, k - m), min(k, n)&#10;    while low &lt;= high:&#10;        cut1 = (low + high) // 2&#10;        cut2 = k - cut1&#10;        left1 = float(&#x27;-inf&#x27;) if cut1 == 0 else arr1[cut1-1]&#10;        left2 = float(&#x27;-inf&#x27;) if cut2 == 0 else arr2[cut2-1]&#10;        right1 = float(&#x27;inf&#x27;) if cut1 == n else arr1[cut1]&#10;        right2 = float(&#x27;inf&#x27;) if cut2 == m else arr2[cut2]&#10;        if left1 &lt;= right2 and left2 &lt;= right1: return max(left1, left2)&#10;        elif left1 &gt; right2: high = cut1 - 1&#10;        else: low = cut1 + 1&#10;    return 1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">10</td>
      <td rowspan="1">Bs 10 Search In Rotated Sorted Array II<br><br></b> <a href="https://leetcode.com/problems/search-in-rotated-sorted-array-ii/" target="_blank">LeetCode 81</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> nums = [2,5,6,0,0,1,2], target = 0<br><b>Output:</b> true</td>
      <td><b>Time:</b> O(log N) average, O(N) worst case<br><b>Space:</b> O(1)</td>
      <td>Optimal: If `nums[low] == nums[mid] == nums[high]`, shrink the search space by `low++` and `high--`. Otherwise, proceed with the standard rotated binary search.</td>
      <td><b>Edge Cases:</b> <b>Duplicates causing ambiguity:</b> Shrink bounds safely.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def search(nums: List[int], target: int) -&gt; bool:&#10;    low, high = 0, len(nums) - 1&#10;    while low &lt;= high:&#10;        mid = (low + high) // 2&#10;        if nums[mid] == target: return True&#10;        if nums[low] == nums[mid] == nums[high]:&#10;            low += 1; high -= 1; continue&#10;        if nums[low] &lt;= nums[mid]:&#10;            if nums[low] &lt;= target &lt;= nums[mid]: high = mid - 1&#10;            else: low = mid + 1&#10;        else:&#10;            if nums[mid] &lt;= target &lt;= nums[high]: low = mid + 1&#10;            else: high = mid - 1&#10;    return False</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">11</td>
      <td rowspan="1">Bs 11 Minimum Days To Make M Bouquets<br><br></b> <a href="https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/" target="_blank">LeetCode 1482</a></td>
      <td rowspan="1"><b>Example 1:</b> Find day threshold.</td>
      <td><b>Time:</b> O(N log(maxD - minD))<br><b>Space:</b> O(1)</td>
      <td>Optimal: Binary search on days from `min(bloom)` to `max(bloom)`. Count consecutive bloomed flowers, if it reaches `k`, form a bouquet. Return minimum valid day.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minDays(bloomDay: List[int], m: int, k: int) -&gt; int:&#10;    if m * k &gt; len(bloomDay): return -1&#10;    def isPossible(day):&#10;        count, bouquets = 0, 0&#10;        for d in bloomDay:&#10;            if d &lt;= day: count += 1&#10;            else: bouquets += count // k; count = 0&#10;        bouquets += count // k&#10;        return bouquets &gt;= m&#10;    low, high = min(bloomDay), max(bloomDay)&#10;    ans = -1&#10;    while low &lt;= high:&#10;        mid = (low + high) // 2&#10;        if isPossible(mid): ans = mid; high = mid - 1&#10;        else: low = mid + 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">12</td>
      <td rowspan="1">Bs 12 Find The Smallest Divisor Given A Threshold<br><br></b> <a href="https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/" target="_blank">LeetCode 1283</a></td>
      <td rowspan="1"><b>Example 1:</b> Summing ceils.</td>
      <td><b>Time:</b> O(N log(max(nums)))<br><b>Space:</b> O(1)</td>
      <td>Optimal: Binary search the divisor from 1 to `max(nums)`. Compute `sum(ceil(num / mid))`. If sum <= threshold, shrink high.<br><br><b>Dependencies:</b> <code>#include <math.h></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import math&#10;def smallestDivisor(nums: List[int], threshold: int) -&gt; int:&#10;    low, high = 1, max(nums)&#10;    while low &lt;= high:&#10;        mid = (low + high) // 2&#10;        total = sum(math.ceil(num / mid) for num in nums)&#10;        if total &lt;= threshold: high = mid - 1&#10;        else: low = mid + 1&#10;    return low</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">13</td>
      <td rowspan="1">Bs 13 Capacity To Ship Packages Within D Days<br><br></b> <a href="https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/" target="_blank">LeetCode 1011</a></td>
      <td rowspan="1"><b>Example 1:</b> Find ship capacity.</td>
      <td><b>Time:</b> O(N log(sum - max))<br><b>Space:</b> O(1)</td>
      <td>Optimal: Binary search on capacity. Low = `max(weights)`, High = `sum(weights)`. Iterate through packages and accumulate weight, increment day if limit is exceeded.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def shipWithinDays(weights: List[int], days: int) -&gt; int:&#10;    def canShip(cap):&#10;        d, load = 1, 0&#10;        for w in weights:&#10;            if load + w &gt; cap: d += 1; load = w&#10;            else: load += w&#10;        return d &lt;= days&#10;    low, high = max(weights), sum(weights)&#10;    while low &lt;= high:&#10;        mid = (low + high) // 2&#10;        if canShip(mid): high = mid - 1&#10;        else: low = mid + 1&#10;    return low</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">14</td>
      <td rowspan="1">Bs 14 Kth Missing Positive Number<br><br></b> <a href="https://leetcode.com/problems/kth-missing-positive-number/" target="_blank">LeetCode 1539</a></td>
      <td rowspan="1"><b>Example 1:</b> Calculate missing.</td>
      <td><b>Time:</b> O(log N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Binary search. At index `mid`, the number of missing elements before `arr[mid]` is `arr[mid] - (mid + 1)`. If this is < `k`, search right `low = mid + 1`. Else search left `high = mid - 1`. Ans is `high + 1 + k` or `low + k`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findKthPositive(arr: List[int], k: int) -&gt; int:&#10;    low, high = 0, len(arr) - 1&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        missing = arr[mid] - (mid + 1)&#10;        if missing &lt; k: low = mid + 1&#10;        else: high = mid - 1&#10;    return low + k</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">15</td>
      <td rowspan="1">Bs 15 Aggressive Cows<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/aggressive-cows/0" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Minimax binary search.</td>
      <td><b>Time:</b> O(N log N + N log(Max-Min))<br><b>Space:</b> O(1)</td>
      <td>Optimal: Sort the stalls. Binary search for distance from `1` to `max-min`. For a distance `mid`, check if we can place all `C` cows such that distance between any two is >= `mid`. If possible, move `low = mid + 1` to maximize it, else `high = mid - 1`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def aggressiveCows(stalls: List[int], k: int) -&gt; int:&#10;    stalls.sort()&#10;    def can_place(dist):&#10;        cnt_cows = 1&#10;        last = stalls[0]&#10;        for i in range(1, len(stalls)):&#10;            if stalls[i] - last &gt;= dist:&#10;                cnt_cows += 1&#10;                last = stalls[i]&#10;        return cnt_cows &gt;= k&#10;    low, high = 1, stalls[-1] - stalls[0]&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        if can_place(mid): low = mid + 1&#10;        else: high = mid - 1&#10;    return high</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">16</td>
      <td rowspan="1">Bs 16 Split Array Largest Sum<br><br></b> <a href="https://leetcode.com/problems/split-array-largest-sum/" target="_blank">LeetCode 410</a></td>
      <td rowspan="1"><b>Example 1:</b> Equivalent to allocate books.</td>
      <td><b>Time:</b> O(N log(Sum-Max))<br><b>Space:</b> O(1)</td>
      <td>Optimal: Identical logic to Allocate Books. Binary search from `max(nums)` to `sum(nums)`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def splitArray(nums: List[int], k: int) -&gt; int:&#10;    def count_partitions(max_sum):&#10;        partitions, subarray_sum = 1, 0&#10;        for num in nums:&#10;            if subarray_sum + num &lt;= max_sum:&#10;                subarray_sum += num&#10;            else:&#10;                partitions += 1&#10;                subarray_sum = num&#10;        return partitions&#10;    low, high = max(nums), sum(nums)&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        if count_partitions(mid) &gt; k: low = mid + 1&#10;        else: high = mid - 1&#10;    return low</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">17</td>
      <td rowspan="1">Bs 17 Painters Partition Problem<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/the-painters-partition-problem1535/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Minimax identical to book allocation.</td>
      <td><b>Time:</b> O(N log(Sum-Max))<br><b>Space:</b> O(1)</td>
      <td>Optimal: Identical to Allocate Books and Split Array Largest Sum. Binary search `max(boards)` to `sum(boards)`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findLargestMinDistance(boards: List[int], k: int) -&gt; int:&#10;    def count_painters(time):&#10;        painters, boards_painter = 1, 0&#10;        for b in boards:&#10;            if boards_painter + b &lt;= time:&#10;                boards_painter += b&#10;            else:&#10;                painters += 1&#10;                boards_painter = b&#10;        return painters&#10;    low, high = max(boards), sum(boards)&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        if count_painters(mid) &gt; k: low = mid + 1&#10;        else: high = mid - 1&#10;    return low</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">18</td>
      <td rowspan="1">Bs 18 Minimize Max Distance To Gas Station<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/minimize-max-distance-to-gas-station/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Double binary search.</td>
      <td><b>Time:</b> O(N log(MaxDist / 1e-6))<br><b>Space:</b> O(1)</td>
      <td>Optimal: Binary search on the real answer (distance) with a precision (e.g., 1e-6). For a given `mid` distance, count how many gas stations need to be inserted in each gap: `ceil((stations[i+1] - stations[i]) / mid) - 1`. If total needed > k, `low = mid`, else `high = mid`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findSmallestMaxDist(stations: List[int], k: int) -&gt; float:&#10;    def num_required(dist):&#10;        cnt = 0&#10;        for i in range(1, len(stations)):&#10;            number_in_between = int((stations[i] - stations[i-1]) / dist)&#10;            if (stations[i] - stations[i-1]) == (dist * number_in_between):&#10;                number_in_between -= 1&#10;            cnt += number_in_between&#10;        return cnt&#10;    low, high = 0, 0&#10;    for i in range(len(stations) - 1):&#10;        high = max(high, float(stations[i+1] - stations[i]))&#10;    diff = 1e-6&#10;    while high - low &gt; diff:&#10;        mid = low + (high - low) / 2.0&#10;        if num_required(mid) &gt; k: low = mid&#10;        else: high = mid&#10;    return high</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">19</td>
      <td rowspan="1">Bs 19 Search In A 2D Matrix II<br><br></b> <a href="https://leetcode.com/problems/search-a-2d-matrix-ii/" target="_blank">LeetCode 240</a></td>
      <td rowspan="1"><b>Example 1:</b> Start from top right.</td>
      <td><b>Time:</b> O(N + M)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Start from the top-right corner. If `target == current`, return true. If `target < current`, move left (`c--`). If `target > current`, move down (`r++`).</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def searchMatrix(matrix: List[List[int]], target: int) -&gt; bool:&#10;    r, c = 0, len(matrix[0]) - 1&#10;    while r &lt; len(matrix) and c &gt;= 0:&#10;        if matrix[r][c] == target: return True&#10;        elif matrix[r][c] &gt; target: c -= 1&#10;        else: r += 1&#10;    return False</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">20</td>
      <td rowspan="1">Bs 20 Find A Peak Element II<br><br></b> <a href="https://leetcode.com/problems/find-a-peak-element-ii/" target="_blank">LeetCode 1901</a></td>
      <td rowspan="1"><b>Example 1:</b> Binary search on columns.</td>
      <td><b>Time:</b> O(N log M)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Binary search on columns. Find middle column, find max element in this column. Compare it with its left and right neighbors. If it's > both, it's a peak. If left is greater, peak exists in left half. Else, peak exists in right half.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findPeakGrid(mat: List[List[int]]) -&gt; List[int]:&#10;    n, m = len(mat), len(mat[0])&#10;    low, high = 0, m - 1&#10;    while low &lt;= high:&#10;        mid = (low + high) // 2&#10;        max_row = 0&#10;        for i in range(n):&#10;            if mat[i][mid] &gt; mat[max_row][mid]: max_row = i&#10;        left = mat[max_row][mid-1] if mid - 1 &gt;= 0 else -1&#10;        right = mat[max_row][mid+1] if mid + 1 &lt; m else -1&#10;        if mat[max_row][mid] &gt; left and mat[max_row][mid] &gt; right:&#10;            return [max_row, mid]&#10;        elif mat[max_row][mid] &lt; left:&#10;            high = mid - 1&#10;        else:&#10;            low = mid + 1&#10;    return [-1, -1]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">21</td>
      <td rowspan="1">Bs 21 Matrix Median<br><br></b> <a href="https://www.interviewbit.com/problems/matrix-median/" target="_blank">InterviewBit</a></td>
      <td rowspan="1"><b>Example 1:</b> Binary search on answer range.</td>
      <td><b>Time:</b> O(32 * N log M)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Binary search on the value range `[1, 10^9]`. For a candidate `mid`, count how many numbers are `<= mid` across all rows using `upper_bound`. If count `> (N*M)/2`, `mid` could be median, search lower. Else search higher.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import bisect&#10;def findMedian(A: List[List[int]]) -&gt; int:&#10;    low, high = 1, int(1e9)&#10;    n, m = len(A), len(A[0])&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        cnt = sum(bisect.bisect_right(row, mid) for row in A)&#10;        if cnt &lt;= (n * m) // 2:&#10;            low = mid + 1&#10;        else:&#10;            high = mid - 1&#10;    return low</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">22</td>
      <td rowspan="1">Bs 22 Kth Smallest Number In Multiplication Table<br><br></b> <a href="https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/" target="_blank">LeetCode 668</a></td>
      <td rowspan="1"><b>Example 1:</b> Binary Search on answer.</td>
      <td><b>Time:</b> O(m * log(m*n))<br><b>Space:</b> O(1)</td>
      <td>Optimal: Binary search on range `[1, m*n]`. For a value `mid`, the number of elements `<= mid` in row `i` is `min(mid / i, n)`. Sum this for all rows to get total count. If count >= k, search left. Else search right.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findKthNumber(m: int, n: int, k: int) -&gt; int:&#10;    low, high = 1, m * n&#10;    while low &lt; high:&#10;        mid = low + (high - low) // 2&#10;        count = sum(min(mid // i, n) for i in range(1, m + 1))&#10;        if count &gt;= k:&#10;            high = mid&#10;        else:&#10;            low = mid + 1&#10;    return low</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">23</td>
      <td rowspan="1">Bs 23 Find K Th Smallest Pair Distance<br><br></b> <a href="https://leetcode.com/problems/find-k-th-smallest-pair-distance/" target="_blank">LeetCode 719</a></td>
      <td rowspan="1"><b>Example 1:</b> Sort and binary search on distance.</td>
      <td><b>Time:</b> O(N log N + N log(max_dist))<br><b>Space:</b> O(1)</td>
      <td>Optimal: Sort array. Binary search on distance `[0, nums.back() - nums.front()]`. For a candidate `mid`, count pairs with distance `<= mid` using a sliding window. If count >= k, search left. Else search right.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def smallestDistancePair(nums: List[int], k: int) -&gt; int:&#10;    nums.sort()&#10;    low, high = 0, nums[-1] - nums[0]&#10;    def countPairs(mid):&#10;        count, l = 0, 0&#10;        for r in range(len(nums)):&#10;            while nums[r] - nums[l] &gt; mid: l += 1&#10;            count += (r - l)&#10;        return count&#10;    while low &lt; high:&#10;        mid = low + (high - low) // 2&#10;        if countPairs(mid) &gt;= k:&#10;            high = mid&#10;        else:&#10;            low = mid + 1&#10;    return low</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">24</td>
      <td rowspan="1">Bs 24 Roti Prata Spoj<br><br></b> <a href="https://www.spoj.com/problems/PRATA/" target="_blank">SPOJ</a></td>
      <td rowspan="1"><b>Example 1:</b> Binary Search on Answer.</td>
      <td><b>Time:</b> O(L * log(max_time))<br><b>Space:</b> O(1)</td>
      <td>Optimal: Search space is `0` to `max_time`, where `max_time` is the time taken by the fastest cook to make all `P` pratas alone. `isPossible(mid)` checks if the total pratas made by all cooks in `mid` time is at least `P`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minTime(p: int, rank: List[int]) -&gt; int:&#10;    def isPossible(mid):&#10;        count = 0&#10;        for r in rank:&#10;            time, j = 0, 1&#10;            while time + r * j &lt;= mid:&#10;                count += 1&#10;                time += r * j&#10;                j += 1&#10;            if count &gt;= p: return True&#10;        return count &gt;= p&#10;    low, high = 0, 10**8&#10;    ans = -1&#10;    while low &lt;= high:&#10;        mid = (low + high) // 2&#10;        if isPossible(mid):&#10;            ans = mid&#10;            high = mid - 1&#10;        else:&#10;            low = mid + 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">25</td>
      <td rowspan="1">Bs 25 Double Helix Spoj<br><br></b> <a href="https://www.spoj.com/problems/ANARC05B/" target="_blank">SPOJ</a></td>
      <td rowspan="1"><b>Example 1:</b> Two Pointers / Binary Search.</td>
      <td><b>Time:</b> O(N + M)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Use two pointers to traverse both sorted arrays simultaneously. Accumulate sums `sum1` and `sum2`. When elements match (intersection), add `max(sum1, sum2) + element` to the total answer and reset `sum1` and `sum2`. After the loop, add the remaining max sum.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxPathSum(arr1: List[int], arr2: List[int]) -&gt; int:&#10;    sum1 = sum2 = ans = 0&#10;    i = j = 0&#10;    n, m = len(arr1), len(arr2)&#10;    while i &lt; n and j &lt; m:&#10;        if arr1[i] &lt; arr2[j]:&#10;            sum1 += arr1[i]&#10;            i += 1&#10;        elif arr1[i] &gt; arr2[j]:&#10;            sum2 += arr2[j]&#10;            j += 1&#10;        else:&#10;            ans += max(sum1, sum2) + arr1[i]&#10;            sum1, sum2 = 0, 0&#10;            i += 1; j += 1&#10;    while i &lt; n:&#10;        sum1 += arr1[i]&#10;        i += 1&#10;    while j &lt; m:&#10;        sum2 += arr2[j]&#10;        j += 1&#10;    ans += max(sum1, sum2)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">26</td>
      <td rowspan="1">Bs 26 Subset Sums Spoj<br><br></b> <a href="https://www.spoj.com/problems/SUBSUMS/" target="_blank">SPOJ</a></td>
      <td rowspan="1"><b>Example 1:</b> Meet in the Middle.</td>
      <td><b>Time:</b> O(2^(N/2) * log(2^(N/2)))<br><b>Space:</b> O(2^(N/2))</td>
      <td>Optimal: Divide the array into two halves. Find all possible subset sums for both halves (`sum1` and `sum2`). Sort `sum2`. For each sum in `sum1`, we need to find the number of elements in `sum2` that satisfy `A - sum <= x <= B - sum`. This can be done using Binary Search (`upper_bound` - `lower_bound`).</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import bisect&#10;def solve(arr: List[int], A: int, B: int) -&gt; int:&#10;    n = len(arr)&#10;    def get_sums(arr_slice):&#10;        sums = [0]&#10;        for x in arr_slice:&#10;            sums += [s + x for s in sums]&#10;        return sums&#10;    left = get_sums(arr[:n//2])&#10;    right = sorted(get_sums(arr[n//2:]))&#10;    count = 0&#10;    for x in left:&#10;        low = bisect.bisect_left(right, A - x)&#10;        high = bisect.bisect_right(right, B - x)&#10;        count += (high - low)&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">27</td>
      <td rowspan="1">Bs 27 Smallest Factorial Number<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/smallest-factorial-number5929/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Binary Search.</td>
      <td><b>Time:</b> O(log_5(N) * log(5*N))<br><b>Space:</b> O(1)</td>
      <td>Optimal: Trailing zeros depend on number of 5s. Find count of 5s in `mid!`. Use binary search on the number. Low = 0, high = 5*N. If `check(mid) >= n`, `ans = mid` and `high = mid - 1`. Else `low = mid + 1`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findNum(n: int) -&gt; int:&#10;    if n == 1: return 5&#10;    def check(p):&#10;        count, f = 0, 5&#10;        while f &lt;= p:&#10;            count += p // f&#10;            f *= 5&#10;        return count &gt;= n&#10;    low, high = 0, 5 * n&#10;    ans = 0&#10;    while low &lt;= high:&#10;        mid = (low + high) // 2&#10;        if check(mid):&#10;            ans = mid&#10;            high = mid - 1&#10;        else:&#10;            low = mid + 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">28</td>
      <td rowspan="1">Bs 28 Value Equal To Index Value<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/value-equal-to-index-value1330/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Linear scan.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Iterate through the array. If the value at `i` is equal to `i + 1`, append it to the result array.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def valueEqualToIndex(arr, n):&#10;    ans = []&#10;    for i in range(n):&#10;        if arr[i] == i + 1:&#10;            ans.append(arr[i])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">29</td>
      <td rowspan="1">Bs 29 Count Squares<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/count-squares3649/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Square root.</td>
      <td><b>Time:</b> O(1)<br><b>Space:</b> O(1)</td>
      <td>Optimal: The number of perfect squares less than `N` is equal to `sqrt(N - 1)` rounded down.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import math&#10;def countSquares(N):&#10;    return int(math.sqrt(N - 1))</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">30</td>
      <td rowspan="1">Bs 30 Middle Of Three<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/middle-of-three2926/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Simple if-else.</td>
      <td><b>Time:</b> O(1)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Compare the numbers. If A is between B and C, return A. If B is between A and C, return B. Else return C.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def middle(A, B, C):&#10;    if (A &lt; B and B &lt; C) or (C &lt; B and B &lt; A): return B&#10;    if (B &lt; A and A &lt; C) or (C &lt; A and A &lt; B): return A&#10;    return C</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">31</td>
      <td rowspan="1">Bs 31 Majority Element<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/majority-element-1587115620/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Moore's Voting Algorithm.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Use Moore's Voting Algorithm to find a candidate for majority element. Then count the occurrences of the candidate in the array to verify if it appears more than N/2 times.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def majorityElement(a, size):&#10;    count = 0&#10;    candidate = -1&#10;    for num in a:&#10;        if count == 0:&#10;            candidate = num&#10;            count = 1&#10;        elif num == candidate: count += 1&#10;        else: count -= 1&#10;    count = 0&#10;    for num in a:&#10;        if num == candidate: count += 1&#10;    return candidate if count &gt; size // 2 else -1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">32</td>
      <td rowspan="1">Bs 32 Searching In An Array Where Adjacent Differ By At Most K<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/searching-in-an-array-where-adjacent-differ-by-at-most-k0456/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Jump Search.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Instead of linear search, we can jump ahead. The minimum jump we can make from index `i` to reach `x` is `abs(arr[i] - x) / k`. We jump this amount and check if we found it. Make sure jump is at least 1.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def search(arr, n, x, k):&#10;    i = 0&#10;    while i &lt; n:&#10;        if arr[i] == x: return i&#10;        i = i + max(1, abs(arr[i] - x) // k)&#10;    return -1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">33</td>
      <td rowspan="1">Bs 33 Find A Pair With The Given Difference<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/find-pair-given-difference1559/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Sort and two pointers.</td>
      <td><b>Time:</b> O(L log L)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Sort the array. Use two pointers `i = 0` and `j = 1`. If `arr[j] - arr[i] == N` and `i != j`, return true. If difference < N, `j++`. Else `i++`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findPair(arr, size, n):&#10;    arr.sort()&#10;    i, j = 0, 1&#10;    while i &lt; size and j &lt; size:&#10;        if i != j and arr[j] - arr[i] == n: return True&#10;        elif arr[j] - arr[i] &lt; n: j += 1&#10;        else: i += 1&#10;    return False</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">34</td>
      <td rowspan="1">Bs 34 Find Four Elements That Sum To A Given Value<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/find-all-four-sum-numbers1732/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Two loops and two pointers.</td>
      <td><b>Time:</b> O(N^3)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Sort the array. Use two nested loops for the first two elements. Then use two pointers for the remaining two elements to find the target sum. Skip duplicates at all levels.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def fourSum(arr, k):&#10;    ans = []&#10;    n = len(arr)&#10;    arr.sort()&#10;    for i in range(n):&#10;        if i &gt; 0 and arr[i] == arr[i-1]: continue&#10;        for j in range(i + 1, n):&#10;            if j &gt; i + 1 and arr[j] == arr[j-1]: continue&#10;            left, right = j + 1, n - 1&#10;            while left &lt; right:&#10;                total = arr[i] + arr[j] + arr[left] + arr[right]&#10;                if total == k:&#10;                    ans.append([arr[i], arr[j], arr[left], arr[right]])&#10;                    left += 1; right -= 1&#10;                    while left &lt; right and arr[left] == arr[left-1]: left += 1&#10;                    while left &lt; right and arr[right] == arr[right+1]: right -= 1&#10;                elif total &lt; k: left += 1&#10;                else: right -= 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">35</td>
      <td rowspan="1">Bs 35 Find Nth Root Of M<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/find-nth-root-of-m5843/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Binary Search.</td>
      <td><b>Time:</b> O(N * log M)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Search space is `[1, m]`. Check `mid^n`. Since `mid^n` can overflow, use a custom power function that returns 1 if `mid^n == m`, 0 if `< m`, and 2 if `> m`. Adjust `low` and `high` accordingly.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def NthRoot(n, m):&#10;    def func(mid, n, m):&#10;        ans = 1&#10;        for _ in range(n):&#10;            ans *= mid&#10;            if ans &gt; m: return 2&#10;        if ans == m: return 1&#10;        return 0&#10;    low, high = 1, m&#10;    while low &lt;= high:&#10;        mid = (low + high) // 2&#10;        midN = func(mid, n, m)&#10;        if midN == 1: return mid&#10;        elif midN == 0: low = mid + 1&#10;        else: high = mid - 1&#10;    return -1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">36</td>
      <td rowspan="1">Bs 36 Row With Max 1S<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/row-with-max-1s0023/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Lower Bound per row.</td>
      <td><b>Time:</b> O(N log M)<br><b>Space:</b> O(1)</td>
      <td>Optimal: Since rows are sorted, use binary search (`lower_bound` of 1) to find the first index of 1 in each row. The number of 1s is `m - index`. Keep track of the row with the maximum 1s.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def rowWithMax1s(arr, n, m):&#10;    def lowerBound(a, m, x):&#10;        low, high, ans = 0, m - 1, m&#10;        while low &lt;= high:&#10;            mid = (low + high) // 2&#10;            if a[mid] &gt;= x:&#10;                ans = mid&#10;                high = mid - 1&#10;            else:&#10;                low = mid + 1&#10;        return ans&#10;    max_cnt = 0&#10;    index = -1&#10;    for i in range(n):&#10;        cnt_ones = m - lowerBound(arr[i], m, 1)&#10;        if cnt_ones &gt; max_cnt:&#10;            max_cnt = cnt_ones&#10;            index = i&#10;    return index</code></pre></details></td>
    </tr>
  </tbody>
</table>


## Recursion

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
      <td rowspan="1">1</td>
      <td rowspan="1">Rec 01 Combination Sum<br><br></b> <a href="https://leetcode.com/problems/combination-sum/" target="_blank">LeetCode 39</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> candidates = [2,3,6,7], target = 7<br><b>Output:</b> [[2,2,3],[7]]<br><br><b>Note (Constraint):</b> The same number may be chosen unlimited number of times.</td>
      <td><b>Time:</b> O(2<sup>T</sup>) (Trade-off)<br><b>Space:</b> O(T) (Trade-off)</td>
      <td>Pick/Non-Pick but when picking, we *do not* increment the index `i`, allowing the same element to be picked infinitely until `target < 0`.</td>
      <td><b>Edge Cases:</b> <b>Infinite Loop Prevention:</b> Base cases must immediately return if `target < 0` to prevent infinite recursion on the same index.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def combination_sum(candidates: list[int], target: int) -&gt; list[list[int]]:&#10;    ans = []&#10;    def solve(i, current_target, temp):&#10;        if i == len(candidates):&#10;            if current_target == 0:&#10;                ans.append(temp.copy())&#10;            return&#10;            &#10;        if candidates[i] &lt;= current_target:&#10;            temp.append(candidates[i])&#10;            solve(i, current_target - candidates[i], temp)&#10;            temp.pop()&#10;            &#10;        solve(i + 1, current_target, temp)&#10;        &#10;    solve(0, target, [])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">2</td>
      <td rowspan="1">Rec 02 N Queens<br><br></b> <a href="https://leetcode.com/problems/n-queens/" target="_blank">LeetCode 51</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> n = 4<br><b>Output:</b> [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]<br><br><b>Note (Constraint):</b> 1 &le; n &le; 9</td>
      <td><b>Time:</b> O(N!) (Constraint)<br><b>Space:</b> O(N) (Constraint)</td>
      <td>Backtracking. Try placing a queen in each row of the current column. Use `O(1)` lookups (Hashing logic) via arrays to check if row/diagonals are safe.<br><br><b>Dependencies:</b> Hash Maps/Arrays for safety checks</td>
      <td><b>Edge Cases:</b> <b>Diagonal Math:</b> Lower diagonal is tracked via `row + col`, Upper diagonal via `(n - 1) + (col - row)`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def solve_n_queens(n: int) -&gt; list[list[str]]:&#10;    ans = []&#10;    board = [[&quot;.&quot;] * n for _ in range(n)]&#10;    left_row = [0] * n&#10;    upper_diag = [0] * (2 * n - 1)&#10;    lower_diag = [0] * (2 * n - 1)&#10;    &#10;    def solve(col):&#10;        if col == n:&#10;            ans.append([&quot;&quot;.join(row) for row in board])&#10;            return&#10;            &#10;        for row in range(n):&#10;            if left_row[row] == 0 and lower_diag[row + col] == 0 and upper_diag[n - 1 + col - row] == 0:&#10;                board[row][col] = &#x27;Q&#x27;&#10;                left_row[row] = 1&#10;                lower_diag[row + col] = 1&#10;                upper_diag[n - 1 + col - row] = 1&#10;                &#10;                solve(col + 1)&#10;                &#10;                board[row][col] = &#x27;.&#x27;&#10;                left_row[row] = 0&#10;                lower_diag[row + col] = 0&#10;                upper_diag[n - 1 + col - row] = 0&#10;                &#10;    solve(0)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">3</td>
      <td rowspan="1">Rec 03 Permutations<br><br></b> <a href="https://leetcode.com/problems/permutations/" target="_blank">LeetCode 46</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> nums = [1,2,3]<br><b>Output:</b> [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]</td>
      <td><b>Time:</b> O(N! * N)<br><b>Space:</b> O(N)</td>
      <td>Backtracking. Swap elements to generate permutations. For index `i`, swap it with every index from `i` to `n-1`, recurse, then backtrack (swap back).<br><br><b>Dependencies:</b> <code>std::swap</code></td>
      <td><b>Edge Cases:</b> <b>Backtracking necessity:</b> Without the second swap (backtrack), the array remains mutated for subsequent sibling recursion branches.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def permute(nums: list[int]) -&gt; list[list[int]]:&#10;    ans = []&#10;    def solve(idx):&#10;        if idx == len(nums):&#10;            ans.append(nums[:])&#10;            return&#10;        for i in range(idx, len(nums)):&#10;            nums[idx], nums[i] = nums[i], nums[idx]&#10;            solve(idx + 1)&#10;            nums[idx], nums[i] = nums[i], nums[idx]&#10;    solve(0)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">4</td>
      <td rowspan="1">Rec 04 Sudoku Solver<br><br></b> <a href="https://leetcode.com/problems/sudoku-solver/" target="_blank">LeetCode 37</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> board with '.' for empty cells. Solve in-place.</td>
      <td><b>Time:</b> O(9^(n*n))<br><b>Space:</b> O(1) auxiliary</td>
      <td>Backtracking. Find first empty cell, try placing 1-9. Validate row, col, and 3x3 sub-grid. Recursively solve the rest. If it fails, backtrack.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def solveSudoku(board: List[List[str]]) -&gt; None:&#10;    def isValid(row, col, ch):&#10;        for i in range(9):&#10;            if board[i][col] == ch: return False&#10;            if board[row][i] == ch: return False&#10;            if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == ch: return False&#10;        return True&#10;    def solve():&#10;        for i in range(len(board)):&#10;            for j in range(len(board[0])):&#10;                if board[i][j] == &#x27;.&#x27;:&#10;                    for c in &#x27;123456789&#x27;:&#10;                        if isValid(i, j, c):&#10;                            board[i][j] = c&#10;                            if solve(): return True&#10;                            else: board[i][j] = &#x27;.&#x27;&#10;                    return False&#10;        return True&#10;    solve()</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">5</td>
      <td rowspan="1">Rec 05 M Coloring Problem<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/m-coloring-problem-1587115620/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Return true if possible.</td>
      <td><b>Time:</b> O(M^N)<br><b>Space:</b> O(N)</td>
      <td>Backtracking. Try coloring each node with color 1 to m. For a color, check if any adjacent node has the same color. If safe, assign and recurse for next node. If recursion returns false, backtrack.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def graphColoring(graph: List[List[int]], m: int, n: int) -&gt; bool:&#10;    color = [0] * n&#10;    def isSafe(node, col):&#10;        for k in range(n):&#10;            if k != node and graph[k][node] == 1 and color[k] == col: return False&#10;        return True&#10;    def solve(node):&#10;        if node == n: return True&#10;        for i in range(1, m + 1):&#10;            if isSafe(node, i):&#10;                color[node] = i&#10;                if solve(node + 1): return True&#10;                color[node] = 0&#10;        return False&#10;    return solve(0)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">6</td>
      <td rowspan="1">Rec 06 Rat In A Maze<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Lexicographical order paths.</td>
      <td><b>Time:</b> O(4^(N*N))<br><b>Space:</b> O(N*N)</td>
      <td>Backtracking. Explore 4 directions (D, L, R, U) in lexicographical order to get sorted paths naturally. Mark cell as visited, recurse, then unmark (backtrack).</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findPath(m: List[List[int]], n: int) -&gt; List[str]:&#10;    ans = []&#10;    vis = [[0 for _ in range(n)] for _ in range(n)]&#10;    di = [1, 0, 0, -1]&#10;    dj = [0, -1, 1, 0]&#10;    dir_str = &quot;DLRU&quot;&#10;    def solve(i, j, move):&#10;        if i == n - 1 and j == n - 1:&#10;            ans.append(move)&#10;            return&#10;        for ind in range(4):&#10;            nexti, nextj = i + di[ind], j + dj[ind]&#10;            if 0 &lt;= nexti &lt; n and 0 &lt;= nextj &lt; n and not vis[nexti][nextj] and m[nexti][nextj] == 1:&#10;                vis[i][j] = 1&#10;                solve(nexti, nextj, move + dir_str[ind])&#10;                vis[i][j] = 0&#10;    if m[0][0] == 1: solve(0, 0, &quot;&quot;)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">7</td>
      <td rowspan="1">Rec 07 Word Break<br><br></b> <a href="https://leetcode.com/problems/word-break/" target="_blank">LeetCode 139</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> s = 'leetcode', wordDict = ['leet','code']<br><b>Output:</b> true</td>
      <td><b>Time:</b> O(N^3)<br><b>Space:</b> O(N)</td>
      <td>Recursion with Memoization (or DP). For each index, try all possible word lengths. If a prefix exists in dict, recurse for the suffix. DP array `dp[i]` stores if `s[0...i-1]` is valid.<br><br><b>Dependencies:</b> <code>#include <unordered_set></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def wordBreak(s: str, wordDict: List[str]) -&gt; bool:&#10;    word_set = set(wordDict)&#10;    dp = [False] * (len(s) + 1)&#10;    dp[0] = True&#10;    for i in range(1, len(s) + 1):&#10;        for j in range(i):&#10;            if dp[j] and s[j:i] in word_set:&#10;                dp[i] = True&#10;                break&#10;    return dp[-1]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">8</td>
      <td rowspan="1">Rec 08 Word Break II<br><br></b> <a href="https://leetcode.com/problems/word-break-ii/" target="_blank">LeetCode 140</a></td>
      <td rowspan="1"><b>Example 1:</b> Return list of sentences.</td>
      <td><b>Time:</b> O(2^N)<br><b>Space:</b> O(2^N)</td>
      <td>Backtracking. Generate all combinations. At each step, if a prefix is in dict, recursively call for the rest of the string and append the prefix to the result of the recursive call.<br><br><b>Dependencies:</b> <code>#include <unordered_set></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def wordBreak(s: str, wordDict: List[str]) -&gt; List[str]:&#10;    word_set = set(wordDict)&#10;    memo = {}&#10;    def solve(s):&#10;        if s in memo: return memo[s]&#10;        if not s: return [&quot;&quot;]&#10;        res = []&#10;        for i in range(1, len(s) + 1):&#10;            word = s[:i]&#10;            if word in word_set:&#10;                rem = solve(s[i:])&#10;                for st in rem:&#10;                    res.append(word + (&quot; &quot; if st else &quot;&quot;) + st)&#10;        memo[s] = res&#10;        return res&#10;    return solve(s)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">9</td>
      <td rowspan="1">Rec 09 Palindrome Partitioning<br><br></b> <a href="https://leetcode.com/problems/palindrome-partitioning/" target="_blank">LeetCode 131</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> s = 'aab'<br><b>Output:</b> [['a','a','b'],['aa','b']]</td>
      <td><b>Time:</b> O(N * 2^N)<br><b>Space:</b> O(N)</td>
      <td>Backtracking. Try to partition the string at every index. If the prefix `s[start:i]` is a palindrome, add it to current path and recurse for the rest of the string `s[i:end]`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def partition(s: str) -&gt; List[List[str]]:&#10;    res = []&#10;    path = []&#10;    def isPalindrome(s, start, end):&#10;        while start &lt;= end:&#10;            if s[start] != s[end]: return False&#10;            start += 1; end -= 1&#10;        return True&#10;    def solve(index):&#10;        if index == len(s):&#10;            res.append(list(path))&#10;            return&#10;        for i in range(index, len(s)):&#10;            if isPalindrome(s, index, i):&#10;                path.append(s[index:i+1])&#10;                solve(i + 1)&#10;                path.pop()&#10;    solve(0)&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">10</td>
      <td rowspan="1">Rec 10 Expression Add Operators<br><br></b> <a href="https://leetcode.com/problems/expression-add-operators/" target="_blank">LeetCode 282</a></td>
      <td rowspan="1"><b>Example 1:</b> Return expressions.</td>
      <td><b>Time:</b> O(N * 4^N)<br><b>Space:</b> O(N)</td>
      <td>Backtracking. Keep track of the evaluated sum so far, and the previous operand (for multiplication precedence). For '*', `newSum = sum - prev + prev * curr`. Handle leading zeros.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def addOperators(num: str, target: int) -&gt; List[str]:&#10;    ans = []&#10;    def solve(ind, path, eval_sum, multed):&#10;        if ind == len(num):&#10;            if eval_sum == target: ans.append(path)&#10;            return&#10;        for i in range(ind, len(num)):&#10;            if i != ind and num[ind] == &#x27;0&#x27;: break&#10;            cur_str = num[ind:i+1]&#10;            cur_num = int(cur_str)&#10;            if ind == 0:&#10;                solve(i + 1, path + cur_str, cur_num, cur_num)&#10;            else:&#10;                solve(i + 1, path + &quot;+&quot; + cur_str, eval_sum + cur_num, cur_num)&#10;                solve(i + 1, path + &quot;-&quot; + cur_str, eval_sum - cur_num, -cur_num)&#10;                solve(i + 1, path + &quot;*&quot; + cur_str, eval_sum - multed + multed * cur_num, multed * cur_num)&#10;    solve(0, &quot;&quot;, 0, 0)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">11</td>
      <td rowspan="1">Rec 11 Subset Sums II<br><br></b> <a href="https://leetcode.com/problems/subsets-ii/" target="_blank">LeetCode 90</a></td>
      <td rowspan="1"><b>Example 1:</b><br><b>Output:</b> [[],[1],[1,2],[1,2,2],[2],[2,2]]</td>
      <td><b>Time:</b> O(2^N * N)<br><b>Space:</b> O(2^N * N)</td>
      <td>Sort array first to bring duplicates together. In recursive call, loop from `ind` to `n`. If `i > ind` and `nums[i] == nums[i-1]`, `continue` to skip duplicate recursive branches.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def subsetsWithDup(nums: List[int]) -&gt; List[List[int]]:&#10;    ans = []&#10;    nums.sort()&#10;    def findSubsets(ind, ds):&#10;        ans.append(list(ds))&#10;        for i in range(ind, len(nums)):&#10;            if i != ind and nums[i] == nums[i-1]: continue&#10;            ds.append(nums[i])&#10;            findSubsets(i + 1, ds)&#10;            ds.pop()&#10;    findSubsets(0, [])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">12</td>
      <td rowspan="1">Rec 12 Combination Sum II<br><br></b> <a href="https://leetcode.com/problems/combination-sum-ii/" target="_blank">LeetCode 40</a></td>
      <td rowspan="1"><b>Example 1:</b> Return unique combinations.</td>
      <td><b>Time:</b> O(2^N * k)<br><b>Space:</b> O(k * x)</td>
      <td>Sort the array. Recursive function iterates from `ind` to `n`. Skip duplicates (`if i > ind and arr[i] == arr[i-1]`). If `arr[i] > target`, break. Else add to path, subtract from target, and recurse.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def combinationSum2(candidates: List[int], target: int) -&gt; List[List[int]]:&#10;    ans = []&#10;    candidates.sort()&#10;    def findCombinations(ind, target, ds):&#10;        if target == 0:&#10;            ans.append(list(ds))&#10;            return&#10;        for i in range(ind, len(candidates)):&#10;            if i &gt; ind and candidates[i] == candidates[i-1]: continue&#10;            if candidates[i] &gt; target: break&#10;            ds.append(candidates[i])&#10;            findCombinations(i + 1, target - candidates[i], ds)&#10;            ds.pop()&#10;    findCombinations(0, target, [])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">13</td>
      <td rowspan="1">Rec 13 Combination Sum III<br><br></b> <a href="https://leetcode.com/problems/combination-sum-iii/" target="_blank">LeetCode 216</a></td>
      <td rowspan="1"><b>Example 1:</b> Return combinations.</td>
      <td><b>Time:</b> O(2^9)<br><b>Space:</b> O(k)</td>
      <td>Backtracking. Start from 1, go up to 9. Add the current number to the path and subtract from target. Stop when path size is `k` and `target` is 0.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def combinationSum3(k: int, n: int) -&gt; List[List[int]]:&#10;    ans = []&#10;    def solve(start, k, n, ds):&#10;        if k == 0 and n == 0:&#10;            ans.append(list(ds))&#10;            return&#10;        if k == 0 or n &lt; 0: return&#10;        for i in range(start, 10):&#10;            ds.append(i)&#10;            solve(i + 1, k - 1, n - i, ds)&#10;            ds.pop()&#10;    solve(1, k, n, [])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">14</td>
      <td rowspan="1">Rec 14 Letter Combinations Of A Phone Number<br><br></b> <a href="https://leetcode.com/problems/letter-combinations-of-a-phone-number/" target="_blank">LeetCode 17</a></td>
      <td rowspan="1"><b>Example 1:</b> String combinations.</td>
      <td><b>Time:</b> O(4^N * N)<br><b>Space:</b> O(N)</td>
      <td>Backtracking. Create a mapping of digit to letters. Iterate through digits, for each digit loop through its mapped letters, append to current string, and recurse.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def letterCombinations(digits: str) -&gt; List[str]:&#10;    if not digits: return []&#10;    ans = []&#10;    mapping = [&quot;&quot;, &quot;&quot;, &quot;abc&quot;, &quot;def&quot;, &quot;ghi&quot;, &quot;jkl&quot;, &quot;mno&quot;, &quot;pqrs&quot;, &quot;tuv&quot;, &quot;wxyz&quot;]&#10;    def solve(ind, path):&#10;        if ind == len(digits):&#10;            ans.append(path)&#10;            return&#10;        number = int(digits[ind])&#10;        value = mapping[number]&#10;        for i in range(len(value)):&#10;            solve(ind + 1, path + value[i])&#10;    solve(0, &quot;&quot;)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">15</td>
      <td rowspan="1">Rec 15 Subset Sum I<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/subset-sums2234/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Take / Not Take.</td>
      <td><b>Time:</b> O(2^N)<br><b>Space:</b> O(2^N)</td>
      <td>Recursively either include `arr[ind]` in sum, or exclude it. If `ind == N`, add `sum` to result array.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def subsetSums(arr: List[int], N: int) -&gt; List[int]:&#10;    sumSubset = []&#10;    def func(ind, current_sum):&#10;        if ind == N:&#10;            sumSubset.append(current_sum)&#10;            return&#10;        func(ind + 1, current_sum + arr[ind])&#10;        func(ind + 1, current_sum)&#10;    func(0, 0)&#10;    sumSubset.sort()&#10;    return sumSubset</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">16</td>
      <td rowspan="1">Rec 16 N Queens II<br><br></b> <a href="https://leetcode.com/problems/n-queens-ii/" target="_blank">LeetCode 52</a></td>
      <td rowspan="1"><b>Example 1:</b> Backtracking with hashing.</td>
      <td><b>Time:</b> O(N!)<br><b>Space:</b> O(N)</td>
      <td>Use backtracking to place queens column by column. Use three hash arrays (or bitmasks) to track attacked rows, upper diagonals, and lower diagonals. If placing a queen is safe, update hashes, recurse for next column, and then backtrack.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def totalNQueens(n: int) -&gt; int:&#10;    count = 0&#10;    leftRow = [0] * n&#10;    upperDiag = [0] * (2 * n - 1)&#10;    lowerDiag = [0] * (2 * n - 1)&#10;    def solve(col):&#10;        nonlocal count&#10;        if col == n:&#10;            count += 1&#10;            return&#10;        for row in range(n):&#10;            if leftRow[row] == 0 and lowerDiag[row + col] == 0 and upperDiag[n - 1 + col - row] == 0:&#10;                leftRow[row] = 1&#10;                lowerDiag[row + col] = 1&#10;                upperDiag[n - 1 + col - row] = 1&#10;                solve(col + 1)&#10;                leftRow[row] = 0&#10;                lowerDiag[row + col] = 0&#10;                upperDiag[n - 1 + col - row] = 0&#10;    solve(0)&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">17</td>
      <td rowspan="1">Rec 17 Word Search<br><br></b> <a href="https://leetcode.com/problems/word-search/" target="_blank">LeetCode 79</a></td>
      <td rowspan="1"><b>Example 1:</b> Backtracking DFS.</td>
      <td><b>Time:</b> O(N * M * 4^L)<br><b>Space:</b> O(L) recursion stack</td>
      <td>Start DFS from each cell that matches the first letter of the word. In DFS, check 4 neighbors. Mark current cell as visited (e.g. change to '#') before moving to neighbors, and unmark (backtrack) after exploring.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def exist(board: List[List[str]], word: str) -&gt; bool:&#10;    def dfs(i, j, idx):&#10;        if idx == len(word): return True&#10;        if i &lt; 0 or i &gt;= len(board) or j &lt; 0 or j &gt;= len(board[0]) or board[i][j] != word[idx]:&#10;            return False&#10;        temp = board[i][j]&#10;        board[i][j] = &#x27;#&#x27;&#10;        found = (dfs(i+1, j, idx+1) or dfs(i-1, j, idx+1) or&#10;                 dfs(i, j+1, idx+1) or dfs(i, j-1, idx+1))&#10;        board[i][j] = temp&#10;        return found&#10;    for i in range(len(board)):&#10;        for j in range(len(board[0])):&#10;            if board[i][j] == word[0] and dfs(i, j, 0):&#10;                return True&#10;    return False</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">18</td>
      <td rowspan="1">Rec 18 K Th Symbol In Grammar<br><br></b> <a href="https://leetcode.com/problems/k-th-symbol-in-grammar/" target="_blank">LeetCode 779</a></td>
      <td rowspan="1"><b>Example 1:</b> Recursive division.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Row N has length 2^(N-1). The first half of row N is exactly same as row N-1. The second half of row N is the complement of row N-1. If k is in the first half (k <= mid), return solve(N-1, k). If k is in the second half, return !solve(N-1, k - mid).</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def kthGrammar(n: int, k: int) -&gt; int:&#10;    if n == 1 and k == 1: return 0&#10;    mid = 2 ** (n - 2)&#10;    if k &lt;= mid:&#10;        return kthGrammar(n - 1, k)&#10;    else:&#10;        return 1 - kthGrammar(n - 1, k - mid)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">19</td>
      <td rowspan="1">Rec 19 Beautiful Arrangement<br><br></b> <a href="https://leetcode.com/problems/beautiful-arrangement/" target="_blank">LeetCode 526</a></td>
      <td rowspan="1"><b>Example 1:</b> Backtracking.</td>
      <td><b>Time:</b> O(K) where K is number of valid permutations<br><b>Space:</b> O(N)</td>
      <td>Use an array to track visited numbers. Iterate from index 1 to n. For the current index, try placing an unvisited number. Check if the condition `(num % idx == 0 || idx % num == 0)` is met. If so, mark as visited, recurse to `idx + 1`, then backtrack.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def countArrangement(n: int) -&gt; int:&#10;    count = 0&#10;    visited = [0] * (n + 1)&#10;    def solve(idx):&#10;        nonlocal count&#10;        if idx &gt; n:&#10;            count += 1&#10;            return&#10;        for i in range(1, n + 1):&#10;            if not visited[i] and (i % idx == 0 or idx % i == 0):&#10;                visited[i] = 1&#10;                solve(idx + 1)&#10;                visited[i] = 0&#10;    solve(1)&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">20</td>
      <td rowspan="1">Rec 20 Print All Permutations Of A String<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/permutations-of-a-given-string2041/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Recursive Backtracking.</td>
      <td><b>Time:</b> O(N! * N)<br><b>Space:</b> O(N)</td>
      <td>Convert string to char array and sort it. Use backtracking: pass a boolean visited array and a temporary string. If temporary string length equals original length, add to answer. Else, iterate through characters. To avoid duplicates, if `i > 0` and `s[i] == s[i-1]` and `!vis[i-1]`, skip. Otherwise, mark visited, append, recurse, unmark, pop.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def find_permutation(S: str) -&gt; List[str]:&#10;    S = sorted(list(S))&#10;    ans = []&#10;    vis = [False] * len(S)&#10;    def solve(curr):&#10;        if len(curr) == len(S):&#10;            ans.append(&quot;&quot;.join(curr))&#10;            return&#10;        for i in range(len(S)):&#10;            if vis[i] or (i &gt; 0 and S[i] == S[i-1] and not vis[i-1]):&#10;                continue&#10;            vis[i] = True&#10;            curr.append(S[i])&#10;            solve(curr)&#10;            curr.pop()&#10;            vis[i] = False&#10;    solve([])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">21</td>
      <td rowspan="1">Rec 21 Remove Invalid Parentheses<br><br></b> <a href="https://leetcode.com/problems/remove-invalid-parentheses/" target="_blank">LeetCode 301</a></td>
      <td rowspan="1"><b>Example 1:</b> Recursion and Backtracking.</td>
      <td><b>Time:</b> O(2^N)<br><b>Space:</b> O(N)</td>
      <td>First find the number of misplaced left (`rm_l`) and right (`rm_r`) parentheses. Then use backtracking to try removing `rm_l` and `rm_r` parentheses. To avoid duplicates, skip identical adjacent characters. Finally, check if the resulting string is valid.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def removeInvalidParentheses(s: str) -&gt; List[str]:&#10;    def is_valid(s):&#10;        count = 0&#10;        for c in s:&#10;            if c == &#x27;(&#x27;: count += 1&#10;            elif c == &#x27;)&#x27;: count -= 1&#10;            if count &lt; 0: return False&#10;        return count == 0&#10;    rm_l, rm_r = 0, 0&#10;    for c in s:&#10;        if c == &#x27;(&#x27;: rm_l += 1&#10;        elif c == &#x27;)&#x27;:&#10;            if rm_l &gt; 0: rm_l -= 1&#10;            else: rm_r += 1&#10;    ans = []&#10;    def solve(s, start, rm_l, rm_r):&#10;        if rm_l == 0 and rm_r == 0:&#10;            if is_valid(s): ans.append(s)&#10;            return&#10;        for i in range(start, len(s)):&#10;            if i != start and s[i] == s[i-1]: continue&#10;            if s[i] == &#x27;(&#x27; and rm_l &gt; 0:&#10;                solve(s[:i] + s[i+1:], i, rm_l - 1, rm_r)&#10;            elif s[i] == &#x27;)&#x27; and rm_r &gt; 0:&#10;                solve(s[:i] + s[i+1:], i, rm_l, rm_r - 1)&#10;    solve(s, 0, rm_l, rm_r)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">22</td>
      <td rowspan="1">Rec 22 Matchsticks To Square<br><br></b> <a href="https://leetcode.com/problems/matchsticks-to-square/" target="_blank">LeetCode 473</a></td>
      <td rowspan="1"><b>Example 1:</b> Backtracking to 4 subsets.</td>
      <td><b>Time:</b> O(4^N)<br><b>Space:</b> O(N)</td>
      <td>Calculate sum. If sum % 4 != 0, return false. Target side length is sum / 4. Sort matchsticks in descending order to optimize. Create an array `sides` of size 4. For each matchstick, try adding it to one of the 4 sides. If a side equals the target or is less, recurse.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def makesquare(matchsticks: List[int]) -&gt; bool:&#10;    total = sum(matchsticks)&#10;    if total % 4 != 0 or len(matchsticks) &lt; 4: return False&#10;    target = total // 4&#10;    matchsticks.sort(reverse=True)&#10;    sides = [0] * 4&#10;    def solve(ind):&#10;        if ind == len(matchsticks):&#10;            return sides[0] == sides[1] == sides[2] == target&#10;        for i in range(4):&#10;            if sides[i] + matchsticks[ind] &lt;= target:&#10;                sides[i] += matchsticks[ind]&#10;                if solve(ind + 1): return True&#10;                sides[i] -= matchsticks[ind]&#10;            if sides[i] == 0: break&#10;        return False&#10;    return solve(0)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">23</td>
      <td rowspan="1">Rec 23 Tug Of War<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/tug-of-war/0" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Recursive Backtracking.</td>
      <td><b>Time:</b> O(2^N)<br><b>Space:</b> O(N)</td>
      <td>Keep track of the number of elements included in subset 1 and their sum. Recurse by including the current element in subset 1 or subset 2. Base case: if we reach end, check if subset 1 has `n/2` elements. If so, compute difference and update global minimum.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def tugOfWar(arr: List[int]) -&gt; int:&#10;    n = len(arr)&#10;    totalSum = sum(arr)&#10;    minDiff = [float(&#x27;inf&#x27;)]&#10;    def solve(ind, cnt, sum1):&#10;        if ind == n:&#10;            if cnt == n // 2:&#10;                sum2 = totalSum - sum1&#10;                minDiff[0] = min(minDiff[0], abs(sum1 - sum2))&#10;            return&#10;        if cnt &lt; n // 2:&#10;            solve(ind + 1, cnt + 1, sum1 + arr[ind])&#10;        solve(ind + 1, cnt, sum1)&#10;    solve(0, 0, 0)&#10;    return minDiff[0]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">24</td>
      <td rowspan="1">Rec 24 Find Paths From Corner Cell To Middle Cell<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/paths-from-corner-to-middle/0" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> BFS / DFS for path finding.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N^2)</td>
      <td>Perform BFS or DFS starting from all 4 corners simultaneously or individually. At each cell `(r, c)`, the jump size is `val = grid[r][c]`. We can move to `(r+val, c)`, `(r-val, c)`, `(r, c+val)`, `(r, c-val)`. Target is `(N/2, N/2)`.<br><br><b>Dependencies:</b> <code>#include <queue></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def solve(grid: List[List[int]]):&#10;    n = len(grid)&#10;    q = collections.deque([(0,0), (0,n-1), (n-1,0), (n-1,n-1)])&#10;    vis = set(q)&#10;    dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]&#10;    while q:&#10;        r, c = q.popleft()&#10;        if r == n // 2 and c == n // 2: return True&#10;        val = grid[r][c]&#10;        if val == 0: continue&#10;        for i in range(4):&#10;            nr, nc = r + dr[i] * val, c + dc[i] * val&#10;            if 0 &lt;= nr &lt; n and 0 &lt;= nc &lt; n and (nr, nc) not in vis:&#10;                vis.add((nr, nc))&#10;                q.append((nr, nc))&#10;    return False</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">25</td>
      <td rowspan="1">Rec 25 Arithmetic Expressions<br><br></b> <a href="https://www.hackerrank.com/challenges/arithmetic-expressions/problem" target="_blank">HackerRank</a></td>
      <td rowspan="1"><b>Example 1:</b> DP with path reconstruction.</td>
      <td><b>Time:</b> O(N * 101)<br><b>Space:</b> O(N * 101)</td>
      <td>Use a DP table `dp[i][mod]` to store the operator used to reach remainder `mod` at index `i`. Iterate through the array, for each reachable mod from previous step, try `(mod + arr[i]) % 101`, `(mod - arr[i]) % 101`, `(mod * arr[i]) % 101`. Then backtrack from `dp[N-1][0]` to find the operators.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def arithmeticExpressions(arr: List[int]) -&gt; str:&#10;    n = len(arr)&#10;    dp = [[None] * 101 for _ in range(n)]&#10;    dp[0][arr[0] % 101] = (&#x27;&#x27;, 0)&#10;    for i in range(1, n):&#10;        for j in range(101):&#10;            if dp[i-1][j] is not None:&#10;                dp[i][(j + arr[i]) % 101] = (&#x27;+&#x27;, j)&#10;                dp[i][(j - arr[i] % 101 + 101) % 101] = (&#x27;-&#x27;, j)&#10;                dp[i][(j * arr[i]) % 101] = (&#x27;*&#x27;, j)&#10;    res = []&#10;    curr = 0&#10;    for i in range(n - 1, 0, -1):&#10;        op, prev_mod = dp[i][curr]&#10;        res.append(str(arr[i]))&#10;        res.append(op)&#10;        curr = prev_mod&#10;    res.append(str(arr[0]))&#10;    return &quot;&quot;.join(reversed(res))</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">26</td>
      <td rowspan="1">Rec 26 Find All Possible Palindromic Partitions Of A String<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/find-all-possible-palindromic-partitions-of-a-string/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Recursive Backtracking.</td>
      <td><b>Time:</b> O(N * 2^N)<br><b>Space:</b> O(N)</td>
      <td>Iterate through the string. Extract substring `S[ind..i]`. If it is a palindrome, add it to the current partition list and recursively call for `i+1`. When `ind == length`, push the partition list to the answer.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def allPalindromicPerms(S: str) -&gt; List[List[str]]:&#10;    ans = []&#10;    def is_pal(s): return s == s[::-1]&#10;    def solve(ind, curr):&#10;        if ind == len(S):&#10;            ans.append(curr[:])&#10;            return&#10;        for i in range(ind, len(S)):&#10;            sub = S[ind:i+1]&#10;            if is_pal(sub):&#10;                curr.append(sub)&#10;                solve(i + 1, curr)&#10;                curr.pop()&#10;    solve(0, [])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">27</td>
      <td rowspan="1">Rec 27 Partition Array To K Subsets<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/partition-array-to-k-subsets/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Recursive Backtracking.</td>
      <td><b>Time:</b> O(K * 2^N)<br><b>Space:</b> O(N)</td>
      <td>If total sum is not divisible by K, return false. Sort array in descending order. Use a boolean array `vis`. Helper function `solve(ind, currentSum, k)`: if `k == 1` return true. If `currentSum == target`, `solve(0, 0, k-1)`. Otherwise, iterate from `ind` to `N`, if `!vis[i]` and `currentSum + arr[i] <= target`, mark `vis[i] = true`, recurse, unmark.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isKPartitionPossible(a: List[int], n: int, k: int) -&gt; bool:&#10;    total = sum(a)&#10;    if total % k != 0 or n &lt; k: return False&#10;    target = total // k&#10;    vis = [False] * n&#10;    def solve(ind, currSum, k):&#10;        if k == 1: return True&#10;        if currSum == target: return solve(0, 0, k - 1)&#10;        for i in range(ind, n):&#10;            if not vis[i] and currSum + a[i] &lt;= target:&#10;                vis[i] = True&#10;                if solve(i + 1, currSum + a[i], k): return True&#10;                vis[i] = False&#10;        return False&#10;    return solve(0, 0, k)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">28</td>
      <td rowspan="1">Rec 28 Longest Possible Route In A Matrix With Hurdles<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/longest-possible-route-in-a-matrix-with-hurdles/0" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Recursive Backtracking.</td>
      <td><b>Time:</b> O(4^(N*M))<br><b>Space:</b> O(N*M)</td>
      <td>Use a global `max_dist` or pass it by reference. In `solve(r, c, dist)`, if `(r, c) == (dest_r, dest_c)`, `max_dist = max(max_dist, dist)` and return. Mark `(r, c)` as visited. Explore 4 directions. Unmark `(r, c)`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def longestPath(mat: List[List[int]], xs: int, ys: int, xd: int, yd: int) -&gt; int:&#10;    if mat[xs][ys] == 0 or mat[xd][yd] == 0: return -1&#10;    maxDist = [-1]&#10;    n, m = len(mat), len(mat[0])&#10;    def solve(r, c, dist):&#10;        if r == xd and c == yd:&#10;            maxDist[0] = max(maxDist[0], dist)&#10;            return&#10;        mat[r][c] = 0&#10;        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:&#10;            if 0 &lt;= nr &lt; n and 0 &lt;= nc &lt; m and mat[nr][nc] == 1:&#10;                solve(nr, nc, dist + 1)&#10;        mat[r][c] = 1&#10;    solve(xs, ys, 0)&#10;    return maxDist[0]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">29</td>
      <td rowspan="1">Rec 29 Find Shortest Safe Route In A Path With Landmines<br><br></b> <a href="https://www.geeksforgeeks.org/find-shortest-safe-route-in-a-path-with-landmines/" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> BFS or Backtracking.</td>
      <td><b>Time:</b> O(R * C)<br><b>Space:</b> O(R * C)</td>
      <td>First, mark all adjacent cells of landmines as unsafe. Then start from each cell in the first column and use BFS or Backtracking to find the shortest path to the last column, avoiding unsafe cells.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">from collections import deque&#10;def findShortestPath(mat):&#10;    R, C = len(mat), len(mat[0])&#10;    grid = [[1] * C for _ in range(R)]&#10;    dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]&#10;    for i in range(R):&#10;        for j in range(C):&#10;            if mat[i][j] == 0:&#10;                grid[i][j] = 0&#10;                for k in range(4):&#10;                    nr, nc = i + dr[k], j + dc[k]&#10;                    if 0 &lt;= nr &lt; R and 0 &lt;= nc &lt; C: grid[nr][nc] = 0&#10;    q = deque()&#10;    vis = [[False] * C for _ in range(R)]&#10;    for i in range(R):&#10;        if grid[i][0] == 1:&#10;            q.append((i, 0, 1))&#10;            vis[i][0] = True&#10;    while q:&#10;        r, c, dist = q.popleft()&#10;        if c == C - 1: return dist&#10;        for k in range(4):&#10;            nr, nc = r + dr[k], c + dc[k]&#10;            if 0 &lt;= nr &lt; R and 0 &lt;= nc &lt; C and grid[nr][nc] == 1 and not vis[nr][nc]:&#10;                vis[nr][nc] = True&#10;                q.append((nr, nc, dist + 1))&#10;    return -1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">30</td>
      <td rowspan="1">Rec 30 Combinational Sum<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/combination-sum-1587115620/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Backtracking.</td>
      <td><b>Time:</b> O(2^N * K)<br><b>Space:</b> O(K * X)</td>
      <td>Sort the array and remove duplicates. Use backtracking. At each step, either include the current element (and stay at the current element to allow unlimited picks) or move to the next element. Backtrack when sum < 0 or we reach the end.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def combinationSum(A, B):&#10;    A = sorted(list(set(A)))&#10;    ans = []&#10;    def solve(idx, current_sum, curr):&#10;        if current_sum == B:&#10;            ans.append(list(curr))&#10;            return&#10;        if current_sum &gt; B or idx == len(A): return&#10;        curr.append(A[idx])&#10;        solve(idx, current_sum + A[idx], curr)&#10;        curr.pop()&#10;        solve(idx + 1, current_sum, curr)&#10;    solve(0, 0, [])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">31</td>
      <td rowspan="1">Rec 31 Find Maximum Number Possible By Doing At Most K Swaps<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/largest-number-in-k-swaps-1587115620/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Backtracking.</td>
      <td><b>Time:</b> O(N! / (N-K)!)<br><b>Space:</b> O(N)</td>
      <td>Use backtracking to try swapping each digit with every digit that appears after it and is greater than it. Keep track of the maximum string seen so far. Prune if swaps == 0.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findMaximumNum(str_val, k):&#10;    max_str = [str_val]&#10;    def solve(curr, k_left, idx):&#10;        if k_left == 0 or idx == len(curr) - 1: return&#10;        max_char = curr[idx]&#10;        for i in range(idx + 1, len(curr)):&#10;            if curr[i] &gt; max_char: max_char = curr[i]&#10;        if max_char != curr[idx]: k_left -= 1&#10;        for i in range(len(curr) - 1, idx - 1, -1):&#10;            if curr[i] == max_char:&#10;                curr_list = list(curr)&#10;                curr_list[idx], curr_list[i] = curr_list[i], curr_list[idx]&#10;                new_str = &quot;&quot;.join(curr_list)&#10;                if new_str &gt; max_str[0]: max_str[0] = new_str&#10;                solve(new_str, k_left, idx + 1)&#10;    solve(str_val, k, 0)&#10;    return max_str[0]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">32</td>
      <td rowspan="1">Rec 32 Find If There Is A Path Of More Than K Length From A Source<br><br></b> <a href="https://www.geeksforgeeks.org/find-if-there-is-a-path-of-more-than-k-length-from-a-source/" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> DFS Backtracking.</td>
      <td><b>Time:</b> O(V!)<br><b>Space:</b> O(V)</td>
      <td>Use Backtracking to perform DFS traversal from the source. Mark the current vertex as visited, subtract the edge weight from `k`, and recursively call for all adjacent unvisited vertices. If `k <= 0`, return true. Backtrack by unmarking the vertex.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def pathMoreThanK(src, k, adj, vis):&#10;    if k &lt;= 0: return True&#10;    vis[src] = True&#10;    for v, w in adj[src]:&#10;        if not vis[v]:&#10;            if pathMoreThanK(v, k - w, adj, vis):&#10;                return True&#10;    vis[src] = False&#10;    return False</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">33</td>
      <td rowspan="1">Rec 33 Longest Possible Route In A Matrix With Hurdles<br><br></b> <a href="https://www.geeksforgeeks.org/longest-possible-route-in-a-matrix-with-hurdles/" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Backtracking.</td>
      <td><b>Time:</b> O(4^(M*N))<br><b>Space:</b> O(M*N)</td>
      <td>Use Backtracking. Start from the source, mark it as visited, recursively find the longest path from all valid unvisited adjacent cells, add 1 to the maximum among them. Unmark the cell after returning.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findLongestPath(mat, i, j, di, dj, curr, max_dist, vis):&#10;    if i == di and j == dj:&#10;        max_dist[0] = max(max_dist[0], curr)&#10;        return&#10;    vis[i][j] = True&#10;    dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]&#10;    for k in range(4):&#10;        nr, nc = i + dr[k], j + dc[k]&#10;        if 0 &lt;= nr &lt; len(mat) and 0 &lt;= nc &lt; len(mat[0]) and mat[nr][nc] == 1 and not vis[nr][nc]:&#10;            findLongestPath(mat, nr, nc, di, dj, curr + 1, max_dist, vis)&#10;    vis[i][j] = False</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">34</td>
      <td rowspan="1">Rec 34 Print All Possible Paths From Top Left To Bottom Right Of A Mxn Matrix<br><br></b> <a href="https://www.geeksforgeeks.org/print-all-possible-paths-from-top-left-to-bottom-right-of-a-mxn-matrix/" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> DFS.</td>
      <td><b>Time:</b> O(2^(M+N))<br><b>Space:</b> O(M+N)</td>
      <td>Use simple DFS from top-left. From cell (i, j), we can move to (i+1, j) or (i, j+1). Keep track of the path elements in an array/list. When reaching bottom-right, print/save the path.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findPaths(mat, i, j, path, ans):&#10;    if i == len(mat) - 1 and j == len(mat[0]) - 1:&#10;        ans.append(path + [mat[i][j]])&#10;        return&#10;    path.append(mat[i][j])&#10;    if i + 1 &lt; len(mat): findPaths(mat, i + 1, j, path, ans)&#10;    if j + 1 &lt; len(mat[0]): findPaths(mat, i, j + 1, path, ans)&#10;    path.pop()</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">35</td>
      <td rowspan="1">Rec 35 Word Break Problem Using Backtracking<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/word-break-part-23249/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Backtracking.</td>
      <td><b>Time:</b> O(2^N)<br><b>Space:</b> O(N)</td>
      <td>Iterate from current index. For each prefix, if it is in the dictionary, add it to the current sentence string, add a space, and recur for the suffix. If we reach the end of the string, add the current sentence to the answer.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def wordBreak(n, dict_words, s):&#10;    st = set(dict_words)&#10;    ans = []&#10;    def solve(idx, curr):&#10;        if idx == len(s):&#10;            ans.append(curr.strip())&#10;            return&#10;        for i in range(idx, len(s)):&#10;            word = s[idx:i+1]&#10;            if word in st:&#10;                solve(i + 1, curr + word + &quot; &quot;)&#10;    solve(0, &quot;&quot;)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">36</td>
      <td rowspan="1">Rec 36 Print 1 To N Without Loop<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/print-1-to-n-without-using-loops-1587115620/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Recursion.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Use a recursive function. Call `f(N-1)` first and then print `N`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def printTillN(N):&#10;    if N == 0: return&#10;    printTillN(N - 1)&#10;    print(N, end=&quot; &quot;)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">37</td>
      <td rowspan="1">Rec 37 Print N To 1 Without Loop<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/print-n-to-1-without-loop/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Recursion.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Use a recursive function. Print `N` first and then call `f(N-1)`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def printNos(N):&#10;    if N == 0: return&#10;    print(N, end=&quot; &quot;)&#10;    printNos(N - 1)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">38</td>
      <td rowspan="1">Rec 38 Sum Of First N Terms<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/sum-of-first-n-terms5843/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Math or Recursion.</td>
      <td><b>Time:</b> O(1) Math, O(N) Recursion<br><b>Space:</b> O(1) Math, O(N) Recursion</td>
      <td>The mathematical formula for the sum of cubes is `(n * (n + 1) / 2)^2`. Alternatively, use recursion `f(n) = n^3 + f(n-1)`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def sumOfSeries(n):&#10;    return (n * (n + 1) // 2) ** 2</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">39</td>
      <td rowspan="1">Rec 39 Find All Factorial Numbers Less Than Or Equal To N<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/find-all-factorial-numbers-less-than-or-equal-to-n3548/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Recursion.</td>
      <td><b>Time:</b> O(K) where K! <= N<br><b>Space:</b> O(K)</td>
      <td>Maintain a current factorial value and an index `i`. At each recursive step, compute the next factorial by multiplying by `i`. If the next factorial is `<= n`, add it to the list and recurse.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def factorialNumbers(N):&#10;    ans = []&#10;    def findFactorials(i, fact):&#10;        if fact &gt; N: return&#10;        ans.append(fact)&#10;        findFactorials(i + 1, fact * (i + 1))&#10;    findFactorials(1, 1)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">40</td>
      <td rowspan="1">Rec 40 Reverse An Array<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/reverse-an-array/0" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Recursion with two pointers.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N) recursive stack</td>
      <td>Swap `arr[l]` and `arr[r]` and then recursively call `reverse(arr, l+1, r-1)`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def reverseArray(arr, l, r):&#10;    if l &gt;= r: return&#10;    arr[l], arr[r] = arr[r], arr[l]&#10;    reverseArray(arr, l + 1, r - 1)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">41</td>
      <td rowspan="1">Rec 41 Fibonacci Number<br><br></b> <a href="https://leetcode.com/problems/fibonacci-number/" target="_blank">LeetCode 509</a></td>
      <td rowspan="1"><b>Example 1:</b> Base Case.</td>
      <td><b>Time:</b> O(2^N)<br><b>Space:</b> O(N)</td>
      <td>Return `fib(n-1) + fib(n-2)` with base cases `fib(0) = 0`, `fib(1) = 1`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def fib(n):&#10;    if n &lt;= 1: return n&#10;    return fib(n - 1) + fib(n - 2)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">42</td>
      <td rowspan="1">Rec 42 Count Good Numbers<br><br></b> <a href="https://leetcode.com/problems/count-good-numbers/" target="_blank">LeetCode 1922</a></td>
      <td rowspan="1"><b>Example 1:</b> Modular Exponentiation.</td>
      <td><b>Time:</b> O(log N)<br><b>Space:</b> O(1)</td>
      <td>There are 5 even digits and 4 prime digits. At even indices we have 5 choices. At odd indices we have 4 choices. If `n` is even, we have `n/2` even indices and `n/2` odd indices. So answer is `(5^(n/2) * 4^(n/2)) % mod`. If `n` is odd, we have `n/2 + 1` even indices. So answer is `(5^(n/2 + 1) * 4^(n/2)) % mod`. Use binary exponentiation.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def countGoodNumbers(n):&#10;    mod = 10**9 + 7&#10;    def power(x, y):&#10;        res = 1&#10;        x = x % mod&#10;        while y &gt; 0:&#10;            if y % 2 == 1: res = (res * x) % mod&#10;            y = y // 2&#10;            x = (x * x) % mod&#10;        return res&#10;    evenIndices = (n + 1) // 2&#10;    oddIndices = n // 2&#10;    return (power(5, evenIndices) * power(4, oddIndices)) % mod</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">43</td>
      <td rowspan="1">Rec 43 Sort A Stack Using Recursion<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/sort-a-stack/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Recursive sort and insert.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N)</td>
      <td>Recursively pop elements until the stack is empty. When returning from the recursive call, use another recursive function `sortedInsert` to insert the popped element into its correct sorted position in the stack.<br><br><b>Dependencies:</b> Stack</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def sortedInsert(s, element):&#10;    if not s or element &gt; s[-1]:&#10;        s.append(element)&#10;        return&#10;    num = s.pop()&#10;    sortedInsert(s, element)&#10;    s.append(num)&#10;def sortStack(s):&#10;    if not s: return&#10;    num = s.pop()&#10;    sortStack(s)&#10;    sortedInsert(s, num)</code></pre></details></td>
    </tr>
  </tbody>
</table>


## Linked Lists

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
      <td rowspan="1">1</td>
      <td rowspan="1">Ll 01 Reverse Linked List<br><br></b> <a href="https://leetcode.com/problems/reverse-linked-list/" target="_blank">LeetCode 206</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> head = [1,2,3,4,5]<br><b>Output:</b> [5,4,3,2,1]</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td>Iterative approach: Maintain three pointers (`prev`, `curr`, `next_node`). Re-point `curr->next` to `prev` and slide forward.</td>
      <td><b>Edge Cases:</b> <b>Null List:</b> Automatically handled because the `while` loop checks `curr != NULL`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def reverse_list(head: ListNode) -&gt; ListNode:&#10;    prev = None&#10;    curr = head&#10;    while curr:&#10;        next_node = curr.next&#10;        curr.next = prev&#10;        prev = curr&#10;        curr = next_node&#10;    return prev</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">2</td>
      <td rowspan="1">Ll 02 Middle Of The Linked List<br><br></b> <a href="https://leetcode.com/problems/middle-of-the-linked-list/" target="_blank">LeetCode 876</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> head = [1,2,3,4,5,6]<br><b>Output:</b> [4,5,6]</td>
      <td><b>Time:</b> O(N/2) &cong; O(N) (Constraint)<br><b>Space:</b> O(1)</td>
      <td>Use a slow pointer (moves 1 step) and a fast pointer (moves 2 steps). When fast reaches the end, slow is exactly at the middle.</td>
      <td><b>Edge Cases:</b> <b>Even/Odd Length:</b> Loop condition `fast != NULL && fast->next != NULL` handles both.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def middle_node(head: ListNode) -&gt; ListNode:&#10;    slow, fast = head, head&#10;    while fast and fast.next:&#10;        slow = slow.next&#10;        fast = fast.next.next&#10;    return slow</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">3</td>
      <td rowspan="1">Ll 03 Linked List Cycle<br><br></b> <a href="https://leetcode.com/problems/linked-list-cycle/" target="_blank">LeetCode 141</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> head = [3,2,0,-4], pos = 1<br><b>Output:</b> true</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td>Tortoise and Hare algorithm. If there is a cycle, the fast pointer will eventually "lap" and collide with the slow pointer.</td>
      <td><b>Edge Cases:</b> <b>No Cycle:</b> Handled if `fast == NULL` or `fast->next == NULL`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def has_cycle(head: ListNode) -&gt; bool:&#10;    slow, fast = head, head&#10;    while fast and fast.next:&#10;        slow = slow.next&#10;        fast = fast.next.next&#10;        if slow == fast: return True&#10;    return False</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">4</td>
      <td rowspan="1">Ll 04 Merge Two Sorted Lists<br><br></b> <a href="https://leetcode.com/problems/merge-two-sorted-lists/" target="_blank">LeetCode 21</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> list1 = [1,2,4], list2 = [1,3,4]<br><b>Output:</b> [1,1,2,3,4,4]</td>
      <td><b>Time:</b> O(N + M) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td>Use a dummy node to easily handle the head of the new list. Compare `list1` and `list2`, attaching the smaller node to `tail`.</td>
      <td><b>Edge Cases:</b> <b>Leftover Nodes:</b> When one list exhausts, directly attach the entirety of the other list via `tail->next = list1 ? list1 : list2`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def mergeTwoLists(list1: ListNode, list2: ListNode) -&gt; ListNode:&#10;    dummy = tail = ListNode()&#10;    while list1 and list2:&#10;        if list1.val &lt; list2.val:&#10;            tail.next = list1&#10;            list1 = list1.next&#10;        else:&#10;            tail.next = list2&#10;            list2 = list2.next&#10;        tail = tail.next&#10;    tail.next = list1 or list2&#10;    return dummy.next</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">5</td>
      <td rowspan="1">Ll 05 Remove Nth Node From End Of List<br><br></b> <a href="https://leetcode.com/problems/remove-nth-node-from-end-of-list/" target="_blank">LeetCode 19</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> head = [1,2,3,4,5], n = 2<br><b>Output:</b> [1,2,3,5]</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td>Two-pointer approach. Move `fast` pointer `n` steps ahead. Then move both `slow` and `fast` until `fast` reaches the end. `slow` will be right before the target node.</td>
      <td><b>Edge Cases:</b> <b>Remove Head:</b> If `fast` becomes NULL after moving `n` steps, it means the head needs to be removed. Return `head->next`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def removeNthFromEnd(head: ListNode, n: int) -&gt; ListNode:&#10;    fast = slow = head&#10;    for _ in range(n):&#10;        fast = fast.next&#10;    if not fast: return head.next&#10;    while fast.next:&#10;        fast = fast.next&#10;        slow = slow.next&#10;    slow.next = slow.next.next&#10;    return head</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">6</td>
      <td rowspan="1">Ll 06 Add Two Numbers<br><br></b> <a href="https://leetcode.com/problems/add-two-numbers/" target="_blank">LeetCode 2</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> l1 = [2,4,3], l2 = [5,6,4]<br><b>Output:</b> [7,0,8]</td>
      <td><b>Time:</b> O(max(N, M))<br><b>Space:</b> O(max(N, M))</td>
      <td>Iterate through both lists, keeping a `carry`. Create new nodes for the `sum % 10`.</td>
      <td><b>Edge Cases:</b> <b>Leftover Carry:</b> After the loop, if `carry > 0`, we must append one last node.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def addTwoNumbers(l1: ListNode, l2: ListNode) -&gt; ListNode:&#10;    dummy = temp = ListNode()&#10;    carry = 0&#10;    while l1 or l2 or carry:&#10;        s = carry&#10;        if l1: s += l1.val; l1 = l1.next&#10;        if l2: s += l2.val; l2 = l2.next&#10;        carry = s // 10&#10;        temp.next = ListNode(s % 10)&#10;        temp = temp.next&#10;    return dummy.next</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">7</td>
      <td rowspan="1">Ll 07 Intersection Of Two Linked Lists<br><br></b> <a href="https://leetcode.com/problems/intersection-of-two-linked-lists/" target="_blank">LeetCode 160</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3<br><b>Output:</b> Intersected at '8'</td>
      <td><b>Time:</b> O(N + M)<br><b>Space:</b> O(1)</td>
      <td>Two pointers `a` and `b`. Traverse `A` then `B`, and `B` then `A`. They will meet at the intersection node or `NULL`.</td>
      <td><b>Edge Cases:</b> <b>No Intersection:</b> If no intersection, both pointers will simultaneously hit `NULL` at the end of their second traversal.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def getIntersectionNode(headA: ListNode, headB: ListNode) -&gt; ListNode:&#10;    a, b = headA, headB&#10;    while a != b:&#10;        a = a.next if a else headB&#10;        b = b.next if b else headA&#10;    return a</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">8</td>
      <td rowspan="1">Ll 08 Reverse Nodes In K Group<br><br></b> <a href="https://leetcode.com/problems/reverse-nodes-in-k-group/" target="_blank">LeetCode 25</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> head = [1,2,3,4,5], k = 2<br><b>Output:</b> [2,1,4,3,5]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Find length of list. Traverse groups of size k. For each group, perform standard linked list reversal. Link the prev group's tail to the current reversed head.</td>
      <td><b>Edge Cases:</b> <b>Remaining nodes < K:</b> The loop terminates early, leaving the remaining list intact.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def reverseKGroup(head: Optional[ListNode], k: int) -&gt; Optional[ListNode]:&#10;    if not head or k == 1: return head&#10;    dummy = ListNode(0)&#10;    dummy.next = head&#10;    cur, pre, count = head, dummy, 0&#10;    while cur: &#10;        count += 1; cur = cur.next&#10;    while count &gt;= k:&#10;        cur = pre.next&#10;        nex = cur.next&#10;        for _ in range(1, k):&#10;            cur.next = nex.next&#10;            nex.next = pre.next&#10;            pre.next = nex&#10;            nex = cur.next&#10;        pre = cur&#10;        count -= k&#10;    return dummy.next</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">9</td>
      <td rowspan="1">Ll 09 Copy List With Random Pointer<br><br></b> <a href="https://leetcode.com/problems/copy-list-with-random-pointer/" target="_blank">LeetCode 138</a></td>
      <td rowspan="1"><b>Example 1:</b> Return a deep copy.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>3 Steps O(1) space. 1) Insert copy nodes right after original nodes. 2) Set random pointers for copy nodes: `iter->next->random = iter->random ? iter->random->next : NULL`. 3) Separate the two lists.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def copyRandomList(head: &#x27;Optional[Node]&#x27;) -&gt; &#x27;Optional[Node]&#x27;:&#10;    if not head: return None&#10;    iter_node = head&#10;    while iter_node:&#10;        copy = Node(iter_node.val)&#10;        copy.next = iter_node.next&#10;        iter_node.next = copy&#10;        iter_node = copy.next&#10;    iter_node = head&#10;    while iter_node:&#10;        if iter_node.random: iter_node.next.random = iter_node.random.next&#10;        iter_node = iter_node.next.next&#10;    iter_node = head&#10;    pseudoHead = Node(0)&#10;    copyIter = pseudoHead&#10;    while iter_node:&#10;        nextIter = iter_node.next.next&#10;        copyIter.next = iter_node.next&#10;        iter_node.next = nextIter&#10;        copyIter = copyIter.next&#10;        iter_node = nextIter&#10;    return pseudoHead.next</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">10</td>
      <td rowspan="1">Ll 10 Rotate List<br><br></b> <a href="https://leetcode.com/problems/rotate-list/" target="_blank">LeetCode 61</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> head = [1,2,3,4,5], k = 2<br><b>Output:</b> [4,5,1,2,3]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Compute the length of the list, and make it a circular list by connecting the last node to head. Then find the new break point `(length - k % length)`. Break the circle and return the new head.</td>
      <td><b>Edge Cases:</b> <b>k = 0 or empty list:</b> Return head immediately.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def rotateRight(head: Optional[ListNode], k: int) -&gt; Optional[ListNode]:&#10;    if not head or not head.next or k == 0: return head&#10;    length = 1&#10;    cur = head&#10;    while cur.next:&#10;        length += 1&#10;        cur = cur.next&#10;    cur.next = head&#10;    k = k % length&#10;    k = length - k&#10;    for _ in range(k): cur = cur.next&#10;    head = cur.next&#10;    cur.next = None&#10;    return head</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">11</td>
      <td rowspan="1">Ll 11 Flattening A Linked List<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/flattening-a-linked-list/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Recursively merge.</td>
      <td><b>Time:</b> O(N * M)<br><b>Space:</b> O(N)</td>
      <td>Recursively flatten the `next` list, then merge the current list (`bottom` pointers) with the flattened `next` list, similar to merging two sorted linked lists.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def flatten(root):&#10;    def mergeTwoLists(a, b):&#10;        temp = Node(0)&#10;        res = temp&#10;        while a and b:&#10;            if a.data &lt; b.data:&#10;                temp.bottom = a; temp = temp.bottom; a = a.bottom&#10;            else:&#10;                temp.bottom = b; temp = temp.bottom; b = b.bottom&#10;        if a: temp.bottom = a&#10;        else: temp.bottom = b&#10;        return res.bottom&#10;    if not root or not root.next: return root&#10;    root.next = flatten(root.next)&#10;    root = mergeTwoLists(root, root.next)&#10;    return root</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">12</td>
      <td rowspan="1">Ll 12 Sort A Linked List<br><br></b> <a href="https://leetcode.com/problems/sort-list/" target="_blank">LeetCode 148</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> head = [4,2,1,3]<br><b>Output:</b> [1,2,3,4]</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(log N)</td>
      <td>Merge Sort. Use fast/slow pointers to find the middle of the linked list. Split into two halves, recursively sort both halves, then merge the two sorted halves.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def sortList(head: Optional[ListNode]) -&gt; Optional[ListNode]:&#10;    def mergeTwoLists(list1, list2):&#10;        dummy = ListNode(0)&#10;        tail = dummy&#10;        while list1 and list2:&#10;            if list1.val &lt; list2.val:&#10;                tail.next = list1; list1 = list1.next&#10;            else:&#10;                tail.next = list2; list2 = list2.next&#10;            tail = tail.next&#10;        tail.next = list1 if list1 else list2&#10;        return dummy.next&#10;    if not head or not head.next: return head&#10;    slow, fast = head, head.next&#10;    while fast and fast.next:&#10;        slow = slow.next; fast = fast.next.next&#10;    mid = slow.next&#10;    slow.next = None&#10;    return mergeTwoLists(sortList(head), sortList(mid))</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">13</td>
      <td rowspan="1">Ll 13 Find Pairs With Given Sum In Doubly Linked List<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/find-pairs-with-given-sum-in-doubly-linked-list/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Two pointer approach.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Since it is a sorted DLL, set one pointer at the head and one at the tail. If sum == x, add to result and move both. If sum < x, move left pointer next. Else, move right pointer prev.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findPairsWithGivenSum(head, target):&#10;    ans = []&#10;    if not head: return ans&#10;    left = head&#10;    right = head&#10;    while right.next: right = right.next&#10;    while left and right and left.data &lt; right.data:&#10;        if left.data + right.data == target:&#10;            ans.append((left.data, right.data))&#10;            left = left.next&#10;            right = right.prev&#10;        elif left.data + right.data &lt; target:&#10;            left = left.next&#10;        else:&#10;            right = right.prev&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">14</td>
      <td rowspan="1">Ll 14 Remove Duplicates From Sorted Doubly Linked List<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/remove-duplicates-from-a-sorted-doubly-linked-list/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Skip duplicates.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Traverse the DLL. While `next` node has the same value, bypass it by updating `curr->next` and `curr->next->prev`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def removeDuplicates(head):&#10;    curr = head&#10;    while curr:&#10;        nextNode = curr.next&#10;        while nextNode and nextNode.data == curr.data:&#10;            nextNode = nextNode.next&#10;        curr.next = nextNode&#10;        if nextNode:&#10;            nextNode.prev = curr&#10;        curr = curr.next&#10;    return head</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">15</td>
      <td rowspan="1">Ll 15 Reverse A Doubly Linked List<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/reverse-a-doubly-linked-list/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Swap prev and next.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Traverse the DLL. For each node, swap its `prev` and `next` pointers. The new head will be the last node processed.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def reverseDLL(head):&#10;    if not head or not head.next: return head&#10;    curr = head&#10;    temp = None&#10;    while curr:&#10;        temp = curr.prev&#10;        curr.prev = curr.next&#10;        curr.next = temp&#10;        curr = curr.prev&#10;    return temp.prev</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">16</td>
      <td rowspan="1">Ll 16 Delete All Occurrences Of A Key In Dll<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/delete-all-occurrences-of-a-given-key-in-a-doubly-linked-list/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Update links.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Traverse the list. If `node->data == x`, update the `next` pointer of `node->prev` and `prev` pointer of `node->next`. If the node is head, update head.</td>
      <td><b>Edge Cases:</b> <b>Head deletion:</b> handled by reassigning head pointer.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def deleteAllOccurOfX(head, x):&#10;    curr = head&#10;    while curr:&#10;        if curr.data == x:&#10;            if curr == head: head = curr.next&#10;            if curr.prev: curr.prev.next = curr.next&#10;            if curr.next: curr.next.prev = curr.prev&#10;            curr = curr.next&#10;        else:&#10;            curr = curr.next&#10;    return head</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">17</td>
      <td rowspan="1">Ll 17 Swap Nodes In Pairs<br><br></b> <a href="https://leetcode.com/problems/swap-nodes-in-pairs/" target="_blank">LeetCode 24</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> head = [1,2,3,4]<br><b>Output:</b> [2,1,4,3]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Use a dummy node. Iteratively swap `curr` and `curr->next`. Keep track of `prev` to link the swapped pairs to the rest of the list.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def swapPairs(head: Optional[ListNode]) -&gt; Optional[ListNode]:&#10;    dummy = ListNode(0)&#10;    dummy.next = head&#10;    prev = dummy&#10;    while prev.next and prev.next.next:&#10;        first = prev.next&#10;        second = prev.next.next&#10;        first.next = second.next&#10;        second.next = first&#10;        prev.next = second&#10;        prev = first&#10;    return dummy.next</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">18</td>
      <td rowspan="1">Ll 18 Odd Even Linked List<br><br></b> <a href="https://leetcode.com/problems/odd-even-linked-list/" target="_blank">LeetCode 328</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> head = [1,2,3,4,5]<br><b>Output:</b> [1,3,5,2,4]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Maintain two pointers `odd` and `even`. Keep the `evenHead`. Loop to link `odd->next = even->next` and `even->next = odd->next`. Finally, link `odd->next = evenHead`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def oddEvenList(head: Optional[ListNode]) -&gt; Optional[ListNode]:&#10;    if not head or not head.next: return head&#10;    odd, even, evenHead = head, head.next, head.next&#10;    while even and even.next:&#10;        odd.next = odd.next.next&#10;        even.next = even.next.next&#10;        odd = odd.next&#10;        even = even.next&#10;    odd.next = evenHead&#10;    return head</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">19</td>
      <td rowspan="1">Ll 19 Split Linked List In Parts<br><br></b> <a href="https://leetcode.com/problems/split-linked-list-in-parts/" target="_blank">LeetCode 725</a></td>
      <td rowspan="1"><b>Example 1:</b> Distribution math.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(K)</td>
      <td>First, calculate the length of the list. Then, determine base size `len / k` and extra nodes `len % k`. Iterate through the list, breaking it into parts of appropriate sizes.</td>
      <td><b>Edge Cases:</b> <b>k > length:</b> Fill remaining parts with null.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def splitListToParts(head: Optional[ListNode], k: int) -&gt; List[Optional[ListNode]]:&#10;    length = 0&#10;    curr = head&#10;    while curr:&#10;        length += 1&#10;        curr = curr.next&#10;    partSize, extra = length // k, length % k&#10;    ans = []&#10;    curr = head&#10;    for i in range(k):&#10;        ans.append(curr)&#10;        currentPartSize = partSize + (1 if extra &gt; 0 else 0)&#10;        extra -= 1&#10;        for _ in range(currentPartSize - 1):&#10;            if curr: curr = curr.next&#10;        if curr:&#10;            nextPart = curr.next&#10;            curr.next = None&#10;            curr = nextPart&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">20</td>
      <td rowspan="1">Ll 20 Add Two Numbers II<br><br></b> <a href="https://leetcode.com/problems/add-two-numbers-ii/" target="_blank">LeetCode 445</a></td>
      <td rowspan="1"><b>Example 1:</b> Stack or reverse.</td>
      <td><b>Time:</b> O(N + M)<br><b>Space:</b> O(N + M)</td>
      <td>Use two stacks to store the digits of the lists. Pop from stacks, add along with carry, and construct the new list by inserting at the head.<br><br><b>Dependencies:</b> <code>#include <stack></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -&gt; Optional[ListNode]:&#10;    s1, s2 = [], []&#10;    while l1:&#10;        s1.append(l1.val)&#10;        l1 = l1.next&#10;    while l2:&#10;        s2.append(l2.val)&#10;        l2 = l2.next&#10;    carry = 0&#10;    head = None&#10;    while s1 or s2 or carry:&#10;        sum_val = carry&#10;        if s1: sum_val += s1.pop()&#10;        if s2: sum_val += s2.pop()&#10;        node = ListNode(sum_val % 10)&#10;        node.next = head&#10;        head = node&#10;        carry = sum_val // 10&#10;    return head</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">21</td>
      <td rowspan="1">Ll 21 Insertion Sort List<br><br></b> <a href="https://leetcode.com/problems/insertion-sort-list/" target="_blank">LeetCode 147</a></td>
      <td rowspan="1"><b>Example 1:</b> Dummy head.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(1)</td>
      <td>Use a dummy head for the sorted part. For each node in the original list, iterate through the sorted part to find its correct position and insert it.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def insertionSortList(head: Optional[ListNode]) -&gt; Optional[ListNode]:&#10;    dummy = ListNode(0)&#10;    curr = head&#10;    while curr:&#10;        prev = dummy&#10;        while prev.next and prev.next.val &lt;= curr.val:&#10;            prev = prev.next&#10;        nxt = curr.next&#10;        curr.next = prev.next&#10;        prev.next = curr&#10;        curr = nxt&#10;    return dummy.next</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">22</td>
      <td rowspan="1">Ll 22 Partition List<br><br></b> <a href="https://leetcode.com/problems/partition-list/" target="_blank">LeetCode 86</a></td>
      <td rowspan="1"><b>Example 1:</b> Two lists then join.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Maintain two separate linked lists: `before` and `after` with their own dummy heads. Iterate through original list, appending to `before` or `after` based on value. Then link `before` tail to `after` head.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def partition(head: Optional[ListNode], x: int) -&gt; Optional[ListNode]:&#10;    before_head = ListNode(0)&#10;    before = before_head&#10;    after_head = ListNode(0)&#10;    after = after_head&#10;    while head:&#10;        if head.val &lt; x:&#10;            before.next = head&#10;            before = before.next&#10;        else:&#10;            after.next = head&#10;            after = after.next&#10;        head = head.next&#10;    after.next = None&#10;    before.next = after_head.next&#10;    return before_head.next</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">23</td>
      <td rowspan="1">Ll 23 Reverse Nodes In Even Length Groups<br><br></b> <a href="https://leetcode.com/problems/reverse-nodes-in-even-length-groups/" target="_blank">LeetCode 2074</a></td>
      <td rowspan="1"><b>Example 1:</b> Group tracking.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Traverse the list while tracking the expected group length. First, count the actual number of nodes left in the current group. If the count is even, reverse this sublist and connect it to the previous part. If odd, just skip. Update lengths and pointers.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def reverseEvenLengthGroups(head: Optional[ListNode]) -&gt; Optional[ListNode]:&#10;    groupLen = 1&#10;    prev, curr = None, head&#10;    while curr:&#10;        temp, count = curr, 0&#10;        while count &lt; groupLen and temp:&#10;            temp = temp.next&#10;            count += 1&#10;        if count % 2 == 0:&#10;            gPrev, gCurr = None, curr&#10;            for _ in range(count):&#10;                nxt = gCurr.next&#10;                gCurr.next = gPrev&#10;                gPrev = gCurr&#10;                gCurr = nxt&#10;            prev.next = gPrev&#10;            curr.next = gCurr&#10;            prev = curr&#10;            curr = gCurr&#10;        else:&#10;            for _ in range(count):&#10;                prev = curr&#10;                curr = curr.next&#10;        groupLen += 1&#10;    return head</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">24</td>
      <td rowspan="1">Ll 24 Swapping Nodes In A Linked List<br><br></b> <a href="https://leetcode.com/problems/swapping-nodes-in-a-linked-list/" target="_blank">LeetCode 1721</a></td>
      <td rowspan="1"><b>Example 1:</b> Two passes or three pointers.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Use two pointers. Move `fast` pointer `k-1` steps. `first_node` is at `fast`. Initialize `slow = head`. Move both `slow` and `fast` to the end. `slow` will be at `second_node`. Swap values.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def swapNodes(head: Optional[ListNode], k: int) -&gt; Optional[ListNode]:&#10;    fast = head&#10;    for _ in range(k - 1): fast = fast.next&#10;    first_node = fast&#10;    slow = head&#10;    while fast.next:&#10;        slow = slow.next&#10;        fast = fast.next&#10;    first_node.val, slow.val = slow.val, first_node.val&#10;    return head</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">25</td>
      <td rowspan="1">Ll 25 Merge Nodes In Between Zeros<br><br></b> <a href="https://leetcode.com/problems/merge-nodes-in-between-zeros/" target="_blank">LeetCode 2181</a></td>
      <td rowspan="1"><b>Example 1:</b> Accumulate and connect.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1) extra space if we modify in-place</td>
      <td>Maintain a dummy node. Traverse the list. Maintain a running sum. When we encounter a 0 (and sum > 0), create a new node with `sum`, attach it to dummy list, reset `sum` to 0.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def mergeNodes(head: Optional[ListNode]) -&gt; Optional[ListNode]:&#10;    dummy = currDummy = ListNode(0)&#10;    curr = head.next&#10;    current_sum = 0&#10;    while curr:&#10;        if curr.val == 0:&#10;            currDummy.next = ListNode(current_sum)&#10;            currDummy = currDummy.next&#10;            current_sum = 0&#10;        else:&#10;            current_sum += curr.val&#10;        curr = curr.next&#10;    return dummy.next</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">26</td>
      <td rowspan="1">Ll 26 Design Hashmap<br><br></b> <a href="https://leetcode.com/problems/design-hashmap/" target="_blank">LeetCode 706</a></td>
      <td rowspan="1"><b>Example 1:</b> Array of Linked Lists with Key-Value pairs.</td>
      <td><b>Time:</b> O(1) amortized<br><b>Space:</b> O(Number of elements)</td>
      <td>Similar to HashSet, but each node stores a `(key, value)` pair. On Put, if key exists, update value. Else insert new node. On Get, return value if key found, else -1.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class ListNode:&#10;    def __init__(self, key, val):&#10;        self.key, self.val = key, val&#10;        self.next = None&#10;class MyHashMap:&#10;    def __init__(self):&#10;        self.size = 10007&#10;        self.buckets = [None] * self.size&#10;    def put(self, key: int, value: int) -&gt; None:&#10;        idx = key % self.size&#10;        curr = self.buckets[idx]&#10;        while curr:&#10;            if curr.key == key:&#10;                curr.val = value&#10;                return&#10;            curr = curr.next&#10;        newNode = ListNode(key, value)&#10;        newNode.next = self.buckets[idx]&#10;        self.buckets[idx] = newNode&#10;    def get(self, key: int) -&gt; int:&#10;        idx = key % self.size&#10;        curr = self.buckets[idx]&#10;        while curr:&#10;            if curr.key == key: return curr.val&#10;            curr = curr.next&#10;        return -1&#10;    def remove(self, key: int) -&gt; None:&#10;        idx = key % self.size&#10;        curr = self.buckets[idx]&#10;        prev = None&#10;        while curr:&#10;            if curr.key == key:&#10;                if prev: prev.next = curr.next&#10;                else: self.buckets[idx] = curr.next&#10;                return&#10;            prev = curr&#10;            curr = curr.next</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">27</td>
      <td rowspan="1">Ll 27 Design Browser History<br><br></b> <a href="https://leetcode.com/problems/design-browser-history/" target="_blank">LeetCode 1472</a></td>
      <td rowspan="1"><b>Example 1:</b> Doubly Linked List.</td>
      <td><b>Time:</b> O(1) visit, O(steps) back/forward<br><b>Space:</b> O(N) for URLs</td>
      <td>Use a Doubly Linked List. Each visit creates a new node, clearing forward history. Back and forward operations just traverse the pointers up to `steps` times.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class Node:&#10;    def __init__(self, url):&#10;        self.url = url&#10;        self.prev = self.next = None&#10;class BrowserHistory:&#10;    def __init__(self, homepage: str):&#10;        self.curr = Node(homepage)&#10;    def visit(self, url: str) -&gt; None:&#10;        newNode = Node(url)&#10;        self.curr.next = newNode&#10;        newNode.prev = self.curr&#10;        self.curr = newNode&#10;    def back(self, steps: int) -&gt; str:&#10;        while steps &gt; 0 and self.curr.prev:&#10;            self.curr = self.curr.prev&#10;            steps -= 1&#10;        return self.curr.url&#10;    def forward(self, steps: int) -&gt; str:&#10;        while steps &gt; 0 and self.curr.next:&#10;            self.curr = self.curr.next&#10;            steps -= 1&#10;        return self.curr.url</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">28</td>
      <td rowspan="1">Ll 28 Lru Cache Ll<br><br></b> <a href="https://leetcode.com/problems/lru-cache/" target="_blank">LeetCode 146</a></td>
      <td rowspan="1"><b>Example 1:</b> Duplicate logic entry to ensure coverage.</td>
      <td><b>Time:</b> O(1)<br><b>Space:</b> O(N)</td>
      <td>Included for chapter coverage completeness. See sq_31_lru_cache.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python"># See Stacks and Queues module for full implementation.</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">29</td>
      <td rowspan="1">Ll 29 Lfu Cache Ll<br><br></b> <a href="https://leetcode.com/problems/lfu-cache/" target="_blank">LeetCode 460</a></td>
      <td rowspan="1"><b>Example 1:</b> Duplicate logic entry to ensure coverage.</td>
      <td><b>Time:</b> O(1)<br><b>Space:</b> O(N)</td>
      <td>Included for chapter coverage completeness. See sq_32_lfu_cache.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python"># See Stacks and Queues module for full implementation.</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">30</td>
      <td rowspan="1">Ll 30 All Oone Data Structure<br><br></b> <a href="https://leetcode.com/problems/all-oone-data-structure/" target="_blank">LeetCode 432</a></td>
      <td rowspan="1"><b>Example 1:</b> Doubly linked list of frequency buckets.</td>
      <td><b>Time:</b> O(1) amortized<br><b>Space:</b> O(N)</td>
      <td>Maintain a DLL where each node represents a specific frequency and contains a set of strings. Use a hash map mapping strings to their current bucket. On inc/dec, move the string to the adjacent bucket (create if necessary). Max is tail->prev, Min is head->next.<br><br><b>Dependencies:</b> <code>#include <unordered_set>\n#include <unordered_map></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class Bucket:&#10;    def __init__(self, count):&#10;        self.count = count&#10;        self.keys = set()&#10;        self.prev = self.next = None&#10;class AllOne:&#10;    def __init__(self):&#10;        self.head, self.tail = Bucket(0), Bucket(0)&#10;        self.head.next, self.tail.prev = self.tail, self.head&#10;        self.m = {}&#10;    def _add_bucket(self, prev_b, new_b):&#10;        new_b.prev, new_b.next = prev_b, prev_b.next&#10;        prev_b.next.prev = prev_b.next = new_b&#10;    def _remove_bucket(self, b):&#10;        b.prev.next, b.next.prev = b.next, b.prev&#10;    def inc(self, key: str) -&gt; None:&#10;        if key in self.m:&#10;            curr = self.m[key]&#10;            nxt = curr.next&#10;            if nxt == self.tail or nxt.count != curr.count + 1:&#10;                self._add_bucket(curr, Bucket(curr.count + 1))&#10;                nxt = curr.next&#10;            nxt.keys.add(key)&#10;            self.m[key] = nxt&#10;            curr.keys.remove(key)&#10;            if not curr.keys: self._remove_bucket(curr)&#10;        else:&#10;            nxt = self.head.next&#10;            if nxt == self.tail or nxt.count != 1:&#10;                self._add_bucket(self.head, Bucket(1))&#10;                nxt = self.head.next&#10;            nxt.keys.add(key)&#10;            self.m[key] = nxt&#10;    def dec(self, key: str) -&gt; None:&#10;        curr = self.m[key]&#10;        if curr.count == 1:&#10;            del self.m[key]&#10;        else:&#10;            prv = curr.prev&#10;            if prv == self.head or prv.count != curr.count - 1:&#10;                self._add_bucket(curr.prev, Bucket(curr.count - 1))&#10;                prv = curr.prev&#10;            prv.keys.add(key)&#10;            self.m[key] = prv&#10;        curr.keys.remove(key)&#10;        if not curr.keys: self._remove_bucket(curr)&#10;    def getMaxKey(self) -&gt; str:&#10;        return next(iter(self.tail.prev.keys)) if self.tail.prev != self.head else &quot;&quot;&#10;    def getMinKey(self) -&gt; str:&#10;        return next(iter(self.head.next.keys)) if self.head.next != self.tail else &quot;&quot;</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">31</td>
      <td rowspan="1">Ll 31 Flatten A Multilevel Doubly Linked List<br><br></b> <a href="https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/" target="_blank">LeetCode 430</a></td>
      <td rowspan="1"><b>Example 1:</b> DFS / Recursion.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Iterate through the list. When a node has a child, find the tail of the child list. Connect the tail to `node->next`, and `node->next` to the child. Update `prev` pointers. Set `node->child` to `nullptr`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def flatten(head: &#x27;Optional[Node]&#x27;) -&gt; &#x27;Optional[Node]&#x27;:&#10;    if not head: return None&#10;    curr = head&#10;    while curr:&#10;        if curr.child:&#10;            tail = curr.child&#10;            while tail.next: tail = tail.next&#10;            tail.next = curr.next&#10;            if curr.next: curr.next.prev = tail&#10;            curr.next = curr.child&#10;            curr.child.prev = curr&#10;            curr.child = None&#10;        curr = curr.next&#10;    return head</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">32</td>
      <td rowspan="1">Ll 32 Multiply Two Linked Lists<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/multiply-two-linked-lists/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Traverse and compute numbers.</td>
      <td><b>Time:</b> O(N + M)<br><b>Space:</b> O(1)</td>
      <td>Traverse the first linked list and compute the number it represents modulo 10^9+7. Do the same for the second linked list. Multiply the two numbers and return the result modulo 10^9+7.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def multiplyTwoLists(head1: Node, head2: Node) -&gt; int:&#10;    num1 = num2 = 0&#10;    mod = 10**9 + 7&#10;    while head1:&#10;        num1 = (num1 * 10 + head1.data) % mod&#10;        head1 = head1.next&#10;    while head2:&#10;        num2 = (num2 * 10 + head2.data) % mod&#10;        head2 = head2.next&#10;    return (num1 * num2) % mod</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">33</td>
      <td rowspan="1">Ll 33 Delete Nodes Having Greater Value On Right<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/delete-nodes-having-greater-value-on-right/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Reverse, filter, reverse.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Reverse the linked list. Traverse the reversed list and keep track of the maximum value seen so far. If a node's value is less than the maximum, delete it. Otherwise, update the maximum. Finally, reverse the list again.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def compute(head: Node) -&gt; Node:&#10;    def reverseList(node):&#10;        prev, curr = None, node&#10;        while curr:&#10;            nxt = curr.next&#10;            curr.next = prev&#10;            prev = curr&#10;            curr = nxt&#10;        return prev&#10;    head = reverseList(head)&#10;    curr = head&#10;    max_val = head.data&#10;    while curr and curr.next:&#10;        if curr.next.data &lt; max_val:&#10;            curr.next = curr.next.next&#10;        else:&#10;            curr = curr.next&#10;            max_val = curr.data&#10;    return reverseList(head)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">34</td>
      <td rowspan="1">Ll 34 Segregate Even And Odd Nodes In A Linked List<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/segregate-even-and-odd-nodes-in-a-linked-list5035/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Two pointers for even and odd.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Create two dummy nodes, one for the even list and one for the odd list. Traverse the original list and append even nodes to the even list and odd nodes to the odd list. Finally, connect the end of the even list to the head of the odd list and terminate the odd list with NULL.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def divide(N: int, head: Node) -&gt; Node:&#10;    evenStart = evenEnd = None&#10;    oddStart = oddEnd = None&#10;    curr = head&#10;    while curr:&#10;        val = curr.data&#10;        if val % 2 == 0:&#10;            if not evenStart:&#10;                evenStart = evenEnd = curr&#10;            else:&#10;                evenEnd.next = curr&#10;                evenEnd = evenEnd.next&#10;        else:&#10;            if not oddStart:&#10;                oddStart = oddEnd = curr&#10;            else:&#10;                oddEnd.next = curr&#10;                oddEnd = oddEnd.next&#10;        curr = curr.next&#10;    if not oddStart or not evenStart: return head&#10;    evenEnd.next = oddStart&#10;    oddEnd.next = None&#10;    return evenStart</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">35</td>
      <td rowspan="1">Ll 35 Nth Node From End Of Linked List<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Two pointers.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Use two pointers, `fast` and `slow`. Move `fast` `N` steps ahead. If `fast` becomes NULL before `N` steps, return -1 (N > length). Then move both `fast` and `slow` one step at a time until `fast` reaches the end. `slow` will be pointing to the Nth node from the end.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def getNthFromLast(head: Node, n: int) -&gt; int:&#10;    fast, slow = head, head&#10;    for _ in range(n):&#10;        if not fast: return -1&#10;        fast = fast.next&#10;    while fast:&#10;        slow = slow.next&#10;        fast = fast.next&#10;    return slow.data</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">36</td>
      <td rowspan="1">Ll 36 First Non Repeating Character In A Stream<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/first-non-repeating-character-in-a-stream1216/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Queue and frequency array.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Use a queue to maintain the order of characters and an array to keep track of their frequencies. For each character, increment its frequency and push it to the queue. Then, while the queue is not empty and the frequency of the front character is greater than 1, pop it. If the queue is empty, append '#', else append the front character.<br><br><b>Dependencies:</b> <code>#include <queue></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def FirstNonRepeating(A: str) -&gt; str:&#10;    freq = [0] * 26&#10;    q = collections.deque()&#10;    res = []&#10;    for c in A:&#10;        freq[ord(c) - ord(&#x27;a&#x27;)] += 1&#10;        q.append(c)&#10;        while q and freq[ord(q[0]) - ord(&#x27;a&#x27;)] &gt; 1:&#10;            q.popleft()&#10;        if not q: res.append(&#x27;#&#x27;)&#10;        else: res.append(q[0])&#10;    return &quot;&quot;.join(res)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">37</td>
      <td rowspan="1">Ll 37 Clone A Linked List With Next And Random Pointer<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/clone-a-linked-list-with-next-and-random-pointer/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Interleaving lists.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Create a copy of each node and insert it immediately after the original node. Then, set the random pointers for the copied nodes (`curr->next->arb = curr->arb ? curr->arb->next : NULL`). Finally, separate the original and copied lists.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def copyList(head: Node) -&gt; Node:&#10;    if not head: return None&#10;    curr = head&#10;    while curr:&#10;        temp = Node(curr.data)&#10;        temp.next = curr.next&#10;        curr.next = temp&#10;        curr = temp.next&#10;    curr = head&#10;    while curr:&#10;        if curr.arb:&#10;            curr.next.arb = curr.arb.next&#10;        curr = curr.next.next&#10;    curr = head&#10;    copyHead = head.next&#10;    copyCurr = copyHead&#10;    while curr:&#10;        curr.next = curr.next.next&#10;        if copyCurr.next:&#10;            copyCurr.next = copyCurr.next.next&#10;        curr = curr.next&#10;        copyCurr = copyCurr.next&#10;    return copyHead</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">38</td>
      <td rowspan="1">Ll 38 Merge K Sorted Linked Lists<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/merge-k-sorted-linked-lists/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Min-Heap.</td>
      <td><b>Time:</b> O(N * K * log K)<br><b>Space:</b> O(K)</td>
      <td>Create a min-heap and push the head of each linked list into it. Pop the minimum element, append it to the result list, and if the popped node has a next node, push the next node into the heap. Continue until the heap is empty.<br><br><b>Dependencies:</b> <code>#include <queue></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def mergeKLists(arr: List[Node], K: int) -&gt; Node:&#10;    pq = []&#10;    for i in range(K):&#10;        if arr[i]:&#10;            heapq.heappush(pq, (arr[i].data, i, arr[i]))&#10;    dummy = Node(0)&#10;    tail = dummy&#10;    while pq:&#10;        val, idx, curr = heapq.heappop(pq)&#10;        tail.next = curr&#10;        tail = tail.next&#10;        if curr.next:&#10;            heapq.heappush(pq, (curr.next.data, idx, curr.next))&#10;    return dummy.next</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">39</td>
      <td rowspan="1">Ll 39 Reverse A Linked List In Groups Of Given Size<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/reverse-a-linked-list-in-groups-of-given-size/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Recursive grouping.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N/K)</td>
      <td>Reverse the first `k` nodes of the linked list iteratively. After reversing, the `head` pointer will be the end of the reversed group, and `curr` will point to the next node. Recursively call the function for `curr` and set `head->next` to the result.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def reverse(head: Node, k: int) -&gt; Node:&#10;    if not head: return None&#10;    curr, prev, nxt = head, None, None&#10;    count = 0&#10;    while curr and count &lt; k:&#10;        nxt = curr.next&#10;        curr.next = prev&#10;        prev = curr&#10;        curr = nxt&#10;        count += 1&#10;    if nxt:&#10;        head.next = reverse(nxt, k)&#10;    return prev</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">40</td>
      <td rowspan="1">Ll 40 Split A Circular Linked List Into Two Halves<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/split-a-circular-linked-list-into-two-halves/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Slow and Fast Pointer.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Use slow and fast pointers to find the mid of the circular linked list. The slow pointer will point to the mid. Then break the list into two and make both circular.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def splitList(head, head1, head2):&#10;    if head is None: return&#10;    slow, fast = head, head&#10;    while fast.next != head and fast.next.next != head:&#10;        slow = slow.next&#10;        fast = fast.next.next&#10;    if fast.next.next == head:&#10;        fast = fast.next&#10;    head1.head = head&#10;    if head.next != head:&#10;        head2.head = slow.next&#10;    fast.next = slow.next&#10;    slow.next = head</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">41</td>
      <td rowspan="1">Ll 41 Check If Circular Linked List<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/circular-linked-list/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Traverse to head.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Traverse the linked list starting from head. If we reach NULL, it's not circular. If we reach head again, it is circular.</td>
      <td><b>Edge Cases:</b> Empty list<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isCircular(head):&#10;    if head is None: return True&#10;    temp = head.next&#10;    while temp is not None and temp != head:&#10;        temp = temp.next&#10;    return temp == head</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">42</td>
      <td rowspan="1">Ll 42 Count Triplets In A Sorted Doubly Linked List Whose Sum Is Equal To Given Value X<br><br></b> <a href="https://www.geeksforgeeks.org/count-triplets-sorted-doubly-linked-list-whose-sum-equal-given-value-x/" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Two Pointers.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(1)</td>
      <td>Iterate through the list. For each node, use two pointers (left and right) on the remaining list to find pairs that sum to `x - node.data`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def countTriplets(head, x):&#10;    if head is None: return 0&#10;    last = head&#10;    while last.next: last = last.next&#10;    count = 0&#10;    curr = head&#10;    while curr:&#10;        first = curr.next&#10;        right = last&#10;        while first and right and first != right and right.next != first:&#10;            total = curr.data + first.data + right.data&#10;            if total == x:&#10;                count += 1&#10;                first = first.next&#10;                right = right.prev&#10;            elif total &lt; x:&#10;                first = first.next&#10;            else:&#10;                right = right.prev&#10;        curr = curr.next&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">43</td>
      <td rowspan="1">Ll 43 Sort A K Sorted Doubly Linked List<br><br></b> <a href="https://www.geeksforgeeks.org/sort-k-sorted-doubly-linked-list/" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Min Heap.</td>
      <td><b>Time:</b> O(N log K)<br><b>Space:</b> O(K)</td>
      <td>Create a Min Heap of size k+1. Insert the first k+1 elements into the heap. Then, pop the minimum element, place it in the sorted list, and push the next element from the original list into the heap.<br><br><b>Dependencies:</b> Priority Queue</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def sortAKSortedDLL(head, k):&#10;    if not head: return head&#10;    pq = []&#10;    newHead, last = None, None&#10;    i = 0&#10;    while head and i &lt;= k:&#10;        heapq.heappush(pq, (head.data, id(head), head))&#10;        head = head.next&#10;        i += 1&#10;    while pq:&#10;        _, _, minNode = heapq.heappop(pq)&#10;        if not newHead:&#10;            newHead = minNode&#10;            newHead.prev = None&#10;            last = newHead&#10;        else:&#10;            last.next = minNode&#10;            minNode.prev = last&#10;            last = minNode&#10;        if head:&#10;            heapq.heappush(pq, (head.data, id(head), head))&#10;            head = head.next&#10;    last.next = None&#10;    return newHead</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">44</td>
      <td rowspan="1">Ll 44 Rotate Doubly Linked List By N Nodes<br><br></b> <a href="https://www.geeksforgeeks.org/rotate-doubly-linked-list-n-nodes/" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Traverse and link.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Traverse to the Nth node. This will be the new tail. Its next will be the new head. Traverse to the end of the list and link it to the original head.</td>
      <td><b>Edge Cases:</b> N == 0<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def rotateDLL(start, N):&#10;    if N == 0: return start&#10;    current = start&#10;    count = 1&#10;    while count &lt; N and current:&#10;        current = current.next&#10;        count += 1&#10;    if not current: return start&#10;    nthNode = current&#10;    while current.next:&#10;        current = current.next&#10;    current.next = start&#10;    start.prev = current&#10;    start = nthNode.next&#10;    start.prev = None&#10;    nthNode.next = None&#10;    return start</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">45</td>
      <td rowspan="1">Ll 45 Reverse A Doubly Linked List In Groups Of Given Size<br><br></b> <a href="https://www.geeksforgeeks.org/reverse-doubly-linked-list-groups-given-size/" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Recursion.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N/K) recursion stack</td>
      <td>Similar to reversing singly linked list in groups of k. Keep track of prev, next, and current. Reverse k nodes, then recursively call for the rest of the list.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def revListInGroupOfGivenSize(head, k):&#10;    if not head: return None&#10;    current = head&#10;    next_node = None&#10;    new_head = None&#10;    count = 0&#10;    while current and count &lt; k:&#10;        next_node = current.next&#10;        current.prev = next_node&#10;        current.next = new_head&#10;        if new_head:&#10;            new_head.prev = current&#10;        new_head = current&#10;        current = next_node&#10;        count += 1&#10;    if next_node:&#10;        head.next = revListInGroupOfGivenSize(next_node, k)&#10;        head.next.prev = head&#10;    return new_head</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">46</td>
      <td rowspan="1">Ll 46 Can We Reverse A Linked List In Less Than On<br><br></b> N/A</td>
      <td rowspan="1"><b>Example 1:</b> Theoretical Question.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>No, it is not possible. To reverse a linked list, we must visit every single node at least once to change its pointer. Therefore, the minimum time complexity required is strictly O(N), where N is the number of nodes in the linked list.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python"># It is not possible to reverse in less than O(n).</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">47</td>
      <td rowspan="1">Ll 47 Find The First Node Of Loop In Linked List<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/find-the-first-node-of-loop-in-linked-list--170645/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Floyd's Cycle Detection.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Use Floyd's Cycle Detection to find if a cycle exists (slow and fast pointers meet). Then, move slow back to head, and advance both slow and fast by one step until they meet. The meeting point is the start of the loop.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findFirstNode(head):&#10;    slow = head&#10;    fast = head&#10;    while fast and fast.next:&#10;        slow = slow.next&#10;        fast = fast.next.next&#10;        if slow == fast:&#10;            slow = head&#10;            while slow != fast:&#10;                slow = slow.next&#10;                fast = fast.next&#10;            return slow.data&#10;    return -1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">48</td>
      <td rowspan="1">Ll 48 Detect Loop In Linked List<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/detect-loop-in-linked-list/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Floyd's Cycle Detection.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Use Floyd's Cycle Detection algorithm (Tortoise and Hare). Move `slow` by 1 and `fast` by 2. If they meet, a loop exists. If `fast` reaches NULL, there is no loop.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def detectLoop(head):&#10;    slow = fast = head&#10;    while fast and fast.next:&#10;        slow = slow.next&#10;        fast = fast.next.next&#10;        if slow == fast: return True&#10;    return False</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">49</td>
      <td rowspan="1">Ll 49 Remove Loop In Linked List<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/remove-loop-in-linked-list/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Floyd's Cycle Detection + Loop removal.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Use Floyd's Cycle Detection. If a loop is found, reset `slow` to head. Move both `slow` and `fast` by 1. The node where they meet is the start of the loop. Keep track of `fast`'s previous node to set its `next` to NULL.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def removeLoop(head):&#10;    if not head or not head.next: return&#10;    slow = fast = head&#10;    while fast and fast.next:&#10;        slow = slow.next&#10;        fast = fast.next.next&#10;        if slow == fast: break&#10;    if slow == fast:&#10;        slow = head&#10;        if slow == fast:&#10;            while fast.next != slow: fast = fast.next&#10;        else:&#10;            while slow.next != fast.next:&#10;                slow = slow.next&#10;                fast = fast.next&#10;        fast.next = None</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">50</td>
      <td rowspan="1">Ll 50 Remove Duplicates From An Unsorted Linked List<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/remove-duplicates-from-an-unsorted-linked-list/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Hash set.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Use a hash set to store the seen values. Iterate the list. If a node's value is in the set, skip it by updating the `next` pointer of the `prev` node. Else, add it to the set and update `prev`.<br><br><b>Dependencies:</b> Hash Set</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def removeDuplicates(head):&#10;    if not head: return None&#10;    seen = set()&#10;    curr, prev = head, None&#10;    while curr:&#10;        if curr.data in seen:&#10;            prev.next = curr.next&#10;            curr = prev.next&#10;        else:&#10;            seen.add(curr.data)&#10;            prev = curr&#10;            curr = curr.next&#10;    return head</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">51</td>
      <td rowspan="1">Ll 51 Move Last Element To Front Of A Given Linked List<br><br></b> <a href="https://www.geeksforgeeks.org/move-last-element-to-front-of-a-given-linked-list/" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Two Pointers.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Traverse the list to find the last node (`tail`) and the second last node (`sec_last`). Make `sec_last->next = NULL`, `tail->next = head`, and update `head = tail`.</td>
      <td><b>Edge Cases:</b> Empty list or Single node<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def moveToFront(head):&#10;    if not head or not head.next: return head&#10;    sec_last = None&#10;    tail = head&#10;    while tail.next:&#10;        sec_last = tail&#10;        tail = tail.next&#10;    sec_last.next = None&#10;    tail.next = head&#10;    return tail</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">52</td>
      <td rowspan="1">Ll 52 Add 1 To A Number Represented As Linked List<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/add-1-to-a-number-represented-as-linked-list/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Reverse, Add, Reverse.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Reverse the linked list. Add 1 to the first node, and propagate the carry if the value becomes 10. Once done, reverse the list back. If carry still remains at the end, add a new node.</td>
      <td><b>Edge Cases:</b> 999 -> 1000<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def addOne(head):&#10;    def reverse(node):&#10;        curr, prev, nxt = node, None, None&#10;        while curr:&#10;            nxt = curr.next&#10;            curr.next = prev&#10;            prev = curr&#10;            curr = nxt&#10;        return prev&#10;    head = reverse(head)&#10;    curr, prev = head, None&#10;    carry = 1&#10;    while curr:&#10;        total = curr.data + carry&#10;        carry = total // 10&#10;        curr.data = total % 10&#10;        prev = curr&#10;        curr = curr.next&#10;    if carry &gt; 0:&#10;        prev.next = Node(carry)&#10;    return reverse(head)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">53</td>
      <td rowspan="1">Ll 53 Add Two Numbers Represented By Linked Lists<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/add-two-numbers-represented-by-linked-lists/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Reverse, Add, Reverse.</td>
      <td><b>Time:</b> O(max(N, M))<br><b>Space:</b> O(max(N, M))</td>
      <td>Reverse both linked lists. Traverse both lists simultaneously, adding the data values of corresponding nodes along with the carry. Create new nodes for the sum and append them to the result list. Finally, reverse the result list.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def addTwoLists(first, second):&#10;    def reverse(node):&#10;        curr, prev, nxt = node, None, None&#10;        while curr:&#10;            nxt = curr.next&#10;            curr.next = prev&#10;            prev = curr&#10;            curr = nxt&#10;        return prev&#10;    first = reverse(first)&#10;    second = reverse(second)&#10;    dummy = Node(0)&#10;    temp = dummy&#10;    carry = 0&#10;    while first or second or carry:&#10;        total = carry&#10;        if first: total += first.data; first = first.next&#10;        if second: total += second.data; second = second.next&#10;        carry = total // 10&#10;        temp.next = Node(total % 10)&#10;        temp = temp.next&#10;    return reverse(dummy.next)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">54</td>
      <td rowspan="1">Ll 54 Intersection Of Two Sorted Linked Lists<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/intersection-of-two-sorted-linked-lists/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Two Pointers.</td>
      <td><b>Time:</b> O(N + M)<br><b>Space:</b> O(N + M)</td>
      <td>Use two pointers, `ptr1` for the first list and `ptr2` for the second. If `ptr1->data < ptr2->data`, `ptr1++`. If `ptr2->data < ptr1->data`, `ptr2++`. If they are equal, add to the result list and advance both.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findIntersection(head1, head2):&#10;    dummy = Node(0)&#10;    temp = dummy&#10;    p1, p2 = head1, head2&#10;    while p1 and p2:&#10;        if p1.data &lt; p2.data: p1 = p1.next&#10;        elif p2.data &lt; p1.data: p2 = p2.next&#10;        else:&#10;            temp.next = Node(p1.data)&#10;            temp = temp.next&#10;            p1 = p1.next&#10;            p2 = p2.next&#10;    return dummy.next</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">55</td>
      <td rowspan="1">Ll 55 Intersection Point In Y Shaped Linked Lists<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/intersection-point-in-y-shapped-linked-lists/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Two Pointers.</td>
      <td><b>Time:</b> O(N + M)<br><b>Space:</b> O(1)</td>
      <td>Use two pointers `a` and `b`. Traverse both lists. When `a` reaches the end, redirect it to `head2`. When `b` reaches the end, redirect it to `head1`. They will meet at the intersection point or both become NULL.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def intersectPoint(head1, head2):&#10;    a, b = head1, head2&#10;    while a != b:&#10;        a = a.next if a else head2&#10;        b = b.next if b else head1&#10;    if a: return a.data&#10;    return -1</code></pre></details></td>
    </tr>
  </tbody>
</table>


## Stacks Queues

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
      <td rowspan="1">1</td>
      <td rowspan="1">Sq 01 Valid Parentheses<br><br></b> <a href="https://leetcode.com/problems/valid-parentheses/" target="_blank">LeetCode 20</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> s = "()[]{}"<br><b>Output:</b> true</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Use a Stack. Push open brackets. If a closed bracket is found, verify it matches the top of the stack and pop.<br><br><b>Dependencies:</b> <code>std::stack</code></td>
      <td><b>Edge Cases:</b> <b>Empty Stack / Unmatched:</b> If a closed bracket arrives while the stack is empty, it's invalid. If stack is NOT empty at the end, it's invalid.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isValid(s: str) -&gt; bool:&#10;    st = []&#10;    mapping = {&#x27;)&#x27;: &#x27;(&#x27;, &#x27;}&#x27;: &#x27;{&#x27;, &#x27;]&#x27;: &#x27;[&#x27;}&#10;    for char in s:&#10;        if char in mapping:&#10;            top = st.pop() if st else &#x27;#&#x27;&#10;            if mapping[char] != top: return False&#10;        else:&#10;            st.append(char)&#10;    return not st</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">2</td>
      <td rowspan="1">Sq 02 Next Greater Element I<br><br></b> <a href="https://leetcode.com/problems/next-greater-element-i/" target="_blank">LeetCode 496</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> nums1 = [4,1,2], nums2 = [1,3,4,2]<br><b>Output:</b> [-1,3,-1]</td>
      <td><b>Time:</b> O(N + M)<br><b>Space:</b> O(N)</td>
      <td>Monotonic Stack traversing `nums2` from right to left. Maintain stack of elements in decreasing order.<br><br><b>Dependencies:</b> <code>std::stack</code>, <code>std::unordered_map</code></td>
      <td><b>Edge Cases:</b> <b>No greater element:</b> If stack becomes empty after popping smaller elements, there is no NGE, store `-1`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def nextGreaterElement(nums1: list[int], nums2: list[int]) -&gt; list[int]:&#10;    mpp = {}&#10;    st = []&#10;    for num in reversed(nums2):&#10;        while st and st[-1] &lt;= num: st.pop()&#10;        mpp[num] = st[-1] if st else -1&#10;        st.append(num)&#10;    return [mpp[num] for num in nums1]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">3</td>
      <td rowspan="1">Sq 03 Min Stack<br><br></b> <a href="https://leetcode.com/problems/min-stack/" target="_blank">LeetCode 155</a></td>
      <td rowspan="1"><b>Example 1:</b> MinStack minStack = new MinStack(); minStack.push(-2); minStack.push(0); minStack.push(-3); minStack.getMin(); // return -3</td>
      <td><b>Time:</b> O(1) per operation<br><b>Space:</b> O(N)</td>
      <td>Store pairs of `(value, current_minimum)` in the stack. Alternatively, use math to encode the difference between the value and the minimum to achieve O(1) space auxiliary, but a stack of pairs is standard.<br><br><b>Dependencies:</b> <code>#include <stack></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class MinStack:&#10;    def __init__(self):&#10;        self.st = []&#10;    def push(self, val: int) -&gt; None:&#10;        if not self.st:&#10;            self.st.append((val, val))&#10;        else:&#10;            self.st.append((val, min(val, self.st[-1][1])))&#10;    def pop(self) -&gt; None:&#10;        self.st.pop()&#10;    def top(self) -&gt; int:&#10;        return self.st[-1][0]&#10;    def getMin(self) -&gt; int:&#10;        return self.st[-1][1]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">4</td>
      <td rowspan="1">Sq 04 Largest Rectangle In Histogram<br><br></b> <a href="https://leetcode.com/problems/largest-rectangle-in-histogram/" target="_blank">LeetCode 84</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> heights = [2,1,5,6,2,3]<br><b>Output:</b> 10</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Monotonic Stack. Find the next smaller element on the left and right for each bar. Area for bar `i` is `heights[i] * (right[i] - left[i] + 1)`. Alternatively, do it in a single pass stack loop.<br><br><b>Dependencies:</b> <code>#include <stack></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def largestRectangleArea(heights: List[int]) -&gt; int:&#10;    n, maxArea = len(heights), 0&#10;    st = []&#10;    for i in range(n + 1):&#10;        while st and (i == n or heights[st[-1]] &gt;= heights[i]):&#10;            height = heights[st.pop()]&#10;            width = i if not st else i - st[-1] - 1&#10;            maxArea = max(maxArea, width * height)&#10;        st.append(i)&#10;    return maxArea</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">5</td>
      <td rowspan="1">Sq 05 Reverse A String Using Stack<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/reverse-a-string-using-stack/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Push and pop.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Push all characters of the string into a stack. Then pop them out one by one. The popped characters will be in reversed order.<br><br><b>Dependencies:</b> <code>#include <stack></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def reverse(S: str) -&gt; str:&#10;    st = []&#10;    for c in S:&#10;        st.append(c)&#10;    res = &quot;&quot;&#10;    while st:&#10;        res += st.pop()&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">6</td>
      <td rowspan="1">Sq 06 Design A Stack That Supports Getmin<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/special-stack/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Formula approach.</td>
      <td><b>Time:</b> O(1)<br><b>Space:</b> O(1)</td>
      <td>To achieve O(1) space, when pushing `x < minEle`, push `2 * x - minEle` and update `minEle = x`. When popping `y`, if `y < minEle`, then `minEle = 2 * minEle - y`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class SpecialStack:&#10;    def __init__(self):&#10;        self.s = []&#10;        self.minEle = float(&#x27;inf&#x27;)&#10;    def push(self, a):&#10;        if not self.s:&#10;            self.s.append(a)&#10;            self.minEle = a&#10;        elif a &lt; self.minEle:&#10;            self.s.append(2 * a - self.minEle)&#10;            self.minEle = a&#10;        else:&#10;            self.s.append(a)&#10;    def pop(self):&#10;        if not self.s: return -1&#10;        top = self.s.pop()&#10;        if top &lt; self.minEle:&#10;            prevMin = self.minEle&#10;            self.minEle = 2 * self.minEle - top&#10;            return prevMin&#10;        return top&#10;    def getMin(self):&#10;        if not self.s: return -1&#10;        return self.minEle</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">7</td>
      <td rowspan="1">Sq 07 Next Greater Element<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/next-larger-element-1587115620/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Decreasing stack.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Iterate from right to left. Use a stack to keep track of elements. Pop from the stack while the top element is less than or equal to the current element. If stack is empty, NGE is -1, else it's the stack top. Push current element.<br><br><b>Dependencies:</b> <code>#include <stack></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def nextLargerElement(arr: List[int], n: int) -&gt; List[int]:&#10;    res = [-1] * n&#10;    st = []&#10;    for i in range(n - 1, -1, -1):&#10;        while st and st[-1] &lt;= arr[i]:&#10;            st.pop()&#10;        if st:&#10;            res[i] = st[-1]&#10;        st.append(arr[i])&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">8</td>
      <td rowspan="1">Sq 08 Celebrity Problem<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/the-celebrity-problem/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Two pointers or Stack.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Push all elements (0 to N-1) into a stack. Pop two elements `A` and `B`. If `A` knows `B`, `A` cannot be a celebrity, push `B` back. If `A` does not know `B`, `B` cannot be a celebrity, push `A` back. The remaining element is a potential celebrity. Verify it by checking if everyone knows it and it knows no one.<br><br><b>Dependencies:</b> <code>#include <stack></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def celebrity(M: List[List[int]], n: int) -&gt; int:&#10;    st = list(range(n))&#10;    while len(st) &gt; 1:&#10;        a = st.pop()&#10;        b = st.pop()&#10;        if M[a][b] == 1:&#10;            st.append(b)&#10;        else:&#10;            st.append(a)&#10;    if not st: return -1&#10;    pot = st[0]&#10;    for i in range(n):&#10;        if i != pot and (M[pot][i] == 1 or M[i][pot] == 0):&#10;            return -1&#10;    return pot</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">9</td>
      <td rowspan="1">Sq 09 Arithmetic Expression Evaluation<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/arithmetic-expression-evaluation/0" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Two stacks (operands and operators).</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Use two stacks: one for numbers and one for operators. Process the expression character by character. If it's a number, push to numbers stack. If it's `(`, push to operators stack. If it's `)`, solve until `(`. If it's an operator, solve while top of operators stack has same or greater precedence, then push.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def evaluate(tokens: str) -&gt; int:&#10;    def precedence(op):&#10;        if op in (&#x27;+&#x27;, &#x27;-&#x27;): return 1&#10;        if op in (&#x27;*&#x27;, &#x27;/&#x27;): return 2&#10;        return 0&#10;    def applyOp(a, b, op):&#10;        if op == &#x27;+&#x27;: return a + b&#10;        if op == &#x27;-&#x27;: return a - b&#10;        if op == &#x27;*&#x27;: return a * b&#10;        if op == &#x27;/&#x27;: return a // b&#10;        return 0&#10;    values = []&#10;    ops = []&#10;    i = 0&#10;    while i &lt; len(tokens):&#10;        if tokens[i] == &#x27; &#x27;:&#10;            i += 1&#10;            continue&#10;        elif tokens[i] == &#x27;(&#x27;:&#10;            ops.append(tokens[i])&#10;        elif tokens[i].isdigit():&#10;            val = 0&#10;            while i &lt; len(tokens) and tokens[i].isdigit():&#10;                val = (val * 10) + int(tokens[i])&#10;                i += 1&#10;            values.append(val)&#10;            i -= 1&#10;        elif tokens[i] == &#x27;)&#x27;:&#10;            while ops and ops[-1] != &#x27;(&#x27;:&#10;                val2 = values.pop()&#10;                val1 = values.pop()&#10;                op = ops.pop()&#10;                values.append(applyOp(val1, val2, op))&#10;            ops.pop()&#10;        else:&#10;            while ops and precedence(ops[-1]) &gt;= precedence(tokens[i]):&#10;                val2 = values.pop()&#10;                val1 = values.pop()&#10;                op = ops.pop()&#10;                values.append(applyOp(val1, val2, op))&#10;            ops.append(tokens[i])&#10;        i += 1&#10;    while ops:&#10;        val2 = values.pop()&#10;        val1 = values.pop()&#10;        op = ops.pop()&#10;        values.append(applyOp(val1, val2, op))&#10;    return values[-1]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">10</td>
      <td rowspan="1">Sq 10 Evaluation Of Postfix Expression<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/evaluation-of-postfix-expression1735/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Stack of operands.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Iterate through the string. If it's a number, push it to stack. If it's an operator, pop two numbers from stack, apply the operator, and push the result back to stack.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def evaluatePostfix(S: str) -&gt; int:&#10;    st = []&#10;    for c in S:&#10;        if c.isdigit():&#10;            st.append(int(c))&#10;        else:&#10;            op2 = st.pop()&#10;            op1 = st.pop()&#10;            if c == &#x27;+&#x27;: st.append(op1 + op2)&#10;            elif c == &#x27;-&#x27;: st.append(op1 - op2)&#10;            elif c == &#x27;*&#x27;: st.append(op1 * op2)&#10;            elif c == &#x27;/&#x27;: st.append(int(op1 / op2))&#10;    return st[-1]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">11</td>
      <td rowspan="1">Sq 11 Insert An Element At Its Bottom In A Given Stack<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/insert-an-element-at-the-bottom-of-a-stack/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Recursive push.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Use recursion. If the stack is empty, push the element. Otherwise, pop the top element, recursively call the function, and then push the popped element back.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def insertAtBottom(St: List[int], X: int) -&gt; List[int]:&#10;    if not St:&#10;        St.append(X)&#10;        return St&#10;    top = St.pop()&#10;    insertAtBottom(St, X)&#10;    St.append(top)&#10;    return St</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">12</td>
      <td rowspan="1">Sq 12 Reverse A Stack Using Recursion<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/reverse-a-stack/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Recursive pop and insertAtBottom.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N)</td>
      <td>Recursively pop all elements until the stack is empty. Then, as the recursion unwinds, use another recursive function `insertAtBottom` to push the elements at the bottom.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def Reverse(St: List[int]) -&gt; None:&#10;    def insertAtBottom(St, X):&#10;        if not St:&#10;            St.append(X)&#10;            return&#10;        top = St.pop()&#10;        insertAtBottom(St, X)&#10;        St.append(top)&#10;    if not St: return&#10;    top = St.pop()&#10;    Reverse(St)&#10;    insertAtBottom(St, top)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">13</td>
      <td rowspan="1">Sq 13 Maximum Rectangular Area In A Histogram<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/maximum-rectangular-area-in-a-histogram-1587115620/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Next Smaller Element on left and right.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Use a stack to find Next Smaller Element (NSE) and Previous Smaller Element (PSE) for each bar. Then, the width of the rectangle with bar `i` as the minimum height is `NSE[i] - PSE[i] - 1`. The area is `height[i] * width`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def getMaxArea(arr: List[int], n: int) -&gt; int:&#10;    st = []&#10;    max_area = 0&#10;    for i in range(n + 1):&#10;        while st and (i == n or arr[st[-1]] &gt;= arr[i]):&#10;            height = arr[st.pop()]&#10;            width = i if not st else i - st[-1] - 1&#10;            max_area = max(max_area, height * width)&#10;        st.append(i)&#10;    return max_area</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">14</td>
      <td rowspan="1">Sq 14 Next Smaller Element<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/fab3281cefac7140ca15e21505beddf7e4323e08/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Monotonic Stack.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Iterate from right to left. Use a monotonic stack. Pop elements from the stack that are greater than or equal to the current element. The top of the stack is the next smaller element. Push the current element to the stack.<br><br><b>Dependencies:</b> Stack</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def help_classmate(arr, n):&#10;    ans = [-1] * n&#10;    s = []&#10;    for i in range(n - 1, -1, -1):&#10;        while s and s[-1] &gt;= arr[i]: s.pop()&#10;        if s: ans[i] = s[-1]&#10;        s.append(arr[i])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">15</td>
      <td rowspan="1">Sq 15 Maximal Rectangle<br><br></b> <a href="https://leetcode.com/problems/maximal-rectangle/" target="_blank">LeetCode 85</a></td>
      <td rowspan="1"><b>Example 1:</b> Largest Rectangle in Histogram reduction.</td>
      <td><b>Time:</b> O(rows * cols)<br><b>Space:</b> O(cols)</td>
      <td>Treat each row as the base of a histogram. The height of each bar is the number of consecutive 1s above it. Apply the Largest Rectangle in Histogram algorithm for each row and maintain the maximum area.<br><br><b>Dependencies:</b> Stack</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maximalRectangle(matrix):&#10;    if not matrix: return 0&#10;    rows, cols = len(matrix), len(matrix[0])&#10;    heights = [0] * cols&#10;    maxArea = 0&#10;    def largestRectangleArea(h):&#10;        s, max_a = [], 0&#10;        for i, val in enumerate(h + [0]):&#10;            while s and h[s[-1]] &gt;= val:&#10;                height = h[s.pop()]&#10;                width = i if not s else i - s[-1] - 1&#10;                max_a = max(max_a, height * width)&#10;            s.append(i)&#10;        return max_a&#10;    for row in matrix:&#10;        for j in range(cols):&#10;            heights[j] = heights[j] + 1 if row[j] == &#x27;1&#x27; else 0&#10;        maxArea = max(maxArea, largestRectangleArea(heights))&#10;    return maxArea</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">16</td>
      <td rowspan="1">Sq 16 Online Stock Span<br><br></b> <a href="https://leetcode.com/problems/online-stock-span/" target="_blank">LeetCode 901</a></td>
      <td rowspan="1"><b>Example 1:</b> Monotonic Stack.</td>
      <td><b>Time:</b> O(1) amortized<br><b>Space:</b> O(N)</td>
      <td>Use a stack of pairs `(price, span)`. When a new price comes in, initialize its span to 1. Pop elements from the stack while the top element's price is `<= price`, adding their spans to the current span. Push `(price, span)` to the stack.<br><br><b>Dependencies:</b> Stack</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class StockSpanner:&#10;    def __init__(self):&#10;        self.s = []&#10;    def next(self, price: int) -&gt; int:&#10;        span = 1&#10;        while self.s and self.s[-1][0] &lt;= price:&#10;            span += self.s.pop()[1]&#10;        self.s.append((price, span))&#10;        return span</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">17</td>
      <td rowspan="1">Sq 17 Rotten Oranges<br><br></b> <a href="https://leetcode.com/problems/rotting-oranges/" target="_blank">LeetCode 994</a></td>
      <td rowspan="1"><b>Example 1:</b> BFS.</td>
      <td><b>Time:</b> O(rows * cols)<br><b>Space:</b> O(rows * cols)</td>
      <td>Use a Queue for BFS. Find all initially rotten oranges and push them into the queue with time 0. Count total fresh oranges. Pop an orange, rot its adjacent fresh oranges, push them to the queue with `time + 1`, and decrement fresh count. Return the max time if fresh count is 0, else -1.<br><br><b>Dependencies:</b> Queue</td>
      <td><b>Edge Cases:</b> Grid without fresh oranges<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">from collections import deque&#10;def orangesRotting(grid):&#10;    rows, cols = len(grid), len(grid[0])&#10;    q = deque()&#10;    fresh_cnt = 0&#10;    for i in range(rows):&#10;        for j in range(cols):&#10;            if grid[i][j] == 2: q.append((i, j, 0))&#10;            elif grid[i][j] == 1: fresh_cnt += 1&#10;    tm, cnt = 0, 0&#10;    while q:&#10;        r, c, t = q.popleft()&#10;        tm = max(tm, t)&#10;        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:&#10;            nr, nc = r + dr, c + dc&#10;            if 0 &lt;= nr &lt; rows and 0 &lt;= nc &lt; cols and grid[nr][nc] == 1:&#10;                grid[nr][nc] = 2&#10;                q.append((nr, nc, t + 1))&#10;                cnt += 1&#10;    return tm if cnt == fresh_cnt else -1</code></pre></details></td>
    </tr>
  </tbody>
</table>


## Trees

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
      <td rowspan="1">1</td>
      <td rowspan="1">Tree 01 Binary Tree Inorder Traversal<br><br></b> <a href="https://leetcode.com/problems/binary-tree-inorder-traversal/" target="_blank">LeetCode 94</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> root = [1,null,2,3]<br><b>Output:</b> [1,3,2]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Recursive approach. Traverse Left, process Root, then traverse Right.</td>
      <td><b>Edge Cases:</b> <b>Recursion Depth:</b> Worst-case skewed tree takes `O(N)` space.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def inorderTraversal(root: TreeNode) -&gt; list[int]:&#10;    ans = []&#10;    def inorder(node):&#10;        if not node: return&#10;        inorder(node.left)&#10;        ans.append(node.val)&#10;        inorder(node.right)&#10;    inorder(root)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">2</td>
      <td rowspan="1">Tree 02 Maximum Depth Of Binary Tree<br><br></b> <a href="https://leetcode.com/problems/maximum-depth-of-binary-tree/" target="_blank">LeetCode 104</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> root = [3,9,20,null,null,15,7]<br><b>Output:</b> 3</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H) &cong; O(N)</td>
      <td>Recursively find the max depth of left and right subtrees. The depth is `1 + max(left_depth, right_depth)`.<br><br><b>Dependencies:</b> <code>std::max</code></td>
      <td><b>Edge Cases:</b> <b>Null Root:</b> If empty (`root == NULL`), depth is 0.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxDepth(root: TreeNode) -&gt; int:&#10;    if not root: return 0&#10;    return 1 + max(maxDepth(root.left), maxDepth(root.right))</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">3</td>
      <td rowspan="1">Tree 03 Lowest Common Ancestor Of A Binary Tree<br><br></b> <a href="https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/" target="_blank">LeetCode 236</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1<br><b>Output:</b> 3</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>If we find `p` or `q`, return it. If both left and right return non-null, current node is LCA.</td>
      <td><b>Edge Cases:</b> <b>Node is LCA:</b> If one is ancestor of other, it returns immediately.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -&gt; TreeNode:&#10;    if not root or root == p or root == q: return root&#10;    left = lowestCommonAncestor(root.left, p, q)&#10;    right = lowestCommonAncestor(root.right, p, q)&#10;    if not left: return right&#10;    elif not right: return left&#10;    else: return root</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">4</td>
      <td rowspan="1">Tree 04 Same Tree<br><br></b> <a href="https://leetcode.com/problems/same-tree/" target="_blank">LeetCode 100</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> p = [1,2,3], q = [1,2,3]<br><b>Output:</b> true</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Traverse both trees simultaneously. If both nodes are null, true. If one is null or values mismatch, false.</td>
      <td><b>Edge Cases:</b> <b>Structural mismatch:</b> Safely handled by `!p || !q`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isSameTree(p: TreeNode, q: TreeNode) -&gt; bool:&#10;    if not p and not q: return True&#10;    if not p or not q or p.val != q.val: return False&#10;    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">5</td>
      <td rowspan="1">Tree 05 Invert Binary Tree<br><br></b> <a href="https://leetcode.com/problems/invert-binary-tree/" target="_blank">LeetCode 226</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> root = [4,2,7,1,3,6,9]<br><b>Output:</b> [4,7,2,9,6,3,1]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Recursively swap the left and right children of every node.<br><br><b>Dependencies:</b> <code>std::swap</code></td>
      <td><b>Edge Cases:</b> <b>Empty Tree:</b> Returns null immediately.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def invertTree(root: TreeNode) -&gt; TreeNode:&#10;    if not root: return None&#10;    root.left, root.right = root.right, root.left&#10;    invertTree(root.left)&#10;    invertTree(root.right)&#10;    return root</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">6</td>
      <td rowspan="1">Tree 06 Diameter Of Binary Tree<br><br></b> <a href="https://leetcode.com/problems/diameter-of-binary-tree/" target="_blank">LeetCode 543</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> root = [1,2,3,4,5]<br><b>Output:</b> 3 (Path is [4,2,1,3] or [5,2,1,3])</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Modify the Height/Depth algorithm. Calculate `left_depth + right_depth` at every node to find max diameter, while returning standard height.<br><br><b>Dependencies:</b> <code>std::max</code></td>
      <td><b>Edge Cases:</b> <b>Path doesn't pass through root:</b> Handled correctly by tracking the global maximum `max_d` at every recursive step.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def diameterOfBinaryTree(root: TreeNode) -&gt; int:&#10;    max_d = [0]&#10;    def height(node):&#10;        if not node: return 0&#10;        left = height(node.left)&#10;        right = height(node.right)&#10;        max_d[0] = max(max_d[0], left + right)&#10;        return 1 + max(left, right)&#10;    height(root)&#10;    return max_d[0]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">7</td>
      <td rowspan="1">Tree 07 Balanced Binary Tree<br><br></b> <a href="https://leetcode.com/problems/balanced-binary-tree/" target="_blank">LeetCode 110</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> root = [3,9,20,null,null,15,7]<br><b>Output:</b> true</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Modify the Height algorithm. If the difference between `left` and `right` height is > 1, return `-1` to propagate the unbalanced signal.<br><br><b>Dependencies:</b> <code>std::abs</code></td>
      <td><b>Edge Cases:</b> <b>Early Exit:</b> Checking if `left == -1` or `right == -1` immediately breaks the recursion, optimizing time.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isBalanced(root: TreeNode) -&gt; bool:&#10;    def checkHeight(node):&#10;        if not node: return 0&#10;        left = checkHeight(node.left)&#10;        if left == -1: return -1&#10;        right = checkHeight(node.right)&#10;        if right == -1: return -1&#10;        if abs(left - right) &gt; 1: return -1&#10;        return 1 + max(left, right)&#10;    return checkHeight(root) != -1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">8</td>
      <td rowspan="1">Tree 08 Binary Search Tree Iterator<br><br></b> <a href="https://leetcode.com/problems/binary-search-tree-iterator/" target="_blank">LeetCode 173</a></td>
      <td rowspan="1"><b>Example 1:</b> next() returns smallest element.</td>
      <td><b>Time:</b> O(1) amortized<br><b>Space:</b> O(H)</td>
      <td>Use a stack to simulate in-order traversal. Push all left children initially. On next(), pop, return val, and push all left children of popped node's right child.<br><br><b>Dependencies:</b> <code>#include <stack></code></td>
      <td><b>Edge Cases:</b> <b>Empty Tree:</b> Stack is empty.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class BSTIterator:&#10;    def __init__(self, root: TreeNode):&#10;        self.st = []&#10;        self.pushAll(root)&#10;    def pushAll(self, node):&#10;        while node:&#10;            self.st.append(node)&#10;            node = node.left&#10;    def next(self) -&gt; int:&#10;        tmp = self.st.pop()&#10;        self.pushAll(tmp.right)&#10;        return tmp.val&#10;    def hasNext(self) -&gt; bool:&#10;        return len(self.st) &gt; 0</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">9</td>
      <td rowspan="1">Tree 09 Validate Binary Search Tree<br><br></b> <a href="https://leetcode.com/problems/validate-binary-search-tree/" target="_blank">LeetCode 98</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> root = [2,1,3]<br><b>Output:</b> true</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>Recursive validation with min and max bounds for every node. Long long is used to avoid overflow.<br><br><b>Dependencies:</b> <code>#include <limits.h></code></td>
      <td><b>Edge Cases:</b> <b>Values reach INT bounds:</b> Use LLONG_MIN/LLONG_MAX bounds.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isValidBST(root: TreeNode) -&gt; bool:&#10;    def validate(node, low=-float(&#x27;inf&#x27;), high=float(&#x27;inf&#x27;)):&#10;        if not node: return True&#10;        if node.val &lt;= low or node.val &gt;= high: return False&#10;        return validate(node.left, low, node.val) and validate(node.right, node.val, high)&#10;    return validate(root)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">10</td>
      <td rowspan="1">Tree 10 Construct Tree From Preorder And Inorder<br><br></b> <a href="https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/" target="_blank">LeetCode 105</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]<br><b>Output:</b> [3,9,20,null,null,15,7]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N) for Hash Map</td>
      <td>First element of preorder is the root. Find this element in inorder to split into left and right subtrees. Use a Hash Map to store inorder indices for O(1) lookups.<br><br><b>Dependencies:</b> <code>#include <unordered_map></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def buildTree(preorder: List[int], inorder: List[int]) -&gt; Optional[TreeNode]:&#10;    in_map = {val: i for i, val in enumerate(inorder)}&#10;    def build(pre_start, pre_end, in_start, in_end):&#10;        if pre_start &gt; pre_end or in_start &gt; in_end: return None&#10;        root = TreeNode(preorder[pre_start])&#10;        in_root = in_map[root.val]&#10;        nums_left = in_root - in_start&#10;        root.left = build(pre_start + 1, pre_start + nums_left, in_start, in_root - 1)&#10;        root.right = build(pre_start + nums_left + 1, pre_end, in_root + 1, in_end)&#10;        return root&#10;    return build(0, len(preorder) - 1, 0, len(inorder) - 1)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">11</td>
      <td rowspan="1">Tree 11 Maximum Path Sum<br><br></b> <a href="https://leetcode.com/problems/binary-tree-maximum-path-sum/" target="_blank">LeetCode 124</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> root = [-10,9,20,null,null,15,7]<br><b>Output:</b> 42</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>DFS returning max path sum down a single branch. At any node, max path = `node.val + max(0, leftPath) + max(0, rightPath)`. Ignore negative branches.<br><br><b>Dependencies:</b> <code>#include <limits.h></code></td>
      <td><b>Edge Cases:</b> <b>All Negative Nodes:</b> Initialization with `INT_MIN` properly returns the least negative node.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxPathSum(root: Optional[TreeNode]) -&gt; int:&#10;    maxi = [float(&#x27;-inf&#x27;)]&#10;    def maxPathDown(node):&#10;        if not node: return 0&#10;        left = max(0, maxPathDown(node.left))&#10;        right = max(0, maxPathDown(node.right))&#10;        maxi[0] = max(maxi[0], left + right + node.val)&#10;        return max(left, right) + node.val&#10;    maxPathDown(root)&#10;    return int(maxi[0])</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">12</td>
      <td rowspan="1">Tree 12 Boundary Traversal<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Return array of boundary nodes.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>1) Add root if not leaf. 2) Traverse left boundary (excluding leaves). 3) Inorder traverse all leaves. 4) Traverse right boundary, reverse it, then add to answer.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def printBoundaryView(root: TreeNode) -&gt; List[int]:&#10;    if not root: return []&#10;    res = []&#10;    def isLeaf(node): return not node.left and not node.right&#10;    if not isLeaf(root): res.append(root.val)&#10;    cur = root.left&#10;    while cur:&#10;        if not isLeaf(cur): res.append(cur.val)&#10;        cur = cur.left if cur.left else cur.right&#10;    def addLeaves(node):&#10;        if isLeaf(node): res.append(node.val); return&#10;        if node.left: addLeaves(node.left)&#10;        if node.right: addLeaves(node.right)&#10;    addLeaves(root)&#10;    cur = root.right; tmp = []&#10;    while cur:&#10;        if not isLeaf(cur): tmp.append(cur.val)&#10;        cur = cur.right if cur.right else cur.left&#10;    res.extend(tmp[::-1])&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">13</td>
      <td rowspan="1">Tree 13 Zigzag Traversal<br><br></b> <a href="https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/" target="_blank">LeetCode 103</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> root = [3,9,20,null,null,15,7]<br><b>Output:</b> [[3],[20,9],[15,7]]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Standard BFS Level Order Traversal with a boolean flag `leftToRight`. After finishing a level, if the flag is false, reverse the level array before adding to the result.<br><br><b>Dependencies:</b> <code>#include <queue></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def zigzagLevelOrder(root: Optional[TreeNode]) -&gt; List[List[int]]:&#10;    result = []&#10;    if not root: return result&#10;    q = collections.deque([root])&#10;    leftToRight = True&#10;    while q:&#10;        size = len(q)&#10;        row = [0] * size&#10;        for i in range(size):&#10;            node = q.popleft()&#10;            index = i if leftToRight else (size - 1 - i)&#10;            row[index] = node.val&#10;            if node.left: q.append(node.left)&#10;            if node.right: q.append(node.right)&#10;        leftToRight = not leftToRight&#10;        result.append(row)&#10;    return result</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">14</td>
      <td rowspan="1">Tree 14 Vertical Order Traversal<br><br></b> <a href="https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/" target="_blank">LeetCode 987</a></td>
      <td rowspan="1"><b>Example 1:</b><br><b>Output:</b> [[9],[3,15],[20],[7]]</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(N)</td>
      <td>Use a map structure: `map<int, map<int, multiset<int>>>` to store nodes mapped by their horizontal distance and level. BFS traversal ensures levels are processed top-down.<br><br><b>Dependencies:</b> <code>#include <map>\n#include <queue>\n#include <set></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def verticalTraversal(root: Optional[TreeNode]) -&gt; List[List[int]]:&#10;    nodes = collections.defaultdict(lambda: collections.defaultdict(list))&#10;    todo = collections.deque([(root, 0, 0)])&#10;    while todo:&#10;        node, x, y = todo.popleft()&#10;        nodes[x][y].append(node.val)&#10;        if node.left: todo.append((node.left, x - 1, y + 1))&#10;        if node.right: todo.append((node.right, x + 1, y + 1))&#10;    ans = []&#10;    for x in sorted(nodes.keys()):&#10;        col = []&#10;        for y in sorted(nodes[x].keys()):&#10;            col.extend(sorted(nodes[x][y]))&#10;        ans.append(col)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">15</td>
      <td rowspan="1">Tree 15 Top View<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Return list of values.</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(N)</td>
      <td>BFS traversal maintaining horizontal distance (HD) from root. Use a map `hd -> value`. Only insert into the map if the HD is not already present, ensuring the top-most node is recorded.<br><br><b>Dependencies:</b> <code>#include <map>\n#include <queue></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def topView(root: Optional[Node]) -&gt; List[int]:&#10;    ans = []&#10;    if not root: return ans&#10;    mpp = {}&#10;    q = collections.deque([(root, 0)])&#10;    while q:&#10;        node, line = q.popleft()&#10;        if line not in mpp: mpp[line] = node.data&#10;        if node.left: q.append((node.left, line - 1))&#10;        if node.right: q.append((node.right, line + 1))&#10;    for line in sorted(mpp.keys()): ans.append(mpp[line])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">16</td>
      <td rowspan="1">Tree 16 Bottom View<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Return list of values.</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(N)</td>
      <td>BFS traversal maintaining horizontal distance (HD). Map `hd -> value`. Always update the map value for a given HD so that the last node encountered (bottom-most) overrides previous ones.<br><br><b>Dependencies:</b> <code>#include <map>\n#include <queue></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def bottomView(root: Optional[Node]) -&gt; List[int]:&#10;    ans = []&#10;    if not root: return ans&#10;    mpp = {}&#10;    q = collections.deque([(root, 0)])&#10;    while q:&#10;        node, line = q.popleft()&#10;        mpp[line] = node.data&#10;        if node.left: q.append((node.left, line - 1))&#10;        if node.right: q.append((node.right, line + 1))&#10;    for line in sorted(mpp.keys()): ans.append(mpp[line])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">17</td>
      <td rowspan="1">Tree 17 Right View<br><br></b> <a href="https://leetcode.com/problems/binary-tree-right-side-view/" target="_blank">LeetCode 199</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> root = [1,2,3,null,5,null,4]<br><b>Output:</b> [1,3,4]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>DFS Traversing right child before left child. Maintain the current level. If `level == result.size()`, append the node value to the result list.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def rightSideView(root: Optional[TreeNode]) -&gt; List[int]:&#10;    res = []&#10;    def recursion(node, level):&#10;        if not node: return&#10;        if len(res) == level: res.append(node.val)&#10;        recursion(node.right, level + 1)&#10;        recursion(node.left, level + 1)&#10;    recursion(root, 0)&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">18</td>
      <td rowspan="1">Tree 18 Left View<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/left-view-of-binary-tree/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Print left-most node at each level.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>DFS Traversing left child before right child. Maintain the current level. If `level == result.size()`, append the node value to the result list.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def leftView(root: Optional[Node]) -&gt; List[int]:&#10;    res = []&#10;    def recursion(node, level):&#10;        if not node: return&#10;        if len(res) == level: res.append(node.data)&#10;        recursion(node.left, level + 1)&#10;        recursion(node.right, level + 1)&#10;    recursion(root, 0)&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">19</td>
      <td rowspan="1">Tree 19 Construct Tree From Inorder And Postorder<br><br></b> <a href="https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/" target="_blank">LeetCode 106</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]<br><b>Output:</b> [3,9,20,null,null,15,7]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Store inorder indices in a HashMap. The last element in postorder is the root. Find this root in inorder map to determine left subtree size. Recursively build left and right subtrees by slicing array indices.<br><br><b>Dependencies:</b> <code>#include <unordered_map></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def buildTree(inorder: List[int], postorder: List[int]) -&gt; Optional[TreeNode]:&#10;    inMap = {val: i for i, val in enumerate(inorder)}&#10;    def build(inStart, inEnd, postStart, postEnd):&#10;        if inStart &gt; inEnd or postStart &gt; postEnd: return None&#10;        root = TreeNode(postorder[postEnd])&#10;        inRoot = inMap[root.val]&#10;        numsLeft = inRoot - inStart&#10;        root.left = build(inStart, inRoot - 1, postStart, postStart + numsLeft - 1)&#10;        root.right = build(inRoot + 1, inEnd, postStart + numsLeft, postEnd - 1)&#10;        return root&#10;    return build(0, len(inorder) - 1, 0, len(postorder) - 1)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">20</td>
      <td rowspan="1">Tree 20 Serialize And Deserialize Binary Tree<br><br></b> <a href="https://leetcode.com/problems/serialize-and-deserialize-binary-tree/" target="_blank">LeetCode 297</a></td>
      <td rowspan="1"><b>Example 1:</b> Serialization/Deserialization.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Use Level Order Traversal (BFS) using a queue. For serialization, append '#' for null nodes. For deserialization, split string by comma and use a queue to reconstruct the tree structure level by level.<br><br><b>Dependencies:</b> <code>#include <queue>\n#include <sstream></code></td>
      <td><b>Edge Cases:</b> <b>Empty Tree:</b> Serialized string is empty. Deserialize returns null.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;class Codec:&#10;    def serialize(self, root):&#10;        if not root: return &quot;&quot;&#10;        s = []; q = collections.deque([root])&#10;        while q:&#10;            node = q.popleft()&#10;            if node is None: s.append(&quot;#&quot;)&#10;            else: s.append(str(node.val)); q.append(node.left); q.append(node.right)&#10;        return &quot;,&quot;.join(s)&#10;    def deserialize(self, data):&#10;        if not data: return None&#10;        values = data.split(&quot;,&quot;)&#10;        root = TreeNode(int(values[0]))&#10;        q = collections.deque([root])&#10;        i = 1&#10;        while q:&#10;            node = q.popleft()&#10;            if values[i] != &quot;#&quot;: node.left = TreeNode(int(values[i])); q.append(node.left)&#10;            i += 1&#10;            if values[i] != &quot;#&quot;: node.right = TreeNode(int(values[i])); q.append(node.right)&#10;            i += 1&#10;        return root</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">21</td>
      <td rowspan="1">Tree 21 Flatten Binary Tree To Linked List<br><br></b> <a href="https://leetcode.com/problems/flatten-binary-tree-to-linked-list/" target="_blank">LeetCode 114</a></td>
      <td rowspan="1"><b>Example 1:</b> In-place flatten.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Morris Traversal. If node has a left child, find the rightmost node of the left subtree. Point its right to current node's right. Move current node's left to its right, and set left to null. Move to current's right.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def flatten(root: Optional[TreeNode]) -&gt; None:&#10;    curr = root&#10;    while curr:&#10;        if curr.left:&#10;            pre = curr.left&#10;            while pre.right: pre = pre.right&#10;            pre.right = curr.right&#10;            curr.right = curr.left&#10;            curr.left = None&#10;        curr = curr.right</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">22</td>
      <td rowspan="1">Tree 22 Kth Smallest Element In A BST<br><br></b> <a href="https://leetcode.com/problems/kth-smallest-element-in-a-bst/" target="_blank">LeetCode 230</a></td>
      <td rowspan="1"><b>Example 1:</b> Inorder traversal.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1) using Morris Traversal</td>
      <td>Inorder traversal of BST gives sorted elements. Keep a counter, when it reaches K, store the result. Morris Traversal can do this in O(1) space.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def kthSmallest(root: Optional[TreeNode], k: int) -&gt; int:&#10;    count, ans = 0, -1&#10;    curr = root&#10;    while curr:&#10;        if curr.left is None:&#10;            count += 1&#10;            if count == k: ans = curr.val&#10;            curr = curr.right&#10;        else:&#10;            pre = curr.left&#10;            while pre.right and pre.right != curr: pre = pre.right&#10;            if pre.right is None:&#10;                pre.right = curr&#10;                curr = curr.left&#10;            else:&#10;                pre.right = None&#10;                count += 1&#10;                if count == k: ans = curr.val&#10;                curr = curr.right&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">23</td>
      <td rowspan="1">Tree 23 Lowest Common Ancestor Of A Binary Search Tree<br><br></b> <a href="https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/" target="_blank">LeetCode 235</a></td>
      <td rowspan="1"><b>Example 1:</b> Exploit BST property.</td>
      <td><b>Time:</b> O(H)<br><b>Space:</b> O(1)</td>
      <td>If both `p` and `q` are less than root, LCA is in the left subtree. If both are greater, LCA is in the right subtree. Otherwise, the current node is the LCA.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def lowestCommonAncestor(root: &#x27;TreeNode&#x27;, p: &#x27;TreeNode&#x27;, q: &#x27;TreeNode&#x27;) -&gt; &#x27;TreeNode&#x27;:&#10;    while root:&#10;        if root.val &gt; p.val and root.val &gt; q.val: root = root.left&#10;        elif root.val &lt; p.val and root.val &lt; q.val: root = root.right&#10;        else: return root&#10;    return None</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">24</td>
      <td rowspan="1">Tree 24 Insert Into A Binary Search Tree<br><br></b> <a href="https://leetcode.com/problems/insert-into-a-binary-search-tree/" target="_blank">LeetCode 701</a></td>
      <td rowspan="1"><b>Example 1:</b> Traverse and insert.</td>
      <td><b>Time:</b> O(H)<br><b>Space:</b> O(1)</td>
      <td>Traverse left or right depending on the value. Keep track of parent. Insert as left or right child of parent when a null pointer is reached.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def insertIntoBST(root: Optional[TreeNode], val: int) -&gt; Optional[TreeNode]:&#10;    if not root: return TreeNode(val)&#10;    curr = root&#10;    while True:&#10;        if val &lt; curr.val:&#10;            if curr.left: curr = curr.left&#10;            else: curr.left = TreeNode(val); break&#10;        else:&#10;            if curr.right: curr = curr.right&#10;            else: curr.right = TreeNode(val); break&#10;    return root</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">25</td>
      <td rowspan="1">Tree 25 Delete Node In A BST<br><br></b> <a href="https://leetcode.com/problems/delete-node-in-a-bst/" target="_blank">LeetCode 450</a></td>
      <td rowspan="1"><b>Example 1:</b> Locate and delete.</td>
      <td><b>Time:</b> O(H)<br><b>Space:</b> O(H) or O(1)</td>
      <td>Find the node. If it has no left child, return right child. If no right, return left. If both exist, find the right child of the rightmost node in the left subtree, and point it to the node's right child. Return the node's left child.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def deleteNode(root: Optional[TreeNode], key: int) -&gt; Optional[TreeNode]:&#10;    def helper(node):&#10;        if not node.left: return node.right&#10;        if not node.right: return node.left&#10;        rightChild = node.right&#10;        lastRight = node.left&#10;        while lastRight.right: lastRight = lastRight.right&#10;        lastRight.right = rightChild&#10;        return node.left&#10;    if not root: return None&#10;    if root.val == key: return helper(root)&#10;    curr = root&#10;    while curr:&#10;        if curr.val &gt; key:&#10;            if curr.left and curr.left.val == key:&#10;                curr.left = helper(curr.left)&#10;                break&#10;            else: curr = curr.left&#10;        else:&#10;            if curr.right and curr.right.val == key:&#10;                curr.right = helper(curr.right)&#10;                break&#10;            else: curr = curr.right&#10;    return root</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">26</td>
      <td rowspan="1">Tree 26 Inorder Successor In BST<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/inorder-successor-in-bst/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Find next greater.</td>
      <td><b>Time:</b> O(H)<br><b>Space:</b> O(1)</td>
      <td>Traverse BST. If `curr.val > node.val`, then `curr` is a potential successor, store it and move left to find smaller. Else, move right.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def inOrderSuccessor(root, x):&#10;    successor = None&#10;    while root:&#10;        if root.val &lt;= x.val:&#10;            root = root.right&#10;        else:&#10;            successor = root&#10;            root = root.left&#10;    return successor</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">27</td>
      <td rowspan="1">Tree 27 Two Sum IV Input Is A BST<br><br></b> <a href="https://leetcode.com/problems/two-sum-iv-input-is-a-bst/" target="_blank">LeetCode 653</a></td>
      <td rowspan="1"><b>Example 1:</b> BST Iterator two pointer.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>Use two BST iterators: one for normal inorder (next) and one for reverse inorder (before). Apply two-pointer approach like in a sorted array.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class BSTIterator:&#10;    def __init__(self, root, isReverse):&#10;        self.st = []&#10;        self.reverse = isReverse&#10;        self.pushAll(root)&#10;    def pushAll(self, node):&#10;        while node:&#10;            self.st.append(node)&#10;            if self.reverse: node = node.right&#10;            else: node = node.left&#10;    def next(self) -&gt; int:&#10;        tmpNode = self.st.pop()&#10;        if self.reverse: self.pushAll(tmpNode.left)&#10;        else: self.pushAll(tmpNode.right)&#10;        return tmpNode.val&#10;def findTarget(root: Optional[TreeNode], k: int) -&gt; bool:&#10;    if not root: return False&#10;    l = BSTIterator(root, False)&#10;    r = BSTIterator(root, True)&#10;    i = l.next()&#10;    j = r.next()&#10;    while i &lt; j:&#10;        if i + j == k: return True&#10;        elif i + j &lt; k: i = l.next()&#10;        else: j = r.next()&#10;    return False</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">28</td>
      <td rowspan="1">Tree 28 Recover Binary Search Tree<br><br></b> <a href="https://leetcode.com/problems/recover-binary-search-tree/" target="_blank">LeetCode 99</a></td>
      <td rowspan="1"><b>Example 1:</b> Inorder traversal tracking anomalies.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>Inorder traversal of BST gives sorted array. If two are swapped, there will be 1 or 2 anomalies where `prev->val > curr->val`. First anomaly: `first = prev`, `middle = curr`. Second anomaly: `last = curr`. Swap `first` and `last` (or `first` and `middle` if adjacent).</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def recoverTree(root: Optional[TreeNode]) -&gt; None:&#10;    first = middle = last = prev = None&#10;    def inorder(node):&#10;        nonlocal first, middle, last, prev&#10;        if not node: return&#10;        inorder(node.left)&#10;        if prev and node.val &lt; prev.val:&#10;            if not first:&#10;                first = prev&#10;                middle = node&#10;            else:&#10;                last = node&#10;        prev = node&#10;        inorder(node.right)&#10;    inorder(root)&#10;    if first and last:&#10;        first.val, last.val = last.val, first.val&#10;    elif first and middle:&#10;        first.val, middle.val = middle.val, first.val</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">29</td>
      <td rowspan="1">Tree 29 Largest BST In Binary Tree<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/largest-bst/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Bottom-up verification.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>Return `[minNode, maxNode, maxSize]` from each subtree. For current node, if `left.max < node.val < right.min`, it's a BST. Return `[min(node.val, left.min), max(node.val, right.max), left.size + right.size + 1]`. Else, it's not a BST, return `[-inf, inf, max(left.size, right.size)]`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class NodeValue:&#10;    def __init__(self, minNode, maxNode, maxSize):&#10;        self.minNode = minNode&#10;        self.maxNode = maxNode&#10;        self.maxSize = maxSize&#10;def largestBSTSubtreeHelper(root):&#10;    if not root: return NodeValue(float(&#x27;inf&#x27;), float(&#x27;-inf&#x27;), 0)&#10;    left = largestBSTSubtreeHelper(root.left)&#10;    right = largestBSTSubtreeHelper(root.right)&#10;    if left.maxNode &lt; root.data &lt; right.minNode:&#10;        return NodeValue(min(root.data, left.minNode), max(root.data, right.maxNode), left.maxSize + right.maxSize + 1)&#10;    return NodeValue(float(&#x27;-inf&#x27;), float(&#x27;inf&#x27;), max(left.maxSize, right.maxSize))&#10;def largestBst(root):&#10;    return largestBSTSubtreeHelper(root).maxSize</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">30</td>
      <td rowspan="1">Tree 30 Maximum Sum BST In Binary Tree<br><br></b> <a href="https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/" target="_blank">LeetCode 1373</a></td>
      <td rowspan="1"><b>Example 1:</b> Similar to largest BST.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>Bottom-up traversal. Return `[isBST, minNode, maxNode, sum]`. Update global max sum when valid BST is found.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class Info:&#10;    def __init__(self, isBST, minNode, maxNode, sum_val):&#10;        self.isBST = isBST&#10;        self.minNode = minNode&#10;        self.maxNode = maxNode&#10;        self.sum = sum_val&#10;def maxSumBST(root: Optional[TreeNode]) -&gt; int:&#10;    maxSum = 0&#10;    def solve(node):&#10;        nonlocal maxSum&#10;        if not node: return Info(True, float(&#x27;inf&#x27;), float(&#x27;-inf&#x27;), 0)&#10;        left = solve(node.left)&#10;        right = solve(node.right)&#10;        if left.isBST and right.isBST and left.maxNode &lt; node.val &lt; right.minNode:&#10;            currSum = left.sum + right.sum + node.val&#10;            maxSum = max(maxSum, currSum)&#10;            return Info(True, min(node.val, left.minNode), max(node.val, right.maxNode), currSum)&#10;        return Info(False, float(&#x27;-inf&#x27;), float(&#x27;inf&#x27;), max(left.sum, right.sum))&#10;    solve(root)&#10;    return maxSum if maxSum &gt; 0 else 0</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">31</td>
      <td rowspan="1">Tree 31 Kth Largest Element In A BST<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/kth-largest-element-in-bst/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Reverse inorder traversal.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>Kth largest is Kth element in reverse inorder traversal (Right, Root, Left). Maintain a counter `k`. When visiting a node, decrement `k`. If `k == 0`, current node is the answer.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def kthLargest(root, k):&#10;    ans = -1&#10;    def reverseInorder(node):&#10;        nonlocal ans, k&#10;        if not node or k == 0: return&#10;        reverseInorder(node.right)&#10;        k -= 1&#10;        if k == 0:&#10;            ans = node.data&#10;            return&#10;        reverseInorder(node.left)&#10;    reverseInorder(root)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">32</td>
      <td rowspan="1">Tree 32 Predecessor And Successor In BST<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/predecessor-and-successor/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Search down the tree.</td>
      <td><b>Time:</b> O(H)<br><b>Space:</b> O(1)</td>
      <td>For Successor: search for key. If node->val <= key, go right. If node->val > key, update succ = node, go left. For Predecessor: If node->val >= key, go left. If node->val < key, update pred = node, go right.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findPreSuc(root, pre, suc, key):&#10;    curr = root&#10;    while curr:&#10;        if curr.key &gt; key:&#10;            suc[0] = curr&#10;            curr = curr.left&#10;        else:&#10;            curr = curr.right&#10;    curr = root&#10;    while curr:&#10;        if curr.key &lt; key:&#10;            pre[0] = curr&#10;            curr = curr.right&#10;        else:&#10;            curr = curr.left</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">33</td>
      <td rowspan="1">Tree 33 Construct BST From Preorder Traversal<br><br></b> <a href="https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/" target="_blank">LeetCode 1008</a></td>
      <td rowspan="1"><b>Example 1:</b> Upper bound tracking.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>Use an upper bound value. `build(preorder, index, bound)`: If index >= len or preorder[index] > bound, return NULL. Create root with preorder[index]. `root->left = build(..., root->val)`. `root->right = build(..., bound)`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def bstFromPreorder(preorder: List[int]) -&gt; Optional[TreeNode]:&#10;    i = 0&#10;    def build(bound):&#10;        nonlocal i&#10;        if i == len(preorder) or preorder[i] &gt; bound: return None&#10;        root = TreeNode(preorder[i])&#10;        i += 1&#10;        root.left = build(root.val)&#10;        root.right = build(bound)&#10;        return root&#10;    return build(float(&#x27;inf&#x27;))</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">34</td>
      <td rowspan="1">Tree 34 All Nodes Distance K In Binary Tree<br><br></b> <a href="https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/" target="_blank">LeetCode 863</a></td>
      <td rowspan="1"><b>Example 1:</b> Convert to graph or use parent pointers.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Perform BFS/DFS to map each node to its parent. Then, start a BFS from the target node, visiting left, right, and parent. Track visited nodes. After `k` levels in BFS, the current queue holds the answer.<br><br><b>Dependencies:</b> <code>#include <unordered_map>\n#include <queue>\n#include <unordered_set></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def distanceK(root: TreeNode, target: TreeNode, k: int) -&gt; List[int]:&#10;    parent_track = {}&#10;    def markParents(node):&#10;        if node.left:&#10;            parent_track[node.left] = node&#10;            markParents(node.left)&#10;        if node.right:&#10;            parent_track[node.right] = node&#10;            markParents(node.right)&#10;    markParents(root)&#10;    queue = collections.deque([target])&#10;    visited = {target}&#10;    curr_level = 0&#10;    while queue:&#10;        if curr_level == k: break&#10;        size = len(queue)&#10;        for _ in range(size):&#10;            current = queue.popleft()&#10;            if current.left and current.left not in visited:&#10;                queue.append(current.left)&#10;                visited.add(current.left)&#10;            if current.right and current.right not in visited:&#10;                queue.append(current.right)&#10;                visited.add(current.right)&#10;            if current in parent_track and parent_track[current] not in visited:&#10;                queue.append(parent_track[current])&#10;                visited.add(parent_track[current])&#10;        curr_level += 1&#10;    return [node.val for node in queue]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">35</td>
      <td rowspan="1">Tree 35 Amount Of Time For Binary Tree To Be Infected<br><br></b> <a href="https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/" target="_blank">LeetCode 2385</a></td>
      <td rowspan="1"><b>Example 1:</b> Parent pointers and BFS.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Same as 'Distance K' problem. Map parents. Find the start node. Perform BFS from start node. The time taken is the number of levels in BFS until all reachable nodes are visited.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def amountOfTime(root: Optional[TreeNode], start: int) -&gt; int:&#10;    parent_track = {}&#10;    target = None&#10;    queue = collections.deque([root])&#10;    while queue:&#10;        node = queue.popleft()&#10;        if node.val == start: target = node&#10;        if node.left:&#10;            parent_track[node.left] = node&#10;            queue.append(node.left)&#10;        if node.right:&#10;            parent_track[node.right] = node&#10;            queue.append(node.right)&#10;    queue = collections.deque([target])&#10;    visited = {target}&#10;    time = 0&#10;    while queue:&#10;        fl = False&#10;        for _ in range(len(queue)):&#10;            current = queue.popleft()&#10;            if current.left and current.left not in visited:&#10;                visited.add(current.left)&#10;                queue.append(current.left)&#10;                fl = True&#10;            if current.right and current.right not in visited:&#10;                visited.add(current.right)&#10;                queue.append(current.right)&#10;                fl = True&#10;            if current in parent_track and parent_track[current] not in visited:&#10;                visited.add(parent_track[current])&#10;                queue.append(parent_track[current])&#10;                fl = True&#10;        if fl: time += 1&#10;    return time</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">36</td>
      <td rowspan="1">Tree 36 Count Complete Tree Nodes<br><br></b> <a href="https://leetcode.com/problems/count-complete-tree-nodes/" target="_blank">LeetCode 222</a></td>
      <td rowspan="1"><b>Example 1:</b> Recursive with Height check.</td>
      <td><b>Time:</b> O(log^2 N)<br><b>Space:</b> O(log N)</td>
      <td>Compute the left height (following left child) and right height (following right child) of the tree. If they are equal, the tree is a full binary tree, and the number of nodes is `2^h - 1`. If they are not equal, recursively count the nodes in the left and right subtrees and add 1 for the root.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def countNodes(root: Optional[TreeNode]) -&gt; int:&#10;    if not root: return 0&#10;    def get_height(node, is_left):&#10;        h = 0&#10;        while node:&#10;            h += 1&#10;            node = node.left if is_left else node.right&#10;        return h&#10;    lh = get_height(root, True)&#10;    rh = get_height(root, False)&#10;    if lh == rh:&#10;        return (1 &lt;&lt; lh) - 1&#10;    return 1 + countNodes(root.left) + countNodes(root.right)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">37</td>
      <td rowspan="1">Tree 37 Morris Preorder Traversal<br><br></b> <a href="https://leetcode.com/problems/binary-tree-preorder-traversal/" target="_blank">LeetCode 144</a></td>
      <td rowspan="1"><b>Example 1:</b> Threaded Binary Tree.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Similar to Morris Inorder. If left child is null, process current, move right. Else, find predecessor. If predecessor's right is null, process current, make thread, move left. If predecessor's right is current, remove thread, move right.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def preorderTraversal(root: Optional[TreeNode]) -&gt; List[int]:&#10;    preorder = []&#10;    curr = root&#10;    while curr:&#10;        if not curr.left:&#10;            preorder.append(curr.val)&#10;            curr = curr.right&#10;        else:&#10;            prev = curr.left&#10;            while prev.right and prev.right != curr:&#10;                prev = prev.right&#10;            if not prev.right:&#10;                prev.right = curr&#10;                preorder.append(curr.val)&#10;                curr = curr.left&#10;            else:&#10;                prev.right = None&#10;                curr = curr.right&#10;    return preorder</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">38</td>
      <td rowspan="1">Tree 38 Search In A Binary Search Tree<br><br></b> <a href="https://leetcode.com/problems/search-in-a-binary-search-tree/" target="_blank">LeetCode 700</a></td>
      <td rowspan="1"><b>Example 1:</b> Iterative or Recursive.</td>
      <td><b>Time:</b> O(H)<br><b>Space:</b> O(1)</td>
      <td>Start at root. If root is null or its value is `val`, return root. If `val < root.val`, go left. Else go right.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def searchBST(root: Optional[TreeNode], val: int) -&gt; Optional[TreeNode]:&#10;    while root and root.val != val:&#10;        root = root.left if val &lt; root.val else root.right&#10;    return root</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">39</td>
      <td rowspan="1">Tree 39 Find Minimum In Binary Search Tree<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/minimum-element-in-bst/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Leftmost node.</td>
      <td><b>Time:</b> O(H)<br><b>Space:</b> O(1)</td>
      <td>Traverse the left children until a node with no left child is reached. That node contains the minimum value.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minValue(root: Optional[TreeNode]) -&gt; int:&#10;    if not root: return -1&#10;    while root.left:&#10;        root = root.left&#10;    return root.val</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">40</td>
      <td rowspan="1">Tree 40 Inorder Successor In BST<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/populate-inorder-successor-for-all-nodes/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Iterative search.</td>
      <td><b>Time:</b> O(H)<br><b>Space:</b> O(1)</td>
      <td>Start from root. If `p.val >= root.val`, the successor must be in the right subtree (`root = root.right`). If `p.val < root.val`, the current root could be the successor, so record it and search the left subtree for a closer successor (`successor = root; root = root.left`).</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def inorderSuccessor(root: &#x27;TreeNode&#x27;, p: &#x27;TreeNode&#x27;) -&gt; &#x27;TreeNode&#x27;:&#10;    successor = None&#10;    while root:&#10;        if p.val &gt;= root.val:&#10;            root = root.right&#10;        else:&#10;            successor = root&#10;            root = root.left&#10;    return successor</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">41</td>
      <td rowspan="1">Tree 41 Construct Binary Tree From String With Bracket Representation<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/construct-binary-tree-from-string-with-bracket-representation/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Stack approach.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>Iterate through string. If digit or sign, parse number and create node. If '(', continue. If node created, push to stack. If ')', pop from stack. If it has a parent, attach it (left first, then right).<br><br><b>Dependencies:</b> <code>#include <stack></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def treeFromString(s: str):&#10;    if not s: return None&#10;    stack = []&#10;    i = 0&#10;    while i &lt; len(s):&#10;        if s[i] == &#x27;)&#x27;:&#10;            stack.pop()&#10;            i += 1&#10;        elif s[i] == &#x27;(&#x27;:&#10;            i += 1&#10;        else:&#10;            j = i&#10;            while j &lt; len(s) and (s[j].isdigit() or s[j] == &#x27;-&#x27;): j += 1&#10;            node = TreeNode(int(s[i:j]))&#10;            if stack:&#10;                parent = stack[-1]&#10;                if not parent.left: parent.left = node&#10;                else: parent.right = node&#10;            stack.append(node)&#10;            i = j&#10;    return stack[0]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">42</td>
      <td rowspan="1">Tree 42 Transform To Sum Tree<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/transform-to-sum-tree/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Postorder Traversal.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>Recursively get the sum of the left subtree and right subtree. Update current node's value to the sum of left and right. Return the old value of current node + sum of left + sum of right to the caller.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def toSumTree(root):&#10;    def helper(node):&#10;        if not node: return 0&#10;        leftSum = helper(node.left)&#10;        rightSum = helper(node.right)&#10;        oldVal = node.val&#10;        node.val = leftSum + rightSum&#10;        return node.val + oldVal&#10;    helper(root)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">43</td>
      <td rowspan="1">Tree 43 Diagonal Traversal Of Binary Tree<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/diagonal-traversal-of-binary-tree/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Queue based.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Use a queue. Push root. Then loop: Pop a node `curr`. While `curr` is not null, add its value to result, push `curr->left` to queue, and move to `curr->right`.<br><br><b>Dependencies:</b> Queue</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def diagonal(root: Optional[TreeNode]) -&gt; List[int]:&#10;    res = []&#10;    if not root: return res&#10;    q = collections.deque([root])&#10;    while q:&#10;        curr = q.popleft()&#10;        while curr:&#10;            res.append(curr.val)&#10;            if curr.left: q.append(curr.left)&#10;            curr = curr.right&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">44</td>
      <td rowspan="1">Tree 44 Convert Binary Tree Into Doubly Linked List<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/binary-tree-to-dll/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> DFS Inorder, maintaining a `prev` pointer.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>Perform Inorder traversal. Maintain a `prev` pointer (initially null). At each node: if `prev == null`, this node is the head of DLL. Else, `prev->right = node` and `node->left = prev`. Update `prev = node`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def bToDLL(root: Optional[TreeNode]) -&gt; Optional[TreeNode]:&#10;    head = prev = None&#10;    def inorder(node):&#10;        nonlocal head, prev&#10;        if not node: return&#10;        inorder(node.left)&#10;        if prev is None:&#10;            head = node&#10;        else:&#10;            node.left = prev&#10;            prev.right = node&#10;        prev = node&#10;        inorder(node.right)&#10;    inorder(root)&#10;    return head</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">45</td>
      <td rowspan="1">Tree 45 Check If Tree Is Isomorphic<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/check-if-tree-is-isomorphic/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Check swapped and unswapped subtrees.</td>
      <td><b>Time:</b> O(min(M, N))<br><b>Space:</b> O(min(H1, H2))</td>
      <td>Two trees are isomorphic if one can be obtained from another by a series of flips. If roots are null, return true. If values don't match, false. Then check `(isIsomorphic(n1.left, n2.left) && isIsomorphic(n1.right, n2.right))` OR `(isIsomorphic(n1.left, n2.right) && isIsomorphic(n1.right, n2.left))`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isIsomorphic(n1: Optional[TreeNode], n2: Optional[TreeNode]) -&gt; bool:&#10;    if not n1 and not n2: return True&#10;    if not n1 or not n2: return False&#10;    if n1.val != n2.val: return False&#10;    no_swap = isIsomorphic(n1.left, n2.left) and isIsomorphic(n1.right, n2.right)&#10;    swap = isIsomorphic(n1.left, n2.right) and isIsomorphic(n1.right, n2.left)&#10;    return no_swap or swap</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">46</td>
      <td rowspan="1">Tree 46 Min Distance Between Two Given Nodes Of A Binary Tree<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/min-distance-between-two-given-nodes-of-a-binary-tree/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Find LCA, then distance from LCA to nodes.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>1. Find LCA of the two nodes. 2. Find distance from LCA to node 1. 3. Find distance from LCA to node 2. 4. Return the sum.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findDist(root: Optional[TreeNode], a: int, b: int) -&gt; int:&#10;    def lca(node):&#10;        if not node or node.val == a or node.val == b: return node&#10;        left = lca(node.left)&#10;        right = lca(node.right)&#10;        if not left: return right&#10;        if not right: return left&#10;        return node&#10;    &#10;    def getDist(node, val, dist):&#10;        if not node: return -1&#10;        if node.val == val: return dist&#10;        d = getDist(node.left, val, dist + 1)&#10;        if d != -1: return d&#10;        return getDist(node.right, val, dist + 1)&#10;        &#10;    lca_node = lca(root)&#10;    return getDist(lca_node, a, 0) + getDist(lca_node, b, 0)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">47</td>
      <td rowspan="1">Tree 47 Binary Tree To Cdll<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/binary-tree-to-cdll/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Inorder traversal.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>Perform an inorder traversal. Maintain a `prev` pointer. If `prev` is NULL, it's the `head`. Else, set `prev->right = curr` and `curr->left = prev`. Update `prev = curr`. Finally, connect `head` and `prev` (the tail).</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def bTreeToCList(root):&#10;    head = [None]&#10;    prev = [None]&#10;    def inorder(node):&#10;        if not node: return&#10;        inorder(node.left)&#10;        if not head[0]: head[0] = node&#10;        else:&#10;            prev[0].right = node&#10;            node.left = prev[0]&#10;        prev[0] = node&#10;        inorder(node.right)&#10;    inorder(root)&#10;    if head[0] and prev[0]:&#10;        head[0].left = prev[0]&#10;        prev[0].right = head[0]&#10;    return head[0]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">48</td>
      <td rowspan="1">Tree 48 Construct Tree From Inorder And Preorder<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/construct-tree-1/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Hash map for fast search.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>The first element in preorder is the root. Find this root in inorder using a hash map. Elements to the left in inorder form the left subtree, elements to the right form the right subtree. Recurse.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class Node:&#10;    def __init__(self,val): self.data = val; self.left = None; self.right = None&#10;def buildTree(In, pre, n):&#10;    mp = {val: idx for idx, val in enumerate(In)}&#10;    preIdx = [0]&#10;    def buildTreeUtil(inSt, inEnd):&#10;        if inSt &gt; inEnd: return None&#10;        curr = pre[preIdx[0]]&#10;        preIdx[0] += 1&#10;        node = Node(curr)&#10;        if inSt == inEnd: return node&#10;        inIdx = mp[curr]&#10;        node.left = buildTreeUtil(inSt, inIdx - 1)&#10;        node.right = buildTreeUtil(inIdx + 1, inEnd)&#10;        return node&#10;    return buildTreeUtil(0, n - 1)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">49</td>
      <td rowspan="1">Tree 49 Minimum Swap Required To Convert Binary Tree To Binary Search Tree<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/minimum-swap-required-to-convert-binary-tree-to-binary-search-tree/0" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Graph cycle detection on Inorder.</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(N)</td>
      <td>The inorder traversal of a BST is sorted. First, get the inorder traversal of the given complete binary tree using array indices. Then, the problem reduces to finding the minimum swaps to sort an array. Use graph cycles to find min swaps.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minSwaps(A, n):&#10;    v = []&#10;    def inorder(index):&#10;        if index &gt;= n: return&#10;        inorder(2 * index + 1)&#10;        v.append(A[index])&#10;        inorder(2 * index + 2)&#10;    inorder(0)&#10;    t = [(val, idx) for idx, val in enumerate(v)]&#10;    t.sort()&#10;    ans = 0&#10;    vis = {i: False for i in range(n)}&#10;    for i in range(n):&#10;        if vis[i] or t[i][1] == i: continue&#10;        cycle_size, j = 0, i&#10;        while not vis[j]:&#10;            vis[j] = True&#10;            j = t[j][1]&#10;            cycle_size += 1&#10;        if cycle_size &gt; 0: ans += (cycle_size - 1)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">50</td>
      <td rowspan="1">Tree 50 Check If Binary Tree Is Sum Tree Or Not<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/sum-tree/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Recursive check.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>Use a recursive function. A leaf node is always a SumTree. For an internal node, calculate the sum of its left and right subtrees. If its value equals the sum, and both subtrees are SumTrees, return true.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isSumTree(root):&#10;    def isSumTreeFast(node):&#10;        if not node: return True, 0&#10;        if not node.left and not node.right: return True, node.data&#10;        left_is, left_sum = isSumTreeFast(node.left)&#10;        right_is, right_sum = isSumTreeFast(node.right)&#10;        is_sum = node.data == (left_sum + right_sum)&#10;        if left_is and right_is and is_sum:&#10;            return True, 2 * node.data&#10;        else:&#10;            return False, 0&#10;    return isSumTreeFast(root)[0]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">51</td>
      <td rowspan="1">Tree 51 Check If All Leaf Nodes Are At Same Level Or Not<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/leaf-at-same-level/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Recursive check with global variable.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>Traverse the tree, maintaining the current level. The first time a leaf is encountered, store its level. For subsequent leaves, compare their level with the stored level. If any mismatch occurs, return false.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def check(root):&#10;    leafLevel = [0]&#10;    def checkUtil(node, level):&#10;        if not node: return True&#10;        if not node.left and not node.right:&#10;            if leafLevel[0] == 0:&#10;                leafLevel[0] = level&#10;                return True&#10;            return level == leafLevel[0]&#10;        return checkUtil(node.left, level + 1) and checkUtil(node.right, level + 1)&#10;    return checkUtil(root, 1)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">52</td>
      <td rowspan="1">Tree 52 Check If A Binary Tree Contains Duplicate Subtrees Of Size 2 Or More<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/duplicate-subtree-in-binary-tree/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> String serialization.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N)</td>
      <td>Serialize each subtree into a string. Use a hash map to store the frequencies of the serialized strings. If any string (of length > 3 to ignore leaves) has a frequency > 1, a duplicate subtree exists.<br><br><b>Dependencies:</b> Hash Map</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def dupSub(root):&#10;    m = {}&#10;    def solve(node):&#10;        if not node: return &quot;$&quot;&#10;        s = &quot;&quot;&#10;        if not node.left and not node.right:&#10;            return str(node.data)&#10;        s = str(node.data) + &quot;-&quot; + solve(node.left) + &quot;-&quot; + solve(node.right)&#10;        m[s] = m.get(s, 0) + 1&#10;        return s&#10;    solve(root)&#10;    for count in m.values():&#10;        if count &gt;= 2: return 1&#10;    return 0</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">53</td>
      <td rowspan="1">Tree 53 Check If 2 Trees Are Mirror Or Not<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/check-mirror-in-n-ary-tree1528/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Stack and Queue.</td>
      <td><b>Time:</b> O(E)<br><b>Space:</b> O(E)</td>
      <td>Store the children of the first tree in a stack (LIFO) and the children of the second tree in a queue (FIFO) for each node using hash maps. Then compare if the stack top matches the queue front for all nodes.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def checkMirrorTree(n, e, A, B):&#10;    s = collections.defaultdict(list)&#10;    q = collections.defaultdict(collections.deque)&#10;    for i in range(0, 2 * e, 2):&#10;        s[A[i]].append(A[i+1])&#10;        q[B[i]].append(B[i+1])&#10;    for node in s:&#10;        while s[node] and q[node]:&#10;            if s[node][-1] != q[node][0]: return 0&#10;            s[node].pop()&#10;            q[node].popleft()&#10;        if s[node] or q[node]: return 0&#10;    return 1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">54</td>
      <td rowspan="1">Tree 54 Sum Of Nodes On The Longest Path From Root To Leaf Node<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/sum-of-the-longest-bloodline-of-a-tree/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> DFS.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>Use DFS. Keep track of the maximum length and the maximum sum. At each node, check if the current length is greater than max length. If so, update max length and max sum. If lengths are equal, update max sum if current sum is greater.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def sumOfLongRootToLeafPath(root):&#10;    maxLen = [0]&#10;    maxSum = [float(&#x27;-inf&#x27;)]&#10;    def solve(node, sum_val, length):&#10;        if not node:&#10;            if length &gt; maxLen[0]:&#10;                maxLen[0] = length&#10;                maxSum[0] = sum_val&#10;            elif length == maxLen[0]:&#10;                maxSum[0] = max(sum_val, maxSum[0])&#10;            return&#10;        sum_val += node.data&#10;        solve(node.left, sum_val, length + 1)&#10;        solve(node.right, sum_val, length + 1)&#10;    solve(root, 0, 0)&#10;    return maxSum[0] if maxSum[0] != float(&#x27;-inf&#x27;) else 0</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">55</td>
      <td rowspan="1">Tree 55 Kth Ancestor In A Tree<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/kth-ancestor-in-a-tree/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Recursive backtracking.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>Use a recursive function. If the target node is found, return it. As you return back up the call stack, decrement `k`. When `k` becomes 0, the current node is the kth ancestor.</td>
      <td><b>Edge Cases:</b> k > depth<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def kthAncestor(root, k, node):&#10;    ans_node = None&#10;    def solve(root):&#10;        nonlocal k, ans_node&#10;        if not root: return False&#10;        if root.data == node: return True&#10;        left = solve(root.left)&#10;        right = solve(root.right)&#10;        if left or right:&#10;            k -= 1&#10;            if k == 0:&#10;                ans_node = root&#10;                return False&#10;            return True&#10;        return False&#10;    solve(root)&#10;    return ans_node.data if ans_node else -1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">56</td>
      <td rowspan="1">Tree 56 Find All Duplicate Subtrees In A Binary Tree<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/duplicate-subtrees/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Serialization + Hash Map.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N^2)</td>
      <td>Serialize each subtree into a string (e.g., using preorder traversal). Use a hash map to count the frequencies of these serialized strings. If a string appears exactly twice, add the root of that subtree to the result list.<br><br><b>Dependencies:</b> Hash Map</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def printAllDups(root):&#10;    m = {}&#10;    ans = []&#10;    def solve(node):&#10;        if not node: return &quot;N&quot;&#10;        s = str(node.data) + &quot;,&quot; + solve(node.left) + &quot;,&quot; + solve(node.right)&#10;        m[s] = m.get(s, 0) + 1&#10;        if m[s] == 2: ans.append(node)&#10;        return s&#10;    solve(root)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">57</td>
      <td rowspan="1">Tree 57 Symmetric Tree<br><br></b> <a href="https://leetcode.com/problems/symmetric-tree/" target="_blank">LeetCode 101</a></td>
      <td rowspan="1"><b>Example 1:</b> Recursive.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>Use a helper function `isMirror(left, right)`. The tree is symmetric if `root->left` and `root->right` are mirrors. Two trees are mirrors if their roots are equal and `left1->left` is mirror of `right1->right`, and `left1->right` is mirror of `right1->left`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isSymmetric(root):&#10;    def isMirror(n1, n2):&#10;        if not n1 and not n2: return True&#10;        if not n1 or not n2: return False&#10;        return (n1.val == n2.val) and isMirror(n1.left, n2.right) and isMirror(n1.right, n2.left)&#10;    if not root: return True&#10;    return isMirror(root.left, root.right)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">58</td>
      <td rowspan="1">Tree 58 Root To Node Path In Binary Tree<br><br></b> <a href="https://www.interviewbit.com/problems/path-to-given-node/" target="_blank">InterviewBit</a></td>
      <td rowspan="1"><b>Example 1:</b> Recursive backtracking.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>Use recursion. Push current node to the path array. If it's the target node, return true. Recursively search left and right subtrees. If either returns true, return true. If not found in either, pop the current node from the path array and return false.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def solve(A, B):&#10;    arr = []&#10;    def getPath(node, x):&#10;        if not node: return False&#10;        arr.append(node.val)&#10;        if node.val == x: return True&#10;        if getPath(node.left, x) or getPath(node.right, x): return True&#10;        arr.pop()&#10;        return False&#10;    if not A: return arr&#10;    getPath(A, B)&#10;    return arr</code></pre></details></td>
    </tr>
  </tbody>
</table>


## Heaps

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
      <td rowspan="1">1</td>
      <td rowspan="1">Heap 01 Kth Largest Element In An Array<br><br></b> <a href="https://leetcode.com/problems/kth-largest-element-in-an-array/" target="_blank">LeetCode 215</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> nums = [3,2,1,5,6,4], k = 2<br><b>Output:</b> 5<br><br><b>Note (Constraint):</b> Can you solve it without sorting?</td>
      <td><b>Time:</b> O(N log K) (Constraint)<br><b>Space:</b> O(K) (Constraint)</td>
      <td>Use a Min-Heap of size K. When the heap exceeds size K, pop the minimum element. The top of the heap will be the Kth largest.<br><br><b>Dependencies:</b> <code>std::priority_queue</code> / <code>heapq</code></td>
      <td><b>Edge Cases:</b> <b>Min-Heap sizing:</b> By strictly keeping the size to `k`, the `k` largest elements are trapped inside, with the smallest of them right at the top.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def find_kth_largest(nums: list[int], k: int) -&gt; int:&#10;    min_heap = []&#10;    for num in nums:&#10;        heapq.heappush(min_heap, num)&#10;        if len(min_heap) &gt; k:&#10;            heapq.heappop(min_heap)&#10;    return min_heap[0]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">2</td>
      <td rowspan="1">Heap 02 Merge K Sorted Lists<br><br></b> <a href="https://leetcode.com/problems/merge-k-sorted-lists/" target="_blank">LeetCode 23</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> lists = [[1,4,5],[1,3,4],[2,6]]<br><b>Output:</b> [1,1,2,3,4,4,5,6]</td>
      <td><b>Time:</b> O(N log K) (Constraint)<br><b>Space:</b> O(K) (Constraint)</td>
      <td>Push the head of each list into a Min-Heap. Repeatedly pop the smallest node, attach it to the result list, and push its `next` node into the heap.<br><br><b>Dependencies:</b> Custom Comparator</td>
      <td><b>Edge Cases:</b> <b>Pointer Compare:</b> Priority queues need a custom comparator to sort `ListNode*` by their `val`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def merge_k_lists(lists: list[ListNode]) -&gt; ListNode:&#10;    # To avoid comparing ListNodes directly in Python heapq, store (val, index, node)&#10;    heap = []&#10;    for i, lst in enumerate(lists):&#10;        if lst:&#10;            heapq.heappush(heap, (lst.val, i, lst))&#10;            &#10;    dummy = ListNode(0)&#10;    tail = dummy&#10;    &#10;    while heap:&#10;        val, i, node = heapq.heappop(heap)&#10;        tail.next = node&#10;        tail = tail.next&#10;        if node.next:&#10;            heapq.heappush(heap, (node.next.val, i, node.next))&#10;            &#10;    return dummy.next</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">3</td>
      <td rowspan="1">Heap 03 Top K Frequent Elements<br><br></b> <a href="https://leetcode.com/problems/top-k-frequent-elements/" target="_blank">LeetCode 347</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> nums = [1,1,1,2,2,3], k = 2<br><b>Output:</b> [1,2]</td>
      <td><b>Time:</b> O(N log K)<br><b>Space:</b> O(N)</td>
      <td>Use a Hash Map to count frequencies. Use a Min-Heap of size `k` to keep track of the top `k` elements.<br><br><b>Dependencies:</b> <code>std::priority_queue</code>, <code>heapq</code></td>
      <td><b>Edge Cases:</b> <b>Min-Heap capacity:</b> If heap size exceeds `k`, pop the top (which is the element with the lowest frequency currently in the heap).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;from collections import Counter&#10;def topKFrequent(nums: list[int], k: int) -&gt; list[int]:&#10;    count = Counter(nums)&#10;    return heapq.nlargest(k, count.keys(), key=count.get)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">4</td>
      <td rowspan="1">Heap 04 Kth Smallest Element In A Sorted Matrix<br><br></b> <a href="https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/" target="_blank">LeetCode 378</a></td>
      <td rowspan="1"><b>Example 1:</b> Binary search on range.</td>
      <td><b>Time:</b> O(N log(Max-Min))<br><b>Space:</b> O(1)</td>
      <td>Binary search on the value range `[matrix[0][0], matrix[n-1][n-1]]`. Count elements less than or equal to `mid` using two pointers (start from bottom-left). If count >= k, search left half, else search right.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def kthSmallest(matrix: List[List[int]], k: int) -&gt; int:&#10;    n = len(matrix)&#10;    def countLessOrEqual(mid):&#10;        count, r, c = 0, n - 1, 0&#10;        while r &gt;= 0 and c &lt; n:&#10;            if matrix[r][c] &lt;= mid:&#10;                count += r + 1&#10;                c += 1&#10;            else:&#10;                r -= 1&#10;        return count&#10;    low, high = matrix[0][0], matrix[-1][-1]&#10;    while low &lt;= high:&#10;        mid = low + (high - low) // 2&#10;        if countLessOrEqual(mid) &gt;= k:&#10;            high = mid - 1&#10;        else:&#10;            low = mid + 1&#10;    return low</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">5</td>
      <td rowspan="1">Heap 05 Find Median From Data Stream<br><br></b> <a href="https://leetcode.com/problems/find-median-from-data-stream/" target="_blank">LeetCode 295</a></td>
      <td rowspan="1"><b>Example 1:</b> Two heaps.</td>
      <td><b>Time:</b> O(log N) add, O(1) find<br><b>Space:</b> O(N)</td>
      <td>Maintain two heaps: a max-heap for the smaller half of numbers and a min-heap for the larger half. Balance them such that the max-heap has at most 1 more element than the min-heap.<br><br><b>Dependencies:</b> <code>#include <queue></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;class MedianFinder:&#10;    def __init__(self):&#10;        self.small = []&#10;        self.large = []&#10;    def addNum(self, num: int) -&gt; None:&#10;        heapq.heappush(self.small, -num)&#10;        heapq.heappush(self.large, -heapq.heappop(self.small))&#10;        if len(self.small) &lt; len(self.large):&#10;            heapq.heappush(self.small, -heapq.heappop(self.large))&#10;    def findMedian(self) -&gt; float:&#10;        if len(self.small) &gt; len(self.large): return -self.small[0]&#10;        return (-self.small[0] + self.large[0]) / 2.0</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">6</td>
      <td rowspan="1">Heap 06 Replace Each Array Element By Its Corresponding Rank<br><br></b> <a href="https://leetcode.com/problems/rank-transform-of-an-array/" target="_blank">LeetCode 1331</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> [40,10,20,30]<br><b>Output:</b> [4,1,2,3]</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(N)</td>
      <td>Create a copy of array, sort it, and remove duplicates. Use a hash map to map each unique value to its rank. Replace elements in original array using map.<br><br><b>Dependencies:</b> <code>#include <unordered_map>\n#include <set></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def arrayRankTransform(arr: List[int]) -&gt; List[int]:&#10;    st = sorted(list(set(arr)))&#10;    mpp = {num: rank + 1 for rank, num in enumerate(st)}&#10;    return [mpp[num] for num in arr]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">7</td>
      <td rowspan="1">Heap 07 Task Scheduler<br><br></b> <a href="https://leetcode.com/problems/task-scheduler/" target="_blank">LeetCode 621</a></td>
      <td rowspan="1"><b>Example 1:</b> Greedy placement.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Find max frequency `max_f`. Calculate idle slots `(max_f - 1) * n`. Iterate remaining frequencies and subtract from idle slots. Return `tasks.length + max(0, idle_slots)`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def leastInterval(tasks: List[str], n: int) -&gt; int:&#10;    counts = list(collections.Counter(tasks).values())&#10;    max_f = max(counts)&#10;    count_max = counts.count(max_f)&#10;    ans = (max_f - 1) * (n + 1) + count_max&#10;    return max(ans, len(tasks))</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">8</td>
      <td rowspan="1">Heap 08 Hand Of Straights<br><br></b> <a href="https://leetcode.com/problems/hand-of-straights/" target="_blank">LeetCode 846</a></td>
      <td rowspan="1"><b>Example 1:</b> Form consecutive sequences.</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(N)</td>
      <td>Use a map (TreeMap in C++) to store frequencies. Iterate through map. If a number has count > 0, we must form a group starting from it. Decrement counts of `num, num+1, ..., num+groupSize-1`.<br><br><b>Dependencies:</b> <code>#include <map></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def isNStraightHand(hand: List[int], groupSize: int) -&gt; bool:&#10;    if len(hand) % groupSize != 0: return False&#10;    count = collections.Counter(hand)&#10;    for card in sorted(count.keys()):&#10;        if count[card] &gt; 0:&#10;            c = count[card]&#10;            for i in range(groupSize):&#10;                if count[card + i] &lt; c: return False&#10;                count[card + i] -= c&#10;    return True</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">9</td>
      <td rowspan="1">Heap 09 Design Twitter<br><br></b> <a href="https://leetcode.com/problems/design-twitter/" target="_blank">LeetCode 355</a></td>
      <td rowspan="1"><b>Example 1:</b> Object oriented design.</td>
      <td><b>Time:</b> O(N log 10)<br><b>Space:</b> O(U + T)</td>
      <td>Use a hash map to map user to their followees. Use another map to map user to their tweets. For news feed, use a Max-Heap to extract the 10 most recent tweets from the user and their followees.<br><br><b>Dependencies:</b> <code>#include <unordered_map>\n#include <unordered_set>\n#include <queue></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;import collections&#10;class Twitter:&#10;    def __init__(self):&#10;        self.time = 0&#10;        self.tweets = collections.defaultdict(list)&#10;        self.followers = collections.defaultdict(set)&#10;    def postTweet(self, userId: int, tweetId: int) -&gt; None:&#10;        self.tweets[userId].append((self.time, tweetId))&#10;        self.time -= 1&#10;    def getNewsFeed(self, userId: int) -&gt; List[int]:&#10;        users = self.followers[userId] | {userId}&#10;        hq = []&#10;        for u in users:&#10;            for t in self.tweets[u][-10:]:&#10;                heapq.heappush(hq, t)&#10;        return [t[1] for t in heapq.nsmallest(10, hq)]&#10;    def follow(self, followerId: int, followeeId: int) -&gt; None:&#10;        self.followers[followerId].add(followeeId)&#10;    def unfollow(self, followerId: int, followeeId: int) -&gt; None:&#10;        self.followers[followerId].discard(followeeId)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">10</td>
      <td rowspan="1">Heap 10 Kth Largest Element In A Stream<br><br></b> <a href="https://leetcode.com/problems/kth-largest-element-in-a-stream/" target="_blank">LeetCode 703</a></td>
      <td rowspan="1"><b>Example 1:</b> Min-heap of size K.</td>
      <td><b>Time:</b> O(N log K) for init, O(log K) for add<br><b>Space:</b> O(K)</td>
      <td>Maintain a min-heap of size exactly `k`. The top of the min-heap will always represent the kth largest element. For every new element added, if the heap size is less than `k`, push it. If the heap is of size `k` and the new element is greater than the top, pop the top and push the new element.<br><br><b>Dependencies:</b> <code>#include <queue></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;class KthLargest:&#10;    def __init__(self, k: int, nums: List[int]):&#10;        self.k = k&#10;        self.min_heap = nums&#10;        heapq.heapify(self.min_heap)&#10;        while len(self.min_heap) &gt; k:&#10;            heapq.heappop(self.min_heap)&#10;    def add(self, val: int) -&gt; int:&#10;        heapq.heappush(self.min_heap, val)&#10;        if len(self.min_heap) &gt; self.k:&#10;            heapq.heappop(self.min_heap)&#10;        return self.min_heap[0]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">11</td>
      <td rowspan="1">Heap 11 K Closest Points To Origin<br><br></b> <a href="https://leetcode.com/problems/k-closest-points-to-origin/" target="_blank">LeetCode 973</a></td>
      <td rowspan="1"><b>Example 1:</b> Max-heap of pairs.</td>
      <td><b>Time:</b> O(N log K)<br><b>Space:</b> O(K)</td>
      <td>Use a max-heap of size `k` to store pairs of `(distance, point_index)`. Iterate over all points, push into heap. If heap size exceeds `k`, pop the max element. The heap will eventually hold the `k` points with minimum distance.<br><br><b>Dependencies:</b> <code>#include <queue></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def kClosest(points: List[List[int]], k: int) -&gt; List[List[int]]:&#10;    heap = []&#10;    for i, (x, y) in enumerate(points):&#10;        dist = -(x*x + y*y)&#10;        if len(heap) &lt; k:&#10;            heapq.heappush(heap, (dist, i))&#10;        else:&#10;            heapq.heappushpop(heap, (dist, i))&#10;    return [points[i] for _, i in heap]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">12</td>
      <td rowspan="1">Heap 12 Reorganize String<br><br></b> <a href="https://leetcode.com/problems/reorganize-string/" target="_blank">LeetCode 767</a></td>
      <td rowspan="1"><b>Example 1:</b> Duplicate logic entry. See Greedy chapter.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(26)</td>
      <td>See greedy_38_reorganize_string.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python"># Implementation provided in greedy chapter.</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">13</td>
      <td rowspan="1">Heap 13 Smallest Range In K Lists<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/find-smallest-range-containing-elements-from-k-lists/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Min-Heap.</td>
      <td><b>Time:</b> O(N * K * log K)<br><b>Space:</b> O(K)</td>
      <td>Maintain a min-heap of size K, storing the first element of each list along with its list index and element index. Keep track of the `max_val` currently in the heap. The current range is `[heap_min, max_val]`. Extract the min, update the smallest range if needed, and insert the next element from the extracted element's list. Update `max_val` with the new element.<br><br><b>Dependencies:</b> <code>#include <queue></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def findSmallestRange(KSortedArray: List[List[int]], n: int, k: int) -&gt; List[int]:&#10;    pq = []&#10;    mx = float(&#x27;-inf&#x27;)&#10;    for i in range(k):&#10;        heapq.heappush(pq, (KSortedArray[i][0], i, 0))&#10;        mx = max(mx, KSortedArray[i][0])&#10;    ans_range = float(&#x27;inf&#x27;)&#10;    start, end = -1, -1&#10;    while pq:&#10;        mn, row, col = heapq.heappop(pq)&#10;        if mx - mn &lt; ans_range:&#10;            ans_range = mx - mn&#10;            start, end = mn, mx&#10;        if col + 1 &lt; n:&#10;            next_val = KSortedArray[row][col+1]&#10;            heapq.heappush(pq, (next_val, row, col+1))&#10;            mx = max(mx, next_val)&#10;        else:&#10;            break&#10;    return [start, end]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">14</td>
      <td rowspan="1">Heap 14 Kth Largest Sum Contiguous Subarray<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/k-th-largest-sum-contiguous-subarray/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Min-Heap.</td>
      <td><b>Time:</b> O(N^2 log K)<br><b>Space:</b> O(K)</td>
      <td>Iterate all subarrays using two nested loops. Maintain a min-heap of size K to store the top K sums. If the heap size < K, push the current sum. If the heap size == K and current sum > heap top, pop and push current sum. The top of the heap is the Kth largest sum.<br><br><b>Dependencies:</b> <code>#include <queue></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def kthLargest(Arr: List[int], N: int, K: int) -&gt; int:&#10;    pq = []&#10;    for i in range(N):&#10;        s = 0&#10;        for j in range(i, N):&#10;            s += Arr[j]&#10;            if len(pq) &lt; K:&#10;                heapq.heappush(pq, s)&#10;            elif s &gt; pq[0]:&#10;                heapq.heappop(pq)&#10;                heapq.heappush(pq, s)&#10;    return pq[0]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">15</td>
      <td rowspan="1">Heap 15 Minimum Sum Of Two Numbers Formed From Digits Of An Array<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/minimum-sum4058/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Sort or Min-Heap.</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(N)</td>
      <td>Sort the array. Build two strings representing the two numbers by picking digits alternately from the sorted array. Add the two large numbers as strings or build the result dynamically.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def solve(arr: List[int], n: int) -&gt; str:&#10;    arr.sort()&#10;    a, b = &quot;&quot;, &quot;&quot;&#10;    for i in range(n):&#10;        if i % 2 == 0:&#10;            a += str(arr[i])&#10;        else:&#10;            b += str(arr[i])&#10;    res = str(int(a) + int(b)) if a and b else str(int(a or &#x27;0&#x27;) + int(b or &#x27;0&#x27;))&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">16</td>
      <td rowspan="1">Heap 16 Is Binary Tree Heap<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/is-binary-tree-heap/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Tree Traversal.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(H)</td>
      <td>First, check if the tree is complete by counting nodes and ensuring no node's index `i > count`. Then check if every node satisfies the max-heap property (`node.val >= left.val` and `node.val >= right.val`).</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isHeap(tree: Node) -&gt; bool:&#10;    def countNodes(node):&#10;        if not node: return 0&#10;        return 1 + countNodes(node.left) + countNodes(node.right)&#10;    def isCBT(node, index, count):&#10;        if not node: return True&#10;        if index &gt;= count: return False&#10;        return isCBT(node.left, 2 * index + 1, count) and isCBT(node.right, 2 * index + 2, count)&#10;    def isMaxOrder(node):&#10;        if not node.left and not node.right: return True&#10;        if not node.right: return node.data &gt;= node.left.data&#10;        return (node.data &gt;= node.left.data and node.data &gt;= node.right.data and&#10;                isMaxOrder(node.left) and isMaxOrder(node.right))&#10;    count = countNodes(tree)&#10;    return isCBT(tree, 0, count) and isMaxOrder(tree)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">17</td>
      <td rowspan="1">Heap 17 Convert Min Heap To Max Heap<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/convert-min-heap-to-max-heap-1666738710/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Heapify.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(log N) for recursion</td>
      <td>Apply the standard max-heapify process starting from the last non-leaf node `(N/2 - 1)` down to the root. This takes O(N) time.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def convertMinToMaxHeap(arr: List[int], N: int):&#10;    def maxHeapify(i):&#10;        largest, left, right = i, 2 * i + 1, 2 * i + 2&#10;        if left &lt; N and arr[left] &gt; arr[largest]: largest = left&#10;        if right &lt; N and arr[right] &gt; arr[largest]: largest = right&#10;        if largest != i:&#10;            arr[i], arr[largest] = arr[largest], arr[i]&#10;            maxHeapify(largest)&#10;    for i in range((N - 2) // 2, -1, -1):&#10;        maxHeapify(i)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">18</td>
      <td rowspan="1">Heap 18 Minimum Cost Of Ropes<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/minimum-cost-of-ropes-1587115620/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Min-Heap Greedy.</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(N)</td>
      <td>Use a min-heap. Pop two minimum length ropes, add them up, add sum to total cost, and push the merged rope back to the heap. Repeat until one rope remains.<br><br><b>Dependencies:</b> <code>#include <queue></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def minCost(arr: List[int], n: int) -&gt; int:&#10;    pq = list(arr)&#10;    heapq.heapify(pq)&#10;    cost = 0&#10;    while len(pq) &gt; 1:&#10;        a = heapq.heappop(pq)&#10;        b = heapq.heappop(pq)&#10;        cost += a + b&#10;        heapq.heappush(pq, a + b)&#10;    return cost</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">19</td>
      <td rowspan="1">Heap 19 K Th Largest Element In A Stream<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/kth-largest-element-in-a-stream2220/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Min-Heap of size K.</td>
      <td><b>Time:</b> O(N log K)<br><b>Space:</b> O(K)</td>
      <td>Maintain a min-heap of size K. While processing the stream, if heap size is < K, push current element. If heap size == K and current element is > heap top, pop and push current element. Append heap top to result if size is K, else append -1.<br><br><b>Dependencies:</b> <code>#include <queue></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def kthLargest(k: int, arr: List[int], n: int) -&gt; List[int]:&#10;    res = []&#10;    pq = []&#10;    for i in range(n):&#10;        if len(pq) &lt; k:&#10;            heapq.heappush(pq, arr[i])&#10;        elif arr[i] &gt; pq[0]:&#10;            heapq.heappop(pq)&#10;            heapq.heappush(pq, arr[i])&#10;        if len(pq) &lt; k:&#10;            res.append(-1)&#10;        else:&#10;            res.append(pq[0])&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">20</td>
      <td rowspan="1">Heap 20 Merge K Sorted Arrays<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/merge-k-sorted-arrays/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Min Heap.</td>
      <td><b>Time:</b> O(K^2 log K)<br><b>Space:</b> O(K)</td>
      <td>Create a min-heap that stores a tuple: (value, array_index, element_index). Push the first element of each of the K arrays into the heap. While the heap is not empty, pop the minimum element, add it to the result, and if the array from which it was popped has more elements, push the next element to the heap.<br><br><b>Dependencies:</b> Priority Queue</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def mergeKArrays(arr: List[List[int]], K: int) -&gt; List[int]:&#10;    pq = []&#10;    res = []&#10;    for i in range(K):&#10;        heapq.heappush(pq, (arr[i][0], i, 0))&#10;    while pq:&#10;        val, row, col = heapq.heappop(pq)&#10;        res.append(val)&#10;        if col + 1 &lt; len(arr[row]):&#10;            heapq.heappush(pq, (arr[row][col + 1], row, col + 1))&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">21</td>
      <td rowspan="1">Heap 21 Smallest Range Covering Elements From K Lists<br><br></b> <a href="https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/" target="_blank">LeetCode 632</a></td>
      <td rowspan="1"><b>Example 1:</b> Min Heap.</td>
      <td><b>Time:</b> O(N log K)<br><b>Space:</b> O(K)</td>
      <td>Use a min-heap storing `(value, list_idx, elem_idx)`. Also maintain the `current_max` of the elements currently in the heap. The current range is `[heap_top, current_max]`. Pop the min, push the next element from its list, and update `current_max`. Continue until any list is exhausted.<br><br><b>Dependencies:</b> Priority Queue</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def smallestRange(nums: List[List[int]]) -&gt; List[int]:&#10;    pq = []&#10;    currMax = float(&#x27;-inf&#x27;)&#10;    for i in range(len(nums)):&#10;        heapq.heappush(pq, (nums[i][0], i, 0))&#10;        currMax = max(currMax, nums[i][0])&#10;    ans = [pq[0][0], currMax]&#10;    while True:&#10;        val, r, c = heapq.heappop(pq)&#10;        if currMax - val &lt; ans[1] - ans[0]:&#10;            ans = [val, currMax]&#10;        if c + 1 == len(nums[r]):&#10;            break&#10;        next_val = nums[r][c + 1]&#10;        heapq.heappush(pq, (next_val, r, c + 1))&#10;        currMax = max(currMax, next_val)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">22</td>
      <td rowspan="1">Heap 22 K Largest Elements<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/k-largest-elements4206/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Min Heap.</td>
      <td><b>Time:</b> O(N log K)<br><b>Space:</b> O(K)</td>
      <td>Maintain a min-heap of size K. Iterate through the array. If the heap has < K elements, push. Else if the current element > heap's top, pop the top and push the current element. The heap will contain the K largest elements.<br><br><b>Dependencies:</b> Priority Queue</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def kLargest(arr: List[int], n: int, k: int) -&gt; List[int]:&#10;    pq = []&#10;    for i in range(n):&#10;        heapq.heappush(pq, arr[i])&#10;        if len(pq) &gt; k:&#10;            heapq.heappop(pq)&#10;    return sorted(pq, reverse=True)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">23</td>
      <td rowspan="1">Heap 23 Kth Smallest Element<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/kth-smallest-element5635/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Max Heap.</td>
      <td><b>Time:</b> O(N log K)<br><b>Space:</b> O(K)</td>
      <td>Use a Max Heap of size K. Iterate through the array. For the first K elements, insert them into the heap. For the remaining elements, if the element is smaller than the top of the heap, pop the top and insert the element. The top of the heap will be the Kth smallest element.<br><br><b>Dependencies:</b> Priority Queue</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def kthSmallest(arr, l, r, k):&#10;    pq = []&#10;    for i in range(l, r + 1):&#10;        if len(pq) &lt; k: heapq.heappush(pq, -arr[i])&#10;        elif arr[i] &lt; -pq[0]:&#10;            heapq.heappop(pq)&#10;            heapq.heappush(pq, -arr[i])&#10;    return -pq[0]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">24</td>
      <td rowspan="1">Heap 24 Merge Two Binary Max Heaps<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/merge-two-binary-max-heap0144/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Append and Heapify.</td>
      <td><b>Time:</b> O(N + M)<br><b>Space:</b> O(N + M)</td>
      <td>Create a new array by appending the two arrays. Then call `heapify` starting from the last non-leaf node `(n/2 - 1)` down to the root `0`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def mergeHeaps(a, b, n, m):&#10;    ans = a + b&#10;    total = n + m&#10;    def heapify(i):&#10;        largest = i&#10;        l = 2 * i + 1&#10;        r = 2 * i + 2&#10;        if l &lt; total and ans[l] &gt; ans[largest]: largest = l&#10;        if r &lt; total and ans[r] &gt; ans[largest]: largest = r&#10;        if largest != i:&#10;            ans[i], ans[largest] = ans[largest], ans[i]&#10;            heapify(largest)&#10;    for i in range(total // 2 - 1, -1, -1):&#10;        heapify(i)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">25</td>
      <td rowspan="1">Heap 25 Kth Largest Sum Contiguous Subarray<br><br></b> <a href="https://www.geeksforgeeks.org/k-th-largest-sum-contiguous-subarray/" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Prefix sum + Min Heap.</td>
      <td><b>Time:</b> O(N^2 log K)<br><b>Space:</b> O(N + K)</td>
      <td>Iterate through all possible subarrays and calculate their sums using a prefix sum array. Maintain a Min Heap of size K to keep track of the top K sums. At the end, the top of the Min Heap is the K-th largest sum.<br><br><b>Dependencies:</b> Priority Queue</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def kthLargestSum(arr, n, k):&#10;    sum_arr = [0] * (n + 1)&#10;    for i in range(1, n + 1): sum_arr[i] = sum_arr[i - 1] + arr[i - 1]&#10;    pq = []&#10;    for i in range(1, n + 1):&#10;        for j in range(i, n + 1):&#10;            x = sum_arr[j] - sum_arr[i - 1]&#10;            if len(pq) &lt; k: heapq.heappush(pq, x)&#10;            elif x &gt; pq[0]:&#10;                heapq.heappop(pq)&#10;                heapq.heappush(pq, x)&#10;    return pq[0]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">26</td>
      <td rowspan="1">Heap 26 Convert BST To Min Heap<br><br></b> <a href="https://www.geeksforgeeks.org/convert-bst-min-heap/" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Inorder + Preorder.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Since a BST inorder gives sorted values, store the inorder traversal in an array. The requirement says left subtree elements < right subtree elements, which matches a Preorder traversal (Root, Left, Right) since we want the smallest element at the root. So do a Preorder traversal of the tree and replace nodes with array elements.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def convertToMinHeapUtil(root):&#10;    arr = []&#10;    def inorder(node):&#10;        if not node: return&#10;        inorder(node.left)&#10;        arr.append(node.data)&#10;        inorder(node.right)&#10;    def preorderFill(node, idx):&#10;        if not node: return&#10;        node.data = arr[idx[0]]&#10;        idx[0] += 1&#10;        preorderFill(node.left, idx)&#10;        preorderFill(node.right, idx)&#10;    inorder(root)&#10;    preorderFill(root, [0])</code></pre></details></td>
    </tr>
  </tbody>
</table>


## Graphs

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
      <td rowspan="1">1</td>
      <td rowspan="1">Graph 01 Number Of Islands<br><br></b> <a href="https://leetcode.com/problems/number-of-islands/" target="_blank">LeetCode 200</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]<br><b>Output:</b> 3</td>
      <td><b>Time:</b> O(M * N) (Constraint)<br><b>Space:</b> O(M * N) (Constraint)</td>
      <td>Iterate through the grid. When a '1' is found, increment island count and use DFS to sink the island (turn connected '1's to '0's).</td>
      <td><b>Edge Cases:</b> <b>In-place Visited Check:</b> Sinking the island by changing '1' to '0' avoids needing a separate `visited` matrix.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def num_islands(grid: list[list[str]]) -&gt; int:&#10;    if not grid: return 0&#10;    def dfs(i, j):&#10;        if i &lt; 0 or i &gt;= len(grid) or j &lt; 0 or j &gt;= len(grid[0]) or grid[i][j] == &#x27;0&#x27;:&#10;            return&#10;        grid[i][j] = &#x27;0&#x27;&#10;        dfs(i+1, j); dfs(i-1, j); dfs(i, j+1); dfs(i, j-1)&#10;    count = 0&#10;    for i in range(len(grid)):&#10;        for j in range(len(grid[0])):&#10;            if grid[i][j] == &#x27;1&#x27;:&#10;                count += 1&#10;                dfs(i, j)&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">2</td>
      <td rowspan="1">Graph 02 Course Schedule<br><br></b> <a href="https://leetcode.com/problems/course-schedule/" target="_blank">LeetCode 207</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> numCourses = 2, prerequisites = [[1,0]]<br><b>Output:</b> true</td>
      <td><b>Time:</b> O(V + E) (Constraint)<br><b>Space:</b> O(V + E)</td>
      <td>Kahn's Algorithm (BFS). Count in-degrees. Add courses with 0 in-degree to queue. Process queue, reducing in-degrees of neighbors.<br><br><b>Dependencies:</b> <code>std::queue</code></td>
      <td><b>Edge Cases:</b> <b>Graph Building:</b> Convert `prerequisites` edge list into an Adjacency List for fast neighbor lookups.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">from collections import deque&#10;def can_finish(numCourses: int, prerequisites: list[list[int]]) -&gt; bool:&#10;    adj = {i: [] for i in range(numCourses)}&#10;    indegree = [0] * numCourses&#10;    for crs, pre in prerequisites:&#10;        adj[pre].append(crs)&#10;        indegree[crs] += 1&#10;    q = deque([i for i in range(numCourses) if indegree[i] == 0])&#10;    count = 0&#10;    while q:&#10;        node = q.popleft()&#10;        count += 1&#10;        for neighbor in adj[node]:&#10;            indegree[neighbor] -= 1&#10;            if indegree[neighbor] == 0:&#10;                q.append(neighbor)&#10;    return count == numCourses</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">3</td>
      <td rowspan="1">Graph 03 Bipartite Graph<br><br></b> <a href="https://leetcode.com/problems/is-graph-bipartite/" target="_blank">LeetCode 785</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> graph = [[1,2,3],[0,2],[0,1,3],[0,2]]<br><b>Output:</b> false</td>
      <td><b>Time:</b> O(V + E)<br><b>Space:</b> O(V)</td>
      <td>BFS/DFS coloring approach. Color adjacent nodes with alternate colors (0 and 1). If an adjacent node has the SAME color, it's not bipartite.<br><br><b>Dependencies:</b> <code>std::queue</code></td>
      <td><b>Edge Cases:</b> <b>Disconnected Graph:</b> Must loop over all nodes `0` to `V-1` to ensure every disconnected component is checked.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">from collections import deque&#10;def isBipartite(graph: list[list[int]]) -&gt; bool:&#10;    n = len(graph)&#10;    color = [-1] * n&#10;    for i in range(n):&#10;        if color[i] != -1: continue&#10;        q = deque([i])&#10;        color[i] = 0&#10;        while q:&#10;            node = q.popleft()&#10;            for neighbor in graph[node]:&#10;                if color[neighbor] == -1:&#10;                    color[neighbor] = 1 - color[node]&#10;                    q.append(neighbor)&#10;                elif color[neighbor] == color[node]:&#10;                    return False&#10;    return True</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">4</td>
      <td rowspan="1">Graph 04 Dijkstras Algorithm<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Source = 0<br><b>Output:</b> distances array.</td>
      <td><b>Time:</b> O(E log V)<br><b>Space:</b> O(V)</td>
      <td>Min-heap (priority queue) to repeatedly extract the node with the minimum distance and relax its neighbors.<br><br><b>Dependencies:</b> <code>#include &lt;queue&gt;</code></td>
      <td><b>Edge Cases:</b> <b>Disconnected graph:</b> Distances remain infinity.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def dijkstra(V: int, adj: List[List[List[int]]], S: int) -&gt; List[int]:&#10;    import heapq&#10;    dist = [float(&#x27;inf&#x27;)] * V&#10;    dist[S] = 0&#10;    pq = [(0, S)]&#10;    while pq:&#10;        d, node = heapq.heappop(pq)&#10;        if d &gt; dist[node]: continue&#10;        for nxt, weight in adj[node]:&#10;            if d + weight &lt; dist[nxt]:&#10;                dist[nxt] = d + weight&#10;                heapq.heappush(pq, (dist[nxt], nxt))&#10;    return dist</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">5</td>
      <td rowspan="1">Graph 05 Topological Sort<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/topological-sort/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> V = 4, adj = [[], [0], [0], [0]]<br><b>Output:</b> valid topological sort.</td>
      <td><b>Time:</b> O(V + E)<br><b>Space:</b> O(V)</td>
      <td>Kahn's Algorithm (BFS) using in-degrees. Add nodes with 0 in-degree to a queue. Pop, append to result, and decrement in-degrees of neighbors.<br><br><b>Dependencies:</b> <code>#include &lt;queue&gt;</code></td>
      <td><b>Edge Cases:</b> <b>Cycles:</b> If cycle exists, result will not contain all V elements.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def topoSort(V: int, adj: List[List[int]]) -&gt; List[int]:&#10;    from collections import deque&#10;    indegree = [0] * V&#10;    for i in range(V):&#10;        for nxt in adj[i]: indegree[nxt] += 1&#10;    q = deque([i for i in range(V) if indegree[i] == 0])&#10;    topo = []&#10;    while q:&#10;        node = q.popleft()&#10;        topo.append(node)&#10;        for nxt in adj[node]:&#10;            indegree[nxt] -= 1&#10;            if indegree[nxt] == 0: q.append(nxt)&#10;    return topo</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">6</td>
      <td rowspan="1">Graph 06 Bellman Ford<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/0" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> V=3, S=0, Edges=[[0,1,5],[1,2,-2],[2,1,-3]]<br><b>Output:</b> [-1]</td>
      <td><b>Time:</b> O(V * E)<br><b>Space:</b> O(V)</td>
      <td>Relax all edges V-1 times. To detect a negative cycle, relax one more time; if any distance updates, there's a negative cycle.</td>
      <td><b>Edge Cases:</b> <b>Disconnected Graphs:</b> Elements unreachable from source remain at 1e8.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def bellman_ford(V: int, edges: List[List[int]], S: int) -&gt; List[int]:&#10;    dist = [int(1e8)] * V&#10;    dist[S] = 0&#10;    for _ in range(V - 1):&#10;        for u, v, wt in edges:&#10;            if dist[u] != int(1e8) and dist[u] + wt &lt; dist[v]:&#10;                dist[v] = dist[u] + wt&#10;    for u, v, wt in edges:&#10;        if dist[u] != int(1e8) and dist[u] + wt &lt; dist[v]:&#10;            return [-1]&#10;    return dist</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">7</td>
      <td rowspan="1">Graph 07 Floyd Warshall<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b><br><b>Output:</b> Shortest paths for all pairs (i, j).</td>
      <td><b>Time:</b> O(V^3)<br><b>Space:</b> O(1) in-place</td>
      <td>Multi-source shortest path. Try to go from i to j via every possible vertex k. Update `matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])`.</td>
      <td><b>Edge Cases:</b> <b>Unreachable nodes:</b> Represented by -1. Replace with 1e9 before algorithm, then back to -1.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def shortest_distance(matrix: List[List[int]]) -&gt; None:&#10;    n = len(matrix)&#10;    for i in range(n):&#10;        for j in range(n):&#10;            if matrix[i][j] == -1: matrix[i][j] = int(1e9)&#10;            if i == j: matrix[i][j] = 0&#10;    for k in range(n):&#10;        for i in range(n):&#10;            for j in range(n):&#10;                if matrix[i][k] != int(1e9) and matrix[k][j] != int(1e9):&#10;                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])&#10;    for i in range(n):&#10;        for j in range(n):&#10;            if matrix[i][j] == int(1e9): matrix[i][j] = -1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">8</td>
      <td rowspan="1">Graph 08 Mst Prims<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/minimum-spanning-tree/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Return the scalar sum of the MST.</td>
      <td><b>Time:</b> O(E log V)<br><b>Space:</b> O(E + V)</td>
      <td>Prim's Algorithm. Use a Min-Heap `(weight, node)`. Always pick the smallest available edge connecting the MST to an unvisited node.<br><br><b>Dependencies:</b> <code>#include <queue></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def spanningTree(V: int, adj: List[List[List[int]]]) -&gt; int:&#10;    pq = [(0, 0)]&#10;    vis = [0] * V&#10;    sum_val = 0&#10;    while pq:&#10;        wt, node = heapq.heappop(pq)&#10;        if vis[node] == 1: continue&#10;        vis[node] = 1&#10;        sum_val += wt&#10;        for adjNode, edW in adj[node]:&#10;            if not vis[adjNode]: heapq.heappush(pq, (edW, adjNode))&#10;    return sum_val</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">9</td>
      <td rowspan="1">Graph 09 Strongly Connected Components Kosaraju<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/strongly-connected-components-kosarajus-algo/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Return an integer count.</td>
      <td><b>Time:</b> O(V + E)<br><b>Space:</b> O(V + E)</td>
      <td>Kosaraju's Algo: 1) Sort nodes by finish time (Topo Sort DFS). 2) Transpose the graph (reverse edges). 3) DFS on transposed graph in order of finish time.<br><br><b>Dependencies:</b> <code>#include <stack></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def kosaraju(V: int, adj: List[List[int]]) -&gt; int:&#10;    vis = [0] * V&#10;    st = []&#10;    def dfs(node):&#10;        vis[node] = 1&#10;        for it in adj[node]:&#10;            if not vis[it]: dfs(it)&#10;        st.append(node)&#10;    for i in range(V):&#10;        if not vis[i]: dfs(i)&#10;    adjT = [[] for _ in range(V)]&#10;    for i in range(V):&#10;        vis[i] = 0&#10;        for it in adj[i]: adjT[it].append(i)&#10;    def dfs3(node):&#10;        vis[node] = 1&#10;        for it in adjT[node]:&#10;            if not vis[it]: dfs3(it)&#10;    scc = 0&#10;    while st:&#10;        node = st.pop()&#10;        if not vis[node]:&#10;            scc += 1; dfs3(node)&#10;    return scc</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">10</td>
      <td rowspan="1">Graph 10 Detect Cycle Directed BFS<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Return true if cycle exists.</td>
      <td><b>Time:</b> O(V + E)<br><b>Space:</b> O(V)</td>
      <td>A DAG has a topological sort of exactly V elements. Use Kahn's BFS. If the number of elements pulled from the queue is < V, there's a cycle.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isCyclic(V: int, adj: List[List[int]]) -&gt; bool:&#10;    indegree = [0] * V&#10;    for i in range(V):&#10;        for it in adj[i]: indegree[it] += 1&#10;    q = [i for i in range(V) if indegree[i] == 0]&#10;    cnt = 0&#10;    while q:&#10;        node = q.pop(0)&#10;        cnt += 1&#10;        for it in adj[node]:&#10;            indegree[it] -= 1&#10;            if indegree[it] == 0: q.append(it)&#10;    return cnt != V</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">11</td>
      <td rowspan="1">Graph 11 Bipartite Graph DFS<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/bipartite-graph/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Return true/false.</td>
      <td><b>Time:</b> O(V + E)<br><b>Space:</b> O(V)</td>
      <td>DFS. Color nodes with 0 and 1. If an adjacent node is uncolored, assign the opposite color and recurse. If it's colored and has the same color, it's not bipartite.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isBipartite(V: int, adj: List[List[int]]) -&gt; bool:&#10;    color = [-1] * V&#10;    def dfs(node, col):&#10;        color[node] = col&#10;        for it in adj[node]:&#10;            if color[it] == -1:&#10;                if not dfs(it, 1 - col): return False&#10;            elif color[it] == col:&#10;                return False&#10;        return True&#10;    for i in range(V):&#10;        if color[i] == -1:&#10;            if not dfs(i, 0): return False&#10;    return True</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">12</td>
      <td rowspan="1">Graph 12 Alien Dictionary<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/alien-dictionary/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> words = ['baa', 'abcd', 'abca', 'cab', 'cad'], K = 4<br><b>Output:</b> 'bdac'</td>
      <td><b>Time:</b> O(N * Len + K + E)<br><b>Space:</b> O(K + E)</td>
      <td>Create a DAG based on mismatching characters between adjacent words. Use Kahn's algorithm (Topological Sort BFS) to find the character order.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findOrder(dict: List[str], N: int, K: int) -&gt; str:&#10;    adj = [[] for _ in range(K)]&#10;    for i in range(N - 1):&#10;        s1, s2 = dict[i], dict[i+1]&#10;        for j in range(min(len(s1), len(s2))):&#10;            if s1[j] != s2[j]:&#10;                adj[ord(s1[j]) - ord(&#x27;a&#x27;)].append(ord(s2[j]) - ord(&#x27;a&#x27;))&#10;                break&#10;    indegree = [0] * K&#10;    for i in range(K):&#10;        for it in adj[i]: indegree[it] += 1&#10;    q = [i for i in range(K) if indegree[i] == 0]&#10;    topo = []&#10;    while q:&#10;        node = q.pop(0)&#10;        topo.append(chr(node + ord(&#x27;a&#x27;)))&#10;        for it in adj[node]:&#10;            indegree[it] -= 1&#10;            if indegree[it] == 0: q.append(it)&#10;    return &#x27;&#x27;.join(topo)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">13</td>
      <td rowspan="1">Graph 13 Shortest Path In Directed Acyclic Graph<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Topo Sort.</td>
      <td><b>Time:</b> O(V + E)<br><b>Space:</b> O(V + E)</td>
      <td>Perform Topological Sort. Then iterate through the topologically sorted vertices. For each vertex `u`, relax its neighbors: `dist[v] = min(dist[v], dist[u] + weight)`. Return `dist` array.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def shortestPath(N: int, M: int, edges: List[List[int]]) -&gt; List[int]:&#10;    adj = [[] for _ in range(N)]&#10;    for u, v, wt in edges:&#10;        adj[u].append((v, wt))&#10;    vis = [0] * N&#10;    st = []&#10;    def topoSort(node):&#10;        vis[node] = 1&#10;        for v, wt in adj[node]:&#10;            if not vis[v]: topoSort(v)&#10;        st.append(node)&#10;    for i in range(N):&#10;        if not vis[i]: topoSort(i)&#10;    dist = [1e9] * N&#10;    dist[0] = 0&#10;    while st:&#10;        node = st.pop()&#10;        if dist[node] != 1e9:&#10;            for v, wt in adj[node]:&#10;                if dist[node] + wt &lt; dist[v]:&#10;                    dist[v] = dist[node] + wt&#10;    return [d if d != 1e9 else -1 for d in dist]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">14</td>
      <td rowspan="1">Graph 14 Shortest Path In Undirected Graph With Unit Distance<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/shortest-path-in-undirected-graph-having-unit-distance/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> BFS approach.</td>
      <td><b>Time:</b> O(V + E)<br><b>Space:</b> O(V + E)</td>
      <td>Standard BFS starting from source. Distance of neighbors is `dist[u] + 1`.<br><br><b>Dependencies:</b> <code>#include <queue></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def shortestPath(edges: List[List[int]], n: int, m: int, src: int) -&gt; List[int]:&#10;    adj = [[] for _ in range(n)]&#10;    for u, v in edges:&#10;        adj[u].append(v)&#10;        adj[v].append(u)&#10;    dist = [1e9] * n&#10;    dist[src] = 0&#10;    q = collections.deque([src])&#10;    while q:&#10;        node = q.popleft()&#10;        for neighbor in adj[node]:&#10;            if dist[node] + 1 &lt; dist[neighbor]:&#10;                dist[neighbor] = dist[node] + 1&#10;                q.append(neighbor)&#10;    return [d if d != 1e9 else -1 for d in dist]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">15</td>
      <td rowspan="1">Graph 15 Bridges In Graph<br><br></b> <a href="https://leetcode.com/problems/critical-connections-in-a-network/" target="_blank">LeetCode 1192</a></td>
      <td rowspan="1"><b>Example 1:</b> Tarjan's algorithm.</td>
      <td><b>Time:</b> O(V + E)<br><b>Space:</b> O(V + E)</td>
      <td>Tarjan's algorithm. Maintain `tin` (time of insertion) and `low` (lowest time reachable). If `low[neighbor] > tin[node]`, the edge `(node, neighbor)` is a bridge. Update `low[node] = min(low[node], low[neighbor])`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def criticalConnections(n: int, connections: List[List[int]]) -&gt; List[List[int]]:&#10;    adj = [[] for _ in range(n)]&#10;    for u, v in connections:&#10;        adj[u].append(v)&#10;        adj[v].append(u)&#10;    vis = [0] * n&#10;    tin, low = [0] * n, [0] * n&#10;    bridges = []&#10;    timer = 1&#10;    def dfs(node, parent):&#10;        nonlocal timer&#10;        vis[node] = 1&#10;        tin[node] = low[node] = timer&#10;        timer += 1&#10;        for neighbor in adj[node]:&#10;            if neighbor == parent: continue&#10;            if not vis[neighbor]:&#10;                dfs(neighbor, node)&#10;                low[node] = min(low[node], low[neighbor])&#10;                if low[neighbor] &gt; tin[node]:&#10;                    bridges.append([node, neighbor])&#10;            else:&#10;                low[node] = min(low[node], low[neighbor])&#10;    dfs(0, -1)&#10;    return bridges</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">16</td>
      <td rowspan="1">Graph 16 Articulation Point I<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/articulation-point-1/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Tarjan's algorithm with discovery times.</td>
      <td><b>Time:</b> O(V + E)<br><b>Space:</b> O(V)</td>
      <td>Maintain `tin` (insertion time) and `low` (lowest insertion time reachable). A node `u` is an articulation point if `low[v] >= tin[u]` (and it's not root). If root, it's an articulation point if it has >1 children in DFS tree.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class Solution:&#10;    def __init__(self):&#10;        self.timer = 0&#10;    def dfs(self, node, parent, vis, tin, low, mark, adj):&#10;        vis[node] = 1&#10;        tin[node] = low[node] = self.timer&#10;        self.timer += 1&#10;        child = 0&#10;        for it in adj[node]:&#10;            if it == parent: continue&#10;            if not vis[it]:&#10;                self.dfs(it, node, vis, tin, low, mark, adj)&#10;                low[node] = min(low[node], low[it])&#10;                if low[it] &gt;= tin[node] and parent != -1:&#10;                    mark[node] = 1&#10;                child += 1&#10;            else:&#10;                low[node] = min(low[node], tin[it])&#10;        if child &gt; 1 and parent == -1:&#10;            mark[node] = 1&#10;    def articulationPoints(self, V, adj):&#10;        vis = [0] * V&#10;        tin = [0] * V&#10;        low = [0] * V&#10;        mark = [0] * V&#10;        for i in range(V):&#10;            if not vis[i]:&#10;                self.dfs(i, -1, vis, tin, low, mark, adj)&#10;        ans = []&#10;        for i in range(V):&#10;            if mark[i] == 1: ans.append(i)&#10;        if len(ans) == 0: return [-1]&#10;        return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">17</td>
      <td rowspan="1">Graph 17 Number Of Provinces Dsu<br><br></b> <a href="https://leetcode.com/problems/number-of-provinces/" target="_blank">LeetCode 547</a></td>
      <td rowspan="1"><b>Example 1:</b> Connect elements, count unique parents.</td>
      <td><b>Time:</b> O(N^2 * alpha(N))<br><b>Space:</b> O(N)</td>
      <td>Create DSU of size `n`. For every edge in `isConnected`, union the two nodes. The number of provinces is the number of nodes where `find(i) == i`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class DisjointSet:&#10;    def __init__(self, n):&#10;        self.parent = list(range(n + 1))&#10;        self.size = [1] * (n + 1)&#10;    def findUPar(self, node):&#10;        if node == self.parent[node]:&#10;            return node&#10;        self.parent[node] = self.findUPar(self.parent[node])&#10;        return self.parent[node]&#10;    def unionBySize(self, u, v):&#10;        ulp_u = self.findUPar(u)&#10;        ulp_v = self.findUPar(v)&#10;        if ulp_u == ulp_v: return&#10;        if self.size[ulp_u] &lt; self.size[ulp_v]:&#10;            self.parent[ulp_u] = ulp_v&#10;            self.size[ulp_v] += self.size[ulp_u]&#10;        else:&#10;            self.parent[ulp_v] = ulp_u&#10;            self.size[ulp_u] += self.size[ulp_v]&#10;def findCircleNum(isConnected: List[List[int]]) -&gt; int:&#10;    n = len(isConnected)&#10;    ds = DisjointSet(n)&#10;    for i in range(n):&#10;        for j in range(n):&#10;            if isConnected[i][j] == 1:&#10;                ds.unionBySize(i, j)&#10;    cnt = 0&#10;    for i in range(n):&#10;        if ds.findUPar(i) == i:&#10;            cnt += 1&#10;    return cnt</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">18</td>
      <td rowspan="1">Graph 18 Accounts Merge<br><br></b> <a href="https://leetcode.com/problems/accounts-merge/" target="_blank">LeetCode 721</a></td>
      <td rowspan="1"><b>Example 1:</b> DSU on accounts using emails.</td>
      <td><b>Time:</b> O(N log N * alpha(N)) where N is total emails<br><b>Space:</b> O(N)</td>
      <td>Map each email to an account index. If an email is seen again, union the current account index with the previously mapped account index. Finally, group emails by their root account index, sort them, and attach the name.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def accountsMerge(accounts: List[List[str]]) -&gt; List[List[str]]:&#10;    n = len(accounts)&#10;    parent = list(range(n))&#10;    def find(i):&#10;        if parent[i] == i: return i&#10;        parent[i] = find(parent[i])&#10;        return parent[i]&#10;    def union(i, j):&#10;        root_i, root_j = find(i), find(j)&#10;        if root_i != root_j: parent[root_i] = root_j&#10;    email_to_id = {}&#10;    for i, acc in enumerate(accounts):&#10;        for email in acc[1:]:&#10;            if email in email_to_id:&#10;                union(i, email_to_id[email])&#10;            else:&#10;                email_to_id[email] = i&#10;    id_to_emails = collections.defaultdict(list)&#10;    for email, i in email_to_id.items():&#10;        id_to_emails[find(i)].append(email)&#10;    ans = []&#10;    for i, emails in id_to_emails.items():&#10;        ans.append([accounts[i][0]] + sorted(emails))&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">19</td>
      <td rowspan="1">Graph 19 Number Of Operations To Make Network Connected<br><br></b> <a href="https://leetcode.com/problems/number-of-operations-to-make-network-connected/" target="_blank">LeetCode 1319</a></td>
      <td rowspan="1"><b>Example 1:</b> Extra edges and connected components.</td>
      <td><b>Time:</b> O(E * alpha(N))<br><b>Space:</b> O(N)</td>
      <td>If total edges < n - 1, impossible. Use DSU to count number of connected components `C` and number of extra edges `E`. An edge is extra if `find(u) == find(v)`. We need `C - 1` edges to connect `C` components. Since total edges >= n - 1, we guaranteed have enough extra edges. Answer is `C - 1`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def makeConnected(n: int, connections: List[List[int]]) -&gt; int:&#10;    if len(connections) &lt; n - 1: return -1&#10;    parent = list(range(n))&#10;    def find(i):&#10;        if parent[i] == i: return i&#10;        parent[i] = find(parent[i])&#10;        return parent[i]&#10;    components = n&#10;    for u, v in connections:&#10;        root_u, root_v = find(u), find(v)&#10;        if root_u != root_v:&#10;            parent[root_u] = root_v&#10;            components -= 1&#10;    return components - 1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">20</td>
      <td rowspan="1">Graph 20 Most Stones Removed With Same Row Or Column<br><br></b> <a href="https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/" target="_blank">LeetCode 947</a></td>
      <td rowspan="1"><b>Example 1:</b> Treat rows and columns as nodes.</td>
      <td><b>Time:</b> O(N * alpha(N))<br><b>Space:</b> O(N)</td>
      <td>Imagine rows and columns are nodes in a bipartite graph. A stone at `(r, c)` connects row `r` and column `c`. The answer is `total_stones - number_of_connected_components`. We can map cols to `col + 10001` to use a single DSU.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def removeStones(stones: List[List[int]]) -&gt; int:&#10;    parent = {}&#10;    components = [0]&#10;    def find(i):&#10;        if i not in parent:&#10;            parent[i] = i&#10;            components[0] += 1&#10;        if parent[i] == i: return i&#10;        parent[i] = find(parent[i])&#10;        return parent[i]&#10;    def union(i, j):&#10;        root_i, root_j = find(i), find(j)&#10;        if root_i != root_j:&#10;            parent[root_i] = root_j&#10;            components[0] -= 1&#10;    for r, c in stones:&#10;        union(r, ~c)&#10;    return len(stones) - components[0]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">21</td>
      <td rowspan="1">Graph 21 Making A Large Island<br><br></b> <a href="https://leetcode.com/problems/making-a-large-island/" target="_blank">LeetCode 827</a></td>
      <td rowspan="1"><b>Example 1:</b> Component sizes with DSU.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N^2)</td>
      <td>Step 1: Use DSU to connect all adjacent 1s and calculate the size of each component. Step 2: For each 0, check its 4 neighbors. Find the unique roots of those neighbors. The potential new island size is `1 + sum(size[root])` for each unique root. Find max potential size. Handle case where matrix is all 1s.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def largestIsland(grid: List[List[int]]) -&gt; int:&#10;    n = len(grid)&#10;    parent = list(range(n * n))&#10;    size = [1] * (n * n)&#10;    def find(i):&#10;        if parent[i] == i: return i&#10;        parent[i] = find(parent[i])&#10;        return parent[i]&#10;    def union(i, j):&#10;        root_i, root_j = find(i), find(j)&#10;        if root_i != root_j:&#10;            if size[root_i] &lt; size[root_j]:&#10;                parent[root_i] = root_j&#10;                size[root_j] += size[root_i]&#10;            else:&#10;                parent[root_j] = root_i&#10;                size[root_i] += size[root_j]&#10;    dirs = [(-1,0), (1,0), (0,-1), (0,1)]&#10;    for r in range(n):&#10;        for c in range(n):&#10;            if grid[r][c] == 1:&#10;                for dr, dc in dirs:&#10;                    nr, nc = r + dr, c + dc&#10;                    if 0 &lt;= nr &lt; n and 0 &lt;= nc &lt; n and grid[nr][nc] == 1:&#10;                        union(r * n + c, nr * n + nc)&#10;    mx = 0&#10;    for r in range(n):&#10;        for c in range(n):&#10;            if grid[r][c] == 0:&#10;                components = set()&#10;                for dr, dc in dirs:&#10;                    nr, nc = r + dr, c + dc&#10;                    if 0 &lt;= nr &lt; n and 0 &lt;= nc &lt; n and grid[nr][nc] == 1:&#10;                        components.add(find(nr * n + nc))&#10;                mx = max(mx, 1 + sum(size[comp] for comp in components))&#10;    return mx if mx &gt; 0 else n * n</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">22</td>
      <td rowspan="1">Graph 22 Swim In Rising Water<br><br></b> <a href="https://leetcode.com/problems/swim-in-rising-water/" target="_blank">LeetCode 778</a></td>
      <td rowspan="1"><b>Example 1:</b> Dijkstra-like or Binary Search + BFS.</td>
      <td><b>Time:</b> O(N^2 log N)<br><b>Space:</b> O(N^2)</td>
      <td>Use a priority queue (Dijkstra variant). The cost to reach a cell is `max(cost_of_previous_cell, grid[r][c])`. Extract min cost cell, relax neighbors.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def swimInWater(grid: List[List[int]]) -&gt; int:&#10;    n = len(grid)&#10;    pq = [(grid[0][0], 0, 0)]&#10;    dist = [[float(&#x27;inf&#x27;)] * n for _ in range(n)]&#10;    dist[0][0] = grid[0][0]&#10;    dirs = [(-1,0), (1,0), (0,-1), (0,1)]&#10;    while pq:&#10;        d, r, c = heapq.heappop(pq)&#10;        if r == n - 1 and c == n - 1: return d&#10;        for dr, dc in dirs:&#10;            nr, nc = r + dr, c + dc&#10;            if 0 &lt;= nr &lt; n and 0 &lt;= nc &lt; n:&#10;                next_d = max(d, grid[nr][nc])&#10;                if next_d &lt; dist[nr][nc]:&#10;                    dist[nr][nc] = next_d&#10;                    heapq.heappush(pq, (next_d, nr, nc))&#10;    return 0</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">23</td>
      <td rowspan="1">Graph 23 Word Ladder I<br><br></b> <a href="https://leetcode.com/problems/word-ladder/" target="_blank">LeetCode 127</a></td>
      <td rowspan="1"><b>Example 1:</b> BFS level by level.</td>
      <td><b>Time:</b> O(N * M * 26) where N is words, M is word length<br><b>Space:</b> O(N)</td>
      <td>BFS. Start from `beginWord`. In each step, change one character from 'a' to 'z' and check if new word is in `wordList`. If yes, push to queue, erase from `wordList` to avoid loops, and continue. Track level/steps.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -&gt; int:&#10;    wordSet = set(wordList)&#10;    if endWord not in wordSet: return 0&#10;    q = collections.deque([(beginWord, 1)])&#10;    if beginWord in wordSet: wordSet.remove(beginWord)&#10;    while q:&#10;        word, steps = q.popleft()&#10;        if word == endWord: return steps&#10;        for i in range(len(word)):&#10;            for c in &#x27;abcdefghijklmnopqrstuvwxyz&#x27;:&#10;                newWord = word[:i] + c + word[i+1:]&#10;                if newWord in wordSet:&#10;                    wordSet.remove(newWord)&#10;                    q.append((newWord, steps + 1))&#10;    return 0</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">24</td>
      <td rowspan="1">Graph 24 Word Ladder II<br><br></b> <a href="https://leetcode.com/problems/word-ladder-ii/" target="_blank">LeetCode 126</a></td>
      <td rowspan="1"><b>Example 1:</b> BFS for distance, DFS for paths.</td>
      <td><b>Time:</b> O(V + E + Paths)<br><b>Space:</b> O(V + E)</td>
      <td>BFS to find minimum steps to reach each word. Then DFS starting from `endWord` backwards to `beginWord`, only exploring paths where `dist[next_word] == dist[curr_word] - 1`. Reverse the built paths.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def findLadders(beginWord: str, endWord: str, wordList: List[str]) -&gt; List[List[str]]:&#10;    wordSet = set(wordList)&#10;    if endWord not in wordSet: return []&#10;    q = collections.deque([beginWord])&#10;    mpp = {beginWord: 1}&#10;    wordSet.discard(beginWord)&#10;    while q:&#10;        word = q.popleft()&#10;        if word == endWord: break&#10;        steps = mpp[word]&#10;        for i in range(len(word)):&#10;            for c in &#x27;abcdefghijklmnopqrstuvwxyz&#x27;:&#10;                newWord = word[:i] + c + word[i+1:]&#10;                if newWord in wordSet:&#10;                    mpp[newWord] = steps + 1&#10;                    q.append(newWord)&#10;                    wordSet.remove(newWord)&#10;    ans = []&#10;    if endWord in mpp:&#10;        def dfs(word, seq):&#10;            if word == beginWord:&#10;                ans.append(seq[::-1])&#10;                return&#10;            steps = mpp[word]&#10;            for i in range(len(word)):&#10;                for c in &#x27;abcdefghijklmnopqrstuvwxyz&#x27;:&#10;                    newWord = word[:i] + c + word[i+1:]&#10;                    if newWord in mpp and mpp[newWord] + 1 == steps:&#10;                        seq.append(newWord)&#10;                        dfs(newWord, seq)&#10;                        seq.pop()&#10;        dfs(endWord, [endWord])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">25</td>
      <td rowspan="1">Graph 25 Network Delay Time<br><br></b> <a href="https://leetcode.com/problems/network-delay-time/" target="_blank">LeetCode 743</a></td>
      <td rowspan="1"><b>Example 1:</b> Dijkstra's to find max shortest path.</td>
      <td><b>Time:</b> O(E log V)<br><b>Space:</b> O(V + E)</td>
      <td>Standard Dijkstra's shortest path from node `k`. Return the maximum value in the distances array. If any node remains unvisited (dist == inf), return -1.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def networkDelayTime(times: List[List[int]], n: int, k: int) -&gt; int:&#10;    adj = collections.defaultdict(list)&#10;    for u, v, w in times:&#10;        adj[u].append((v, w))&#10;    pq = [(0, k)]&#10;    dist = {i: float(&#x27;inf&#x27;) for i in range(1, n + 1)}&#10;    dist[k] = 0&#10;    while pq:&#10;        time, node = heapq.heappop(pq)&#10;        if time &gt; dist[node]: continue&#10;        for adjNode, wt in adj[node]:&#10;            if time + wt &lt; dist[adjNode]:&#10;                dist[adjNode] = time + wt&#10;                heapq.heappush(pq, (time + wt, adjNode))&#10;    mx = max(dist.values())&#10;    return mx if mx != float(&#x27;inf&#x27;) else -1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">26</td>
      <td rowspan="1">Graph 26 Cheapest Flights Within K Stops<br><br></b> <a href="https://leetcode.com/problems/cheapest-flights-within-k-stops/" target="_blank">LeetCode 787</a></td>
      <td rowspan="1"><b>Example 1:</b> Dijkstra's with Stops / BFS.</td>
      <td><b>Time:</b> O(E)<br><b>Space:</b> O(N + E)</td>
      <td>Use a queue storing `(stops, node, cost)`. We don't need a priority queue because stops increase uniformly by 1. Distance array stores min cost to reach each node. Only push to queue if new cost is cheaper. If `stops > k`, skip.<br><br><b>Dependencies:</b> <code>#include <queue></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -&gt; int:&#10;    adj = collections.defaultdict(list)&#10;    for u, v, w in flights:&#10;        adj[u].append((v, w))&#10;    q = collections.deque([(0, src, 0)]) # stops, node, cost&#10;    dist = [float(&#x27;inf&#x27;)] * n&#10;    dist[src] = 0&#10;    while q:&#10;        stops, node, cost = q.popleft()&#10;        if stops &gt; k: continue&#10;        for nxt, weight in adj[node]:&#10;            if cost + weight &lt; dist[nxt] and stops &lt;= k:&#10;                dist[nxt] = cost + weight&#10;                q.append((stops + 1, nxt, cost + weight))&#10;    return dist[dst] if dist[dst] != float(&#x27;inf&#x27;) else -1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">27</td>
      <td rowspan="1">Graph 27 Minimum Multiplications To Reach End<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/minimum-multiplications-to-reach-end/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> BFS / Dijkstra's with unit weights.</td>
      <td><b>Time:</b> O(100000 * N)<br><b>Space:</b> O(100000)</td>
      <td>Since each multiplication is 1 step, we can use BFS. The 'nodes' are values from 0 to 99999. Use an array `dist` initialized to infinity. Push `start` to queue. For each popped node, multiply by all array elements `% 100000`. If we find a shorter path, push to queue.<br><br><b>Dependencies:</b> <code>#include <queue></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def minimumMultiplications(arr: List[int], start: int, end: int) -&gt; int:&#10;    if start == end: return 0&#10;    q = collections.deque([(start, 0)])&#10;    dist = [float(&#x27;inf&#x27;)] * 100000&#10;    dist[start] = 0&#10;    mod = 100000&#10;    while q:&#10;        node, steps = q.popleft()&#10;        for it in arr:&#10;            num = (node * it) % mod&#10;            if steps + 1 &lt; dist[num]:&#10;                dist[num] = steps + 1&#10;                if num == end: return steps + 1&#10;                q.append((num, steps + 1))&#10;    return -1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">28</td>
      <td rowspan="1">Graph 28 Number Of Ways To Arrive At Destination<br><br></b> <a href="https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/" target="_blank">LeetCode 1976</a></td>
      <td rowspan="1"><b>Example 1:</b> Dijkstra's with Ways Count.</td>
      <td><b>Time:</b> O(E log V)<br><b>Space:</b> O(V + E)</td>
      <td>Modify Dijkstra's. Keep `dist` array and `ways` array. When relaxing an edge: if `curr_dist + weight < dist[neighbor]`, update `dist`, push to PQ, and `ways[neighbor] = ways[curr_node]`. If `curr_dist + weight == dist[neighbor]`, `ways[neighbor] = (ways[neighbor] + ways[curr_node]) % MOD`.<br><br><b>Dependencies:</b> <code>#include <queue></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections, heapq&#10;def countPaths(n: int, roads: List[List[int]]) -&gt; int:&#10;    adj = collections.defaultdict(list)&#10;    for u, v, w in roads:&#10;        adj[u].append((v, w))&#10;        adj[v].append((u, w))&#10;    heap = [(0, 0)]&#10;    dist = [float(&#x27;inf&#x27;)] * n&#10;    ways = [0] * n&#10;    dist[0] = 0&#10;    ways[0] = 1&#10;    mod = 10**9 + 7&#10;    while heap:&#10;        d, node = heapq.heappop(heap)&#10;        if d &gt; dist[node]: continue&#10;        for nxt, weight in adj[node]:&#10;            if d + weight &lt; dist[nxt]:&#10;                dist[nxt] = d + weight&#10;                ways[nxt] = ways[node]&#10;                heapq.heappush(heap, (dist[nxt], nxt))&#10;            elif d + weight == dist[nxt]:&#10;                ways[nxt] = (ways[nxt] + ways[node]) % mod&#10;    return ways[n-1]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">29</td>
      <td rowspan="1">Graph 29 Find The City With The Smallest Number Of Neighbors At A Threshold Distance<br><br></b> <a href="https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/" target="_blank">LeetCode 1334</a></td>
      <td rowspan="1"><b>Example 1:</b> Floyd-Warshall Algorithm.</td>
      <td><b>Time:</b> O(V^3)<br><b>Space:</b> O(V^2)</td>
      <td>Use Floyd-Warshall to find shortest paths between all pairs of nodes. For each city, count the number of reachable cities within `distanceThreshold`. Return the city with the minimum count (and greatest ID on tie).</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findTheCity(n: int, edges: List[List[int]], distanceThreshold: int) -&gt; int:&#10;    dist = [[float(&#x27;inf&#x27;)] * n for _ in range(n)]&#10;    for i in range(n): dist[i][i] = 0&#10;    for u, v, w in edges:&#10;        dist[u][v] = w&#10;        dist[v][u] = w&#10;    for k in range(n):&#10;        for i in range(n):&#10;            for j in range(n):&#10;                if dist[i][k] != float(&#x27;inf&#x27;) and dist[k][j] != float(&#x27;inf&#x27;):&#10;                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])&#10;    minCities = n&#10;    ansCity = -1&#10;    for i in range(n):&#10;        cnt = sum(1 for j in range(n) if dist[i][j] &lt;= distanceThreshold)&#10;        if cnt &lt;= minCities:&#10;            minCities = cnt&#10;            ansCity = i&#10;    return ansCity</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">30</td>
      <td rowspan="1">Graph 30 Find Eventual Safe States<br><br></b> <a href="https://leetcode.com/problems/find-eventual-safe-states/" target="_blank">LeetCode 802</a></td>
      <td rowspan="1"><b>Example 1:</b> Topological Sort using Kahn's Algorithm on reversed graph.</td>
      <td><b>Time:</b> O(V + E)<br><b>Space:</b> O(V + E)</td>
      <td>Reverse all edges in the graph. Terminal nodes become sources (indegree 0). Run Kahn's algorithm (BFS topological sort). Any node processed is part of a path that only leads to terminal nodes (safe node). Sort the resulting nodes.<br><br><b>Dependencies:</b> <code>#include <queue></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def eventualSafeNodes(graph: List[List[int]]) -&gt; List[int]:&#10;    V = len(graph)&#10;    adjRev = [[] for _ in range(V)]&#10;    indegree = [0] * V&#10;    for i in range(V):&#10;        for neighbor in graph[i]:&#10;            adjRev[neighbor].append(i)&#10;            indegree[i] += 1&#10;    q = collections.deque([i for i in range(V) if indegree[i] == 0])&#10;    safeNodes = []&#10;    while q:&#10;        node = q.popleft()&#10;        safeNodes.append(node)&#10;        for neighbor in adjRev[node]:&#10;            indegree[neighbor] -= 1&#10;            if indegree[neighbor] == 0:&#10;                q.append(neighbor)&#10;    return sorted(safeNodes)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">31</td>
      <td rowspan="1">Graph 31 As Far From Land As Possible<br><br></b> <a href="https://leetcode.com/problems/as-far-from-land-as-possible/" target="_blank">LeetCode 1162</a></td>
      <td rowspan="1"><b>Example 1:</b> Multi-source BFS.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N^2)</td>
      <td>Push all land cells (1s) into a queue and mark them as visited. Perform BFS outward. The last water cell processed gives the maximum distance. Track layers/steps during BFS.<br><br><b>Dependencies:</b> <code>#include <queue></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def maxDistance(grid: List[List[int]]) -&gt; int:&#10;    n = len(grid)&#10;    q = collections.deque()&#10;    for i in range(n):&#10;        for j in range(n):&#10;            if grid[i][j] == 1: q.append((i, j))&#10;    if not q or len(q) == n * n: return -1&#10;    dist = -1&#10;    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]&#10;    while q:&#10;        for _ in range(len(q)):&#10;            r, c = q.popleft()&#10;            for i in range(4):&#10;                nr, nc = r + dr[i], c + dc[i]&#10;                if 0 &lt;= nr &lt; n and 0 &lt;= nc &lt; n and grid[nr][nc] == 0:&#10;                    grid[nr][nc] = 1&#10;                    q.append((nr, nc))&#10;        dist += 1&#10;    return dist</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">32</td>
      <td rowspan="1">Graph 32 Find Closest Node To Given Two Nodes<br><br></b> <a href="https://leetcode.com/problems/find-closest-node-to-given-two-nodes/" target="_blank">LeetCode 2359</a></td>
      <td rowspan="1"><b>Example 1:</b> Two BFS traversals.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Run BFS from `node1` to get `dist1` array, and BFS from `node2` to get `dist2` array. Then iterate through all nodes `0` to `n-1`. For nodes reachable from both, compute `max(dist1[i], dist2[i])`. Return the node that minimizes this maximum distance. On tie, return the smallest index.<br><br><b>Dependencies:</b> <code>#include <queue></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def closestMeetingNode(edges: List[int], node1: int, node2: int) -&gt; int:&#10;    def bfs(start):&#10;        dist = [float(&#x27;inf&#x27;)] * len(edges)&#10;        q = collections.deque([start])&#10;        dist[start] = 0&#10;        while q:&#10;            node = q.popleft()&#10;            nxt = edges[node]&#10;            if nxt != -1 and dist[nxt] == float(&#x27;inf&#x27;):&#10;                dist[nxt] = dist[node] + 1&#10;                q.append(nxt)&#10;        return dist&#10;    d1, d2 = bfs(node1), bfs(node2)&#10;    min_dist, ans = float(&#x27;inf&#x27;), -1&#10;    for i in range(len(edges)):&#10;        if d1[i] != float(&#x27;inf&#x27;) and d2[i] != float(&#x27;inf&#x27;):&#10;            mx = max(d1[i], d2[i])&#10;            if mx &lt; min_dist:&#10;                min_dist = mx&#10;                ans = i&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">33</td>
      <td rowspan="1">Graph 33 Minimum Score Of A Path Between Two Cities<br><br></b> <a href="https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/" target="_blank">LeetCode 2492</a></td>
      <td rowspan="1"><b>Example 1:</b> BFS / DSU to find min edge in component.</td>
      <td><b>Time:</b> O(V + E)<br><b>Space:</b> O(V + E)</td>
      <td>Since a path can revisit nodes and edges, the minimum score path from 1 to `n` is simply the minimum weight edge in the connected component containing node 1 and `n`. Perform BFS/DFS from node 1 and find the minimum edge weight in the entire component.<br><br><b>Dependencies:</b> <code>#include <queue></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def minScore(n: int, roads: List[List[int]]) -&gt; int:&#10;    adj = collections.defaultdict(list)&#10;    for u, v, w in roads:&#10;        adj[u].append((v, w))&#10;        adj[v].append((u, w))&#10;    q = collections.deque([1])&#10;    vis = set([1])&#10;    min_score = float(&#x27;inf&#x27;)&#10;    while q:&#10;        node = q.popleft()&#10;        for nxt, wt in adj[node]:&#10;            min_score = min(min_score, wt)&#10;            if nxt not in vis:&#10;                vis.add(nxt)&#10;                q.append(nxt)&#10;    return min_score</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">34</td>
      <td rowspan="1">Graph 34 Shortest Bridge<br><br></b> <a href="https://leetcode.com/problems/shortest-bridge/" target="_blank">LeetCode 934</a></td>
      <td rowspan="1"><b>Example 1:</b> DFS + BFS.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N^2)</td>
      <td>Step 1: Use DFS to find the first island. Mark all its cells (e.g., set to 2) and push them into a queue for BFS. Step 2: Perform multi-source BFS from the queue. Expand the island level by level. The first time we hit a `1` (which belongs to the second island), the number of layers expanded is the shortest bridge.<br><br><b>Dependencies:</b> <code>#include <queue></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def shortestBridge(grid: List[List[int]]) -&gt; int:&#10;    n = len(grid)&#10;    q = collections.deque()&#10;    def dfs(r, c):&#10;        grid[r][c] = 2&#10;        q.append((r, c))&#10;        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:&#10;            if 0 &lt;= nr &lt; n and 0 &lt;= nc &lt; n and grid[nr][nc] == 1:&#10;                dfs(nr, nc)&#10;    found = False&#10;    for i in range(n):&#10;        if found: break&#10;        for j in range(n):&#10;            if grid[i][j] == 1:&#10;                dfs(i, j)&#10;                found = True&#10;                break&#10;    steps = 0&#10;    while q:&#10;        for _ in range(len(q)):&#10;            r, c = q.popleft()&#10;            for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:&#10;                if 0 &lt;= nr &lt; n and 0 &lt;= nc &lt; n:&#10;                    if grid[nr][nc] == 1: return steps&#10;                    if grid[nr][nc] == 0:&#10;                        grid[nr][nc] = 2&#10;                        q.append((nr, nc))&#10;        steps += 1&#10;    return steps</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">35</td>
      <td rowspan="1">Graph 35 Minimum Time Taken By Each Job To Be Completed Given By A Directed Acyclic Graph<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/minimum-time-taken-by-each-job-to-be-completed-given-by-a-directed-acyclic-graph/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Modified Kahn's Algorithm.</td>
      <td><b>Time:</b> O(V + E)<br><b>Space:</b> O(V)</td>
      <td>Use Kahn's Algorithm. All nodes with indegree 0 take 1 unit of time. For other nodes `V`, when they are pushed to the queue from `U`, their time is `time[U] + 1`.<br><br><b>Dependencies:</b> Queue</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minimumTime(n: int, edges: List[List[int]], m: int) -&gt; List[int]:&#10;    adj = [[] for _ in range(n + 1)]&#10;    indegree = [0] * (n + 1)&#10;    for u, v in edges:&#10;        adj[u].append(v)&#10;        indegree[v] += 1&#10;    q = collections.deque()&#10;    ans = [0] * (n + 1)&#10;    for i in range(1, n + 1):&#10;        if indegree[i] == 0:&#10;            q.append(i)&#10;            ans[i] = 1&#10;    while q:&#10;        node = q.popleft()&#10;        for neighbor in adj[node]:&#10;            indegree[neighbor] -= 1&#10;            if indegree[neighbor] == 0:&#10;                ans[neighbor] = ans[node] + 1&#10;                q.append(neighbor)&#10;    return ans[1:]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">36</td>
      <td rowspan="1">Graph 36 Find The Number Of Islands<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/find-the-number-of-islands/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> DFS or BFS.</td>
      <td><b>Time:</b> O(N * M)<br><b>Space:</b> O(N * M) worst case stack</td>
      <td>Traverse the grid. When a '1' is found, increment island count and use DFS/BFS to mark all its 8-connected neighbors as '0' (or visited) to avoid recounting.</td>
      <td><b>Edge Cases:</b> Empty grid<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def numIslands(grid: List[List[str]]) -&gt; int:&#10;    if not grid: return 0&#10;    n, m = len(grid), len(grid[0])&#10;    def dfs(r, c):&#10;        grid[r][c] = &#x27;0&#x27;&#10;        for delrow in [-1, 0, 1]:&#10;            for delcol in [-1, 0, 1]:&#10;                nrow, ncol = r + delrow, c + delcol&#10;                if 0 &lt;= nrow &lt; n and 0 &lt;= ncol &lt; m and grid[nrow][ncol] == &#x27;1&#x27;:&#10;                    dfs(nrow, ncol)&#10;    count = 0&#10;    for i in range(n):&#10;        for j in range(m):&#10;            if grid[i][j] == &#x27;1&#x27;:&#10;                count += 1&#10;                dfs(i, j)&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">37</td>
      <td rowspan="1">Graph 37 Detect Negative Cycle In A Graph<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/negative-weight-cycle3504/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Bellman Ford variant.</td>
      <td><b>Time:</b> O(V * E)<br><b>Space:</b> O(V)</td>
      <td>Use Bellman Ford algorithm. Relax all edges V-1 times. Then relax one more time. If any shortest path distance updates in the V-th relaxation, it means there is a negative weight cycle.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isNegativeWeightCycle(n, edges):&#10;    dist = [1e8] * n&#10;    dist[0] = 0&#10;    for _ in range(n - 1):&#10;        for u, v, wt in edges:&#10;            if dist[u] != 1e8 and dist[u] + wt &lt; dist[v]:&#10;                dist[v] = dist[u] + wt&#10;    for u, v, wt in edges:&#10;        if dist[u] != 1e8 and dist[u] + wt &lt; dist[v]:&#10;            return 1&#10;    return 0</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">38</td>
      <td rowspan="1">Graph 38 Find Bridge In A Graph<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/bridge-edge-in-graph/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Tarjan's Algorithm / DFS.</td>
      <td><b>Time:</b> O(V + E)<br><b>Space:</b> O(V)</td>
      <td>Remove the given edge `(c, d)` from the graph. Then run a DFS/BFS from `c`. If `d` is not reachable from `c`, then `(c, d)` was a bridge.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isBridge(V, adj, c, d):&#10;    vis = [False] * V&#10;    def dfs(node):&#10;        vis[node] = True&#10;        for nbr in adj[node]:&#10;            if (node == c and nbr == d) or (node == d and nbr == c): continue&#10;            if not vis[nbr]: dfs(nbr)&#10;    dfs(c)&#10;    return 1 if not vis[d] else 0</code></pre></details></td>
    </tr>
  </tbody>
</table>


## Dynamic Programming

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
      <td rowspan="1">1</td>
      <td rowspan="1">DP 01 Climbing Stairs<br><br></b> <a href="https://leetcode.com/problems/climbing-stairs/" target="_blank">LeetCode 70</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> n = 3<br><b>Output:</b> 3 (1+1+1, 1+2, 2+1)</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1) (Constraint)</td>
      <td>Space Optimization (Bottom-Up): Since state `n` only depends on `n-1` and `n-2`, we only need two variables.</td>
      <td><b>Edge Cases:</b> <b>Variable Swapping:</b> `prev2` becomes `prev`, and `prev` becomes the new `curr`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def climbStairs(n: int) -&gt; int:&#10;    if n &lt;= 1: return 1&#10;    prev2, prev = 1, 1&#10;    for i in range(2, n + 1):&#10;        curr = prev + prev2&#10;        prev2, prev = prev, curr&#10;    return prev</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">2</td>
      <td rowspan="1">DP 02 Longest Common Subsequence<br><br></b> <a href="https://leetcode.com/problems/longest-common-subsequence/" target="_blank">LeetCode 1143</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> text1 = "abcde", text2 = "ace"<br><b>Output:</b> 3 ("ace")</td>
      <td><b>Time:</b> O(M * N) (Constraint)<br><b>Space:</b> O(M * N) (Trade-off)</td>
      <td>Tabulation (Bottom-Up). Use a 2D array where `dp[i][j]` represents the LCS of prefixes of length `i` and `j`.<br><br><b>Dependencies:</b> <code>std::max</code></td>
      <td><b>Edge Cases:</b> <b>1-Based Indexing:</b> Shifting indices by 1 prevents out-of-bounds checks and elegantly handles the 0-length prefix base case.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def longestCommonSubsequence(text1: str, text2: str) -&gt; int:&#10;    n, m = len(text1), len(text2)&#10;    dp = [[0] * (m + 1) for _ in range(n + 1)]&#10;    for i in range(1, n + 1):&#10;        for j in range(1, m + 1):&#10;            if text1[i - 1] == text2[j - 1]:&#10;                dp[i][j] = 1 + dp[i - 1][j - 1]&#10;            else:&#10;                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])&#10;    return dp[n][m]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">3</td>
      <td rowspan="1">DP 03 Coin Change<br><br></b> <a href="https://leetcode.com/problems/coin-change/" target="_blank">LeetCode 322</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> coins = [1,2,5], amount = 11<br><b>Output:</b> 3 (5+5+1)</td>
      <td><b>Time:</b> O(Amount * N)<br><b>Space:</b> O(Amount)</td>
      <td>Unbounded Knapsack. State `dp[i]` is the min coins needed to make amount `i`. `dp[i] = min(dp[i], 1 + dp[i - coin])`.<br><br><b>Dependencies:</b> <code>std::min</code></td>
      <td><b>Edge Cases:</b> <b>Initialization:</b> Fill array with `Amount + 1` (acting as infinity). If `dp[Amount]` remains `Amount + 1`, return `-1`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def coinChange(coins: list[int], amount: int) -&gt; int:&#10;    dp = [amount + 1] * (amount + 1)&#10;    dp[0] = 0&#10;    for i in range(1, amount + 1):&#10;        for coin in coins:&#10;            if i - coin &gt;= 0:&#10;                dp[i] = min(dp[i], 1 + dp[i - coin])&#10;    return dp[amount] if dp[amount] &lt;= amount else -1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">4</td>
      <td rowspan="1">DP 04 Longest Increasing Subsequence<br><br></b> <a href="https://leetcode.com/problems/longest-increasing-subsequence/" target="_blank">LeetCode 300</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> nums = [10,9,2,5,3,7,101,18]<br><b>Output:</b> 4 ([2,3,7,101])</td>
      <td><b>Time:</b> O(N log N) (Constraint)<br><b>Space:</b> O(N)</td>
      <td>Binary Search Patience Sorting method. Maintain a `temp` array. If current element is larger than `temp.back()`, append. Else, replace the first element >= current.<br><br><b>Dependencies:</b> <code>std::lower_bound</code> / <code>bisect_left</code></td>
      <td><b>Edge Cases:</b> <b>Temp Array:</b> `temp` does NOT store the actual LIS, but its length correctly represents the LIS length.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import bisect&#10;def lengthOfLIS(nums: list[int]) -&gt; int:&#10;    temp = []&#10;    for num in nums:&#10;        idx = bisect.bisect_left(temp, num)&#10;        if idx == len(temp):&#10;            temp.append(num)&#10;        else:&#10;            temp[idx] = num&#10;    return len(temp)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">5</td>
      <td rowspan="1">DP 05 House Robber<br><br></b> <a href="https://leetcode.com/problems/house-robber/" target="_blank">LeetCode 198</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> nums = [1,2,3,1]<br><b>Output:</b> 4 (Rob house 1 and 3)</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Space Optimized DP. Maintain two variables: `prev1` (max up to previous house) and `prev2` (max up to the house before previous). `curr = max(num + prev2, prev1)`.<br><br><b>Dependencies:</b> <code>std::max</code></td>
      <td><b>Edge Cases:</b> <b>Array length < 2:</b> Automatically handled if initialized properly and loop condition ensures no out-of-bounds.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def rob(nums: list[int]) -&gt; int:&#10;    prev1, prev2 = 0, 0&#10;    for num in nums:&#10;        curr = max(num + prev2, prev1)&#10;        prev2 = prev1&#10;        prev1 = curr&#10;    return prev1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">6</td>
      <td rowspan="1">DP 06 01 Knapsack<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> N=3, W=4, values[]={1,2,3}, weight[]={4,5,1}<br><b>Output:</b> 3</td>
      <td><b>Time:</b> O(N * W)<br><b>Space:</b> O(W)</td>
      <td>2D DP or 1D array space-optimized DP. Check take and not-take scenarios.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def knapSack(W: int, wt: List[int], val: List[int], n: int) -&gt; int:&#10;    prev = [0] * (W + 1)&#10;    for w in range(wt[0], W + 1): prev[w] = val[0]&#10;    for ind in range(1, n):&#10;        for w in range(W, -1, -1):&#10;            notTake = prev[w]&#10;            take = float(&#x27;-inf&#x27;)&#10;            if wt[ind] &lt;= w: take = val[ind] + prev[w - wt[ind]]&#10;            prev[w] = max(take, notTake)&#10;    return prev[W]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">7</td>
      <td rowspan="1">DP 07 Edit Distance<br><br></b> <a href="https://leetcode.com/problems/edit-distance/" target="_blank">LeetCode 72</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> word1 = 'horse', word2 = 'ros'<br><b>Output:</b> 3</td>
      <td><b>Time:</b> O(N * M)<br><b>Space:</b> O(M)</td>
      <td>2D DP. If chars match, dp[i-1][j-1]. Else, 1 + min(insert, delete, replace).</td>
      <td><b>Edge Cases:</b> <b>Empty Strings:</b> Deletions/insertions equal to length.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minDistance(word1: str, word2: str) -&gt; int:&#10;    n, m = len(word1), len(word2)&#10;    prev = list(range(m+1))&#10;    for i in range(1, n+1):&#10;        cur = [i] + [0]*m&#10;        for j in range(1, m+1):&#10;            if word1[i-1] == word2[j-1]: cur[j] = prev[j-1]&#10;            else: cur[j] = 1 + min(prev[j], cur[j-1], prev[j-1])&#10;        prev = cur&#10;    return prev[m]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">8</td>
      <td rowspan="1">DP 08 Matrix Chain Multiplication<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> N=5, arr=[40, 20, 30, 10, 30]<br><b>Output:</b> 26000</td>
      <td><b>Time:</b> O(N^3)<br><b>Space:</b> O(N^2)</td>
      <td>Partition DP. Try partitioning the matrices at every possible split `k` between `i` and `j`. Cost is `arr[i-1]*arr[k]*arr[j]`. Take the minimum.<br><br><b>Dependencies:</b> <code>#include <vector></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def matrixMultiplication(N: int, arr: List[int]) -&gt; int:&#10;    dp = [[-1] * N for _ in range(N)]&#10;    def f(i, j):&#10;        if i == j: return 0&#10;        if dp[i][j] != -1: return dp[i][j]&#10;        mini = int(1e9)&#10;        for k in range(i, j):&#10;            steps = arr[i-1] * arr[k] * arr[j] + f(i, k) + f(k+1, j)&#10;            mini = min(mini, steps)&#10;        dp[i][j] = mini&#10;        return mini&#10;    return f(1, N-1)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">9</td>
      <td rowspan="1">DP 09 Subset Sum Problem<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> set=[3,34,4,12,5,2], sum=9<br><b>Output:</b> True</td>
      <td><b>Time:</b> O(N * Sum)<br><b>Space:</b> O(Sum) space optimized</td>
      <td>DP logic like 0/1 Knapsack. DP state is `dp[index][target]`. At each index, you can take or not take the element if `target >= arr[i]`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isSubsetSum(arr: List[int], sum: int) -&gt; bool:&#10;    n = len(arr)&#10;    prev = [False] * (sum + 1)&#10;    prev[0] = True&#10;    if arr[0] &lt;= sum: prev[arr[0]] = True&#10;    for ind in range(1, n):&#10;        cur = [False] * (sum + 1)&#10;        cur[0] = True&#10;        for target in range(1, sum + 1):&#10;            notTaken = prev[target]&#10;            taken = False&#10;            if arr[ind] &lt;= target: taken = prev[target - arr[ind]]&#10;            cur[target] = notTaken or taken&#10;        prev = cur&#10;    return prev[sum]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">10</td>
      <td rowspan="1">DP 10 Minimum Path Sum<br><br></b> <a href="https://leetcode.com/problems/minimum-path-sum/" target="_blank">LeetCode 64</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> grid = [[1,3,1],[1,5,1],[4,2,1]]<br><b>Output:</b> 7</td>
      <td><b>Time:</b> O(N * M)<br><b>Space:</b> O(M)</td>
      <td>DP on Grids. Space optimize to 1D. `cur[j] = grid[i][j] + min(up, left)`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minPathSum(grid: List[List[int]]) -&gt; int:&#10;    n, m = len(grid), len(grid[0])&#10;    prev = [0] * m&#10;    for i in range(n):&#10;        cur = [0] * m&#10;        for j in range(m):&#10;            if i == 0 and j == 0: cur[j] = grid[i][j]&#10;            else:&#10;                up, left = grid[i][j], grid[i][j]&#10;                up += prev[j] if i &gt; 0 else float(&#x27;inf&#x27;)&#10;                left += cur[j-1] if j &gt; 0 else float(&#x27;inf&#x27;)&#10;                cur[j] = min(up, left)&#10;        prev = cur&#10;    return prev[-1]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">11</td>
      <td rowspan="1">DP 11 Triangle<br><br></b> <a href="https://leetcode.com/problems/triangle/" target="_blank">LeetCode 120</a></td>
      <td rowspan="1"><b>Example 1:</b><br><b>Output:</b> 11</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N)</td>
      <td>Start from bottom row and move upwards. `dp[j] = triangle[i][j] + min(dp[j], dp[j+1])`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minimumTotal(triangle: List[List[int]]) -&gt; int:&#10;    n = len(triangle)&#10;    front = triangle[-1][:]&#10;    for i in range(n-2, -1, -1):&#10;        cur = [0] * n&#10;        for j in range(i, -1, -1):&#10;            cur[j] = triangle[i][j] + min(front[j], front[j+1])&#10;        front = cur&#10;    return front[0]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">12</td>
      <td rowspan="1">DP 12 Minimum Falling Path Sum<br><br></b> <a href="https://leetcode.com/problems/minimum-falling-path-sum/" target="_blank">LeetCode 931</a></td>
      <td rowspan="1"><b>Example 1:</b><br><b>Output:</b> 13</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N)</td>
      <td>Similar to minimum path sum, but we can fall diagonally. Space optimize by using previous row.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minFallingPathSum(matrix: List[List[int]]) -&gt; int:&#10;    n = len(matrix)&#10;    prev = matrix[0][:]&#10;    for i in range(1, n):&#10;        cur = [0] * n&#10;        for j in range(n):&#10;            up = matrix[i][j] + prev[j]&#10;            ld = matrix[i][j] + (prev[j-1] if j &gt; 0 else float(&#x27;inf&#x27;))&#10;            rd = matrix[i][j] + (prev[j+1] if j &lt; n-1 else float(&#x27;inf&#x27;))&#10;            cur[j] = min(up, ld, rd)&#10;        prev = cur&#10;    return min(prev)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">13</td>
      <td rowspan="1">DP 13 Cherry Pickup II<br><br></b> <a href="https://leetcode.com/problems/cherry-pickup-ii/" target="_blank">LeetCode 1463</a></td>
      <td rowspan="1"><b>Example 1:</b> 3D DP.</td>
      <td><b>Time:</b> O(N * M * M * 9)<br><b>Space:</b> O(M * M)</td>
      <td>Robots move simultaneously. State is `dp[row][col1][col2]`. Try all 9 combinations of moves for both robots.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def cherryPickup(grid: List[List[int]]) -&gt; int:&#10;    n, m = len(grid), len(grid[0])&#10;    front = [[0]*m for _ in range(m)]&#10;    for j1 in range(m):&#10;        for j2 in range(m):&#10;            if j1 == j2: front[j1][j2] = grid[n-1][j1]&#10;            else: front[j1][j2] = grid[n-1][j1] + grid[n-1][j2]&#10;    for i in range(n-2, -1, -1):&#10;        cur = [[0]*m for _ in range(m)]&#10;        for j1 in range(m):&#10;            for j2 in range(m):&#10;                maxi = -int(1e9)&#10;                for dj1 in [-1, 0, 1]:&#10;                    for dj2 in [-1, 0, 1]:&#10;                        val = grid[i][j1] if j1 == j2 else grid[i][j1] + grid[i][j2]&#10;                        if 0 &lt;= j1+dj1 &lt; m and 0 &lt;= j2+dj2 &lt; m:&#10;                            val += front[j1+dj1][j2+dj2]&#10;                        else: val += -int(1e9)&#10;                        maxi = max(maxi, val)&#10;                cur[j1][j2] = maxi&#10;        front = cur&#10;    return front[0][m-1]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">14</td>
      <td rowspan="1">DP 14 Partition Equal Subset Sum<br><br></b> <a href="https://leetcode.com/problems/partition-equal-subset-sum/" target="_blank">LeetCode 416</a></td>
      <td rowspan="1"><b>Example 1:</b><br><b>Output:</b> True.</td>
      <td><b>Time:</b> O(N * Target)<br><b>Space:</b> O(Target)</td>
      <td>If total sum is odd, impossible. Else, find if there's a subset with sum `Total/2` using space-optimized DP.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def canPartition(nums: List[int]) -&gt; bool:&#10;    total_sum = sum(nums)&#10;    if total_sum % 2 != 0: return False&#10;    target = total_sum // 2&#10;    prev = [False] * (target + 1)&#10;    prev[0] = True&#10;    if nums[0] &lt;= target: prev[nums[0]] = True&#10;    for ind in range(1, len(nums)):&#10;        cur = [False] * (target + 1)&#10;        cur[0] = True&#10;        for t in range(1, target + 1):&#10;            notTaken = prev[t]&#10;            taken = False&#10;            if nums[ind] &lt;= t: taken = prev[t - nums[ind]]&#10;            cur[t] = notTaken or taken&#10;        prev = cur&#10;    return prev[target]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">15</td>
      <td rowspan="1">DP 15 Target Sum<br><br></b> <a href="https://leetcode.com/problems/target-sum/" target="_blank">LeetCode 494</a></td>
      <td rowspan="1"><b>Example 1:</b> Count Subsets with Diff = target.</td>
      <td><b>Time:</b> O(N * Target)<br><b>Space:</b> O(Target)</td>
      <td>Subset sum variation. `S1 - S2 = target`, `S1 + S2 = totalSum`. So, `S1 = (target + totalSum) / 2`. Find subsets with this target sum.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findTargetSumWays(nums: List[int], target: int) -&gt; int:&#10;    total = sum(nums)&#10;    if total - target &lt; 0 or (total - target) % 2 == 1: return 0&#10;    s2 = (total - target) // 2&#10;    prev = [0] * (s2 + 1)&#10;    if nums[0] == 0: prev[0] = 2&#10;    else: prev[0] = 1&#10;    if nums[0] != 0 and nums[0] &lt;= s2: prev[nums[0]] = 1&#10;    for ind in range(1, len(nums)):&#10;        cur = [0] * (s2 + 1)&#10;        for t in range(s2 + 1):&#10;            notTaken = prev[t]&#10;            taken = 0&#10;            if nums[ind] &lt;= t: taken = prev[t - nums[ind]]&#10;            cur[t] = notTaken + taken&#10;        prev = cur&#10;    return prev[s2]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">16</td>
      <td rowspan="1">DP 16 Burst Balloons<br><br></b> <a href="https://leetcode.com/problems/burst-balloons/" target="_blank">LeetCode 312</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> nums = [3,1,5,8]<br><b>Output:</b> 167</td>
      <td><b>Time:</b> O(N^3)<br><b>Space:</b> O(N^2)</td>
      <td>MCM Pattern. Add 1 at the beginning and end. Loop lengths from 1 to N. Iterate start `i` and end `j`. Then iterate `k` from `i` to `j`, meaning balloon `k` is the LAST one to burst in the range `[i, j]`. The coins collected are `nums[i-1] * nums[k] * nums[j+1] + dp[i][k-1] + dp[k+1][j]`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxCoins(nums: List[int]) -&gt; int:&#10;    n = len(nums)&#10;    nums = [1] + nums + [1]&#10;    dp = [[0] * (n + 2) for _ in range(n + 2)]&#10;    for i in range(n, 0, -1):&#10;        for j in range(1, n + 1):&#10;            if i &gt; j: continue&#10;            maxi = float(&#x27;-inf&#x27;)&#10;            for k in range(i, j + 1):&#10;                cost = nums[i-1]*nums[k]*nums[j+1] + dp[i][k-1] + dp[k+1][j]&#10;                maxi = max(maxi, cost)&#10;            dp[i][j] = maxi&#10;    return dp[1][n]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">17</td>
      <td rowspan="1">DP 17 Palindrome Partitioning II<br><br></b> <a href="https://leetcode.com/problems/palindrome-partitioning-ii/" target="_blank">LeetCode 132</a></td>
      <td rowspan="1"><b>Example 1:</b> <br><b>Input:</b> s = 'aab'<br><b>Output:</b> 1</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N)</td>
      <td>Front Partitioning. `dp[i]` is the minimum cuts for `s[i...n-1]`. To compute `dp[i]`, iterate `j` from `i` to `n-1`. If `s[i...j]` is a palindrome, then `cost = 1 + dp[j+1]`. `dp[i]` is the minimum of these costs. Return `dp[0] - 1`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minCut(s: str) -&gt; int:&#10;    n = len(s)&#10;    dp = [0] * (n + 1)&#10;    for i in range(n - 1, -1, -1):&#10;        min_cuts = float(&#x27;inf&#x27;)&#10;        for j in range(i, n):&#10;            if s[i:j+1] == s[i:j+1][::-1]:&#10;                cost = 1 + dp[j+1]&#10;                min_cuts = min(min_cuts, cost)&#10;        dp[i] = min_cuts&#10;    return dp[0] - 1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">18</td>
      <td rowspan="1">DP 18 Evaluate Boolean Expression To True<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/boolean-parenthesization5610/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> MCM DP pattern.</td>
      <td><b>Time:</b> O(N^3)<br><b>Space:</b> O(N^2)</td>
      <td>MCM DP. `dp[i][j][isTrue]` stores the number of ways to evaluate `S[i..j]` to boolean `isTrue`. Iterate length, start, and partition `k`. Calculate T/F ways based on the operator at `k`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def countWays(N: int, S: str) -&gt; int:&#10;    mod = 1003&#10;    dp = [[[0, 0] for _ in range(N)] for _ in range(N)]&#10;    for i in range(N - 1, -1, -2):&#10;        for j in range(i, N, 2):&#10;            if i == j:&#10;                dp[i][j][1] = 1 if S[i] == &#x27;T&#x27; else 0&#10;                dp[i][j][0] = 1 if S[i] == &#x27;F&#x27; else 0&#10;                continue&#10;            waysT, waysF = 0, 0&#10;            for k in range(i + 1, j, 2):&#10;                lT, lF = dp[i][k-1][1], dp[i][k-1][0]&#10;                rT, rF = dp[k+1][j][1], dp[k+1][j][0]&#10;                if S[k] == &#x27;&amp;&#x27;:&#10;                    waysT = (waysT + lT * rT) % mod&#10;                    waysF = (waysF + lT * rF + lF * rT + lF * rF) % mod&#10;                elif S[k] == &#x27;|&#x27;:&#10;                    waysT = (waysT + lT * rT + lT * rF + lF * rT) % mod&#10;                    waysF = (waysF + lF * rF) % mod&#10;                elif S[k] == &#x27;^&#x27;:&#10;                    waysT = (waysT + lT * rF + lF * rT) % mod&#10;                    waysF = (waysF + lT * rT + lF * rF) % mod&#10;            dp[i][j][1] = waysT&#10;            dp[i][j][0] = waysF&#10;    return dp[0][N-1][1]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">19</td>
      <td rowspan="1">DP 19 Count Square Submatrices With All Ones<br><br></b> <a href="https://leetcode.com/problems/count-square-submatrices-with-all-ones/" target="_blank">LeetCode 1277</a></td>
      <td rowspan="1"><b>Example 1:</b> Return total count.</td>
      <td><b>Time:</b> O(N * M)<br><b>Space:</b> O(N * M)</td>
      <td>`dp[i][j]` is the size of the largest square ending at `(i, j)`. It also represents the number of squares ending at `(i, j)`. `dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1` if `matrix[i][j] == 1`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def countSquares(matrix: List[List[int]]) -&gt; int:&#10;    n, m = len(matrix), len(matrix[0])&#10;    dp = [[0]*m for _ in range(n)]&#10;    total = 0&#10;    for i in range(n):&#10;        for j in range(m):&#10;            if matrix[i][j] == 1:&#10;                if i == 0 or j == 0: dp[i][j] = 1&#10;                else: dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1&#10;                total += dp[i][j]&#10;    return total</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">20</td>
      <td rowspan="1">DP 20 Minimum Cost To Cut A Stick<br><br></b> <a href="https://leetcode.com/problems/minimum-cost-to-cut-a-stick/" target="_blank">LeetCode 1547</a></td>
      <td rowspan="1"><b>Example 1:</b> Cost depends on current stick length.</td>
      <td><b>Time:</b> O(C^3) where C is number of cuts<br><b>Space:</b> O(C^2)</td>
      <td>Sort cuts array and prepend 0, append `n`. Use MCM pattern. `dp[i][j]` is the minimum cost to cut the stick between cuts `i` and `j`. `dp[i][j] = min(cost + cuts[j+1] - cuts[i-1])`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minCost(n: int, cuts: List[int]) -&gt; int:&#10;    cuts = [0] + sorted(cuts) + [n]&#10;    c = len(cuts) - 2&#10;    dp = [[0] * (c + 2) for _ in range(c + 2)]&#10;    for i in range(c, 0, -1):&#10;        for j in range(1, c + 1):&#10;            if i &gt; j: continue&#10;            mini = float(&#x27;inf&#x27;)&#10;            for k in range(i, j + 1):&#10;                cost = cuts[j+1] - cuts[i-1] + dp[i][k-1] + dp[k+1][j]&#10;                mini = min(mini, cost)&#10;            dp[i][j] = mini&#10;    return dp[1][c]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">21</td>
      <td rowspan="1">DP 21 Partition Array For Maximum Sum<br><br></b> <a href="https://leetcode.com/problems/partition-array-for-maximum-sum/" target="_blank">LeetCode 1043</a></td>
      <td rowspan="1"><b>Example 1:</b> Front partitioning DP.</td>
      <td><b>Time:</b> O(N * K)<br><b>Space:</b> O(N)</td>
      <td>Front partitioning. `dp[i]` is max sum for `arr[i..n-1]`. For each `i`, iterate `j` up to `i+k-1`. Find `maxi` element in this window, and add `maxi * length + dp[j+1]`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxSumAfterPartitioning(arr: List[int], k: int) -&gt; int:&#10;    n = len(arr)&#10;    dp = [0] * (n + 1)&#10;    for i in range(n - 1, -1, -1):&#10;        max_val = 0&#10;        max_ans = 0&#10;        length = 0&#10;        for j in range(i, min(n, i + k)):&#10;            length += 1&#10;            max_val = max(max_val, arr[j])&#10;            current_sum = max_val * length + dp[j+1]&#10;            max_ans = max(max_ans, current_sum)&#10;        dp[i] = max_ans&#10;    return dp[0]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">22</td>
      <td rowspan="1">DP 22 Distinct Subsequences<br><br></b> <a href="https://leetcode.com/problems/distinct-subsequences/" target="_blank">LeetCode 115</a></td>
      <td rowspan="1"><b>Example 1:</b> Subsequence match count.</td>
      <td><b>Time:</b> O(N * M)<br><b>Space:</b> O(M)</td>
      <td>If characters match, `dp[i][j] = dp[i-1][j-1] + dp[i-1][j]`. If they don't, `dp[i][j] = dp[i-1][j]`. Optimize to 1D array.</td>
      <td><b>Edge Cases:</b> <b>Integer Overflow:</b> Use double or long long, or cast to unsigned int.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def numDistinct(s: str, t: str) -&gt; int:&#10;    n, m = len(s), len(t)&#10;    dp = [0] * (m + 1)&#10;    dp[0] = 1&#10;    for i in range(1, n + 1):&#10;        for j in range(m, 0, -1):&#10;            if s[i-1] == t[j-1]:&#10;                dp[j] += dp[j-1]&#10;    return dp[m]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">23</td>
      <td rowspan="1">DP 23 Wildcard Matching<br><br></b> <a href="https://leetcode.com/problems/wildcard-matching/" target="_blank">LeetCode 44</a></td>
      <td rowspan="1"><b>Example 1:</b> 2D DP.</td>
      <td><b>Time:</b> O(N * M)<br><b>Space:</b> O(N * M) or O(M)</td>
      <td>Use a 2D DP array where `dp[i][j]` means if `s[0..i-1]` matches `p[0..j-1]`. If `p[j-1] == '?'` or `s[i-1] == p[j-1]`, `dp[i][j] = dp[i-1][j-1]`. If `p[j-1] == '*'`, it can match empty (`dp[i][j-1]`) or match one character (`dp[i-1][j]`).</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isMatch(s: str, p: str) -&gt; bool:&#10;    n, m = len(s), len(p)&#10;    dp = [[False] * (m + 1) for _ in range(n + 1)]&#10;    dp[0][0] = True&#10;    for j in range(1, m + 1):&#10;        if p[j-1] == &#x27;*&#x27;: dp[0][j] = dp[0][j-1]&#10;    for i in range(1, n + 1):&#10;        for j in range(1, m + 1):&#10;            if p[j-1] in {s[i-1], &#x27;?&#x27;}:&#10;                dp[i][j] = dp[i-1][j-1]&#10;            elif p[j-1] == &#x27;*&#x27;:&#10;                dp[i][j] = dp[i-1][j] or dp[i][j-1]&#10;    return dp[n][m]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">24</td>
      <td rowspan="1">DP 24 Best Time To Buy And Sell Stock II<br><br></b> <a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/" target="_blank">LeetCode 122</a></td>
      <td rowspan="1"><b>Example 1:</b> Valley Peak approach.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Add the profit whenever the price is higher than the previous day. This is equivalent to capturing every upward slope.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxProfit(prices: List[int]) -&gt; int:&#10;    return sum(max(prices[i] - prices[i-1], 0) for i in range(1, len(prices)))</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">25</td>
      <td rowspan="1">DP 25 Best Time To Buy And Sell Stock III<br><br></b> <a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/" target="_blank">LeetCode 123</a></td>
      <td rowspan="1"><b>Example 1:</b> 3D DP / State Machine.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Maintain four variables representing the max profit after first buy, first sell, second buy, and second sell. Update them iteratively.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxProfit(prices: List[int]) -&gt; int:&#10;    buy1 = buy2 = float(&#x27;-inf&#x27;)&#10;    sell1 = sell2 = 0&#10;    for price in prices:&#10;        buy1 = max(buy1, -price)&#10;        sell1 = max(sell1, buy1 + price)&#10;        buy2 = max(buy2, sell1 - price)&#10;        sell2 = max(sell2, buy2 + price)&#10;    return sell2</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">26</td>
      <td rowspan="1">DP 26 Best Time To Buy And Sell Stock IV<br><br></b> <a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/" target="_blank">LeetCode 188</a></td>
      <td rowspan="1"><b>Example 1:</b> DP with transactions.</td>
      <td><b>Time:</b> O(N * K)<br><b>Space:</b> O(N * K) or O(K)</td>
      <td>If `k >= n/2`, it's equivalent to infinite transactions (Stock II). Else, use a DP array `dp[k][n]` where `dp[i][j]` is max profit using `i` transactions up to day `j`. Optimize inner loop by tracking `maxDiff = max(maxDiff, dp[i-1][j-1] - prices[j-1])`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxProfit(k: int, prices: List[int]) -&gt; int:&#10;    n = len(prices)&#10;    if n &lt;= 1: return 0&#10;    if k &gt;= n // 2:&#10;        return sum(max(prices[i] - prices[i-1], 0) for i in range(1, n))&#10;    buy = [float(&#x27;-inf&#x27;)] * (k + 1)&#10;    sell = [0] * (k + 1)&#10;    for price in prices:&#10;        for i in range(1, k + 1):&#10;            buy[i] = max(buy[i], sell[i-1] - price)&#10;            sell[i] = max(sell[i], buy[i] + price)&#10;    return sell[k]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">27</td>
      <td rowspan="1">DP 27 Best Time To Buy And Sell Stock With Cooldown<br><br></b> <a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/" target="_blank">LeetCode 309</a></td>
      <td rowspan="1"><b>Example 1:</b> State Machine DP.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Maintain 3 states: `hold` (holding a stock), `sold` (just sold, entering cooldown next), `rest` (not holding, not in cooldown). Transitions: `hold = max(hold, rest - price)`, `sold = hold + price`, `rest = max(rest, sold_prev)`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxProfit(prices: List[int]) -&gt; int:&#10;    hold, sold, rest = float(&#x27;-inf&#x27;), 0, 0&#10;    for price in prices:&#10;        prev_sold = sold&#10;        sold = hold + price&#10;        hold = max(hold, rest - price)&#10;        rest = max(rest, prev_sold)&#10;    return max(rest, sold)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">28</td>
      <td rowspan="1">DP 28 Best Time To Buy And Sell Stock With Transaction Fee<br><br></b> <a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/" target="_blank">LeetCode 714</a></td>
      <td rowspan="1"><b>Example 1:</b> DP State Machine.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Similar to Stock II, but subtract `fee` when selling. Maintain `cash` (max profit not holding stock) and `hold` (max profit holding stock). `cash = max(cash, hold + price - fee)`, `hold = max(hold, cash - price)`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxProfit(prices: List[int], fee: int) -&gt; int:&#10;    cash, hold = 0, -prices[0]&#10;    for i in range(1, len(prices)):&#10;        cash = max(cash, hold + prices[i] - fee)&#10;        hold = max(hold, cash - prices[i])&#10;    return cash</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">29</td>
      <td rowspan="1">DP 29 Largest Divisible Subset<br><br></b> <a href="https://leetcode.com/problems/largest-divisible-subset/" target="_blank">LeetCode 368</a></td>
      <td rowspan="1"><b>Example 1:</b> Sort and LIS variant.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N)</td>
      <td>Sort the array. Then use LIS logic: `dp[i]` is max subset ending at `i`. If `nums[i] % nums[j] == 0`, `dp[i] = max(dp[i], dp[j] + 1)`. Also keep a `parent` array to reconstruct the subset.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def largestDivisibleSubset(nums: List[int]) -&gt; List[int]:&#10;    if not nums: return []&#10;    nums.sort()&#10;    n = len(nums)&#10;    dp, parent = [1] * n, [-1] * n&#10;    max_len, max_idx = 1, 0&#10;    for i in range(1, n):&#10;        for j in range(i):&#10;            if nums[i] % nums[j] == 0 and dp[i] &lt; dp[j] + 1:&#10;                dp[i] = dp[j] + 1&#10;                parent[i] = j&#10;        if dp[i] &gt; max_len:&#10;            max_len, max_idx = dp[i], i&#10;    res = []&#10;    while max_idx != -1:&#10;        res.append(nums[max_idx])&#10;        max_idx = parent[max_idx]&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">30</td>
      <td rowspan="1">DP 30 Longest String Chain<br><br></b> <a href="https://leetcode.com/problems/longest-string-chain/" target="_blank">LeetCode 1048</a></td>
      <td rowspan="1"><b>Example 1:</b> Sort by length and use hash map.</td>
      <td><b>Time:</b> O(N log N + N * L^2) where L is max word length<br><b>Space:</b> O(N * L)</td>
      <td>Sort words by length. Use a hash map `dp` to store the longest chain ending at `word`. For each word, try removing one character at a time to form `prev_word`. `dp[word] = max(dp[word], dp[prev_word] + 1)`.<br><br><b>Dependencies:</b> <code>#include <unordered_map></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def longestStrChain(words: List[str]) -&gt; int:&#10;    words.sort(key=len)&#10;    dp = {}&#10;    max_len = 1&#10;    for word in words:&#10;        dp[word] = 1&#10;        for i in range(len(word)):&#10;            prev = word[:i] + word[i+1:]&#10;            if prev in dp:&#10;                dp[word] = max(dp[word], dp[prev] + 1)&#10;        max_len = max(max_len, dp[word])&#10;    return max_len</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">31</td>
      <td rowspan="1">DP 31 Longest Bitonic Subsequence<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/longest-bitonic-subsequence0824/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> LIS from left + LIS from right.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N)</td>
      <td>Compute LIS ending at `i` from left to right (`inc[i]`). Compute LIS starting at `i` from right to left (`dec[i]`). The max bitonic subsequence length is `max(inc[i] + dec[i] - 1)` for all `i`. Sometimes pure increasing or pure decreasing is also bitonic depending on definition, adjust if necessary.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def LongestBitonicSequence(nums: List[int]) -&gt; int:&#10;    n = len(nums)&#10;    inc = [1] * n&#10;    dec = [1] * n&#10;    for i in range(1, n):&#10;        for j in range(i):&#10;            if nums[i] &gt; nums[j]: inc[i] = max(inc[i], inc[j] + 1)&#10;    for i in range(n - 2, -1, -1):&#10;        for j in range(n - 1, i, -1):&#10;            if nums[i] &gt; nums[j]: dec[i] = max(dec[i], dec[j] + 1)&#10;    return max(inc[i] + dec[i] - 1 for i in range(n))</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">32</td>
      <td rowspan="1">DP 32 Number Of Longest Increasing Subsequence<br><br></b> <a href="https://leetcode.com/problems/number-of-longest-increasing-subsequence/" target="_blank">LeetCode 673</a></td>
      <td rowspan="1"><b>Example 1:</b> Two DP arrays (Length and Count).</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N)</td>
      <td>Maintain `lengths[i]` (length of LIS ending at i) and `counts[i]` (number of LIS ending at i). If `nums[i] > nums[j]`: if `lengths[j] + 1 > lengths[i]`, then `lengths[i] = lengths[j] + 1` and `counts[i] = counts[j]`. Else if `lengths[j] + 1 == lengths[i]`, then `counts[i] += counts[j]`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findNumberOfLIS(nums: List[int]) -&gt; int:&#10;    n = len(nums)&#10;    lengths = [1] * n&#10;    counts = [1] * n&#10;    max_len = 0&#10;    res = 0&#10;    for i in range(n):&#10;        for j in range(i):&#10;            if nums[i] &gt; nums[j]:&#10;                if lengths[j] + 1 &gt; lengths[i]:&#10;                    lengths[i] = lengths[j] + 1&#10;                    counts[i] = counts[j]&#10;                elif lengths[j] + 1 == lengths[i]:&#10;                    counts[i] += counts[j]&#10;        if lengths[i] &gt; max_len:&#10;            max_len = lengths[i]&#10;            res = counts[i]&#10;        elif lengths[i] == max_len:&#10;            res += counts[i]&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">33</td>
      <td rowspan="1">DP 33 Longest Alternating Subsequence<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/longest-alternating-subsequence5951/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Two state DP.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Maintain two lengths: `up` (ending with ascending) and `down` (ending with descending). Iterate array: if `arr[i] > arr[i-1]`, `up = down + 1`. If `arr[i] < arr[i-1]`, `down = up + 1`. Return `max(up, down)`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def AlternatingaMaxLength(nums: List[int]) -&gt; int:&#10;    if not nums: return 0&#10;    up = down = 1&#10;    for i in range(1, len(nums)):&#10;        if nums[i] &gt; nums[i-1]: up = down + 1&#10;        elif nums[i] &lt; nums[i-1]: down = up + 1&#10;    return max(up, down)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">34</td>
      <td rowspan="1">DP 34 Largest Square Formed In A Matrix<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/largest-square-formed-in-a-matrix0806/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Bottom-up DP.</td>
      <td><b>Time:</b> O(N * M)<br><b>Space:</b> O(N * M) or O(M)</td>
      <td>`dp[i][j]` is side of max square ending at `(i, j)`. If `mat[i][j] == 1`, `dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1`. Result is max over all `dp[i][j]`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxSquare(n: int, m: int, mat: List[List[int]]) -&gt; int:&#10;    dp = [[0] * m for _ in range(n)]&#10;    ans = 0&#10;    for i in range(n):&#10;        for j in range(m):&#10;            if mat[i][j] == 1:&#10;                if i == 0 or j == 0:&#10;                    dp[i][j] = 1&#10;                else:&#10;                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1&#10;                ans = max(ans, dp[i][j])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">35</td>
      <td rowspan="1">DP 35 Pairs With Specific Difference<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/pairs-with-specific-difference1533/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Sort and DP or Greedy.</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(1)</td>
      <td>Sort array. Iterate from end. If `arr[i] - arr[i-1] < K`, we pair them, add sum to answer, and `i -= 2`. Else, `i -= 1`. Greedy approach works because pairing larger numbers gives a larger sum.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxSumPairWithDifferenceLessThanK(arr: List[int], N: int, K: int) -&gt; int:&#10;    arr.sort()&#10;    ans = 0&#10;    i = N - 1&#10;    while i &gt; 0:&#10;        if arr[i] - arr[i-1] &lt; K:&#10;            ans += arr[i] + arr[i-1]&#10;            i -= 2&#10;        else:&#10;            i -= 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">36</td>
      <td rowspan="1">DP 36 Maximum Path Sum In Matrix<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/path-in-matrix3805/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> 2D DP.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N)</td>
      <td>Start from bottom row up. `dp[i][j] = matrix[i][j] + max(dp[i+1][j], dp[i+1][j-1], dp[i+1][j+1])`. The answer is max value in `dp[0]`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maximumPath(N: int, Matrix: List[List[int]]) -&gt; int:&#10;    prev = Matrix[-1][:]&#10;    for i in range(N - 2, -1, -1):&#10;        curr = [0] * N&#10;        for j in range(N):&#10;            up = Matrix[i][j] + prev[j]&#10;            ld = Matrix[i][j] + prev[j-1] if j &gt; 0 else 0&#10;            rd = Matrix[i][j] + prev[j+1] if j &lt; N - 1 else 0&#10;            curr[j] = max(up, ld, rd)&#10;        prev = curr&#10;    return max(prev)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">37</td>
      <td rowspan="1">DP 37 Maximum Difference Of Zeros And Ones In Binary String<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/maximum-difference-of-zeros-and-ones-in-binary-string4111/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Kadane's Algorithm.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>Convert '0' to 1 and '1' to -1. Find the maximum subarray sum using Kadane's algorithm. If max sum is negative, it means string has all 1s, return -1.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxSubstring(S: str) -&gt; int:&#10;    mx, curr = float(&#x27;-inf&#x27;), 0&#10;    for c in S:&#10;        val = 1 if c == &#x27;0&#x27; else -1&#10;        curr = max(val, curr + val)&#10;        mx = max(mx, curr)&#10;    return mx</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">38</td>
      <td rowspan="1">DP 38 Minimum Removals From Array To Make Max Min K<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/minimum-removals3851/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> DP after sorting.</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(1)</td>
      <td>Sort array. We want to find the longest subarray `arr[i..j]` such that `arr[j] - arr[i] <= K`. `dp[i]` could store the max `j` for index `i`. Or use Binary Search (`upper_bound`) for each `i` to find the valid `j`, maximizing `j - i + 1`. Total removed = `N - max_length`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import bisect&#10;def removals(arr: List[int], k: int) -&gt; int:&#10;    n = len(arr)&#10;    arr.sort()&#10;    maxLen = 0&#10;    for i in range(n):&#10;        j = bisect.bisect_right(arr, arr[i] + k) - 1&#10;        maxLen = max(maxLen, j - i + 1)&#10;    return n - maxLen</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">39</td>
      <td rowspan="1">DP 39 Longest Common Substring<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/longest-common-substring1452/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> 2D DP.</td>
      <td><b>Time:</b> O(N * M)<br><b>Space:</b> O(M)</td>
      <td>`dp[i][j]` is the length of longest common suffix of `S1[0..i-1]` and `S2[0..j-1]`. If `S1[i-1] == S2[j-1]`, `dp[i][j] = dp[i-1][j-1] + 1`. Else, `dp[i][j] = 0`. Max value in `dp` table is answer.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def longestCommonSubstr(S1: str, S2: str, n: int, m: int) -&gt; int:&#10;    prev = [0] * (m + 1)&#10;    ans = 0&#10;    for i in range(1, n + 1):&#10;        curr = [0] * (m + 1)&#10;        for j in range(1, m + 1):&#10;            if S1[i-1] == S2[j-1]:&#10;                curr[j] = prev[j-1] + 1&#10;                ans = max(ans, curr[j])&#10;            else:&#10;                curr[j] = 0&#10;        prev = curr&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">40</td>
      <td rowspan="1">DP 40 Reach A Given Score<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/reach-a-given-score-1587115621/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Unbounded Knapsack.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>`dp[i]` represents number of ways to reach score `i`. Init `dp[0] = 1`. For each score option (3, 5, 10), iterate from option to `n`, `dp[i] += dp[i - option]`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def count(n: int) -&gt; int:&#10;    dp = [0] * (n + 1)&#10;    dp[0] = 1&#10;    scores = [3, 5, 10]&#10;    for s in scores:&#10;        for i in range(s, n + 1):&#10;            dp[i] += dp[i - s]&#10;    return dp[n]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">41</td>
      <td rowspan="1">DP 41 Coin Change Maximum Ways<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/coin-change2448/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> 1D Tabulation.</td>
      <td><b>Time:</b> O(M * N)<br><b>Space:</b> O(N)</td>
      <td>Create a `dp` array of size `N + 1` initialized to 0. `dp[0] = 1`. For each coin, iterate through all amounts from `coin` to `N` and update `dp[j] += dp[j - coin]`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def count(coins: List[int], N: int, sum: int) -&gt; int:&#10;    dp = [0] * (sum + 1)&#10;    dp[0] = 1&#10;    for coin in coins:&#10;        for j in range(coin, sum + 1):&#10;            dp[j] += dp[j - coin]&#10;    return dp[sum]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">42</td>
      <td rowspan="1">DP 42 Palindromic Partitioning<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/palindromic-patitioning4845/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> 1D DP.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N^2)</td>
      <td>Create a `dp` array where `dp[i]` is min cuts for `str[0..i]`. Also use a 2D boolean DP to check if `str[j..i]` is a palindrome. If it is, `dp[i] = min(dp[i], dp[j-1] + 1)`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def palindromicPartition(string: str) -&gt; int:&#10;    n = len(string)&#10;    isPal = [[False] * n for _ in range(n)]&#10;    dp = [0] * n&#10;    for i in range(n):&#10;        minCut = i&#10;        for j in range(i + 1):&#10;            if string[i] == string[j] and (i - j &lt; 2 or isPal[j+1][i-1]):&#10;                isPal[j][i] = True&#10;                if j == 0:&#10;                    minCut = 0&#10;                else:&#10;                    minCut = min(minCut, dp[j-1] + 1)&#10;        dp[i] = minCut&#10;    return dp[-1]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">43</td>
      <td rowspan="1">DP 43 Maximum Sum Increasing Subsequence<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/maximum-sum-increasing-subsequence4749/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> DP (LIS variant).</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N)</td>
      <td>Variation of LIS. Create an array `msis` initialized with the given array values. For each `i` from 1 to `n-1`, for each `j` from 0 to `i-1`, if `arr[i] > arr[j]` and `msis[i] < msis[j] + arr[i]`, update `msis[i]`. The max in `msis` is the answer.<br><br><b>Dependencies:</b> DP</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxSumIS(arr, n):&#10;    msis = list(arr)&#10;    max_sum = msis[0]&#10;    for i in range(1, n):&#10;        for j in range(i):&#10;            if arr[i] &gt; arr[j] and msis[i] &lt; msis[j] + arr[i]:&#10;                msis[i] = msis[j] + arr[i]&#10;        max_sum = max(max_sum, msis[i])&#10;    return max_sum</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">44</td>
      <td rowspan="1">DP 44 Count All Subsequences Having Product Less Than K<br><br></b> <a href="https://www.geeksforgeeks.org/count-subsequences-product-less-k/" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> DP.</td>
      <td><b>Time:</b> O(N * K)<br><b>Space:</b> O(N * K)</td>
      <td>Use a 2D DP array where `dp[i][j]` is the number of subsequences of first `i` elements with product less than or equal to `j`. `dp[i][j] = dp[i-1][j] + dp[i-1][j/arr[i-1]] + 1`.<br><br><b>Dependencies:</b> DP</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def countSubsequences(a, k):&#10;    n = len(a)&#10;    dp = [[0] * (k + 1) for _ in range(n + 1)]&#10;    for i in range(1, n + 1):&#10;        for j in range(1, k + 1):&#10;            dp[i][j] = dp[i - 1][j]&#10;            if a[i - 1] &lt;= j and a[i - 1] &gt; 0:&#10;                dp[i][j] += dp[i - 1][j // a[i - 1]] + 1&#10;    return dp[n][k]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">45</td>
      <td rowspan="1">DP 45 Longest Subsequence Such That Difference Between Adjacents Is One<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/longest-subsequence-such-that-difference-between-adjacents-is-one4724/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> DP (LIS variant).</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N)</td>
      <td>Use a 1D DP array `dp` where `dp[i]` is the length of the longest subsequence ending at `i`. For each `i`, check all `j < i`. If `abs(A[i] - A[j]) == 1`, update `dp[i] = max(dp[i], dp[j] + 1)`.<br><br><b>Dependencies:</b> DP</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def longestSubsequence(N, A):&#10;    dp = [1] * N&#10;    ans = 1&#10;    for i in range(1, N):&#10;        for j in range(i):&#10;            if abs(A[i] - A[j]) == 1:&#10;                dp[i] = max(dp[i], dp[j] + 1)&#10;        ans = max(ans, dp[i])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">46</td>
      <td rowspan="1">DP 46 Maximum Subsequence Sum Such That No Three Are Consecutive<br><br></b> <a href="https://www.geeksforgeeks.org/maximum-subsequence-sum-such-that-no-three-are-consecutive/" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> DP.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Use a DP array. `dp[i]` is the max sum considering up to index `i`. For `i`, the max sum is `max(dp[i-1] (exclude i), dp[i-2] + arr[i] (exclude i-1), dp[i-3] + arr[i] + arr[i-1] (exclude i-2))`.<br><br><b>Dependencies:</b> DP</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxSum(arr):&#10;    n = len(arr)&#10;    if n == 0: return 0&#10;    if n == 1: return arr[0]&#10;    if n == 2: return arr[0] + arr[1]&#10;    dp = [0] * n&#10;    dp[0] = arr[0]&#10;    dp[1] = arr[0] + arr[1]&#10;    dp[2] = max(dp[1], arr[0] + arr[2], arr[1] + arr[2])&#10;    for i in range(3, n):&#10;        dp[i] = max(dp[i-1], dp[i-2] + arr[i], dp[i-3] + arr[i] + arr[i-1])&#10;    return dp[n-1]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">47</td>
      <td rowspan="1">DP 47 Egg Dropping Puzzle<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/egg-dropping-puzzle-1587115620/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> DP + Binary Search / Math.</td>
      <td><b>Time:</b> O(N * K log K)<br><b>Space:</b> O(N * K)</td>
      <td>Use DP. `dp[i][j]` is the min attempts with `i` eggs and `j` floors. Try dropping from every floor `x` from 1 to `j`. `res = 1 + max(dp[i-1][x-1] (breaks), dp[i][j-x] (doesn't break))`. Optimize this nested loop using Binary Search or use a different state `dp[m][k]` = floors checked with `m` moves and `k` eggs.<br><br><b>Dependencies:</b> DP</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def eggDrop(n, k):&#10;    dp = [[0] * (n + 1) for _ in range(k + 1)]&#10;    m = 0&#10;    while dp[m][n] &lt; k:&#10;        m += 1&#10;        for x in range(1, n + 1):&#10;            dp[m][x] = 1 + dp[m-1][x-1] + dp[m-1][x]&#10;    return m</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">48</td>
      <td rowspan="1">DP 48 Maximum Length Chain Of Pairs<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/max-length-chain/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Sort and Greedy / DP.</td>
      <td><b>Time:</b> O(N log N)<br><b>Space:</b> O(1)</td>
      <td>This is exactly the Activity Selection Problem. Sort the pairs by their second element. Iterate through the sorted pairs and keep track of the end of the last selected pair. If the next pair's start is > last end, select it.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class Pair:&#10;    def __init__(self, a, b):&#10;        self.a = a&#10;        self.b = b&#10;def maxChainLen(Parr, n):&#10;    Parr.sort(key=lambda x: x.b)&#10;    count = 1&#10;    last_end = Parr[0].b&#10;    for i in range(1, n):&#10;        if Parr[i].a &gt; last_end:&#10;            count += 1&#10;            last_end = Parr[i].b&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">49</td>
      <td rowspan="1">DP 49 Optimal Strategy For A Game<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/optimal-strategy-for-a-game-1587115620/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> DP.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N^2)</td>
      <td>If you pick `i`, opponent picks `i+1` or `j`, leaving you with `(i+2, j)` or `(i+1, j-1)`. Opponent plays optimally to minimize your profit. So you get `A[i] + min(dp(i+2, j), dp(i+1, j-1))`. Similarly for picking `j`. Take the max of these two choices.<br><br><b>Dependencies:</b> DP</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maximumAmount(arr, n):&#10;    dp = [[0] * n for _ in range(n)]&#10;    for gap in range(n):&#10;        for i in range(n - gap):&#10;            j = i + gap&#10;            x = dp[i+2][j] if i + 2 &lt;= j else 0&#10;            y = dp[i+1][j-1] if i + 1 &lt;= j - 1 else 0&#10;            z = dp[i][j-2] if i &lt;= j - 2 else 0&#10;            dp[i][j] = max(arr[i] + min(x, y), arr[j] + min(y, z))&#10;    return dp[0][n-1]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">50</td>
      <td rowspan="1">DP 50 Minimum Insertions To Make String Palindrome<br><br></b> <a href="https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/" target="_blank">LeetCode 1312</a></td>
      <td rowspan="1"><b>Example 1:</b> Longest Palindromic Subsequence.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N^2)</td>
      <td>Find the Longest Palindromic Subsequence (LPS). The minimum insertions required will be `string_length - LPS_length`. LPS is just LCS(s, reverse(s)).</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minInsertions(s):&#10;    n = len(s)&#10;    t = s[::-1]&#10;    dp = [[0] * (n + 1) for _ in range(n + 1)]&#10;    for i in range(1, n + 1):&#10;        for j in range(1, n + 1):&#10;            if s[i-1] == t[j-1]: dp[i][j] = 1 + dp[i-1][j-1]&#10;            else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])&#10;    return n - dp[n][n]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">51</td>
      <td rowspan="1">DP 51 Print Longest Common Subsequence<br><br></b> <a href="https://www.geeksforgeeks.org/printing-longest-common-subsequence/" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> DP table backtracking.</td>
      <td><b>Time:</b> O(M * N)<br><b>Space:</b> O(M * N)</td>
      <td>Build the LCS DP table. Start from `dp[m][n]`. If `s1[i-1] == s2[j-1]`, include this character in the result and move diagonally to `dp[i-1][j-1]`. Otherwise, move to the maximum of `dp[i-1][j]` or `dp[i][j-1]`. Reverse the string at the end.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def printLCS(s1, s2):&#10;    m, n = len(s1), len(s2)&#10;    dp = [[0] * (n + 1) for _ in range(m + 1)]&#10;    for i in range(1, m + 1):&#10;        for j in range(1, n + 1):&#10;            if s1[i-1] == s2[j-1]: dp[i][j] = 1 + dp[i-1][j-1]&#10;            else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])&#10;    i, j = m, n&#10;    res = &quot;&quot;&#10;    while i &gt; 0 and j &gt; 0:&#10;        if s1[i-1] == s2[j-1]:&#10;            res += s1[i-1]&#10;            i -= 1; j -= 1&#10;        elif dp[i-1][j] &gt; dp[i][j-1]: i -= 1&#10;        else: j -= 1&#10;    return res[::-1]</code></pre></details></td>
    </tr>
  </tbody>
</table>


## Tries

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
      <td rowspan="1">1</td>
      <td rowspan="1">Trie 01 Implement Trie Prefix Tree<br><br></b> <a href="https://leetcode.com/problems/implement-trie-prefix-tree/" target="_blank">LeetCode 208</a></td>
      <td rowspan="1"><b>Example 1:</b> `insert("apple")`, `search("apple")` -> true, `search("app")` -> false, `startsWith("app")` -> true.<br><br><b>Note (Constraint):</b> 1 &le; word.length &le; 2000, lowercase English letters.</td>
      <td><b>Time:</b> O(Length of word) (Constraint)<br><b>Space:</b> O(Length * 26) per word</td>
      <td>Use a Tree where each node contains an array of 26 pointers (for 'a'-'z') and a boolean flag `isEnd`.<br><br><b>Dependencies:</b> Custom Node Struct/Class</td>
      <td><b>Edge Cases:</b> <b>startsWith vs search:</b> `startsWith` returns true simply if the traversal succeeds without hitting NULL. `search` requires the final node's `isEnd` flag to be true.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class TrieNode:&#10;    def __init__(self):&#10;        self.children = {}&#10;        self.is_end = False&#10;&#10;class Trie:&#10;    def __init__(self):&#10;        self.root = TrieNode()&#10;&#10;    def insert(self, word: str) -&gt; None:&#10;        node = self.root&#10;        for char in word:&#10;            if char not in node.children:&#10;                node.children[char] = TrieNode()&#10;            node = node.children[char]&#10;        node.is_end = True&#10;&#10;    def search(self, word: str) -&gt; bool:&#10;        node = self.root&#10;        for char in word:&#10;            if char not in node.children:&#10;                return False&#10;            node = node.children[char]&#10;        return node.is_end&#10;&#10;    def startsWith(self, prefix: str) -&gt; bool:&#10;        node = self.root&#10;        for char in prefix:&#10;            if char not in node.children:&#10;                return False&#10;            node = node.children[char]&#10;        return True</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">2</td>
      <td rowspan="1">Trie 02 Implement Trie II<br><br></b> <a href="https://www.codingninjas.com/studio/problems/implement-trie_1387095" target="_blank">Coding Ninjas</a></td>
      <td rowspan="1"><b>Example 1:</b> Specialized Trie functions.</td>
      <td><b>Time:</b> O(len) per operation<br><b>Space:</b> O(N * len)</td>
      <td>Trie Nodes have a `cntEndWith` and `cntPrefix` integers. Increment `cntPrefix` dynamically as you insert, and `cntEndWith` at the final node. Decrement them during erase.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class Node:&#10;    def __init__(self):&#10;        self.links = [None] * 26&#10;        self.cntEndWith = 0&#10;        self.cntPrefix = 0&#10;class Trie:&#10;    def __init__(self):&#10;        self.root = Node()&#10;    def insert(self, word: str):&#10;        node = self.root&#10;        for ch in word:&#10;            idx = ord(ch) - 97&#10;            if not node.links[idx]: node.links[idx] = Node()&#10;            node = node.links[idx]&#10;            node.cntPrefix += 1&#10;        node.cntEndWith += 1&#10;    def countWordsEqualTo(self, word: str) -&gt; int:&#10;        node = self.root&#10;        for ch in word:&#10;            idx = ord(ch) - 97&#10;            if not node.links[idx]: return 0&#10;            node = node.links[idx]&#10;        return node.cntEndWith</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">3</td>
      <td rowspan="1">Trie 03 Longest String With All Prefixes<br><br></b> <a href="https://www.codingninjas.com/codestudio/problems/complete-string_2687860" target="_blank">Coding Ninjas</a></td>
      <td rowspan="1"><b>Example 1:</b> Insert all, check each word.</td>
      <td><b>Time:</b> O(N * max_len)<br><b>Space:</b> O(N * max_len)</td>
      <td>Insert all words into a Trie. For each word, check if every prefix exists (i.e., every node from root to end has `isEnd == true`). Keep track of the longest valid word. Resolve ties lexicographically.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class Node:&#10;    def __init__(self):&#10;        self.links = [None] * 26&#10;        self.flag = False&#10;    def containsKey(self, ch):&#10;        return self.links[ord(ch) - ord(&#x27;a&#x27;)] is not None&#10;    def put(self, ch, node):&#10;        self.links[ord(ch) - ord(&#x27;a&#x27;)] = node&#10;    def get(self, ch):&#10;        return self.links[ord(ch) - ord(&#x27;a&#x27;)]&#10;    def setEnd(self): self.flag = True&#10;    def isEnd(self): return self.flag&#10;class Trie:&#10;    def __init__(self):&#10;        self.root = Node()&#10;    def insert(self, word):&#10;        node = self.root&#10;        for ch in word:&#10;            if not node.containsKey(ch): node.put(ch, Node())&#10;            node = node.get(ch)&#10;        node.setEnd()&#10;    def checkAllPrefixes(self, word):&#10;        node = self.root&#10;        for ch in word:&#10;            if node.containsKey(ch):&#10;                node = node.get(ch)&#10;                if not node.isEnd(): return False&#10;            else: return False&#10;        return True&#10;def completeString(n: int, a: List[str]) -&gt; str:&#10;    trie = Trie()&#10;    for word in a: trie.insert(word)&#10;    longest = &quot;&quot;&#10;    for word in a:&#10;        if trie.checkAllPrefixes(word):&#10;            if len(word) &gt; len(longest):&#10;                longest = word&#10;            elif len(word) == len(longest) and word &lt; longest:&#10;                longest = word&#10;    return longest if longest else &quot;None&quot;</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">4</td>
      <td rowspan="1">Trie 04 Number Of Distinct Substrings In A String<br><br></b> <a href="https://www.codingninjas.com/codestudio/problems/count-distinct-substrings_985292" target="_blank">Coding Ninjas</a></td>
      <td rowspan="1"><b>Example 1:</b> Insert all suffixes.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N^2)</td>
      <td>To find all substrings, iterate `i` from 0 to N-1, and `j` from `i` to N-1. Each sequence `s[i...j]` is a substring. Insert it into the Trie. Every time we create a new node, it corresponds to a new distinct substring. Increment count. Add 1 for the empty substring.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class Node:&#10;    def __init__(self):&#10;        self.links = [None] * 26&#10;    def containsKey(self, ch):&#10;        return self.links[ord(ch) - ord(&#x27;a&#x27;)] is not None&#10;    def put(self, ch, node):&#10;        self.links[ord(ch) - ord(&#x27;a&#x27;)] = node&#10;    def get(self, ch):&#10;        return self.links[ord(ch) - ord(&#x27;a&#x27;)]&#10;def countDistinctSubstrings(s: str) -&gt; int:&#10;    root = Node()&#10;    count = 0&#10;    for i in range(len(s)):&#10;        node = root&#10;        for j in range(i, len(s)):&#10;            if not node.containsKey(s[j]):&#10;                node.put(s[j], Node())&#10;                count += 1&#10;            node = node.get(s[j])&#10;    return count + 1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">5</td>
      <td rowspan="1">Trie 05 Maximum Xor Of Two Numbers In An Array<br><br></b> <a href="https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/" target="_blank">LeetCode 421</a></td>
      <td rowspan="1"><b>Example 1:</b> Bit Trie.</td>
      <td><b>Time:</b> O(N * 32)<br><b>Space:</b> O(N * 32)</td>
      <td>Insert binary representation of each number (from MSB to LSB, 31 to 0) into a Trie. To find max XOR for `x`, traverse the Trie aiming for opposite bits (1 for 0, 0 for 1). If opposite bit exists, go that way and add `1 << i` to result. Else go same way.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class Node:&#10;    def __init__(self):&#10;        self.links = [None, None]&#10;    def containsKey(self, bit): return self.links[bit] is not None&#10;    def put(self, bit, node): self.links[bit] = node&#10;    def get(self, bit): return self.links[bit]&#10;class Trie:&#10;    def __init__(self):&#10;        self.root = Node()&#10;    def insert(self, num):&#10;        node = self.root&#10;        for i in range(31, -1, -1):&#10;            bit = (num &gt;&gt; i) &amp; 1&#10;            if not node.containsKey(bit):&#10;                node.put(bit, Node())&#10;            node = node.get(bit)&#10;    def getMax(self, num):&#10;        node = self.root&#10;        maxNum = 0&#10;        for i in range(31, -1, -1):&#10;            bit = (num &gt;&gt; i) &amp; 1&#10;            if node.containsKey(1 - bit):&#10;                maxNum |= (1 &lt;&lt; i)&#10;                node = node.get(1 - bit)&#10;            else:&#10;                node = node.get(bit)&#10;        return maxNum&#10;def findMaximumXOR(nums: List[int]) -&gt; int:&#10;    trie = Trie()&#10;    for num in nums: trie.insert(num)&#10;    maxi = 0&#10;    for num in nums:&#10;        maxi = max(maxi, trie.getMax(num))&#10;    return maxi</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">6</td>
      <td rowspan="1">Trie 06 Maximum Xor With An Element From Array<br><br></b> <a href="https://leetcode.com/problems/maximum-xor-with-an-element-from-array/" target="_blank">LeetCode 1707</a></td>
      <td rowspan="1"><b>Example 1:</b> Offline Queries.</td>
      <td><b>Time:</b> O(N log N + Q log Q + Q * 32 + N * 32)<br><b>Space:</b> O(N * 32 + Q)</td>
      <td>Sort `nums` array. Store queries as `{m, x, index}` and sort them by `m`. Iterate through queries. While `nums[i] <= m`, insert `nums[i]` into Trie. If Trie is empty, answer is -1. Else, query Trie for max XOR with `x`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class Node:&#10;    def __init__(self):&#10;        self.links = [None, None]&#10;    def containsKey(self, bit): return self.links[bit] is not None&#10;    def put(self, bit, node): self.links[bit] = node&#10;    def get(self, bit): return self.links[bit]&#10;class Trie:&#10;    def __init__(self):&#10;        self.root = Node()&#10;    def insert(self, num):&#10;        node = self.root&#10;        for i in range(31, -1, -1):&#10;            bit = (num &gt;&gt; i) &amp; 1&#10;            if not node.containsKey(bit): node.put(bit, Node())&#10;            node = node.get(bit)&#10;    def getMax(self, num):&#10;        node = self.root&#10;        maxNum = 0&#10;        for i in range(31, -1, -1):&#10;            bit = (num &gt;&gt; i) &amp; 1&#10;            if node.containsKey(1 - bit):&#10;                maxNum |= (1 &lt;&lt; i)&#10;                node = node.get(1 - bit)&#10;            else:&#10;                node = node.get(bit)&#10;        return maxNum&#10;def maximizeXor(nums: List[int], queries: List[List[int]]) -&gt; List[int]:&#10;    nums.sort()&#10;    oQ = sorted([(q[1], q[0], i) for i, q in enumerate(queries)])&#10;    ans = [0] * len(queries)&#10;    trie = Trie()&#10;    ind = 0&#10;    for m, x, qInd in oQ:&#10;        while ind &lt; len(nums) and nums[ind] &lt;= m:&#10;            trie.insert(nums[ind])&#10;            ind += 1&#10;        if ind == 0: ans[qInd] = -1&#10;        else: ans[qInd] = trie.getMax(x)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">7</td>
      <td rowspan="1">Trie 07 Word Search II<br><br></b> <a href="https://leetcode.com/problems/word-search-ii/" target="_blank">LeetCode 212</a></td>
      <td rowspan="1"><b>Example 1:</b> DFS + Trie.</td>
      <td><b>Time:</b> O(M * N * 4^L)<br><b>Space:</b> O(sum(L))</td>
      <td>Insert all words into a Trie. Store the actual word at the `isEnd` node for easy retrieval. Do DFS from each cell. During DFS, traverse the Trie simultaneously. If a Trie node has a word, add it to results and remove the word from the node to avoid duplicates.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class Node:&#10;    def __init__(self):&#10;        self.links = [None] * 26&#10;        self.word = &quot;&quot;&#10;def findWords(board: List[List[str]], words: List[str]) -&gt; List[str]:&#10;    root = Node()&#10;    for w in words:&#10;        node = root&#10;        for c in w:&#10;            if not node.links[ord(c)-97]: node.links[ord(c)-97] = Node()&#10;            node = node.links[ord(c)-97]&#10;        node.word = w&#10;    res = []&#10;    def dfs(i, j, node):&#10;        c = board[i][j]&#10;        if c == &#x27;#&#x27; or not node.links[ord(c)-97]: return&#10;        node = node.links[ord(c)-97]&#10;        if node.word:&#10;            res.append(node.word)&#10;            node.word = &quot;&quot;&#10;        board[i][j] = &#x27;#&#x27;&#10;        for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:&#10;            if 0 &lt;= i+x &lt; len(board) and 0 &lt;= j+y &lt; len(board[0]):&#10;                dfs(i+x, j+y, node)&#10;        board[i][j] = c&#10;    for i in range(len(board)):&#10;        for j in range(len(board[0])):&#10;            dfs(i, j, root)&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">8</td>
      <td rowspan="1">Trie 08 Palindrome Pairs<br><br></b> <a href="https://leetcode.com/problems/palindrome-pairs/" target="_blank">LeetCode 336</a></td>
      <td rowspan="1"><b>Example 1:</b> Trie of reversed words.</td>
      <td><b>Time:</b> O(N * L^2)<br><b>Space:</b> O(N * L)</td>
      <td>Insert the REVERSE of every word into a Trie. Store index of word at node. For each word, search the Trie. Three cases: 1. Trie word is longer (current word exhausted, check if rest of Trie branch is palindrome). 2. Current word is longer (Trie exhausted, check if rest of current word is palindrome). 3. Exact match. Store valid indices.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class Node:&#10;    def __init__(self):&#10;        self.links = [None] * 26&#10;        self.idx = -1&#10;        self.pal_indices = []&#10;def is_pal(s, i, j):&#10;    while i &lt; j:&#10;        if s[i] != s[j]: return False&#10;        i += 1; j -= 1&#10;    return True&#10;def palindromePairs(words: List[str]) -&gt; List[List[int]]:&#10;    root = Node()&#10;    for i, w in enumerate(words):&#10;        node = root&#10;        for j in range(len(w) - 1, -1, -1):&#10;            if is_pal(w, 0, j): node.pal_indices.append(i)&#10;            idx = ord(w[j]) - 97&#10;            if not node.links[idx]: node.links[idx] = Node()&#10;            node = node.links[idx]&#10;        node.idx = i&#10;        node.pal_indices.append(i)&#10;    res = []&#10;    for i, w in enumerate(words):&#10;        node = root&#10;        valid = True&#10;        for j in range(len(w)):&#10;            if node.idx != -1 and node.idx != i and is_pal(w, j, len(w)-1):&#10;                res.append([i, node.idx])&#10;            idx = ord(w[j]) - 97&#10;            if not node.links[idx]:&#10;                valid = False&#10;                break&#10;            node = node.links[idx]&#10;        if valid:&#10;            for pid in node.pal_indices:&#10;                if i != pid: res.append([i, pid])&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">9</td>
      <td rowspan="1">Trie 09 Print Anagrams Together<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/print-anagrams-together/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Trie with sorted string.</td>
      <td><b>Time:</b> O(N * K log K)<br><b>Space:</b> O(N * K)</td>
      <td>Sort each string to form a key. Insert the sorted key into the Trie. At the end node of the key in the Trie, store a list of indices representing the original strings that map to this key.<br><br><b>Dependencies:</b> Trie</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class TrieNode:&#10;    def __init__(self):&#10;        self.children = {}&#10;        self.indices = []&#10;class Solution:&#10;    def Anagrams(self, string_list):&#10;        root = TrieNode()&#10;        for i, word in enumerate(string_list):&#10;            sorted_word = &quot;&quot;.join(sorted(word))&#10;            node = root&#10;            for char in sorted_word:&#10;                if char not in node.children:&#10;                    node.children[char] = TrieNode()&#10;                node = node.children[char]&#10;            node.indices.append(i)&#10;        ans = []&#10;        def traverse(node):&#10;            if node.indices:&#10;                ans.append([string_list[i] for i in node.indices])&#10;            for child in node.children.values():&#10;                traverse(child)&#10;        traverse(root)&#10;        return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">10</td>
      <td rowspan="1">Trie 10 Maximum Xor Subarray<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/maximum-xor-subarray/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Trie + Prefix XOR.</td>
      <td><b>Time:</b> O(N * 32)<br><b>Space:</b> O(N * 32)</td>
      <td>Compute prefix XORs. For each prefix XOR `curr_xor`, insert it into a Trie. Then, query the Trie to find the maximum XOR of `curr_xor` with any previously inserted prefix XOR (by trying to follow the opposite bit path). The maximum value over all queries is the answer.<br><br><b>Dependencies:</b> Trie</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class Node:&#10;    def __init__(self):&#10;        self.links = [None, None]&#10;class Trie:&#10;    def __init__(self):&#10;        self.root = Node()&#10;    def insert(self, num):&#10;        node = self.root&#10;        for i in range(31, -1, -1):&#10;            bit = (num &gt;&gt; i) &amp; 1&#10;            if not node.links[bit]:&#10;                node.links[bit] = Node()&#10;            node = node.links[bit]&#10;    def getMax(self, num):&#10;        node = self.root&#10;        maxNum = 0&#10;        for i in range(31, -1, -1):&#10;            bit = (num &gt;&gt; i) &amp; 1&#10;            if node.links[1 - bit]:&#10;                maxNum |= (1 &lt;&lt; i)&#10;                node = node.links[1 - bit]&#10;            else:&#10;                node = node.links[bit]&#10;        return maxNum&#10;def maxSubarrayXOR(N, arr):&#10;    trie = Trie()&#10;    trie.insert(0)&#10;    max_xor, curr_xor = float(&#x27;-inf&#x27;), 0&#10;    for num in arr:&#10;        curr_xor ^= num&#10;        trie.insert(curr_xor)&#10;        max_xor = max(max_xor, trie.getMax(curr_xor))&#10;    return max_xor</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">11</td>
      <td rowspan="1">Trie 11 Design Add And Search Words Data Structure<br><br></b> <a href="https://leetcode.com/problems/design-add-and-search-words-data-structure/" target="_blank">LeetCode 211</a></td>
      <td rowspan="1"><b>Example 1:</b> Backtracking with Trie.</td>
      <td><b>Time:</b> O(Word Length) for Add, O(26^Dots * Word Length) for Search<br><b>Space:</b> O(Total Chars)</td>
      <td>Add words normally to the Trie. When searching, if the current character is '.', iterate over all 26 possible children and recursively search the remaining word. If any path returns true, the word is found.<br><br><b>Dependencies:</b> Trie</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class TrieNode:&#10;    def __init__(self):&#10;        self.children = {}&#10;        self.isEnd = False&#10;class WordDictionary:&#10;    def __init__(self):&#10;        self.root = TrieNode()&#10;    def addWord(self, word: str) -&gt; None:&#10;        node = self.root&#10;        for char in word:&#10;            if char not in node.children:&#10;                node.children[char] = TrieNode()&#10;            node = node.children[char]&#10;        node.isEnd = True&#10;    def search(self, word: str) -&gt; bool:&#10;        def searchInNode(i, node):&#10;            if not node: return False&#10;            if i == len(word): return node.isEnd&#10;            if word[i] != &#x27;.&#x27;:&#10;                if word[i] not in node.children: return False&#10;                return searchInNode(i + 1, node.children[word[i]])&#10;            for child in node.children.values():&#10;                if searchInNode(i + 1, child): return True&#10;            return False&#10;        return searchInNode(0, self.root)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">12</td>
      <td rowspan="1">Trie 12 Implement Magic Dictionary<br><br></b> <a href="https://leetcode.com/problems/implement-magic-dictionary/" target="_blank">LeetCode 676</a></td>
      <td rowspan="1"><b>Example 1:</b> Recursive Trie Search.</td>
      <td><b>Time:</b> O(N) Add, O(N * 26) Search<br><b>Space:</b> O(Total Chars)</td>
      <td>Store dictionary in a Trie. For searching, recursively traverse the Trie. Maintain a `modified` boolean flag. If characters mismatch, set `modified` to true and continue. If we reach the end of the word and `modified` is true, return true.<br><br><b>Dependencies:</b> Trie</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class TrieNode:&#10;    def __init__(self):&#10;        self.children = {}&#10;        self.isEnd = False&#10;class MagicDictionary:&#10;    def __init__(self):&#10;        self.root = TrieNode()&#10;    def buildDict(self, dictionary: list[str]) -&gt; None:&#10;        for word in dictionary:&#10;            node = self.root&#10;            for char in word:&#10;                if char not in node.children:&#10;                    node.children[char] = TrieNode()&#10;                node = node.children[char]&#10;            node.isEnd = True&#10;    def search(self, searchWord: str) -&gt; bool:&#10;        def dfs(i, node, modified):&#10;            if i == len(searchWord): return modified and node.isEnd&#10;            if modified:&#10;                if searchWord[i] in node.children:&#10;                    return dfs(i + 1, node.children[searchWord[i]], True)&#10;                return False&#10;            for char, child in node.children.items():&#10;                if dfs(i + 1, child, char != searchWord[i]): return True&#10;            return False&#10;        return dfs(0, self.root, False)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">13</td>
      <td rowspan="1">Trie 13 Find All Words In A Matrix<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/find-all-words-in-a-matrix/1" target="_blank">GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Trie + DFS.</td>
      <td><b>Time:</b> O(N * M * 4^L) where L is max word length<br><b>Space:</b> O(Total Chars in Dict)</td>
      <td>Build a Trie from the dictionary. Perform DFS from every cell in the matrix. During DFS, traverse the Trie simultaneously. If `node.word` is found, add it to result and clear `node.word` to prevent duplicates. Mark visited cells to avoid loops.<br><br><b>Dependencies:</b> Trie</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class TrieNode:&#10;    def __init__(self):&#10;        self.children = {}&#10;        self.word = &quot;&quot;&#10;class Solution:&#10;    def findWords(self, board: list[list[str]], words: list[str]) -&gt; list[str]:&#10;        root = TrieNode()&#10;        for w in words:&#10;            node = root&#10;            for c in w:&#10;                if c not in node.children:&#10;                    node.children[c] = TrieNode()&#10;                node = node.children[c]&#10;            node.word = w&#10;        ans = []&#10;        def dfs(i, j, node):&#10;            c = board[i][j]&#10;            if c == &#x27;#&#x27; or c not in node.children: return&#10;            node = node.children[c]&#10;            if node.word:&#10;                ans.append(node.word)&#10;                node.word = &quot;&quot;&#10;            board[i][j] = &#x27;#&#x27;&#10;            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:&#10;                r, c_nxt = i + dr, j + dc&#10;                if 0 &lt;= r &lt; len(board) and 0 &lt;= c_nxt &lt; len(board[0]):&#10;                    dfs(r, c_nxt, node)&#10;            board[i][j] = c&#10;        for i in range(len(board)):&#10;            for j in range(len(board[0])):&#10;                dfs(i, j, root)&#10;        return sorted(ans)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">14</td>
      <td rowspan="1">Trie 14 Replace Words<br><br></b> <a href="https://leetcode.com/problems/replace-words/" target="_blank">LeetCode 648</a></td>
      <td rowspan="1"><b>Example 1:</b> Trie matching.</td>
      <td><b>Time:</b> O(N * W)<br><b>Space:</b> O(Total Chars in Dict + Sentence Length)</td>
      <td>Insert all dictionary roots into a Trie. For each word in the sentence, search the Trie. If a prefix matches a root (i.e., `isEnd` becomes true), replace the word with the root. If no root matches, keep the original word.<br><br><b>Dependencies:</b> Trie</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class TrieNode:&#10;    def __init__(self):&#10;        self.children = {}&#10;        self.isEnd = False&#10;class Solution:&#10;    def replaceWords(self, dictionary: list[str], sentence: str) -&gt; str:&#10;        root = TrieNode()&#10;        for word in dictionary:&#10;            node = root&#10;            for char in word:&#10;                if char not in node.children:&#10;                    node.children[char] = TrieNode()&#10;                node = node.children[char]&#10;            node.isEnd = True&#10;        def findRoot(word):&#10;            node = root&#10;            prefix = &quot;&quot;&#10;            for char in word:&#10;                if char not in node.children: break&#10;                prefix += char&#10;                node = node.children[char]&#10;                if node.isEnd: return prefix&#10;            return word&#10;        return &quot; &quot;.join(findRoot(word) for word in sentence.split())</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">15</td>
      <td rowspan="1">Trie 15 Longest Word In Dictionary<br><br></b> <a href="https://leetcode.com/problems/longest-word-in-dictionary/" target="_blank">LeetCode 720</a></td>
      <td rowspan="1"><b>Example 1:</b> Trie + DFS.</td>
      <td><b>Time:</b> O(Total Chars)<br><b>Space:</b> O(Total Chars)</td>
      <td>Insert all words into a Trie, marking the end of each word. Perform DFS on the Trie. Only proceed to children that are marked as the end of a word (i.e., `isEnd == true`). Keep track of the longest string found during DFS.<br><br><b>Dependencies:</b> Trie</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class TrieNode:&#10;    def __init__(self):&#10;        self.children = {}&#10;        self.isEnd = False&#10;        self.word = &quot;&quot;&#10;class Solution:&#10;    def longestWord(self, words: list[str]) -&gt; str:&#10;        root = TrieNode()&#10;        for w in words:&#10;            node = root&#10;            for c in w:&#10;                if c not in node.children:&#10;                    node.children[c] = TrieNode()&#10;                node = node.children[c]&#10;            node.isEnd = True&#10;            node.word = w&#10;        longest = &quot;&quot;&#10;        def dfs(node):&#10;            nonlocal longest&#10;            if node.isEnd:&#10;                if len(node.word) &gt; len(longest) or (len(node.word) == len(longest) and node.word &lt; longest):&#10;                    longest = node.word&#10;            for child in node.children.values():&#10;                if child.isEnd:&#10;                    dfs(child)&#10;        for child in root.children.values():&#10;            if child.isEnd:&#10;                dfs(child)&#10;        return longest</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">16</td>
      <td rowspan="1">Trie 16 Camelcase Matching<br><br></b> <a href="https://leetcode.com/problems/camelcase-matching/" target="_blank">LeetCode 1023</a></td>
      <td rowspan="1"><b>Example 1:</b> Trie matching.</td>
      <td><b>Time:</b> O(N * M)<br><b>Space:</b> O(1) excluding output</td>
      <td>Build a Trie with the queries (optional, can also be done linearly). Better approach: for each query, match characters with pattern. If characters match, increment pattern index. If characters mismatch and query character is uppercase, it's a mismatch. Finally, check if pattern index reached pattern length.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def camelMatch(queries, pattern):&#10;    ans = []&#10;    for q in queries:&#10;        i = 0&#10;        match = True&#10;        for c in q:&#10;            if i &lt; len(pattern) and c == pattern[i]: i += 1&#10;            elif c.isupper():&#10;                match = False&#10;                break&#10;        if i &lt; len(pattern): match = False&#10;        ans.append(match)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">17</td>
      <td rowspan="1">Trie 17 Prefix And Suffix Search<br><br></b> <a href="https://leetcode.com/problems/prefix-and-suffix-search/" target="_blank">LeetCode 745</a></td>
      <td rowspan="1"><b>Example 1:</b> Suffix + '{' + Prefix Trie.</td>
      <td><b>Time:</b> O(N * K^2) Insert, O(K) Search<br><b>Space:</b> O(N * K^2)</td>
      <td>For each word, generate all possible suffixes, append a special character '{', and then append the original word. Insert all these combinations into a Trie along with the index. When querying, search for `suffix + '{' + prefix` in the Trie.<br><br><b>Dependencies:</b> Trie</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class TrieNode:&#10;    def __init__(self):&#10;        self.children = {}&#10;        self.index = -1&#10;class WordFilter:&#10;    def __init__(self, words: list[str]):&#10;        self.root = TrieNode()&#10;        for i, w in enumerate(words):&#10;            for j in range(len(w) + 1):&#10;                s = w[j:] + &quot;{&quot; + w&#10;                node = self.root&#10;                for char in s:&#10;                    if char not in node.children:&#10;                        node.children[char] = TrieNode()&#10;                    node = node.children[char]&#10;                    node.index = i&#10;    def f(self, pref: str, suff: str) -&gt; int:&#10;        s = suff + &quot;{&quot; + pref&#10;        node = self.root&#10;        for char in s:&#10;            if char not in node.children: return -1&#10;            node = node.children[char]&#10;        return node.index</code></pre></details></td>
    </tr>
  </tbody>
</table>


## Patterns

<p><b>Note:</b> All patterns share a common complexity of <b>Time: O(N<sup>2</sup>)</b> and <b>Space: O(1)</b>. The approach involves standard nested loops for row and column printing.</p>
<table border="1">
  <thead>
    <tr>
      <th style="width: 5%;">S.No</th>
      <th style="width: 25%;">Problem Name</th>
      <th style="width: 30%;">Example & Constraints</th>
      <th style="width: 40%;">Logic</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Pat 01 Rectangular Star</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code>Example 1:&#10;Input: N = 3&#10;Output:&#10;***&#10;***&#10;***&#10;&#10;Example 2:&#10;Input: N = 5&#10;Output:&#10;*****&#10;*****&#10;*****&#10;*****&#10;*****</code></pre><br><br><b>Note (Constraint):</b> 1 &le; N &le; 20</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(n):&#10;        print(&quot;*&quot; * n)</code></pre></details></td>
    </tr>
    <tr>
      <td>2</td>
      <td>Pat 02 Right Angled Triangle</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code>Example 1:&#10;Input: N = 3&#10;Output:&#10;*&#10;**&#10;***&#10;&#10;Example 2:&#10;Input: N = 5&#10;Output:&#10;*&#10;**&#10;***&#10;****&#10;*****</code></pre><br><br><b>Note (Constraint):</b> 1 &le; N &le; 20</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(1, n + 1):&#10;        print(&quot;* &quot; * i)</code></pre></details></td>
    </tr>
    <tr>
      <td>3</td>
      <td>Pat 03 Right Angled Number Pyramid</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code>Example 1:&#10;Input: N = 3&#10;Output:&#10;1&#10;1 2&#10;1 2 3&#10;&#10;Example 2:&#10;Input: N = 5&#10;Output:&#10;1&#10;1 2&#10;1 2 3&#10;1 2 3 4&#10;1 2 3 4 5</code></pre><br><br><b>Note (Constraint):</b> 1 &le; N &le; 20</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(1, n + 1):&#10;        for j in range(1, i + 1):&#10;            print(j, end=&quot; &quot;)&#10;        print()</code></pre></details></td>
    </tr>
    <tr>
      <td>4</td>
      <td>Pat 04 Right Angled Number Pyramid II</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code>Example 1:&#10;Input: N = 3&#10;Output:&#10;1&#10;2 2&#10;3 3 3&#10;&#10;Example 2:&#10;Input: N = 5&#10;Output:&#10;1&#10;2 2&#10;3 3 3&#10;4 4 4 4&#10;5 5 5 5 5</code></pre><br><br><b>Note (Constraint):</b> 1 &le; N &le; 20</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(1, n + 1):&#10;        for j in range(1, i + 1):&#10;            print(i, end=&quot; &quot;)&#10;        print()</code></pre></details></td>
    </tr>
    <tr>
      <td>5</td>
      <td>Pat 05 Inverted Right Pyramid</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code>Example 1:&#10;Input: N = 3&#10;Output:&#10;* * *&#10;* *&#10;*&#10;&#10;Example 2:&#10;Input: N = 5&#10;Output:&#10;* * * * *&#10;* * * *&#10;* * *&#10;* *&#10;*</code></pre><br><br><b>Note (Constraint):</b> 1 &le; N &le; 20</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(n, 0, -1):&#10;        print(&quot;* &quot; * i)</code></pre></details></td>
    </tr>
    <tr>
      <td>6</td>
      <td>Pat 06 Inverted Numbered Right Pyramid</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code>Example 1:&#10;Input: N = 3&#10;Output:&#10;1 2 3&#10;1 2&#10;1&#10;&#10;Example 2:&#10;Input: N = 5&#10;Output:&#10;1 2 3 4 5&#10;1 2 3 4&#10;1 2 3&#10;1 2&#10;1</code></pre><br><br><b>Note (Constraint):</b> 1 &le; N &le; 20</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(n, 0, -1):&#10;        for j in range(1, i + 1):&#10;            print(j, end=&quot; &quot;)&#10;        print()</code></pre></details></td>
    </tr>
    <tr>
      <td>7</td>
      <td>Pat 07 Star Pyramid</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code>Example 1:&#10;Input: N = 3&#10;Output:&#10;  *&#10; ***&#10;*****&#10;&#10;Example 2:&#10;Input: N = 5&#10;Output:&#10;    *&#10;   ***&#10;  *****&#10; *******&#10;*********</code></pre><br><br><b>Note (Constraint):</b> 1 &le; N &le; 20</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(n):&#10;        spaces = &quot; &quot; * (n - i - 1)&#10;        stars = &quot;*&quot; * (2 * i + 1)&#10;        print(spaces + stars + spaces)</code></pre></details></td>
    </tr>
    <tr>
      <td>8</td>
      <td>Pat 08 Inverted Star Pyramid</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code>Example 1:&#10;Input: N = 3&#10;Output:&#10;*****&#10; ***&#10;  *&#10;&#10;Example 2:&#10;Input: N = 5&#10;Output:&#10;*********&#10; *******&#10;  *****&#10;   ***&#10;    *</code></pre><br><br><b>Note (Constraint):</b> 1 &le; N &le; 20</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(n):&#10;        spaces = &quot; &quot; * i&#10;        stars = &quot;*&quot; * (2 * (n - i) - 1)&#10;        print(spaces + stars + spaces)</code></pre></details></td>
    </tr>
    <tr>
      <td>9</td>
      <td>Pat 09 Diamond Star Pattern</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code>Example 1:&#10;Input: N = 3&#10;Output:&#10;  *&#10; ***&#10;*****&#10;*****&#10; ***&#10;  *&#10;</code></pre><br><br><b>Note (Constraint):</b> 1 &le; N &le; 20</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(n):&#10;        spaces = &quot; &quot; * (n - i - 1)&#10;        stars = &quot;*&quot; * (2 * i + 1)&#10;        print(spaces + stars + spaces)&#10;    for i in range(n):&#10;        spaces = &quot; &quot; * i&#10;        stars = &quot;*&quot; * (2 * (n - i) - 1)&#10;        print(spaces + stars + spaces)</code></pre></details></td>
    </tr>
    <tr>
      <td>10</td>
      <td>Pat 10 Half Diamond Star Pattern</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code>Example 1:&#10;Input: N = 3&#10;Output:&#10;*&#10;**&#10;***&#10;**&#10;*&#10;</code></pre><br><br><b>Note (Constraint):</b> 1 &le; N &le; 20</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(1, 2 * n):&#10;        stars = i if i &lt;= n else 2 * n - i&#10;        print(&quot;*&quot; * stars)</code></pre></details></td>
    </tr>
    <tr>
      <td>11</td>
      <td>Pat 11 Binary Number Triangle</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code>Example 1:&#10;Input: N = 3&#10;Output:&#10;1&#10;0 1&#10;1 0 1&#10;</code></pre><br><br><b>Note (Constraint):</b> 1 &le; N &le; 20</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(n):&#10;        start = 1 if i % 2 == 0 else 0&#10;        for j in range(i + 1):&#10;            print(start, end=&quot; &quot;)&#10;            start = 1 - start&#10;        print()</code></pre></details></td>
    </tr>
    <tr>
      <td>12</td>
      <td>Pat 12 Number Crown Pattern</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code>Example 1:&#10;Input: N = 3&#10;Output:&#10;1    1&#10;12  21&#10;123321</code></pre><br><br><b>Note (Constraint):</b> 1 &le; N &le; 20</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    space = 2 * (n - 1)&#10;    for i in range(1, n + 1):&#10;        for j in range(1, i + 1):&#10;            print(j, end=&quot;&quot;)&#10;        print(&quot; &quot; * space, end=&quot;&quot;)&#10;        for j in range(i, 0, -1):&#10;            print(j, end=&quot;&quot;)&#10;        print()&#10;        space -= 2</code></pre></details></td>
    </tr>
    <tr>
      <td>13</td>
      <td>Pat 13 Increasing Number Triangle</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code>Example 1:&#10;Input: N = 3&#10;Output:&#10;1&#10;2 3&#10;4 5 6</code></pre><br><br><b>Note (Constraint):</b> 1 &le; N &le; 20</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    num = 1&#10;    for i in range(1, n + 1):&#10;        for j in range(1, i + 1):&#10;            print(num, end=&quot; &quot;)&#10;            num += 1&#10;        print()</code></pre></details></td>
    </tr>
    <tr>
      <td>14</td>
      <td>Pat 14 Increasing Letter Triangle</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code>Example 1:&#10;Input: N = 3&#10;Output:&#10;A&#10;A B&#10;A B C</code></pre><br><br><b>Note (Constraint):</b> 1 &le; N &le; 20</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(n):&#10;        for j in range(i + 1):&#10;            print(chr(ord(&#x27;A&#x27;) + j), end=&quot; &quot;)&#10;        print()</code></pre></details></td>
    </tr>
    <tr>
      <td>15</td>
      <td>Pat 15 Reverse Letter Triangle</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code>Example 1:&#10;Input: N = 3&#10;Output:&#10;A B C&#10;A B&#10;A</code></pre><br><br><b>Note (Constraint):</b> 1 &le; N &le; 20</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(n):&#10;        for j in range(n - i):&#10;            print(chr(ord(&#x27;A&#x27;) + j), end=&quot; &quot;)&#10;        print()</code></pre></details></td>
    </tr>
    <tr>
      <td>16</td>
      <td>Pat 16 Alpha Ramp Pattern</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code>Example 1:&#10;Input: N = 3&#10;Output:&#10;A&#10;B B&#10;C C C</code></pre><br><br><b>Note (Constraint):</b> 1 &le; N &le; 20</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(n):&#10;        ch = chr(ord(&#x27;A&#x27;) + i)&#10;        for j in range(i + 1):&#10;            print(ch, end=&quot; &quot;)&#10;        print()</code></pre></details></td>
    </tr>
    <tr>
      <td>17</td>
      <td>Pat 17 Alpha Hill Pattern</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code>Example 1:&#10;Input: N = 3&#10;Output:&#10;  A&#10; ABA&#10;ABCBA</code></pre><br><br><b>Note (Constraint):</b> 1 &le; N &le; 20</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(n):&#10;        spaces = &quot; &quot; * (n - i - 1)&#10;        print(spaces, end=&quot;&quot;)&#10;        ch = ord(&#x27;A&#x27;)&#10;        breakpoint = (2 * i + 1) // 2&#10;        for j in range(1, 2 * i + 2):&#10;            print(chr(ch), end=&quot;&quot;)&#10;            if j &lt;= breakpoint:&#10;                ch += 1&#10;            else:&#10;                ch -= 1&#10;        print(spaces)</code></pre></details></td>
    </tr>
    <tr>
      <td>18</td>
      <td>Pat 18 Alpha Triangle</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code>Example 1:&#10;Input: N = 3&#10;Output:&#10;C&#10;C B&#10;C B A</code></pre><br><br><b>Note (Constraint):</b> 1 &le; N &le; 20</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(n):&#10;        ch = ord(&#x27;A&#x27;) + n - 1&#10;        for j in range(i + 1):&#10;            print(chr(ch - i + j), end=&quot; &quot;)&#10;        print()</code></pre></details></td>
    </tr>
    <tr>
      <td>19</td>
      <td>Pat 19 Symmetric Void Pattern</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code>Example 1:&#10;Input: N = 3&#10;Output:&#10;******&#10;**  **&#10;*    *&#10;*    *&#10;**  **&#10;******</code></pre><br><br><b>Note (Constraint):</b> 1 &le; N &le; 20</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    iniSpace = 0&#10;    for i in range(n):&#10;        print(&quot;*&quot; * (n - i) + &quot; &quot; * iniSpace + &quot;*&quot; * (n - i))&#10;        iniSpace += 2&#10;    iniSpace = 2 * n - 2&#10;    for i in range(1, n + 1):&#10;        print(&quot;*&quot; * i + &quot; &quot; * iniSpace + &quot;*&quot; * i)&#10;        iniSpace -= 2</code></pre></details></td>
    </tr>
    <tr>
      <td>20</td>
      <td>Pat 20 Symmetric Butterfly Pattern</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code>Example 1:&#10;Input: N = 3&#10;Output:&#10;*    *&#10;**  **&#10;******&#10;**  **&#10;*    *</code></pre><br><br><b>Note (Constraint):</b> 1 &le; N &le; 20</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    spaces = 2 * n - 2&#10;    for i in range(1, 2 * n):&#10;        stars = i if i &lt;= n else 2 * n - i&#10;        print(&quot;*&quot; * stars + &quot; &quot; * spaces + &quot;*&quot; * stars)&#10;        if i &lt; n:&#10;            spaces -= 2&#10;        else:&#10;            spaces += 2</code></pre></details></td>
    </tr>
    <tr>
      <td>21</td>
      <td>Pat 21 Hollow Rectangle Pattern</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code>Example 1:&#10;Input: N = 3&#10;Output:&#10;***&#10;* *&#10;***</code></pre><br><br><b>Note (Constraint):</b> 1 &le; N &le; 20</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(n):&#10;        for j in range(n):&#10;            if i == 0 or j == 0 or i == n - 1 or j == n - 1:&#10;                print(&quot;*&quot;, end=&quot;&quot;)&#10;            else:&#10;                print(&quot; &quot;, end=&quot;&quot;)&#10;        print()</code></pre></details></td>
    </tr>
    <tr>
      <td>22</td>
      <td>Pat 22 The Number Pattern</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code>Example 1:&#10;Input: N = 3&#10;Output:&#10;3 3 3 3 3&#10;3 2 2 2 3&#10;3 2 1 2 3&#10;3 2 2 2 3&#10;3 3 3 3 3</code></pre><br><br><b>Note (Constraint):</b> 1 &le; N &le; 20</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(2 * n - 1):&#10;        for j in range(2 * n - 1):&#10;            top = i&#10;            left = j&#10;            right = (2 * n - 2) - j&#10;            down = (2 * n - 2) - i&#10;            print(n - min(top, left, right, down), end=&quot; &quot;)&#10;        print()</code></pre></details></td>
    </tr>
  </tbody>
</table>


