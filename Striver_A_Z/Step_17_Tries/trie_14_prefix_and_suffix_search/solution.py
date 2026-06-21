# Time Complexity: O(N * K^2) Insert, O(K) Search
# Space Complexity: O(N * K^2)
# Explanation: For each word, generate all possible suffixes, append a special character '{', and then append the original word. Insert all these combinations into a Trie along with the index. When querying, search for `suffix + '{' + prefix` in the Trie.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = -1
class WordFilter:
    def __init__(self, words: list[str]):
        self.root = TrieNode()
        for i, w in enumerate(words):
            for j in range(len(w) + 1):
                s = w[j:] + "{" + w
                node = self.root
                for char in s:
                    if char not in node.children:
                        node.children[char] = TrieNode()
                    node = node.children[char]
                    node.index = i
    def f(self, pref: str, suff: str) -> int:
        s = suff + "{" + pref
        node = self.root
        for char in s:
            if char not in node.children: return -1
            node = node.children[char]
        return node.index

