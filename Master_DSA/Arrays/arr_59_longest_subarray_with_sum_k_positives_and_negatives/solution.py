# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Use a hash map to store the first occurrence of each prefix sum. While iterating, if `current_sum == K`, max length is `i+1`. If `current_sum - K` exists in the hash map, update max length with `i - map[current_sum - K]`. If `current_sum` is not in map, insert it.

def lenOfLongSubarr(A, N, K):
    preSumMap = {}
    sum_val = 0
    max_len = 0
    for i in range(N):
        sum_val += A[i]
        if sum_val == K: max_len = max(max_len, i + 1)
        rem = sum_val - K
        if rem in preSumMap:
            max_len = max(max_len, i - preSumMap[rem])
        if sum_val not in preSumMap:
            preSumMap[sum_val] = i
    return max_len

