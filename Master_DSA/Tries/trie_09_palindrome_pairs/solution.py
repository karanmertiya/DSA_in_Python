# Time Complexity: O(N * L^2)
# Space Complexity: O(N * L)
# Explanation: Insert the REVERSE of every word into a Trie. Store index of word at node. For each word, search the Trie. Three cases: 1. Trie word is longer (current word exhausted, check if rest of Trie branch is palindrome). 2. Current word is longer (Trie exhausted, check if rest of current word is palindrome). 3. Exact match. Store valid indices.

class Node:
    def __init__(self):
        self.links = [None] * 26
        self.idx = -1
        self.pal_indices = []
def is_pal(s, i, j):
    while i < j:
        if s[i] != s[j]: return False
        i += 1; j -= 1
    return True
def palindromePairs(words: List[str]) -> List[List[int]]:
    root = Node()
    for i, w in enumerate(words):
        node = root
        for j in range(len(w) - 1, -1, -1):
            if is_pal(w, 0, j): node.pal_indices.append(i)
            idx = ord(w[j]) - 97
            if not node.links[idx]: node.links[idx] = Node()
            node = node.links[idx]
        node.idx = i
        node.pal_indices.append(i)
    res = []
    for i, w in enumerate(words):
        node = root
        valid = True
        for j in range(len(w)):
            if node.idx != -1 and node.idx != i and is_pal(w, j, len(w)-1):
                res.append([i, node.idx])
            idx = ord(w[j]) - 97
            if not node.links[idx]:
                valid = False
                break
            node = node.links[idx]
        if valid:
            for pid in node.pal_indices:
                if i != pid: res.append([i, pid])
    return res

