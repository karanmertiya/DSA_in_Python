# Time Complexity: O(m * log(m*n))
# Space Complexity: O(1)
# Explanation: Binary search on range `[1, m*n]`. For a value `mid`, the number of elements `<= mid` in row `i` is `min(mid / i, n)`. Sum this for all rows to get total count. If count >= k, search left. Else search right.

def findKthNumber(m: int, n: int, k: int) -> int:
    low, high = 1, m * n
    while low < high:
        mid = low + (high - low) // 2
        count = sum(min(mid // i, n) for i in range(1, m + 1))
        if count >= k:
            high = mid
        else:
            low = mid + 1
    return low

