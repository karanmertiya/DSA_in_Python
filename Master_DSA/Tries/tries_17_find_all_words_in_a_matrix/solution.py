# Time Complexity: O(N * M * 4^L) where L is max word length
# Space Complexity: O(Total Chars in Dict)
# Explanation: Build a Trie from the dictionary. Perform DFS from every cell in the matrix. During DFS, traverse the Trie simultaneously. If `node.word` is found, add it to result and clear `node.word` to prevent duplicates. Mark visited cells to avoid loops.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = ""
class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = TrieNode()
        for w in words:
            node = root
            for c in w:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.word = w
        ans = []
        def dfs(i, j, node):
            c = board[i][j]
            if c == '#' or c not in node.children: return
            node = node.children[c]
            if node.word:
                ans.append(node.word)
                node.word = ""
            board[i][j] = '#'
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                r, c_nxt = i + dr, j + dc
                if 0 <= r < len(board) and 0 <= c_nxt < len(board[0]):
                    dfs(r, c_nxt, node)
            board[i][j] = c
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, root)
        return sorted(ans)

