# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
# Explanation: Since a path can revisit nodes and edges, the minimum score path from 1 to `n` is simply the minimum weight edge in the connected component containing node 1 and `n`. Perform BFS/DFS from node 1 and find the minimum edge weight in the entire component.

import collections
def minScore(n: int, roads: List[List[int]]) -> int:
    adj = collections.defaultdict(list)
    for u, v, w in roads:
        adj[u].append((v, w))
        adj[v].append((u, w))
    q = collections.deque([1])
    vis = set([1])
    min_score = float('inf')
    while q:
        node = q.popleft()
        for nxt, wt in adj[node]:
            min_score = min(min_score, wt)
            if nxt not in vis:
                vis.add(nxt)
                q.append(nxt)
    return min_score

