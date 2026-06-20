# Time Complexity: O(N * Len + K + E)
# Space Complexity: O(K + E)
# Explanation: Create a DAG based on mismatching characters between adjacent words. Use Kahn's algorithm (Topological Sort BFS) to find the character order.

def findOrder(dict: List[str], N: int, K: int) -> str:
    adj = [[] for _ in range(K)]
    for i in range(N - 1):
        s1, s2 = dict[i], dict[i+1]
        for j in range(min(len(s1), len(s2))):
            if s1[j] != s2[j]:
                adj[ord(s1[j]) - ord('a')].append(ord(s2[j]) - ord('a'))
                break
    indegree = [0] * K
    for i in range(K):
        for it in adj[i]: indegree[it] += 1
    q = [i for i in range(K) if indegree[i] == 0]
    topo = []
    while q:
        node = q.pop(0)
        topo.append(chr(node + ord('a')))
        for it in adj[node]:
            indegree[it] -= 1
            if indegree[it] == 0: q.append(it)
    return ''.join(topo)

