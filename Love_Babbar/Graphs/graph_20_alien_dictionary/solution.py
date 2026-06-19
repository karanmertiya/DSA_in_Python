# Time Complexity: O(N * length of words + K)
# Space Complexity: O(K)
# Explanation: Compare adjacent words. The first mismatching character defines a directed edge `char1 -> char2`. Create an adjacency list of these edges. Then perform a topological sort to get the valid character order.

def findOrder(dict: List[str], N: int, K: int) -> str:
    adj = [[] for _ in range(K)]
    for i in range(N - 1):
        s1, s2 = dict[i], dict[i+1]
        for ptr in range(min(len(s1), len(s2))):
            if s1[ptr] != s2[ptr]:
                adj[ord(s1[ptr]) - ord('a')].append(ord(s2[ptr]) - ord('a'))
                break
    indegree = [0] * K
    for i in range(K):
        for node in adj[i]:
            indegree[node] += 1
    q = collections.deque()
    for i in range(K):
        if indegree[i] == 0:
            q.append(i)
    topo = ""
    while q:
        node = q.popleft()
        topo += chr(node + ord('a'))
        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)
    return topo

