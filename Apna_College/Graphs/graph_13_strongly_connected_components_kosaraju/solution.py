# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
# Explanation: Kosaraju's Algo: 1) Sort nodes by finish time (Topo Sort DFS). 2) Transpose the graph (reverse edges). 3) DFS on transposed graph in order of finish time.

def kosaraju(V: int, adj: List[List[int]]) -> int:
    vis = [0] * V
    st = []
    def dfs(node):
        vis[node] = 1
        for it in adj[node]:
            if not vis[it]: dfs(it)
        st.append(node)
    for i in range(V):
        if not vis[i]: dfs(i)
    adjT = [[] for _ in range(V)]
    for i in range(V):
        vis[i] = 0
        for it in adj[i]: adjT[it].append(i)
    def dfs3(node):
        vis[node] = 1
        for it in adjT[node]:
            if not vis[it]: dfs3(it)
    scc = 0
    while st:
        node = st.pop()
        if not vis[node]:
            scc += 1; dfs3(node)
    return scc

