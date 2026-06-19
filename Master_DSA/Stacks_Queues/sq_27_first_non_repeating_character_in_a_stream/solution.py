# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Use a frequency array or hash map to count character occurrences. Use a queue to maintain the order of characters. When a character arrives, increment its count and push to queue. While the queue is not empty and the front element's count > 1, pop it. The front is the answer.

from collections import deque
def FirstNonRepeating(A):
    count = {}
    q = deque()
    ans = []
    for char in A:
        count[char] = count.get(char, 0) + 1
        q.append(char)
        while q:
            if count[q[0]] > 1: q.popleft()
            else:
                ans.append(q[0])
                break
        if not q: ans.append('#')
    return "".join(ans)

