# Time Complexity: O(V + E)
# Space Complexity: O(V)
# Explanation: Use standard DFS. When returning from the DFS call of a node (meaning all its descendants are visited), push the node to a stack. The stack will contain the topological sort.

def topoSort(V: int, adj: List[List[int]]) -> List[int]:
    vis = [0] * V
    st = []
    def dfs(node):
        vis[node] = 1
        for neighbor in adj[node]:
            if not vis[neighbor]:
                dfs(neighbor)
        st.append(node)
    for i in range(V):
        if not vis[i]:
            dfs(i)
    return st[::-1]

