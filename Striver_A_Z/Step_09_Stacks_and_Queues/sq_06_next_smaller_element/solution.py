# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Iterate from right to left. Use a monotonic stack. Pop elements from the stack that are greater than or equal to the current element. The top of the stack is the next smaller element. Push the current element to the stack.

def help_classmate(arr, n):
    ans = [-1] * n
    s = []
    for i in range(n - 1, -1, -1):
        while s and s[-1] >= arr[i]: s.pop()
        if s: ans[i] = s[-1]
        s.append(arr[i])
    return ans

