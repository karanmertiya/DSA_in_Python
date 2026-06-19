# Time Complexity: O(N^2 + sum(word_len))
# Space Complexity: O(N + sum(word_len))
# Explanation: Insert all dictionary words into a Trie. Use DP where `dp[i]` is true if `s[0...i-1]` is valid. For index `i`, start a Trie search. If we find a valid word ending at `j`, then `dp[j+1]` becomes true (if `dp[i]` was true).

class Node:
    def __init__(self):
        self.links = [None] * 26
        self.isEnd = False
class Trie:
    def __init__(self): self.root = Node()
    def insert(self, word):
        node = self.root
        for c in word:
            if not node.links[ord(c)-97]: node.links[ord(c)-97] = Node()
            node = node.links[ord(c)-97]
        node.isEnd = True
def wordBreak(s: str, wordDict: List[str]) -> bool:
    t = Trie()
    for w in wordDict: t.insert(w)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(len(s)):
        if not dp[i]: continue
        node = t.root
        for j in range(i, len(s)):
            if not node.links[ord(s[j])-97]: break
            node = node.links[ord(s[j])-97]
            if node.isEnd: dp[j+1] = True
    return dp[-1]

