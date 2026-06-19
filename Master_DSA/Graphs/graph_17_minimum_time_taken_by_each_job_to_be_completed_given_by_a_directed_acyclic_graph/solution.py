# Time Complexity: O(V + E)
# Space Complexity: O(V)
# Explanation: Use Kahn's Algorithm. All nodes with indegree 0 take 1 unit of time. For other nodes `V`, when they are pushed to the queue from `U`, their time is `time[U] + 1`.

def minimumTime(n: int, edges: List[List[int]], m: int) -> List[int]:
    adj = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    for u, v in edges:
        adj[u].append(v)
        indegree[v] += 1
    q = collections.deque()
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            ans[i] = 1
    while q:
        node = q.popleft()
        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                ans[neighbor] = ans[node] + 1
                q.append(neighbor)
    return ans[1:]

