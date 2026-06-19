# Time Complexity: O(V + E)
# Space Complexity: O(V)
# Explanation: Use DFS. Maintain a `visited` array and a `pathVisited` array. Mark both as true for the current node. Recurse for adjacent nodes. If an adjacent node is `visited` AND `pathVisited`, a cycle exists.

def isCyclic(V: int, adj: List[List[int]]) -> bool:
    vis = [0] * V
    pathVis = [0] * V
    def dfsCheck(node):
        vis[node] = 1
        pathVis[node] = 1
        for neighbor in adj[node]:
            if not vis[neighbor]:
                if dfsCheck(neighbor): return True
            elif pathVis[neighbor]:
                return True
        pathVis[node] = 0
        return False
    for i in range(V):
        if not vis[i]:
            if dfsCheck(i): return True
    return False

