# Time Complexity: O(N * max_len)
# Space Complexity: O(N * max_len)
# Explanation: Insert all words into a Trie. For each word, check if every prefix exists (i.e., every node from root to end has `isEnd == true`). Keep track of the longest valid word. Resolve ties lexicographically.

class Node:
    def __init__(self):
        self.links = [None] * 26
        self.flag = False
    def containsKey(self, ch):
        return self.links[ord(ch) - ord('a')] is not None
    def put(self, ch, node):
        self.links[ord(ch) - ord('a')] = node
    def get(self, ch):
        return self.links[ord(ch) - ord('a')]
    def setEnd(self): self.flag = True
    def isEnd(self): return self.flag
class Trie:
    def __init__(self):
        self.root = Node()
    def insert(self, word):
        node = self.root
        for ch in word:
            if not node.containsKey(ch): node.put(ch, Node())
            node = node.get(ch)
        node.setEnd()
    def checkAllPrefixes(self, word):
        node = self.root
        for ch in word:
            if node.containsKey(ch):
                node = node.get(ch)
                if not node.isEnd(): return False
            else: return False
        return True
def completeString(n: int, a: List[str]) -> str:
    trie = Trie()
    for word in a: trie.insert(word)
    longest = ""
    for word in a:
        if trie.checkAllPrefixes(word):
            if len(word) > len(longest):
                longest = word
            elif len(word) == len(longest) and word < longest:
                longest = word
    return longest if longest else "None"

