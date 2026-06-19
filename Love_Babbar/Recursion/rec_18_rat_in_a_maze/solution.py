# Time Complexity: O(4^(N^2))
# Space Complexity: O(N^2)
# Explanation: Use backtracking to explore paths in lexicographical order: Down, Left, Right, Up (DLRU). Maintain a visited array. If destination is reached, add path to answers. Backtrack by unmarking visited.

def findPath(m: List[List[int]], n: int) -> List[str]:
    ans = []
    vis = [[0 for _ in range(n)] for _ in range(n)]
    di = [1, 0, 0, -1]
    dj = [0, -1, 1, 0]
    direction = "DLRU"
    def solve(i, j, move):
        if i == n - 1 and j == n - 1:
            ans.append(move)
            return
        for ind in range(4):
            nexti = i + di[ind]
            nextj = j + dj[ind]
            if 0 <= nexti < n and 0 <= nextj < n and not vis[nexti][nextj] and m[nexti][nextj] == 1:
                vis[i][j] = 1
                solve(nexti, nextj, move + direction[ind])
                vis[i][j] = 0
    if m[0][0] == 1: solve(0, 0, "")
    return ans

