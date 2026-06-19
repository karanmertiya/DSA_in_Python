# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Use a hash map to store the frequencies of the elements seen so far. For each element `x`, check if `K - x` is in the hash map. If it is, add its frequency to the `count`. Finally, increment the frequency of `x` in the hash map.

import collections
def getPairsCount(arr: List[int], n: int, k: int) -> int:
    m = collections.defaultdict(int)
    count = 0
    for x in arr:
        if k - x in m:
            count += m[k - x]
        m[x] += 1
    return count

