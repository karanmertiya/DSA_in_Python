# Time Complexity: O(N^2) or worse
# Space Complexity: O(N) or O(1)
# Explanation: Brute Force: Standard unoptimized approach. (TODO: Implement specific logic)

# TODO: Implement Brute Force
def pairWithMaxSum(arr, N):
    maxi = 0
    for i in range(N - 1):
        maxi = max(maxi, arr[i] + arr[i+1])
    return maxi

# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Optimal: The maximum sum of two smallest elements in any subarray will always be the maximum sum of adjacent elements. So, just iterate and find the max of `arr[i] + arr[i+1]`.

def pairWithMaxSum(arr, N):
    maxi = 0
    for i in range(N - 1):
        maxi = max(maxi, arr[i] + arr[i+1])
    return maxi

