# Time Complexity: O(1) 32 bits
# Space Complexity: O(1)
# Explanation: Iterate through 32 bits. If bit in `c` is 1, at least one of `a` or `b` needs to be 1. If both are 0, flip one (1 flip). If bit in `c` is 0, both `a` and `b` must be 0. Flips needed = bit of `a` + bit of `b`.

def minFlips(a: int, b: int, c: int) -> int:
    flips = 0
    for i in range(32):
        bit_a = (a >> i) & 1
        bit_b = (b >> i) & 1
        bit_c = (c >> i) & 1
        if bit_c == 1:
            if bit_a == 0 and bit_b == 0: flips += 1
        else:
            flips += bit_a + bit_b
    return flips

