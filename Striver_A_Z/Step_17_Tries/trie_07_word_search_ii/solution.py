# Time Complexity: O(M * N * 4^L)
# Space Complexity: O(sum(L))
# Explanation: Insert all words into a Trie. Store the actual word at the `isEnd` node for easy retrieval. Do DFS from each cell. During DFS, traverse the Trie simultaneously. If a Trie node has a word, add it to results and remove the word from the node to avoid duplicates.

class Node:
    def __init__(self):
        self.links = [None] * 26
        self.word = ""
def findWords(board: List[List[str]], words: List[str]) -> List[str]:
    root = Node()
    for w in words:
        node = root
        for c in w:
            if not node.links[ord(c)-97]: node.links[ord(c)-97] = Node()
            node = node.links[ord(c)-97]
        node.word = w
    res = []
    def dfs(i, j, node):
        c = board[i][j]
        if c == '#' or not node.links[ord(c)-97]: return
        node = node.links[ord(c)-97]
        if node.word:
            res.append(node.word)
            node.word = ""
        board[i][j] = '#'
        for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if 0 <= i+x < len(board) and 0 <= j+y < len(board[0]):
                dfs(i+x, j+y, node)
        board[i][j] = c
    for i in range(len(board)):
        for j in range(len(board[0])):
            dfs(i, j, root)
    return res

