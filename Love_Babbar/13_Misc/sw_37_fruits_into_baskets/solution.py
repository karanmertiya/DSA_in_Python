# Time Complexity: O(N)
# Space Complexity: O(1) (at most 3 elements in map)
# Explanation: This translates to finding the longest subarray with at most 2 distinct elements. Maintain a frequency map and use a sliding window. If distinct elements > 2, shrink the window until distinct elements <= 2.

import collections
def totalFruit(fruits: List[int]) -> int:
    count = collections.defaultdict(int)
    l = maxFruits = 0
    for r in range(len(fruits)):
        count[fruits[r]] += 1
        while len(count) > 2:
            count[fruits[l]] -= 1
            if count[fruits[l]] == 0:
                del count[fruits[l]]
            l += 1
        maxFruits = max(maxFruits, r - l + 1)
    return maxFruits

