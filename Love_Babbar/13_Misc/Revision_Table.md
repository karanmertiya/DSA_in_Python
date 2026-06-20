# 13 Misc Revision Table

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
      <td><b>Example 1:</b> <br><b>Input:</b> N = 12345<br><b>Output:</b> 5</td>
      <td><details><summary><b>Approach 1</b></summary><b>Time:</b> O(1)<br><b>Space:</b> O(1)</details><details><summary><b>Approach 2</b></summary><b>Time:</b> O(log10 N)<br><b>Space:</b> O(1)</details><details><summary><b>Approach 3</b></summary><b>Time:</b> O(1)<br><b>Space:</b> O(1)</details></td>
      <td><details><summary><b>Approach 1</b></summary><b>Explanation:</b> Convert the number to a string and return its length.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def countDigits(n: int) -&gt; int:&#10;    return len(str(n))</code></pre></details></details><details><summary><b>Approach 2</b></summary><b>Explanation:</b> Use a while loop to repeatedly divide the number by 10 and increment a counter.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def countDigits(n: int) -&gt; int:&#10;    if n == 0: return 1&#10;    count = 0&#10;    while n &gt; 0:&#10;        count += 1&#10;        n //= 10&#10;    return count</code></pre></details></details><details><summary><b>Approach 3</b></summary><b>Explanation:</b> Use the base-10 logarithm function to find the number of digits mathematically.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import math&#10;def countDigits(n: int) -&gt; int:&#10;    if n == 0: return 1&#10;    return int(math.log10(n) + 1)</code></pre></details></details></td>
    </tr>
    <tr>
      <td>2</td>
      <td>Math 02 Reverse Integer<br><br></b> <a href="https://leetcode.com/problems/reverse-integer/" target="_blank">LeetCode 7</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td><b>Example 1:</b> <br><b>Input:</b> x = 123<br><b>Output:</b> 321</td>
      <td><details><summary><b>Approach 1</b></summary><b>Time:</b> O(log10 x)<br><b>Space:</b> O(1)</details><details><summary><b>Approach 2</b></summary><b>Time:</b> O(log10 x)<br><b>Space:</b> O(1)</details></td>
      <td><details><summary><b>Approach 1</b></summary><b>Explanation:</b> Strict 32-bit environment (LeetCode standard): Extract digit, check for overflow against INT_MAX/10 and INT_MIN/10 *before* multiplying ans by 10.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def reverse(x: int) -&gt; int:&#10;    sign = [1, -1][x &lt; 0]&#10;    ans = int(str(abs(x))[::-1])&#10;    return sign * ans if ans &lt;= 2**31 - 1 else 0</code></pre></details></details><details><summary><b>Approach 2</b></summary><b>Explanation:</b> Relaxed 64-bit environment: Store answer in a 64-bit integer (`long long`). At the end, check if it exceeds 32-bit bounds and return 0 if it does.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def reverse(x: int) -&gt; int:&#10;    # Python handles arbitrarily large integers natively.&#10;    # So we simply reverse and check against 32-bit bounds.&#10;    ans = int(str(abs(x))[::-1])&#10;    if x &lt; 0: ans = -ans&#10;    if ans &gt; 2**31 - 1 or ans &lt; -2**31: return 0&#10;    return ans</code></pre></details></details></td>
    </tr>
    <tr>
      <td>3</td>
      <td>Math 03 Palindrome Number<br><br></b> <a href="https://leetcode.com/problems/palindrome-number/" target="_blank">LeetCode 9</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td><b>Example 1:</b> <br><b>Input:</b> x = 121<br><b>Output:</b> true</td>
      <td><b>Time:</b> O(log10 x)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Negative numbers are false. Reverse half the number. If original equals reversed, it is a palindrome.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isPalindrome(x: int) -&gt; bool:&#10;    if x &lt; 0 or (x % 10 == 0 and x != 0): return False&#10;    rev = 0&#10;    while x &gt; rev:&#10;        rev = rev * 10 + x % 10&#10;        x //= 10&#10;    return x == rev or x == rev // 10</code></pre></details></td>
    </tr>
    <tr>
      <td>4</td>
      <td>Math 04 Gcd Or Hcf<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/lcm-and-gcd4551/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td><b>Example 1:</b> <br><b>Input:</b> A = 4, B = 8<br><b>Output:</b> 4</td>
      <td><details><summary><b>Approach 1</b></summary><b>Time:</b> O(min(a, b))<br><b>Space:</b> O(1)</details><details><summary><b>Approach 2</b></summary><b>Time:</b> O(log(min(a, b)))<br><b>Space:</b> O(1)</details></td>
      <td><details><summary><b>Approach 1</b></summary><b>Explanation:</b> Brute Force: Iterate from 1 to min(a, b) and find the highest number that divides both.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def lcmAndGcd(a: int, b: int) -&gt; list[int]:&#10;    gcd = 1&#10;    for i in range(1, min(a, b) + 1):&#10;        if a % i == 0 and b % i == 0:&#10;            gcd = i&#10;    lcm = (a // gcd) * b  # Divide first to prevent overflow&#10;    return [lcm, gcd]</code></pre></details></details><details><summary><b>Approach 2</b></summary><b>Explanation:</b> Euclidean Algorithm (Optimal): Repeatedly replace max(a,b) with max(a,b) % min(a,b). The final non-zero value is the GCD. Note: LCM can be found in O(1) extra time using formula: LCM(a,b) = (a*b) / GCD(a,b)<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def lcmAndGcd(a: int, b: int) -&gt; list[int]:&#10;    original_a, original_b = a, b&#10;    while a &gt; 0 and b &gt; 0:&#10;        if a &gt; b:&#10;            a = a % b&#10;        else:&#10;            b = b % a&#10;    # m if n == 0 else n can be replaced by a + b since one is 0&#10;    gcd = a + b&#10;    lcm = (original_a // gcd) * original_b  # Divide first to prevent overflow&#10;    return [lcm, gcd]</code></pre></details></details></td>
    </tr>
    <tr>
      <td>5</td>
      <td>Math 05 Check For Prime<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/prime-number2314/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td><b>Example 1:</b> <br><b>Input:</b> N = 5<br><b>Output:</b> 1</td>
      <td><details><summary><b>Approach 1</b></summary><b>Time:</b> O(N)<br><b>Space:</b> O(1)</details><details><summary><b>Approach 2</b></summary><b>Time:</b> O(sqrt(N))<br><b>Space:</b> O(1)</details></td>
      <td><details><summary><b>Approach 1</b></summary><b>Explanation:</b> Brute Force: Iterate from 2 to N-1 and check if N is divisible.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isPrime(N: int) -&gt; int:&#10;    if N &lt;= 1: return 0&#10;    for i in range(2, N):&#10;        if N % i == 0: return 0&#10;    return 1</code></pre></details></details><details><summary><b>Approach 2</b></summary><b>Explanation:</b> Optimal: Check divisibility up to sqrt(N). Factors appear in pairs.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isPrime(N: int) -&gt; int:&#10;    if N &lt;= 1: return 0&#10;    for i in range(2, int(N**0.5) + 1):&#10;        if N % i == 0: return 0&#10;    return 1</code></pre></details></details></td>
    </tr>
    <tr>
      <td>6</td>
      <td>Math 06 Factorial Trailing Zeroes<br><br></b> <a href="https://leetcode.com/problems/factorial-trailing-zeroes/" target="_blank">LeetCode 172</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Counting 5s.</td>
      <td><b>Time:</b> O(log_5(N))<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Trailing zeroes are produced by 10s, which are pairs of 2 and 5. Since 2s are more frequent, we just count the number of 5s in prime factors of numbers up to N. This is `N/5 + N/25 + N/125 + ...`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def trailingZeroes(n: int) -&gt; int:&#10;    count = 0&#10;    while n &gt; 0:&#10;        count += n // 5&#10;        n //= 5&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td>7</td>
      <td>Math 07 Count Primes<br><br></b> <a href="https://leetcode.com/problems/count-primes/" target="_blank">LeetCode 204</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Sieve of Eratosthenes.</td>
      <td><b>Time:</b> O(N log(log N))<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Use the Sieve of Eratosthenes. Initialize a boolean array of size `n` with `true`. Mark `0` and `1` as `false`. For each `i` from `2` to `sqrt(n)`, if `i` is prime, mark its multiples as `false` starting from `i*i`. Finally, count the number of `true`s.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def countPrimes(n: int) -&gt; int:&#10;    if n &lt;= 2: return 0&#10;    isPrime = [True] * n&#10;    isPrime[0] = isPrime[1] = False&#10;    for i in range(2, int(n ** 0.5) + 1):&#10;        if isPrime[i]:&#10;            for j in range(i * i, n, i):&#10;                isPrime[j] = False&#10;    return sum(isPrime)</code></pre></details></td>
    </tr>
    <tr>
      <td>8</td>
      <td>Math 08 Valid Perfect Square<br><br></b> <a href="https://leetcode.com/problems/valid-perfect-square/" target="_blank">LeetCode 367</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Binary Search.</td>
      <td><b>Time:</b> O(log N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Use binary search from `1` to `num/2` or up to `46340` (sqrt of INT_MAX). If `mid * mid == num`, return true. Else if `mid * mid < num`, `low = mid + 1`. Else `high = mid - 1`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isPerfectSquare(num: int) -&gt; bool:&#10;    if num == 1: return True&#10;    low, high = 1, num // 2&#10;    while low &lt;= high:&#10;        mid = (low + high) // 2&#10;        sq = mid * mid&#10;        if sq == num: return True&#10;        elif sq &lt; num: low = mid + 1&#10;        else: high = mid - 1&#10;    return False</code></pre></details></td>
    </tr>
    <tr>
      <td>9</td>
      <td>Math 09 Power Of Three<br><br></b> <a href="https://leetcode.com/problems/power-of-three/" target="_blank">LeetCode 326</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Modulo with largest power.</td>
      <td><b>Time:</b> O(1)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Since `n` is a 32-bit signed integer, the largest power of 3 that fits is `3^19 = 1162261467`. A number `n` is a power of 3 if `n > 0` and `1162261467 % n == 0`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isPowerOfThree(n: int) -&gt; bool:&#10;    return n &gt; 0 and 1162261467 % n == 0</code></pre></details></td>
    </tr>
    <tr>
      <td>10</td>
      <td>Math 10 Power Of Four<br><br></b> <a href="https://leetcode.com/problems/power-of-four/" target="_blank">LeetCode 342</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Bit Manipulation.</td>
      <td><b>Time:</b> O(1)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> A power of 4 is also a power of 2, so `n > 0 && (n & (n-1)) == 0` must hold. Also, the single set bit must be at an even position (0-indexed). The mask `0x55555555` has 1s at all even positions. So `(n & 0x55555555) != 0`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isPowerOfFour(n: int) -&gt; bool:&#10;    return n &gt; 0 and (n &amp; (n - 1)) == 0 and (n &amp; 0x55555555) != 0</code></pre></details></td>
    </tr>
    <tr>
      <td>11</td>
      <td>Math 11 Add Digits<br><br></b> <a href="https://leetcode.com/problems/add-digits/" target="_blank">LeetCode 258</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Digital Root.</td>
      <td><b>Time:</b> O(1)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> This is known as the digital root. The formula is `1 + (n - 1) % 9`. If `n == 0`, return `0`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def addDigits(num: int) -&gt; int:&#10;    if num == 0: return 0&#10;    return 1 + (num - 1) % 9</code></pre></details></td>
    </tr>
    <tr>
      <td>12</td>
      <td>Math 12 Ugly Number<br><br></b> <a href="https://leetcode.com/problems/ugly-number/" target="_blank">LeetCode 263</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Division.</td>
      <td><b>Time:</b> O(log N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> If `n <= 0`, return false. Divide `n` by 2, 3, and 5 as long as it is divisible. If the remaining number is 1, it's an ugly number, else false.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isUgly(n: int) -&gt; bool:&#10;    if n &lt;= 0: return False&#10;    for p in [2, 3, 5]:&#10;        while n % p == 0:&#10;            n //= p&#10;    return n == 1</code></pre></details></td>
    </tr>
    <tr>
      <td>13</td>
      <td>Math 13 Perfect Number<br><br></b> <a href="https://leetcode.com/problems/perfect-number/" target="_blank">LeetCode 507</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Sum of divisors.</td>
      <td><b>Time:</b> O(sqrt(N))<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> If `num <= 1`, return false. Iterate up to `sqrt(num)`. If `i` divides `num`, add `i` and `num/i` to the sum. After the loop, compare sum with `num`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def checkPerfectNumber(num: int) -&gt; bool:&#10;    if num &lt;= 1: return False&#10;    total = 1&#10;    for i in range(2, int(num ** 0.5) + 1):&#10;        if num % i == 0:&#10;            total += i&#10;            if i * i != num: total += num // i&#10;    return total == num</code></pre></details></td>
    </tr>
    <tr>
      <td>14</td>
      <td>Math 14 Excel Sheet Column Title<br><br></b> <a href="https://leetcode.com/problems/excel-sheet-column-title/" target="_blank">LeetCode 168</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Base 26 conversion.</td>
      <td><b>Time:</b> O(log_26(N))<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> This is essentially base 26 conversion, but 1-indexed (A=1, B=2, Z=26). To make it 0-indexed, decrement `columnNumber` by 1 at each step, get the remainder modulo 26, convert to character, and divide by 26.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def convertToTitle(columnNumber: int) -&gt; str:&#10;    res = []&#10;    while columnNumber &gt; 0:&#10;        columnNumber -= 1&#10;        res.append(chr(ord(&#x27;A&#x27;) + (columnNumber % 26)))&#10;        columnNumber //= 26&#10;    return &quot;&quot;.join(res[::-1])</code></pre></details></td>
    </tr>
    <tr>
      <td>15</td>
      <td>Math 15 Sieve Of Eratosthenes<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/sieve-of-eratosthenes5242/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td><b>Example 1:</b> Classic implementation.</td>
      <td><b>Time:</b> O(N log(log N))<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Same as `countPrimes`, but return the actual prime numbers in a list instead of just the count.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def sieveOfEratosthenes(N):&#10;    is_prime = [True] * (N + 1)&#10;    is_prime[0] = is_prime[1] = False&#10;    for i in range(2, int(N**0.5) + 1):&#10;        if is_prime[i]:&#10;            for j in range(i*i, N + 1, i):&#10;                is_prime[j] = False&#10;    return [i for i in range(2, N + 1) if is_prime[i]]</code></pre></details></td>
    </tr>
    <tr>
      <td>16</td>
      <td>Hash 16 Count Frequencies<br><br></b> <a href="https://www.geeksforgeeks.org/problems/frequency-of-array-elements-1587115620/1" target="_blank">GeeksforGeeks</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td><b></b> <br><b>Input:</b> arr = [10, 5, 10, 15, 10, 5]<br><b>Output:</b> 10->3, 5->2, 15->1<br><br><b></b> 1 &le; N &le; 10<sup>5</sup></td>
      <td><details><summary><b>Approach 1</b></summary><b>Time:</b> O(N^2)<br><b>Space:</b> O(N)</details><details><summary><b>Approach 2</b></summary><b>Time:</b> O(N<sup>2</sup>) (Trade-off)<br><b>Space:</b> O(N) (Trade-off)</details></td>
      <td><details><summary><b>Approach 1</b></summary><b>Explanation:</b> Brute Force: Use two nested loops to count frequency of each element, marking visited ones.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def countFreq(arr):&#10;    n = len(arr)&#10;    visited = [False] * n&#10;    for i in range(n):&#10;        if visited[i]: continue&#10;        count = 1&#10;        for j in range(i+1, n):&#10;            if arr[i] == arr[j]:&#10;                visited[j] = True&#10;                count += 1&#10;        print(arr[i], count)</code></pre></details></details><details><summary><b>Approach 2</b></summary><b>Explanation:</b> Optimal: Use two nested loops to count occurrences. Mark visited elements to avoid recounting.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def count_freq(arr: list[int]) -&gt; None:\n    freq = {}\n    for num in arr:\n        freq[num] = freq.get(num, 0) + 1\n    for key, val in freq.items():\n        print(f&#x27;{key} {val}&#x27;)</code></pre></details></details></td>
    </tr>
    <tr>
      <td>17</td>
      <td>Hash 17 Highest Lowest Frequency<br><br></b> <a href="https://leetcode.com/problems/sort-array-by-increasing-frequency/" target="_blank">LeetCode 1636</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td><b></b> <br><b>Input:</b> arr = [10, 5, 10, 15, 10, 5]<br><b>Output:</b> Highest=10, Lowest=15<br><br><b></b> 1 &le; N &le; 10<sup>5</sup></td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(N) (Trade-off)</td>
      <td><b>Explanation:</b> Optimal: Build a frequency map, then iterate through the map to find the max and min frequencies.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def find_high_low_freq(arr: list[int]) -&gt; tuple:&#10;    freq = {}&#10;    for num in arr:&#10;        freq[num] = freq.get(num, 0) + 1&#10;    &#10;    max_f, min_f = 0, float(&#x27;inf&#x27;)&#10;    max_ele, min_ele = 0, 0&#10;    &#10;    for ele, count in freq.items():&#10;        if count &gt; max_f:&#10;            max_f, max_ele = count, ele&#10;        if count &lt; min_f:&#10;            min_f, min_ele = count, ele&#10;    return max_ele, min_ele</code></pre></details></td>
    </tr>
    <tr>
      <td>18</td>
      <td>Hash 18 Intersection Of Two Arrays<br><br></b> <a href="https://leetcode.com/problems/intersection-of-two-arrays/" target="_blank">LeetCode 349</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td><b></b> <br><b>Input:</b> nums1 = [1,2,2,1], nums2 = [2,2]<br><b>Output:</b> [2]<br><br><b></b> 1 &le; N, M &le; 1000</td>
      <td><details><summary><b>Approach 1</b></summary><b>Time:</b> O(N * M)<br><b>Space:</b> O(min(N, M))</details><details><summary><b>Approach 2</b></summary><b>Time:</b> O(N + M) (Constraint)<br><b>Space:</b> O(N) (Trade-off)</details></td>
      <td><details><summary><b>Approach 1</b></summary><b>Explanation:</b> Brute Force: Iterate through the first array and check each element in the second array.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def intersection(nums1, nums2):&#10;    res = []&#10;    for x in nums1:&#10;        if x in nums2 and x not in res:&#10;            res.append(x)&#10;    return res</code></pre></details></details><details><summary><b>Approach 2</b></summary><b>Explanation:</b> Optimal: Store elements of the first array in a Hash Set, then iterate over the second array to find matches.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def intersection(nums1: list[int], nums2: list[int]) -&gt; list[int]:&#10;    set1 = set(nums1)&#10;    res = []&#10;    for num in nums2:&#10;        if num in set1:&#10;            res.append(num)&#10;            set1.remove(num) # Ensure uniqueness&#10;    return res</code></pre></details></details></td>
    </tr>
    <tr>
      <td>19</td>
      <td>Hash 19 Union Of Two Arrays<br><br></b> <a href="https://www.geeksforgeeks.org/problems/union-of-two-arrays3538/1" target="_blank">GeeksforGeeks</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td><b></b> <br><b>Input:</b> a = [1, 2, 3], b = [2, 3, 4]<br><b>Output:</b> [1, 2, 3, 4]<br><br><b></b> Arrays may not be sorted.</td>
      <td><b>Time:</b> O(N + M) (Constraint)<br><b>Space:</b> O(N + M) (Trade-off)</td>
      <td><b>Explanation:</b> Optimal: Insert all elements from both arrays into a Hash Set. The Set natively drops duplicates.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def find_union(a: list[int], b: list[int]) -&gt; list[int]:&#10;    # Set union operator implicitly merges and drops duplicates&#10;    s = set(a) | set(b)&#10;    return list(s)</code></pre></details></td>
    </tr>
    <tr>
      <td>20</td>
      <td>Hash 20 Subarray With 0 Sum<br><br></b> <a href="https://www.geeksforgeeks.org/problems/subarray-with-0-sum-1587115621/1" target="_blank">GeeksforGeeks</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td><b></b> <br><b>Input:</b> arr = [4, 2, -3, 1, 6]<br><b>Output:</b> true (2, -3, 1)<br><br><b></b> Array contains positive and negative integers.</td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(N) (Trade-off)</td>
      <td><b>Explanation:</b> Optimal: Use a Prefix Sum and a Hash Set. If a prefix sum repeats, or equals 0, a 0-sum subarray exists between the identical prefix sums.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def has_zero_sum_subarray(arr: list[int]) -&gt; bool:&#10;    prefix_sums = set()&#10;    curr_sum = 0&#10;    for num in arr:&#10;        curr_sum += num&#10;        if curr_sum == 0 or curr_sum in prefix_sums:&#10;            return True&#10;        prefix_sums.add(curr_sum)&#10;    return False</code></pre></details></td>
    </tr>
    <tr>
      <td>21</td>
      <td>Hash 21 Subarray Sum Equals K<br><br></b> <a href="https://leetcode.com/problems/subarray-sum-equals-k/" target="_blank">LeetCode 560</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td><b></b> <br><b>Input:</b> nums = [1,1,1], k = 2<br><b>Output:</b> 2<br><br><b></b> Negative numbers allowed, preventing pure Sliding Window approaches.</td>
      <td><details><summary><b>Approach 1</b></summary><b>Time:</b> O(N^2)<br><b>Space:</b> O(1)</details><details><summary><b>Approach 2</b></summary><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(N) (Trade-off)</details></td>
      <td><details><summary><b>Approach 1</b></summary><b>Explanation:</b> Brute Force: Generate all possible subarrays and compute their sums.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def subarraySum(nums, k):&#10;    count = 0&#10;    for i in range(len(nums)):&#10;        current_sum = 0&#10;        for j in range(i, len(nums)):&#10;            current_sum += nums[j]&#10;            if current_sum == k:&#10;                count += 1&#10;    return count</code></pre></details></details><details><summary><b>Approach 2</b></summary><b>Explanation:</b> Optimal: Maintain a Hash Map of `prefix_sum` -> `frequency`. If `curr_sum - k` exists in the map, add its frequency to the count.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def subarray_sum(nums: list[int], k: int) -&gt; int:&#10;    prefix_freq = {0: 1}&#10;    count = 0&#10;    curr_sum = 0&#10;    for num in nums:&#10;        curr_sum += num&#10;        remove = curr_sum - k&#10;        if remove in prefix_freq:&#10;            count += prefix_freq[remove]&#10;        prefix_freq[curr_sum] = prefix_freq.get(curr_sum, 0) + 1&#10;    return count</code></pre></details></details></td>
    </tr>
    <tr>
      <td>22</td>
      <td>Hash 22 Longest Subarray With 0 Sum<br><br></b> <a href="https://www.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1" target="_blank">GeeksforGeeks</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td><b></b> <br><b>Input:</b> arr = [15,-2,2,-8,1,7,10,23]<br><b>Output:</b> 5<br><br><b></b> 1 &le; N &le; 10<sup>5</sup></td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(N) (Trade-off)</td>
      <td><b>Explanation:</b> Optimal: Store `prefix_sum` -> `index` in Hash Map. If sum repeats, calculate distance `i - hash[sum]`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def max_len(arr: list[int]) -&gt; int:&#10;    prefix_index = {}&#10;    max_len = sum = 0&#10;    for i, num in enumerate(arr):&#10;        sum += num&#10;        if sum == 0:&#10;            max_len = i + 1&#10;        elif sum in prefix_index:&#10;            max_len = max(max_len, i - prefix_index[sum])&#10;        else:&#10;            prefix_index[sum] = i&#10;    return max_len</code></pre></details></td>
    </tr>
    <tr>
      <td>23</td>
      <td>Hash 23 Longest Subarray With Sum K<br><br></b> <a href="https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1" target="_blank">GeeksforGeeks</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td><b></b> <br><b>Input:</b> arr = [10, 5, 2, 7, 1, 9], k = 15<br><b>Output:</b> 4<br><br><b></b> 1 &le; N &le; 10<sup>5</sup></td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(N) (Trade-off)</td>
      <td><b>Explanation:</b> Optimal: Prefix Sum Map storing indices. Check if `sum - K` exists in map and calculate index difference.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def len_of_long_subarr(arr: list[int], k: int) -&gt; int:&#10;    prefix_index = {}&#10;    max_len = sum = 0&#10;    for i, num in enumerate(arr):&#10;        sum += num&#10;        if sum == k:&#10;            max_len = i + 1&#10;        needed = sum - k&#10;        if needed in prefix_index:&#10;            max_len = max(max_len, i - prefix_index[needed])&#10;        if sum not in prefix_index:&#10;            prefix_index[sum] = i&#10;    return max_len</code></pre></details></td>
    </tr>
    <tr>
      <td>24</td>
      <td>Hash 24 Two Sum<br><br></b> <a href="https://leetcode.com/problems/two-sum/" target="_blank">LeetCode 1</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td><b></b> <br><b>Input:</b> nums = [2,7,11,15], target = 9<br><b>Output:</b> [0,1]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Optimal: Iterate while storing numbers and their indices in a hash map. Check if `target - num` already exists.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def twoSum(nums: list[int], target: int) -&gt; list[int]:&#10;    mpp = {}&#10;    for i, num in enumerate(nums):&#10;        needed = target - num&#10;        if needed in mpp:&#10;            return [mpp[needed], i]&#10;        mpp[num] = i&#10;    return []</code></pre></details></td>
    </tr>
    <tr>
      <td>25</td>
      <td>Hash 25 Group Anagrams<br><br></b> <a href="https://leetcode.com/problems/group-anagrams/" target="_blank">LeetCode 49</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td><b></b> <br><b>Input:</b> strs = ["eat","tea","tan","ate","nat","bat"]<br><b>Output:</b> [["bat"],["nat","tan"],["ate","eat","tea"]]</td>
      <td><b>Time:</b> O(N * K log K)<br><b>Space:</b> O(N * K)</td>
      <td><b>Explanation:</b> Optimal: Use a hash map where the key is the sorted version of the string, and the value is a list of anagrams.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">from collections import defaultdict&#10;def groupAnagrams(strs: list[str]) -&gt; list[list[str]]:&#10;    mpp = defaultdict(list)&#10;    for s in strs:&#10;        mpp[tuple(sorted(s))].append(s)&#10;    return list(mpp.values())</code></pre></details></td>
    </tr>
    <tr>
      <td>26</td>
      <td>Hash 26 Longest Consecutive Sequence<br><br></b> <a href="https://leetcode.com/problems/longest-consecutive-sequence/" target="_blank">LeetCode 128</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td><b></b> <br><b>Input:</b> nums = [100,4,200,1,3,2]<br><b>Output:</b> 4 (The sequence is [1, 2, 3, 4])</td>
      <td><details><summary><b>Approach 1</b></summary><b>Time:</b> O(N log N)<br><b>Space:</b> O(1)</details><details><summary><b>Approach 2</b></summary><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(N)</details></td>
      <td><details><summary><b>Approach 1</b></summary><b>Explanation:</b> Brute Force: Sort the array first, then count consecutive elements linearly.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def longestConsecutive(nums):&#10;    if not nums: return 0&#10;    nums.sort()&#10;    longest, current = 1, 1&#10;    for i in range(1, len(nums)):&#10;        if nums[i] == nums[i-1]: continue&#10;        if nums[i] == nums[i-1] + 1:&#10;            current += 1&#10;        else:&#10;            longest = max(longest, current)&#10;            current = 1&#10;    return max(longest, current)</code></pre></details></details><details><summary><b>Approach 2</b></summary><b>Explanation:</b> Optimal: Insert all elements into a Hash Set. Iterate through elements. If `num - 1` is NOT in the set, it's the start of a sequence. Count forwards.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def longestConsecutive(nums: list[int]) -&gt; int:&#10;    num_set = set(nums)&#10;    max_len = 0&#10;    for num in num_set:&#10;        if num - 1 not in num_set:&#10;            curr_num = num&#10;            curr_len = 1&#10;            while curr_num + 1 in num_set:&#10;                curr_num += 1&#10;                curr_len += 1&#10;            max_len = max(max_len, curr_len)&#10;    return max_len</code></pre></details></details></td>
    </tr>
    <tr>
      <td>27</td>
      <td>Hash 27 Longest Subarray With 0 Sum<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, SDE Sheet</details></td>
      <td><b></b> Hash Map.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Optimal: Maintain the prefix sum and a hash map storing the first occurrence index of each prefix sum. If sum is 0, length is `i+1`. If sum is in the map, length is `i - map[sum]`. Update max length.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxLen(n, arr):&#10;    m = {}&#10;    maxi, sum_val = 0, 0&#10;    for i in range(n):&#10;        sum_val += arr[i]&#10;        if sum_val == 0: maxi = i + 1&#10;        else:&#10;            if sum_val in m:&#10;                maxi = max(maxi, i - m[sum_val])&#10;            else:&#10;                m[sum_val] = i&#10;    return maxi</code></pre></details></td>
    </tr>
    <tr>
      <td>28</td>
      <td>Hash 28 Count Distinct Elements In Every Window<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/count-distinct-elements-in-every-window/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b></b> Sliding Window + Hash Map.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(K)</td>
      <td><b>Explanation:</b> Optimal: Use a hash map to keep track of element frequencies in the window of size K. The number of distinct elements is the size of the hash map. As window slides, increment frequency of new element, decrement frequency of outgoing element. If frequency becomes 0, remove it from map.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def countDistinct(arr, n, k):&#10;    m = {}&#10;    ans = []&#10;    for i in range(k):&#10;        m[arr[i]] = m.get(arr[i], 0) + 1&#10;    ans.append(len(m))&#10;    for i in range(k, n):&#10;        m[arr[i - k]] -= 1&#10;        if m[arr[i - k]] == 0: del m[arr[i - k]]&#10;        m[arr[i]] = m.get(arr[i], 0) + 1&#10;        ans.append(len(m))&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>29</td>
      <td>Sw 29 Longest Substring Without Repeating Characters<br><br></b> <a href="https://leetcode.com/problems/longest-substring-without-repeating-characters/" target="_blank">LeetCode 3</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, SDE Sheet, Love Babbar</details></td>
      <td><b>Example 1:</b> <br><b>Input:</b> s = "abcabcbb"<br><b>Output:</b> 3 ("abc")</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(min(N, M))</td>
      <td><b>Explanation:</b> Sliding window with a Hash Map storing the latest index of each character. Move `left` pointer to `max(left, map[char] + 1)`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def lengthOfLongestSubstring(s: str) -&gt; int:&#10;    mpp = {}&#10;    left = max_len = 0&#10;    for right, char in enumerate(s):&#10;        if char in mpp:&#10;            left = max(left, mpp[char] + 1)&#10;        mpp[char] = right&#10;        max_len = max(max_len, right - left + 1)&#10;    return max_len</code></pre></details></td>
    </tr>
    <tr>
      <td>30</td>
      <td>Sw 30 Trapping Rain Water<br><br></b> <a href="https://leetcode.com/problems/trapping-rain-water/" target="_blank">LeetCode 42</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td><b>Example 1:</b> <br><b>Input:</b> height = [0,1,0,2,1,0,1,3,2,1,2,1]<br><b>Output:</b> 6</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Two pointers `left` and `right`. Maintain `left_max` and `right_max`. Move the pointer pointing to the smaller max, adding trapped water.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def trap(height: list[int]) -&gt; int:&#10;    left, right = 0, len(height) - 1&#10;    res, maxLeft, maxRight = 0, 0, 0&#10;    while left &lt;= right:&#10;        if height[left] &lt;= height[right]:&#10;            if height[left] &gt;= maxLeft: maxLeft = height[left]&#10;            else: res += maxLeft - height[left]&#10;            left += 1&#10;        else:&#10;            if height[right] &gt;= maxRight: maxRight = height[right]&#10;            else: res += maxRight - height[right]&#10;            right -= 1&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td>31</td>
      <td>Sw 31 Count Occurrences Of Anagrams<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/count-occurences-of-anagrams5839/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Fixed window and frequency map.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(26) = O(1)</td>
      <td><b>Explanation:</b> Maintain a frequency map of the pattern. Use a sliding window of size equal to the length of the pattern. Keep track of the number of characters fully matched (`count`). If `count` equals the number of unique characters in the pattern, an anagram is found.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def search(pat: str, txt: str) -&gt; int:&#10;    k, n = len(pat), len(txt)&#10;    if k &gt; n: return 0&#10;    count = collections.Counter(pat)&#10;    distinct = len(count)&#10;    i = j = ans = 0&#10;    while j &lt; n:&#10;        if txt[j] in count:&#10;            count[txt[j]] -= 1&#10;            if count[txt[j]] == 0:&#10;                distinct -= 1&#10;        if j - i + 1 &lt; k:&#10;            j += 1&#10;        elif j - i + 1 == k:&#10;            if distinct == 0:&#10;                ans += 1&#10;            if txt[i] in count:&#10;                count[txt[i]] += 1&#10;                if count[txt[i]] == 1:&#10;                    distinct += 1&#10;            i += 1&#10;            j += 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>32</td>
      <td>Sw 32 Maximum Of All Subarrays Of Size K<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/maximum-of-all-subarrays-of-size-k3101/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Deque.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(K)</td>
      <td><b>Explanation:</b> Use a deque to store indices of elements. The deque will maintain elements in decreasing order. For each element, remove elements from the back of the deque that are smaller than the current element. Also, remove elements from the front that are out of the current window. The front of the deque will always have the maximum element of the current window.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def max_of_subarrays(arr: List[int], n: int, k: int) -&gt; List[int]:&#10;    res = []&#10;    dq = collections.deque()&#10;    for i in range(n):&#10;        if dq and dq[0] == i - k:&#10;            dq.popleft()&#10;        while dq and arr[dq[-1]] &lt;= arr[i]:&#10;            dq.pop()&#10;        dq.append(i)&#10;        if i &gt;= k - 1:&#10;            res.append(arr[dq[0]])&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td>33</td>
      <td>Sw 33 Minimum Window Substring<br><br></b> <a href="https://leetcode.com/problems/minimum-window-substring/" target="_blank">LeetCode 76</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td><b>Example 1:</b> Variable sliding window.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Maintain a frequency map of `t`. Expand the window by moving `right`. When the window contains all characters of `t`, try to shrink it by moving `left` to find the minimum window. Keep track of the minimum window length and its starting index.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def minWindow(s: str, t: str) -&gt; str:&#10;    if len(s) &lt; len(t): return &quot;&quot;&#10;    count = collections.Counter(t)&#10;    required = len(t)&#10;    l = r = 0&#10;    minLen = float(&#x27;inf&#x27;)&#10;    minStart = 0&#10;    while r &lt; len(s):&#10;        if count[s[r]] &gt; 0:&#10;            required -= 1&#10;        count[s[r]] -= 1&#10;        r += 1&#10;        while required == 0:&#10;            if r - l &lt; minLen:&#10;                minLen = r - l&#10;                minStart = l&#10;            count[s[l]] += 1&#10;            if count[s[l]] &gt; 0:&#10;                required += 1&#10;            l += 1&#10;    return &quot;&quot; if minLen == float(&#x27;inf&#x27;) else s[minStart:minStart+minLen]</code></pre></details></td>
    </tr>
    <tr>
      <td>34</td>
      <td>Sw 34 Longest K Unique Characters Substring<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td><b>Example 1:</b> Variable window and hash map.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(K)</td>
      <td><b>Explanation:</b> Maintain a hash map of character frequencies. Expand the window by moving `j`. If the number of unique characters exceeds `k`, shrink the window from the left (`i`) until the number of unique characters is `k`. Update the maximum length when exactly `k` unique characters are present.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def longestKSubstr(s: str, k: int) -&gt; int:&#10;    count = collections.defaultdict(int)&#10;    i = j = 0&#10;    maxLen = -1&#10;    while j &lt; len(s):&#10;        count[s[j]] += 1&#10;        if len(count) == k:&#10;            maxLen = max(maxLen, j - i + 1)&#10;        elif len(count) &gt; k:&#10;            while len(count) &gt; k:&#10;                count[s[i]] -= 1&#10;                if count[s[i]] == 0:&#10;                    del count[s[i]]&#10;                i += 1&#10;        j += 1&#10;    return maxLen</code></pre></details></td>
    </tr>
    <tr>
      <td>35</td>
      <td>Sw 35 Subarrays With K Different Integers<br><br></b> <a href="https://leetcode.com/problems/subarrays-with-k-different-integers/" target="_blank">LeetCode 992</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td><b>Example 1:</b> Exact K = atMost(K) - atMost(K-1).</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td><b>Explanation:</b> Finding exact `k` distinct is hard directly. Instead, find subarrays with at most `k` distinct integers. The number of exact `k` is `atMost(k) - atMost(k - 1)`. The `atMost` function uses a sliding window.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def subarraysWithKDistinct(nums: List[int], k: int) -&gt; int:&#10;    def atMost(k):&#10;        count = collections.defaultdict(int)&#10;        res = i = 0&#10;        for j in range(len(nums)):&#10;            if count[nums[j]] == 0: k -= 1&#10;            count[nums[j]] += 1&#10;            while k &lt; 0:&#10;                count[nums[i]] -= 1&#10;                if count[nums[i]] == 0: k += 1&#10;                i += 1&#10;            res += j - i + 1&#10;        return res&#10;    return atMost(k) - atMost(k - 1)</code></pre></details></td>
    </tr>
    <tr>
      <td>36</td>
      <td>Sw 36 Minimum Size Subarray Sum<br><br></b> <a href="https://leetcode.com/problems/minimum-size-subarray-sum/" target="_blank">LeetCode 209</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Variable sliding window.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Use a sliding window. Add elements to the current sum. While the sum is >= target, update the minimum length and shrink the window from the left.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minSubArrayLen(target: int, nums: List[int]) -&gt; int:&#10;    l = sum = 0&#10;    minLen = float(&#x27;inf&#x27;)&#10;    for r in range(len(nums)):&#10;        sum += nums[r]&#10;        while sum &gt;= target:&#10;            minLen = min(minLen, r - l + 1)&#10;            sum -= nums[l]&#10;            l += 1&#10;    return 0 if minLen == float(&#x27;inf&#x27;) else minLen</code></pre></details></td>
    </tr>
    <tr>
      <td>37</td>
      <td>Sw 37 Fruits Into Baskets<br><br></b> <a href="https://leetcode.com/problems/fruit-into-baskets/" target="_blank">LeetCode 904</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td><b>Example 1:</b> Longest subarray with at most 2 distinct elements.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1) (at most 3 elements in map)</td>
      <td><b>Explanation:</b> This translates to finding the longest subarray with at most 2 distinct elements. Maintain a frequency map and use a sliding window. If distinct elements > 2, shrink the window until distinct elements <= 2.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def totalFruit(fruits: List[int]) -&gt; int:&#10;    count = collections.defaultdict(int)&#10;    l = maxFruits = 0&#10;    for r in range(len(fruits)):&#10;        count[fruits[r]] += 1&#10;        while len(count) &gt; 2:&#10;            count[fruits[l]] -= 1&#10;            if count[fruits[l]] == 0:&#10;                del count[fruits[l]]&#10;            l += 1&#10;        maxFruits = max(maxFruits, r - l + 1)&#10;    return maxFruits</code></pre></details></td>
    </tr>
    <tr>
      <td>38</td>
      <td>Sw 38 Max Consecutive Ones III<br><br></b> <a href="https://leetcode.com/problems/max-consecutive-ones-iii/" target="_blank">LeetCode 1004</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td><b>Example 1:</b> Sliding Window.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Use a sliding window. Expand the right pointer. If the element is 0, increment a zero counter. While the zero counter > k, shrink the window from the left by moving the left pointer and decrementing the zero counter if left element is 0. The max window size is the answer.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def longestOnes(nums, k):&#10;    left = 0&#10;    zeroes = 0&#10;    max_len = 0&#10;    for right in range(len(nums)):&#10;        if nums[right] == 0: zeroes += 1&#10;        while zeroes &gt; k:&#10;            if nums[left] == 0: zeroes -= 1&#10;            left += 1&#10;        max_len = max(max_len, right - left + 1)&#10;    return max_len</code></pre></details></td>
    </tr>
    <tr>
      <td>39</td>
      <td>Sw 39 Longest Repeating Character Replacement<br><br></b> <a href="https://leetcode.com/problems/longest-repeating-character-replacement/" target="_blank">LeetCode 424</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td><b>Example 1:</b> Sliding Window + Max Freq.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Use a sliding window. Maintain the character frequencies and the `max_freq` in the window. The number of replacements needed is `window_size - max_freq`. If this is > k, shrink the window from left and decrement the corresponding frequency.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def characterReplacement(s, k):&#10;    count = [0] * 26&#10;    left = 0&#10;    max_freq = 0&#10;    max_len = 0&#10;    for right in range(len(s)):&#10;        count[ord(s[right]) - ord(&#x27;A&#x27;)] += 1&#10;        max_freq = max(max_freq, count[ord(s[right]) - ord(&#x27;A&#x27;)])&#10;        if (right - left + 1) - max_freq &gt; k:&#10;            count[ord(s[left]) - ord(&#x27;A&#x27;)] -= 1&#10;            left += 1&#10;        max_len = max(max_len, right - left + 1)&#10;    return max_len</code></pre></details></td>
    </tr>
    <tr>
      <td>40</td>
      <td>Sw 40 Binary Subarrays With Sum<br><br></b> <a href="https://leetcode.com/problems/binary-subarrays-with-sum/" target="_blank">LeetCode 930</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td><b>Example 1:</b> atMost(goal) - atMost(goal - 1).</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Use the helper function `atMost(goal)` which finds the number of subarrays with sum <= goal. The answer is `atMost(goal) - atMost(goal - 1)`. In `atMost`, use a sliding window to maintain the sum.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def numSubarraysWithSum(nums, goal):&#10;    def atMost(k):&#10;        if k &lt; 0: return 0&#10;        left, sum_val, count = 0, 0, 0&#10;        for right in range(len(nums)):&#10;            sum_val += nums[right]&#10;            while sum_val &gt; k:&#10;                sum_val -= nums[left]&#10;                left += 1&#10;            count += (right - left + 1)&#10;        return count&#10;    return atMost(goal) - atMost(goal - 1)</code></pre></details></td>
    </tr>
    <tr>
      <td>41</td>
      <td>Sw 41 Count Number Of Nice Subarrays<br><br></b> <a href="https://leetcode.com/problems/count-number-of-nice-subarrays/" target="_blank">LeetCode 1248</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td><b>Example 1:</b> atMost(k) - atMost(k - 1).</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Replace all odd numbers with 1 and even numbers with 0. The problem then reduces to finding the number of subarrays with a sum equal to k. Use the `atMost(k) - atMost(k - 1)` sliding window approach.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def numberOfSubarrays(nums, k):&#10;    def atMost(limit):&#10;        if limit &lt; 0: return 0&#10;        left, count, res = 0, 0, 0&#10;        for right in range(len(nums)):&#10;            if nums[right] % 2 != 0: count += 1&#10;            while count &gt; limit:&#10;                if nums[left] % 2 != 0: count -= 1&#10;                left += 1&#10;            res += (right - left + 1)&#10;        return res&#10;    return atMost(k) - atMost(k - 1)</code></pre></details></td>
    </tr>
    <tr>
      <td>42</td>
      <td>Sw 42 Number Of Substrings Containing All Three Characters<br><br></b> <a href="https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/" target="_blank">LeetCode 1358</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td><b>Example 1:</b> Store last seen indices.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Iterate through the string. Track the last seen indices of 'a', 'b', and 'c'. If all three have been seen, the number of valid substrings ending at the current index `i` is `1 + min(last_a, last_b, last_c)`. Add this to the total count.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def numberOfSubstrings(s):&#10;    last = [-1, -1, -1]&#10;    count = 0&#10;    for i in range(len(s)):&#10;        last[ord(s[i]) - ord(&#x27;a&#x27;)] = i&#10;        if last[0] != -1 and last[1] != -1 and last[2] != -1:&#10;            count += 1 + min(last)&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td>43</td>
      <td>Sw 43 Maximum Points You Can Obtain From Cards<br><br></b> <a href="https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/" target="_blank">LeetCode 1423</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td><b>Example 1:</b> Sliding Window on remaining cards.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Instead of picking cards from the ends, find the subarray of length `N - K` that has the minimum sum. Subtract this minimum sum from the total sum of the array. That gives the maximum score.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def maxScore(cardPoints, k):&#10;    n = len(cardPoints)&#10;    total_sum = sum(cardPoints)&#10;    window_size = n - k&#10;    window_sum = sum(cardPoints[:window_size])&#10;    min_window_sum = window_sum&#10;    for i in range(window_size, n):&#10;        window_sum += cardPoints[i] - cardPoints[i - window_size]&#10;        min_window_sum = min(min_window_sum, window_sum)&#10;    return total_sum - min_window_sum</code></pre></details></td>
    </tr>
    <tr>
      <td>44</td>
      <td>Sw 44 Find All Anagrams In A String<br><br></b> <a href="https://leetcode.com/problems/find-all-anagrams-in-a-string/" target="_blank">LeetCode 438</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar, Striver A Z</details></td>
      <td><b>Example 1:</b> Fixed Window + Hash Map.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Create frequency arrays for `p` and a window of size `p.length()` in `s`. Slide the window across `s`, updating the window frequencies. If the arrays match, add the window's start index to the result.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findAnagrams(s, p):&#10;    ans = []&#10;    if len(p) &gt; len(s): return ans&#10;    countP, countS = [0]*26, [0]*26&#10;    for i in range(len(p)):&#10;        countP[ord(p[i]) - ord(&#x27;a&#x27;)] += 1&#10;        countS[ord(s[i]) - ord(&#x27;a&#x27;)] += 1&#10;    if countP == countS: ans.append(0)&#10;    for i in range(len(p), len(s)):&#10;        countS[ord(s[i]) - ord(&#x27;a&#x27;)] += 1&#10;        countS[ord(s[i - len(p)]) - ord(&#x27;a&#x27;)] -= 1&#10;        if countP == countS: ans.append(i - len(p) + 1)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>45</td>
      <td>Sw 45 Permutation In String<br><br></b> <a href="https://leetcode.com/problems/permutation-in-string/" target="_blank">LeetCode 567</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Sliding Window + Frequency Array.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Use a sliding window of size `len(s1)` over `s2`. Maintain frequency arrays for `s1` and the current window in `s2`. Compare arrays at each step.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def checkInclusion(s1, s2):&#10;    if len(s1) &gt; len(s2): return False&#10;    c1, c2 = [0]*26, [0]*26&#10;    for i in range(len(s1)):&#10;        c1[ord(s1[i]) - 97] += 1&#10;        c2[ord(s2[i]) - 97] += 1&#10;    if c1 == c2: return True&#10;    for i in range(len(s1), len(s2)):&#10;        c2[ord(s2[i]) - 97] += 1&#10;        c2[ord(s2[i - len(s1)]) - 97] -= 1&#10;        if c1 == c2: return True&#10;    return False</code></pre></details></td>
    </tr>
    <tr>
      <td>46</td>
      <td>Sw 46 First Negative Integer In Every Window Of Size K<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Queue.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(K)</td>
      <td><b>Explanation:</b> Maintain a queue of negative integers in the current window. While moving the window, add new negative integers, remove old ones out of window. The front of queue is the first negative.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">from collections import deque&#10;def printFirstNegativeInteger(A, N, K):&#10;    ans = []&#10;    q = deque()&#10;    for i in range(K - 1):&#10;        if A[i] &lt; 0: q.append(A[i])&#10;    for i in range(K - 1, N):&#10;        if A[i] &lt; 0: q.append(A[i])&#10;        ans.append(q[0] if q else 0)&#10;        if A[i - K + 1] &lt; 0 and q and q[0] == A[i - K + 1]: q.popleft()&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>47</td>
      <td>Sw 47 Count Occurrences Of Anagrams<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/count-occurences-of-anagrams1536/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Sliding Window + Frequency Map.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Use a sliding window of size `pat.length()`. Keep frequency map of `pat`. Track `count` of distinct characters to match. While moving window, decrease `count` if char frequency matches. If `count == 0`, increment answer.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def search(pat, txt):&#10;    m = {}&#10;    for c in pat: m[c] = m.get(c, 0) + 1&#10;    count, ans, k = len(m), 0, len(pat)&#10;    i = 0&#10;    for j in range(len(txt)):&#10;        if txt[j] in m:&#10;            m[txt[j]] -= 1&#10;            if m[txt[j]] == 0: count -= 1&#10;        if j - i + 1 == k:&#10;            if count == 0: ans += 1&#10;            if txt[i] in m:&#10;                m[txt[i]] += 1&#10;                if m[txt[i]] == 1: count += 1&#10;            i += 1&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>48</td>
      <td>Sw 48 Smallest Window In A String Containing All The Characters Of Another String<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/smallest-window-in-a-string-containing-all-the-characters-of-another-string-1587115621/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Love Babbar</details></td>
      <td><b>Example 1:</b> Sliding Window.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td><b>Explanation:</b> Same as Minimum Window Substring. Use frequency map of `P` and a sliding window over `S`. Shrink window from left when all characters match to find the minimum length.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def smallestWindow(s, p):&#10;    if len(p) &gt; len(s): return &quot;-1&quot;&#10;    m = {}&#10;    for c in p: m[c] = m.get(c, 0) + 1&#10;    count, minLen, start, i = len(m), float(&#x27;inf&#x27;), 0, 0&#10;    for j in range(len(s)):&#10;        if s[j] in m:&#10;            m[s[j]] -= 1&#10;            if m[s[j]] == 0: count -= 1&#10;        while count == 0:&#10;            if j - i + 1 &lt; minLen:&#10;                minLen = j - i + 1&#10;                start = i&#10;            if s[i] in m:&#10;                m[s[i]] += 1&#10;                if m[s[i]] &gt; 0: count += 1&#10;            i += 1&#10;    return &quot;-1&quot; if minLen == float(&#x27;inf&#x27;) else s[start:start+minLen]</code></pre></details></td>
    </tr>
  </tbody>
</table>
