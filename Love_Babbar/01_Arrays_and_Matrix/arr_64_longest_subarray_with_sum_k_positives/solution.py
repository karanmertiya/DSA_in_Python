# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Since all elements are positive, use two pointers (sliding window). Expand `right` and add to sum. If sum > K, shrink `left` and subtract from sum. If sum == K, update max length.

def lenOfLongSubarr(A, N, K):
    left, sum_val, max_len = 0, 0, 0
    for right in range(N):
        sum_val += A[right]
        while sum_val > K and left <= right:
            sum_val -= A[left]
            left += 1
        if sum_val == K:
            max_len = max(max_len, right - left + 1)
    return max_len

