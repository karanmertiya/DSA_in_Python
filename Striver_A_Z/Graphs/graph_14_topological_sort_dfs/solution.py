# Time Complexity: O(V + E)
# Space Complexity: O(V)
# Explanation: Use DFS. Maintain a visited array. Once all adjacent nodes of a vertex are visited, push the vertex to a stack. Print the stack for the topological order.

def topoSort(V: int, adj: List[List[int]]) -> List[int]:
    vis = [0] * V
    st = []
    def dfs(node):
        vis[node] = 1
        for it in adj[node]:
            if not vis[it]: dfs(it)
        st.append(node)
    for i in range(V):
        if not vis[i]: dfs(i)
    return st[::-1]

