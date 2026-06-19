# Time Complexity: O(N log A)
# Space Complexity: O(A)
# Explanation: Count character frequencies. Use a max-heap to store (count, char). Pop the top two most frequent characters, append them to the result, decrement their counts, and push them back if count > 0. If one character is left and its count > 1, it's impossible.

import collections, heapq
def reorganizeString(s: str) -> str:
    count = collections.Counter(s)
    pq = [(-freq, char) for char, freq in count.items()]
    heapq.heapify(pq)
    res = ""
    while len(pq) > 1:
        freq1, char1 = heapq.heappop(pq)
        freq2, char2 = heapq.heappop(pq)
        res += char1 + char2
        if freq1 < -1: heapq.heappush(pq, (freq1 + 1, char1))
        if freq2 < -1: heapq.heappush(pq, (freq2 + 1, char2))
    if pq:
        freq, char = pq[0]
        if freq < -1: return ""
        res += char
    return res

