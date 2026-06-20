# Time Complexity: O(N log K)
# Space Complexity: O(K)
# Explanation: Use a max-heap of size `k` to store pairs of `(distance, point_index)`. Iterate over all points, push into heap. If heap size exceeds `k`, pop the max element. The heap will eventually hold the `k` points with minimum distance.

import heapq
def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    heap = []
    for i, (x, y) in enumerate(points):
        dist = -(x*x + y*y)
        if len(heap) < k:
            heapq.heappush(heap, (dist, i))
        else:
            heapq.heappushpop(heap, (dist, i))
    return [points[i] for _, i in heap]

