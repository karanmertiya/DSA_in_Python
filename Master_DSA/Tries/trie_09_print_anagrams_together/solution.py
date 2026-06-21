# Time Complexity: O(N * K log K)
# Space Complexity: O(N * K)
# Explanation: Sort each string to form a key. Insert the sorted key into the Trie. At the end node of the key in the Trie, store a list of indices representing the original strings that map to this key.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.indices = []
class Solution:
    def Anagrams(self, string_list):
        root = TrieNode()
        for i, word in enumerate(string_list):
            sorted_word = "".join(sorted(word))
            node = root
            for char in sorted_word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.indices.append(i)
        ans = []
        def traverse(node):
            if node.indices:
                ans.append([string_list[i] for i in node.indices])
            for child in node.children.values():
                traverse(child)
        traverse(root)
        return ans

