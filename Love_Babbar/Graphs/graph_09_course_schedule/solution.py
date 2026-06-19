# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
# Explanation: Kahn's BFS or DFS cycle detection. Here Kahn's BFS is used. If topological sort contains all V vertices, then true.

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    from collections import deque
    adj = [[] for _ in range(numCourses)]
    indegree = [0]*numCourses
    for dest, src in prerequisites:
        adj[src].append(dest)
        indegree[dest] += 1
    q = deque([i for i in range(numCourses) if indegree[i] == 0])
    count = 0
    while q:
        node = q.popleft()
        count += 1
        for nxt in adj[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0: q.append(nxt)
    return count == numCourses

