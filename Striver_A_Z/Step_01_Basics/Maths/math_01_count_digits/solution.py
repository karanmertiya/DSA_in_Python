# Time Complexity: O(log10 N)
# Space Complexity: O(1)
# Explanation: Convert to string and return length, or repeatedly divide by 10. O(log10 N) time.

def evenlyDivides(N: int) -> int:
    if N == 0: return 1
    count, temp = 0, N
    while temp > 0:
        digit = temp % 10
        if digit != 0 and N % digit == 0: count += 1
        temp //= 10
    return count

