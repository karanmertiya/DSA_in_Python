# Time Complexity: O(32) &cong; O(1) (Trade-off)
# Space Complexity: O(1)
# Explanation: Iterate through all 32 bits and check if each is set.

def hamming_weight(n: int) -> int:
    count = 0
    while n:
        n &= (n - 1)
        count += 1
    return count

