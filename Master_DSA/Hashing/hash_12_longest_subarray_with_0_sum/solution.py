# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Optimal: Maintain the prefix sum and a hash map storing the first occurrence index of each prefix sum. If sum is 0, length is `i+1`. If sum is in the map, length is `i - map[sum]`. Update max length.

def maxLen(n, arr):
    m = {}
    maxi, sum_val = 0, 0
    for i in range(n):
        sum_val += arr[i]
        if sum_val == 0: maxi = i + 1
        else:
            if sum_val in m:
                maxi = max(maxi, i - m[sum_val])
            else:
                m[sum_val] = i
    return maxi

