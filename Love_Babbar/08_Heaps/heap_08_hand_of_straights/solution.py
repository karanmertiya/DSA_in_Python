# Time Complexity: O(N log N)
# Space Complexity: O(N)
# Explanation: Use a map (TreeMap in C++) to store frequencies. Iterate through map. If a number has count > 0, we must form a group starting from it. Decrement counts of `num, num+1, ..., num+groupSize-1`.

import collections
def isNStraightHand(hand: List[int], groupSize: int) -> bool:
    if len(hand) % groupSize != 0: return False
    count = collections.Counter(hand)
    for card in sorted(count.keys()):
        if count[card] > 0:
            c = count[card]
            for i in range(groupSize):
                if count[card + i] < c: return False
                count[card + i] -= c
    return True

