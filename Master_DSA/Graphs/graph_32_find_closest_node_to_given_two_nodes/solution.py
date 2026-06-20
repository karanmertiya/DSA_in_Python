# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Run BFS from `node1` to get `dist1` array, and BFS from `node2` to get `dist2` array. Then iterate through all nodes `0` to `n-1`. For nodes reachable from both, compute `max(dist1[i], dist2[i])`. Return the node that minimizes this maximum distance. On tie, return the smallest index.

import collections
def closestMeetingNode(edges: List[int], node1: int, node2: int) -> int:
    def bfs(start):
        dist = [float('inf')] * len(edges)
        q = collections.deque([start])
        dist[start] = 0
        while q:
            node = q.popleft()
            nxt = edges[node]
            if nxt != -1 and dist[nxt] == float('inf'):
                dist[nxt] = dist[node] + 1
                q.append(nxt)
        return dist
    d1, d2 = bfs(node1), bfs(node2)
    min_dist, ans = float('inf'), -1
    for i in range(len(edges)):
        if d1[i] != float('inf') and d2[i] != float('inf'):
            mx = max(d1[i], d2[i])
            if mx < min_dist:
                min_dist = mx
                ans = i
    return ans

