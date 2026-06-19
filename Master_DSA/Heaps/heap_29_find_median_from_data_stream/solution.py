# Time Complexity: O(log N) add, O(1) find
# Space Complexity: O(N)
# Explanation: Use two heaps: a max-heap for the smaller half of numbers, and a min-heap for the larger half. Keep the sizes balanced (either equal, or max-heap has 1 more). Median is root of max-heap (odd total) or average of both roots (even total).

import heapq
class MedianFinder:
    def __init__(self):
        self.small, self.large = [], []
    def addNum(self, num: int) -> None:
        heapq.heappush(self.large, num)
        heapq.heappush(self.small, -heapq.heappop(self.large))
        if len(self.small) > len(self.large):
            heapq.heappush(self.large, -heapq.heappop(self.small))
    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return self.large[0]
        return (self.large[0] - self.small[0]) / 2

