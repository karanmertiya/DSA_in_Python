# Time Complexity: O(N log K)
# Space Complexity: O(K)
# Explanation: Use a max-heap of size K to store `(distance_squared, index)`. For each point, if the heap size is < K, push it. Otherwise, if its distance is less than the max-heap's top distance, pop the top and push the new point.

import heapq
def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    pq = []
    for i, (x, y) in enumerate(points):
        dist = -(x*x + y*y)
        if len(pq) < k:
            heapq.heappush(pq, (dist, i))
        else:
            heapq.heappushpop(pq, (dist, i))
    return [points[i] for _, i in pq]

