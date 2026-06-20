# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Use a queue to maintain the order of characters and an array to keep track of their frequencies. For each character, increment its frequency and push it to the queue. Then, while the queue is not empty and the frequency of the front character is greater than 1, pop it. If the queue is empty, append '#', else append the front character.

import collections
def FirstNonRepeating(A: str) -> str:
    freq = [0] * 26
    q = collections.deque()
    res = []
    for c in A:
        freq[ord(c) - ord('a')] += 1
        q.append(c)
        while q and freq[ord(q[0]) - ord('a')] > 1:
            q.popleft()
        if not q: res.append('#')
        else: res.append(q[0])
    return "".join(res)

