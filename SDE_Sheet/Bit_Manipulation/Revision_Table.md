# Bit Manipulation Revision Table

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
      <td rowspan="2">1</td>
      <td rowspan="2">Bit 02 Check Ith Bit Set<br><br></b> <a href='https://www.geeksforgeeks.org/problems/check-whether-k-th-bit-is-set-or-not-1587115620/1' target='_blank'>GeeksforGeeks</a></td>
      <td rowspan="2"><b>Example 1:</b> Input: N=4 (100 in binary), i=2, Output: true<br><br><b>Note (Constraint):</b> 1 &le; N &le; 10<sup>9</sup>, 0 &le; i &le; 31</td>
      <td><b>Time:</b> O(1)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Right shift N by i times and check if the least significant bit is 1.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def check_kth_bit_right_shift(n: int, k: int) -&gt; bool:&#10;    return ((n &gt;&gt; k) &amp; 1) != 0</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(1) (Constraint)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>Shift Overflow:</b> If checking bits > 30, `1 << k` overflows a 32-bit signed int. Requires `1LL << k`.</td>
      <td><b>Explanation:</b> Left shift 1 by i times to create a mask, then bitwise AND with N.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def check_kth_bit_left_shift(n: int, k: int) -&gt; bool:&#10;    # Python handles arbitrary length ints natively&#10;    return (n &amp; (1 &lt;&lt; k)) != 0</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">2</td>
      <td rowspan="2">Bit 05 Power Of Two<br><br></b> <a href='https://leetcode.com/problems/power-of-two/' target='_blank'>LeetCode 231</a></td>
      <td rowspan="2"><b>Example 1:</b> Input: N=16, Output: true<br><b>Example 2:</b> Input: N=3, Output: false<br><br><b>Note (Constraint):</b> -2<sup>31</sup> &le; N &le; 2<sup>31</sup> - 1</td>
      <td><b>Time:</b> O(log2(N)) (Trade-off)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>Zero/Negative Handle:</b> Powers of 2 must be strictly positive.</td>
      <td><b>Explanation:</b> Iteratively divide by 2. If it ever yields an odd number > 1, it is not a power of 2.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def is_power_of_two_brute(n: int) -&gt; bool:&#10;    if n &lt;= 0: return False&#10;    while n % 2 == 0:&#10;        n //= 2&#10;    return n == 1</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(1) (Constraint)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>Underflow Check:</b> `N > 0` strictly blocks `n=0` or negatives which break the `n & (n-1)` logic.</td>
      <td><b>Explanation:</b> A power of 2 has exactly 1 set bit. Thus `N & (N-1)` must equal 0.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def is_power_of_two_optimal(n: int) -&gt; bool:&#10;    return (n &gt; 0) and ((n &amp; (n - 1)) == 0)</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">3</td>
      <td rowspan="2">Bit 06 Count Set Bits<br><br></b> <a href='https://leetcode.com/problems/number-of-1-bits/' target='_blank'>LeetCode 191</a></td>
      <td rowspan="2"><b>Example 1:</b> Input: N=11 (1011), Output: 3<br><br><b>Note (Constraint):</b> 1 &le; N &le; 2<sup>31</sup> - 1</td>
      <td><b>Time:</b> O(32) &cong; O(1) (Trade-off)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>Static Loop Iterations:</b> Loop always runs 32 times regardless of number size.</td>
      <td><b>Explanation:</b> Iterate through all 32 bits and check if each is set.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def hamming_weight_brute(n: int) -&gt; int:&#10;    count = 0&#10;    for i in range(32):&#10;        if (n &gt;&gt; i) &amp; 1:&#10;            count += 1&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(Set Bits) (Constraint)<br><b>Space:</b> O(1)</td>
      <td><b>Built-in Lib (Alternative):</b><br><code>__builtin_popcount(n)</code></td>
      <td><b>Dynamic Efficiency:</b> Time complexity is tightly bound strictly to the number of 1s, bypassing zeros completely.</td>
      <td><b>Explanation:</b> Brian Kernighan's Algorithm: Strip the lowest set bit using `N & (N-1)` until N reaches 0.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def hamming_weight_optimal(n: int) -&gt; int:&#10;    count = 0&#10;    while n &gt; 0:&#10;        n = n &amp; (n - 1)&#10;        count += 1&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">4</td>
      <td rowspan="2">Bit 08 Single Number<br><br></b> <a href='https://leetcode.com/problems/single-number/' target='_blank'>LeetCode 136</a><br><br><b>Variants:</b><br>- What if elements are sorted? (Can use Binary Search `O(log N)` Time).<br>- What if elements are strictly positive? (Can use Array mapping if constraints allow).</td>
      <td rowspan="2"><b>Example 1:</b> Input: nums = [4,1,2,1,2], Output: 4<br><br><b>Note (Constraint):</b> 1 &le; N &le; 3 * 10<sup>4</sup><br>-3 * 10<sup>4</sup> &le; nums[i] &le; 3 * 10<sup>4</sup></td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(N) (Trade-off)</td>
      <td><b>Data Structure:</b><br><code>std::unordered_map</code> / <code>dict</code></td>
      <td><b>Memory Heavy:</b> Fails optimal space constraint due to dynamic hash mapping allocation.</td>
      <td><b>Explanation:</b> Use a Hash Map to count occurrences. Return the element with count 1.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def single_number_brute(nums: list[int]) -&gt; int:&#10;    freq = {}&#10;    for num in nums:&#10;        freq[num] = freq.get(num, 0) + 1&#10;    for num, count in freq.items():&#10;        if count == 1:&#10;            return num&#10;    return -1</code></pre></details></td>
    </tr>
    <tr>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(1) (Constraint)</td>
      <td>-</td>
      <td><b>Commutativity:</b> XOR order doesn't matter, natively eliminating negative numbers constraints seamlessly.</td>
      <td><b>Explanation:</b> XOR all elements. Identical pairs cancel out (A ^ A = 0), leaving only the unique element (0 ^ B = B).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def single_number_optimal(nums: list[int]) -&gt; int:&#10;    xor_res = 0&#10;    for num in nums:&#10;        xor_res ^= num&#10;    return xor_res</code></pre></details></td>
    </tr>
  </tbody>
</table>
