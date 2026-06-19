# Time Complexity: O(N * M * 8 * L)
# Space Complexity: O(1)
# Explanation: Iterate through the grid. For each matching starting character, check all 8 directions to see if the full word exists in a straight line.

def searchWord(grid, word):
    R, C, L = len(grid), len(grid[0]), len(word)
    dr = [-1, -1, -1, 0, 0, 1, 1, 1]
    dc = [-1, 0, 1, -1, 1, -1, 0, 1]
    ans = []
    for r in range(R):
        for c in range(C):
            if grid[r][c] == word[0]:
                for dir in range(8):
                    currR, currC = r + dr[dir], c + dc[dir]
                    k = 1
                    while k < L:
                        if currR < 0 or currR >= R or currC < 0 or currC >= C: break
                        if grid[currR][currC] != word[k]: break
                        currR += dr[dir]
                        currC += dc[dir]
                        k += 1
                    if k == L:
                        ans.append([r, c])
                        break
    return ans

