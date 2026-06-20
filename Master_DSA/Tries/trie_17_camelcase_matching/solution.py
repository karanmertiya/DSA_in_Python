# Time Complexity: O(N * M)
# Space Complexity: O(1) excluding output
# Explanation: Build a Trie with the queries (optional, can also be done linearly). Better approach: for each query, match characters with pattern. If characters match, increment pattern index. If characters mismatch and query character is uppercase, it's a mismatch. Finally, check if pattern index reached pattern length.

def camelMatch(queries, pattern):
    ans = []
    for q in queries:
        i = 0
        match = True
        for c in q:
            if i < len(pattern) and c == pattern[i]: i += 1
            elif c.isupper():
                match = False
                break
        if i < len(pattern): match = False
        ans.append(match)
    return ans

