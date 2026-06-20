# Time Complexity: O(N * M * 4^L)
# Space Complexity: O(L) recursion stack
# Explanation: Start DFS from each cell that matches the first letter of the word. In DFS, check 4 neighbors. Mark current cell as visited (e.g. change to '#') before moving to neighbors, and unmark (backtrack) after exploring.

def exist(board: List[List[str]], word: str) -> bool:
    def dfs(i, j, idx):
        if idx == len(word): return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[idx]:
            return False
        temp = board[i][j]
        board[i][j] = '#'
        found = (dfs(i+1, j, idx+1) or dfs(i-1, j, idx+1) or
                 dfs(i, j+1, idx+1) or dfs(i, j-1, idx+1))
        board[i][j] = temp
        return found
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0] and dfs(i, j, 0):
                return True
    return False

