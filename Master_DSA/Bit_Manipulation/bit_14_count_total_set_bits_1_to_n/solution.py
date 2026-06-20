# Time Complexity: O(N log N)
# Space Complexity: O(1)
# Explanation: Loop from 1 to N and count set bits using Brian Kernighan's.

def countSetBitsBrute(N: int) -> int:
    total = 0
    for i in range(1, N+1):
        while i:
            i &= (i - 1)
            total += 1
    return total

# Time Complexity: O(log N)
# Space Complexity: O(log N)
# Explanation: Find largest power of 2 <= n (`x`). Bits up to `2^x - 1` are `x * 2^(x-1)`. The MSB of remaining numbers is `n - 2^x + 1`. Then recursively call for `n - 2^x`.

def countSetBits(n: int) -> int:
    if n <= 0: return 0
    x = 0
    while (1 << x) <= n:
        x += 1
    x -= 1
    bitsUpTo2x = x * (1 << (x - 1))
    msbOfRest = n - (1 << x) + 1
    rest = n - (1 << x)
    return bitsUpTo2x + msbOfRest + countSetBits(rest)

