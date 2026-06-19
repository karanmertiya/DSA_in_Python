# Time Complexity: O(N log K)
# Space Complexity: O(N)
# Explanation: Use a Hash Map to count frequencies. Use a Min-Heap of size `k` to keep track of the top `k` elements.

import heapq
from collections import Counter
def topKFrequent(nums: list[int], k: int) -> list[int]:
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)

