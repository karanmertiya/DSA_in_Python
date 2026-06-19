# Basic Maths Revision Table

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
      <td>Math 01 Count Digits<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/count-digits5716/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Input: N = 12345, Output: 5</td>
      <td><b>Time:</b> O(log10 N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>N=0:</b> Handled naturally if checking N > 0, otherwise special condition.</td>
      <td><b>Explanation:</b> Convert to string and return length, or repeatedly divide by 10. O(log10 N) time.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def evenlyDivides(N: int) -&gt; int:&#10;    if N == 0: return 1&#10;    count, temp = 0, N&#10;    while temp &gt; 0:&#10;        digit = temp % 10&#10;        if digit != 0 and N % digit == 0: count += 1&#10;        temp //= 10&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td>2</td>
      <td>Math 02 Reverse Integer<br><br></b> <a href='https://leetcode.com/problems/reverse-integer/' target='_blank'>LeetCode 7</a></td>
      <td><b>Example 1:</b> Input: x = 123, Output: 321</td>
      <td><b>Time:</b> O(log10 x)<br><b>Space:</b> O(1)</td>
      <td><code>#include <limits.h></code></td>
      <td><b>Overflow:</b> If ans > INT_MAX/10, return 0.</td>
      <td><b>Explanation:</b> Extract last digit using modulo, multiply answer by 10 and add. Check bounds for 32-bit integer.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def reverse(x: int) -&gt; int:&#10;    sign = [1, -1][x &lt; 0]&#10;    ans = int(str(abs(x))[::-1])&#10;    return sign * ans if ans &lt;= 2**31 - 1 else 0</code></pre></details></td>
    </tr>
    <tr>
      <td>3</td>
      <td>Math 03 Palindrome Number<br><br></b> <a href='https://leetcode.com/problems/palindrome-number/' target='_blank'>LeetCode 9</a></td>
      <td><b>Example 1:</b> Input: x = 121, Output: true</td>
      <td><b>Time:</b> O(log10 x)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>Negative Numbers:</b> Instant false. Trailing zeroes instant false.</td>
      <td><b>Explanation:</b> Negative numbers are false. Reverse half the number. If original equals reversed, it is a palindrome.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isPalindrome(x: int) -&gt; bool:&#10;    if x &lt; 0 or (x % 10 == 0 and x != 0): return False&#10;    rev = 0&#10;    while x &gt; rev:&#10;        rev = rev * 10 + x % 10&#10;        x //= 10&#10;    return x == rev or x == rev // 10</code></pre></details></td>
    </tr>
    <tr>
      <td>4</td>
      <td>Math 04 Gcd Or Hcf<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/lcm-and-gcd4551/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Input: A = 4, B = 8, Output: 4</td>
      <td><b>Time:</b> O(log(min(a,b)))<br><b>Space:</b> O(1)</td>
      <td><code>#include <numeric></code></td>
      <td><b>One is 0:</b> Return the other number.</td>
      <td><b>Explanation:</b> Euclidean Algorithm. gcd(a, b) = gcd(b, a % b). Stop when one is 0.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def gcd(a: int, b: int) -&gt; int:&#10;    while a &gt; 0 and b &gt; 0:&#10;        if a &gt; b: a = a % b&#10;        else: b = b % a&#10;    return b if a == 0 else a</code></pre></details></td>
    </tr>
    <tr>
      <td>5</td>
      <td>Math 05 Check For Prime<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/prime-number2314/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Input: N = 5, Output: 1</td>
      <td><b>Time:</b> O(sqrt(N))<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>N=1:</b> Not prime.</td>
      <td><b>Explanation:</b> Check divisibility up to sqrt(N).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isPrime(N: int) -&gt; int:&#10;    if N &lt;= 1: return 0&#10;    for i in range(2, int(N**0.5) + 1):&#10;        if N % i == 0: return 0&#10;    return 1</code></pre></details></td>
    </tr>
    <tr>
      <td>6</td>
      <td>Math 16 Count Primes<br><br></b> <a href='https://leetcode.com/problems/count-primes/' target='_blank'>LeetCode 204</a></td>
      <td><b>Example 1:</b> Sieve of Eratosthenes.</td>
      <td><b>Time:</b> O(N log(log N))<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>n <= 2</td>
      <td><b>Explanation:</b> Use the Sieve of Eratosthenes. Create a boolean array of size `n` initialized to true. Set indices 0 and 1 to false. Iterate from `p=2` to `sqrt(n)`. If `p` is prime, mark all its multiples starting from `p*p` as false. Count the remaining true values.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def countPrimes(n):&#10;    if n &lt;= 2: return 0&#10;    is_prime = [True] * n&#10;    is_prime[0] = is_prime[1] = False&#10;    for i in range(2, int(n**0.5) + 1):&#10;        if is_prime[i]:&#10;            for j in range(i*i, n, i):&#10;                is_prime[j] = False&#10;    return sum(is_prime)</code></pre></details></td>
    </tr>
    <tr>
      <td>7</td>
      <td>Math 17 Pow X N<br><br></b> <a href='https://leetcode.com/problems/powx-n/' target='_blank'>LeetCode 50</a></td>
      <td><b>Example 1:</b> Binary Exponentiation.</td>
      <td><b>Time:</b> O(log N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>Negative power, n = INT_MIN</td>
      <td><b>Explanation:</b> Use binary exponentiation. Initialize `ans = 1.0`. Keep a copy of `n` as a long long `nn`. If `nn < 0`, make it positive. While `nn > 0`, if `nn % 2 == 1`, multiply `ans` by `x` and decrement `nn`. Otherwise, square `x` and halve `nn`. If original `n < 0`, return `1.0 / ans`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def myPow(x, n):&#10;    ans, nn = 1.0, abs(n)&#10;    while nn &gt; 0:&#10;        if nn % 2 == 1:&#10;            ans *= x&#10;            nn -= 1&#10;        else:&#10;            x *= x&#10;            nn //= 2&#10;    return ans if n &gt;= 0 else 1.0 / ans</code></pre></details></td>
    </tr>
    <tr>
      <td>8</td>
      <td>Math 18 Sieve Of Eratosthenes<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/sieve-of-eratosthenes5242/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Classic implementation.</td>
      <td><b>Time:</b> O(N log(log N))<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Same as `countPrimes`, but return the actual prime numbers in a list instead of just the count.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def sieveOfEratosthenes(N):&#10;    is_prime = [True] * (N + 1)&#10;    is_prime[0] = is_prime[1] = False&#10;    for i in range(2, int(N**0.5) + 1):&#10;        if is_prime[i]:&#10;            for j in range(i*i, N + 1, i):&#10;                is_prime[j] = False&#10;    return [i for i in range(2, N + 1) if is_prime[i]]</code></pre></details></td>
    </tr>
    <tr>
      <td>9</td>
      <td>Math 19 Prime Factors<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/prime-factors5052/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Iterative division.</td>
      <td><b>Time:</b> O(sqrt(N))<br><b>Space:</b> O(1) excluding output</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Iterate from `i = 2` to `sqrt(N)`. If `N % i == 0`, `i` is a prime factor. Add `i` to result, and repeatedly divide `N` by `i` until it's no longer divisible. After the loop, if `N > 1`, then `N` itself is a prime factor and should be added.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def AllPrimeFactors(N):&#10;    ans = []&#10;    for i in range(2, int(N**0.5) + 1):&#10;        if N % i == 0:&#10;            ans.append(i)&#10;            while N % i == 0: N //= i&#10;    if N &gt; 1: ans.append(N)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>10</td>
      <td>Math 20 Print All Divisors<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/print-all-divisors-of-a-number/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Iterate up to sqrt(N).</td>
      <td><b>Time:</b> O(sqrt(N) + k log k)<br><b>Space:</b> O(k)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Iterate `i` from 1 to `sqrt(N)`. If `N % i == 0`, add `i` to the list of divisors. If `N / i != i`, also add `N / i`. Sort the list before returning.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_divisors(n):&#10;    ans = []&#10;    for i in range(1, int(n**0.5) + 1):&#10;        if n % i == 0:&#10;            ans.append(i)&#10;            if n // i != i: ans.append(n // i)&#10;    ans.sort()&#10;    print(*(ans))</code></pre></details></td>
    </tr>
    <tr>
      <td>11</td>
      <td>Math 22 Reverse Integer<br><br></b> <a href='https://leetcode.com/problems/reverse-integer/' target='_blank'>LeetCode 7</a></td>
      <td><b>Example 1:</b> Math with overflow check.</td>
      <td><b>Time:</b> O(log10(X))<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>Overflow checks</td>
      <td><b>Explanation:</b> Use a while loop to extract the last digit using `x % 10` and add it to the reversed number `ans = ans * 10 + digit`. Check for overflow before multiplying by 10.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def reverse(x):&#10;    sign = [1, -1][x &lt; 0]&#10;    ans = int(str(abs(x))[::-1]) * sign&#10;    if not -2**31 &lt;= ans &lt;= 2**31 - 1: return 0&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>12</td>
      <td>Math 23 Palindrome Number<br><br></b> <a href='https://leetcode.com/problems/palindrome-number/' target='_blank'>LeetCode 9</a></td>
      <td><b>Example 1:</b> Reverse half the number.</td>
      <td><b>Time:</b> O(log10(X))<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>x < 0, x % 10 == 0</td>
      <td><b>Explanation:</b> Negative numbers are not palindromes. Numbers ending in 0 (except 0 itself) are not palindromes. Reverse the second half of the number. If `x == reversed` or `x == reversed / 10` (for odd length), it's a palindrome.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isPalindrome(x):&#10;    if x &lt; 0 or (x != 0 and x % 10 == 0): return False&#10;    rev = 0&#10;    while x &gt; rev:&#10;        rev = rev * 10 + x % 10&#10;        x //= 10&#10;    return x == rev or x == rev // 10</code></pre></details></td>
    </tr>
    <tr>
      <td>13</td>
      <td>Math 24 Armstrong Number<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/armstrong-numbers2727/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Math.</td>
      <td><b>Time:</b> O(log10(N))<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Extract each digit, cube it, and sum them up. If the sum equals the original number, it's an Armstrong number.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def armstrongNumber(n):&#10;    return &quot;Yes&quot; if sum(int(d)**3 for d in str(n)) == n else &quot;No&quot;</code></pre></details></td>
    </tr>
    <tr>
      <td>14</td>
      <td>Math 25 Gcd Or Hcf<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/gcd-of-two-numbers3459/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Euclidean Algorithm.</td>
      <td><b>Time:</b> O(log(min(A, B)))<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Use Euclidean algorithm. `gcd(A, B) = gcd(B, A % B)`. Repeat until `B` becomes 0, then `A` is the GCD.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def gcd(A, B):&#10;    while A &gt; 0 and B &gt; 0:&#10;        if A &gt; B: A %= B&#10;        else: B %= A&#10;    return B if A == 0 else A</code></pre></details></td>
    </tr>
  </tbody>
</table>
