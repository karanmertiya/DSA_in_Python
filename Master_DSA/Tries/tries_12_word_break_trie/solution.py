# Time Complexity: O(N^2)
# Space Complexity: O(N + sum of word lengths in dict)
# Explanation: Build a Trie with all words in `wordDict`. Use a recursive function with memoization `solve(i)` which returns true if the substring `s[i...]` can be segmented. Inside `solve(i)`, traverse the Trie starting from `s[i]`. If we reach a Trie node where `isEnd` is true, recursively call `solve(j+1)`. If any returns true, then `solve(i)` is true.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        root = TrieNode()
        for word in wordDict:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.isEnd = True
        memo = {}
        def solve(i):
            if i == len(s): return True
            if i in memo: return memo[i]
            node = root
            for j in range(i, len(s)):
                if s[j] not in node.children: break
                node = node.children[s[j]]
                if node.isEnd and solve(j + 1):
                    memo[i] = True
                    return True
            memo[i] = False
            return False
        return solve(0)

