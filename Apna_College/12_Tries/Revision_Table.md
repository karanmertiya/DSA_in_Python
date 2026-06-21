# 12 Tries Revision Table

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
      <td rowspan="1">Trie 01 Implement Trie II<br><br></b> <a href="https://www.codingninjas.com/studio/problems/implement-trie_1387095" target="_blank">Coding Ninjas</a></td>
      <td rowspan="1"><b>Example 1:</b> Specialized Trie functions.</td>
      <td><b>Time:</b> O(len) per operation<br><b>Space:</b> O(N * len)</td>
      <td>Trie Nodes have a `cntEndWith` and `cntPrefix` integers. Increment `cntPrefix` dynamically as you insert, and `cntEndWith` at the final node. Decrement them during erase.</td>
      <td><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class Node:&#10;    def __init__(self):&#10;        self.links = [None] * 26&#10;        self.cntEndWith = 0&#10;        self.cntPrefix = 0&#10;class Trie:&#10;    def __init__(self):&#10;        self.root = Node()&#10;    def insert(self, word: str):&#10;        node = self.root&#10;        for ch in word:&#10;            idx = ord(ch) - 97&#10;            if not node.links[idx]: node.links[idx] = Node()&#10;            node = node.links[idx]&#10;            node.cntPrefix += 1&#10;        node.cntEndWith += 1&#10;    def countWordsEqualTo(self, word: str) -&gt; int:&#10;        node = self.root&#10;        for ch in word:&#10;            idx = ord(ch) - 97&#10;            if not node.links[idx]: return 0&#10;            node = node.links[idx]&#10;        return node.cntEndWith</code></pre></details></td>
    </tr>
  </tbody>
</table>
