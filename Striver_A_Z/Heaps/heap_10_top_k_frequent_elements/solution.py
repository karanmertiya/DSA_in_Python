# Time Complexity: O(N log K)
# Space Complexity: O(N)
# Explanation: Count frequencies using a map. Use a Min-Heap of size K, storing pairs `(freq, num)`. If size > K, pop. Heap will contain the top K elements.

import collections, heapq
def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = collections.Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)

