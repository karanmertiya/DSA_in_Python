# Time Complexity: O(N log N * alpha(N)) where N is total emails
# Space Complexity: O(N)
# Explanation: Map each email to an account index. If an email is seen again, union the current account index with the previously mapped account index. Finally, group emails by their root account index, sort them, and attach the name.

def accountsMerge(accounts: List[List[str]]) -> List[List[str]]:
    n = len(accounts)
    parent = list(range(n))
    def find(i):
        if parent[i] == i: return i
        parent[i] = find(parent[i])
        return parent[i]
    def union(i, j):
        root_i, root_j = find(i), find(j)
        if root_i != root_j: parent[root_i] = root_j
    email_to_id = {}
    for i, acc in enumerate(accounts):
        for email in acc[1:]:
            if email in email_to_id:
                union(i, email_to_id[email])
            else:
                email_to_id[email] = i
    id_to_emails = collections.defaultdict(list)
    for email, i in email_to_id.items():
        id_to_emails[find(i)].append(email)
    ans = []
    for i, emails in id_to_emails.items():
        ans.append([accounts[i][0]] + sorted(emails))
    return ans

