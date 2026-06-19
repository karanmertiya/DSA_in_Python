# Time Complexity: O(N log K)
# Space Complexity: O(N)
# Explanation: Count frequencies using a hash map. Maintain a min-heap of size K storing `(frequency, element)`. Push each pair into the heap. If size > K, pop. The remaining elements in the heap are the top K frequent.

import collections, heapq
def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = collections.Counter(nums)
    pq = []
    for num, freq in count.items():
        heapq.heappush(pq, (freq, num))
        if len(pq) > k:
            heapq.heappop(pq)
    return [num for freq, num in pq]

