# Time Complexity: O(log10(X))
# Space Complexity: O(1)
# Explanation: Use a while loop to extract the last digit using `x % 10` and add it to the reversed number `ans = ans * 10 + digit`. Check for overflow before multiplying by 10.

def reverse(x):
    sign = [1, -1][x < 0]
    ans = int(str(abs(x))[::-1]) * sign
    if not -2**31 <= ans <= 2**31 - 1: return 0
    return ans

