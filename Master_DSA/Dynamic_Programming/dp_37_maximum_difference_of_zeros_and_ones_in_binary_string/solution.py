# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Convert '0' to 1 and '1' to -1. Find the maximum subarray sum using Kadane's algorithm. If max sum is negative, it means string has all 1s, return -1.

def maxSubstring(S: str) -> int:
    mx, curr = float('-inf'), 0
    for c in S:
        val = 1 if c == '0' else -1
        curr = max(val, curr + val)
        mx = max(mx, curr)
    return mx

