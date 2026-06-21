# Time Complexity: O(N * 32)
# Space Complexity: O(N * 32)
# Explanation: Compute prefix XORs. For each prefix XOR `curr_xor`, insert it into a Trie. Then, query the Trie to find the maximum XOR of `curr_xor` with any previously inserted prefix XOR (by trying to follow the opposite bit path). The maximum value over all queries is the answer.

class Node:
    def __init__(self):
        self.links = [None, None]
class Trie:
    def __init__(self):
        self.root = Node()
    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if not node.links[bit]:
                node.links[bit] = Node()
            node = node.links[bit]
    def getMax(self, num):
        node = self.root
        maxNum = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if node.links[1 - bit]:
                maxNum |= (1 << i)
                node = node.links[1 - bit]
            else:
                node = node.links[bit]
        return maxNum
def maxSubarrayXOR(N, arr):
    trie = Trie()
    trie.insert(0)
    max_xor, curr_xor = float('-inf'), 0
    for num in arr:
        curr_xor ^= num
        trie.insert(curr_xor)
        max_xor = max(max_xor, trie.getMax(curr_xor))
    return max_xor

