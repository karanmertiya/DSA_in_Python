# Time Complexity: O(M^N)
# Space Complexity: O(N)
# Explanation: Try coloring nodes one by one. For each node, try all M colors. Check if it's safe (no adjacent node has the same color). If safe, color it and recurse to the next node. If recursion returns true, we are done. Else backtrack and try next color.

def graphColoring(graph, m, n):
    color = [0] * n
    def isSafe(node, col):
        for k in range(n):
            if k != node and graph[k][node] == 1 and color[k] == col:
                return False
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

