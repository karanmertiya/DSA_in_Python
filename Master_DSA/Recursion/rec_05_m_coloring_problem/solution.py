# Time Complexity: O(M^N)
# Space Complexity: O(N)
# Explanation: Backtracking. Try coloring each node with color 1 to m. For a color, check if any adjacent node has the same color. If safe, assign and recurse for next node. If recursion returns false, backtrack.

def graphColoring(graph: List[List[int]], m: int, n: int) -> bool:
    color = [0] * n
    def isSafe(node, col):
        for k in range(n):
            if k != node and graph[k][node] == 1 and color[k] == col: return False
        return True
    def solve(node):
        if node == n: return True
        for i in range(1, m + 1):
            if isSafe(node, i):
                color[node] = i
                if solve(node + 1): return True
                color[node] = 0
        return False
    return solve(0)

