# Patterns Revision Table

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
      <td>Pattern 1 Rectangular Star</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code>Example 1:&#10;Input: N = 3&#10;Output:&#10;***&#10;***&#10;***&#10;&#10;Example 2:&#10;Input: N = 5&#10;Output:&#10;*****&#10;*****&#10;*****&#10;*****&#10;*****</code></pre><br><br><b>Note (Constraint):</b> 1 &le; N &le; 20</td>
      <td><b>Time:</b> O(N<sup>2</sup>)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>Grid print restricts space to O(1). Time bounds hardcoded to area N&times;N.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(n):&#10;        print(&quot;*&quot; * n)&#10;&#10;if __name__ == &quot;__main__&quot;:&#10;    print_pattern(5)&#10;</code></pre></details></td>
    </tr>
    <tr>
      <td>2</td>
      <td>Pattern 2 Right Angled Triangle</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code>Example 1:&#10;Input: N = 3&#10;Output:&#10;*&#10;**&#10;***&#10;&#10;Example 2:&#10;Input: N = 5&#10;Output:&#10;*&#10;**&#10;***&#10;****&#10;*****</code></pre><br><br><b>Note (Constraint):</b> 1 &le; N &le; 20</td>
      <td><b>Time:</b> O(N<sup>2</sup>)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>Grid print restricts space to O(1). Time bounds hardcoded to area N&times;N.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(1, n + 1):&#10;        print(&quot;* &quot; * i)&#10;&#10;if __name__ == &quot;__main__&quot;:&#10;    print_pattern(5)&#10;</code></pre></details></td>
    </tr>
    <tr>
      <td>3</td>
      <td>Pattern 3 Right Angled Number Pyramid</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code>Example 1:&#10;Input: N = 3&#10;Output:&#10;1&#10;1 2&#10;1 2 3&#10;&#10;Example 2:&#10;Input: N = 5&#10;Output:&#10;1&#10;1 2&#10;1 2 3&#10;1 2 3 4&#10;1 2 3 4 5</code></pre><br><br><b>Note (Constraint):</b> 1 &le; N &le; 20</td>
      <td><b>Time:</b> O(N<sup>2</sup>)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>Grid print restricts space to O(1). Time bounds hardcoded to area N&times;N.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(1, n + 1):&#10;        for j in range(1, i + 1):&#10;            print(j, end=&quot; &quot;)&#10;        print()&#10;&#10;if __name__ == &quot;__main__&quot;:&#10;    print_pattern(5)&#10;</code></pre></details></td>
    </tr>
    <tr>
      <td>4</td>
      <td>Pattern 4 Right Angled Number Pyramid Ii</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code>Example 1:&#10;Input: N = 3&#10;Output:&#10;1&#10;2 2&#10;3 3 3&#10;&#10;Example 2:&#10;Input: N = 5&#10;Output:&#10;1&#10;2 2&#10;3 3 3&#10;4 4 4 4&#10;5 5 5 5 5</code></pre><br><br><b>Note (Constraint):</b> 1 &le; N &le; 20</td>
      <td><b>Time:</b> O(N<sup>2</sup>)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>Grid print restricts space to O(1). Time bounds hardcoded to area N&times;N.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(1, n + 1):&#10;        for j in range(1, i + 1):&#10;            print(i, end=&quot; &quot;)&#10;        print()&#10;&#10;if __name__ == &quot;__main__&quot;:&#10;    print_pattern(5)&#10;</code></pre></details></td>
    </tr>
    <tr>
      <td>5</td>
      <td>Pattern 5 Inverted Right Pyramid</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code>Example 1:&#10;Input: N = 3&#10;Output:&#10;* * *&#10;* *&#10;*&#10;&#10;Example 2:&#10;Input: N = 5&#10;Output:&#10;* * * * *&#10;* * * *&#10;* * *&#10;* *&#10;*</code></pre><br><br><b>Note (Constraint):</b> 1 &le; N &le; 20</td>
      <td><b>Time:</b> O(N<sup>2</sup>)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>Grid print restricts space to O(1). Time bounds hardcoded to area N&times;N.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(n, 0, -1):&#10;        print(&quot;* &quot; * i)&#10;&#10;if __name__ == &quot;__main__&quot;:&#10;    print_pattern(5)&#10;</code></pre></details></td>
    </tr>
    <tr>
      <td>6</td>
      <td>Pattern 6 Inverted Numbered Right Pyramid</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code>Example 1:&#10;Input: N = 3&#10;Output:&#10;1 2 3&#10;1 2&#10;1&#10;&#10;Example 2:&#10;Input: N = 5&#10;Output:&#10;1 2 3 4 5&#10;1 2 3 4&#10;1 2 3&#10;1 2&#10;1</code></pre><br><br><b>Note (Constraint):</b> 1 &le; N &le; 20</td>
      <td><b>Time:</b> O(N<sup>2</sup>)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>Grid print restricts space to O(1). Time bounds hardcoded to area N&times;N.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(n, 0, -1):&#10;        for j in range(1, i + 1):&#10;            print(j, end=&quot; &quot;)&#10;        print()&#10;&#10;if __name__ == &quot;__main__&quot;:&#10;    print_pattern(5)&#10;</code></pre></details></td>
    </tr>
    <tr>
      <td>7</td>
      <td>Pattern 7 Star Pyramid</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code>Example 1:&#10;Input: N = 3&#10;Output:&#10;  *&#10; ***&#10;*****&#10;&#10;Example 2:&#10;Input: N = 5&#10;Output:&#10;    *&#10;   ***&#10;  *****&#10; *******&#10;*********</code></pre><br><br><b>Note (Constraint):</b> 1 &le; N &le; 20</td>
      <td><b>Time:</b> O(N<sup>2</sup>)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>Grid print restricts space to O(1). Time bounds hardcoded to area N&times;N.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(n):&#10;        spaces = &quot; &quot; * (n - i - 1)&#10;        stars = &quot;*&quot; * (2 * i + 1)&#10;        print(spaces + stars + spaces)&#10;&#10;if __name__ == &quot;__main__&quot;:&#10;    print_pattern(5)&#10;</code></pre></details></td>
    </tr>
    <tr>
      <td>8</td>
      <td>Pattern 8 Inverted Star Pyramid</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code>Example 1:&#10;Input: N = 3&#10;Output:&#10;*****&#10; ***&#10;  *&#10;&#10;Example 2:&#10;Input: N = 5&#10;Output:&#10;*********&#10; *******&#10;  *****&#10;   ***&#10;    *</code></pre><br><br><b>Note (Constraint):</b> 1 &le; N &le; 20</td>
      <td><b>Time:</b> O(N<sup>2</sup>)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>Grid print restricts space to O(1). Time bounds hardcoded to area N&times;N.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(n):&#10;        spaces = &quot; &quot; * i&#10;        stars = &quot;*&quot; * (2 * (n - i) - 1)&#10;        print(spaces + stars + spaces)&#10;&#10;if __name__ == &quot;__main__&quot;:&#10;    print_pattern(5)&#10;</code></pre></details></td>
    </tr>
    <tr>
      <td>9</td>
      <td>Pattern 9 Diamond Star Pattern</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code>Example 1:&#10;Input: N = 3&#10;Output:&#10;  *&#10; ***&#10;*****&#10;*****&#10; ***&#10;  *&#10;</code></pre><br><br><b>Note (Constraint):</b> 1 &le; N &le; 20</td>
      <td><b>Time:</b> O(N<sup>2</sup>)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>Grid print restricts space to O(1). Time bounds hardcoded to area N&times;N.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(n):&#10;        spaces = &quot; &quot; * (n - i - 1)&#10;        stars = &quot;*&quot; * (2 * i + 1)&#10;        print(spaces + stars + spaces)&#10;    for i in range(n):&#10;        spaces = &quot; &quot; * i&#10;        stars = &quot;*&quot; * (2 * (n - i) - 1)&#10;        print(spaces + stars + spaces)&#10;&#10;if __name__ == &quot;__main__&quot;:&#10;    print_pattern(5)&#10;</code></pre></details></td>
    </tr>
    <tr>
      <td>10</td>
      <td>Pattern 10 Half Diamond Star Pattern</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code>Example 1:&#10;Input: N = 3&#10;Output:&#10;*&#10;**&#10;***&#10;**&#10;*&#10;</code></pre><br><br><b>Note (Constraint):</b> 1 &le; N &le; 20</td>
      <td><b>Time:</b> O(N<sup>2</sup>)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>Grid print restricts space to O(1). Time bounds hardcoded to area N&times;N.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(1, 2 * n):&#10;        stars = i if i &lt;= n else 2 * n - i&#10;        print(&quot;*&quot; * stars)&#10;&#10;if __name__ == &quot;__main__&quot;:&#10;    print_pattern(5)&#10;</code></pre></details></td>
    </tr>
    <tr>
      <td>11</td>
      <td>Pattern 11 Binary Number Triangle</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code>Example 1:&#10;Input: N = 3&#10;Output:&#10;1&#10;0 1&#10;1 0 1&#10;</code></pre><br><br><b>Note (Constraint):</b> 1 &le; N &le; 20</td>
      <td><b>Time:</b> O(N<sup>2</sup>)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>Grid print restricts space to O(1). Time bounds hardcoded to area N&times;N.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(n):&#10;        start = 1 if i % 2 == 0 else 0&#10;        for j in range(i + 1):&#10;            print(start, end=&quot; &quot;)&#10;            start = 1 - start&#10;        print()&#10;&#10;if __name__ == &quot;__main__&quot;:&#10;    print_pattern(5)&#10;</code></pre></details></td>
    </tr>
    <tr>
      <td>12</td>
      <td>Pattern 12 Number Crown Pattern</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code>Example 1:&#10;Input: N = 3&#10;Output:&#10;1    1&#10;12  21&#10;123321</code></pre><br><br><b>Note (Constraint):</b> 1 &le; N &le; 20</td>
      <td><b>Time:</b> O(N<sup>2</sup>)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>Grid print restricts space to O(1). Time bounds hardcoded to area N&times;N.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    space = 2 * (n - 1)&#10;    for i in range(1, n + 1):&#10;        for j in range(1, i + 1):&#10;            print(j, end=&quot;&quot;)&#10;        print(&quot; &quot; * space, end=&quot;&quot;)&#10;        for j in range(i, 0, -1):&#10;            print(j, end=&quot;&quot;)&#10;        print()&#10;        space -= 2&#10;&#10;if __name__ == &quot;__main__&quot;:&#10;    print_pattern(5)&#10;</code></pre></details></td>
    </tr>
    <tr>
      <td>13</td>
      <td>Pattern 13 Increasing Number Triangle</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code>Example 1:&#10;Input: N = 3&#10;Output:&#10;1&#10;2 3&#10;4 5 6</code></pre><br><br><b>Note (Constraint):</b> 1 &le; N &le; 20</td>
      <td><b>Time:</b> O(N<sup>2</sup>)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>Grid print restricts space to O(1). Time bounds hardcoded to area N&times;N.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    num = 1&#10;    for i in range(1, n + 1):&#10;        for j in range(1, i + 1):&#10;            print(num, end=&quot; &quot;)&#10;            num += 1&#10;        print()&#10;&#10;if __name__ == &quot;__main__&quot;:&#10;    print_pattern(5)&#10;</code></pre></details></td>
    </tr>
    <tr>
      <td>14</td>
      <td>Pattern 14 Increasing Letter Triangle</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code>Example 1:&#10;Input: N = 3&#10;Output:&#10;A&#10;A B&#10;A B C</code></pre><br><br><b>Note (Constraint):</b> 1 &le; N &le; 20</td>
      <td><b>Time:</b> O(N<sup>2</sup>)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>Grid print restricts space to O(1). Time bounds hardcoded to area N&times;N.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(n):&#10;        for j in range(i + 1):&#10;            print(chr(ord(&#x27;A&#x27;) + j), end=&quot; &quot;)&#10;        print()&#10;&#10;if __name__ == &quot;__main__&quot;:&#10;    print_pattern(5)&#10;</code></pre></details></td>
    </tr>
    <tr>
      <td>15</td>
      <td>Pattern 15 Reverse Letter Triangle</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code>Example 1:&#10;Input: N = 3&#10;Output:&#10;A B C&#10;A B&#10;A</code></pre><br><br><b>Note (Constraint):</b> 1 &le; N &le; 20</td>
      <td><b>Time:</b> O(N<sup>2</sup>)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>Grid print restricts space to O(1). Time bounds hardcoded to area N&times;N.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(n):&#10;        for j in range(n - i):&#10;            print(chr(ord(&#x27;A&#x27;) + j), end=&quot; &quot;)&#10;        print()&#10;&#10;if __name__ == &quot;__main__&quot;:&#10;    print_pattern(5)&#10;</code></pre></details></td>
    </tr>
    <tr>
      <td>16</td>
      <td>Pattern 16 Alpha Ramp Pattern</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code>Example 1:&#10;Input: N = 3&#10;Output:&#10;A&#10;B B&#10;C C C</code></pre><br><br><b>Note (Constraint):</b> 1 &le; N &le; 20</td>
      <td><b>Time:</b> O(N<sup>2</sup>)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>Grid print restricts space to O(1). Time bounds hardcoded to area N&times;N.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(n):&#10;        ch = chr(ord(&#x27;A&#x27;) + i)&#10;        for j in range(i + 1):&#10;            print(ch, end=&quot; &quot;)&#10;        print()&#10;&#10;if __name__ == &quot;__main__&quot;:&#10;    print_pattern(5)&#10;</code></pre></details></td>
    </tr>
    <tr>
      <td>17</td>
      <td>Pattern 17 Alpha Hill Pattern</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code>Example 1:&#10;Input: N = 3&#10;Output:&#10;  A&#10; ABA&#10;ABCBA</code></pre><br><br><b>Note (Constraint):</b> 1 &le; N &le; 20</td>
      <td><b>Time:</b> O(N<sup>2</sup>)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>Grid print restricts space to O(1). Time bounds hardcoded to area N&times;N.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(n):&#10;        spaces = &quot; &quot; * (n - i - 1)&#10;        print(spaces, end=&quot;&quot;)&#10;        ch = ord(&#x27;A&#x27;)&#10;        breakpoint = (2 * i + 1) // 2&#10;        for j in range(1, 2 * i + 2):&#10;            print(chr(ch), end=&quot;&quot;)&#10;            if j &lt;= breakpoint:&#10;                ch += 1&#10;            else:&#10;                ch -= 1&#10;        print(spaces)&#10;&#10;if __name__ == &quot;__main__&quot;:&#10;    print_pattern(5)&#10;</code></pre></details></td>
    </tr>
    <tr>
      <td>18</td>
      <td>Pattern 18 Alpha Triangle</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code>Example 1:&#10;Input: N = 3&#10;Output:&#10;C&#10;C B&#10;C B A</code></pre><br><br><b>Note (Constraint):</b> 1 &le; N &le; 20</td>
      <td><b>Time:</b> O(N<sup>2</sup>)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>Grid print restricts space to O(1). Time bounds hardcoded to area N&times;N.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(n):&#10;        ch = ord(&#x27;A&#x27;) + n - 1&#10;        for j in range(i + 1):&#10;            print(chr(ch - i + j), end=&quot; &quot;)&#10;        print()&#10;&#10;if __name__ == &quot;__main__&quot;:&#10;    print_pattern(5)&#10;</code></pre></details></td>
    </tr>
    <tr>
      <td>19</td>
      <td>Pattern 19 Symmetric Void Pattern</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code>Example 1:&#10;Input: N = 3&#10;Output:&#10;******&#10;**  **&#10;*    *&#10;*    *&#10;**  **&#10;******</code></pre><br><br><b>Note (Constraint):</b> 1 &le; N &le; 20</td>
      <td><b>Time:</b> O(N<sup>2</sup>)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>Grid print restricts space to O(1). Time bounds hardcoded to area N&times;N.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    iniSpace = 0&#10;    for i in range(n):&#10;        print(&quot;*&quot; * (n - i) + &quot; &quot; * iniSpace + &quot;*&quot; * (n - i))&#10;        iniSpace += 2&#10;    iniSpace = 2 * n - 2&#10;    for i in range(1, n + 1):&#10;        print(&quot;*&quot; * i + &quot; &quot; * iniSpace + &quot;*&quot; * i)&#10;        iniSpace -= 2&#10;&#10;if __name__ == &quot;__main__&quot;:&#10;    print_pattern(5)&#10;</code></pre></details></td>
    </tr>
    <tr>
      <td>20</td>
      <td>Pattern 20 Symmetric Butterfly Pattern</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code>Example 1:&#10;Input: N = 3&#10;Output:&#10;*    *&#10;**  **&#10;******&#10;**  **&#10;*    *</code></pre><br><br><b>Note (Constraint):</b> 1 &le; N &le; 20</td>
      <td><b>Time:</b> O(N<sup>2</sup>)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>Grid print restricts space to O(1). Time bounds hardcoded to area N&times;N.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    spaces = 2 * n - 2&#10;    for i in range(1, 2 * n):&#10;        stars = i if i &lt;= n else 2 * n - i&#10;        print(&quot;*&quot; * stars + &quot; &quot; * spaces + &quot;*&quot; * stars)&#10;        if i &lt; n:&#10;            spaces -= 2&#10;        else:&#10;            spaces += 2&#10;&#10;if __name__ == &quot;__main__&quot;:&#10;    print_pattern(5)&#10;</code></pre></details></td>
    </tr>
    <tr>
      <td>21</td>
      <td>Pattern 21 Hollow Rectangle Pattern</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code>Example 1:&#10;Input: N = 3&#10;Output:&#10;***&#10;* *&#10;***</code></pre><br><br><b>Note (Constraint):</b> 1 &le; N &le; 20</td>
      <td><b>Time:</b> O(N<sup>2</sup>)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>Grid print restricts space to O(1). Time bounds hardcoded to area N&times;N.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(n):&#10;        for j in range(n):&#10;            if i == 0 or j == 0 or i == n - 1 or j == n - 1:&#10;                print(&quot;*&quot;, end=&quot;&quot;)&#10;            else:&#10;                print(&quot; &quot;, end=&quot;&quot;)&#10;        print()&#10;&#10;if __name__ == &quot;__main__&quot;:&#10;    print_pattern(5)&#10;</code></pre></details></td>
    </tr>
    <tr>
      <td>22</td>
      <td>Pattern 22 The Number Pattern</td>
      <td><pre style="white-space: pre-wrap; word-wrap: break-word;"><code>Example 1:&#10;Input: N = 3&#10;Output:&#10;3 3 3 3 3&#10;3 2 2 2 3&#10;3 2 1 2 3&#10;3 2 2 2 3&#10;3 3 3 3 3</code></pre><br><br><b>Note (Constraint):</b> 1 &le; N &le; 20</td>
      <td><b>Time:</b> O(N<sup>2</sup>)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>Grid print restricts space to O(1). Time bounds hardcoded to area N&times;N.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def print_pattern(n: int) -&gt; None:&#10;    for i in range(2 * n - 1):&#10;        for j in range(2 * n - 1):&#10;            top = i&#10;            left = j&#10;            right = (2 * n - 2) - j&#10;            down = (2 * n - 2) - i&#10;            print(n - min(top, left, right, down), end=&quot; &quot;)&#10;        print()&#10;&#10;if __name__ == &quot;__main__&quot;:&#10;    print_pattern(4)&#10;</code></pre></details></td>
    </tr>
  </tbody>
</table>
