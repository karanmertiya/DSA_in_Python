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

