# Time Complexity: O(Total Chars)
# Space Complexity: O(Total Chars)
# Explanation: Insert all words into a Trie, marking the end of each word. Perform DFS on the Trie. Only proceed to children that are marked as the end of a word (i.e., `isEnd == true`). Keep track of the longest string found during DFS.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.word = ""
class Solution:
    def longestWord(self, words: list[str]) -> str:
        root = TrieNode()
        for w in words:
            node = root
            for c in w:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.isEnd = True
            node.word = w
        longest = ""
        def dfs(node):
            nonlocal longest
            if node.isEnd:
                if len(node.word) > len(longest) or (len(node.word) == len(longest) and node.word < longest):
                    longest = node.word
            for child in node.children.values():
                if child.isEnd:
                    dfs(child)
        for child in root.children.values():
            if child.isEnd:
                dfs(child)
        return longest

