# Time Complexity: O(length of word)
# Space Complexity: O(total characters * 26)
# Explanation: Modify Node to store `countEndsWith` and `countPrefix`. Increment `countPrefix` while traversing during insertion, and `countEndsWith` at the end. For erase, decrement these counts.

class Node:
    def __init__(self):
        self.links = [None] * 26
        self.cntEndWith = 0
        self.cntPrefix = 0
    def containsKey(self, ch):
        return self.links[ord(ch) - ord('a')] is not None
    def put(self, ch, node):
        self.links[ord(ch) - ord('a')] = node
    def get(self, ch):
        return self.links[ord(ch) - ord('a')]
    def increaseEnd(self): self.cntEndWith += 1
    def increasePrefix(self): self.cntPrefix += 1
    def deleteEnd(self): self.cntEndWith -= 1
    def reducePrefix(self): self.cntPrefix -= 1
    def getEnd(self): return self.cntEndWith
    def getPrefix(self): return self.cntPrefix

class Trie:
    def __init__(self):
        self.root = Node()
    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                node.put(ch, Node())
            node = node.get(ch)
            node.increasePrefix()
        node.increaseEnd()
    def countWordsEqualTo(self, word: str) -> int:
        node = self.root
        for ch in word:
            if not node.containsKey(ch):
                return 0
            node = node.get(ch)
        return node.getEnd()
    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.root
        for ch in prefix:
            if not node.containsKey(ch):
                return 0
            node = node.get(ch)
        return node.getPrefix()
    def erase(self, word: str) -> None:
        node = self.root
        for ch in word:
            if node.containsKey(ch):
                node = node.get(ch)
                node.reducePrefix()
            else:
                return
        node.deleteEnd()

