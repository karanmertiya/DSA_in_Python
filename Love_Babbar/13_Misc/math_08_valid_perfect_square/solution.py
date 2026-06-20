# Time Complexity: O(log N)
# Space Complexity: O(1)
# Explanation: Use binary search from `1` to `num/2` or up to `46340` (sqrt of INT_MAX). If `mid * mid == num`, return true. Else if `mid * mid < num`, `low = mid + 1`. Else `high = mid - 1`.

def isPerfectSquare(num: int) -> bool:
    if num == 1: return True
    low, high = 1, num // 2
    while low <= high:
        mid = (low + high) // 2
        sq = mid * mid
        if sq == num: return True
        elif sq < num: low = mid + 1
        else: high = mid - 1
    return False

