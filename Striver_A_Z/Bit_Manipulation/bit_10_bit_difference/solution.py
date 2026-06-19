# Time Complexity: O(1) or O(set bits)
# Space Complexity: O(1)
# Explanation: The XOR of A and B will have set bits only at positions where A and B differ. Thus, we just need to count the set bits in `A ^ B`.

def countBitsFlip(a, b):
    n = a ^ b
    count = 0
    while n:
        count += 1
        n &= (n - 1)
    return count

