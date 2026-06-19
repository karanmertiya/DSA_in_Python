# Time Complexity: O(log(A^B))
# Space Complexity: O(1)
# Explanation: Take the XOR of A and B (`A ^ B`). The number of set bits in the result is the number of bits that need to be flipped. Use Brian Kernighan's algorithm to count.

def countBitsFlip(a: int, b: int) -> int:
    n = a ^ b
    count = 0
    while n > 0:
        n &= (n - 1)
        count += 1
    return count

