# Time Complexity: O(N * M * log(N * M)) where N=accounts, M=max emails
# Space Complexity: O(N * M)
# Explanation: Create a DSU of size N (number of accounts). Map each email to its first seen account ID. If an email is seen again, union the current account ID with the mapped account ID. Then group emails by the ultimate parent of their account ID. Sort emails in each group and format the result.

import collections
def accountsMerge(accounts: List[List[str]]) -> List[List[str]]:
    n = len(accounts)
    ds = DisjointSet(n)
    mailNode = {}
    for i in range(n):
        for j in range(1, len(accounts[i])):
            mail = accounts[i][j]
            if mail not in mailNode:
                mailNode[mail] = i
            else:
                ds.union(i, mailNode[mail])
    mergedMails = collections.defaultdict(list)
    for mail, node in mailNode.items():
        root = ds.find(node)
        mergedMails[root].append(mail)
    ans = []
    for i in range(n):
        if i not in mergedMails: continue
        ans.append([accounts[i][0]] + sorted(mergedMails[i]))
    return ans

