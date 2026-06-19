# Time Complexity: O(log N) add, O(1) find
# Space Complexity: O(N)
# Explanation: Maintain two heaps: a max-heap for the smaller half of the numbers, and a min-heap for the larger half. Ensure the max-heap has either the same size or one more element than the min-heap. The median is either the top of the max-heap or the average of the tops.

import heapq
class MedianFinder:
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
    def addNum(self, num: int) -> None:
        if not self.maxHeap or num <= -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
        elif len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2.0
        return -self.maxHeap[0]

