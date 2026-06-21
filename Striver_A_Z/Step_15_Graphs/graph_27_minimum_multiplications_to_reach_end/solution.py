# Time Complexity: O(100000 * N)
# Space Complexity: O(100000)
# Explanation: Since each multiplication is 1 step, we can use BFS. The 'nodes' are values from 0 to 99999. Use an array `dist` initialized to infinity. Push `start` to queue. For each popped node, multiply by all array elements `% 100000`. If we find a shorter path, push to queue.

import collections
def minimumMultiplications(arr: List[int], start: int, end: int) -> int:
    if start == end: return 0
    q = collections.deque([(start, 0)])
    dist = [float('inf')] * 100000
    dist[start] = 0
    mod = 100000
    while q:
        node, steps = q.popleft()
        for it in arr:
            num = (node * it) % mod
            if steps + 1 < dist[num]:
                dist[num] = steps + 1
                if num == end: return steps + 1
                q.append((num, steps + 1))
    return -1

