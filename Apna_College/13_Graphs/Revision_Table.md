# 13 Graphs Revision Table

<table border="1">
  <thead>
    <tr>
      <th style="width: 5%;">S.No</th>
      <th style="width: 15%;">Problem Name</th>
      <th style="width: 30%;">Example & Constraints</th>
      <th style="width: 15%;">Complexity</th>
      <th style="width: 35%;">Logic</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Graph 01 Bellman Ford<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/0" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> SDE Sheet, Apna College, Love Babbar, Striver A Z</details></td>
      <td>**Example 1:** Input: V=3, S=0, Edges=[[0,1,5],[1,2,-2],[2,1,-3]], Output: [-1]</td>
      <td><b>Time:</b> O(V * E)<br><b>Space:</b> O(V)</td>
      <td><b>Explanation:</b> Relax all edges V-1 times. To detect a negative cycle, relax one more time; if any distance updates, there's a negative cycle.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def bellman_ford(V: int, edges: List[List[int]], S: int) -&gt; List[int]:&#10;    dist = [int(1e8)] * V&#10;    dist[S] = 0&#10;    for _ in range(V - 1):&#10;        for u, v, wt in edges:&#10;            if dist[u] != int(1e8) and dist[u] + wt &lt; dist[v]:&#10;                dist[v] = dist[u] + wt&#10;    for u, v, wt in edges:&#10;        if dist[u] != int(1e8) and dist[u] + wt &lt; dist[v]:&#10;            return [-1]&#10;    return dist</code></pre></details></td>
    </tr>
    <tr>
      <td>2</td>
      <td>Graph 02 Floyd Warshall<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> SDE Sheet, Apna College, Love Babbar, Striver A Z</details></td>
      <td>**Example 1:** Output: Shortest paths for all pairs (i, j).</td>
      <td><b>Time:</b> O(V^3)<br><b>Space:</b> O(1) in-place</td>
      <td><b>Explanation:</b> Multi-source shortest path. Try to go from i to j via every possible vertex k. Update `matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def shortest_distance(matrix: List[List[int]]) -&gt; None:&#10;    n = len(matrix)&#10;    for i in range(n):&#10;        for j in range(n):&#10;            if matrix[i][j] == -1: matrix[i][j] = int(1e9)&#10;            if i == j: matrix[i][j] = 0&#10;    for k in range(n):&#10;        for i in range(n):&#10;            for j in range(n):&#10;                if matrix[i][k] != int(1e9) and matrix[k][j] != int(1e9):&#10;                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])&#10;    for i in range(n):&#10;        for j in range(n):&#10;            if matrix[i][j] == int(1e9): matrix[i][j] = -1</code></pre></details></td>
    </tr>
    <tr>
      <td>3</td>
      <td>Graph 03 Mst Prims<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/minimum-spanning-tree/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, SDE Sheet, Love Babbar, Apna College</details></td>
      <td>**Example 1:** Return the scalar sum of the MST.</td>
      <td><b>Time:</b> O(E log V)<br><b>Space:</b> O(E + V)</td>
      <td><b>Explanation:</b> Prim's Algorithm. Use a Min-Heap `(weight, node)`. Always pick the smallest available edge connecting the MST to an unvisited node.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def spanningTree(V: int, adj: List[List[List[int]]]) -&gt; int:&#10;    pq = [(0, 0)]&#10;    vis = [0] * V&#10;    sum_val = 0&#10;    while pq:&#10;        wt, node = heapq.heappop(pq)&#10;        if vis[node] == 1: continue&#10;        vis[node] = 1&#10;        sum_val += wt&#10;        for adjNode, edW in adj[node]:&#10;            if not vis[adjNode]: heapq.heappush(pq, (edW, adjNode))&#10;    return sum_val</code></pre></details></td>
    </tr>
    <tr>
      <td>4</td>
      <td>Graph 04 Strongly Connected Components Kosaraju<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/strongly-connected-components-kosarajus-algo/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, SDE Sheet, Love Babbar, Apna College</details></td>
      <td>**Example 1:** Return an integer count.</td>
      <td><b>Time:</b> O(V + E)<br><b>Space:</b> O(V + E)</td>
      <td><b>Explanation:</b> Kosaraju's Algo: 1) Sort nodes by finish time (Topo Sort DFS). 2) Transpose the graph (reverse edges). 3) DFS on transposed graph in order of finish time.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def kosaraju(V: int, adj: List[List[int]]) -&gt; int:&#10;    vis = [0] * V&#10;    st = []&#10;    def dfs(node):&#10;        vis[node] = 1&#10;        for it in adj[node]:&#10;            if not vis[it]: dfs(it)&#10;        st.append(node)&#10;    for i in range(V):&#10;        if not vis[i]: dfs(i)&#10;    adjT = [[] for _ in range(V)]&#10;    for i in range(V):&#10;        vis[i] = 0&#10;        for it in adj[i]: adjT[it].append(i)&#10;    def dfs3(node):&#10;        vis[node] = 1&#10;        for it in adjT[node]:&#10;            if not vis[it]: dfs3(it)&#10;    scc = 0&#10;    while st:&#10;        node = st.pop()&#10;        if not vis[node]:&#10;            scc += 1; dfs3(node)&#10;    return scc</code></pre></details></td>
    </tr>
  </tbody>
</table>
