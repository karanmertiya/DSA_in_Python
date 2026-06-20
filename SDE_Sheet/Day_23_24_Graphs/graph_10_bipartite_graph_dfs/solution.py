# Time Complexity: O(V + E)
# Space Complexity: O(V)
# Explanation: DFS. Color nodes with 0 and 1. If an adjacent node is uncolored, assign the opposite color and recurse. If it's colored and has the same color, it's not bipartite.

def isBipartite(V: int, adj: List[List[int]]) -> bool:
    color = [-1] * V
    def dfs(node, col):
        color[node] = col
        for it in adj[node]:
            if color[it] == -1:
                if not dfs(it, 1 - col): return False
            elif color[it] == col:
                return False
        return True
    for i in range(V):
        if color[i] == -1:
            if not dfs(i, 0): return False
    return True

