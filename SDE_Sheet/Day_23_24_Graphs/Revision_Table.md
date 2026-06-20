# Day 23 24 Graphs Revision Table

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
      <td>Graph 01 Number Of Islands<br><br></b> <a href="https://leetcode.com/problems/number-of-islands/" target="_blank">LeetCode 200</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, SDE Sheet, Love Babbar</details></td>
      <td><b>Example 1:</b> <br><b>Input:</b> grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]<br><b>Output:</b> 3</td>
      <td><b>Time:</b> O(M * N) (Constraint)<br><b>Space:</b> O(M * N) (Constraint)</td>
      <td><b>Explanation:</b> Iterate through the grid. When a '1' is found, increment island count and use DFS to sink the island (turn connected '1's to '0's).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def num_islands(grid: list[list[str]]) -&gt; int:&#10;    if not grid: return 0&#10;    def dfs(i, j):&#10;        if i &lt; 0 or i &gt;= len(grid) or j &lt; 0 or j &gt;= len(grid[0]) or grid[i][j] == &#x27;0&#x27;:&#10;            return&#10;        grid[i][j] = &#x27;0&#x27;&#10;        dfs(i+1, j); dfs(i-1, j); dfs(i, j+1); dfs(i, j-1)&#10;    count = 0&#10;    for i in range(len(grid)):&#10;        for j in range(len(grid[0])):&#10;            if grid[i][j] == &#x27;1&#x27;:&#10;                count += 1&#10;                dfs(i, j)&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td>2</td>
      <td>Graph 02 Course Schedule<br><br></b> <a href="https://leetcode.com/problems/course-schedule/" target="_blank">LeetCode 207</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, SDE Sheet, Love Babbar</details></td>
      <td><b>Example 1:</b> <br><b>Input:</b> numCourses = 2, prerequisites = [[1,0]]<br><b>Output:</b> true</td>
      <td><b>Time:</b> O(V + E) (Constraint)<br><b>Space:</b> O(V + E)</td>
      <td><b>Explanation:</b> Kahn's Algorithm (BFS). Count in-degrees. Add courses with 0 in-degree to queue. Process queue, reducing in-degrees of neighbors.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">from collections import deque&#10;def can_finish(numCourses: int, prerequisites: list[list[int]]) -&gt; bool:&#10;    adj = {i: [] for i in range(numCourses)}&#10;    indegree = [0] * numCourses&#10;    for crs, pre in prerequisites:&#10;        adj[pre].append(crs)&#10;        indegree[crs] += 1&#10;    q = deque([i for i in range(numCourses) if indegree[i] == 0])&#10;    count = 0&#10;    while q:&#10;        node = q.popleft()&#10;        count += 1&#10;        for neighbor in adj[node]:&#10;            indegree[neighbor] -= 1&#10;            if indegree[neighbor] == 0:&#10;                q.append(neighbor)&#10;    return count == numCourses</code></pre></details></td>
    </tr>
    <tr>
      <td>3</td>
      <td>Graph 03 Bipartite Graph<br><br></b> <a href="https://leetcode.com/problems/is-graph-bipartite/" target="_blank">LeetCode 785</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, Love Babbar, SDE Sheet</details></td>
      <td><b>Example 1:</b> <br><b>Input:</b> graph = [[1,2,3],[0,2],[0,1,3],[0,2]]<br><b>Output:</b> false</td>
      <td><b>Time:</b> O(V + E)<br><b>Space:</b> O(V)</td>
      <td><b>Explanation:</b> BFS/DFS coloring approach. Color adjacent nodes with alternate colors (0 and 1). If an adjacent node has the SAME color, it's not bipartite.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">from collections import deque&#10;def isBipartite(graph: list[list[int]]) -&gt; bool:&#10;    n = len(graph)&#10;    color = [-1] * n&#10;    for i in range(n):&#10;        if color[i] != -1: continue&#10;        q = deque([i])&#10;        color[i] = 0&#10;        while q:&#10;            node = q.popleft()&#10;            for neighbor in graph[node]:&#10;                if color[neighbor] == -1:&#10;                    color[neighbor] = 1 - color[node]&#10;                    q.append(neighbor)&#10;                elif color[neighbor] == color[node]:&#10;                    return False&#10;    return True</code></pre></details></td>
    </tr>
    <tr>
      <td>4</td>
      <td>Graph 04 Dijkstras Algorithm<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, SDE Sheet, Love Babbar</details></td>
      <td><b>Example 1:</b> Source = 0<br><b>Output:</b> distances array.</td>
      <td><b>Time:</b> O(E log V)<br><b>Space:</b> O(V)</td>
      <td><b>Explanation:</b> Min-heap (priority queue) to repeatedly extract the node with the minimum distance and relax its neighbors.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def dijkstra(V: int, adj: List[List[List[int]]], S: int) -&gt; List[int]:&#10;    import heapq&#10;    dist = [float(&#x27;inf&#x27;)] * V&#10;    dist[S] = 0&#10;    pq = [(0, S)]&#10;    while pq:&#10;        d, node = heapq.heappop(pq)&#10;        if d &gt; dist[node]: continue&#10;        for nxt, weight in adj[node]:&#10;            if d + weight &lt; dist[nxt]:&#10;                dist[nxt] = d + weight&#10;                heapq.heappush(pq, (dist[nxt], nxt))&#10;    return dist</code></pre></details></td>
    </tr>
    <tr>
      <td>5</td>
      <td>Graph 05 Topological Sort<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/topological-sort/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, SDE Sheet, Love Babbar</details></td>
      <td><b>Example 1:</b> <br><b>Input:</b> V = 4, adj = [[], [0], [0], [0]]<br><b>Output:</b> valid topological sort.</td>
      <td><b>Time:</b> O(V + E)<br><b>Space:</b> O(V)</td>
      <td><b>Explanation:</b> Kahn's Algorithm (BFS) using in-degrees. Add nodes with 0 in-degree to a queue. Pop, append to result, and decrement in-degrees of neighbors.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def topoSort(V: int, adj: List[List[int]]) -&gt; List[int]:&#10;    from collections import deque&#10;    indegree = [0] * V&#10;    for i in range(V):&#10;        for nxt in adj[i]: indegree[nxt] += 1&#10;    q = deque([i for i in range(V) if indegree[i] == 0])&#10;    topo = []&#10;    while q:&#10;        node = q.popleft()&#10;        topo.append(node)&#10;        for nxt in adj[node]:&#10;            indegree[nxt] -= 1&#10;            if indegree[nxt] == 0: q.append(nxt)&#10;    return topo</code></pre></details></td>
    </tr>
    <tr>
      <td>6</td>
      <td>Graph 06 Bellman Ford<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/0" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, SDE Sheet, Apna College, Love Babbar</details></td>
      <td><b>Example 1:</b> <br><b>Input:</b> V=3, S=0, Edges=[[0,1,5],[1,2,-2],[2,1,-3]]<br><b>Output:</b> [-1]</td>
      <td><b>Time:</b> O(V * E)<br><b>Space:</b> O(V)</td>
      <td><b>Explanation:</b> Relax all edges V-1 times. To detect a negative cycle, relax one more time; if any distance updates, there's a negative cycle.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def bellman_ford(V: int, edges: List[List[int]], S: int) -&gt; List[int]:&#10;    dist = [int(1e8)] * V&#10;    dist[S] = 0&#10;    for _ in range(V - 1):&#10;        for u, v, wt in edges:&#10;            if dist[u] != int(1e8) and dist[u] + wt &lt; dist[v]:&#10;                dist[v] = dist[u] + wt&#10;    for u, v, wt in edges:&#10;        if dist[u] != int(1e8) and dist[u] + wt &lt; dist[v]:&#10;            return [-1]&#10;    return dist</code></pre></details></td>
    </tr>
    <tr>
      <td>7</td>
      <td>Graph 07 Floyd Warshall<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, SDE Sheet, Apna College, Love Babbar</details></td>
      <td><b>Example 1:</b><br><b>Output:</b> Shortest paths for all pairs (i, j).</td>
      <td><b>Time:</b> O(V^3)<br><b>Space:</b> O(1) in-place</td>
      <td><b>Explanation:</b> Multi-source shortest path. Try to go from i to j via every possible vertex k. Update `matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def shortest_distance(matrix: List[List[int]]) -&gt; None:&#10;    n = len(matrix)&#10;    for i in range(n):&#10;        for j in range(n):&#10;            if matrix[i][j] == -1: matrix[i][j] = int(1e9)&#10;            if i == j: matrix[i][j] = 0&#10;    for k in range(n):&#10;        for i in range(n):&#10;            for j in range(n):&#10;                if matrix[i][k] != int(1e9) and matrix[k][j] != int(1e9):&#10;                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])&#10;    for i in range(n):&#10;        for j in range(n):&#10;            if matrix[i][j] == int(1e9): matrix[i][j] = -1</code></pre></details></td>
    </tr>
    <tr>
      <td>8</td>
      <td>Graph 08 Mst Prims<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/minimum-spanning-tree/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, SDE Sheet, Apna College, Love Babbar</details></td>
      <td><b>Example 1:</b> Return the scalar sum of the MST.</td>
      <td><b>Time:</b> O(E log V)<br><b>Space:</b> O(E + V)</td>
      <td><b>Explanation:</b> Prim's Algorithm. Use a Min-Heap `(weight, node)`. Always pick the smallest available edge connecting the MST to an unvisited node.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def spanningTree(V: int, adj: List[List[List[int]]]) -&gt; int:&#10;    pq = [(0, 0)]&#10;    vis = [0] * V&#10;    sum_val = 0&#10;    while pq:&#10;        wt, node = heapq.heappop(pq)&#10;        if vis[node] == 1: continue&#10;        vis[node] = 1&#10;        sum_val += wt&#10;        for adjNode, edW in adj[node]:&#10;            if not vis[adjNode]: heapq.heappush(pq, (edW, adjNode))&#10;    return sum_val</code></pre></details></td>
    </tr>
    <tr>
      <td>9</td>
      <td>Graph 09 Strongly Connected Components Kosaraju<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/strongly-connected-components-kosarajus-algo/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, SDE Sheet, Apna College, Love Babbar</details></td>
      <td><b>Example 1:</b> Return an integer count.</td>
      <td><b>Time:</b> O(V + E)<br><b>Space:</b> O(V + E)</td>
      <td><b>Explanation:</b> Kosaraju's Algo: 1) Sort nodes by finish time (Topo Sort DFS). 2) Transpose the graph (reverse edges). 3) DFS on transposed graph in order of finish time.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def kosaraju(V: int, adj: List[List[int]]) -&gt; int:&#10;    vis = [0] * V&#10;    st = []&#10;    def dfs(node):&#10;        vis[node] = 1&#10;        for it in adj[node]:&#10;            if not vis[it]: dfs(it)&#10;        st.append(node)&#10;    for i in range(V):&#10;        if not vis[i]: dfs(i)&#10;    adjT = [[] for _ in range(V)]&#10;    for i in range(V):&#10;        vis[i] = 0&#10;        for it in adj[i]: adjT[it].append(i)&#10;    def dfs3(node):&#10;        vis[node] = 1&#10;        for it in adjT[node]:&#10;            if not vis[it]: dfs3(it)&#10;    scc = 0&#10;    while st:&#10;        node = st.pop()&#10;        if not vis[node]:&#10;            scc += 1; dfs3(node)&#10;    return scc</code></pre></details></td>
    </tr>
    <tr>
      <td>10</td>
      <td>Graph 10 Bipartite Graph DFS<br><br></b> <a href="https://practice.geeksforgeeks.org/problems/bipartite-graph/1" target="_blank">GFG</a><br><br><details><summary>ℹ️</summary><b>Tags:</b> Striver A Z, SDE Sheet, Love Babbar</details></td>
      <td><b>Example 1:</b> Return true/false.</td>
      <td><b>Time:</b> O(V + E)<br><b>Space:</b> O(V)</td>
      <td><b>Explanation:</b> DFS. Color nodes with 0 and 1. If an adjacent node is uncolored, assign the opposite color and recurse. If it's colored and has the same color, it's not bipartite.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isBipartite(V: int, adj: List[List[int]]) -&gt; bool:&#10;    color = [-1] * V&#10;    def dfs(node, col):&#10;        color[node] = col&#10;        for it in adj[node]:&#10;            if color[it] == -1:&#10;                if not dfs(it, 1 - col): return False&#10;            elif color[it] == col:&#10;                return False&#10;        return True&#10;    for i in range(V):&#10;        if color[i] == -1:&#10;            if not dfs(i, 0): return False&#10;    return True</code></pre></details></td>
    </tr>
  </tbody>
</table>
