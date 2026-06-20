# Time Complexity: O(log10 x)
# Space Complexity: O(1)
# Explanation: Strict 32-bit environment (LeetCode standard): Extract digit, check for overflow against INT_MAX/10 and INT_MIN/10 *before* multiplying ans by 10.

def reverse(x: int) -> int:
    sign = [1, -1][x < 0]
    ans = int(str(abs(x))[::-1])
    return sign * ans if ans <= 2**31 - 1 else 0

# Time Complexity: O(log10 x)
# Space Complexity: O(1)
# Explanation: Relaxed 64-bit environment: Store answer in a 64-bit integer (`long long`). At the end, check if it exceeds 32-bit bounds and return 0 if it does.

def reverse(x: int) -> int:
    # Python handles arbitrarily large integers natively.
    # So we simply reverse and check against 32-bit bounds.
    ans = int(str(abs(x))[::-1])
    if x < 0: ans = -ans
    if ans > 2**31 - 1 or ans < -2**31: return 0
    return ans

