# Graphs Revision Table

<table border="1">
  <thead>
    <tr>
      <th rowspan="2" style="width: 5%;">S.No</th>
      <th rowspan="2" style="width: 15%;">Problem Name</th>
      <th rowspan="2" style="width: 25%;">Example & Constraints</th>
      <th rowspan="2" style="width: 10%;">Complexity</th>
      <th colspan="2" style="width: 20%;">Conditions & Edge Cases</th>
      <th rowspan="2" style="width: 25%;">Logic</th>
    </tr>
    <tr>
      <th>Dependencies / Setup</th>
      <th>Edge Case Handling</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Graph 01 Number Of Islands<br><br></b> <a href='https://leetcode.com/problems/number-of-islands/' target='_blank'>LeetCode 200</a></td>
      <td><b>Example 1:</b> Input: grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]], Output: 3</td>
      <td><b>Time:</b> O(M * N) (Constraint)<br><b>Space:</b> O(M * N) (Constraint)</td>
      <td>-</td>
      <td><b>In-place Visited Check:</b> Sinking the island by changing '1' to '0' avoids needing a separate `visited` matrix.</td>
      <td><b>Explanation:</b> Iterate through the grid. When a '1' is found, increment island count and use DFS to sink the island (turn connected '1's to '0's).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def num_islands(grid: list[list[str]]) -&gt; int:&#10;    if not grid: return 0&#10;    def dfs(i, j):&#10;        if i &lt; 0 or i &gt;= len(grid) or j &lt; 0 or j &gt;= len(grid[0]) or grid[i][j] == &#x27;0&#x27;:&#10;            return&#10;        grid[i][j] = &#x27;0&#x27;&#10;        dfs(i+1, j); dfs(i-1, j); dfs(i, j+1); dfs(i, j-1)&#10;    count = 0&#10;    for i in range(len(grid)):&#10;        for j in range(len(grid[0])):&#10;            if grid[i][j] == &#x27;1&#x27;:&#10;                count += 1&#10;                dfs(i, j)&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td>2</td>
      <td>Graph 02 Course Schedule<br><br></b> <a href='https://leetcode.com/problems/course-schedule/' target='_blank'>LeetCode 207</a></td>
      <td><b>Example 1:</b> Input: numCourses = 2, prerequisites = [[1,0]], Output: true</td>
      <td><b>Time:</b> O(V + E) (Constraint)<br><b>Space:</b> O(V + E)</td>
      <td><code>std::queue</code></td>
      <td><b>Graph Building:</b> Convert `prerequisites` edge list into an Adjacency List for fast neighbor lookups.</td>
      <td><b>Explanation:</b> Kahn's Algorithm (BFS). Count in-degrees. Add courses with 0 in-degree to queue. Process queue, reducing in-degrees of neighbors.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">from collections import deque&#10;def can_finish(numCourses: int, prerequisites: list[list[int]]) -&gt; bool:&#10;    adj = {i: [] for i in range(numCourses)}&#10;    indegree = [0] * numCourses&#10;    for crs, pre in prerequisites:&#10;        adj[pre].append(crs)&#10;        indegree[crs] += 1&#10;    q = deque([i for i in range(numCourses) if indegree[i] == 0])&#10;    count = 0&#10;    while q:&#10;        node = q.popleft()&#10;        count += 1&#10;        for neighbor in adj[node]:&#10;            indegree[neighbor] -= 1&#10;            if indegree[neighbor] == 0:&#10;                q.append(neighbor)&#10;    return count == numCourses</code></pre></details></td>
    </tr>
    <tr>
      <td>3</td>
      <td>Graph 03 Rotting Oranges<br><br></b> <a href='https://leetcode.com/problems/rotting-oranges/' target='_blank'>LeetCode 994</a></td>
      <td><b>Example 1:</b> Input: grid = [[2,1,1],[1,1,0],[0,1,1]], Output: 4</td>
      <td><b>Time:</b> O(M * N)<br><b>Space:</b> O(M * N)</td>
      <td><code>std::queue</code></td>
      <td><b>Unreachable Oranges:</b> Track total fresh oranges initially. If remaining fresh > 0 after BFS, return -1.</td>
      <td><b>Explanation:</b> Multi-source BFS. Put all initially rotten oranges in queue. Process level by level.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">from collections import deque&#10;def orangesRotting(grid: list[list[int]]) -&gt; int:&#10;    q = deque()&#10;    fresh = 0&#10;    for i in range(len(grid)):&#10;        for j in range(len(grid[0])):&#10;            if grid[i][j] == 2: q.append((i, j))&#10;            elif grid[i][j] == 1: fresh += 1&#10;    time = 0&#10;    dirs = [(1,0), (-1,0), (0,1), (0,-1)]&#10;    while q and fresh &gt; 0:&#10;        for _ in range(len(q)):&#10;            r, c = q.popleft()&#10;            for dr, dc in dirs:&#10;                nr, nc = r + dr, c + dc&#10;                if 0 &lt;= nr &lt; len(grid) and 0 &lt;= nc &lt; len(grid[0]) and grid[nr][nc] == 1:&#10;                    grid[nr][nc] = 2&#10;                    q.append((nr, nc))&#10;                    fresh -= 1&#10;        time += 1&#10;    return time if fresh == 0 else -1</code></pre></details></td>
    </tr>
    <tr>
      <td>4</td>
      <td>Graph 04 Bipartite Graph<br><br></b> <a href='https://leetcode.com/problems/is-graph-bipartite/' target='_blank'>LeetCode 785</a></td>
      <td><b>Example 1:</b> Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]], Output: false</td>
      <td><b>Time:</b> O(V + E)<br><b>Space:</b> O(V)</td>
      <td><code>std::queue</code></td>
      <td><b>Disconnected Graph:</b> Must loop over all nodes `0` to `V-1` to ensure every disconnected component is checked.</td>
      <td><b>Explanation:</b> BFS/DFS coloring approach. Color adjacent nodes with alternate colors (0 and 1). If an adjacent node has the SAME color, it's not bipartite.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">from collections import deque&#10;def isBipartite(graph: list[list[int]]) -&gt; bool:&#10;    n = len(graph)&#10;    color = [-1] * n&#10;    for i in range(n):&#10;        if color[i] != -1: continue&#10;        q = deque([i])&#10;        color[i] = 0&#10;        while q:&#10;            node = q.popleft()&#10;            for neighbor in graph[node]:&#10;                if color[neighbor] == -1:&#10;                    color[neighbor] = 1 - color[node]&#10;                    q.append(neighbor)&#10;                elif color[neighbor] == color[node]:&#10;                    return False&#10;    return True</code></pre></details></td>
    </tr>
    <tr>
      <td>5</td>
      <td>Graph 06 Dijkstras Algorithm<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Source = 0, Output: distances array.</td>
      <td><b>Time:</b> O(E log V)<br><b>Space:</b> O(V)</td>
      <td><code>#include &lt;queue&gt;</code></td>
      <td><b>Disconnected graph:</b> Distances remain infinity.</td>
      <td><b>Explanation:</b> Min-heap (priority queue) to repeatedly extract the node with the minimum distance and relax its neighbors.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def dijkstra(V: int, adj: List[List[List[int]]], S: int) -&gt; List[int]:&#10;    import heapq&#10;    dist = [float(&#x27;inf&#x27;)] * V&#10;    dist[S] = 0&#10;    pq = [(0, S)]&#10;    while pq:&#10;        d, node = heapq.heappop(pq)&#10;        if d &gt; dist[node]: continue&#10;        for nxt, weight in adj[node]:&#10;            if d + weight &lt; dist[nxt]:&#10;                dist[nxt] = d + weight&#10;                heapq.heappush(pq, (dist[nxt], nxt))&#10;    return dist</code></pre></details></td>
    </tr>
    <tr>
      <td>6</td>
      <td>Graph 07 Topological Sort<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/topological-sort/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Input: V = 4, adj = [[], [0], [0], [0]], Output: valid topological sort.</td>
      <td><b>Time:</b> O(V + E)<br><b>Space:</b> O(V)</td>
      <td><code>#include &lt;queue&gt;</code></td>
      <td><b>Cycles:</b> If cycle exists, result will not contain all V elements.</td>
      <td><b>Explanation:</b> Kahn's Algorithm (BFS) using in-degrees. Add nodes with 0 in-degree to a queue. Pop, append to result, and decrement in-degrees of neighbors.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def topoSort(V: int, adj: List[List[int]]) -&gt; List[int]:&#10;    from collections import deque&#10;    indegree = [0] * V&#10;    for i in range(V):&#10;        for nxt in adj[i]: indegree[nxt] += 1&#10;    q = deque([i for i in range(V) if indegree[i] == 0])&#10;    topo = []&#10;    while q:&#10;        node = q.popleft()&#10;        topo.append(node)&#10;        for nxt in adj[node]:&#10;            indegree[nxt] -= 1&#10;            if indegree[nxt] == 0: q.append(nxt)&#10;    return topo</code></pre></details></td>
    </tr>
    <tr>
      <td>7</td>
      <td>Graph 08 Number Of Islands<br><br></b> <a href='https://leetcode.com/problems/number-of-islands/' target='_blank'>LeetCode 200</a></td>
      <td><b>Example 1:</b> Input: grid=[['1','1','0','0','0'],...], Output: 1</td>
      <td><b>Time:</b> O(N * M)<br><b>Space:</b> O(N * M) auxiliary</td>
      <td>-</td>
      <td><b>Empty Grid:</b> Returns 0.</td>
      <td><b>Explanation:</b> Traverse grid. Whenever a '1' is found, increment counter and trigger BFS/DFS to sink the island (mark '0').<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def numIslands(grid: List[List[str]]) -&gt; int:&#10;    if not grid: return 0&#10;    def dfs(r, c):&#10;        if r&lt;0 or c&lt;0 or r&gt;=len(grid) or c&gt;=len(grid[0]) or grid[r][c] == &#x27;0&#x27;: return&#10;        grid[r][c] = &#x27;0&#x27;&#10;        dfs(r+1,c); dfs(r-1,c); dfs(r,c+1); dfs(r,c-1)&#10;    count = 0&#10;    for i in range(len(grid)):&#10;        for j in range(len(grid[0])):&#10;            if grid[i][j] == &#x27;1&#x27;:&#10;                count += 1&#10;                dfs(i, j)&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td>8</td>
      <td>Graph 09 Course Schedule<br><br></b> <a href='https://leetcode.com/problems/course-schedule/' target='_blank'>LeetCode 207</a></td>
      <td><b>Example 1:</b> Input: numCourses = 2, prerequisites = [[1,0]], Output: true</td>
      <td><b>Time:</b> O(V + E)<br><b>Space:</b> O(V + E)</td>
      <td>-</td>
      <td><b>Multiple components:</b> Still works because we enqueue all 0-indegree nodes.</td>
      <td><b>Explanation:</b> Kahn's BFS or DFS cycle detection. Here Kahn's BFS is used. If topological sort contains all V vertices, then true.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def canFinish(numCourses: int, prerequisites: List[List[int]]) -&gt; bool:&#10;    from collections import deque&#10;    adj = [[] for _ in range(numCourses)]&#10;    indegree = [0]*numCourses&#10;    for dest, src in prerequisites:&#10;        adj[src].append(dest)&#10;        indegree[dest] += 1&#10;    q = deque([i for i in range(numCourses) if indegree[i] == 0])&#10;    count = 0&#10;    while q:&#10;        node = q.popleft()&#10;        count += 1&#10;        for nxt in adj[node]:&#10;            indegree[nxt] -= 1&#10;            if indegree[nxt] == 0: q.append(nxt)&#10;    return count == numCourses</code></pre></details></td>
    </tr>
    <tr>
      <td>9</td>
      <td>Graph 10 Bellman Ford<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/0' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Input: V=3, S=0, Edges=[[0,1,5],[1,2,-2],[2,1,-3]], Output: [-1]</td>
      <td><b>Time:</b> O(V * E)<br><b>Space:</b> O(V)</td>
      <td>-</td>
      <td><b>Disconnected Graphs:</b> Elements unreachable from source remain at 1e8.</td>
      <td><b>Explanation:</b> Relax all edges V-1 times. To detect a negative cycle, relax one more time; if any distance updates, there's a negative cycle.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def bellman_ford(V: int, edges: List[List[int]], S: int) -&gt; List[int]:&#10;    dist = [int(1e8)] * V&#10;    dist[S] = 0&#10;    for _ in range(V - 1):&#10;        for u, v, wt in edges:&#10;            if dist[u] != int(1e8) and dist[u] + wt &lt; dist[v]:&#10;                dist[v] = dist[u] + wt&#10;    for u, v, wt in edges:&#10;        if dist[u] != int(1e8) and dist[u] + wt &lt; dist[v]:&#10;            return [-1]&#10;    return dist</code></pre></details></td>
    </tr>
    <tr>
      <td>10</td>
      <td>Graph 11 Floyd Warshall<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Output: Shortest paths for all pairs (i, j).</td>
      <td><b>Time:</b> O(V^3)<br><b>Space:</b> O(1) in-place</td>
      <td>-</td>
      <td><b>Unreachable nodes:</b> Represented by -1. Replace with 1e9 before algorithm, then back to -1.</td>
      <td><b>Explanation:</b> Multi-source shortest path. Try to go from i to j via every possible vertex k. Update `matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def shortest_distance(matrix: List[List[int]]) -&gt; None:&#10;    n = len(matrix)&#10;    for i in range(n):&#10;        for j in range(n):&#10;            if matrix[i][j] == -1: matrix[i][j] = int(1e9)&#10;            if i == j: matrix[i][j] = 0&#10;    for k in range(n):&#10;        for i in range(n):&#10;            for j in range(n):&#10;                if matrix[i][k] != int(1e9) and matrix[k][j] != int(1e9):&#10;                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])&#10;    for i in range(n):&#10;        for j in range(n):&#10;            if matrix[i][j] == int(1e9): matrix[i][j] = -1</code></pre></details></td>
    </tr>
    <tr>
      <td>11</td>
      <td>Graph 12 Mst Prims<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/minimum-spanning-tree/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Return the scalar sum of the MST.</td>
      <td><b>Time:</b> O(E log V)<br><b>Space:</b> O(E + V)</td>
      <td><code>#include <queue></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Prim's Algorithm. Use a Min-Heap `(weight, node)`. Always pick the smallest available edge connecting the MST to an unvisited node.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def spanningTree(V: int, adj: List[List[List[int]]]) -&gt; int:&#10;    pq = [(0, 0)]&#10;    vis = [0] * V&#10;    sum_val = 0&#10;    while pq:&#10;        wt, node = heapq.heappop(pq)&#10;        if vis[node] == 1: continue&#10;        vis[node] = 1&#10;        sum_val += wt&#10;        for adjNode, edW in adj[node]:&#10;            if not vis[adjNode]: heapq.heappush(pq, (edW, adjNode))&#10;    return sum_val</code></pre></details></td>
    </tr>
    <tr>
      <td>12</td>
      <td>Graph 13 Strongly Connected Components Kosaraju<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/strongly-connected-components-kosarajus-algo/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Return an integer count.</td>
      <td><b>Time:</b> O(V + E)<br><b>Space:</b> O(V + E)</td>
      <td><code>#include <stack></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Kosaraju's Algo: 1) Sort nodes by finish time (Topo Sort DFS). 2) Transpose the graph (reverse edges). 3) DFS on transposed graph in order of finish time.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def kosaraju(V: int, adj: List[List[int]]) -&gt; int:&#10;    vis = [0] * V&#10;    st = []&#10;    def dfs(node):&#10;        vis[node] = 1&#10;        for it in adj[node]:&#10;            if not vis[it]: dfs(it)&#10;        st.append(node)&#10;    for i in range(V):&#10;        if not vis[i]: dfs(i)&#10;    adjT = [[] for _ in range(V)]&#10;    for i in range(V):&#10;        vis[i] = 0&#10;        for it in adj[i]: adjT[it].append(i)&#10;    def dfs3(node):&#10;        vis[node] = 1&#10;        for it in adjT[node]:&#10;            if not vis[it]: dfs3(it)&#10;    scc = 0&#10;    while st:&#10;        node = st.pop()&#10;        if not vis[node]:&#10;            scc += 1; dfs3(node)&#10;    return scc</code></pre></details></td>
    </tr>
    <tr>
      <td>13</td>
      <td>Graph 14 Topological Sort Dfs<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/topological-sort/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Return array.</td>
      <td><b>Time:</b> O(V + E)<br><b>Space:</b> O(V)</td>
      <td><code>#include <stack></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Use DFS. Maintain a visited array. Once all adjacent nodes of a vertex are visited, push the vertex to a stack. Print the stack for the topological order.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def topoSort(V: int, adj: List[List[int]]) -&gt; List[int]:&#10;    vis = [0] * V&#10;    st = []&#10;    def dfs(node):&#10;        vis[node] = 1&#10;        for it in adj[node]:&#10;            if not vis[it]: dfs(it)&#10;        st.append(node)&#10;    for i in range(V):&#10;        if not vis[i]: dfs(i)&#10;    return st[::-1]</code></pre></details></td>
    </tr>
    <tr>
      <td>14</td>
      <td>Graph 15 Kahn Algorithm Bfs<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/topological-sort/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Kahn's.</td>
      <td><b>Time:</b> O(V + E)<br><b>Space:</b> O(V)</td>
      <td><code>#include <queue></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Compute in-degrees for all nodes. Push nodes with 0 in-degree to a queue. Pop, add to answer, and reduce in-degrees of neighbors. If a neighbor reaches 0, push it.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def topoSort(V: int, adj: List[List[int]]) -&gt; List[int]:&#10;    indegree = [0] * V&#10;    for i in range(V):&#10;        for it in adj[i]: indegree[it] += 1&#10;    q = [i for i in range(V) if indegree[i] == 0]&#10;    topo = []&#10;    while q:&#10;        node = q.pop(0)&#10;        topo.append(node)&#10;        for it in adj[node]:&#10;            indegree[it] -= 1&#10;            if indegree[it] == 0: q.append(it)&#10;    return topo</code></pre></details></td>
    </tr>
    <tr>
      <td>15</td>
      <td>Graph 16 Detect Cycle Directed Bfs<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Return true if cycle exists.</td>
      <td><b>Time:</b> O(V + E)<br><b>Space:</b> O(V)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> A DAG has a topological sort of exactly V elements. Use Kahn's BFS. If the number of elements pulled from the queue is < V, there's a cycle.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isCyclic(V: int, adj: List[List[int]]) -&gt; bool:&#10;    indegree = [0] * V&#10;    for i in range(V):&#10;        for it in adj[i]: indegree[it] += 1&#10;    q = [i for i in range(V) if indegree[i] == 0]&#10;    cnt = 0&#10;    while q:&#10;        node = q.pop(0)&#10;        cnt += 1&#10;        for it in adj[node]:&#10;            indegree[it] -= 1&#10;            if indegree[it] == 0: q.append(it)&#10;    return cnt != V</code></pre></details></td>
    </tr>
    <tr>
      <td>16</td>
      <td>Graph 17 Bipartite Graph Dfs<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/bipartite-graph/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Return true/false.</td>
      <td><b>Time:</b> O(V + E)<br><b>Space:</b> O(V)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> DFS. Color nodes with 0 and 1. If an adjacent node is uncolored, assign the opposite color and recurse. If it's colored and has the same color, it's not bipartite.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def isBipartite(V: int, adj: List[List[int]]) -&gt; bool:&#10;    color = [-1] * V&#10;    def dfs(node, col):&#10;        color[node] = col&#10;        for it in adj[node]:&#10;            if color[it] == -1:&#10;                if not dfs(it, 1 - col): return False&#10;            elif color[it] == col:&#10;                return False&#10;        return True&#10;    for i in range(V):&#10;        if color[i] == -1:&#10;            if not dfs(i, 0): return False&#10;    return True</code></pre></details></td>
    </tr>
    <tr>
      <td>17</td>
      <td>Graph 18 Alien Dictionary<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/alien-dictionary/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> words = ['baa', 'abcd', 'abca', 'cab', 'cad'], K = 4, Output: 'bdac'</td>
      <td><b>Time:</b> O(N * Len + K + E)<br><b>Space:</b> O(K + E)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Create a DAG based on mismatching characters between adjacent words. Use Kahn's algorithm (Topological Sort BFS) to find the character order.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findOrder(dict: List[str], N: int, K: int) -&gt; str:&#10;    adj = [[] for _ in range(K)]&#10;    for i in range(N - 1):&#10;        s1, s2 = dict[i], dict[i+1]&#10;        for j in range(min(len(s1), len(s2))):&#10;            if s1[j] != s2[j]:&#10;                adj[ord(s1[j]) - ord(&#x27;a&#x27;)].append(ord(s2[j]) - ord(&#x27;a&#x27;))&#10;                break&#10;    indegree = [0] * K&#10;    for i in range(K):&#10;        for it in adj[i]: indegree[it] += 1&#10;    q = [i for i in range(K) if indegree[i] == 0]&#10;    topo = []&#10;    while q:&#10;        node = q.pop(0)&#10;        topo.append(chr(node + ord(&#x27;a&#x27;)))&#10;        for it in adj[node]:&#10;            indegree[it] -= 1&#10;            if indegree[it] == 0: q.append(it)&#10;    return &#x27;&#x27;.join(topo)</code></pre></details></td>
    </tr>
    <tr>
      <td>18</td>
      <td>Graph 19 Shortest Path In Directed Acyclic Graph<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Topo Sort.</td>
      <td><b>Time:</b> O(V + E)<br><b>Space:</b> O(V + E)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Perform Topological Sort. Then iterate through the topologically sorted vertices. For each vertex `u`, relax its neighbors: `dist[v] = min(dist[v], dist[u] + weight)`. Return `dist` array.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def shortestPath(N: int, M: int, edges: List[List[int]]) -&gt; List[int]:&#10;    adj = [[] for _ in range(N)]&#10;    for u, v, wt in edges:&#10;        adj[u].append((v, wt))&#10;    vis = [0] * N&#10;    st = []&#10;    def topoSort(node):&#10;        vis[node] = 1&#10;        for v, wt in adj[node]:&#10;            if not vis[v]: topoSort(v)&#10;        st.append(node)&#10;    for i in range(N):&#10;        if not vis[i]: topoSort(i)&#10;    dist = [1e9] * N&#10;    dist[0] = 0&#10;    while st:&#10;        node = st.pop()&#10;        if dist[node] != 1e9:&#10;            for v, wt in adj[node]:&#10;                if dist[node] + wt &lt; dist[v]:&#10;                    dist[v] = dist[node] + wt&#10;    return [d if d != 1e9 else -1 for d in dist]</code></pre></details></td>
    </tr>
    <tr>
      <td>19</td>
      <td>Graph 20 Shortest Path In Undirected Graph With Unit Distance<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/shortest-path-in-undirected-graph-having-unit-distance/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> BFS approach.</td>
      <td><b>Time:</b> O(V + E)<br><b>Space:</b> O(V + E)</td>
      <td><code>#include <queue></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Standard BFS starting from source. Distance of neighbors is `dist[u] + 1`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def shortestPath(edges: List[List[int]], n: int, m: int, src: int) -&gt; List[int]:&#10;    adj = [[] for _ in range(n)]&#10;    for u, v in edges:&#10;        adj[u].append(v)&#10;        adj[v].append(u)&#10;    dist = [1e9] * n&#10;    dist[src] = 0&#10;    q = collections.deque([src])&#10;    while q:&#10;        node = q.popleft()&#10;        for neighbor in adj[node]:&#10;            if dist[node] + 1 &lt; dist[neighbor]:&#10;                dist[neighbor] = dist[node] + 1&#10;                q.append(neighbor)&#10;    return [d if d != 1e9 else -1 for d in dist]</code></pre></details></td>
    </tr>
    <tr>
      <td>20</td>
      <td>Graph 21 Dijkstras Algorithm<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> PQ based Dijkstra.</td>
      <td><b>Time:</b> O(E log V)<br><b>Space:</b> O(V)</td>
      <td><code>#include <queue></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Use a Min-Heap. `dist` array initialized to infinity. Push `{0, src}` to PQ. Pop `node`. If `dist[node] + weight < dist[adjNode]`, update `dist[adjNode]` and push `{dist[adjNode], adjNode}` to PQ.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def dijkstra(V: int, adj: List[List[List[int]]], S: int) -&gt; List[int]:&#10;    pq = [(0, S)]&#10;    dist = [1e9] * V&#10;    dist[S] = 0&#10;    while pq:&#10;        dis, node = heapq.heappop(pq)&#10;        for adjNode, edgeWeight in adj[node]:&#10;            if dis + edgeWeight &lt; dist[adjNode]:&#10;                dist[adjNode] = dis + edgeWeight&#10;                heapq.heappush(pq, (dist[adjNode], adjNode))&#10;    return dist</code></pre></details></td>
    </tr>
    <tr>
      <td>21</td>
      <td>Graph 22 Bellman Ford Algorithm<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/0' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Detect negative cycle.</td>
      <td><b>Time:</b> O(V * E)<br><b>Space:</b> O(V)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Relax all E edges V-1 times. If any edge can still be relaxed in the Vth iteration, then there's a negative cycle.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def bellman_ford(V: int, edges: List[List[int]], S: int) -&gt; List[int]:&#10;    dist = [int(1e8)] * V&#10;    dist[S] = 0&#10;    for _ in range(V - 1):&#10;        for u, v, wt in edges:&#10;            if dist[u] != int(1e8) and dist[u] + wt &lt; dist[v]:&#10;                dist[v] = dist[u] + wt&#10;    for u, v, wt in edges:&#10;        if dist[u] != int(1e8) and dist[u] + wt &lt; dist[v]:&#10;            return [-1]&#10;    return dist</code></pre></details></td>
    </tr>
    <tr>
      <td>22</td>
      <td>Graph 23 Floyd Warshall Algorithm<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> All pairs shortest path.</td>
      <td><b>Time:</b> O(V^3)<br><b>Space:</b> O(V^2) or O(1) if in-place</td>
      <td>-</td>
      <td><b>Unreachable:</b> Replace -1 with infinity before loop, revert back to -1 after.</td>
      <td><b>Explanation:</b> Iterate `k` (via node) from 0 to V-1. Iterate `i` and `j`. `matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])`. If `matrix[i][i] < 0`, negative cycle exists.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def shortest_distance(matrix):&#10;    n = len(matrix)&#10;    for i in range(n):&#10;        for j in range(n):&#10;            if matrix[i][j] == -1: matrix[i][j] = float(&#x27;inf&#x27;)&#10;            if i == j: matrix[i][j] = 0&#10;    for k in range(n):&#10;        for i in range(n):&#10;            for j in range(n):&#10;                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])&#10;    for i in range(n):&#10;        for j in range(n):&#10;            if matrix[i][j] == float(&#x27;inf&#x27;): matrix[i][j] = -1</code></pre></details></td>
    </tr>
    <tr>
      <td>23</td>
      <td>Graph 24 Minimum Spanning Tree<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/minimum-spanning-tree/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Kruskal or Prim's.</td>
      <td><b>Time:</b> O(E log V)<br><b>Space:</b> O(V)</td>
      <td><code>#include <queue></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Prim's Algorithm. Push `{0, 0}` to Min-Heap. If node is visited, continue. Mark visited, add weight to sum. Push all adjacent unvisited nodes to Heap.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def spanningTree(V: int, adj: List[List[List[int]]]) -&gt; int:&#10;    pq = [(0, 0)]&#10;    vis = [0] * V&#10;    sum = 0&#10;    while pq:&#10;        wt, node = heapq.heappop(pq)&#10;        if vis[node]: continue&#10;        vis[node] = 1&#10;        sum += wt&#10;        for adjNode, edW in adj[node]:&#10;            if not vis[adjNode]:&#10;                heapq.heappush(pq, (edW, adjNode))&#10;    return sum</code></pre></details></td>
    </tr>
    <tr>
      <td>24</td>
      <td>Graph 25 Prims Algorithm<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/minimum-spanning-tree/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> MST.</td>
      <td><b>Time:</b> O(E log V)<br><b>Space:</b> O(V)</td>
      <td><code>#include <queue></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Same as previous. Min Heap of `{weight, node}`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def spanningTree(V: int, adj: List[List[List[int]]]) -&gt; int:&#10;    pq = [(0, 0)]&#10;    vis = [0] * V&#10;    sum = 0&#10;    while pq:&#10;        wt, node = heapq.heappop(pq)&#10;        if vis[node]: continue&#10;        vis[node] = 1&#10;        sum += wt&#10;        for adjNode, edW in adj[node]:&#10;            if not vis[adjNode]:&#10;                heapq.heappush(pq, (edW, adjNode))&#10;    return sum</code></pre></details></td>
    </tr>
    <tr>
      <td>25</td>
      <td>Graph 26 Kruskals Algorithm<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/minimum-spanning-tree/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> DSU approach.</td>
      <td><b>Time:</b> O(E log E + E * alpha)<br><b>Space:</b> O(V + E)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Sort all edges by weight. Iterate through sorted edges. Use Disjoint Set Union (DSU) to check if adding the edge forms a cycle. If not, add edge to MST and union the sets.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class DisjointSet:&#10;    def __init__(self, n):&#10;        self.parent = list(range(n + 1))&#10;        self.size = [1] * (n + 1)&#10;    def find(self, i):&#10;        if self.parent[i] == i: return i&#10;        self.parent[i] = self.find(self.parent[i])&#10;        return self.parent[i]&#10;    def union(self, i, j):&#10;        root_i, root_j = self.find(i), self.find(j)&#10;        if root_i != root_j:&#10;            if self.size[root_i] &lt; self.size[root_j]:&#10;                self.parent[root_i] = root_j&#10;                self.size[root_j] += self.size[root_i]&#10;            else:&#10;                self.parent[root_j] = root_i&#10;                self.size[root_i] += self.size[root_j]&#10;&#10;def spanningTree(V, adj):&#10;    edges = []&#10;    for i in range(V):&#10;        for neighbor, wt in adj[i]:&#10;            edges.append((wt, i, neighbor))&#10;    edges.sort()&#10;    ds = DisjointSet(V)&#10;    sum = 0&#10;    for wt, u, v in edges:&#10;        if ds.find(u) != ds.find(v):&#10;            sum += wt&#10;            ds.union(u, v)&#10;    return sum</code></pre></details></td>
    </tr>
    <tr>
      <td>26</td>
      <td>Graph 27 Strongly Connected Components Kosarajus Algorithm<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/strongly-connected-components-kosarajus-algo/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Reverse graph.</td>
      <td><b>Time:</b> O(V + E)<br><b>Space:</b> O(V + E)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Kosaraju's Algorithm. 1. Topo sort the graph to get finish times (push to stack on completion). 2. Reverse all edges. 3. Pop from stack and run DFS on the reversed graph. Each successful DFS from stack gives one SCC.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def kosaraju(V: int, adj: List[List[int]]) -&gt; int:&#10;    vis = [0] * V&#10;    st = []&#10;    def dfs(node):&#10;        vis[node] = 1&#10;        for neighbor in adj[node]:&#10;            if not vis[neighbor]: dfs(neighbor)&#10;        st.append(node)&#10;    for i in range(V):&#10;        if not vis[i]: dfs(i)&#10;    adjT = [[] for _ in range(V)]&#10;    for i in range(V):&#10;        vis[i] = 0&#10;        for neighbor in adj[i]:&#10;            adjT[neighbor].append(i)&#10;    def dfs2(node):&#10;        vis[node] = 1&#10;        for neighbor in adjT[node]:&#10;            if not vis[neighbor]: dfs2(neighbor)&#10;    scc = 0&#10;    while st:&#10;        node = st.pop()&#10;        if not vis[node]:&#10;            scc += 1&#10;            dfs2(node)&#10;    return scc</code></pre></details></td>
    </tr>
    <tr>
      <td>27</td>
      <td>Graph 28 Bridges In Graph<br><br></b> <a href='https://leetcode.com/problems/critical-connections-in-a-network/' target='_blank'>LeetCode 1192</a></td>
      <td><b>Example 1:</b> Tarjan's algorithm.</td>
      <td><b>Time:</b> O(V + E)<br><b>Space:</b> O(V + E)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Tarjan's algorithm. Maintain `tin` (time of insertion) and `low` (lowest time reachable). If `low[neighbor] > tin[node]`, the edge `(node, neighbor)` is a bridge. Update `low[node] = min(low[node], low[neighbor])`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def criticalConnections(n: int, connections: List[List[int]]) -&gt; List[List[int]]:&#10;    adj = [[] for _ in range(n)]&#10;    for u, v in connections:&#10;        adj[u].append(v)&#10;        adj[v].append(u)&#10;    vis = [0] * n&#10;    tin, low = [0] * n, [0] * n&#10;    bridges = []&#10;    timer = 1&#10;    def dfs(node, parent):&#10;        nonlocal timer&#10;        vis[node] = 1&#10;        tin[node] = low[node] = timer&#10;        timer += 1&#10;        for neighbor in adj[node]:&#10;            if neighbor == parent: continue&#10;            if not vis[neighbor]:&#10;                dfs(neighbor, node)&#10;                low[node] = min(low[node], low[neighbor])&#10;                if low[neighbor] &gt; tin[node]:&#10;                    bridges.append([node, neighbor])&#10;            else:&#10;                low[node] = min(low[node], low[neighbor])&#10;    dfs(0, -1)&#10;    return bridges</code></pre></details></td>
    </tr>
    <tr>
      <td>28</td>
      <td>Graph 29 Articulation Point I<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/articulation-point-1/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Tarjan's algorithm with discovery times.</td>
      <td><b>Time:</b> O(V + E)<br><b>Space:</b> O(V)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Maintain `tin` (insertion time) and `low` (lowest insertion time reachable). A node `u` is an articulation point if `low[v] >= tin[u]` (and it's not root). If root, it's an articulation point if it has >1 children in DFS tree.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class Solution:&#10;    def __init__(self):&#10;        self.timer = 0&#10;    def dfs(self, node, parent, vis, tin, low, mark, adj):&#10;        vis[node] = 1&#10;        tin[node] = low[node] = self.timer&#10;        self.timer += 1&#10;        child = 0&#10;        for it in adj[node]:&#10;            if it == parent: continue&#10;            if not vis[it]:&#10;                self.dfs(it, node, vis, tin, low, mark, adj)&#10;                low[node] = min(low[node], low[it])&#10;                if low[it] &gt;= tin[node] and parent != -1:&#10;                    mark[node] = 1&#10;                child += 1&#10;            else:&#10;                low[node] = min(low[node], tin[it])&#10;        if child &gt; 1 and parent == -1:&#10;            mark[node] = 1&#10;    def articulationPoints(self, V, adj):&#10;        vis = [0] * V&#10;        tin = [0] * V&#10;        low = [0] * V&#10;        mark = [0] * V&#10;        for i in range(V):&#10;            if not vis[i]:&#10;                self.dfs(i, -1, vis, tin, low, mark, adj)&#10;        ans = []&#10;        for i in range(V):&#10;            if mark[i] == 1: ans.append(i)&#10;        if len(ans) == 0: return [-1]&#10;        return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>29</td>
      <td>Graph 30 Number Of Provinces Dsu<br><br></b> <a href='https://leetcode.com/problems/number-of-provinces/' target='_blank'>LeetCode 547</a></td>
      <td><b>Example 1:</b> Connect elements, count unique parents.</td>
      <td><b>Time:</b> O(N^2 * alpha(N))<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Create DSU of size `n`. For every edge in `isConnected`, union the two nodes. The number of provinces is the number of nodes where `find(i) == i`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class DisjointSet:&#10;    def __init__(self, n):&#10;        self.parent = list(range(n + 1))&#10;        self.size = [1] * (n + 1)&#10;    def findUPar(self, node):&#10;        if node == self.parent[node]:&#10;            return node&#10;        self.parent[node] = self.findUPar(self.parent[node])&#10;        return self.parent[node]&#10;    def unionBySize(self, u, v):&#10;        ulp_u = self.findUPar(u)&#10;        ulp_v = self.findUPar(v)&#10;        if ulp_u == ulp_v: return&#10;        if self.size[ulp_u] &lt; self.size[ulp_v]:&#10;            self.parent[ulp_u] = ulp_v&#10;            self.size[ulp_v] += self.size[ulp_u]&#10;        else:&#10;            self.parent[ulp_v] = ulp_u&#10;            self.size[ulp_u] += self.size[ulp_v]&#10;def findCircleNum(isConnected: List[List[int]]) -&gt; int:&#10;    n = len(isConnected)&#10;    ds = DisjointSet(n)&#10;    for i in range(n):&#10;        for j in range(n):&#10;            if isConnected[i][j] == 1:&#10;                ds.unionBySize(i, j)&#10;    cnt = 0&#10;    for i in range(n):&#10;        if ds.findUPar(i) == i:&#10;            cnt += 1&#10;    return cnt</code></pre></details></td>
    </tr>
    <tr>
      <td>30</td>
      <td>Graph 31 Accounts Merge<br><br></b> <a href='https://leetcode.com/problems/accounts-merge/' target='_blank'>LeetCode 721</a></td>
      <td><b>Example 1:</b> DSU on accounts using emails.</td>
      <td><b>Time:</b> O(N log N * alpha(N)) where N is total emails<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Map each email to an account index. If an email is seen again, union the current account index with the previously mapped account index. Finally, group emails by their root account index, sort them, and attach the name.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def accountsMerge(accounts: List[List[str]]) -&gt; List[List[str]]:&#10;    n = len(accounts)&#10;    parent = list(range(n))&#10;    def find(i):&#10;        if parent[i] == i: return i&#10;        parent[i] = find(parent[i])&#10;        return parent[i]&#10;    def union(i, j):&#10;        root_i, root_j = find(i), find(j)&#10;        if root_i != root_j: parent[root_i] = root_j&#10;    email_to_id = {}&#10;    for i, acc in enumerate(accounts):&#10;        for email in acc[1:]:&#10;            if email in email_to_id:&#10;                union(i, email_to_id[email])&#10;            else:&#10;                email_to_id[email] = i&#10;    id_to_emails = collections.defaultdict(list)&#10;    for email, i in email_to_id.items():&#10;        id_to_emails[find(i)].append(email)&#10;    ans = []&#10;    for i, emails in id_to_emails.items():&#10;        ans.append([accounts[i][0]] + sorted(emails))&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>31</td>
      <td>Graph 32 Number Of Operations To Make Network Connected<br><br></b> <a href='https://leetcode.com/problems/number-of-operations-to-make-network-connected/' target='_blank'>LeetCode 1319</a></td>
      <td><b>Example 1:</b> Extra edges and connected components.</td>
      <td><b>Time:</b> O(E * alpha(N))<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> If total edges < n - 1, impossible. Use DSU to count number of connected components `C` and number of extra edges `E`. An edge is extra if `find(u) == find(v)`. We need `C - 1` edges to connect `C` components. Since total edges >= n - 1, we guaranteed have enough extra edges. Answer is `C - 1`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def makeConnected(n: int, connections: List[List[int]]) -&gt; int:&#10;    if len(connections) &lt; n - 1: return -1&#10;    parent = list(range(n))&#10;    def find(i):&#10;        if parent[i] == i: return i&#10;        parent[i] = find(parent[i])&#10;        return parent[i]&#10;    components = n&#10;    for u, v in connections:&#10;        root_u, root_v = find(u), find(v)&#10;        if root_u != root_v:&#10;            parent[root_u] = root_v&#10;            components -= 1&#10;    return components - 1</code></pre></details></td>
    </tr>
    <tr>
      <td>32</td>
      <td>Graph 33 Most Stones Removed With Same Row Or Column<br><br></b> <a href='https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/' target='_blank'>LeetCode 947</a></td>
      <td><b>Example 1:</b> Treat rows and columns as nodes.</td>
      <td><b>Time:</b> O(N * alpha(N))<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Imagine rows and columns are nodes in a bipartite graph. A stone at `(r, c)` connects row `r` and column `c`. The answer is `total_stones - number_of_connected_components`. We can map cols to `col + 10001` to use a single DSU.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def removeStones(stones: List[List[int]]) -&gt; int:&#10;    parent = {}&#10;    components = [0]&#10;    def find(i):&#10;        if i not in parent:&#10;            parent[i] = i&#10;            components[0] += 1&#10;        if parent[i] == i: return i&#10;        parent[i] = find(parent[i])&#10;        return parent[i]&#10;    def union(i, j):&#10;        root_i, root_j = find(i), find(j)&#10;        if root_i != root_j:&#10;            parent[root_i] = root_j&#10;            components[0] -= 1&#10;    for r, c in stones:&#10;        union(r, ~c)&#10;    return len(stones) - components[0]</code></pre></details></td>
    </tr>
    <tr>
      <td>33</td>
      <td>Graph 34 Making A Large Island<br><br></b> <a href='https://leetcode.com/problems/making-a-large-island/' target='_blank'>LeetCode 827</a></td>
      <td><b>Example 1:</b> Component sizes with DSU.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N^2)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Step 1: Use DSU to connect all adjacent 1s and calculate the size of each component. Step 2: For each 0, check its 4 neighbors. Find the unique roots of those neighbors. The potential new island size is `1 + sum(size[root])` for each unique root. Find max potential size. Handle case where matrix is all 1s.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def largestIsland(grid: List[List[int]]) -&gt; int:&#10;    n = len(grid)&#10;    parent = list(range(n * n))&#10;    size = [1] * (n * n)&#10;    def find(i):&#10;        if parent[i] == i: return i&#10;        parent[i] = find(parent[i])&#10;        return parent[i]&#10;    def union(i, j):&#10;        root_i, root_j = find(i), find(j)&#10;        if root_i != root_j:&#10;            if size[root_i] &lt; size[root_j]:&#10;                parent[root_i] = root_j&#10;                size[root_j] += size[root_i]&#10;            else:&#10;                parent[root_j] = root_i&#10;                size[root_i] += size[root_j]&#10;    dirs = [(-1,0), (1,0), (0,-1), (0,1)]&#10;    for r in range(n):&#10;        for c in range(n):&#10;            if grid[r][c] == 1:&#10;                for dr, dc in dirs:&#10;                    nr, nc = r + dr, c + dc&#10;                    if 0 &lt;= nr &lt; n and 0 &lt;= nc &lt; n and grid[nr][nc] == 1:&#10;                        union(r * n + c, nr * n + nc)&#10;    mx = 0&#10;    for r in range(n):&#10;        for c in range(n):&#10;            if grid[r][c] == 0:&#10;                components = set()&#10;                for dr, dc in dirs:&#10;                    nr, nc = r + dr, c + dc&#10;                    if 0 &lt;= nr &lt; n and 0 &lt;= nc &lt; n and grid[nr][nc] == 1:&#10;                        components.add(find(nr * n + nc))&#10;                mx = max(mx, 1 + sum(size[comp] for comp in components))&#10;    return mx if mx &gt; 0 else n * n</code></pre></details></td>
    </tr>
    <tr>
      <td>34</td>
      <td>Graph 35 Swim In Rising Water<br><br></b> <a href='https://leetcode.com/problems/swim-in-rising-water/' target='_blank'>LeetCode 778</a></td>
      <td><b>Example 1:</b> Dijkstra-like or Binary Search + BFS.</td>
      <td><b>Time:</b> O(N^2 log N)<br><b>Space:</b> O(N^2)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Use a priority queue (Dijkstra variant). The cost to reach a cell is `max(cost_of_previous_cell, grid[r][c])`. Extract min cost cell, relax neighbors.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def swimInWater(grid: List[List[int]]) -&gt; int:&#10;    n = len(grid)&#10;    pq = [(grid[0][0], 0, 0)]&#10;    dist = [[float(&#x27;inf&#x27;)] * n for _ in range(n)]&#10;    dist[0][0] = grid[0][0]&#10;    dirs = [(-1,0), (1,0), (0,-1), (0,1)]&#10;    while pq:&#10;        d, r, c = heapq.heappop(pq)&#10;        if r == n - 1 and c == n - 1: return d&#10;        for dr, dc in dirs:&#10;            nr, nc = r + dr, c + dc&#10;            if 0 &lt;= nr &lt; n and 0 &lt;= nc &lt; n:&#10;                next_d = max(d, grid[nr][nc])&#10;                if next_d &lt; dist[nr][nc]:&#10;                    dist[nr][nc] = next_d&#10;                    heapq.heappush(pq, (next_d, nr, nc))&#10;    return 0</code></pre></details></td>
    </tr>
    <tr>
      <td>35</td>
      <td>Graph 36 Word Ladder I<br><br></b> <a href='https://leetcode.com/problems/word-ladder/' target='_blank'>LeetCode 127</a></td>
      <td><b>Example 1:</b> BFS level by level.</td>
      <td><b>Time:</b> O(N * M * 26) where N is words, M is word length<br><b>Space:</b> O(N)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> BFS. Start from `beginWord`. In each step, change one character from 'a' to 'z' and check if new word is in `wordList`. If yes, push to queue, erase from `wordList` to avoid loops, and continue. Track level/steps.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -&gt; int:&#10;    wordSet = set(wordList)&#10;    if endWord not in wordSet: return 0&#10;    q = collections.deque([(beginWord, 1)])&#10;    if beginWord in wordSet: wordSet.remove(beginWord)&#10;    while q:&#10;        word, steps = q.popleft()&#10;        if word == endWord: return steps&#10;        for i in range(len(word)):&#10;            for c in &#x27;abcdefghijklmnopqrstuvwxyz&#x27;:&#10;                newWord = word[:i] + c + word[i+1:]&#10;                if newWord in wordSet:&#10;                    wordSet.remove(newWord)&#10;                    q.append((newWord, steps + 1))&#10;    return 0</code></pre></details></td>
    </tr>
    <tr>
      <td>36</td>
      <td>Graph 37 Word Ladder Ii<br><br></b> <a href='https://leetcode.com/problems/word-ladder-ii/' target='_blank'>LeetCode 126</a></td>
      <td><b>Example 1:</b> BFS for distance, DFS for paths.</td>
      <td><b>Time:</b> O(V + E + Paths)<br><b>Space:</b> O(V + E)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> BFS to find minimum steps to reach each word. Then DFS starting from `endWord` backwards to `beginWord`, only exploring paths where `dist[next_word] == dist[curr_word] - 1`. Reverse the built paths.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def findLadders(beginWord: str, endWord: str, wordList: List[str]) -&gt; List[List[str]]:&#10;    wordSet = set(wordList)&#10;    if endWord not in wordSet: return []&#10;    q = collections.deque([beginWord])&#10;    mpp = {beginWord: 1}&#10;    wordSet.discard(beginWord)&#10;    while q:&#10;        word = q.popleft()&#10;        if word == endWord: break&#10;        steps = mpp[word]&#10;        for i in range(len(word)):&#10;            for c in &#x27;abcdefghijklmnopqrstuvwxyz&#x27;:&#10;                newWord = word[:i] + c + word[i+1:]&#10;                if newWord in wordSet:&#10;                    mpp[newWord] = steps + 1&#10;                    q.append(newWord)&#10;                    wordSet.remove(newWord)&#10;    ans = []&#10;    if endWord in mpp:&#10;        def dfs(word, seq):&#10;            if word == beginWord:&#10;                ans.append(seq[::-1])&#10;                return&#10;            steps = mpp[word]&#10;            for i in range(len(word)):&#10;                for c in &#x27;abcdefghijklmnopqrstuvwxyz&#x27;:&#10;                    newWord = word[:i] + c + word[i+1:]&#10;                    if newWord in mpp and mpp[newWord] + 1 == steps:&#10;                        seq.append(newWord)&#10;                        dfs(newWord, seq)&#10;                        seq.pop()&#10;        dfs(endWord, [endWord])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>37</td>
      <td>Graph 38 Network Delay Time<br><br></b> <a href='https://leetcode.com/problems/network-delay-time/' target='_blank'>LeetCode 743</a></td>
      <td><b>Example 1:</b> Dijkstra's to find max shortest path.</td>
      <td><b>Time:</b> O(E log V)<br><b>Space:</b> O(V + E)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Standard Dijkstra's shortest path from node `k`. Return the maximum value in the distances array. If any node remains unvisited (dist == inf), return -1.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def networkDelayTime(times: List[List[int]], n: int, k: int) -&gt; int:&#10;    adj = collections.defaultdict(list)&#10;    for u, v, w in times:&#10;        adj[u].append((v, w))&#10;    pq = [(0, k)]&#10;    dist = {i: float(&#x27;inf&#x27;) for i in range(1, n + 1)}&#10;    dist[k] = 0&#10;    while pq:&#10;        time, node = heapq.heappop(pq)&#10;        if time &gt; dist[node]: continue&#10;        for adjNode, wt in adj[node]:&#10;            if time + wt &lt; dist[adjNode]:&#10;                dist[adjNode] = time + wt&#10;                heapq.heappush(pq, (time + wt, adjNode))&#10;    mx = max(dist.values())&#10;    return mx if mx != float(&#x27;inf&#x27;) else -1</code></pre></details></td>
    </tr>
    <tr>
      <td>38</td>
      <td>Graph 39 Cheapest Flights Within K Stops<br><br></b> <a href='https://leetcode.com/problems/cheapest-flights-within-k-stops/' target='_blank'>LeetCode 787</a></td>
      <td><b>Example 1:</b> Dijkstra's with Stops / BFS.</td>
      <td><b>Time:</b> O(E)<br><b>Space:</b> O(N + E)</td>
      <td><code>#include <queue></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Use a queue storing `(stops, node, cost)`. We don't need a priority queue because stops increase uniformly by 1. Distance array stores min cost to reach each node. Only push to queue if new cost is cheaper. If `stops > k`, skip.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -&gt; int:&#10;    adj = collections.defaultdict(list)&#10;    for u, v, w in flights:&#10;        adj[u].append((v, w))&#10;    q = collections.deque([(0, src, 0)]) # stops, node, cost&#10;    dist = [float(&#x27;inf&#x27;)] * n&#10;    dist[src] = 0&#10;    while q:&#10;        stops, node, cost = q.popleft()&#10;        if stops &gt; k: continue&#10;        for nxt, weight in adj[node]:&#10;            if cost + weight &lt; dist[nxt] and stops &lt;= k:&#10;                dist[nxt] = cost + weight&#10;                q.append((stops + 1, nxt, cost + weight))&#10;    return dist[dst] if dist[dst] != float(&#x27;inf&#x27;) else -1</code></pre></details></td>
    </tr>
    <tr>
      <td>39</td>
      <td>Graph 40 Minimum Multiplications To Reach End<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/minimum-multiplications-to-reach-end/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> BFS / Dijkstra's with unit weights.</td>
      <td><b>Time:</b> O(100000 * N)<br><b>Space:</b> O(100000)</td>
      <td><code>#include <queue></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Since each multiplication is 1 step, we can use BFS. The 'nodes' are values from 0 to 99999. Use an array `dist` initialized to infinity. Push `start` to queue. For each popped node, multiply by all array elements `% 100000`. If we find a shorter path, push to queue.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def minimumMultiplications(arr: List[int], start: int, end: int) -&gt; int:&#10;    if start == end: return 0&#10;    q = collections.deque([(start, 0)])&#10;    dist = [float(&#x27;inf&#x27;)] * 100000&#10;    dist[start] = 0&#10;    mod = 100000&#10;    while q:&#10;        node, steps = q.popleft()&#10;        for it in arr:&#10;            num = (node * it) % mod&#10;            if steps + 1 &lt; dist[num]:&#10;                dist[num] = steps + 1&#10;                if num == end: return steps + 1&#10;                q.append((num, steps + 1))&#10;    return -1</code></pre></details></td>
    </tr>
    <tr>
      <td>40</td>
      <td>Graph 41 Number Of Ways To Arrive At Destination<br><br></b> <a href='https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/' target='_blank'>LeetCode 1976</a></td>
      <td><b>Example 1:</b> Dijkstra's with Ways Count.</td>
      <td><b>Time:</b> O(E log V)<br><b>Space:</b> O(V + E)</td>
      <td><code>#include <queue></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Modify Dijkstra's. Keep `dist` array and `ways` array. When relaxing an edge: if `curr_dist + weight < dist[neighbor]`, update `dist`, push to PQ, and `ways[neighbor] = ways[curr_node]`. If `curr_dist + weight == dist[neighbor]`, `ways[neighbor] = (ways[neighbor] + ways[curr_node]) % MOD`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections, heapq&#10;def countPaths(n: int, roads: List[List[int]]) -&gt; int:&#10;    adj = collections.defaultdict(list)&#10;    for u, v, w in roads:&#10;        adj[u].append((v, w))&#10;        adj[v].append((u, w))&#10;    heap = [(0, 0)]&#10;    dist = [float(&#x27;inf&#x27;)] * n&#10;    ways = [0] * n&#10;    dist[0] = 0&#10;    ways[0] = 1&#10;    mod = 10**9 + 7&#10;    while heap:&#10;        d, node = heapq.heappop(heap)&#10;        if d &gt; dist[node]: continue&#10;        for nxt, weight in adj[node]:&#10;            if d + weight &lt; dist[nxt]:&#10;                dist[nxt] = d + weight&#10;                ways[nxt] = ways[node]&#10;                heapq.heappush(heap, (dist[nxt], nxt))&#10;            elif d + weight == dist[nxt]:&#10;                ways[nxt] = (ways[nxt] + ways[node]) % mod&#10;    return ways[n-1]</code></pre></details></td>
    </tr>
    <tr>
      <td>41</td>
      <td>Graph 42 Find The City With The Smallest Number Of Neighbors At A Threshold Distance<br><br></b> <a href='https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/' target='_blank'>LeetCode 1334</a></td>
      <td><b>Example 1:</b> Floyd-Warshall Algorithm.</td>
      <td><b>Time:</b> O(V^3)<br><b>Space:</b> O(V^2)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Use Floyd-Warshall to find shortest paths between all pairs of nodes. For each city, count the number of reachable cities within `distanceThreshold`. Return the city with the minimum count (and greatest ID on tie).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def findTheCity(n: int, edges: List[List[int]], distanceThreshold: int) -&gt; int:&#10;    dist = [[float(&#x27;inf&#x27;)] * n for _ in range(n)]&#10;    for i in range(n): dist[i][i] = 0&#10;    for u, v, w in edges:&#10;        dist[u][v] = w&#10;        dist[v][u] = w&#10;    for k in range(n):&#10;        for i in range(n):&#10;            for j in range(n):&#10;                if dist[i][k] != float(&#x27;inf&#x27;) and dist[k][j] != float(&#x27;inf&#x27;):&#10;                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])&#10;    minCities = n&#10;    ansCity = -1&#10;    for i in range(n):&#10;        cnt = sum(1 for j in range(n) if dist[i][j] &lt;= distanceThreshold)&#10;        if cnt &lt;= minCities:&#10;            minCities = cnt&#10;            ansCity = i&#10;    return ansCity</code></pre></details></td>
    </tr>
    <tr>
      <td>42</td>
      <td>Graph 43 Minimum Spanning Tree Prim<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/minimum-spanning-tree/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Prim's Algorithm using Min-Heap.</td>
      <td><b>Time:</b> O(E log V)<br><b>Space:</b> O(E + V)</td>
      <td><code>#include <queue></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Start from node 0. Push `(0, 0)` -> `(weight, node)` into PQ. Maintain `visited` array. Pop min edge. If not visited, mark visited, add weight to sum. Traverse its neighbors; if not visited, push to PQ.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def spanningTree(V, adj):&#10;    pq = [(0, 0)]&#10;    vis = [0] * V&#10;    sum_wt = 0&#10;    while pq:&#10;        wt, node = heapq.heappop(pq)&#10;        if vis[node]: continue&#10;        vis[node] = 1&#10;        sum_wt += wt&#10;        for neighbor in adj[node]:&#10;            adjNode, edW = neighbor[0], neighbor[1]&#10;            if not vis[adjNode]:&#10;                heapq.heappush(pq, (edW, adjNode))&#10;    return sum_wt</code></pre></details></td>
    </tr>
    <tr>
      <td>43</td>
      <td>Graph 44 Kruskals Minimum Spanning Tree Algorithm<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/minimum-spanning-tree/1' target='_blank'>GFG</a></td>
      <td><b>Example 1:</b> Disjoint Set / Union Find.</td>
      <td><b>Time:</b> O(E log E)<br><b>Space:</b> O(E + V)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Extract all edges as `(weight, u, v)`. Sort edges by weight. Iterate through sorted edges. Use Disjoint Set (Union-Find) to check if `u` and `v` are in the same component. If not, union them and add weight to sum.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">class DisjointSet:&#10;    def __init__(self, n):&#10;        self.parent = list(range(n + 1))&#10;        self.rank = [0] * (n + 1)&#10;    def find(self, i):&#10;        if self.parent[i] == i: return i&#10;        self.parent[i] = self.find(self.parent[i])&#10;        return self.parent[i]&#10;    def union(self, i, j):&#10;        root_i = self.find(i)&#10;        root_j = self.find(j)&#10;        if root_i != root_j:&#10;            if self.rank[root_i] &lt; self.rank[root_j]:&#10;                self.parent[root_i] = root_j&#10;            elif self.rank[root_i] &gt; self.rank[root_j]:&#10;                self.parent[root_j] = root_i&#10;            else:&#10;                self.parent[root_j] = root_i&#10;                self.rank[root_i] += 1&#10;            return True&#10;        return False&#10;&#10;def spanningTree(V, adj):&#10;    edges = []&#10;    for i in range(V):&#10;        for neighbor in adj[i]:&#10;            edges.append((neighbor[1], i, neighbor[0]))&#10;    edges.sort()&#10;    ds = DisjointSet(V)&#10;    mst_wt = 0&#10;    for wt, u, v in edges:&#10;        if ds.union(u, v):&#10;            mst_wt += wt&#10;    return mst_wt</code></pre></details></td>
    </tr>
    <tr>
      <td>44</td>
      <td>Graph 45 Number Of Provinces Disjoint Set<br><br></b> <a href='https://leetcode.com/problems/number-of-provinces/' target='_blank'>LeetCode 547</a></td>
      <td><b>Example 1:</b> Counting Unique Parents in DSU.</td>
      <td><b>Time:</b> O(V^2 * alpha)<br><b>Space:</b> O(V)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Initialize Disjoint Set for `n` nodes. Iterate through `isConnected` matrix. If `isConnected[i][j] == 1`, union `i` and `j`. After processing all edges, count how many nodes are their own parents (`parent[i] == i`).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python"># Use DisjointSet class&#10;def findCircleNum(isConnected: List[List[int]]) -&gt; int:&#10;    n = len(isConnected)&#10;    ds = DisjointSet(n)&#10;    for i in range(n):&#10;        for j in range(n):&#10;            if isConnected[i][j] == 1: ds.union(i, j)&#10;    return sum(1 for i in range(n) if ds.find(i) == i)</code></pre></details></td>
    </tr>
    <tr>
      <td>45</td>
      <td>Graph 46 Number Of Operations To Make Network Connected<br><br></b> <a href='https://leetcode.com/problems/number-of-operations-to-make-network-connected/' target='_blank'>LeetCode 1319</a></td>
      <td><b>Example 1:</b> Count Extra Edges using DSU.</td>
      <td><b>Time:</b> O(E * alpha)<br><b>Space:</b> O(V)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> If total edges < n - 1, return -1. Count extra edges while building DSU. If union fails (already connected), it's an extra edge. Number of operations to connect components is `components - 1`. If `extraEdges >= components - 1`, return `components - 1`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def makeConnected(n: int, connections: List[List[int]]) -&gt; int:&#10;    if len(connections) &lt; n - 1: return -1&#10;    ds = DisjointSet(n)&#10;    extraEdges = 0&#10;    for u, v in connections:&#10;        if not ds.union(u, v): extraEdges += 1&#10;    components = sum(1 for i in range(n) if ds.find(i) == i)&#10;    if extraEdges &gt;= components - 1: return components - 1&#10;    return -1</code></pre></details></td>
    </tr>
    <tr>
      <td>46</td>
      <td>Graph 47 Most Stones Removed With Same Row Or Column<br><br></b> <a href='https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/' target='_blank'>LeetCode 947</a></td>
      <td><b>Example 1:</b> DSU on Rows and Columns.</td>
      <td><b>Time:</b> O(N * alpha)<br><b>Space:</b> O(Max(Row, Col))</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Treat rows and columns as nodes in DSU. Connect row `x` to column `y` for each stone. Max row and max col define the size of DSU. A column node index can be `maxRow + y + 1` to separate from row indices. The answer is `total stones - number of connected components`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def removeStones(stones: List[List[int]]) -&gt; int:&#10;    maxRow = maxCol = 0&#10;    for x, y in stones:&#10;        maxRow = max(maxRow, x)&#10;        maxCol = max(maxCol, y)&#10;    ds = DisjointSet(maxRow + maxCol + 1)&#10;    stoneNodes = set()&#10;    for x, y in stones:&#10;        nodeRow = x&#10;        nodeCol = y + maxRow + 1&#10;        ds.union(nodeRow, nodeCol)&#10;        stoneNodes.add(nodeRow)&#10;        stoneNodes.add(nodeCol)&#10;    components = sum(1 for node in stoneNodes if ds.find(node) == node)&#10;    return len(stones) - components</code></pre></details></td>
    </tr>
    <tr>
      <td>47</td>
      <td>Graph 48 Accounts Merge<br><br></b> <a href='https://leetcode.com/problems/accounts-merge/' target='_blank'>LeetCode 721</a></td>
      <td><b>Example 1:</b> Map Emails to IDs, DSU on IDs.</td>
      <td><b>Time:</b> O(N * M * log(N * M)) where N=accounts, M=max emails<br><b>Space:</b> O(N * M)</td>
      <td><code>#include <unordered_map></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Create a DSU of size N (number of accounts). Map each email to its first seen account ID. If an email is seen again, union the current account ID with the mapped account ID. Then group emails by the ultimate parent of their account ID. Sort emails in each group and format the result.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def accountsMerge(accounts: List[List[str]]) -&gt; List[List[str]]:&#10;    n = len(accounts)&#10;    ds = DisjointSet(n)&#10;    mailNode = {}&#10;    for i in range(n):&#10;        for j in range(1, len(accounts[i])):&#10;            mail = accounts[i][j]&#10;            if mail not in mailNode:&#10;                mailNode[mail] = i&#10;            else:&#10;                ds.union(i, mailNode[mail])&#10;    mergedMails = collections.defaultdict(list)&#10;    for mail, node in mailNode.items():&#10;        root = ds.find(node)&#10;        mergedMails[root].append(mail)&#10;    ans = []&#10;    for i in range(n):&#10;        if i not in mergedMails: continue&#10;        ans.append([accounts[i][0]] + sorted(mergedMails[i]))&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>48</td>
      <td>Graph 49 Network Delay Time<br><br></b> <a href='https://leetcode.com/problems/network-delay-time/' target='_blank'>LeetCode 743</a></td>
      <td><b>Example 1:</b> Dijkstra's Algorithm.</td>
      <td><b>Time:</b> O(E log V)<br><b>Space:</b> O(N + E)</td>
      <td><code>#include <queue></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Find shortest path from source node `k` to all other nodes using Dijkstra's algorithm. The answer is the maximum distance among all nodes. If any node is unreachable (distance is infinity), return -1.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections, heapq&#10;def networkDelayTime(times: List[List[int]], n: int, k: int) -&gt; int:&#10;    adj = collections.defaultdict(list)&#10;    for u, v, w in times:&#10;        adj[u].append((v, w))&#10;    dist = [float(&#x27;inf&#x27;)] * (n + 1)&#10;    dist[k] = 0&#10;    pq = [(0, k)]&#10;    while pq:&#10;        d, node = heapq.heappop(pq)&#10;        if d &gt; dist[node]: continue&#10;        for nxt, wt in adj[node]:&#10;            if d + wt &lt; dist[nxt]:&#10;                dist[nxt] = d + wt&#10;                heapq.heappush(pq, (dist[nxt], nxt))&#10;    ans = max(dist[1:])&#10;    return ans if ans != float(&#x27;inf&#x27;) else -1</code></pre></details></td>
    </tr>
    <tr>
      <td>49</td>
      <td>Graph 50 Find Eventual Safe States<br><br></b> <a href='https://leetcode.com/problems/find-eventual-safe-states/' target='_blank'>LeetCode 802</a></td>
      <td><b>Example 1:</b> Topological Sort using Kahn's Algorithm on reversed graph.</td>
      <td><b>Time:</b> O(V + E)<br><b>Space:</b> O(V + E)</td>
      <td><code>#include <queue></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Reverse all edges in the graph. Terminal nodes become sources (indegree 0). Run Kahn's algorithm (BFS topological sort). Any node processed is part of a path that only leads to terminal nodes (safe node). Sort the resulting nodes.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def eventualSafeNodes(graph: List[List[int]]) -&gt; List[int]:&#10;    V = len(graph)&#10;    adjRev = [[] for _ in range(V)]&#10;    indegree = [0] * V&#10;    for i in range(V):&#10;        for neighbor in graph[i]:&#10;            adjRev[neighbor].append(i)&#10;            indegree[i] += 1&#10;    q = collections.deque([i for i in range(V) if indegree[i] == 0])&#10;    safeNodes = []&#10;    while q:&#10;        node = q.popleft()&#10;        safeNodes.append(node)&#10;        for neighbor in adjRev[node]:&#10;            indegree[neighbor] -= 1&#10;            if indegree[neighbor] == 0:&#10;                q.append(neighbor)&#10;    return sorted(safeNodes)</code></pre></details></td>
    </tr>
    <tr>
      <td>50</td>
      <td>Graph 51 Word Ladder<br><br></b> <a href='https://leetcode.com/problems/word-ladder/' target='_blank'>LeetCode 127</a></td>
      <td><b>Example 1:</b> BFS Shortest Path.</td>
      <td><b>Time:</b> O(N * L * 26) where L is word length<br><b>Space:</b> O(N)</td>
      <td><code>#include <queue>\n#include <unordered_set></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Use BFS. Insert words from `wordList` into a hash set for O(1) lookup. Push `{beginWord, 1}` to a queue and remove it from the set. Pop a word, change each character one by one to 'a'-'z'. If the new word is in the set, push `{newWord, steps+1}` and remove from set. If `newWord == endWord`, return `steps+1`.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -&gt; int:&#10;    wordSet = set(wordList)&#10;    q = collections.deque([(beginWord, 1)])&#10;    if beginWord in wordSet: wordSet.remove(beginWord)&#10;    while q:&#10;        word, steps = q.popleft()&#10;        if word == endWord: return steps&#10;        for i in range(len(word)):&#10;            for c in &#x27;abcdefghijklmnopqrstuvwxyz&#x27;:&#10;                newWord = word[:i] + c + word[i+1:]&#10;                if newWord in wordSet:&#10;                    wordSet.remove(newWord)&#10;                    q.append((newWord, steps + 1))&#10;    return 0</code></pre></details></td>
    </tr>
    <tr>
      <td>51</td>
      <td>Graph 52 Word Ladder Ii<br><br></b> <a href='https://leetcode.com/problems/word-ladder-ii/' target='_blank'>LeetCode 126</a></td>
      <td><b>Example 1:</b> BFS to find shortest path map + DFS to backtrack paths.</td>
      <td><b>Time:</b> O(N * L * 26 + Paths)<br><b>Space:</b> O(N * L)</td>
      <td><code>#include <queue>\n#include <unordered_set>\n#include <unordered_map></code></td>
      <td>-</td>
      <td><b>Explanation:</b> First, use BFS to build a map storing the shortest distance from `beginWord` to every reachable word. Then use DFS starting from `endWord` backwards to `beginWord` to reconstruct the paths. In DFS, only traverse to words whose distance is exactly 1 less than the current word's distance.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import collections&#10;def findLadders(beginWord: str, endWord: str, wordList: List[str]) -&gt; List[List[str]]:&#10;    wordSet = set(wordList)&#10;    mpp = {beginWord: 1}&#10;    q = collections.deque([beginWord])&#10;    if beginWord in wordSet: wordSet.remove(beginWord)&#10;    while q:&#10;        word = q.popleft()&#10;        steps = mpp[word]&#10;        if word == endWord: break&#10;        for i in range(len(word)):&#10;            for c in &#x27;abcdefghijklmnopqrstuvwxyz&#x27;:&#10;                newWord = word[:i] + c + word[i+1:]&#10;                if newWord in wordSet:&#10;                    wordSet.remove(newWord)&#10;                    q.append(newWord)&#10;                    mpp[newWord] = steps + 1&#10;    ans = []&#10;    if endWord in mpp:&#10;        def dfs(word, seq):&#10;            if word == beginWord:&#10;                ans.append(seq[::-1])&#10;                return&#10;            steps = mpp[word]&#10;            for i in range(len(word)):&#10;                for c in &#x27;abcdefghijklmnopqrstuvwxyz&#x27;:&#10;                    newWord = word[:i] + c + word[i+1:]&#10;                    if newWord in mpp and mpp[newWord] == steps - 1:&#10;                        dfs(newWord, seq + [newWord])&#10;        dfs(endWord, [endWord])&#10;    return ans</code></pre></details></td>
    </tr>
    <tr>
      <td>52</td>
      <td>Graph 53 Making A Large Island<br><br></b> <a href='https://leetcode.com/problems/making-a-large-island/' target='_blank'>LeetCode 827</a></td>
      <td><b>Example 1:</b> Disjoint Set / Union Find.</td>
      <td><b>Time:</b> O(N^2)<br><b>Space:</b> O(N^2)</td>
      <td>-</td>
      <td>-</td>
      <td><b>Explanation:</b> Step 1: Traverse the grid. For each `1`, union it with its `1` neighbors. Calculate the size of each component using DSU. Step 2: Traverse again. For each `0`, check its 4 neighbors. Find unique ultimate parents among neighbors, sum their sizes, and add 1 (for the flipped `0`). Keep track of the maximum size found.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python"># Uses DSU with rank/size&#10;def largestIsland(grid: List[List[int]]) -&gt; int:&#10;    n = len(grid)&#10;    ds = DisjointSet(n * n)&#10;    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]&#10;    for r in range(n):&#10;        for c in range(n):&#10;            if grid[r][c] == 0: continue&#10;            for i in range(4):&#10;                nr, nc = r + dr[i], c + dc[i]&#10;                if 0 &lt;= nr &lt; n and 0 &lt;= nc &lt; n and grid[nr][nc] == 1:&#10;                    ds.union(r * n + c, nr * n + nc)&#10;    mx = 0&#10;    for r in range(n):&#10;        for c in range(n):&#10;            if grid[r][c] == 1: continue&#10;            components = set()&#10;            for i in range(4):&#10;                nr, nc = r + dr[i], c + dc[i]&#10;                if 0 &lt;= nr &lt; n and 0 &lt;= nc &lt; n and grid[nr][nc] == 1:&#10;                    components.add(ds.find(nr * n + nc))&#10;            sizeTotal = sum(ds.size[root] for root in components)&#10;            mx = max(mx, sizeTotal + 1)&#10;    for cell in range(n * n):&#10;        mx = max(mx, ds.size[ds.find(cell)])&#10;    return mx</code></pre></details></td>
    </tr>
    <tr>
      <td>53</td>
      <td>Graph 54 Swim In Rising Water<br><br></b> <a href='https://leetcode.com/problems/swim-in-rising-water/' target='_blank'>LeetCode 778</a></td>
      <td><b>Example 1:</b> Dijkstra's Algorithm with Max Path Edge.</td>
      <td><b>Time:</b> O(N^2 log N)<br><b>Space:</b> O(N^2)</td>
      <td><code>#include <queue></code></td>
      <td>-</td>
      <td><b>Explanation:</b> Use a priority queue to always process the cell with the minimum maximum-elevation so far. `pq` stores `(max_elev_in_path, r, c)`. Push `(grid[0][0], 0, 0)`. While pq is not empty, pop the minimum. If we reach `(n-1, n-1)`, return the `max_elev`. For each neighbor, the new max elevation is `max(max_elev, grid[nr][nc])`. Push to pq if not visited.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">import heapq&#10;def swimInWater(grid: List[List[int]]) -&gt; int:&#10;    n = len(grid)&#10;    pq = [(grid[0][0], 0, 0)]&#10;    vis = [[0] * n for _ in range(n)]&#10;    vis[0][0] = 1&#10;    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]&#10;    while pq:&#10;        t, r, c = heapq.heappop(pq)&#10;        if r == n - 1 and c == n - 1: return t&#10;        for i in range(4):&#10;            nr, nc = r + dr[i], c + dc[i]&#10;            if 0 &lt;= nr &lt; n and 0 &lt;= nc &lt; n and not vis[nr][nc]:&#10;                vis[nr][nc] = 1&#10;                heapq.heappush(pq, (max(t, grid[nr][nc]), nr, nc))&#10;    return 0</code></pre></details></td>
    </tr>
  </tbody>
</table>
