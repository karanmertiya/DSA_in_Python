# Time Complexity: O(V^3)
# Space Complexity: O(V^2)
# Explanation: Use Floyd-Warshall to find shortest paths between all pairs of nodes. For each city, count the number of reachable cities within `distanceThreshold`. Return the city with the minimum count (and greatest ID on tie).

def findTheCity(n: int, edges: List[List[int]], distanceThreshold: int) -> int:
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n): dist[i][i] = 0
    for u, v, w in edges:
        dist[u][v] = w
        dist[v][u] = w
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    minCities = n
    ansCity = -1
    for i in range(n):
        cnt = sum(1 for j in range(n) if dist[i][j] <= distanceThreshold)
        if cnt <= minCities:
            minCities = cnt
            ansCity = i
    return ansCity

