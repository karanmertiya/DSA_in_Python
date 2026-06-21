# Time Complexity: O(N * 32)
# Space Complexity: O(N * 32)
# Explanation: Insert binary representation of each number (from MSB to LSB, 31 to 0) into a Trie. To find max XOR for `x`, traverse the Trie aiming for opposite bits (1 for 0, 0 for 1). If opposite bit exists, go that way and add `1 << i` to result. Else go same way.

class Node:
    def __init__(self):
        self.links = [None, None]
    def containsKey(self, bit): return self.links[bit] is not None
    def put(self, bit, node): self.links[bit] = node
    def get(self, bit): return self.links[bit]
class Trie:
    def __init__(self):
        self.root = Node()
    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if not node.containsKey(bit):
                node.put(bit, Node())
            node = node.get(bit)
    def getMax(self, num):
        node = self.root
        maxNum = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if node.containsKey(1 - bit):
                maxNum |= (1 << i)
                node = node.get(1 - bit)
            else:
                node = node.get(bit)
        return maxNum
def findMaximumXOR(nums: List[int]) -> int:
    trie = Trie()
    for num in nums: trie.insert(num)
    maxi = 0
    for num in nums:
        maxi = max(maxi, trie.getMax(num))
    return maxi

