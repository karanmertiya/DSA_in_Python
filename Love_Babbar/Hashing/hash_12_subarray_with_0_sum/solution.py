# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Maintain the prefix sum. If the current prefix sum is 0, or if it has been seen before (stored in a Hash Set), then a subarray with 0 sum exists.

def subArrayExists(arr, n):
    s = set()
    sum_val = 0
    for num in arr:
        sum_val += num
        if sum_val == 0 or sum_val in s: return True
        s.add(sum_val)
    return False

