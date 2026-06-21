# Step 08 Bit Manipulation Revision Table

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
      <td rowspan="1">Math 01 Power Of Two<br><br></b> <a href="https://leetcode.com/problems/power-of-two/" target="_blank">LeetCode 231</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> SDE Sheet, Love Babbar, Striver A Z</details></td>
      <td rowspan="1"><b>Example 1:</b> Bit Manipulation.</td>
      <td><b>Time:</b> O(1)<br><b>Space:</b> O(1)</td>
      <td>If a number is a power of two, it has exactly one bit set in its binary representation. The expression `n & (n - 1)` clears the lowest set bit. Thus, if `n > 0` and `(n & (n - 1)) == 0`, it is a power of two.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isPowerOfTwo(n: int) -&gt; bool:&#10;    return n &gt; 0 and (n &amp; (n - 1)) == 0</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">2</td>
      <td rowspan="2">Bit 02 Swap Two Numbers<br><br></b> <a href="https://www.geeksforgeeks.org/problems/swap-two-numbers3844/1" target="_blank">GeeksforGeeks</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
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
      <td rowspan="2">3</td>
      <td rowspan="2">Bit 03 Check Ith Bit Set<br><br></b> <a href="https://www.geeksforgeeks.org/problems/check-whether-k-th-bit-is-set-or-not-1587115620/1" target="_blank">GeeksforGeeks</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
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
      <td rowspan="1">4</td>
      <td rowspan="1">Bit 04 Operations Set Clear Toggle<br><br></b> <a href="https://www.geeksforgeeks.org/problems/bit-manipulation-1666686020/1" target="_blank">GeeksforGeeks</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td rowspan="1"><b> </b><br>N=70, i=3 -> Set:78, Clear:62, Toggle:78<br><br><b> </b> 1 &le; N &le; 10<sup>9</sup></td>
      <td><b>Time:</b> O(1)<br><b>Space:</b> O(1)</td>
      <td>Use OR (`|`) to set, AND with NOT (`& ~`) to clear, and XOR (`^`) to toggle.</td>
      <td><b>Edge Cases:</b> **Shift Overflow:** `1LL` used strictly to prevent overflow beyond 31 bits.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def bit_operations(n: int, i: int) -&gt; list:&#10;    set_bit = n | (1 &lt;&lt; i)&#10;    clear_bit = n &amp; ~(1 &lt;&lt; i)&#10;    toggle_bit = n ^ (1 &lt;&lt; i)&#10;    return [set_bit, clear_bit, toggle_bit]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">5</td>
      <td rowspan="2">Bit 05 Divide Two Integers<br><br></b> <a href="https://leetcode.com/problems/divide-two-integers/" target="_blank">LeetCode 29</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
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
      <td rowspan="2">Bit 06 Count Set Bits<br><br></b> <a href="https://leetcode.com/problems/number-of-1-bits/" target="_blank">LeetCode 191</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
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
      <td rowspan="1">7</td>
      <td rowspan="1">Bit 07 Minimum Bit Flips To Convert Number<br><br></b> <a href="https://leetcode.com/problems/minimum-bit-flips-to-convert-number/" target="_blank">LeetCode 2220</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td rowspan="1"><b> </b><br><br><b>Input:</b> start=10 (1010), goal=7 (0111)<br><b>Output:</b> 3 flips</td>
      <td><b>Time:</b> O(Set Bits)<br><b>Space:</b> O(1)</td>
      <td>XOR `start` and `goal` to isolate differing bits, then count the set bits in the result.</td>
      <td><b>Edge Cases:</b> **XOR Magic:** XOR inherently maps identical bits to 0 and different bits to 1, instantly mapping the problem to Hamming Weight.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def min_bit_flips(start: int, goal: int) -&gt; int:&#10;    xor_res = start ^ goal&#10;    count = 0&#10;    while xor_res &gt; 0:&#10;        xor_res &amp;= (xor_res - 1)&#10;        count += 1&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">8</td>
      <td rowspan="2">Bit 08 Single Number<br><br></b> <a href="https://leetcode.com/problems/single-number/" target="_blank">LeetCode 136</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> SDE Sheet, Striver A Z, Love Babbar</details></td>
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
      <td rowspan="2">9</td>
      <td rowspan="2">Bit 09 Single Number II<br><br></b> <a href="https://leetcode.com/problems/single-number-ii/" target="_blank">LeetCode 137</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
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
      <td rowspan="1">10</td>
      <td rowspan="1">Bit 10 Single Number III<br><br></b> <a href="https://leetcode.com/problems/single-number-iii/" target="_blank">LeetCode 260</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td rowspan="1"><b> </b><br><br><b>Input:</b> nums = [1,2,1,3,2,5]<br><b>Output:</b> [3,5]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>XOR all elements to get `x ^ y`. Find the rightmost set bit in this XOR result. This bit distinguishes `x` and `y`. Iterate through array again, divide numbers into two groups based on this bit, and XOR each group. The results are `x` and `y`.</td>
      <td><b>Edge Cases:</b> **Overflow:** Rightmost set bit can be found using `val & -(unsigned int)val`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def singleNumber(nums: list[int]) -&gt; list[int]:&#10;    xor_all = 0&#10;    for n in nums: xor_all ^= n&#10;    rightmost_set_bit = xor_all &amp; -xor_all&#10;    x, y = 0, 0&#10;    for n in nums:&#10;        if n &amp; rightmost_set_bit: x ^= n&#10;        else: y ^= n&#10;    return [x, y]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="2">11</td>
      <td rowspan="2">Bit 11 Subsets<br><br></b> <a href="https://leetcode.com/problems/subsets/" target="_blank">LeetCode 78</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> SDE Sheet, Striver A Z, Love Babbar</details></td>
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
      <td rowspan="1">12</td>
      <td rowspan="1">Bit 12 Find The Original Array Of Prefix Xor<br><br></b> <a href="https://leetcode.com/problems/find-the-original-array-of-prefix-xor/" target="_blank">LeetCode 2433</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td rowspan="1"><b> </b> `pref = [5,2,0,3,1]`.<br><b>Output:</b> `[5,7,2,3,2]`.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Since `pref[i] = pref[i-1] ^ arr[i]`, we can find `arr[i]` by doing `pref[i-1] ^ pref[i]`. `arr[0] = pref[0]`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findArray(pref: list[int]) -&gt; list[int]:&#10;    arr = [0] * len(pref)&#10;    arr[0] = pref[0]&#10;    for i in range(1, len(pref)):&#10;        arr[i] = pref[i-1] ^ pref[i]&#10;    return arr</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">13</td>
      <td rowspan="1">Bit 13 Maximum Xor For Each Query<br><br></b> <a href="https://leetcode.com/problems/maximum-xor-for-each-query/" target="_blank">LeetCode 1829</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td rowspan="1"><b> </b> `nums = [0,1,1,3], maximumBit = 2`.<br><b>Output:</b> `[0,3,2,3]`.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>The maximum possible value is `(1 << maximumBit) - 1`. If current running XOR is `curr`, we want `k` such that `curr ^ k = max_val`. Thus `k = curr ^ max_val`. Do this iteratively backwards.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def getMaximumXor(nums: list[int], maximumBit: int) -&gt; list[int]:&#10;    curr = 0&#10;    for n in nums: curr ^= n&#10;    max_val = (1 &lt;&lt; maximumBit) - 1&#10;    ans = []&#10;    for i in range(len(nums)-1, -1, -1):&#10;        ans.append(curr ^ max_val)&#10;        curr ^= nums[i]&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">14</td>
      <td rowspan="1">Bit 14 Minimum Flips To Make A Or B Equal To C<br><br></b> <a href="https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/" target="_blank">LeetCode 1318</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td rowspan="1"><b> </b><br><br><b>Input:</b> a=2, b=6, c=5<br><b>Output:</b> 3</td>
      <td><b>Time:</b> O(1)<br><b>Space:</b> O(1)</td>
      <td>Iterate through 32 bits. If bit in `c` is 1, at least one of `a` or `b` needs to be 1. If both are 0, flip one (1 flip). If bit in `c` is 0, both `a` and `b` must be 0. Flips needed = bit of `a` + bit of `b`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minFlips(a: int, b: int, c: int) -&gt; int:&#10;    flips = 0&#10;    for i in range(32):&#10;        bit_a = (a &gt;&gt; i) &amp; 1&#10;        bit_b = (b &gt;&gt; i) &amp; 1&#10;        bit_c = (c &gt;&gt; i) &amp; 1&#10;        if bit_c == 1:&#10;            if bit_a == 0 and bit_b == 0: flips += 1&#10;        else:&#10;            flips += bit_a + bit_b&#10;    return flips</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">15</td>
      <td rowspan="1">Bit 15 Number Of Steps To Reduce To Zero<br><br></b> <a href="https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/" target="_blank">LeetCode 1342</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td rowspan="1"><b> </b><br><br><b>Input:</b> num = 14<br><b>Output:</b> 6</td>
      <td><b>Time:</b> O(log N)<br><b>Space:</b> O(1)</td>
      <td>If `num` is odd, subtract 1 (equivalent to clearing rightmost bit). If even, divide by 2 (equivalent to right shift).</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def numberOfSteps(num: int) -&gt; int:&#10;    if num == 0: return 0&#10;    steps = 0&#10;    while num &gt; 0:&#10;        if num &amp; 1: num -= 1&#10;        else: num &gt;&gt;= 1&#10;        steps += 1&#10;    return steps</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">16</td>
      <td rowspan="1">Bit 16 Decode Xored Array<br><br></b> <a href="https://leetcode.com/problems/decode-xored-array/" target="_blank">LeetCode 1720</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td rowspan="1"><b> </b><br><br><b>Input:</b> encoded=[1,2,3], first=1<br><b>Output:</b> [1,0,2,1]</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>Since `encoded[i] = arr[i] ^ arr[i+1]`, it implies `arr[i+1] = arr[i] ^ encoded[i]`. We have `arr[0]`, so we can iteratively find the rest.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def decode(encoded: list[int], first: int) -&gt; list[int]:&#10;    arr = [0] * (len(encoded) + 1)&#10;    arr[0] = first&#10;    for i in range(len(encoded)):&#10;        arr[i+1] = arr[i] ^ encoded[i]&#10;    return arr</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">17</td>
      <td rowspan="1">Bit 17 Longest Substring Vowels Even Counts<br><br></b> <a href="https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/" target="_blank">LeetCode 1371</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td rowspan="1"><b> </b><br><br><b>Input:</b> s = "eleetminicoworoep"<br><b>Output:</b> 13</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(32) since only 5 bits used</td>
      <td>Use a 5-bit mask to represent the parity of counts for 'a','e','i','o','u'. If we encounter a vowel, flip its bit. If the same mask is seen again at index `i` (was previously seen at `j`), then the substring `s[j+1...i]` has even vowel counts. Use a hash map to store first occurrence of each mask.<br><br><b>Dependencies:</b> <code>#include <unordered_map></code></td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findTheLongestSubstring(s: str) -&gt; int:&#10;    m = {0: -1}&#10;    mask, maxLen = 0, 0&#10;    vowels = {&#x27;a&#x27;: 0, &#x27;e&#x27;: 1, &#x27;i&#x27;: 2, &#x27;o&#x27;: 3, &#x27;u&#x27;: 4}&#10;    for i, char in enumerate(s):&#10;        if char in vowels:&#10;            mask ^= (1 &lt;&lt; vowels[char])&#10;        if mask in m:&#10;            maxLen = max(maxLen, i - m[mask])&#10;        else:&#10;            m[mask] = i&#10;    return maxLen</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">18</td>
      <td rowspan="1">Bit 18 Xor Queries Of A Subarray<br><br></b> <a href="https://leetcode.com/problems/xor-queries-of-a-subarray/" target="_blank">LeetCode 1310</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar</details></td>
      <td rowspan="1"><b> </b><br><br><b>Input:</b> arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]<br><b>Output:</b> [2,7,14,8]</td>
      <td><b>Time:</b> O(N + Q)<br><b>Space:</b> O(N)</td>
      <td>Create a prefix XOR array. Query answer for `[L, R]` is `prefix[R] ^ prefix[L-1]`. If `L == 0`, answer is `prefix[R]`.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def xorQueries(arr: list[int], queries: list[list[int]]) -&gt; list[int]:&#10;    pref = [0] * len(arr)&#10;    pref[0] = arr[0]&#10;    for i in range(1, len(arr)):&#10;        pref[i] = pref[i-1] ^ arr[i]&#10;    ans = []&#10;    for l, r in queries:&#10;        if l == 0: ans.append(pref[r])&#10;        else: ans.append(pref[r] ^ pref[l-1])&#10;    return ans</code></pre></details></td>
    </tr>
  </tbody>
</table>
