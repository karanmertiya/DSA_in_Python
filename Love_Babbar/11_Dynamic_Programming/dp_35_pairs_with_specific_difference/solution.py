# Time Complexity: O(N log N)
# Space Complexity: O(1)
# Explanation: Sort array. Iterate from end. If `arr[i] - arr[i-1] < K`, we pair them, add sum to answer, and `i -= 2`. Else, `i -= 1`. Greedy approach works because pairing larger numbers gives a larger sum.

def maxSumPairWithDifferenceLessThanK(arr: List[int], N: int, K: int) -> int:
    arr.sort()
    ans = 0
    i = N - 1
    while i > 0:
        if arr[i] - arr[i-1] < K:
            ans += arr[i] + arr[i-1]
            i -= 2
        else:
            i -= 1
    return ans

