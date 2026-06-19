# Time Complexity: O(4^(N*N))
# Space Complexity: O(N*N)
# Explanation: Start DFS from (0,0). Try D, L, R, U sequentially. If valid and not visited, mark visited, append direction to path, recurse, then unmark (backtrack) and pop direction. If reached (N-1, N-1), add path to results.

def findPath(m, n):
    ans = []
    vis = [[0 for _ in range(n)] for _ in range(n)]
    dirs = "DLRU"
    di = [1, 0, 0, -1]
    dj = [0, -1, 1, 0]
    def solve(i, j, move):
        if i == n - 1 and j == n - 1:
            ans.append(move)
            return
        for ind in range(4):
            ni = i + di[ind]
            nj = j + dj[ind]
            if 0 <= ni < n and 0 <= nj < n and not vis[ni][nj] and m[ni][nj] == 1:
                vis[i][j] = 1
                solve(ni, nj, move + dirs[ind])
                vis[i][j] = 0
    if m[0][0] == 1:
        solve(0, 0, "")
    return ans

