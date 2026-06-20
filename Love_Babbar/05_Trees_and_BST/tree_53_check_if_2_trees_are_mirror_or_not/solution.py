# Time Complexity: O(E)
# Space Complexity: O(E)
# Explanation: Store the children of the first tree in a stack (LIFO) and the children of the second tree in a queue (FIFO) for each node using hash maps. Then compare if the stack top matches the queue front for all nodes.

import collections
def checkMirrorTree(n, e, A, B):
    s = collections.defaultdict(list)
    q = collections.defaultdict(collections.deque)
    for i in range(0, 2 * e, 2):
        s[A[i]].append(A[i+1])
        q[B[i]].append(B[i+1])
    for node in s:
        while s[node] and q[node]:
            if s[node][-1] != q[node][0]: return 0
            s[node].pop()
            q[node].popleft()
        if s[node] or q[node]: return 0
    return 1

