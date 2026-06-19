# Time Complexity: O(log_5(N) * log(5*N))
# Space Complexity: O(1)
# Explanation: Trailing zeros depend on number of 5s. Find count of 5s in `mid!`. Use binary search on the number. Low = 0, high = 5*N. If `check(mid) >= n`, `ans = mid` and `high = mid - 1`. Else `low = mid + 1`.

def findNum(n: int) -> int:
    if n == 1: return 5
    def check(p):
        count, f = 0, 5
        while f <= p:
            count += p // f
            f *= 5
        return count >= n
    low, high = 0, 5 * n
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if check(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

