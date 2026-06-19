# Time Complexity: O(N * alpha)
# Space Complexity: O(Max(Row, Col))
# Explanation: Treat rows and columns as nodes in DSU. Connect row `x` to column `y` for each stone. Max row and max col define the size of DSU. A column node index can be `maxRow + y + 1` to separate from row indices. The answer is `total stones - number of connected components`.

def removeStones(stones: List[List[int]]) -> int:
    maxRow = maxCol = 0
    for x, y in stones:
        maxRow = max(maxRow, x)
        maxCol = max(maxCol, y)
    ds = DisjointSet(maxRow + maxCol + 1)
    stoneNodes = set()
    for x, y in stones:
        nodeRow = x
        nodeCol = y + maxRow + 1
        ds.union(nodeRow, nodeCol)
        stoneNodes.add(nodeRow)
        stoneNodes.add(nodeCol)
    components = sum(1 for node in stoneNodes if ds.find(node) == node)
    return len(stones) - components

