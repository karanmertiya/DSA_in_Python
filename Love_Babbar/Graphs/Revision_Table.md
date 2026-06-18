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
  </tbody>
</table>
