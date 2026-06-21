# Time Complexity: O(N) Add, O(N * 26) Search
# Space Complexity: O(Total Chars)
# Explanation: Store dictionary in a Trie. For searching, recursively traverse the Trie. Maintain a `modified` boolean flag. If characters mismatch, set `modified` to true and continue. If we reach the end of the word and `modified` is true, return true.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class MagicDictionary:
    def __init__(self):
        self.root = TrieNode()
    def buildDict(self, dictionary: list[str]) -> None:
        for word in dictionary:
            node = self.root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.isEnd = True
    def search(self, searchWord: str) -> bool:
        def dfs(i, node, modified):
            if i == len(searchWord): return modified and node.isEnd
            if modified:
                if searchWord[i] in node.children:
                    return dfs(i + 1, node.children[searchWord[i]], True)
                return False
            for char, child in node.children.items():
                if dfs(i + 1, child, char != searchWord[i]): return True
            return False
        return dfs(0, self.root, False)

