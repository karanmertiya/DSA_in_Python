# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Use a stack or two pointers. If using two pointers: `left = 0`, `right = N - 1`. If `knows(left, right)`, then `left` cannot be the celebrity, so `left++`. Else, `right` cannot be the celebrity, so `right--`. The remaining person `left` is a potential candidate. Verify by checking if `left` knows no one and everyone knows `left`.

def celebrity(M, n):
    left, right = 0, n - 1
    while left < right:
        if M[left][right] == 1: left += 1
        else: right -= 1
    for i in range(n):
        if i != left and (M[left][i] == 1 or M[i][left] == 0): return -1
    return left

