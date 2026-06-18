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
      <td rowspan="3">1</td>
      <td rowspan="3">Math 01 Count Digits</td>
      <td rowspan="3"><b>Example 1:</b> Input: N = 12345, Output: 5<br><b>Example 2:</b> Input: N = -8394, Output: 4<br><br><b>Note (Constraint):</b> -10<sup>9</sup> &le; N &le; 10<sup>9</sup></td>
      <td><b>Time:</b> O(log10(N))<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>Sign Handle:</b><br><code>if (n == 0) return 1;</code><br><code>n = abs(n);</code></td>
      <td><b>Explanation:</b> Divide by 10 continuously until N becomes 0.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def count_digits_brute(n: int) -&gt; int:&#10;    # Edge Case: 0 has 1 digit, negative numbers require abs()&#10;    if n == 0: return 1&#10;    n = abs(n)&#10;    cnt = 0&#10;    while n &gt; 0:&#10;        cnt += 1&#10;        n //= 10&#10;    return cnt</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(1) (Constraint)<br><b>Space:</b> O(log10(N)) (Trade-off)</td>
      <td><b>Type Casting:</b><br><code>to_string()</code> / <code>str()</code></td>
      <td><b>Sign Handle:</b><br><code>n = abs(n);</code></td>
      <td><b>Explanation:</b> Convert number to string and return length.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def count_digits_better(n: int) -&gt; int:&#10;    if n == 0: return 1&#10;    # Trade-off: Allocates string memory&#10;    return len(str(abs(n)))</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(1) (Constraint)<br><b>Space:</b> O(1)</td>
      <td><b>Math Lib:</b><br><code>log10()</code></td>
      <td><b>Sign Handle:</b><br><code>n = abs(n);</code></td>
      <td><b>Explanation:</b> Use base-10 logarithm to find digit count mathematically.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import math&#10;&#10;def count_digits_optimal(n: int) -&gt; int:&#10;    if n == 0: return 1&#10;    n = abs(n)&#10;    return int(math.log10(n) + 1)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">2</td>
      <td rowspan="2">Math 02 Reverse A Number</td>
      <td rowspan="2"><b>Example 1:</b> Input: N = 1234, Output: 4321<br><b>Example 2:</b> Input: N = -10400, Output: -401<br><br><b>Note (Constraint):</b> -2<sup>31</sup> &le; N &le; 2<sup>31</sup> - 1</td>
      <td><b>Time:</b> O(log10(N))<br><b>Space:</b> O(log10(N)) (Trade-off)</td>
      <td><b>String Lib:</b><br><code>reverse()</code>, <code>stoi()</code></td>
      <td><b>Negative Signs:</b> Reversing a '-' results in invalid parsing. Store sign, process <code>abs(n)</code>.</td>
      <td><b>Explanation:</b> Convert to string, reverse the string, and parse back to integer.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def reverse_number_brute(n: int) -&gt; int:&#10;    # Edge Case: Explicitly store and remove sign before string conversion&#10;    is_neg = n &lt; 0&#10;    s = str(abs(n))&#10;    res = int(s[::-1])&#10;    if res &gt; 2**31 - 1: return 0&#10;    return -res if is_neg else res</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(log10(N))<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>Data-type Agnostic Overflow Check:</b><br><code>temp / 10 != revNum</code></td>
      <td><b>Explanation:</b> Extract digits using modulo 10 and build the reversed number mathematically.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def reverse_number_optimal(n: int) -&gt; int:&#10;    rev_num = 0&#10;    sign = -1 if n &lt; 0 else 1&#10;    n = abs(n)&#10;    while n &gt; 0:&#10;        ld = n % 10&#10;        rev_num = (rev_num * 10) + ld&#10;        n //= 10&#10;    if rev_num &gt; 2**31 - 1: return 0&#10;    return sign * rev_num</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">3</td>
      <td rowspan="2">Math 03 Check Palindrome</td>
      <td rowspan="2"><b>Example 1:</b> Input: N = 121, Output: true<br><b>Example 2:</b> Input: N = -121, Output: false<br><br><b>Note (Constraint):</b> -2<sup>31</sup> &le; N &le; 2<sup>31</sup> - 1</td>
      <td><b>Time:</b> O(log10(N))<br><b>Space:</b> O(log10(N)) (Trade-off)</td>
      <td><b>String Lib:</b><br><code>to_string()</code>, <code>reverse()</code></td>
      <td><b>Negative Numbers:</b> Naturally handled by string equality (`-121` != `121-`)</td>
      <td><b>Explanation:</b> Convert the number to a string and compare it with its reversed version.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def is_palindrome_brute(n: int) -&gt; bool:&#10;    s = str(n)&#10;    return s == s[::-1]</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(log10(N))<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>State Preservation:</b> Loop destroys `n`, requires `dup` variable.<br><b>Negative Signs:</b><br><code>if(n < 0) return false;</code></td>
      <td><b>Explanation:</b> Reverse the number mathematically and compare it to the original.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def is_palindrome_optimal(n: int) -&gt; bool:&#10;    # Edge Case: Negative numbers are strictly not palindromes&#10;    if n &lt; 0: return False&#10;    &#10;    dup = n&#10;    rev_num = 0&#10;    while n &gt; 0:&#10;        ld = n % 10&#10;        rev_num = (rev_num * 10) + ld&#10;        n //= 10&#10;    return dup == rev_num</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">4</td>
      <td rowspan="1">Math 05 Armstrong Numbers</td>
      <td rowspan="1"><b>Example 1:</b> Input: N = 153, Output: true<br><b>Example 2:</b> Input: N = 1634, Output: true<br><br><b>Note (Constraint):</b> 1 &le; N &le; 10<sup>9</sup></td>
      <td><b>Time:</b> O(log10(N))<br><b>Space:</b> O(1)</td>
      <td><b>Math Lib:</b><br><code>log10()</code>, <code>pow()</code>, <code>round()</code></td>
      <td><b>Two-Pass Logic:</b> Requires digit count upfront (e.g. 1634 requires ^4).</td>
      <td><b>Explanation:</b> Extract digit count first, then mathematically sum digits raised to that count.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import math&#10;&#10;def is_armstrong(n: int) -&gt; bool:&#10;    dup = n&#10;    sum_val = 0&#10;    digits = int(math.log10(n) + 1) if n &gt; 0 else 1&#10;    while n &gt; 0:&#10;        ld = n % 10&#10;        sum_val += ld ** digits&#10;        n //= 10&#10;    return sum_val == dup</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">5</td>
      <td rowspan="2">Math 07 Check For Prime</td>
      <td rowspan="2"><b>Example 1:</b> Input: N = 11, Output: true<br><br><b>Note (Constraint):</b> 1 &le; N &le; 10<sup>9</sup></td>
      <td><b>Time:</b> O(N) (Trade-off)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>TLE Guarantee:</b> N=10^9 takes ~10<sup>9</sup> ops. Fails tight bounds.</td>
      <td><b>Explanation:</b> Iterate from 2 to N-1 and check divisibility.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def check_prime_brute(n: int) -&gt; bool:&#10;    if n &lt;= 1:&#10;        return False&#10;    for i in range(2, n):&#10;        if n % i == 0:&#10;            return False&#10;    return True</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(&radic;N) (Constraint)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>Math Optimization:</b> <code>i * i <= n</code> prevents floating point <code>sqrt(n)</code> overhead.<br><br><b>Skipping Evens:</b> <code>if(n%2==0) return false;</code> halves the loop size.</td>
      <td><b>Explanation:</b> Iterate from 2 up to sqrt(N) checking divisor pairs.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def check_prime_optimal(n: int) -&gt; bool:&#10;    if n &lt;= 1: return False&#10;    if n == 2: return True&#10;    # Edge Case Optimization: Halve range by skipping evens&#10;    if n % 2 == 0: return False&#10;    &#10;    limit = int(n**0.5)&#10;    for i in range(3, limit + 1, 2):&#10;        if n % i == 0:&#10;            return False&#10;    return True</code></pre></details></td>
    </tr>
  </tbody>
</table>
