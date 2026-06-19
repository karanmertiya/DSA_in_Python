# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Keep track of the prefix sum. Store the first occurrence of each prefix sum in a hash map. If `prefix_sum - K` exists in the hash map, calculate the length of the subarray and update the maximum length.

def lenOfLongSubarr(A: List[int], N: int, K: int) -> int:
    preSum = {}
    currSum = 0
    maxLen = 0
    for i in range(N):
        currSum += A[i]
        if currSum == K:
            maxLen = max(maxLen, i + 1)
        if currSum - K in preSum:
            maxLen = max(maxLen, i - preSum[currSum - K])
        if currSum not in preSum:
            preSum[currSum] = i
    return maxLen

