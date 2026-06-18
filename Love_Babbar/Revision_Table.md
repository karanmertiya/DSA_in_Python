# Love Babbar - Master Revision Table

## Patterns

<table border="1">
  <thead>
    <tr>
      <th>S.No</th>
      <th>Problem Name</th>
      <th>Example</th>
      <th>Common Constraints</th>
      <th>Approach Type</th>
      <th>Time</th>
      <th>Space</th>
      <th>Specific Conditions / Edge Cases</th>
      <th>Logic</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Pattern 01 Rectangular Star</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-text">Example 1:&#10;Input: N = 3&#10;Output:&#10;***&#10;***&#10;***&#10;&#10;Example 2:&#10;Input: N = 5&#10;Output:&#10;*****&#10;*****&#10;*****&#10;*****&#10;*****</code></pre></td>
      <td>1 &le; N &le; 20</td>
      <td><b>Optimal</b></td>
      <td><code>O(N<sup>2</sup>)</code><br><i>Constraint</i></td>
      <td><code>O(1)</code><br><i>Constraint</i></td>
      <td>Grid print naturally restricts space to O(1). Time bounds hardcoded to area N&times;N.</td>
      <td>
        <pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(n):&#10;        print(&quot;*&quot; * n)</code></pre>
      </td>
    </tr>
    <tr>
      <td>2</td>
      <td>Pattern 02 Right Angled Triangle</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-text">Example 1:&#10;Input: N = 3&#10;Output:&#10;*&#10;**&#10;***&#10;&#10;Example 2:&#10;Input: N = 5&#10;Output:&#10;*&#10;**&#10;***&#10;****&#10;*****</code></pre></td>
      <td>1 &le; N &le; 20</td>
      <td><b>Optimal</b></td>
      <td><code>O(N<sup>2</sup>)</code><br><i>Constraint</i></td>
      <td><code>O(1)</code><br><i>Constraint</i></td>
      <td>Grid print naturally restricts space to O(1). Time bounds hardcoded to area N&times;N.</td>
      <td>
        <pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(1, n + 1):&#10;        print(&quot;* &quot; * i)</code></pre>
      </td>
    </tr>
    <tr>
      <td>3</td>
      <td>Pattern 03 Right Angled Number Pyramid</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-text">Example 1:&#10;Input: N = 3&#10;Output:&#10;1&#10;1 2&#10;1 2 3&#10;&#10;Example 2:&#10;Input: N = 5&#10;Output:&#10;1&#10;1 2&#10;1 2 3&#10;1 2 3 4&#10;1 2 3 4 5</code></pre></td>
      <td>1 &le; N &le; 20</td>
      <td><b>Optimal</b></td>
      <td><code>O(N<sup>2</sup>)</code><br><i>Constraint</i></td>
      <td><code>O(1)</code><br><i>Constraint</i></td>
      <td>Grid print naturally restricts space to O(1). Time bounds hardcoded to area N&times;N.</td>
      <td>
        <pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(1, n + 1):&#10;        for j in range(1, i + 1):&#10;            print(j, end=&quot; &quot;)&#10;        print()</code></pre>
      </td>
    </tr>
    <tr>
      <td>4</td>
      <td>Pattern 04 Right Angled Number Pyramid Ii</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-text">Example 1:&#10;Input: N = 3&#10;Output:&#10;1&#10;2 2&#10;3 3 3&#10;&#10;Example 2:&#10;Input: N = 5&#10;Output:&#10;1&#10;2 2&#10;3 3 3&#10;4 4 4 4&#10;5 5 5 5 5</code></pre></td>
      <td>1 &le; N &le; 20</td>
      <td><b>Optimal</b></td>
      <td><code>O(N<sup>2</sup>)</code><br><i>Constraint</i></td>
      <td><code>O(1)</code><br><i>Constraint</i></td>
      <td>Grid print naturally restricts space to O(1). Time bounds hardcoded to area N&times;N.</td>
      <td>
        <pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(1, n + 1):&#10;        for j in range(1, i + 1):&#10;            print(i, end=&quot; &quot;)&#10;        print()</code></pre>
      </td>
    </tr>
    <tr>
      <td>5</td>
      <td>Pattern 05 Inverted Right Pyramid</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-text">Example 1:&#10;Input: N = 3&#10;Output:&#10;* * *&#10;* *&#10;*&#10;&#10;Example 2:&#10;Input: N = 5&#10;Output:&#10;* * * * *&#10;* * * *&#10;* * *&#10;* *&#10;*</code></pre></td>
      <td>1 &le; N &le; 20</td>
      <td><b>Optimal</b></td>
      <td><code>O(N<sup>2</sup>)</code><br><i>Constraint</i></td>
      <td><code>O(1)</code><br><i>Constraint</i></td>
      <td>Grid print naturally restricts space to O(1). Time bounds hardcoded to area N&times;N.</td>
      <td>
        <pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(n, 0, -1):&#10;        print(&quot;* &quot; * i)</code></pre>
      </td>
    </tr>
    <tr>
      <td>6</td>
      <td>Pattern 06 Inverted Numbered Right Pyramid</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-text">Example 1:&#10;Input: N = 3&#10;Output:&#10;1 2 3&#10;1 2&#10;1&#10;&#10;Example 2:&#10;Input: N = 5&#10;Output:&#10;1 2 3 4 5&#10;1 2 3 4&#10;1 2 3&#10;1 2&#10;1</code></pre></td>
      <td>1 &le; N &le; 20</td>
      <td><b>Optimal</b></td>
      <td><code>O(N<sup>2</sup>)</code><br><i>Constraint</i></td>
      <td><code>O(1)</code><br><i>Constraint</i></td>
      <td>Grid print naturally restricts space to O(1). Time bounds hardcoded to area N&times;N.</td>
      <td>
        <pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(n, 0, -1):&#10;        for j in range(1, i + 1):&#10;            print(j, end=&quot; &quot;)&#10;        print()</code></pre>
      </td>
    </tr>
    <tr>
      <td>7</td>
      <td>Pattern 07 Star Pyramid</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-text">Example 1:&#10;Input: N = 3&#10;Output:&#10;  *&#10; ***&#10;*****&#10;&#10;Example 2:&#10;Input: N = 5&#10;Output:&#10;    *&#10;   ***&#10;  *****&#10; *******&#10;*********</code></pre></td>
      <td>1 &le; N &le; 20</td>
      <td><b>Optimal</b></td>
      <td><code>O(N<sup>2</sup>)</code><br><i>Constraint</i></td>
      <td><code>O(1)</code><br><i>Constraint</i></td>
      <td>Grid print naturally restricts space to O(1). Time bounds hardcoded to area N&times;N.</td>
      <td>
        <pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(n):&#10;        spaces = &quot; &quot; * (n - i - 1)&#10;        stars = &quot;*&quot; * (2 * i + 1)&#10;        print(spaces + stars + spaces)</code></pre>
      </td>
    </tr>
    <tr>
      <td>8</td>
      <td>Pattern 08 Inverted Star Pyramid</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-text">Example 1:&#10;Input: N = 3&#10;Output:&#10;*****&#10; ***&#10;  *&#10;&#10;Example 2:&#10;Input: N = 5&#10;Output:&#10;*********&#10; *******&#10;  *****&#10;   ***&#10;    *</code></pre></td>
      <td>1 &le; N &le; 20</td>
      <td><b>Optimal</b></td>
      <td><code>O(N<sup>2</sup>)</code><br><i>Constraint</i></td>
      <td><code>O(1)</code><br><i>Constraint</i></td>
      <td>Grid print naturally restricts space to O(1). Time bounds hardcoded to area N&times;N.</td>
      <td>
        <pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(n):&#10;        spaces = &quot; &quot; * i&#10;        stars = &quot;*&quot; * (2 * (n - i) - 1)&#10;        print(spaces + stars + spaces)</code></pre>
      </td>
    </tr>
    <tr>
      <td>9</td>
      <td>Pattern 09 Diamond Star Pattern</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-text">Example 1:&#10;Input: N = 3&#10;Output:&#10;  *&#10; ***&#10;*****&#10;*****&#10; ***&#10;  *&#10;</code></pre></td>
      <td>1 &le; N &le; 20</td>
      <td><b>Optimal</b></td>
      <td><code>O(N<sup>2</sup>)</code><br><i>Constraint</i></td>
      <td><code>O(1)</code><br><i>Constraint</i></td>
      <td>Grid print naturally restricts space to O(1). Time bounds hardcoded to area N&times;N.</td>
      <td>
        <pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(n):&#10;        spaces = &quot; &quot; * (n - i - 1)&#10;        stars = &quot;*&quot; * (2 * i + 1)&#10;        print(spaces + stars + spaces)&#10;    for i in range(n):&#10;        spaces = &quot; &quot; * i&#10;        stars = &quot;*&quot; * (2 * (n - i) - 1)&#10;        print(spaces + stars + spaces)</code></pre>
      </td>
    </tr>
    <tr>
      <td>10</td>
      <td>Pattern 10 Half Diamond Star Pattern</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-text">Example 1:&#10;Input: N = 3&#10;Output:&#10;*&#10;**&#10;***&#10;**&#10;*&#10;</code></pre></td>
      <td>1 &le; N &le; 20</td>
      <td><b>Optimal</b></td>
      <td><code>O(N<sup>2</sup>)</code><br><i>Constraint</i></td>
      <td><code>O(1)</code><br><i>Constraint</i></td>
      <td>Grid print naturally restricts space to O(1). Time bounds hardcoded to area N&times;N.</td>
      <td>
        <pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(1, 2 * n):&#10;        stars = i if i &lt;= n else 2 * n - i&#10;        print(&quot;*&quot; * stars)</code></pre>
      </td>
    </tr>
    <tr>
      <td>11</td>
      <td>Pattern 11 Binary Number Triangle</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-text">Example 1:&#10;Input: N = 3&#10;Output:&#10;1&#10;0 1&#10;1 0 1&#10;</code></pre></td>
      <td>1 &le; N &le; 20</td>
      <td><b>Optimal</b></td>
      <td><code>O(N<sup>2</sup>)</code><br><i>Constraint</i></td>
      <td><code>O(1)</code><br><i>Constraint</i></td>
      <td>Grid print naturally restricts space to O(1). Time bounds hardcoded to area N&times;N.</td>
      <td>
        <pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(n):&#10;        start = 1 if i % 2 == 0 else 0&#10;        for j in range(i + 1):&#10;            print(start, end=&quot; &quot;)&#10;            start = 1 - start&#10;        print()</code></pre>
      </td>
    </tr>
    <tr>
      <td>12</td>
      <td>Pattern 12 Number Crown Pattern</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-text">Example 1:&#10;Input: N = 3&#10;Output:&#10;1    1&#10;12  21&#10;123321</code></pre></td>
      <td>1 &le; N &le; 20</td>
      <td><b>Optimal</b></td>
      <td><code>O(N<sup>2</sup>)</code><br><i>Constraint</i></td>
      <td><code>O(1)</code><br><i>Constraint</i></td>
      <td>Grid print naturally restricts space to O(1). Time bounds hardcoded to area N&times;N.</td>
      <td>
        <pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    space = 2 * (n - 1)&#10;    for i in range(1, n + 1):&#10;        for j in range(1, i + 1):&#10;            print(j, end=&quot;&quot;)&#10;        print(&quot; &quot; * space, end=&quot;&quot;)&#10;        for j in range(i, 0, -1):&#10;            print(j, end=&quot;&quot;)&#10;        print()&#10;        space -= 2</code></pre>
      </td>
    </tr>
    <tr>
      <td>13</td>
      <td>Pattern 13 Increasing Number Triangle</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-text">Example 1:&#10;Input: N = 3&#10;Output:&#10;1&#10;2 3&#10;4 5 6</code></pre></td>
      <td>1 &le; N &le; 20</td>
      <td><b>Optimal</b></td>
      <td><code>O(N<sup>2</sup>)</code><br><i>Constraint</i></td>
      <td><code>O(1)</code><br><i>Constraint</i></td>
      <td>Grid print naturally restricts space to O(1). Time bounds hardcoded to area N&times;N.</td>
      <td>
        <pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    num = 1&#10;    for i in range(1, n + 1):&#10;        for j in range(1, i + 1):&#10;            print(num, end=&quot; &quot;)&#10;            num += 1&#10;        print()</code></pre>
      </td>
    </tr>
    <tr>
      <td>14</td>
      <td>Pattern 19 Symmetric Void Pattern</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-text">Example 1:&#10;Input: N = 3&#10;Output:&#10;******&#10;**  **&#10;*    *&#10;*    *&#10;**  **&#10;******</code></pre></td>
      <td>1 &le; N &le; 20</td>
      <td><b>Optimal</b></td>
      <td><code>O(N<sup>2</sup>)</code><br><i>Constraint</i></td>
      <td><code>O(1)</code><br><i>Constraint</i></td>
      <td>Grid print naturally restricts space to O(1). Time bounds hardcoded to area N&times;N.</td>
      <td>
        <pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    iniSpace = 0&#10;    for i in range(n):&#10;        print(&quot;*&quot; * (n - i) + &quot; &quot; * iniSpace + &quot;*&quot; * (n - i))&#10;        iniSpace += 2&#10;    iniSpace = 2 * n - 2&#10;    for i in range(1, n + 1):&#10;        print(&quot;*&quot; * i + &quot; &quot; * iniSpace + &quot;*&quot; * i)&#10;        iniSpace -= 2</code></pre>
      </td>
    </tr>
    <tr>
      <td>15</td>
      <td>Pattern 20 Symmetric Butterfly Pattern</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-text">Example 1:&#10;Input: N = 3&#10;Output:&#10;*    *&#10;**  **&#10;******&#10;**  **&#10;*    *</code></pre></td>
      <td>1 &le; N &le; 20</td>
      <td><b>Optimal</b></td>
      <td><code>O(N<sup>2</sup>)</code><br><i>Constraint</i></td>
      <td><code>O(1)</code><br><i>Constraint</i></td>
      <td>Grid print naturally restricts space to O(1). Time bounds hardcoded to area N&times;N.</td>
      <td>
        <pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    spaces = 2 * n - 2&#10;    for i in range(1, 2 * n):&#10;        stars = i if i &lt;= n else 2 * n - i&#10;        print(&quot;*&quot; * stars + &quot; &quot; * spaces + &quot;*&quot; * stars)&#10;        if i &lt; n:&#10;            spaces -= 2&#10;        else:&#10;            spaces += 2</code></pre>
      </td>
    </tr>
    <tr>
      <td>16</td>
      <td>Pattern 21 Hollow Rectangle Pattern</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-text">Example 1:&#10;Input: N = 3&#10;Output:&#10;***&#10;* *&#10;***</code></pre></td>
      <td>1 &le; N &le; 20</td>
      <td><b>Optimal</b></td>
      <td><code>O(N<sup>2</sup>)</code><br><i>Constraint</i></td>
      <td><code>O(1)</code><br><i>Constraint</i></td>
      <td>Grid print naturally restricts space to O(1). Time bounds hardcoded to area N&times;N.</td>
      <td>
        <pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(n):&#10;        for j in range(n):&#10;            if i == 0 or j == 0 or i == n - 1 or j == n - 1:&#10;                print(&quot;*&quot;, end=&quot;&quot;)&#10;            else:&#10;                print(&quot; &quot;, end=&quot;&quot;)&#10;        print()</code></pre>
      </td>
    </tr>
  </tbody>
