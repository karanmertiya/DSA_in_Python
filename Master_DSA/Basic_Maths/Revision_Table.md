# Basic Maths Revision Table

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
      <td>Math 06 Factorial Trailing Zeroes<br><br></b> <a href="https://leetcode.com/problems/factorial-trailing-zeroes/" target="_blank">LeetCode 172</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td>**Example 1:** Counting 5s.</td>
      <td><b>Time:</b> O(log_5(N))<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Trailing zeroes are produced by 10s, which are pairs of 2 and 5. Since 2s are more frequent, we just count the number of 5s in prime factors of numbers up to N. This is `N/5 + N/25 + N/125 + ...`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def trailingZeroes(n: int) -&gt; int:&#10;    count = 0&#10;    while n &gt; 0:&#10;        count += n // 5&#10;        n //= 5&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td>7</td>
      <td>Math 07 Count Primes<br><br></b> <a href="https://leetcode.com/problems/count-primes/" target="_blank">LeetCode 204</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td>**Example 1:** Sieve of Eratosthenes.</td>
      <td><b>Time:</b> O(N log(log N))<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Use the Sieve of Eratosthenes. Initialize a boolean array of size `n` with `true`. Mark `0` and `1` as `false`. For each `i` from `2` to `sqrt(n)`, if `i` is prime, mark its multiples as `false` starting from `i*i`. Finally, count the number of `true`s.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def countPrimes(n: int) -&gt; int:&#10;    if n &lt;= 2: return 0&#10;    isPrime = [True] * n&#10;    isPrime[0] = isPrime[1] = False&#10;    for i in range(2, int(n ** 0.5) + 1):&#10;        if isPrime[i]:&#10;            for j in range(i * i, n, i):&#10;                isPrime[j] = False&#10;    return sum(isPrime)</code></pre></details></td>
    </tr>
    <tr>
      <td>8</td>
      <td>Math 08 Valid Perfect Square<br><br></b> <a href="https://leetcode.com/problems/valid-perfect-square/" target="_blank">LeetCode 367</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td>**Example 1:** Binary Search.</td>
      <td><b>Time:</b> O(log N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Use binary search from `1` to `num/2` or up to `46340` (sqrt of INT_MAX). If `mid * mid == num`, return true. Else if `mid * mid < num`, `low = mid + 1`. Else `high = mid - 1`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isPerfectSquare(num: int) -&gt; bool:&#10;    if num == 1: return True&#10;    low, high = 1, num // 2&#10;    while low &lt;= high:&#10;        mid = (low + high) // 2&#10;        sq = mid * mid&#10;        if sq == num: return True&#10;        elif sq &lt; num: low = mid + 1&#10;        else: high = mid - 1&#10;    return False</code></pre></details></td>
    </tr>
    <tr>
      <td>9</td>
      <td>Math 09 Power Of Two<br><br></b> <a href="https://leetcode.com/problems/power-of-two/" target="_blank">LeetCode 231</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, SDE Sheet, Striver A Z</details></td>
      <td>**Example 1:** Bit Manipulation.</td>
      <td><b>Time:</b> O(1)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> If a number is a power of two, it has exactly one bit set in its binary representation. The expression `n & (n - 1)` clears the lowest set bit. Thus, if `n > 0` and `(n & (n - 1)) == 0`, it is a power of two.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isPowerOfTwo(n: int) -&gt; bool:&#10;    return n &gt; 0 and (n &amp; (n - 1)) == 0</code></pre></details></td>
    </tr>
    <tr>
      <td>10</td>
      <td>Math 10 Power Of Three<br><br></b> <a href="https://leetcode.com/problems/power-of-three/" target="_blank">LeetCode 326</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td>**Example 1:** Modulo with largest power.</td>
      <td><b>Time:</b> O(1)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Since `n` is a 32-bit signed integer, the largest power of 3 that fits is `3^19 = 1162261467`. A number `n` is a power of 3 if `n > 0` and `1162261467 % n == 0`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isPowerOfThree(n: int) -&gt; bool:&#10;    return n &gt; 0 and 1162261467 % n == 0</code></pre></details></td>
    </tr>
    <tr>
      <td>11</td>
      <td>Math 11 Power Of Four<br><br></b> <a href="https://leetcode.com/problems/power-of-four/" target="_blank">LeetCode 342</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td>**Example 1:** Bit Manipulation.</td>
      <td><b>Time:</b> O(1)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> A power of 4 is also a power of 2, so `n > 0 && (n & (n-1)) == 0` must hold. Also, the single set bit must be at an even position (0-indexed). The mask `0x55555555` has 1s at all even positions. So `(n & 0x55555555) != 0`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isPowerOfFour(n: int) -&gt; bool:&#10;    return n &gt; 0 and (n &amp; (n - 1)) == 0 and (n &amp; 0x55555555) != 0</code></pre></details></td>
    </tr>
    <tr>
      <td>12</td>
      <td>Math 12 Add Digits<br><br></b> <a href="https://leetcode.com/problems/add-digits/" target="_blank">LeetCode 258</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td>**Example 1:** Digital Root.</td>
      <td><b>Time:</b> O(1)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> This is known as the digital root. The formula is `1 + (n - 1) % 9`. If `n == 0`, return `0`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def addDigits(num: int) -&gt; int:&#10;    if num == 0: return 0&#10;    return 1 + (num - 1) % 9</code></pre></details></td>
    </tr>
    <tr>
      <td>13</td>
      <td>Math 13 Ugly Number<br><br></b> <a href="https://leetcode.com/problems/ugly-number/" target="_blank">LeetCode 263</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td>**Example 1:** Division.</td>
      <td><b>Time:</b> O(log N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> If `n <= 0`, return false. Divide `n` by 2, 3, and 5 as long as it is divisible. If the remaining number is 1, it's an ugly number, else false.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isUgly(n: int) -&gt; bool:&#10;    if n &lt;= 0: return False&#10;    for p in [2, 3, 5]:&#10;        while n % p == 0:&#10;            n //= p&#10;    return n == 1</code></pre></details></td>
    </tr>
    <tr>
      <td>14</td>
      <td>Math 14 Perfect Number<br><br></b> <a href="https://leetcode.com/problems/perfect-number/" target="_blank">LeetCode 507</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td>**Example 1:** Sum of divisors.</td>
      <td><b>Time:</b> O(sqrt(N))<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> If `num <= 1`, return false. Iterate up to `sqrt(num)`. If `i` divides `num`, add `i` and `num/i` to the sum. After the loop, compare sum with `num`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def checkPerfectNumber(num: int) -&gt; bool:&#10;    if num &lt;= 1: return False&#10;    total = 1&#10;    for i in range(2, int(num ** 0.5) + 1):&#10;        if num % i == 0:&#10;            total += i&#10;            if i * i != num: total += num // i&#10;    return total == num</code></pre></details></td>
    </tr>
    <tr>
      <td>15</td>
      <td>Math 15 Excel Sheet Column Title<br><br></b> <a href="https://leetcode.com/problems/excel-sheet-column-title/" target="_blank">LeetCode 168</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td>**Example 1:** Base 26 conversion.</td>
      <td><b>Time:</b> O(log_26(N))<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> This is essentially base 26 conversion, but 1-indexed (A=1, B=2, Z=26). To make it 0-indexed, decrement `columnNumber` by 1 at each step, get the remainder modulo 26, convert to character, and divide by 26.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def convertToTitle(columnNumber: int) -&gt; str:&#10;    res = []&#10;    while columnNumber &gt; 0:&#10;        columnNumber -= 1&#10;        res.append(chr(ord(&#x27;A&#x27;) + (columnNumber % 26)))&#10;        columnNumber //= 26&#10;    return &quot;&quot;.join(res[::-1])</code></pre></details></td>
    </tr>
    <tr>
      <td>16</td>
      <td>Math 16 Pow X N<br><br></b> <a href="https://leetcode.com/problems/powx-n/" target="_blank">LeetCode 50</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, SDE Sheet, Striver A Z</details></td>
      <td>**Example 1:** Binary Exponentiation.</td>
      <td><details><summary><b>Approach 1</b></summary><b>Time:</b> O(N)<br><b>Space:</b> O(1)</details><details><summary><b>Approach 2</b></summary><b>Time:</b> O(log N)<br><b>Space:</b> O(1)</details></td>
      <td><details><summary><b>Approach 1</b></summary><b>Explanation:</b> Brute Force: Loop n times and multiply ans by x.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def myPow(x: float, n: int) -&gt; float:&#10;    ans = 1.0&#10;    nn = abs(n)&#10;    for _ in range(nn):&#10;        ans *= x&#10;    return 1.0 / ans if n &lt; 0 else ans</code></pre></details></details><details><summary><b>Approach 2</b></summary><b>Explanation:</b> Optimal: Binary Exponentiation. If n is even, x = x*x, n = n/2. If odd, ans = ans*x, n = n-1.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def myPow(x, n):&#10;    ans, nn = 1.0, abs(n)&#10;    while nn &gt; 0:&#10;        if nn % 2 == 1:&#10;            ans *= x&#10;            nn -= 1&#10;        else:&#10;            x *= x&#10;            nn //= 2&#10;    return ans if n &gt;= 0 else 1.0 / ans</code></pre></details></details></td>
    </tr>
    <tr>
      <td>17</td>
      <td>Math 17 Sieve Of Eratosthenes<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/sieve-of-eratosthenes5242/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td>**Example 1:** Classic implementation.</td>
      <td><b>Time:</b> O(N log(log N))<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Same as `countPrimes`, but return the actual prime numbers in a list instead of just the count.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def sieveOfEratosthenes(N):&#10;    is_prime = [True] * (N + 1)&#10;    is_prime[0] = is_prime[1] = False&#10;    for i in range(2, int(N**0.5) + 1):&#10;        if is_prime[i]:&#10;            for j in range(i*i, N + 1, i):&#10;                is_prime[j] = False&#10;    return [i for i in range(2, N + 1) if is_prime[i]]</code></pre></details></td>
    </tr>
    <tr>
      <td>18</td>
      <td>Math 18 Prime Factors<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/prime-factors5052/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z</details></td>
      <td>**Example 1:** Iterative division.</td>
      <td><b>Time:</b> O(sqrt(N))<br><b>Space:</b> O(1) excluding output</td>
      <td><b>Explanation:</b> Iterate from `i = 2` to `sqrt(N)`. If `N % i == 0`, `i` is a prime factor. Add `i` to result, and repeatedly divide `N` by `i` until it's no longer divisible. After the loop, if `N > 1`, then `N` itself is a prime factor and should be added.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def AllPrimeFactors(N):&#10;    ans = []&#10;    for i in range(2, int(N**0.5) + 1):&#10;        if N % i == 0:&#10;            ans.append(i)&#10;            while N % i == 0: N //= i&#10;    if N &gt; 1: ans.append(N)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>19</td>
      <td>Math 19 Print All Divisors<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/print-all-divisors-of-a-number/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z</details></td>
      <td>**Example 1:** Iterate up to sqrt(N).</td>
      <td><details><summary><b>Approach 1</b></summary><b>Time:</b> O(N)<br><b>Space:</b> O(1)</details><details><summary><b>Approach 2</b></summary><b>Time:</b> O(sqrt(N) + k log k)<br><b>Space:</b> O(k)</details></td>
      <td><details><summary><b>Approach 1</b></summary><b>Explanation:</b> Brute Force: Iterate from 1 to N and check if N % i == 0.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def printDivisors(n: int):&#10;    for i in range(1, n + 1):&#10;        if n % i == 0:&#10;            print(i, end=&quot; &quot;)</code></pre></details></details><details><summary><b>Approach 2</b></summary><b>Explanation:</b> Optimal: Iterate up to sqrt(N). If 'i' divides N, then 'N/i' is also a divisor.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_divisors(n):&#10;    ans = []&#10;    for i in range(1, int(n**0.5) + 1):&#10;        if n % i == 0:&#10;            ans.append(i)&#10;            if n // i != i: ans.append(n // i)&#10;    ans.sort()&#10;    print(*(ans))</code></pre></details></details></td>
    </tr>
    <tr>
      <td>20</td>
      <td>Math 20 Armstrong Number<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/armstrong-numbers2727/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z</details></td>
      <td>**Example 1:** Math.</td>
      <td><b>Time:</b> O(log10(N))<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Extract each digit, cube it, and sum them up. If the sum equals the original number, it's an Armstrong number.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def armstrongNumber(n):&#10;    return &quot;Yes&quot; if sum(int(d)**3 for d in str(n)) == n else &quot;No&quot;</code></pre></details></td>
    </tr>
  </tbody>
</table>
