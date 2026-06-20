# Time Complexity: O(1)
# Space Complexity: O(1)
# Explanation: The number of perfect squares less than `N` is equal to `sqrt(N - 1)` rounded down.

import math
def countSquares(N):
    return int(math.sqrt(N - 1))