</table>

<br>

## Basic Maths

<table border="1">
  <thead>
    <tr>
      <th>S.No</th>
      <th>Problem Name</th>
      <th>Example</th>
      <th>Common Constraints</th>
      <th>Approach Type</th>
      <th>Time</th>
      <th>Space</th>
      <th>Specific Conditions / Edge Cases</th>
      <th>Logic</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">1</td>
      <td rowspan="3">Math 01 Count Digits</td>
      <td rowspan="3"><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-text">Example 1:&#10;Input: N = 12345&#10;Output: 5&#10;&#10;Example 2:&#10;Input: N = 8394&#10;Output: 4</code></pre></td>
      <td rowspan="3">1 &le; N &le; 10<sup>9</sup></td>
      <td><b>Brute Force</b></td>
      <td><code>O(log10(N))</code><br><i>Constraint</i></td>
      <td><code>O(1)</code><br><i>Constraint</i></td>
      <td><b>Sign Edge Case:</b> Fails on N=0. Requires explicit check.</td>
      <td><details><summary>View Code</summary><br><i>Note: Divide by 10 continuously until N becomes 0.</i><br><br><b>Edge Case Code:</b><br><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">if n &lt;= 0: return 1</code></pre><br><b>Implementation:</b><br><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def count_digits_brute(n: int) -&gt; int:&#10;    # Edge Case: Handle N=0 specifically&#10;    if n &lt;= 0: return 1&#10;    cnt = 0&#10;    while n &gt; 0:&#10;        cnt += 1&#10;        n //= 10&#10;    return cnt</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Better</b></td>
      <td><code>O(1)</code><br><i>Constraint</i></td>
      <td><code>O(log10(N))</code><br><i>Trade-off</i></td>
      <td><b>Memory Trade-off:</b> String allocation required. Avoid for strictly O(1) space constraints.</td>
      <td><details><summary>View Code</summary><br><i>Note: Convert number to string and return length.</i><br><br><b>Implementation:</b><br><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def count_digits_better(n: int) -&gt; int:&#10;    # Trade-off: Allocates string memory proportional to digit count&#10;    return len(str(n))</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Optimal</b></td>
      <td><code>O(1)</code><br><i>Constraint</i></td>
      <td><code>O(1)</code><br><i>Constraint</i></td>
      <td><b>Library Requirement:</b> Must use math library. Fails if standard libraries are restricted.</td>
      <td><details><summary>View Code</summary><br><i>Note: Use base-10 logarithm to find digit count mathematically.</i><br><br><b>Implementation:</b><br><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import math&#10;&#10;def count_digits_optimal(n: int) -&gt; int:&#10;    # Edge Case check for zero&#10;    if n &lt;= 0: return 1&#10;    return int(math.log10(n) + 1)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">2</td>
      <td rowspan="2">Math 02 Reverse A Number</td>
      <td rowspan="2"><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-text">Example 1:&#10;Input: N = 1234&#10;Output: 4321&#10;&#10;Example 2:&#10;Input: N = 10400&#10;Output: 401</code></pre></td>
      <td rowspan="2">-2<sup>31</sup> &le; N &le; 2<sup>31</sup> - 1</td>
      <td><b>Brute Force</b></td>
      <td><code>O(log10(N))</code><br><i>Trade-off</i></td>
      <td><code>O(log10(N))</code><br><i>Trade-off</i></td>
      <td><b>Negative Signs:</b> Reversing a string with '-' results in invalid parsing.</td>
      <td><details><summary>View Code</summary><br><i>Note: Convert to string, reverse the string, and parse back to integer.</i><br><br><b>Implementation:</b><br><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def reverse_number_brute(n: int) -&gt; int:&#10;    # Edge Case: Explicitly store and remove sign before string conversion&#10;    is_neg = n &lt; 0&#10;    s = str(abs(n))&#10;    res = int(s[::-1])&#10;    return -res if is_neg else res</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Optimal</b></td>
      <td><code>O(log10(N))</code><br><i>Constraint</i></td>
      <td><code>O(1)</code><br><i>Constraint</i></td>
      <td><b>Overflow Risk:</b> Number fits in 32-bit int, but its reverse might not. Forces explicit checks.</td>
      <td><details><summary>View Code</summary><br><i>Note: Extract digits using modulo 10 and build the reversed number mathematically.</i><br><br><b>Edge Case Code:</b><br><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python"></code></pre><br><b>Implementation:</b><br><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def reverse_number_optimal(n: int) -&gt; int:&#10;    rev_num = 0&#10;    sign = -1 if n &lt; 0 else 1&#10;    n = abs(n)&#10;    while n &gt; 0:&#10;        ld = n % 10&#10;        rev_num = (rev_num * 10) + ld&#10;        n //= 10&#10;    # Python handles arbitrarily large ints, but we enforce 32-bit constraint artificially if required.&#10;    return sign * rev_num</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">3</td>
      <td rowspan="1">Math 03 Check Palindrome</td>
      <td rowspan="1"><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-text">Example 1:&#10;Input: N = 121&#10;Output: true&#10;&#10;Example 2:&#10;Input: N = 123&#10;Output: false</code></pre></td>
      <td rowspan="1">-2<sup>31</sup> &le; N &le; 2<sup>31</sup> - 1</td>
      <td><b>Optimal</b></td>
      <td><code>O(log10(N))</code><br><i>Constraint</i></td>
      <td><code>O(1)</code><br><i>Constraint</i></td>
      <td><b>Variable Requirement:</b> Number is destroyed during loop, requires `dup` variable for final check.</td>
      <td><details><summary>View Code</summary><br><i>Note: Reverse the number mathematically and compare it to the original.</i><br><br><b>Implementation:</b><br><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def is_palindrome_optimal(n: int) -&gt; bool:&#10;    # Edge Case: Negative numbers are strictly not palindromes&#10;    if n &lt; 0: return False&#10;    &#10;    dup = n&#10;    rev_num = 0&#10;    while n &gt; 0:&#10;        ld = n % 10&#10;        rev_num = (rev_num * 10) + ld&#10;        n //= 10&#10;    return dup == rev_num</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">4</td>
      <td rowspan="2">Math 04 Gcd Or Hcf</td>
      <td rowspan="2"><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-text">Example 1:&#10;Input: N1 = 9, N2 = 12&#10;Output: 3&#10;&#10;Example 2:&#10;Input: N1 = 20, N2 = 15&#10;Output: 5</code></pre></td>
      <td rowspan="2">1 &le; N1, N2 &le; 10<sup>9</sup></td>
      <td><b>Brute Force</b></td>
      <td><code>O(min(N1, N2))</code><br><i>Trade-off</i></td>
      <td><code>O(1)</code><br><i>Constraint</i></td>
      <td><b>TLE Risk:</b> ~10<sup>9</sup> ops heavily exceeds 1 sec limit.</td>
      <td><details><summary>View Code</summary><br><i>Note: Iterate from min(N1, N2) down to 1. The first number dividing both is the GCD.</i><br><br><b>Implementation:</b><br><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def gcd_brute(n1: int, n2: int) -&gt; int:&#10;    for i in range(min(n1, n2), 0, -1):&#10;        if n1 % i == 0 and n2 % i == 0:&#10;            return i&#10;    return 1</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Optimal</b></td>
      <td><code>O(log(&Phi;)(min(N1, N2)))</code><br><i>Constraint</i></td>
      <td><code>O(1)</code><br><i>Constraint</i></td>
      <td><b>Modulo Safety:</b> Euclidean Algorithm easily passes 10<sup>9</sup> via log-scale modulo operations.</td>
      <td><details><summary>View Code</summary><br><i>Note: Euclidean algorithm: gcd(a, b) = gcd(b, a % b) until one becomes 0.</i><br><br><b>Implementation:</b><br><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def gcd_optimal(a: int, b: int) -&gt; int:&#10;    while a &gt; 0 and b &gt; 0:&#10;        # Uses modulo rather than subtraction for logarithmic time complexity&#10;        if a &gt; b:&#10;            a = a % b&#10;        else:&#10;            b = b % a&#10;    if a == 0:&#10;        return b&#10;    return a</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">5</td>
      <td rowspan="2">Math 06 Print All Divisors</td>
      <td rowspan="2"><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-text">Example 1:&#10;Input: N = 36&#10;Output: 1 2 3 4 6 9 12 18 36</code></pre></td>
      <td rowspan="2">1 &le; N &le; 10<sup>6</sup></td>
      <td><b>Brute Force</b></td>
      <td><code>O(N)</code><br><i>Trade-off</i></td>
      <td><code>O(1)</code><br><i>Constraint</i></td>
      <td><b>TLE Risk:</b> N=10^6 takes ~10<sup>6</sup> ops. Highly inefficient compared to optimal.</td>
      <td><details><summary>View Code</summary><br><i>Note: Iterate from 1 to N and check for divisibility.</i><br><br><b>Implementation:</b><br><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_divisors_brute(n: int) -&gt; None:&#10;    for i in range(1, n + 1):&#10;        if n % i == 0:&#10;            print(i, end=&quot; &quot;)</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Optimal</b></td>
      <td><code>O(&radic;N * log(&radic;N))</code><br><i>Constraint</i></td>
      <td><code>O(&radic;N)</code><br><i>Trade-off</i></td>
      <td><b>Perfect Squares:</b> Checking `(n / i) != i` explicitly prevents duplicate divisor entries.</td>
      <td><details><summary>View Code</summary><br><i>Note: Iterate up to sqrt(N) to find pairs of divisors, then sort.</i><br><br><b>Edge Case Code:</b><br><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python"></code></pre><br><b>Implementation:</b><br><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_divisors_optimal(n: int) -&gt; None:&#10;    divisors = []&#10;    for i in range(1, int(n**0.5) + 1):&#10;        if n % i == 0:&#10;            divisors.append(i)&#10;            # Edge Case: Avoid duplicate addition for perfect square roots&#10;            if n // i != i:&#10;                divisors.append(n // i)&#10;    divisors.sort()&#10;    for d in divisors:&#10;        print(d, end=&quot; &quot;)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">6</td>
      <td rowspan="2">Math 07 Check For Prime</td>
      <td rowspan="2"><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-text">Example 1:&#10;Input: N = 11&#10;Output: true&#10;&#10;Example 2:&#10;Input: N = 15&#10;Output: false</code></pre></td>
      <td rowspan="2">1 &le; N &le; 10<sup>9</sup></td>
      <td><b>Brute Force</b></td>
      <td><code>O(N)</code><br><i>Trade-off</i></td>
      <td><code>O(1)</code><br><i>Constraint</i></td>
      <td><b>TLE Guarantee:</b> N=10^9 takes ~10<sup>9</sup> ops. Guaranteed TLE on any modern platform.</td>
      <td><details><summary>View Code</summary><br><i>Note: Iterate from 2 to N-1 and check divisibility.</i><br><br><b>Implementation:</b><br><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def check_prime_brute(n: int) -&gt; bool:&#10;    if n &lt;= 1:&#10;        return False&#10;    for i in range(2, n):&#10;        if n % i == 0:&#10;            return False&#10;    return True</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Optimal</b></td>
      <td><code>O(&radic;N)</code><br><i>Constraint</i></td>
      <td><code>O(1)</code><br><i>Constraint</i></td>
      <td><b>Loop Optimization:</b> `i * i <= n` is far superior to computing `sqrt(n)` repeatedly.</td>
      <td><details><summary>View Code</summary><br><i>Note: Iterate from 2 up to sqrt(N) since divisors come in pairs.</i><br><br><b>Implementation:</b><br><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def check_prime_optimal(n: int) -&gt; bool:&#10;    if n &lt;= 1:&#10;        return False&#10;    limit = int(n**0.5)&#10;    for i in range(2, limit + 1):&#10;        if n % i == 0:&#10;            return False&#10;    return True</code></pre></details></td>
    </tr>
  </tbody>
</table>

<br>

