# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Repeated addition. Add `n` to a sum `n` times.

def square_brute(n: int) -> int:
    return sum(abs(n) for _ in range(abs(n)))

# Time Complexity: O(log N)
# Space Complexity: O(log N) (Call stack)
# Explanation: If `n` is even, `n = 2*x`, then `n^2 = 4*x^2 = (x^2) << 2`. If `n` is odd, `n = 2*x + 1`, then `n^2 = 4*x^2 + 4*x + 1 = ((x^2 + x) << 2) + 1`.

def square(n: int) -> int:
    if n == 0: return 0
    n = abs(n)
    x = n >> 1
    if n & 1:
        return (square(x) << 2) + (x << 2) + 1
    else:
        return square(x) << 2

