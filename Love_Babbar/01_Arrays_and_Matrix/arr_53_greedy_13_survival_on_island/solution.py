# Time Complexity: O(N^2) or worse
# Space Complexity: O(N) or O(1)
# Explanation: Brute Force: Standard unoptimized approach. (TODO: Implement specific logic)

# TODO: Implement Brute Force
import math
def minimumDays(S, N, M):
    if M > N: return -1
    if S > 6 and (N * 6) < (M * 7): return -1
    return math.ceil((S * M) / N)

# Time Complexity: O(1)
# Space Complexity: O(1)
# Explanation: Optimal: If total required food > max food you can buy in S days excluding Sundays, return -1. Else, total required food is `S * M`. Minimum days = `ceil((S * M) / N)`. Also handle the edge case where `N < M` or if survival > 6 days and `(N * 6) < (M * 7)`.

import math
def minimumDays(S, N, M):
    if M > N: return -1
    if S > 6 and (N * 6) < (M * 7): return -1
    return math.ceil((S * M) / N)

