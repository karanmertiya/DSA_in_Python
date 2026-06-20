# Time Complexity: O(V + E) (Constraint)
# Space Complexity: O(V + E)
# Explanation: Kahn's Algorithm (BFS). Count in-degrees. Add courses with 0 in-degree to queue. Process queue, reducing in-degrees of neighbors.

from collections import deque
def can_finish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    adj = {i: [] for i in range(numCourses)}
    indegree = [0] * numCourses
    for crs, pre in prerequisites:
        adj[pre].append(crs)
        indegree[crs] += 1
    q = deque([i for i in range(numCourses) if indegree[i] == 0])
    count = 0
    while q:
        node = q.popleft()
        count += 1
        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)
    return count == numCourses

