# Time Complexity: O(N^2) or worse
# Space Complexity: O(N) or O(1)
# Explanation: Brute Force: Standard unoptimized approach. (TODO: Implement specific logic)

# TODO: Implement Brute Force
def subArrayExists(arr, n):
    sumSet = set()
    curr_sum = 0
    for num in arr:
        curr_sum += num
        if curr_sum == 0 or curr_sum in sumSet:
            return True
        sumSet.add(curr_sum)
    return False

# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Optimal: Iterate through the array and calculate the prefix sum. If the prefix sum is 0 or it already exists in a hash set, it means a subarray with sum 0 exists.

def subArrayExists(arr, n):
    sumSet = set()
    curr_sum = 0
    for num in arr:
        curr_sum += num
        if curr_sum == 0 or curr_sum in sumSet:
            return True
        sumSet.add(curr_sum)
    return False

