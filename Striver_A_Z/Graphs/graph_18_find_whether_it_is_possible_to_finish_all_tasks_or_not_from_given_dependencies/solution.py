# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
# Explanation: This is equivalent to detecting a cycle in a directed graph. If a cycle exists, it's impossible. Use Kahn's algorithm: if the number of elements in the topological sort is not equal to `N`, then a cycle exists.

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    adj = [[] for _ in range(numCourses)]
    for u, v in prerequisites:
        adj[v].append(u)
    indegree = [0] * numCourses
    for i in range(numCourses):
        for node in adj[i]:
            indegree[node] += 1
    q = collections.deque()
    for i in range(numCourses):
        if indegree[i] == 0:
            q.append(i)
    cnt = 0
    while q:
        node = q.popleft()
        cnt += 1
        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)
    return cnt == numCourses

