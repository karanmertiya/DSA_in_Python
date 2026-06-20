# Time Complexity: O(N^2)
# Space Complexity: O(N^2)
# Explanation: To find all substrings, iterate `i` from 0 to N-1, and `j` from `i` to N-1. Each sequence `s[i...j]` is a substring. Insert it into the Trie. Every time we create a new node, it corresponds to a new distinct substring. Increment count. Add 1 for the empty substring.

class Node:
    def __init__(self):
        self.links = [None] * 26
    def containsKey(self, ch):
        return self.links[ord(ch) - ord('a')] is not None
    def put(self, ch, node):
        self.links[ord(ch) - ord('a')] = node
    def get(self, ch):
        return self.links[ord(ch) - ord('a')]
def countDistinctSubstrings(s: str) -> int:
    root = Node()
    count = 0
    for i in range(len(s)):
        node = root
        for j in range(i, len(s)):
            if not node.containsKey(s[j]):
                node.put(s[j], Node())
                count += 1
            node = node.get(s[j])
    return count + 1

