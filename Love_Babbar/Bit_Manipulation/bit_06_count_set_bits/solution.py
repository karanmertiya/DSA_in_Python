# Time Complexity: O(32) &cong; O(1) (Trade-off)
# Space Complexity: O(1)
# Explanation: Iterate through all 32 bits and check if each is set.

def hamming_weight_brute(n: int) -> int:
    count = 0
    for i in range(32):
        if (n >> i) & 1:
            count += 1
    return count

# Time Complexity: O(Set Bits) (Constraint)
# Space Complexity: O(1)
# Explanation: Brian Kernighan's Algorithm: Strip the lowest set bit using `N & (N-1)` until N reaches 0.

def hamming_weight_optimal(n: int) -> int:
    count = 0
    while n > 0:
        n = n & (n - 1)
        count += 1
    return count

