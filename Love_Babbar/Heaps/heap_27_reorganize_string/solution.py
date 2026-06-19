# Time Complexity: O(N log(26))
# Space Complexity: O(26)
# Explanation: Count character frequencies. Push pairs `(freq, char)` to a max-heap. Pop two most frequent distinct characters, append to result, decrement frequencies, and push back if frequency > 0. If at the end one character remains with freq > 1, return empty string.

import collections
import heapq
def reorganizeString(s: str) -> str:
    count = collections.Counter(s)
    pq = [[-freq, char] for char, freq in count.items()]
    heapq.heapify(pq)
    res = []
    while len(pq) >= 2:
        freq1, char1 = heapq.heappop(pq)
        freq2, char2 = heapq.heappop(pq)
        res.extend([char1, char2])
        if freq1 < -1: heapq.heappush(pq, [freq1 + 1, char1])
        if freq2 < -1: heapq.heappush(pq, [freq2 + 1, char2])
    if pq:
        freq, char = pq[0]
        if freq < -1: return ""
        res.append(char)
    return "".join(res)

