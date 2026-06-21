# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Find max frequency `max_f`. Calculate idle slots `(max_f - 1) * n`. Iterate remaining frequencies and subtract from idle slots. Return `tasks.length + max(0, idle_slots)`.

import collections
def leastInterval(tasks: List[str], n: int) -> int:
    counts = list(collections.Counter(tasks).values())
    max_f = max(counts)
    count_max = counts.count(max_f)
    ans = (max_f - 1) * (n + 1) + count_max
    return max(ans, len(tasks))

