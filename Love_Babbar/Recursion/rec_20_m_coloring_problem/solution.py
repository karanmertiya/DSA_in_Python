# Time Complexity: O(M^N)
# Space Complexity: O(N)
# Explanation: Try coloring each node from `1` to `M`. Before coloring, check if it's safe (no adjacent node has same color). If safe, color it and recurse for next node. Backtrack if no color works.

def graphColoring(graph, m, V):
    color = [0] * V
    def isSafe(node, col):
        for k in range(V):
            if k != node and graph[k][node] == 1 and color[k] == col:
                return False
        return True
    def solve(node):
        if node == V: return True
        for i in range(1, m + 1):
            if isSafe(node, i):
                color[node] = i
                if solve(node + 1): return True
                color[node] = 0
        return False
    return solve(0)

