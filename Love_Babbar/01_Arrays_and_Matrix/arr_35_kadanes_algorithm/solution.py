# Time Complexity: O(N^2) or worse
# Space Complexity: O(N) or O(1)
# Explanation: Brute Force: Standard unoptimized approach. (TODO: Implement specific logic)

# TODO: Implement Brute Force
def maxSubarraySum(arr: List[int], n: int) -> int:
    maxSum = currSum = arr[0]
    for i in range(1, n):
        currSum = max(arr[i], currSum + arr[i])
        maxSum = max(maxSum, currSum)
    return maxSum

# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Optimal: Maintain `max_sum` and `curr_sum`. For each element, `curr_sum = max(element, curr_sum + element)`. `max_sum = max(max_sum, curr_sum)`.

def maxSubarraySum(arr: List[int], n: int) -> int:
    maxSum = currSum = arr[0]
    for i in range(1, n):
        currSum = max(arr[i], currSum + arr[i])
        maxSum = max(maxSum, currSum)
    return maxSum

