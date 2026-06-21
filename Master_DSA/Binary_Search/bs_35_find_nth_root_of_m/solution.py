# Time Complexity: O(N * log M)
# Space Complexity: O(1)
# Explanation: Optimal: Search space is `[1, m]`. Check `mid^n`. Since `mid^n` can overflow, use a custom power function that returns 1 if `mid^n == m`, 0 if `< m`, and 2 if `> m`. Adjust `low` and `high` accordingly.

def NthRoot(n, m):
    def func(mid, n, m):
        ans = 1
        for _ in range(n):
            ans *= mid
            if ans > m: return 2
        if ans == m: return 1
        return 0
    low, high = 1, m
    while low <= high:
        mid = (low + high) // 2
        midN = func(mid, n, m)
        if midN == 1: return mid
        elif midN == 0: low = mid + 1
        else: high = mid - 1
    return -1

