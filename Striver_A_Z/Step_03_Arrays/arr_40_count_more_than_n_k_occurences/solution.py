# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Optimal: Store the frequencies of all elements in a hash map. Iterate through the hash map and count the number of elements having frequency greater than `N/k`.

import collections
def countOccurence(arr, n, k):
    count = collections.Counter(arr)
    res = 0
    target = n // k
    for key, val in count.items():
        if val > target:
            res += 1
    return res

