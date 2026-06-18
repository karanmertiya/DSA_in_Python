# Time Complexity: O(Set Bits) (Constraint)
# Space Complexity: O(1)
# Explanation: XOR `start` and `goal` to isolate differing bits, then count the set bits in the result.

def min_bit_flips(start: int, goal: int) -> int:
    xor_res = start ^ goal
    count = 0
    while xor_res > 0:
        xor_res &= (xor_res - 1)
        count += 1
    return count

