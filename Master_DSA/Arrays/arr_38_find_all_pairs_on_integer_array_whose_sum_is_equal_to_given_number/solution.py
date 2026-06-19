# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Use a hash map to store frequencies. For each element `num`, check if `K - num` exists in the map. If so, add its frequency to the count. Then increment the frequency of `num` in the map.

import collections
def getPairsCount(arr, n, k):
    m = collections.defaultdict(int)
    count = 0
    for num in arr:
        if (k - num) in m:
            count += m[k - num]
        m[num] += 1
    return count

