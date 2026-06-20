# Time Complexity: O(N^2) or worse
# Space Complexity: O(N) or O(1)
# Explanation: Brute Force: Standard unoptimized approach. (TODO: Implement specific logic)

# TODO: Implement Brute Force
import math
def countSquares(N):
    return int(math.sqrt(N - 1))

# Time Complexity: O(1)
# Space Complexity: O(1)
# Explanation: Optimal: The number of perfect squares less than `N` is equal to `sqrt(N - 1)` rounded down.

import math
def countSquares(N):
    return int(math.sqrt(N - 1))

