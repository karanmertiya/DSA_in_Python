# Time Complexity: O(Word Length) for Add, O(26^Dots * Word Length) for Search
# Space Complexity: O(Total Chars)
# Explanation: Add words normally to the Trie. When searching, if the current character is '.', iterate over all 26 possible children and recursively search the remaining word. If any path returns true, the word is found.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True
    def search(self, word: str) -> bool:
        def searchInNode(i, node):
            if not node: return False
            if i == len(word): return node.isEnd
            if word[i] != '.':
                if word[i] not in node.children: return False
                return searchInNode(i + 1, node.children[word[i]])
            for child in node.children.values():
                if searchInNode(i + 1, child): return True
            return False
        return searchInNode(0, self.root)

