# Time Complexity: O(N log N)
# Space Complexity: O(1)
# Explanation: This is exactly the Activity Selection Problem. Sort the pairs by their second element. Iterate through the sorted pairs and keep track of the end of the last selected pair. If the next pair's start is > last end, select it.

class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b
def maxChainLen(Parr, n):
    Parr.sort(key=lambda x: x.b)
    count = 1
    last_end = Parr[0].b
    for i in range(1, n):
        if Parr[i].a > last_end:
            count += 1
            last_end = Parr[i].b
    return count

