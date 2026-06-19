# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
# Explanation: Kosaraju's Algorithm. 1. Topo sort the graph to get finish times (push to stack on completion). 2. Reverse all edges. 3. Pop from stack and run DFS on the reversed graph. Each successful DFS from stack gives one SCC.

def kosaraju(V: int, adj: List[List[int]]) -> int:
    vis = [0] * V
    st = []
    def dfs(node):
        vis[node] = 1
        for neighbor in adj[node]:
            if not vis[neighbor]: dfs(neighbor)
        st.append(node)
    for i in range(V):
        if not vis[i]: dfs(i)
    adjT = [[] for _ in range(V)]
    for i in range(V):
        vis[i] = 0
        for neighbor in adj[i]:
            adjT[neighbor].append(i)
    def dfs2(node):
        vis[node] = 1
        for neighbor in adjT[node]:
            if not vis[neighbor]: dfs2(neighbor)
    scc = 0
    while st:
        node = st.pop()
        if not vis[node]:
            scc += 1
            dfs2(node)
    return scc

