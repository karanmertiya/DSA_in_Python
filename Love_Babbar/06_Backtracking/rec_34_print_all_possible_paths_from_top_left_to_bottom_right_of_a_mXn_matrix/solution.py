# Time Complexity: O(2^(M+N))
# Space Complexity: O(M+N)
# Explanation: Use simple DFS from top-left. From cell (i, j), we can move to (i+1, j) or (i, j+1). Keep track of the path elements in an array/list. When reaching bottom-right, print/save the path.

def findPaths(mat, i, j, path, ans):
    if i == len(mat) - 1 and j == len(mat[0]) - 1:
        ans.append(path + [mat[i][j]])
        return
    path.append(mat[i][j])
    if i + 1 < len(mat): findPaths(mat, i + 1, j, path, ans)
    if j + 1 < len(mat[0]): findPaths(mat, i, j + 1, path, ans)
    path.pop()

