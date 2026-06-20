# Day 28 29 Tries Revision Table

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
      <td>Trie 01 Implement Trie Prefix Tree<br><br></b> <a href="https://leetcode.com/problems/implement-trie-prefix-tree/" target="_blank">LeetCode 208</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> SDE Sheet, Love Babbar, Striver A Z</details></td>
      <td>**Example 1:** `insert("apple")`, `search("apple")` -> true, `search("app")` -> false, `startsWith("app")` -> true.<br><br>**Note (Constraint):** 1 &le; word.length &le; 2000, lowercase English letters.</td>
      <td><b>Time:</b> O(Length of word) (Constraint)<br><b>Space:</b> O(Length * 26) per word</td>
      <td><b>Explanation:</b> Use a Tree where each node contains an array of 26 pointers (for 'a'-'z') and a boolean flag `isEnd`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class TrieNode:&#10;    def __init__(self):&#10;        self.children = {}&#10;        self.is_end = False&#10;&#10;class Trie:&#10;    def __init__(self):&#10;        self.root = TrieNode()&#10;&#10;    def insert(self, word: str) -&gt; None:&#10;        node = self.root&#10;        for char in word:&#10;            if char not in node.children:&#10;                node.children[char] = TrieNode()&#10;            node = node.children[char]&#10;        node.is_end = True&#10;&#10;    def search(self, word: str) -&gt; bool:&#10;        node = self.root&#10;        for char in word:&#10;            if char not in node.children:&#10;                return False&#10;            node = node.children[char]&#10;        return node.is_end&#10;&#10;    def startsWith(self, prefix: str) -&gt; bool:&#10;        node = self.root&#10;        for char in prefix:&#10;            if char not in node.children:&#10;                return False&#10;            node = node.children[char]&#10;        return True</code></pre></details></td>
    </tr>
    <tr>
      <td>2</td>
      <td>Trie 02 Implement Trie Ii<br><br></b> <a href="https://www.codingninjas.com/studio/problems/implement-trie_1387095" target="_blank">Coding Ninjas</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet, Apna College</details></td>
      <td>**Example 1:** Specialized Trie functions.</td>
      <td><b>Time:</b> O(len) per operation<br><b>Space:</b> O(N * len)</td>
      <td><b>Explanation:</b> Trie Nodes have a `cntEndWith` and `cntPrefix` integers. Increment `cntPrefix` dynamically as you insert, and `cntEndWith` at the final node. Decrement them during erase.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class Node:&#10;    def __init__(self):&#10;        self.links = [None] * 26&#10;        self.cntEndWith = 0&#10;        self.cntPrefix = 0&#10;class Trie:&#10;    def __init__(self):&#10;        self.root = Node()&#10;    def insert(self, word: str):&#10;        node = self.root&#10;        for ch in word:&#10;            idx = ord(ch) - 97&#10;            if not node.links[idx]: node.links[idx] = Node()&#10;            node = node.links[idx]&#10;            node.cntPrefix += 1&#10;        node.cntEndWith += 1&#10;    def countWordsEqualTo(self, word: str) -&gt; int:&#10;        node = self.root&#10;        for ch in word:&#10;            idx = ord(ch) - 97&#10;            if not node.links[idx]: return 0&#10;            node = node.links[idx]&#10;        return node.cntEndWith</code></pre></details></td>
    </tr>
  </tbody>
</table>
