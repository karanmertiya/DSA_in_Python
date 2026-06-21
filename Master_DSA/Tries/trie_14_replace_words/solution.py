# Time Complexity: O(N * W)
# Space Complexity: O(Total Chars in Dict + Sentence Length)
# Explanation: Insert all dictionary roots into a Trie. For each word in the sentence, search the Trie. If a prefix matches a root (i.e., `isEnd` becomes true), replace the word with the root. If no root matches, keep the original word.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        root = TrieNode()
        for word in dictionary:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.isEnd = True
        def findRoot(word):
            node = root
            prefix = ""
            for char in word:
                if char not in node.children: break
                prefix += char
                node = node.children[char]
                if node.isEnd: return prefix
            return word
        return " ".join(findRoot(word) for word in sentence.split())

