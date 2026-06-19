# Time Complexity: O(N)
# Space Complexity: O(K)
# Explanation: Maintain a queue of negative integers in the current window. While moving the window, add new negative integers, remove old ones out of window. The front of queue is the first negative.

from collections import deque
def printFirstNegativeInteger(A, N, K):
    ans = []
    q = deque()
    for i in range(K - 1):
        if A[i] < 0: q.append(A[i])
    for i in range(K - 1, N):
        if A[i] < 0: q.append(A[i])
        ans.append(q[0] if q else 0)
        if A[i - K + 1] < 0 and q and q[0] == A[i - K + 1]: q.popleft()
    return ans

