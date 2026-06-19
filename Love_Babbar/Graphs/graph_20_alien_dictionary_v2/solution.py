# Time Complexity: O(N * L + K)
# Space Complexity: O(K)
# Explanation: Compare adjacent words in the sorted dictionary. The first differing character creates a directed edge `char1 -> char2` indicating `char1` comes before `char2`. Build a directed graph and perform Topological Sorting to get the order.

from collections import deque, defaultdict
def findOrder(dict_arr, N, K):
    adj = defaultdict(list)
    for i in range(N - 1):
        s1, s2 = dict_arr[i], dict_arr[i+1]
        for j in range(min(len(s1), len(s2))):
            if s1[j] != s2[j]:
                adj[ord(s1[j]) - ord('a')].append(ord(s2[j]) - ord('a'))
                break
    inDegree = [0] * K
    for i in range(K):
        for nbr in adj[i]:
            inDegree[nbr] += 1
    q = deque([i for i in range(K) if inDegree[i] == 0])
    ans = ""
    while q:
        node = q.popleft()
        ans += chr(node + ord('a'))
        for nbr in adj[node]:
            inDegree[nbr] -= 1
            if inDegree[nbr] == 0: q.append(nbr)
    return ans

