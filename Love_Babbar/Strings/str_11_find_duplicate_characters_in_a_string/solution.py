# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Use a hash map or frequency array to count occurrences of each character. Then, iterate through the map/array and print characters with a count greater than 1.

import collections
def printDups(s: str):
    count = collections.Counter(s)
    for k, v in count.items():
        if v > 1:
            print(f"{k}, count = {v}")

