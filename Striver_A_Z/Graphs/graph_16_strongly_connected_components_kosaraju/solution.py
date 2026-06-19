# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
# Explanation: 1. Perform DFS and push nodes to stack upon finish (topological sort order). 2. Reverse all edges of the graph. 3. Pop nodes from stack and perform DFS on the reversed graph. Each DFS call gives one Strongly Connected Component.

def kosaraju(V, adj):
    vis = [False] * V
    st = []
    def dfs1(node):
        vis[node] = True
        for nbr in adj[node]:
            if not vis[nbr]: dfs1(nbr)
        st.append(node)
    for i in range(V):
        if not vis[i]: dfs1(i)
    revAdj = [[] for _ in range(V)]
    for i in range(V):
        vis[i] = False
        for nbr in adj[i]: revAdj[nbr].append(i)
    def dfs2(node):
        vis[node] = True
        for nbr in revAdj[node]:
            if not vis[nbr]: dfs2(nbr)
    scc = 0
    while st:
        node = st.pop()
        if not vis[node]:
            dfs2(node)
            scc += 1
    return scc

