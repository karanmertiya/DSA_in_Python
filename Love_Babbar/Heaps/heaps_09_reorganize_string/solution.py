# Time Complexity: O(N log 26)
# Space Complexity: O(26)
# Explanation: Count character frequencies. Use a Max Heap storing `(freq, char)`. Pop the top element, add it to the result, decrement its frequency, and temporarily store it (so it can't be picked in the next iteration). If the stored element has `freq > 0`, push it back. If the heap is empty but the stored element is not, it's impossible.

import collections, heapq
def reorganizeString(s):
    count = collections.Counter(s)
    pq = [[-freq, char] for char, freq in count.items()]
    heapq.heapify(pq)
    res = ""
    prev = None
    while pq:
        curr = heapq.heappop(pq)
        res += curr[1]
        curr[0] += 1
        if prev and prev[0] < 0: heapq.heappush(pq, prev)
        prev = curr
    return res if len(res) == len(s) else ""

