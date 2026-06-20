# Time Complexity: O(len) per operation
# Space Complexity: O(N * len)
# Explanation: Trie Nodes have a `cntEndWith` and `cntPrefix` integers. Increment `cntPrefix` dynamically as you insert, and `cntEndWith` at the final node. Decrement them during erase.

class Node:
    def __init__(self):
        self.links = [None] * 26
        self.cntEndWith = 0
        self.cntPrefix = 0
class Trie:
    def __init__(self):
        self.root = Node()
    def insert(self, word: str):
        node = self.root
        for ch in word:
            idx = ord(ch) - 97
            if not node.links[idx]: node.links[idx] = Node()
            node = node.links[idx]
            node.cntPrefix += 1
        node.cntEndWith += 1
    def countWordsEqualTo(self, word: str) -> int:
        node = self.root
        for ch in word:
            idx = ord(ch) - 97
            if not node.links[idx]: return 0
            node = node.links[idx]
        return node.cntEndWith

