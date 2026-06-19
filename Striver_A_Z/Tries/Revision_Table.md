# Tries Revision Table

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
      <td rowspan="1">1</td>
      <td rowspan="1">Trie 01 Implement Trie Prefix Tree<br><br></b> <a href='https://leetcode.com/problems/implement-trie-prefix-tree/' target='_blank'>LeetCode 208</a></td>
      <td rowspan="1"><b>Example 1:</b> `insert("apple")`, `search("apple")` -> true, `search("app")` -> false, `startsWith("app")` -> true.<br><br><b>Note (Constraint):</b> 1 &le; word.length &le; 2000, lowercase English letters.</td>
      <td><b>Time:</b> O(Length of word) (Constraint)<br><b>Space:</b> O(Length * 26) per word</td>
      <td>Custom Node Struct/Class</td>
      <td><b>startsWith vs search:</b> `startsWith` returns true simply if the traversal succeeds without hitting NULL. `search` requires the final node's `isEnd` flag to be true.</td>
      <td><b>Explanation:</b> Use a Tree where each node contains an array of 26 pointers (for 'a'-'z') and a boolean flag `isEnd`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class TrieNode:&#10;    def __init__(self):&#10;        self.children = {}&#10;        self.is_end = False&#10;&#10;class Trie:&#10;    def __init__(self):&#10;        self.root = TrieNode()&#10;&#10;    def insert(self, word: str) -&gt; None:&#10;        node = self.root&#10;        for char in word:&#10;            if char not in node.children:&#10;                node.children[char] = TrieNode()&#10;            node = node.children[char]&#10;        node.is_end = True&#10;&#10;    def search(self, word: str) -&gt; bool:&#10;        node = self.root&#10;        for char in word:&#10;            if char not in node.children:&#10;                return False&#10;            node = node.children[char]&#10;        return node.is_end&#10;&#10;    def startsWith(self, prefix: str) -&gt; bool:&#10;        node = self.root&#10;        for char in prefix:&#10;            if char not in node.children:&#10;                return False&#10;            node = node.children[char]&#10;        return True</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">2</td>
      <td rowspan="1">Tries 02 Implement Trie Ii<br><br></b> <a href='https://www.codingninjas.com/studio/problems/implement-trie_1387095' target='_blank'>Coding Ninjas</a></td>
      <td rowspan="1"><b>Example 1:</b> Specialized Trie functions.</td>
      <td><b>Time:</b> O(len) per operation<br><b>Space:</b> O(N * len)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Trie Nodes have a `cntEndWith` and `cntPrefix` integers. Increment `cntPrefix` dynamically as you insert, and `cntEndWith` at the final node. Decrement them during erase.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class Node:&#10;    def __init__(self):&#10;        self.links = [None] * 26&#10;        self.cntEndWith = 0&#10;        self.cntPrefix = 0&#10;class Trie:&#10;    def __init__(self):&#10;        self.root = Node()&#10;    def insert(self, word: str):&#10;        node = self.root&#10;        for ch in word:&#10;            idx = ord(ch) - 97&#10;            if not node.links[idx]: node.links[idx] = Node()&#10;            node = node.links[idx]&#10;            node.cntPrefix += 1&#10;        node.cntEndWith += 1&#10;    def countWordsEqualTo(self, word: str) -&gt; int:&#10;        node = self.root&#10;        for ch in word:&#10;            idx = ord(ch) - 97&#10;            if not node.links[idx]: return 0&#10;            node = node.links[idx]&#10;        return node.cntEndWith</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">3</td>
      <td rowspan="1">Trie 22 Implement Trie Prefix Tree<br><br></b> <a href='https://leetcode.com/problems/implement-trie-prefix-tree/' target='_blank'>LeetCode 208</a></td>
      <td rowspan="1"><b>Example 1:</b> Standard Trie with 26 links.</td>
      <td><b>Time:</b> O(length of word) for all operations<br><b>Space:</b> O(total characters inserted * 26)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Create a Node struct with an array of 26 Node pointers and a boolean `flag`. Insert: Traverse characters, create new nodes if missing, mark last node's `flag = true`. Search: Traverse characters, return false if missing link, else return `flag` of last node. StartsWith: Similar to Search but return true at the end without checking `flag`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class Node:&#10;    def __init__(self):&#10;        self.links = [None] * 26&#10;        self.flag = False&#10;    def containsKey(self, ch):&#10;        return self.links[ord(ch) - ord(&#x27;a&#x27;)] is not None&#10;    def put(self, ch, node):&#10;        self.links[ord(ch) - ord(&#x27;a&#x27;)] = node&#10;    def get(self, ch):&#10;        return self.links[ord(ch) - ord(&#x27;a&#x27;)]&#10;    def setEnd(self):&#10;        self.flag = True&#10;    def isEnd(self):&#10;        return self.flag&#10;&#10;class Trie:&#10;    def __init__(self):&#10;        self.root = Node()&#10;    def insert(self, word: str) -&gt; None:&#10;        node = self.root&#10;        for ch in word:&#10;            if not node.containsKey(ch):&#10;                node.put(ch, Node())&#10;            node = node.get(ch)&#10;        node.setEnd()&#10;    def search(self, word: str) -&gt; bool:&#10;        node = self.root&#10;        for ch in word:&#10;            if not node.containsKey(ch):&#10;                return False&#10;            node = node.get(ch)&#10;        return node.isEnd()&#10;    def startsWith(self, prefix: str) -&gt; bool:&#10;        node = self.root&#10;        for ch in prefix:&#10;            if not node.containsKey(ch):&#10;                return False&#10;            node = node.get(ch)&#10;        return True</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">4</td>
      <td rowspan="1">Trie 23 Implement Trie Ii<br><br></b> <a href='https://www.codingninjas.com/codestudio/problems/implement-trie_1387095' target='_blank'>Coding Ninjas</a></td>
      <td rowspan="1"><b>Example 1:</b> Trie with counts.</td>
      <td><b>Time:</b> O(length of word)<br><b>Space:</b> O(total characters * 26)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Modify Node to store `countEndsWith` and `countPrefix`. Increment `countPrefix` while traversing during insertion, and `countEndsWith` at the end. For erase, decrement these counts.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class Node:&#10;    def __init__(self):&#10;        self.links = [None] * 26&#10;        self.cntEndWith = 0&#10;        self.cntPrefix = 0&#10;    def containsKey(self, ch):&#10;        return self.links[ord(ch) - ord(&#x27;a&#x27;)] is not None&#10;    def put(self, ch, node):&#10;        self.links[ord(ch) - ord(&#x27;a&#x27;)] = node&#10;    def get(self, ch):&#10;        return self.links[ord(ch) - ord(&#x27;a&#x27;)]&#10;    def increaseEnd(self): self.cntEndWith += 1&#10;    def increasePrefix(self): self.cntPrefix += 1&#10;    def deleteEnd(self): self.cntEndWith -= 1&#10;    def reducePrefix(self): self.cntPrefix -= 1&#10;    def getEnd(self): return self.cntEndWith&#10;    def getPrefix(self): return self.cntPrefix&#10;&#10;class Trie:&#10;    def __init__(self):&#10;        self.root = Node()&#10;    def insert(self, word: str) -&gt; None:&#10;        node = self.root&#10;        for ch in word:&#10;            if not node.containsKey(ch):&#10;                node.put(ch, Node())&#10;            node = node.get(ch)&#10;            node.increasePrefix()&#10;        node.increaseEnd()&#10;    def countWordsEqualTo(self, word: str) -&gt; int:&#10;        node = self.root&#10;        for ch in word:&#10;            if not node.containsKey(ch):&#10;                return 0&#10;            node = node.get(ch)&#10;        return node.getEnd()&#10;    def countWordsStartingWith(self, prefix: str) -&gt; int:&#10;        node = self.root&#10;        for ch in prefix:&#10;            if not node.containsKey(ch):&#10;                return 0&#10;            node = node.get(ch)&#10;        return node.getPrefix()&#10;    def erase(self, word: str) -&gt; None:&#10;        node = self.root&#10;        for ch in word:&#10;            if node.containsKey(ch):&#10;                node = node.get(ch)&#10;                node.reducePrefix()&#10;            else:&#10;                return&#10;        node.deleteEnd()</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">5</td>
      <td rowspan="1">Trie 24 Longest String With All Prefixes<br><br></b> <a href='https://www.codingninjas.com/codestudio/problems/complete-string_2687860' target='_blank'>Coding Ninjas</a></td>
      <td rowspan="1"><b>Example 1:</b> Insert all, check each word.</td>
      <td><b>Time:</b> O(N * max_len)<br><b>Space:</b> O(N * max_len)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Insert all words into a Trie. For each word, check if every prefix exists (i.e., every node from root to end has `isEnd == true`). Keep track of the longest valid word. Resolve ties lexicographically.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class Node:&#10;    def __init__(self):&#10;        self.links = [None] * 26&#10;        self.flag = False&#10;    def containsKey(self, ch):&#10;        return self.links[ord(ch) - ord(&#x27;a&#x27;)] is not None&#10;    def put(self, ch, node):&#10;        self.links[ord(ch) - ord(&#x27;a&#x27;)] = node&#10;    def get(self, ch):&#10;        return self.links[ord(ch) - ord(&#x27;a&#x27;)]&#10;    def setEnd(self): self.flag = True&#10;    def isEnd(self): return self.flag&#10;class Trie:&#10;    def __init__(self):&#10;        self.root = Node()&#10;    def insert(self, word):&#10;        node = self.root&#10;        for ch in word:&#10;            if not node.containsKey(ch): node.put(ch, Node())&#10;            node = node.get(ch)&#10;        node.setEnd()&#10;    def checkAllPrefixes(self, word):&#10;        node = self.root&#10;        for ch in word:&#10;            if node.containsKey(ch):&#10;                node = node.get(ch)&#10;                if not node.isEnd(): return False&#10;            else: return False&#10;        return True&#10;def completeString(n: int, a: List[str]) -&gt; str:&#10;    trie = Trie()&#10;    for word in a: trie.insert(word)&#10;    longest = &quot;&quot;&#10;    for word in a:&#10;        if trie.checkAllPrefixes(word):&#10;            if len(word) &gt; len(longest):&#10;                longest = word&#10;            elif len(word) == len(longest) and word &lt; longest:&#10;                longest = word&#10;    return longest if longest else &quot;None&quot;</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">6</td>
      <td rowspan="1">Trie 25 Number Of Distinct Substrings In A String<br><br></b> <a href='https://www.codingninjas.com/codestudio/problems/count-distinct-substrings_985292' target='_blank'>Coding Ninjas</a></td>
      <td rowspan="1"><b>Example 1:</b> Insert all suffixes.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N^2)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> To find all substrings, iterate `i` from 0 to N-1, and `j` from `i` to N-1. Each sequence `s[i...j]` is a substring. Insert it into the Trie. Every time we create a new node, it corresponds to a new distinct substring. Increment count. Add 1 for the empty substring.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class Node:&#10;    def __init__(self):&#10;        self.links = [None] * 26&#10;    def containsKey(self, ch):&#10;        return self.links[ord(ch) - ord(&#x27;a&#x27;)] is not None&#10;    def put(self, ch, node):&#10;        self.links[ord(ch) - ord(&#x27;a&#x27;)] = node&#10;    def get(self, ch):&#10;        return self.links[ord(ch) - ord(&#x27;a&#x27;)]&#10;def countDistinctSubstrings(s: str) -&gt; int:&#10;    root = Node()&#10;    count = 0&#10;    for i in range(len(s)):&#10;        node = root&#10;        for j in range(i, len(s)):&#10;            if not node.containsKey(s[j]):&#10;                node.put(s[j], Node())&#10;                count += 1&#10;            node = node.get(s[j])&#10;    return count + 1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">7</td>
      <td rowspan="1">Trie 26 Maximum Xor Of Two Numbers In An Array<br><br></b> <a href='https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/' target='_blank'>LeetCode 421</a></td>
      <td rowspan="1"><b>Example 1:</b> Bit Trie.</td>
      <td><b>Time:</b> O(N * 32)<br><b>Space:</b> O(N * 32)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Insert binary representation of each number (from MSB to LSB, 31 to 0) into a Trie. To find max XOR for `x`, traverse the Trie aiming for opposite bits (1 for 0, 0 for 1). If opposite bit exists, go that way and add `1 << i` to result. Else go same way.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class Node:&#10;    def __init__(self):&#10;        self.links = [None, None]&#10;    def containsKey(self, bit): return self.links[bit] is not None&#10;    def put(self, bit, node): self.links[bit] = node&#10;    def get(self, bit): return self.links[bit]&#10;class Trie:&#10;    def __init__(self):&#10;        self.root = Node()&#10;    def insert(self, num):&#10;        node = self.root&#10;        for i in range(31, -1, -1):&#10;            bit = (num &gt;&gt; i) &amp; 1&#10;            if not node.containsKey(bit):&#10;                node.put(bit, Node())&#10;            node = node.get(bit)&#10;    def getMax(self, num):&#10;        node = self.root&#10;        maxNum = 0&#10;        for i in range(31, -1, -1):&#10;            bit = (num &gt;&gt; i) &amp; 1&#10;            if node.containsKey(1 - bit):&#10;                maxNum |= (1 &lt;&lt; i)&#10;                node = node.get(1 - bit)&#10;            else:&#10;                node = node.get(bit)&#10;        return maxNum&#10;def findMaximumXOR(nums: List[int]) -&gt; int:&#10;    trie = Trie()&#10;    for num in nums: trie.insert(num)&#10;    maxi = 0&#10;    for num in nums:&#10;        maxi = max(maxi, trie.getMax(num))&#10;    return maxi</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">8</td>
      <td rowspan="1">Trie 27 Maximum Xor With An Element From Array<br><br></b> <a href='https://leetcode.com/problems/maximum-xor-with-an-element-from-array/' target='_blank'>LeetCode 1707</a></td>
      <td rowspan="1"><b>Example 1:</b> Offline Queries.</td>
      <td><b>Time:</b> O(N log N + Q log Q + Q * 32 + N * 32)<br><b>Space:</b> O(N * 32 + Q)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Sort `nums` array. Store queries as `{m, x, index}` and sort them by `m`. Iterate through queries. While `nums[i] <= m`, insert `nums[i]` into Trie. If Trie is empty, answer is -1. Else, query Trie for max XOR with `x`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class Node:&#10;    def __init__(self):&#10;        self.links = [None, None]&#10;    def containsKey(self, bit): return self.links[bit] is not None&#10;    def put(self, bit, node): self.links[bit] = node&#10;    def get(self, bit): return self.links[bit]&#10;class Trie:&#10;    def __init__(self):&#10;        self.root = Node()&#10;    def insert(self, num):&#10;        node = self.root&#10;        for i in range(31, -1, -1):&#10;            bit = (num &gt;&gt; i) &amp; 1&#10;            if not node.containsKey(bit): node.put(bit, Node())&#10;            node = node.get(bit)&#10;    def getMax(self, num):&#10;        node = self.root&#10;        maxNum = 0&#10;        for i in range(31, -1, -1):&#10;            bit = (num &gt;&gt; i) &amp; 1&#10;            if node.containsKey(1 - bit):&#10;                maxNum |= (1 &lt;&lt; i)&#10;                node = node.get(1 - bit)&#10;            else:&#10;                node = node.get(bit)&#10;        return maxNum&#10;def maximizeXor(nums: List[int], queries: List[List[int]]) -&gt; List[int]:&#10;    nums.sort()&#10;    oQ = sorted([(q[1], q[0], i) for i, q in enumerate(queries)])&#10;    ans = [0] * len(queries)&#10;    trie = Trie()&#10;    ind = 0&#10;    for m, x, qInd in oQ:&#10;        while ind &lt; len(nums) and nums[ind] &lt;= m:&#10;            trie.insert(nums[ind])&#10;            ind += 1&#10;        if ind == 0: ans[qInd] = -1&#10;        else: ans[qInd] = trie.getMax(x)&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">9</td>
      <td rowspan="1">Trie 28 Word Break Trie<br><br></b> <a href='https://leetcode.com/problems/word-break/' target='_blank'>LeetCode 139</a></td>
      <td rowspan="1"><b>Example 1:</b> DP with Trie search.</td>
      <td><b>Time:</b> O(N^2 + sum(word_len))<br><b>Space:</b> O(N + sum(word_len))</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Insert all dictionary words into a Trie. Use DP where `dp[i]` is true if `s[0...i-1]` is valid. For index `i`, start a Trie search. If we find a valid word ending at `j`, then `dp[j+1]` becomes true (if `dp[i]` was true).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class Node:&#10;    def __init__(self):&#10;        self.links = [None] * 26&#10;        self.isEnd = False&#10;class Trie:&#10;    def __init__(self): self.root = Node()&#10;    def insert(self, word):&#10;        node = self.root&#10;        for c in word:&#10;            if not node.links[ord(c)-97]: node.links[ord(c)-97] = Node()&#10;            node = node.links[ord(c)-97]&#10;        node.isEnd = True&#10;def wordBreak(s: str, wordDict: List[str]) -&gt; bool:&#10;    t = Trie()&#10;    for w in wordDict: t.insert(w)&#10;    dp = [False] * (len(s) + 1)&#10;    dp[0] = True&#10;    for i in range(len(s)):&#10;        if not dp[i]: continue&#10;        node = t.root&#10;        for j in range(i, len(s)):&#10;            if not node.links[ord(s[j])-97]: break&#10;            node = node.links[ord(s[j])-97]&#10;            if node.isEnd: dp[j+1] = True&#10;    return dp[-1]</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">10</td>
      <td rowspan="1">Trie 29 Word Search Ii<br><br></b> <a href='https://leetcode.com/problems/word-search-ii/' target='_blank'>LeetCode 212</a></td>
      <td rowspan="1"><b>Example 1:</b> DFS + Trie.</td>
      <td><b>Time:</b> O(M * N * 4^L)<br><b>Space:</b> O(sum(L))</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Insert all words into a Trie. Store the actual word at the `isEnd` node for easy retrieval. Do DFS from each cell. During DFS, traverse the Trie simultaneously. If a Trie node has a word, add it to results and remove the word from the node to avoid duplicates.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class Node:&#10;    def __init__(self):&#10;        self.links = [None] * 26&#10;        self.word = &quot;&quot;&#10;def findWords(board: List[List[str]], words: List[str]) -&gt; List[str]:&#10;    root = Node()&#10;    for w in words:&#10;        node = root&#10;        for c in w:&#10;            if not node.links[ord(c)-97]: node.links[ord(c)-97] = Node()&#10;            node = node.links[ord(c)-97]&#10;        node.word = w&#10;    res = []&#10;    def dfs(i, j, node):&#10;        c = board[i][j]&#10;        if c == &#x27;#&#x27; or not node.links[ord(c)-97]: return&#10;        node = node.links[ord(c)-97]&#10;        if node.word:&#10;            res.append(node.word)&#10;            node.word = &quot;&quot;&#10;        board[i][j] = &#x27;#&#x27;&#10;        for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:&#10;            if 0 &lt;= i+x &lt; len(board) and 0 &lt;= j+y &lt; len(board[0]):&#10;                dfs(i+x, j+y, node)&#10;        board[i][j] = c&#10;    for i in range(len(board)):&#10;        for j in range(len(board[0])):&#10;            dfs(i, j, root)&#10;    return res</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">11</td>
      <td rowspan="1">Trie 30 Palindrome Pairs<br><br></b> <a href='https://leetcode.com/problems/palindrome-pairs/' target='_blank'>LeetCode 336</a></td>
      <td rowspan="1"><b>Example 1:</b> Trie of reversed words.</td>
      <td><b>Time:</b> O(N * L^2)<br><b>Space:</b> O(N * L)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Insert the REVERSE of every word into a Trie. Store index of word at node. For each word, search the Trie. Three cases: 1. Trie word is longer (current word exhausted, check if rest of Trie branch is palindrome). 2. Current word is longer (Trie exhausted, check if rest of current word is palindrome). 3. Exact match. Store valid indices.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class Node:&#10;    def __init__(self):&#10;        self.links = [None] * 26&#10;        self.idx = -1&#10;        self.pal_indices = []&#10;def is_pal(s, i, j):&#10;    while i &lt; j:&#10;        if s[i] != s[j]: return False&#10;        i += 1; j -= 1&#10;    return True&#10;def palindromePairs(words: List[str]) -&gt; List[List[int]]:&#10;    root = Node()&#10;    for i, w in enumerate(words):&#10;        node = root&#10;        for j in range(len(w) - 1, -1, -1):&#10;            if is_pal(w, 0, j): node.pal_indices.append(i)&#10;            idx = ord(w[j]) - 97&#10;            if not node.links[idx]: node.links[idx] = Node()&#10;            node = node.links[idx]&#10;        node.idx = i&#10;        node.pal_indices.append(i)&#10;    res = []&#10;    for i, w in enumerate(words):&#10;        node = root&#10;        valid = True&#10;        for j in range(len(w)):&#10;            if node.idx != -1 and node.idx != i and is_pal(w, j, len(w)-1):&#10;                res.append([i, node.idx])&#10;            idx = ord(w[j]) - 97&#10;            if not node.links[idx]:&#10;                valid = False&#10;                break&#10;            node = node.links[idx]&#10;        if valid:&#10;            for pid in node.pal_indices:&#10;                if i != pid: res.append([i, pid])&#10;    return res</code></pre></details></td>
    </tr>
  </tbody>
</table>
