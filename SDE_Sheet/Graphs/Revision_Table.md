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
      <td rowspan="1">1</td>
      <td rowspan="1">Graph 01 Number Of Islands<br><br></b> <a href='https://leetcode.com/problems/number-of-islands/' target='_blank'>LeetCode 200</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]], Output: 3</td>
      <td><b>Time:</b> O(M * N) (Constraint)<br><b>Space:</b> O(M * N) (Constraint)</td>
      <td>-</td>
      <td><b>In-place Visited Check:</b> Sinking the island by changing '1' to '0' avoids needing a separate `visited` matrix.</td>
      <td><b>Explanation:</b> Iterate through the grid. When a '1' is found, increment island count and use DFS to sink the island (turn connected '1's to '0's).<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def num_islands(grid: list[list[str]]) -&gt; int:&#10;    if not grid: return 0&#10;    def dfs(i, j):&#10;        if i &lt; 0 or i &gt;= len(grid) or j &lt; 0 or j &gt;= len(grid[0]) or grid[i][j] == &#x27;0&#x27;:&#10;            return&#10;        grid[i][j] = &#x27;0&#x27;&#10;        dfs(i+1, j); dfs(i-1, j); dfs(i, j+1); dfs(i, j-1)&#10;    count = 0&#10;    for i in range(len(grid)):&#10;        for j in range(len(grid[0])):&#10;            if grid[i][j] == &#x27;1&#x27;:&#10;                count += 1&#10;                dfs(i, j)&#10;    return count</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">2</td>
      <td rowspan="1">Graph 02 Course Schedule<br><br></b> <a href='https://leetcode.com/problems/course-schedule/' target='_blank'>LeetCode 207</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: numCourses = 2, prerequisites = [[1,0]], Output: true</td>
      <td><b>Time:</b> O(V + E) (Constraint)<br><b>Space:</b> O(V + E)</td>
      <td><code>std::queue</code></td>
      <td><b>Graph Building:</b> Convert `prerequisites` edge list into an Adjacency List for fast neighbor lookups.</td>
      <td><b>Explanation:</b> Kahn's Algorithm (BFS). Count in-degrees. Add courses with 0 in-degree to queue. Process queue, reducing in-degrees of neighbors.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">from collections import deque&#10;def can_finish(numCourses: int, prerequisites: list[list[int]]) -&gt; bool:&#10;    adj = {i: [] for i in range(numCourses)}&#10;    indegree = [0] * numCourses&#10;    for crs, pre in prerequisites:&#10;        adj[pre].append(crs)&#10;        indegree[crs] += 1&#10;    q = deque([i for i in range(numCourses) if indegree[i] == 0])&#10;    count = 0&#10;    while q:&#10;        node = q.popleft()&#10;        count += 1&#10;        for neighbor in adj[node]:&#10;            indegree[neighbor] -= 1&#10;            if indegree[neighbor] == 0:&#10;                q.append(neighbor)&#10;    return count == numCourses</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">3</td>
      <td rowspan="1">Graph 03 Rotting Oranges<br><br></b> <a href='https://leetcode.com/problems/rotting-oranges/' target='_blank'>LeetCode 994</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: grid = [[2,1,1],[1,1,0],[0,1,1]], Output: 4</td>
      <td><b>Time:</b> O(M * N)<br><b>Space:</b> O(M * N)</td>
      <td><code>std::queue</code></td>
      <td><b>Unreachable Oranges:</b> Track total fresh oranges initially. If remaining fresh > 0 after BFS, return -1.</td>
      <td><b>Explanation:</b> Multi-source BFS. Put all initially rotten oranges in queue. Process level by level.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">from collections import deque&#10;def orangesRotting(grid: list[list[int]]) -&gt; int:&#10;    q = deque()&#10;    fresh = 0&#10;    for i in range(len(grid)):&#10;        for j in range(len(grid[0])):&#10;            if grid[i][j] == 2: q.append((i, j))&#10;            elif grid[i][j] == 1: fresh += 1&#10;    time = 0&#10;    dirs = [(1,0), (-1,0), (0,1), (0,-1)]&#10;    while q and fresh &gt; 0:&#10;        for _ in range(len(q)):&#10;            r, c = q.popleft()&#10;            for dr, dc in dirs:&#10;                nr, nc = r + dr, c + dc&#10;                if 0 &lt;= nr &lt; len(grid) and 0 &lt;= nc &lt; len(grid[0]) and grid[nr][nc] == 1:&#10;                    grid[nr][nc] = 2&#10;                    q.append((nr, nc))&#10;                    fresh -= 1&#10;        time += 1&#10;    return time if fresh == 0 else -1</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">4</td>
      <td rowspan="1">Graph 04 Bipartite Graph<br><br></b> <a href='https://leetcode.com/problems/is-graph-bipartite/' target='_blank'>LeetCode 785</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]], Output: false</td>
      <td><b>Time:</b> O(V + E)<br><b>Space:</b> O(V)</td>
      <td><code>std::queue</code></td>
      <td><b>Disconnected Graph:</b> Must loop over all nodes `0` to `V-1` to ensure every disconnected component is checked.</td>
      <td><b>Explanation:</b> BFS/DFS coloring approach. Color adjacent nodes with alternate colors (0 and 1). If an adjacent node has the SAME color, it's not bipartite.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">from collections import deque&#10;def isBipartite(graph: list[list[int]]) -&gt; bool:&#10;    n = len(graph)&#10;    color = [-1] * n&#10;    for i in range(n):&#10;        if color[i] != -1: continue&#10;        q = deque([i])&#10;        color[i] = 0&#10;        while q:&#10;            node = q.popleft()&#10;            for neighbor in graph[node]:&#10;                if color[neighbor] == -1:&#10;                    color[neighbor] = 1 - color[node]&#10;                    q.append(neighbor)&#10;                elif color[neighbor] == color[node]:&#10;                    return False&#10;    return True</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">5</td>
      <td rowspan="1">Graph 06 Dijkstras Algorithm<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1' target='_blank'>GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Source = 0, Output: distances array.</td>
      <td><b>Time:</b> O(E log V)<br><b>Space:</b> O(V)</td>
      <td><code>#include &lt;queue&gt;</code></td>
      <td><b>Disconnected graph:</b> Distances remain infinity.</td>
      <td><b>Explanation:</b> Min-heap (priority queue) to repeatedly extract the node with the minimum distance and relax its neighbors.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def dijkstra(V: int, adj: List[List[List[int]]], S: int) -&gt; List[int]:&#10;    import heapq&#10;    dist = [float(&#x27;inf&#x27;)] * V&#10;    dist[S] = 0&#10;    pq = [(0, S)]&#10;    while pq:&#10;        d, node = heapq.heappop(pq)&#10;        if d &gt; dist[node]: continue&#10;        for nxt, weight in adj[node]:&#10;            if d + weight &lt; dist[nxt]:&#10;                dist[nxt] = d + weight&#10;                heapq.heappush(pq, (dist[nxt], nxt))&#10;    return dist</code></pre></details></td>
    </tr>
    <tr>
      <td rowspan="1">6</td>
      <td rowspan="1">Graph 07 Topological Sort<br><br></b> <a href='https://practice.geeksforgeeks.org/problems/topological-sort/1' target='_blank'>GFG</a></td>
      <td rowspan="1"><b>Example 1:</b> Input: V = 4, adj = [[], [0], [0], [0]], Output: valid topological sort.</td>
      <td><b>Time:</b> O(V + E)<br><b>Space:</b> O(V)</td>
      <td><code>#include &lt;queue&gt;</code></td>
      <td><b>Cycles:</b> If cycle exists, result will not contain all V elements.</td>
      <td><b>Explanation:</b> Kahn's Algorithm (BFS) using in-degrees. Add nodes with 0 in-degree to a queue. Pop, append to result, and decrement in-degrees of neighbors.<br><br><details><summary><b>View Code</b></summary><pre style="white-space: pre-wrap; word-wrap: break-word;"><code class="language-python">def topoSort(V: int, adj: List[List[int]]) -&gt; List[int]:&#10;    from collections import deque&#10;    indegree = [0] * V&#10;    for i in range(V):&#10;        for nxt in adj[i]: indegree[nxt] += 1&#10;    q = deque([i for i in range(V) if indegree[i] == 0])&#10;    topo = []&#10;    while q:&#10;        node = q.popleft()&#10;        topo.append(node)&#10;        for nxt in adj[node]:&#10;            indegree[nxt] -= 1&#10;            if indegree[nxt] == 0: q.append(nxt)&#10;    return topo</code></pre></details></td>
    </tr>
  </tbody>
</table>
