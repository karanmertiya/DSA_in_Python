# Time Complexity: O(N log N + Q log Q + Q * 32 + N * 32)
# Space Complexity: O(N * 32 + Q)
# Explanation: Sort `nums` array. Store queries as `{m, x, index}` and sort them by `m`. Iterate through queries. While `nums[i] <= m`, insert `nums[i]` into Trie. If Trie is empty, answer is -1. Else, query Trie for max XOR with `x`.

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
            if not node.containsKey(bit): node.put(bit, Node())
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
def maximizeXor(nums: List[int], queries: List[List[int]]) -> List[int]:
    nums.sort()
    oQ = sorted([(q[1], q[0], i) for i, q in enumerate(queries)])
    ans = [0] * len(queries)
    trie = Trie()
    ind = 0
    for m, x, qInd in oQ:
        while ind < len(nums) and nums[ind] <= m:
            trie.insert(nums[ind])
            ind += 1
        if ind == 0: ans[qInd] = -1
        else: ans[qInd] = trie.getMax(x)
    return ans

