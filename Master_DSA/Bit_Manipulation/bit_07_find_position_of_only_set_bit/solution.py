# Time Complexity: O(32)
# Space Complexity: O(1)
# Explanation: Loop through all 32 bits, count set bits, and record the position. If count is strictly 1, return position, else -1.

def findPositionBrute(N: int) -> int:
    count, pos, curr = 0, -1, 1
    while N > 0:
        if N & 1:
            count += 1
            pos = curr
        N >>= 1
        curr += 1
    return pos if count == 1 else -1

# Time Complexity: O(1)
# Space Complexity: O(1)
# Explanation: First, check if `N` is a power of 2 using `N & (N - 1) == 0`. If yes, the position is `log2(N) + 1`.

import math
def findPosition(N: int) -> int:
    if N <= 0 or (N & (N - 1)) != 0: return -1
    return int(math.log2(N)) + 1

