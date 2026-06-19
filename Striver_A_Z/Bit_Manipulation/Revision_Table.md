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
      <td>1</td>
      <td>Bit 01 Swap Two Numbers<br><br></b> <a href='https://www.geeksforgeeks.org/problems/swap-two-numbers3844/1' target='_blank'>GeeksforGeeks</a></td>
      <td><b>Example 1:</b> Input: a=5, b=7, Output: a=7, b=5<br><br><b>Note (Constraint):</b> 1 &le; a, b &le; 10<sup>9</sup></td>
      <td><b>Time:</b> O(1)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>Integer Overflow:</b> Addition `a + b` can overflow if numbers are near `INT_MAX`.</td>
      <td><b>Explanation:</b> Use basic arithmetic (addition and subtraction) to swap.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def swap_arithmetic(a: int, b: int) -&gt; tuple:&#10;    a = a + b&#10;    b = a - b&#10;    a = a - b&#10;    return a, b</code></pre></details></td>
    </tr>
    <tr>
      <td>2</td>
      <td>Bit 02 Check Ith Bit Set<br><br></b> <a href='https://www.geeksforgeeks.org/problems/check-whether-k-th-bit-is-set-or-not-1587115620/1' target='_blank'>GeeksforGeeks</a></td>
      <td><b>Example 1:</b> Input: N=4 (100 in binary), i=2, Output: true<br><br><b>Note (Constraint):</b> 1 &le; N &le; 10<sup>9</sup>, 0 &le; i &le; 31</td>
      <td><b>Time:</b> O(1)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Right shift N by i times and check if the least significant bit is 1.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def check_kth_bit_right_shift(n: int, k: int) -&gt; bool:&#10;    return ((n &gt;&gt; k) &amp; 1) != 0</code></pre></details></td>
    </tr>
    <tr>
      <td>3</td>
      <td>Bit 03 Operations Set Clear Toggle<br><br></b> <a href='https://www.geeksforgeeks.org/problems/bit-manipulation-1666686020/1' target='_blank'>GeeksforGeeks</a></td>
      <td><b>Example 1:</b> N=70, i=3 -> Set:78, Clear:62, Toggle:78<br><br><b>Note (Constraint):</b> 1 &le; N &le; 10<sup>9</sup></td>
      <td><b>Time:</b> O(1) (Constraint)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>Shift Overflow:</b> `1LL` used strictly to prevent overflow beyond 31 bits.</td>
      <td><b>Explanation:</b> Use OR (`|`) to set, AND with NOT (`& ~`) to clear, and XOR (`^`) to toggle.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def bit_operations(n: int, i: int) -&gt; list:&#10;    set_bit = n | (1 &lt;&lt; i)&#10;    clear_bit = n &amp; ~(1 &lt;&lt; i)&#10;    toggle_bit = n ^ (1 &lt;&lt; i)&#10;    return [set_bit, clear_bit, toggle_bit]</code></pre></details></td>
    </tr>
    <tr>
      <td>4</td>
      <td>Bit 05 Power Of Two<br><br></b> <a href='https://leetcode.com/problems/power-of-two/' target='_blank'>LeetCode 231</a></td>
      <td><b>Example 1:</b> Input: N=16, Output: true<br><b>Example 2:</b> Input: N=3, Output: false<br><br><b>Note (Constraint):</b> -2<sup>31</sup> &le; N &le; 2<sup>31</sup> - 1</td>
      <td><b>Time:</b> O(log2(N)) (Trade-off)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>Zero/Negative Handle:</b> Powers of 2 must be strictly positive.</td>
      <td><b>Explanation:</b> Iteratively divide by 2. If it ever yields an odd number > 1, it is not a power of 2.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def is_power_of_two_brute(n: int) -&gt; bool:&#10;    if n &lt;= 0: return False&#10;    while n % 2 == 0:&#10;        n //= 2&#10;    return n == 1</code></pre></details></td>
    </tr>
    <tr>
      <td>5</td>
      <td>Bit 06 Count Set Bits<br><br></b> <a href='https://leetcode.com/problems/number-of-1-bits/' target='_blank'>LeetCode 191</a></td>
      <td><b>Example 1:</b> Input: N=11 (1011), Output: 3<br><br><b>Note (Constraint):</b> 1 &le; N &le; 2<sup>31</sup> - 1</td>
      <td><b>Time:</b> O(32) &cong; O(1) (Trade-off)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>Static Loop Iterations:</b> Loop always runs 32 times regardless of number size.</td>
      <td><b>Explanation:</b> Iterate through all 32 bits and check if each is set.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def hamming_weight_brute(n: int) -&gt; int:&#10;    count = 0&#10;    for i in range(32):&#10;        if (n &gt;&gt; i) &amp; 1:&#10;            count += 1&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td>6</td>
      <td>Bit 07 Minimum Bit Flips<br><br></b> <a href='https://leetcode.com/problems/minimum-bit-flips-to-convert-number/' target='_blank'>LeetCode 2220</a></td>
      <td><b>Example 1:</b> Input: start=10 (1010), goal=7 (0111), Output: 3 flips<br><br><b>Note (Constraint):</b> 0 &le; start, goal &le; 10<sup>9</sup></td>
      <td><b>Time:</b> O(Set Bits) (Constraint)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>XOR Magic:</b> XOR inherently maps identical bits to 0 and different bits to 1, instantly mapping the problem to Hamming Weight.</td>
      <td><b>Explanation:</b> XOR `start` and `goal` to isolate differing bits, then count the set bits in the result.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def min_bit_flips(start: int, goal: int) -&gt; int:&#10;    xor_res = start ^ goal&#10;    count = 0&#10;    while xor_res &gt; 0:&#10;        xor_res &amp;= (xor_res - 1)&#10;        count += 1&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td>7</td>
      <td>Bit 08 Single Number<br><br></b> <a href='https://leetcode.com/problems/single-number/' target='_blank'>LeetCode 136</a><br><br><b>Variants:</b><br>- What if elements are sorted? (Can use Binary Search `O(log N)` Time).<br>- What if elements are strictly positive? (Can use Array mapping if constraints allow).</td>
      <td><b>Example 1:</b> Input: nums = [4,1,2,1,2], Output: 4<br><br><b>Note (Constraint):</b> 1 &le; N &le; 3 * 10<sup>4</sup><br>-3 * 10<sup>4</sup> &le; nums[i] &le; 3 * 10<sup>4</sup></td>
      <td><b>Time:</b> O(N) (Constraint)<br><b>Space:</b> O(N) (Trade-off)</td>
      <td><b>Data Structure:</b><br><code>std::unordered_map</code> / <code>dict</code></td>
      <td><b>Memory Heavy:</b> Fails optimal space constraint due to dynamic hash mapping allocation.</td>
      <td><b>Explanation:</b> Use a Hash Map to count occurrences. Return the element with count 1.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def single_number_brute(nums: list[int]) -&gt; int:&#10;    freq = {}&#10;    for num in nums:&#10;        freq[num] = freq.get(num, 0) + 1&#10;    for num, count in freq.items():&#10;        if count == 1:&#10;            return num&#10;    return -1</code></pre></details></td>
    </tr>
    <tr>
      <td>8</td>
      <td>Bit 08 Power Set<br><br></b> <a href='https://leetcode.com/problems/subsets/' target='_blank'>LeetCode 78</a></td>
      <td><b>Example 1:</b> Input: nums = [1,2,3], Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]</td>
      <td><b>Time:</b> O(N * 2^N)<br><b>Space:</b> O(N * 2^N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Bit manipulation technique. For N elements, there are 2^N subsets. Count from 0 to 2^N - 1. For each number, its binary representation indicates which elements to include.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def subsets(nums: List[int]) -&gt; List[List[int]]:&#10;    n = len(nums)&#10;    subsets_count = 1 &lt;&lt; n&#10;    ans = []&#10;    for i in range(subsets_count):&#10;        subset = []&#10;        for j in range(n):&#10;            if i &amp; (1 &lt;&lt; j):&#10;                subset.append(nums[j])&#10;        ans.append(subset)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>9</td>
      <td>Bit 09 Two Odd Occurring Numbers<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/two-numbers-with-odd-occurrences5846/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Input: Arr = {4, 2, 4, 5, 2, 3, 3, 1}, Output: {5, 1}</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> 1) XOR all elements. Result is XOR of the two odd numbers. 2) Find the rightmost set bit in the result. 3) Divide array elements into two buckets based on this set bit. 4) XORing the two buckets individually yields the two numbers.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def twoOddNum(Arr: List[int], N: int) -&gt; List[int]:&#10;    xor_all = 0&#10;    for num in Arr: xor_all ^= num&#10;    right_set_bit = xor_all &amp; ~(xor_all - 1)&#10;    x, y = 0, 0&#10;    for num in Arr:&#10;        if num &amp; right_set_bit: x ^= num&#10;        else: y ^= num&#10;    if x &lt; y: x, y = y, x&#10;    return [x, y]</code></pre></details></td>
    </tr>
    <tr>
      <td>10</td>
      <td>Bm 16 Find The Original Array Of Prefix Xor<br><br></b> <a href='https://leetcode.com/problems/find-the-original-array-of-prefix-xor/' target='_blank'>LeetCode 2433</a></td>
      <td><b>Example 1:</b> `pref = [5,2,0,3,1]`. Output: `[5,7,2,3,2]`.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Since `pref[i] = pref[i-1] ^ arr[i]`, we can find `arr[i]` by doing `pref[i-1] ^ pref[i]`. `arr[0] = pref[0]`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findArray(pref: List[int]) -&gt; List[int]:&#10;    arr = [0] * len(pref)&#10;    arr[0] = pref[0]&#10;    for i in range(1, len(pref)):&#10;        arr[i] = pref[i-1] ^ pref[i]&#10;    return arr</code></pre></details></td>
    </tr>
    <tr>
      <td>11</td>
      <td>Bm 17 Maximum Xor For Each Query<br><br></b> <a href='https://leetcode.com/problems/maximum-xor-for-each-query/' target='_blank'>LeetCode 1829</a></td>
      <td><b>Example 1:</b> `nums = [0,1,1,3], maximumBit = 2`. Output: `[0,3,2,3]`.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> The maximum possible value is `(1 << maximumBit) - 1`. If current running XOR is `curr`, we want `k` such that `curr ^ k = max_val`. Thus `k = curr ^ max_val`. Do this iteratively backwards.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def getMaximumXor(nums: List[int], maximumBit: int) -&gt; List[int]:&#10;    curr = 0&#10;    for n in nums: curr ^= n&#10;    max_val = (1 &lt;&lt; maximumBit) - 1&#10;    ans = []&#10;    for i in range(len(nums)-1, -1, -1):&#10;        ans.append(curr ^ max_val)&#10;        curr ^= nums[i]&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>12</td>
      <td>Bm 18 Minimum Flips To Make A Or B Equal To C<br><br></b> <a href='https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/' target='_blank'>LeetCode 1318</a></td>
      <td><b>Example 1:</b> Bit by bit analysis.</td>
      <td><b>Time:</b> O(1) 32 bits<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Iterate through 32 bits. If bit in `c` is 1, at least one of `a` or `b` needs to be 1. If both are 0, flip one (1 flip). If bit in `c` is 0, both `a` and `b` must be 0. Flips needed = bit of `a` + bit of `b`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def minFlips(a: int, b: int, c: int) -&gt; int:&#10;    flips = 0&#10;    for i in range(32):&#10;        bit_a = (a &gt;&gt; i) &amp; 1&#10;        bit_b = (b &gt;&gt; i) &amp; 1&#10;        bit_c = (c &gt;&gt; i) &amp; 1&#10;        if bit_c == 1:&#10;            if bit_a == 0 and bit_b == 0: flips += 1&#10;        else:&#10;            flips += bit_a + bit_b&#10;    return flips</code></pre></details></td>
    </tr>
    <tr>
      <td>13</td>
      <td>Bm 19 Number Of Steps To Reduce A Number To Zero<br><br></b> <a href='https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/' target='_blank'>LeetCode 1342</a></td>
      <td><b>Example 1:</b> Simulation.</td>
      <td><b>Time:</b> O(log N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> If `num` is odd, subtract 1 (equivalent to clearing rightmost bit). If even, divide by 2 (equivalent to right shift). Can also be calculated by counting total bits and number of 1s.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def numberOfSteps(num: int) -&gt; int:&#10;    if num == 0: return 0&#10;    steps = 0&#10;    while num &gt; 0:&#10;        if num &amp; 1: num -= 1&#10;        else: num &gt;&gt;= 1&#10;        steps += 1&#10;    return steps</code></pre></details></td>
    </tr>
    <tr>
      <td>14</td>
      <td>Bm 20 Decode Xored Array<br><br></b> <a href='https://leetcode.com/problems/decode-xored-array/' target='_blank'>LeetCode 1720</a></td>
      <td><b>Example 1:</b> Sequential XOR.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Since `encoded[i] = arr[i] ^ arr[i+1]`, it implies `arr[i+1] = arr[i] ^ encoded[i]`. We have `arr[0]`, so we can iteratively find the rest.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def decode(encoded: List[int], first: int) -&gt; List[int]:&#10;    arr = [0] * (len(encoded) + 1)&#10;    arr[0] = first&#10;    for i in range(len(encoded)):&#10;        arr[i+1] = arr[i] ^ encoded[i]&#10;    return arr</code></pre></details></td>
    </tr>
    <tr>
      <td>15</td>
      <td>Bm 21 Find The Longest Substring Containing Vowels In Even Counts<br><br></b> <a href='https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/' target='_blank'>LeetCode 1371</a></td>
      <td><b>Example 1:</b> Bitmask and hashmap.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(32) since only 5 bits used</td>
      <td><code>#include <unordered_map></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Use a 5-bit mask to represent the parity of counts for 'a','e','i','o','u'. If we encounter a vowel, flip its bit. If the same mask is seen again at index `i` (was previously seen at `j`), then the substring `s[j+1...i]` has even vowel counts. Use a hash map to store first occurrence of each mask.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findTheLongestSubstring(s: str) -&gt; int:&#10;    m = {0: -1}&#10;    mask, maxLen = 0, 0&#10;    vowels = {&#x27;a&#x27;: 0, &#x27;e&#x27;: 1, &#x27;i&#x27;: 2, &#x27;o&#x27;: 3, &#x27;u&#x27;: 4}&#10;    for i, char in enumerate(s):&#10;        if char in vowels:&#10;            mask ^= (1 &lt;&lt; vowels[char])&#10;        if mask in m:&#10;            maxLen = max(maxLen, i - m[mask])&#10;        else:&#10;            m[mask] = i&#10;    return maxLen</code></pre></details></td>
    </tr>
    <tr>
      <td>16</td>
      <td>Bm 22 Subsets<br><br></b> <a href='https://leetcode.com/problems/subsets/' target='_blank'>LeetCode 78</a></td>
      <td><b>Example 1:</b> Bitmasking technique.</td>
      <td><b>Time:</b> O(N * 2^N)<br><b>Space:</b> O(2^N * N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Iterate from `0` to `2^N - 1`. If the `j`th bit is set in `i`, include `nums[j]` in the current subset.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def subsets(nums: List[int]) -&gt; List[List[int]]:&#10;    n = len(nums)&#10;    ans = []&#10;    for i in range(1 &lt;&lt; n):&#10;        sub = []&#10;        for j in range(n):&#10;            if i &amp; (1 &lt;&lt; j):&#10;                sub.append(nums[j])&#10;        ans.append(sub)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>17</td>
      <td>Bm 23 Single Number Iii<br><br></b> <a href='https://leetcode.com/problems/single-number-iii/' target='_blank'>LeetCode 260</a></td>
      <td><b>Example 1:</b> Grouping by rightmost set bit.</td>
      <td><b>Time:</b> O(N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>Overflow:</b> Rightmost set bit can be found using `val & -(unsigned int)val`.</td>
      <td><b>Explanation:</b> XOR all elements to get `x ^ y`. Find the rightmost set bit in this XOR result. This bit distinguishes `x` and `y`. Iterate through array again, divide numbers into two groups based on this bit, and XOR each group. The results are `x` and `y`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def singleNumber(nums: List[int]) -&gt; List[int]:&#10;    xor_all = 0&#10;    for n in nums: xor_all ^= n&#10;    rightmost_set_bit = xor_all &amp; -xor_all&#10;    x, y = 0, 0&#10;    for n in nums:&#10;        if n &amp; rightmost_set_bit: x ^= n&#10;        else: y ^= n&#10;    return [x, y]</code></pre></details></td>
    </tr>
    <tr>
      <td>18</td>
      <td>Bm 24 Divide Two Integers<br><br></b> <a href='https://leetcode.com/problems/divide-two-integers/' target='_blank'>LeetCode 29</a></td>
      <td><b>Example 1:</b> Bit shifting.</td>
      <td><b>Time:</b> O(log^2 N)<br><b>Space:</b> O(1)</td>
      <td>-</td>
      <td><b>INT_MIN:</b> Handle edge case `-2147483648 / -1 = 2147483647`.</td>
      <td><b>Explanation:</b> Use left shift to find the largest multiple of divisor that fits into dividend. Subtract it and add the shifted value to quotient. Repeat until dividend < divisor.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def divide(dividend: int, divisor: int) -&gt; int:&#10;    if dividend == -2147483648 and divisor == -1: return 2147483647&#10;    n, d = abs(dividend), abs(divisor)&#10;    sign = (dividend &lt; 0) == (divisor &lt; 0)&#10;    quotient = 0&#10;    while n &gt;= d:&#10;        temp, multiple = d, 1&#10;        while n &gt;= (temp &lt;&lt; 1):&#10;            temp &lt;&lt;= 1&#10;            multiple &lt;&lt;= 1&#10;        n -= temp&#10;        quotient += multiple&#10;    return quotient if sign else -quotient</code></pre></details></td>
    </tr>
    <tr>
      <td>19</td>
      <td>Bm 25 Xor Queries Of A Subarray<br><br></b> <a href='https://leetcode.com/problems/xor-queries-of-a-subarray/' target='_blank'>LeetCode 1310</a></td>
      <td><b>Example 1:</b> Prefix XOR array.</td>
      <td><b>Time:</b> O(N + Q)<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Create a prefix XOR array. Query answer for `[L, R]` is `prefix[R] ^ prefix[L-1]`. If `L == 0`, answer is `prefix[R]`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def xorQueries(arr: List[int], queries: List[List[int]]) -&gt; List[int]:&#10;    pref = [0] * len(arr)&#10;    pref[0] = arr[0]&#10;    for i in range(1, len(arr)):&#10;        pref[i] = pref[i-1] ^ arr[i]&#10;    ans = []&#10;    for l, r in queries:&#10;        if l == 0: ans.append(pref[r])&#10;        else: ans.append(pref[r] ^ pref[l-1])&#10;    return ans</code></pre></details></td>
    </tr>
  </tbody>
</table>
