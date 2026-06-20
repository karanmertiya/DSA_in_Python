# Time Complexity: O(4^(N*N))
# Space Complexity: O(N*N)
# Explanation: Backtracking. Explore 4 directions (D, L, R, U) in lexicographical order to get sorted paths naturally. Mark cell as visited, recurse, then unmark (backtrack).

def findPath(m: List[List[int]], n: int) -> List[str]:
    ans = []
    vis = [[0 for _ in range(n)] for _ in range(n)]
    di = [1, 0, 0, -1]
    dj = [0, -1, 1, 0]
    dir_str = "DLRU"
    def solve(i, j, move):
        if i == n - 1 and j == n - 1:
            ans.append(move)
            return
        for ind in range(4):
            nexti, nextj = i + di[ind], j + dj[ind]
            if 0 <= nexti < n and 0 <= nextj < n and not vis[nexti][nextj] and m[nexti][nextj] == 1:
                vis[i][j] = 1
                solve(nexti, nextj, move + dir_str[ind])
                vis[i][j] = 0
    if m[0][0] == 1: solve(0, 0, "")
    return ans

