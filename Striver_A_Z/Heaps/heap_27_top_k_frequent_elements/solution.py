# Time Complexity: O(N log K) Heap, O(N) Bucket Sort
# Space Complexity: O(N)
# Explanation: Count frequencies using a hash map. Use a min-heap of size `k` storing pairs of `(frequency, element)`. Or use bucket sort where index is frequency and value is list of elements with that frequency.

import collections
import heapq
def topKFrequent(nums: List[int], k: int) -> List[int]:
    counts = collections.Counter(nums)
    return heapq.nlargest(k, counts.keys(), key=counts.get)

