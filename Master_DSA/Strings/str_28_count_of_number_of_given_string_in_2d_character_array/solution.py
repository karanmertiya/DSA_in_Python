# Time Complexity: O(R * C * 4^L)
# Space Complexity: O(L)
# Explanation: Use DFS. For each cell, if it matches the first character of the word, start a DFS to look for the rest of the word in all 4 directions. Keep track of visited cells.

def findOccurrence(mat, target):
    def dfs(r, c, idx):
        if idx == len(target): return 1
        if r < 0 or r >= len(mat) or c < 0 or c >= len(mat[0]) or mat[r][c] != target[idx]: return 0
        temp = mat[r][c]
        mat[r][c] = '#'
        found = (dfs(r + 1, c, idx + 1) +
                 dfs(r - 1, c, idx + 1) +
                 dfs(r, c + 1, idx + 1) +
                 dfs(r, c - 1, idx + 1))
        mat[r][c] = temp
        return found
    count = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == target[0]:
                count += dfs(i, j, 0)
    return count

